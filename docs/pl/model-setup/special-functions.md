---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Funkcje specjalne

![Menu funkcji specjalnych](../assets/model-sf-menu.png)

Funkcje specjalne wyzwalają określone działanie — odtworzenie dźwięku,
wykonanie zrzutu ekranu, zapis logów, sygnalizację wibracyjną i inne — gdy
warunek staje się prawdziwy. Obsługiwanych jest do 100 funkcji; domyślnie nie
ma żadnej. Nową dodaje się przyciskiem **+**; dotknięcie istniejącej pozwala na
**Edycję**/**Przeniesienie**/**Kopiuj-wklej**/**Klonowanie**/**Usunięcie**.

![Dodawanie funkcji specjalnej](../assets/model-sf-add.png)
![Przenoszenie](../assets/model-sf-move.png)

## Pola wspólne dla wszystkich działań

- **State** — włącza/wyłącza funkcję bez jej usuwania.
- **Active condition** — **Always on** albo warunek zależny od położenia
  przełącznika/przełącznika funkcyjnego/przełącznika logicznego/trymu lub od
  trybu lotu. Przytrzymaj `ENT` na przełączniku i zaznacz **Negative**, aby
  odwrócić działanie (np. `SG-up` zmieni się w `!SG-up`, czyli warunek aktywny
  zawsze, gdy SG *nie* jest w górze).
- **Global** — dodaje tę funkcję do **każdego** modelu, istniejącego i
  przyszłego. Jeżeli model ma już identycznie skonfigurowaną funkcję lokalną,
  opcja Global doda ją jako dodatkowy wpis; ponowne wyłączenie Global usuwa
  funkcję ze wszystkich modeli poza aktualnie wybranym. Funkcje globalne są
  przechowywane w pliku `radio.bin`, lokalne — w pliku modelu.

## Działania {: #actions }

**Reset** — resetuje **Flight data** (telemetrię i timery), **All timers**
lub **Whole telemetry**.

![Reset](../assets/model-sf-reset.png)

**Screenshot** — zapisuje zrzut ekranu w katalogu `screenshots/` na karcie
SD/pamięci eMMC.

![Zrzut ekranu](../assets/model-sf-screenshot.png)

**Set failsafe** — zapisuje bieżące położenia kanałów jako failsafe, poprzez
wewnętrzny lub zewnętrzny **Module** RF.

![Ustawianie failsafe](../assets/model-sf-set-failsafe.png)

**Play audio** — najbardziej rozbudowane działanie, obsługujące pełną
sekwencję:

![Odtwarzanie dźwięku](../assets/model-sf-play-audio.png)

