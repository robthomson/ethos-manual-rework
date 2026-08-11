---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Interfejs użytkownika i nawigacja

Ethos można obsługiwać w całości za pomocą prawego **enkodera obrotowego**
(obracanie przesuwa podświetlenie, naciśnięcie działa jak `ENT`) oraz
klawisza `RTN` służącego do wyjścia z menu — ekran dotykowy, jeśli jest na
wyposażeniu, stanowi skrót do tych samych operacji, a nie odrębny sposób
pracy. `MDL`, `DISP` i `SYS` przenoszą bezpośrednio odpowiednio do
Konfiguracji modelu, Konfiguracji ekranów i Ustawień systemu (te same trzy
kafelki co na dolnym pasku); długie naciśnięcie `RTN` z dowolnego miejsca
powoduje powrót wprost do ekranu głównego.

## Menu resetowania

![Menu kontekstowe](../assets/resetmenu.png)

Długie naciśnięcie `ENT` na ekranie głównym otwiera menu resetowania:

- **Reset flight** — resetuje telemetrię, timery i przełączniki funkcyjne
  oraz ponownie uruchamia przedlotową
  [listę kontrolną](../model-setup/checklist.md).
- **Reset telemetry** — resetuje wyłącznie telemetrię.
- **Reset timers** — resetuje wyłącznie timery.
- **Lock touchscreen** — dostępne również przez jednoczesne naciśnięcie
  `ENT` + `PAGE` przez jedną sekundę na ekranie głównym lub jako wyzwalacz
  [funkcji specjalnej](../model-setup/special-functions.md).

## Elementy sterujące edycją

**Dodawanie elementów funkcyjnych** — timer, przełącznik logiczny, funkcję
specjalną, krzywą lub zmienną tworzy się, dotykając znaku **+** obok
nagłówków kolumn w odpowiednim menu. W nadajniku bez ekranu dotykowego
należy podświetlić istniejący element, nacisnąć `ENT` i wybrać z menu
polecenie **Add** — ta sama opcja jest dostępna także w nadajnikach
dotykowych.

### Klawiatura wirtualna

![Klawiatura tekstowa](../assets/keyboard-text-azerty.png)

