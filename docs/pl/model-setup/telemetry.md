---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telemetria

![Wykryte czujniki](../assets/model-telemetry-discovered-new-sensors.png)

Telemetria przekazuje informacje z modelu z powrotem do pilota — jakość
łącza (RSSI, VFR), napięcia i prądy oraz wszystko inne, co raportuje
podłączony czujnik (pozycja GPS, wysokość itd.). Obsługiwanych jest do 100
czujników na model; wykrywanie i konfiguracja odbywają się tutaj, ale
telemetria jest faktycznie *wyświetlana* jako [widgety ekranów
wyświetlania](../displays/index.md), konfigurowane osobno w Konfiguracji
ekranów.

## Jak działa telemetria FrSky {: #how-frsky-telemetry-works }

Czujniki FrSky nie wymagają koncentratora: **Smart Port (S.Port)** to
3-przewodowa magistrala (Gnd, V+, Sygnał), łączona szeregowo w dowolnej
kolejności do złącza S.Port w odbiornikach serii X/S i nowszych, pracująca
w trybie half-duplex z prędkością 57 600 bps (F.Port i FBUS są szybsze).

- **Physical ID** — magistralę współdzieli do 28 węzłów (łącznie z
  odbiornikiem), a każdy potrzebuje unikalnego Physical ID (00–1B hex).
  Urządzenia FrSky mają rozsądne wartości domyślne (np. Vario = 00,
  FLVSS = 01, Current = 02, GPS = 03) — jeśli podłączysz dwa takie same
  urządzenia, Physical ID drugiego trzeba zmienić w [Konfiguracji
  urządzeń](../system-setup/devices.md).
- **Application ID** — niezależny od Physical ID: jeden czujnik może
  raportować wiele wartości, każdą z własnym Application ID. Vario ma
  jeden Physical ID, ale dwa Application ID (wysokość, prędkość pionowa);
  FLVSS ma jeden Physical ID i jeden Application ID (napięcie).
  Monitorowanie dwóch pakietów 6S dwoma czujnikami FLVSS oznacza zmianę
  **obu** identyfikatorów w drugim z nich — Physical ID dla wyłącznej
  komunikacji na magistrali, a Application ID po to, by odbiornik odróżnił
  Lipo 1 od Lipo 2 (np. `0300` → `0301`). Zwykle zmienia się czwartą cyfrę
  szesnastkową, 0–F.

  !!! note
      Czujniki współdzielące Application ID przy różnych Physical ID są
      dopuszczalne wyłącznie przy wyłączonym [wykrywaniu konfliktów
      czujników](../system-setup/alerts.md) — to konfiguracja
      specjalnego przeznaczenia, a nie przypadek domyślny.

Każda odebrana wartość jest śledzona jako osobny czujnik: wartość,
Physical/Application ID, edytowalna nazwa, jednostka, precyzja dziesiętna,
opcjonalna flaga zapisu logów na SD card oraz własne bieżące min/max. Po
skonfigurowaniu czujniki są wykrywane automatycznie przy każdym włączeniu,
ale za pierwszym razem trzeba je wykryć **ręcznie**. Po wykryciu czujnik
może być odczytywany głosowo, podawany do [czujników
obliczanych](#calculated-sensors), używany w [przełącznikach
logicznych](logical-switches.md), [zmiennych](variables.md) lub
[miksach](mixes.md), pokazywany na własnym ekranie telemetrii albo
odczytywany bezpośrednio z tej strony konfiguracji, bez tworzenia
jakiegokolwiek ekranu.

**FBUS** (dawniej F.Port2) idzie o krok dalej, łącząc sterowanie SBUS i
telemetrię S.Port na jednej linii przy 460 800 bps (wobec 115 200 dla
F.Port i 57 600 dla S.Port — te trzy prędkości transmisji są wzajemnie
niekompatybilne) i pozwala jednemu hostowi komunikować się z kilkoma
akcesoriami podrzędnymi na tej jednej linii, przy czym wszystkie można
konfigurować bezprzewodowo z nadajnika.

### Telemetria z wielu odbiorników (ACCESS Trio)

