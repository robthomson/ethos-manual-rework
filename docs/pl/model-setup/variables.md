---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Zmienne

![Zmienne](../assets/model-vars.png)

Zmienne („Vars") to nazwane kontenery przechowujące wartości ustawień danego modelu, do których można się odwołać w dowolnym innym miejscu programowania — w tym w [miksach](mixes.md). Umieszczenie ich w osobnej sekcji oddziela *dane konfiguracyjne* modelu od jego *logiki programowania*: zamiast przeszukiwać dziesiątki miksów w poszukiwaniu wartości do zmiany, wszystko znajduje się w jednym miejscu pod zrozumiałą nazwą. Dostępne są 64 zmienne; domyślnie nie istnieje żadna. Dodaj zmienną przyciskiem **+**; dotknij istniejącej zmiennej, aby uzyskać opcje **Edytuj**/**Przenieś**/**Kopiuj**/**Klonuj**/**Usuń**.

![Dodawanie zmiennej](../assets/model-vars-add.png)

Zmienna może przechowywać stałą wartość albo być regulowana w zdefiniowanych przez użytkownika granicach (aby błędne wartości nie doprowadziły do rozbicia modelu), a także przechowywać *różne* wartości dla każdego aktywnego warunku (np. dla każdego trybu lotu). Wartości są zachowywane pomiędzy sesjami. Zmienna może zastąpić dowolną zwykłą wartość liczbową wszędzie tam, gdzie dostępna jest [funkcja Opcje](../getting-started/user-interface-and-navigation.md#the-options-feature) (pola z ikoną hamburgera).

!!! example
    Szybowiec z dzielonymi lotkami (których wewnętrzne sekcje pełnią jednocześnie rolę klap lądowania) wymaga jednego wspólnego ustawienia różnicowania lotek, stosowanego wszędzie tam, gdzie wszystkie cztery powierzchnie działają jako lotki — zmienna przechowująca tę jedną wartość, przywoływana w każdym istotnym miksie, zapewnia spójność i oznacza, że regulacji dokonuje się tylko w jednym miejscu.

## Dodawanie zmiennej

![Nowa zmienna](../assets/model-vars-new_var.png)

- **Wartość** — bieżąca wartość (wyświetlana tylko do odczytu).
- **Nazwa** — edytowalna.
- **Komentarz** — dowolny tekst objaśniający przeznaczenie zmiennej.
- **Zakres** — dolna/górna granica (jedno miejsce po przecinku, w zakresie ±500%), której wartość zmiennej nigdy nie może przekroczyć.

### Wartości

![Wartości zmiennej](../assets/model-vars-values.png)

- **Stała** — pojedyncza wartość stała, z jednym miejscem po przecinku.
- **Wiele wartości/zmienna** — **Dodaj nową wartość** przypisuje wartość do każdego aktywnego warunku. Np. `Var12` przyjmuje wartość 9%, gdy aktywny jest tryb lotu Thermal (FM4), oraz −3%, gdy aktywny jest Speed (FM5), przy zakresie ograniczonym do −10%…+15%, aby żadna z nich nie przekroczyła rozsądnych granic:

  ![Wartości zależne od trybu lotu](../assets/model-vars-fm-dependent.png)
  ![Dodawanie wartości](../assets/model-vars-add-value.png)

### Akcje

![Akcje zmiennej](../assets/model-vars-actions.png)
![Dodawanie akcji](../assets/model-vars-add-action.png)

Akcje zmieniają wartość zmiennej w czasie, sterowane przez wejście.

**Przypisanie trymu do innej funkcji** — powierza jednemu z fizycznych trymów regulację tej zmiennej zamiast jego zwykłej funkcji, zwykle z ograniczeniem do jednego aktywnego warunku:

![Zmiana przeznaczenia trymu](../assets/model-vars-functions-repurpose.png)
![Wybór trymu do zmiany przeznaczenia](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Zmień przeznaczenie trymu gazu na regulację zmiennej kompensacji wygięcia profilu, ale tylko wtedy, gdy aktywny jest tryb lotu Landing (FM3), z zakresem 0–25% i krokiem 1,0% na kliknięcie. Poza tym aktywnym warunkiem trym automatycznie powraca do swojej zwykłej funkcji.

**Akcje arytmetyczne** — sterowane przez dowolne wejście:

- **Przypisz** — ustawia zmienną na określoną wartość.
- **Dodaj** / **Odejmij** / **Pomnóż** / **Podziel** — działania arytmetyczne na bieżącej wartości.
- **Procent** — stosuje procent wartości wejścia sterującego.
- **Min** / **Max** — ogranicza zmienną względem wejścia sterującego.

  ![Akcje funkcji](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` przypisuje zmiennej wprost wartość 40%; `FS1(edge)` dodaje 2 przy każdym naciśnięciu (z ograniczeniem do maksimum zakresu); `FS2(edge)` odejmuje 2 przy każdym naciśnięciu (z ograniczeniem do minimum zakresu). Opcja **Edge** (długie naciśnięcie przełącznika funkcyjnego) ma tu istotne znaczenie — bez niej akcja wyzwalałaby się w sposób ciągły przez cały czas przytrzymywania przełącznika, zamiast raz na naciśnięcie.

  ![Przykład obliczeniowy](../assets/model-vars-calc-example.png)
