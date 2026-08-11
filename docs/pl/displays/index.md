---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Wyświetlacze

![Ekran główny wyświetlacza](../assets/display-home.png)

Ekran główny to jeden lub więcej **ekranów wyświetlania**, z których każdy
zbudowany jest z **widgetów** umieszczanych i konfigurowanych samodzielnie.
Naciśnięcie `DISP` otwiera edytor bieżącego ekranu.

Dostępnych jest maksymalnie **osiem** ekranów, a każdy z nich powstaje na
bazie jednego z **trzynastu** układów (mieszczących do **dziewięciu** komórek
widgetów). Widgety mogą prezentować telemetrię, ale również dowolną z
siedemnastu innych kategorii informacji — stan modelu/nadajnika, timery,
kanały i wiele więcej. Skonfigurowane ekrany przywołuje się przesunięciem
palca po ekranie dotykowym lub przyciskiem `PAGE` w górę/w dół; górny i dolny
pasek pozostają widoczne na każdym ekranie z wyjątkiem układu pełnoekranowego.

## Dodawanie widgetu

![Typy widgetów](../assets/display-widget-types.png)

Każdy ekran to siatka; dotknięcie pustej komórki otwiera listę wyboru
widgetów. Widgety obejmują zarówno proste odczyty tekstowe i liczbowe, jak i
wskaźniki, wykresy oraz pełne dzienniki telemetrii. Po umieszczeniu widgetu
ponowne jego dotknięcie otwiera to samo menu opcji, które służy do zmiany
rozmiaru, przeniesienia lub usunięcia widgetu:

![Opcje konfiguracji widgetu](../assets/display-widget-config-options.png)

Wybranie ustawień własnych widgetu otwiera formularz konfiguracji właściwy dla
danego widgetu. Pole **źródła** — czyli wartości prezentowanej przez widget —
korzysta z tego samego
[selektora źródła](../getting-started/user-interface-and-navigation.md#choosing-a-source),
co w pozostałych miejscach systemu Ethos:

![Zmiana źródła widgetu](../assets/display-change-source.png)

## Typy widgetów {: #widget-types }

**Value** — pojedynczy odczyt liczbowy lub telemetryczny, prezentowany jako
tekst:

![Konfiguracja widgetu Value](../assets/display-widget-value-config.png)

Większość źródeł obsługuje także redukcję do bieżącej wartości **min** lub
**max** — po wybraniu źródła należy przytrzymać je dłużej i wybrać Min lub Max
— co jest przydatne np. do odczytu najgorszego RSSI w trakcie lotu:

![Widget Value z wartością min](../assets/display-widget-value-min.png)
![Widget Value z minimalnym RSSI](../assets/display-widget-value-min-rssi.png)

Po umieszczeniu widget wyświetla się na ekranie jako zwykły odczyt:

![Widget wartości telemetrycznej](../assets/display-widget-value-telemetry.png)

**Bitmap** — wyświetla statyczny obraz (np. zdjęcie modelu) lub zestaw
obrazów przełączanych w zależności od wartości źródła (np. ikonę akumulatora
zmieniającą się wraz z napięciem):

![Konfiguracja widgetu Bitmap](../assets/display-widget-bitmap-config.png)
![Typ widgetu Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — dedykowany wskaźnik akumulatora odczytujący dane z czujnika takiego
jak FLVSS: całkowite napięcie pakietu, liczbę ogniw oraz napięcie każdego
pojedynczego ogniwa. Spadek poniżej skonfigurowanego progu **Low voltage**
powoduje zmianę koloru wyświetlania na czerwony — w poniższym przykładzie próg
3,3 V zostaje przekroczony przez najniższe ogniwo:

![Konfiguracja widgetu LiPo](../assets/display-widget-lipo-config.png)
![Widget LiPo](../assets/display-widget-lipo.png)

**Channels** — do 8 kanałów wyjściowych w postaci wykresu słupkowego,
poziomego lub pionowego:

![Konfiguracja widgetu Channels](../assets/display-widget-channels-config.png)
![Widget Channels](../assets/display-widget-channels.png)

**Line Chart** — wykreśla wartość źródła w czasie, zerując się przy resecie
lotu (Flight Reset):

![Konfiguracja widgetu Line Chart](../assets/display-widget-line-chart-config.png)
![Widget Line Chart](../assets/display-widget-line-chart.png)

- **Source** — wartość, która jest wykreślana.
- **Pause condition** — źródło wstrzymujące/wznawiające rejestrację (albo po
  prostu dotknięcie działającego widgetu, jeśli nie ma wolnego źródła do tego
  celu).
- **Log period** — interwał próbkowania; 500 ms obejmuje około 6 minut przed
  rozpoczęciem przewijania, 1 s około 12 minut.
- **Inverted** — odwraca wykres w pionie.
- **Auto range** — automatycznie skaluje oś pionową do zakresu danych; po
  wyłączeniu stosowane są stałe wartości **Min**/**Max** (np. niezmienny
  zakres −100%…+100%).

Dotknięcie działającego wykresu przywołuje opcje **Pause/resume**, **Reset**
(wyczyszczenie i ponowny start), **Configure widget** lub przejście do
**Configure screens**:

![Opcje widgetu Line Chart](../assets/display-widget-line-chart-options.png)

**Text** — wyświetla zawartość pliku tekstowego w formacie Markdown
(odczytywanego z katalogu `documents/user/` — zobacz [Menedżer
plików](../system-setup/file-manager.md#top-level-folders)):

![Konfiguracja widgetu Text](../assets/display-widget-text-config.png)
![Widget Text](../assets/display-widget-text.png)

**Timer Log** — przewijalny dziennik poprzednich wartości wybranego timera,
zapisywany przy każdym jego zerowaniu (przydatny do śledzenia zużycia pakietów
lotnych w trakcie sesji); opcja **Reverse** umieszcza najnowszy wpis na górze:

![Konfiguracja widgetu Timer Log](../assets/display-widget-timer-logs-config.png)
![Widget Timer Log](../assets/display-widget-timer-log.png)

Dłuższe przytrzymanie wpisu (lub widgetu) udostępnia opcję **Clear logs**,
edycję/zerowanie powiązanego timera oraz przejście do konfiguracji
widgetu/ekranu:

![Menu wpisu Timer Log](../assets/display-widget-timer-log-menu.png)

**GPS Map** — wykreśla bieżącą pozycję GPS w postaci śladu, dla modeli
wyposażonych w czujnik GPS (więcej szczegółów na temat samego widgetu znajduje
się w wątku *FrSky - ETHOS Lua Script Programming* na rcgroups, post #8854):

![Konfiguracja widgetu GPS Map](../assets/display-widget-gps-map-config.png)

## Opcje na poziomie ekranu

Poza poszczególnymi widgetami każdy ekran ma własne ustawienia — rozmiar
siatki układu, tło oraz to, które ekrany są uwzględniane w cyklu przycisku
`PAGE`:

![Opcje konfiguracji ekranu](../assets/display-screen-config-options.png)

W pełni skonfigurowany ekran główny łączy kilka widgetów w jeden czytelny na
pierwszy rzut oka układ:

![Widok główny](../assets/display-main-view.png)

Zobacz [Dodatkowe wyświetlacze](additional-displays.md), aby dodać kolejne
ekrany poza domyślnym, oraz [Widgety własne](custom-widgets.md), aby poznać
widgety tworzone w Lua wykraczające poza zestaw wbudowany.