Dotknięcie dowolnego pola tekstowego (lub naciśnięcie na nim `ENT`) otwiera
klawiaturę ekranową. Klawisz backspace kasuje znaki na lewo od kursora;
`PAGE` kasuje w prawo, a gdy kursor dotrze do końca tekstu, kontynuuje
kasowanie od lewej strony. Dotknięcie samego pola przenosi kursor w to
miejsce — alternatywnie można użyć `SYS`/`DISP`, aby przesuwać go w
lewo/prawo bez dotyku. Klawisz **?123**/**abc** przełącza klawiaturę
numeryczną (zawierającą również znaki specjalne):

![Klawiatura numeryczna](../assets/keyboard-text-numbers.png)

W **nadajniku bez ekranu dotykowego** naciśnięcie `ENT` na polu tekstowym
przechodzi bezpośrednio do trybu edycji: obracanie enkoderem przewija małe
litery, wielkie litery, cyfry, a następnie znaki specjalne, a naciśnięcie
`ENT` wstawia wybrany znak. `MDL` przełącza wielkość znaku znajdującego się
bezpośrednio na prawo od kursora (i każdy kolejno wpisywany znak zachowuje
tę wielkość aż do ponownego przełączenia). `PAGE` kasuje w prawo od
kursora; `SYS`/`DISP` przesuwają go w lewo/prawo.

## Elementy sterujące wartościami liczbowymi

![Wprowadzanie liczb](../assets/keyboard-numbers.png)

Dotknięcie pola liczbowego otwiera pasek sterowania w dolnej części ekranu:
**`<`**/**`>`** zmieniają wielkość kroku (przełączając kolejne rzędy
wielkości — np. 0.01/0.1/1.0/10.0), **`-`**/**`+`** (lub enkoder obrotowy)
zmieniają wartość o ten krok, a **More** otwiera dalsze opcje:

![Opcje wprowadzania liczb](../assets/keyboard-numbers-options.png)

- Przejście do wartości domyślnej pola
- Ustawienie wartości minimalnej / maksymalnej
- Zastąpienie pola krokowego **suwakiem**

![Wprowadzanie suwakiem](../assets/keyboard-numbers-slider.png)

Suwak (regulowany również enkoderem obrotowym) jest szybszy przy zgrubnych
zmianach; **Disable slider** przywraca pole krokowe. Wartości zakresów
telemetrii edytuje się w ten sam sposób:

![Suwak wyłączony](../assets/keyboard-numbers-options-disable-slider.png)

## Funkcja Options {: #the-options-feature }

Niemal wszędzie tam, gdzie oczekiwana jest wartość lub
[źródło](#choosing-a-source), długie naciśnięcie `ENT` otwiera okno
dialogowe **Options** — oznaką jego dostępności jest mała ikona menu
(„hamburger”) w lewym górnym rogu pola.

### Opcje wartości

![Opcje źródła](../assets/source-with-options.png)

Okno dialogowe opcji wartości podaje nazwę edytowanego parametru i pozwala
wybrać między stałym minimum/maksimum a sterowaniem nim ze **źródła** (np.
z potencjometru, aby regulować wartość w locie). Jeśli pole korzysta już ze
źródła, to samo długie naciśnięcie proponuje zamianę bieżącej wartości tego
źródła na wartość stałą:

![Zamiana źródła na wartość](../assets/source-convert-to-value.png)

### Wybór źródła {: #choosing-a-source }

Wybranie **Choose a source** otwiera dwukolumnowy selektor — najpierw
**kategoria** (wejścia analogowe, przełączniki, przełączniki logiczne,
trymy, kanały, oś żyroskopu, kanał trenera, timer, czujnik telemetryczny
lub kilka wartości specjalnych), a następnie konkretny element z tej
kategorii:

![Menu źródeł](../assets/source-menu.png)

Po ustawieniu źródła to samo długie naciśnięcie otwiera opcje właściwe dla
danego rodzaju źródła:

**Dowolne źródło** —

- **Invert** — neguje źródło (np. aktywne, gdy przełącznik *nie* jest w
  górnym położeniu, zamiast gdy jest).
- **Edge** — wyzwala jednorazowo przy zmianie stanu (fałsz→prawda lub
  prawda→fałsz), zamiast pozostawać aktywnym przez cały czas trwania stanu;
  oznaczane przedrostkiem `†` przy źródle. Dostępne dla przełączników
  ogólnie, a w szczególności dla warunku wyzwalania
  [przełącznika logicznego typu Sticky](../model-setup/logical-switches.md).

**Źródła drążków** — opcje w stylu kalibracji/subtrymu:

![Opcje źródła drążka](../assets/source-stick-options.png)

**Źródła przełączników** —

![Opcje przełącznika 2-pozycyjnego](../assets/source-2pos-options.png)
![Opcje przełącznika](../assets/switch-options.png)

- **Negative** — odwraca działanie przełącznika.
- **HalfRange** — dla przełącznika 2-pozycyjnego lub przełącznika
  logicznego zmienia zakres wyjściowy z ±100% na 0–100%.

**Źródła trymów** —

![Opcje źródła trymu](../assets/source-trim-options.png)

- **Negative** — odwraca działanie trymu (przydatne w sekcji Actions miksu
  wolnego).
- **Full range** — trymy domyślnie działają w zakresie ±25%; jako źródło
  można je rozszerzyć do ±100%.
- **Ignore trainer input** — w
  [przełączniku logicznym](../model-setup/logical-switches.md) wyklucza ruch
  pochodzący z wejścia trenera z wyzwalania przełącznika. Typowe
  zastosowanie: wykrywanie ruchu drążka samego *instruktora* (np. aby
  natychmiast zainterweniować, gdy uczeń popełni błąd) bez wyzwalania
  przełącznika przez sterowanie ucznia.

**Źródła zmiennych** —

![Opcje źródła zmiennej](../assets/source-var-options.png)

- **Negative** — neguje wartość zmiennej dla tego zastosowania.
- **Ignore range** — niektóre pola mają niesymetryczne zakresy (np. Min/Max
  w Wyjściach, obejmujące odpowiednio −150–0% oraz 0–150%). Jeżeli
  [zmienna](../model-setup/variables.md) użyta jako źródło tego pola nie ma
  identycznego zakresu, należy włączyć tę opcję, aby pominąć automatyczną
  konwersję zakresu wykonywaną przez Ethos i uniknąć nieoczekiwanych
  wartości.

**Źródła czujników telemetrycznych** — sprowadzają źródło do bieżącej
wartości minimalnej lub maksymalnej zamiast odczytu chwilowego (niektóre
czujniki udostępniają ponadto dodatkowe opcje specyficzne dla danego
czujnika):

![Opcje min/max czujnika](../assets/source-sensor-options.png)
![Wybrana wartość maksymalna czujnika](../assets/source-sensor-maxi.png)
