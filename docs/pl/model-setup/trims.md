---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trymy

![Trymy](../assets/model-trims.png)

Konfiguruje zakres trymu, wielkość kroku i zachowanie dla każdego drążka,
a także trym krzyżowy oraz trym natychmiastowy. Modele **X20 Pro/R/RS**
oraz **X18** oferują dwa dodatkowe przełączniki trymu, **T5**/**T6**,
przydatne do regulacji w locie wykraczających poza cztery główne drążki:

![Trymy T5/T6](../assets/model-trims-pro-t5-t6.png)

Każdy drążek ma własny, niezależny zestaw ustawień trymu.

## Ustawienia trymu {: #trim-settings }

- **Zakres** — domyślnie ±25%, regulowany aż do pełnego zakresu drążka
  ±100%. Na ekranie głównym trym o domyślnym zakresie wskazuje wartości
  od −100 do 100; trym o pełnym zakresie (100%) wskazuje od −400 do 400
  (4× zakres standardowy).

  !!! warning
      Poszerzenie zakresu oznacza, że zbyt długie przytrzymanie klawisza
      trymu może wprowadzić na tyle dużą korektę, że model stanie się
      niesterowny.

- **Krok** — rozdzielczość przełącznika trymu: **Bardzo drobny**,
  **Drobny**, **Średni**, **Zgrubny**, **Wykładniczy** (drobny w pobliżu
  środka, zgrubny dalej od niego) lub **Własny** (określony procent na
  kliknięcie).

  ![Opcje kroku](../assets/model-trims-step-options.png)

  | Krok | µs na kliknięcie (zakres 25%) |
  |---|---|
  | Bardzo drobny | 0,5 |
  | Drobny | 1 |
  | Średni | 2 |
  | Zgrubny | 4 |
  | Wykładniczy | 0,3–16 |

  Krok własny przy zakresie 25%: 1% = 1 µs/kliknięcie, 100% =
  128 µs/kliknięcie. Przy zakresie 100%: 1% = 5 µs/kliknięcie, 100% =
  512 µs/kliknięcie.

## Tryb

![Tryb trymu steru wysokości](../assets/model-trims-mode-elevator.png)

Domyślnie trym jest zawsze aktywny, ale opcja **Tryb** pozwala zmienić to
zachowanie. Zmiana trybu zeruje trym.

- **OFF** — całkowicie wyłącza trym.

  ![Tryb: off](../assets/model-trims-mode-option-off.png)

  Przydatne na przykład w modelu elektrycznym, w którym trym gazu nie jest
  potrzebny — zwolniony element sterujący można wtedy
  [wykorzystać do regulacji zmiennej Var](variables.md).

- **Łatwy** — jedna wspólna wartość trymu dla wszystkich trybów lotu.
  Typowy wybór dla lotek i steru kierunku, ponieważ rzadko wymagają one
  różnych wartości w zależności od trybu lotu.

  ![Tryb: easy](../assets/model-trims-mode-option-easy.png)

- **Niezależny dla każdego trybu lotu** — trym oddziałuje wyłącznie na
  aktywny tryb lotu. Typowy wybór dla trymu steru wysokości, ponieważ
  zwykle musi on być inny w każdym trybie lotu (np. przy zmianie
  wysklepienia profilu) — w praktyce jest to często główny powód
  konfigurowania trybów lotu.

  ![Tryb: niezależny od trybu lotu](../assets/model-trims-mode-option-fm.png)

- **Własny** — w pełni dowolne zachowanie, budowane z **zachowań**
  dodawanych samodzielnie.

### Własne zachowania trymu

![Dodawanie zachowania](../assets/model-trims-mode-elevator-add-behaviour.png)
![Opcje zachowania](../assets/model-trims-mode-elevator-edit-behaviour.png)

Każdy wiersz zachowania zawiera warunek oraz jedną z opcji:

- **Odłączony** — wybiórczo wyłącza trym przy spełnieniu tego warunku
  (zamiast wyłączać go całkowicie ustawieniem Tryb = OFF).

  ![Odłączony](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Warunek odłączenia](../assets/model-trims-mode-unplugged-select.png)

- **Normalny** (domyślnie) — zwykłe zachowanie trymu.
- **Równy (innemu trymowi)** — ten trym dokładnie odwzorowuje wartość
  trymu z innego warunku.

  ![Równy](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Przesunięcie + (inny trym)** — ten trym jest dodawany do wartości
  trymu z innego warunku.

  ![Przesunięcie](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Przykład praktyczny** — szybowiec z bazowym trymem steru wysokości dla
trybu **Cruise** oraz zależnymi trymami dla trybów **Speed** i
**Thermal**:

![Wybór FM5 Speed](../assets/model-trims-mode-elevator-custom-select.png)
![Wybór FM4 Thermal](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Wytrymuj model do lotu poziomego w trybie domyślnym (Cruise).
2. Dodaj zachowanie: **Przesunięcie + Default**, warunek `FM5(Speed)`.
   Teraz każda korekta trymu wykonana w trybie Speed jest zapisywana jako
   przesunięcie względem wartości bazowej z trybu Cruise — jest odrębna,
   ale wciąż od niej zależna.

   ![Przesunięcie dla trybu Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Dodaj w ten sam sposób drugie zachowanie: **Przesunięcie + Default**,
   warunek `FM4(Thermal)`. (Po utworzeniu pierwszego zachowania okno
   dialogowe oferuje również opcje `Equal FM5(Speed)` oraz
   `Offset + FM5(Thermal)`, ponieważ może już odwołać się także do tego
   zachowania).

   ![Przesunięcie dla trybów Speed i Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Przy takiej konfiguracji późniejsza zmiana bazowego trymu Cruise
(np. po zmianie środka ciężkości) automatycznie przesuwa o tę samą
wartość trymy trybów Speed i Thermal, ponieważ są one przesunięciami
względem wartości bazowej, a nie niezależnymi wartościami.

- **Audio** — pozwala wyłączyć standardowy komunikat głosowy trymu dla
  trymu wykorzystanego do innego celu, gdy jego odczytywanie nie ma już
  sensu.

## Dodatkowe trymy

![Dodawanie dodatkowego trymu](../assets/model-trims-add-trim-select.png)
![Ustawienia dodatkowego trymu](../assets/model-trims-add-trim-edit.png)

Opcja **Dodaj dodatkowy trym** tworzy trym wykraczający poza cztery
standardowe drążki (oraz T5/T6): **Nazwa**, źródła **Góra**/**Dół**
sterujące trymem, a także te same opcje **Zakres**, **Krok**, **Tryb** i
**Audio** co powyżej.

