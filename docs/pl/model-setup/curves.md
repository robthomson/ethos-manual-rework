---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Krzywe

![Typy krzywych](../assets/model-curves-type.png)

Wielokrotnego użytku krzywe odpowiedzi dla [Miksów](mixes.md#anatomy-of-a-mix) lub
[Wyjść](outputs.md#editing-a-channel) — wbudowane Expo jest dostępne
bezpośrednio w obu miejscach, natomiast wszystko bardziej złożone definiuje się tutaj (lub przez
**Dodaj krzywą**, dostępne bezpośrednio z każdego z tych ekranów edycji). Dostępnych jest do 50
krzywych; domyślnie nie istnieje żadna (Expo jest zawsze wbudowane
niezależnie od tego). Dodaj krzywą przyciskiem **+**; dotknij istniejącej krzywej, aby uzyskać
**Edytuj**/**Przenieś**/**Kopiuj-wklej**/**Klonuj**/**Usuń**.

![Dodawanie krzywej](../assets/model-curves-add.png)

## Typy krzywych

- **Expo** — wartość domyślna 40; wartość dodatnia łagodzi odpowiedź wokół
  środka, ujemna ją zaostrza. Złagodzenie odpowiedzi wokół środka drążka pomaga uniknąć
  przesterowania, szczególnie w przypadku mniej doświadczonych pilotów.

  ![Expo](../assets/model-curves-expo.png)

- **Funkcja** — niewielki zestaw stałych kształtów matematycznych:

  ![Typy funkcji](../assets/model-curves-fn-types.png)

  - **x > 0** — przekazuje źródło bez zmian, gdy jest dodatnie;
    zwraca 0, gdy jest ujemne.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — odbicie lustrzane: przekazuje wartość, gdy jest ujemna, i 0, gdy
    jest dodatnia.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — przekazuje źródło jako jego wartość bezwzględną (zawsze
    dodatnią).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — zwraca 100%, gdy źródło jest dodatnie, i 0, gdy jest
    ujemne (twarde przełączenie, nie przekazanie wartości).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — zwraca −100%, gdy wartość jest ujemna, i 0, gdy jest dodatnia.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — zwraca −100%, gdy wartość jest ujemna, i +100%, gdy jest dodatnia.

    ![|f|](../assets/model-curves-fn-barf.png)

  Każdy typ krzywej — włącznie z Funkcją — ma również **Przesunięcie**, które przesuwa
  ją w górę lub w dół na osi Y (z dokładnością do jednego miejsca po przecinku, tak jak
  wartości Y w ogólności):

  ![Przesunięcie funkcji](../assets/model-curves-fn-xgt0-offset.png)

- **Własna** — krzywa oparta na punktach, domyślnie 5 punktów, maksymalnie 21.

  ![5-punktowa krzywa własna](../assets/model-curves-custom5.png)

  - **Wygładzanie** — prowadzi gładką krzywą przez wszystkie punkty zamiast
    prostych odcinków między nimi.

    ![Krzywa wygładzona](../assets/model-curves-custom5-2-smooth.png)

  - **Tryb uproszczony** — **Wł.** ogranicza edycję wyłącznie do równomiernie rozmieszczonych
    współrzędnych Y (X jest stałe); **Wył.** pozwala edytować zarówno X, jak i Y
    dla każdego punktu, z wyjątkiem punktów skrajnych −100%/+100%, które są zablokowane, ponieważ
    krzywa musi zawsze obejmować pełny zakres sygnału.

    ![Tryb uproszczony wyłączony](../assets/model-curves-custom-easy-off.png)

  **Elementy sterujące edytora** (ten sam schemat co w [edytorze krzywej balansu w Wyjściach](outputs.md#balance-channels)):

  - **Źródło** — domyślnie własne źródło (źródła) miksu danej krzywej lub **Automatyczne wejście analogowe**,
    aby wykryć pierwszy poruszony drążek/suwak/potencjometr.
  - Przyciąganie do najbliższego punktu za pomocą enkodera obrotowego oraz przełącznik **Blokada**,
    zamrażający wejścia podczas obserwowania wynikającego z nich ruchu powierzchni sterowej.
  - Kursor na żywo pokazuje bieżącą wartość wejściową sterującą krzywą, co
    pomaga zgrać ją z punktem przed regulacją.

## Sterowanie krzywą za pomocą Var

Zarówno **Przesunięcie** krzywej typu Funkcja, jak i pojedynczy punkt krzywej **Własnej**
mogą być sterowane przez [Var](variables.md) zamiast stałej wartości —
a taki Var może z kolei być regulowany w locie za pomocą przypisanego do tego celu trymu:

![Przesunięcie funkcji z Var](../assets/model-curves-fn-offset-var.png)
![Punkt krzywej własnej z Var](../assets/model-curves-custom-with-var.png)

Pełny przykład zastosowania tego schematu znajdziesz w [Zmienne](variables.md) oraz [Poradnik: Krzywa kompensacji regulowana w locie](../how-to/in-flight-compensation-curve.md).