Przy maksymalnie trzech odbiornikach zarejestrowanych w [Systemie
RF](rf-system.md#registering-and-binding-a-receiver-access) każdy
zbindowany odbiornik można konfigurować indywidualnie (piny portów itd.)
poprzez RX1/RX2/RX3. Zwykle na jedno łącze RF przypada jedna przychodząca
ścieżka telemetrii — wyjątkiem są systemy Tandem/TD, które prowadzą 2,4 GHz
i 900 MHz jako dwie ścieżki w jednym module. Aktywne źródło telemetrii może
zmieniać się w trakcie lotu w zależności od warunków RF; czujnik **RX**
raportuje w czasie rzeczywistym, który odbiornik aktualnie wysyła
telemetrię (i zapisuje to w logach).

Typowa konfiguracja: połącz szeregowo magistralę czujników S.Port przez
wszystkie trzy odbiorniki, zapewniając wspólne zasilanie, a następnie
zarejestruj/zbinduj każdy odbiornik i wykryj czujniki jak zwykle — źródło
telemetrii przełącza się automatycznie wraz ze zmianą aktywnego RX, a dane
*zewnętrznych* czujników S.Port podążają za nim w sposób przezroczysty.
(Wewnętrzne czujniki odbiornika — RSSI, VFR, RxBatt, ADC2, sam RX — nie są
w ten sposób powiązane; zawsze są raportowane dla tego odbiornika, który
aktualnie jest źródłem. Jednoczesna telemetria ze wszystkich trzech naraz
jest planowana, ale jeszcze niedostępna.)

## Czujniki jakości łącza

- **RSSI** (wskaźnik siły sygnału odbiornika) — jak silna jest transmisja
  nadajnika w miejscu odbiornika. Domyślne alarmy: **ACCESS**/**TD**/
  **TW** 35 (niski) / 32 (krytyczny), utrata kontroli około 28; **ACCST**
  45 / 42, utrata kontroli około 38. Komunikat „Telemetry Lost" pojawia
  się, gdy łącze zanika całkowicie — od tego momentu **nie mogą zabrzmieć
  żadne kolejne alarmy**, ponieważ nadajnik nie ma już telemetrii do
  oceny; potraktuj to jako sygnał do natychmiastowego zawrócenia. (Przy
  odległości poniżej ~1 m odbiornik może zostać przesterowany i generować
  fałszywe pętle alarmów Lost/Recovered — to nie jest rzeczywista
  usterka.) RSSI dobrze przybliża efektywny zasięg, ale VFR jest
  pewniejszym wskaźnikiem jakości łącza.

  ![Czujnik RSSI](../assets/model-telemetry-edit-rssi-sensor.png)

  Odbiorniki TD raportują RSSI dla każdego pasma (2.4G, 900M); odbiorniki
  TW również raportują po jednym na pasmo (2.4FSK, 2.4LoRa, 900M) —
  włącz **Individual RSSI alert per band**, aby otrzymywać osobne
  ostrzeżenia głosowe dla każdego z nich zamiast jednego łącznego alarmu:

  ![Indywidualny alarm RSSI](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — liczba poprawnych pakietów na 100
  odebranych; następca (po ACCESS 2.1) wcześniejszego wliczania wskaźnika
  utraconych ramek do RSSI. Domyślne **Low value warning** to 50%.

  ![Czujnik VFR](../assets/model-telemetry-edit-vfr-sensor.png)

  Odbiorniki TD/TW raportują dwa strumienie VFR (po jednym na pasmo);
  **Rx VFR** (w odbiornikach TD/TW/AP/AP Plus) zlicza natomiast każdą
  poprawną ramkę niezależnie od pasma, na którym dotarła — to wartość,
  którą warto obserwować, jeśli śledzisz tylko jeden wskaźnik VFR.

- **RxBatt** — napięcie akumulatora odbiornika.
- **ADC2** — drugie analogowe wejście napięciowe, w odbiornikach, które je
  obsługują.
- **SWR** — SWR anteny, przy korzystaniu z anteny zewnętrznej.
- Czujniki orientacji/ruchu, tam gdzie są obsługiwane: **R.Angle**,
  **P.Angle**, **AccX/Y/Z**.

Każdy czujnik liczbowy otrzymuje też automatycznie czujniki min/max
`<name>-`/`<name>+`, mimo że nie są one pokazywane na głównej liście
czujników.

## Wykrywanie czujników {: #discovering-sensors }

![Wykrywanie nowych czujników: włączone](../assets/model-telemetry-discover-new-sensors-on.png)

Gdy wszystko jest zbindowane i zasilone, włącz **Discover new sensors** —
migająca kropka (lub czerwona wartość, jeśli nie ma jeszcze danych)
oznacza każdy znaleziony czujnik, a ekran zapełnia się automatycznie.
Trzeba to powtórzyć **dla każdego modelu**, a także za każdym razem po
dodaniu nowego czujnika.

![Wykrywanie nowych czujników: wyłączone](../assets/model-telemetry-discover-new-sensors-off.png)

- Po zakończeniu przełącz wykrywanie z powrotem na **Off**.
- **Delete all** usuwa wszystkie czujniki, aby zacząć od nowa.

  ![Czujniki usunięte](../assets/model-telemetry-sensors-deleted.png)

- **Competition mode** ogranicza telemetrię wyłącznie do RSSI i RxBatt —
  na potrzeby zawodów dopuszczających jedynie czujniki stanu łącza.
  Ponowne wyłączenie tego trybu wymaga przełączenia zasilania, zanim
  czujniki będzie można wykryć na nowo.

  ![Potwierdzenie trybu zawodów](../assets/model-telemetry-comp-only-confirm.png)

- Tryb telemetrii **Bluetooth** paruje się z aplikacją telefoniczną FrSky
  FreeLink, która może wyświetlać telemetrię na żywo, a także konfigurować
  urządzenia FrSky, takie jak odbiorniki ze stabilizacją.

  ![Telemetria Bluetooth](../assets/model-telemetry-bt-option.png)

## Edycja czujnika {: #editing-a-sensor }

![Wybór opcji edycji](../assets/model-telemetry-edit-option-select.png)

Dotknij czujnika, aby wybrać **Edit**, **Move**, **Reset** lub **Delete**.
Typowe pola: **Value** (tylko do odczytu), **ID** (Physical +
Application ID oraz odbiornik wysyłający), **Name**, **Unit**,
**Decimals**, **Range** (stałe granice skalowania — istotne głównie wtedy,
gdy czujnik jest używany jako źródło kanału), **Write logs**, **Reset**
(źródło zerujące ten czujnik) oraz **Sensor lost warning delay** (całkowite
wyłączenie lub 1–30 s, domyślnie 10 s, aby odfiltrować krótkie zaniki —
miej świadomość ryzyka ustawienia zbyt dużej wartości; komunikat „sensor
lost" odtwarzany jest tylko raz, nawet jeśli jednocześnie zaniknie wiele
czujników; domyślnie wyłączone dla czujników wewnętrznych odbiornika,
ponieważ te rzadko zanikają).

Niektóre czujniki dodają własne pola:

- **ADC2** — **Ratio** i **Offset**, do korekty skalowania.

  ![Edycja czujnika ADC2](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — progi **Critical value** i **Low value warning**.
- **VFR** — **Low value warning** (domyślnie 50%).
- **VSpeed** (prędkość pionowa z wariometru) — **Range** do ±100 m/s
  (domyślnie ±10 m/s). Samo zachowanie dźwięku wariometru znajduje się
  teraz w [funkcji specjalnej Play Vario](special-functions.md), a nie
  tutaj.

  ![Edycja czujnika VSpeed](../assets/model-telemetry-edit-vspeed-sensor.png)

## Czujniki DIY / innych producentów

![Utworzenie czujnika DIY](../assets/model-telemetry-diy-sensor-select.png)

**Create DIY Sensor** dodaje ręcznie czujnik spoza oferty FrSky: **Auto
detect** (w miarę możliwości automatycznie wypełnia Physical ID,
Application ID i moduł) albo ustawienie ich ręcznie, a do tego **Protocol
decimals/unit** (precyzja danych przychodzących, 0–3 miejsca dziesiętne,
oraz ich natywna jednostka) i **Display decimals/unit** (niezależne od
ustawień protokołu), obok tych samych pól **Range**/**Ratio**/**Offset**/
**Write logs**/**Reset**/**Sensor lost warning delay** co w każdym innym
czujniku.

![Automatyczne wykrywanie czujnika DIY](../assets/model-telemetry-diy-sensor-auto-detect.png)

## Czujniki obliczane {: #calculated-sensors }

![Utworzenie czujnika obliczanego](../assets/model-telemetry-calculated-sensor-select.png)

Tworzenie nowego czujnika na podstawie jednego lub kilku istniejących:

- **Consumption** — zużyta energia, całkowana z czujnika prądu (np. seria
  FAS). Jednostka mAh/Ah, zakres do 1000 Ah.

  ![Czujnik zużycia](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Distance** — na podstawie źródła GPS (plus źródła wysokości, dla
  odległości 3D). Jednostki cm/m/km/ft, do 20 km.

  ![Czujnik odległości](../assets/model-telemetry-calculated-sensor-distance.png)

- **Trip** — zsumowana odległość między kolejnymi pozycjami GPS. Te same
  jednostki, do 1000 km.

  ![Czujnik trasy](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — łączy kaskadowo dwa lub więcej czujników napięcia Lipo,
  aby monitorować pakiety większe niż 6S (do 67,2 V/8S). Wybieraj kolejne
  czujniki ogniw od najniższego do najwyższego; w każdym dodatkowym
  czujniku Lipo trzeba najpierw zmienić **zarówno** Physical, **jak i**
  Application ID w [Konfiguracji
  urządzeń](../system-setup/devices.md) (pomaga w tym tamtejsze narzędzie
  Lipo Voltage), wykryć je pojedynczo i zmienić im nazwy, aby były
  rozróżnialne.

  ![Czujnik Multi Lipo](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Percent** — przeskalowuje czujnik do zakresu 0–100%, z opcją
  **Invert** (np. aby pokazywać wartość *pozostałą* zamiast zużytej).

  ![Czujnik procentowy](../assets/model-telemetry-calculated-sensor-percent.png)

- **Power** — moc w watach z pary źródeł **Current** i **Voltage**, do
  1 000 000 W.

  ![Czujnik mocy](../assets/model-telemetry-calculated-sensor-power.png)

- **Custom** — dowolna formuła łączona z jednego lub wielu źródeł.

Każdy czujnik obliczany ma też opcję **Persistent** (wartość przetrwa
wyłączenie zasilania lub zmianę modelu i zostanie wczytana przy kolejnym
użyciu) oraz przycisk **Reset** bezpośrednio na ekranie edycji.

### Czujniki własne

![Czujnik własny](../assets/model-telemetry-edit-custom-sensor.png)

Zaczyna się od jednego źródła, a następnie przycisk **Add** dołącza kolejne
operacje: **Add(+)**, **Minus(-)**, **Multiply(×)**, **Divide(/)**,
**Min**, **Max**, **Sqrt**. Jednostki wybiera się z długiej listy
obejmującej napięcie, prąd, pojemność, moc, odległość, prędkość, czas,
temperaturę, procenty, kąty, ciśnienie i więcej; zakres od −1 000 000 do
1 000 000, 0–4 miejsca dziesiętne.

![Dodanie linii obliczeń](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "Moc szczytowa"
    Pomnóż czujnik napięcia (`VFAS`) przez czujnik prądu (`Current`), a
    następnie dodaj krok **Max** odwołujący się do bieżącej wartości
    samego czujnika (`MaxPower`), aby śledzić najwyższy zanotowany odczyt
    — 288 W w tym przykładowym locie:

    ![Przykład MaxPower](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "Działanie arytmetyczne na stałej"
    Źródło ustawione na `RSSI 2.4G` (odczyt 64 dB), a następnie akcja
    **Subtract**, której własne źródło zostało przytrzymane dłużej i
    poddane operacji **Convert to value**, co zamienia je w edytowalną
    stałą (20) zamiast żywego źródła — wynikiem jest stałe 44 dB
    (64 − 20):

    ![Przykład odejmowania](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![Konwersja na wartość](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "Wewnętrzna wartość źródła"
    Każde [źródło](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    ma wewnętrzny zakres całkowitoliczbowy ±1024, odpowiadający
    wyświetlanemu zakresowi ±100% — widać to bezpośrednio, kierując
    czujnik własny na przykład na Gaz: pełny gaz odczytywany jest
    wewnętrznie jako **+1024**, a pełny wstecz jako **−1024**.

    ![Wartość wewnętrzna przy maksimum](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![Wartość wewnętrzna przy minimum](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