## Trym krzyżowy

![Trym krzyżowy](../assets/model-trims-cross.png)
![Edycja trymu krzyżowego](../assets/model-trims-cross-edit.png)

Określa, który przełącznik trymu faktycznie reguluje dany drążek — czyli
umożliwia sterowanie trymem drążka za pomocą innego niż zwykle fizycznego
elementu trymowania. (T5/T6 dostępne są wyłącznie w X20 Pro i X18).

## Trym natychmiastowy {: #instant-trim }

![Trym natychmiastowy](../assets/model-trims-instant-trim.png)

Gdy jest aktywny, dodaje bieżące położenia drążków do odpowiadających im
trymów domyślnych (oraz krzyżowych). Najlepiej przypisać go do
przełącznika dostępnego bez puszczania drążków — wyzwolenie go podczas
lotu prosto i poziomo pozwala natychmiast ustawić trymy, zamiast
wielokrotnie klikać klawiszem trymu przy dużym rozstrojeniu. Po locie
trymującym należy go ponownie wyłączyć, aby przypadkowo nie zaburzyć
trymów później.

!!! note
    Trym natychmiastowy działa tylko podczas wyświetlania jednego z
    widoków głównych.

## Przeniesienie trymów do subtrymów

![Przeniesienie trymów do subtrymów](../assets/model-trims-move-trims-to-subtrims.png)

Po wytrymowaniu modelu do lotu poziomego funkcja przenosi wartość trymu
kanału (np. steru wysokości) do jego ustawienia [Subtrym](outputs.md) i
zeruje trym widoczny na ekranie — to przejrzysty sposób na sprawdzenie,
czy trymy lotu nie uległy od tego czasu zmianie.

Przy zastosowaniu trybów lotu kanał może mieć więcej niż jedną istotną
wartość trymu, natomiast Subtrym w Wyjściach jest pojedynczym ustawieniem
globalnym, obowiązującym we wszystkich trybach lotu. Funkcja to
uwzględnia: pobiera trym **aktualnie wybranego** trybu lotu, przenosi go
do Subtrymu, zeruje ten trym i koryguje trymy *wszystkich pozostałych*
trybów lotu na tym samym kanale, aby to skompensować — dzięki czemu
rzeczywiste wychylenie powierzchni sterowej w każdym trybie lotu pozostaje
niezmienione.

!!! tip
    Dla zachowania spójności zawsze uruchamiaj tę funkcję z tego samego
    „bazowego” trybu lotu (np. Cruise w szybowcu) — pod tym warunkiem można
    ją bezpiecznie powtarzać.

Duże wartości trymu lub subtrymu powodują bardzo niesymetryczne wychylenia
— lepiej usunąć przyczynę mechanicznie. Dąż do tego, aby przy neutralnym
położeniu powierzchni sterowych orczyki i cięgna tworzyły kąt 90°
(wyjątkiem są klapy, gdzie rezygnuje się z części ruchu w górę na rzecz
większego ruchu w dół), a następnie użyj ustawienia **Środek PWM**
(PWM center) do precyzyjnego dostrojenia do dokładnie 90°, gdy mechanika
jest już blisko ideału.