- **Voice** — który z maksymalnie 3 skonfigurowanych głosów ma zostać użyty
  (zobacz [Ogólne](../system-setup/general.md#audio-settings)).
- **Repeat** — jednorazowe odtworzenie albo powtarzanie w zadanym odstępie
  (do 10 minut).
- **Skip on startup** — blokuje wyzwolenie tej funkcji podczas uruchamiania.
- **Sequence** — do 100 kroków, każdy jednego z typów:

  - **Play file** — odtwarza wybrany plik audio.

    ![Odtwarzanie pliku](../assets/model-sf-play-audio-add-play-file.png)

  - **Play value** — wypowiada wartość źródła: analogów, przełączników,
    przełączników logicznych, trymów, kanałów, żyroskopu, zegara systemowego,
    trenera, timerów lub telemetrii.

    ![Odtwarzanie wartości](../assets/model-sf-play-audio-add-play-value.png)

  - **Wait duration** — stała pauza, do 10 minut.
  - **Wait condition** — wstrzymuje sekwencję do czasu spełnienia warunku.

  ![Dodawanie wiersza sekwencji](../assets/model-sf-play-audio-add-line.png)
  ![Typ wiersza sekwencji](../assets/model-sf-play-audio-add-line-type.png)

  Na przykład: odtworzenie pliku `vfrlow.wav`, gdy przełącznik logiczny
  `VFRlow` stanie się aktywny, a następnie wypowiedzenie zarejestrowanej
  minimalnej wartości VFR —

  ![Odtwarzanie wartości po pliku](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — albo wstrzymanie sekwencji do momentu przestawienia przełącznika SH w dół:

  ![Sekwencja z warunkiem oczekiwania](../assets/model-sf-play-audio-add-sequence.png)

  Dotknij dowolnego wiersza sekwencji, aby go edytować, dodać nowy, zmienić
  kolejność lub usunąć:

  ![Zarządzanie sekwencją](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptic** — sygnalizacja wibracyjna:

![Wibracje](../assets/model-sf-haptic.png)

- **Pattern** — pojedyncza, podwójna, potrójna, pięciokrotna lub bardzo krótka.

  ![Wzór wibracji](../assets/model-sf-haptic-pattern.png)

- **Strength** — 1–10 (domyślnie 5).
- **Repeat** — jednorazowo albo w zadanym odstępie.
- **Select haptic motors** — w nadajnikach z silniczkami wibracyjnymi w
  agregatach (X20 Pro AW, X20RS lub X20 Pro/X20R doposażony w agregaty MC20R —
  zobacz
  [Sprzęt](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Default** (wewnętrzny silniczek), **All motors**, **Left stick** lub
  **Right stick**.

  ![Wibracje w X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Write Logs** — zapisuje logi `.csv` w katalogu `Logs/` na karcie SD/pamięci
eMMC, ze znacznikami czasu z zegara RTC (kluczowe dla późniejszego rozróżnienia
poszczególnych sesji lotnych):

![Zapis logów](../assets/model-sf-write-logs.png)

- **Write Interval** — 100–500 ms.
- **Sticks/Pots/Sliders**, **Switches**, **Logic Switches**, **Channels**
  — niezależnie włączane kategorie zapisywanych danych.

  **Przeglądanie logów**: otwórz plik logu z katalogu `/Logs` w menedżerze
  plików. Wybierz, które kanały mają zostać wykreślone (RSSI jest wybrany
  domyślnie); przesuwaj wykres enkoderem obrotowym lub przesunięciem palca, a
  powiększaj obracając enkoder z wciśniętym `PAGE`. `DISP` przenosi fokus na
  pierwszy przycisk w prawej kolumnie.

**Play Text** (tylko X20 Pro) — synteza mowy w nadajniku zamiast wcześniej
nagranego pliku:

![Odtwarzanie tekstu](../assets/model-sf-x20pro-play-text.png)

- **Text** — tekst do wypowiedzenia. WIELKIE LITERY są literowane pojedynczo
  (np. „OFF” → „O-F-F”); małe litery są wypowiadane jako słowo („off”).
- **Repeat**, **Skip on startup** — jak wyżej.

**Go to screen** — przełącza wyświetlacz na wybrany ekran, np. przechodzi do
zapisu danych lotu z odbiornika po naciśnięciu przycisku:

![Przejście do ekranu](../assets/model-sf-go-to-screen.png)
![Opcje ekranu](../assets/model-sf-go-to-screen-options.png)

**Lock touchscreen** — blokuje ekran dotykowy przed przypadkowym dotknięciem
(dostępne również bezpośrednio poprzez przytrzymanie razem `ENT` + `PAGE`
przez 1 s na ekranie głównym):

![Blokada ekranu dotykowego](../assets/model-sf-lock-touchscreen.png)

**Load model** — po wyzwoleniu ładuje wskazany **Model**, opcjonalnie z
zapytaniem **Confirmation** przed faktycznym przełączeniem:

![Ładowanie modelu](../assets/model-sf-load-model.png)

**Play vario** — steruje sygnalizacją dźwiękową wariometru na podstawie
wybranego źródła (zwykle czujnika VSpeed wariometru FrSky, ale działa dowolny
czujnik o jednostce m/s):

![Sygnalizacja wariometru](../assets/model-sf-play-vario.png)
![Źródło wariometru: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Range** — zakres prędkości wznoszenia/opadania odwzorowany na wysokość
  tonu, domyślnie ±10 m/s (do ±100 m/s). Powyżej wartości **Center** wysokość
  tonu rośnie liniowo wraz z prędkością wznoszenia aż do maksymalnej wartości
  Range (wysokość tonu dla maksymalnej prędkości ustawia się w [Ogólne →
  Wariometr](../system-setup/general.md#vario)); przy opadaniu emitowany jest
  ciągły ton o wysokości malejącej w kierunku minimalnej wartości Range.
- **Center** — pasmo „zerowego wznoszenia”, domyślnie ±0,3 m/s (do ±2 m/s); w
  jego obrębie wysokość tonu jest stała (wysokość tonu dla zerowej prędkości
  również ustawia się w Ogólne → Wariometr). Przełączenie **Beep**→**Silent**
  całkowicie wycisza ton.

  ![Opcje zakresu/środka wariometru](../assets/model-sf-play-vario-options.png)
