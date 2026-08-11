---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Przełączniki logiczne

![Menu przełączników logicznych](../assets/model-lsw-menu.png)

Przełączniki logiczne to programowane przez użytkownika przełączniki *wirtualne* — nie są to elementy fizyczne, ale można ich używać wszędzie tam, gdzie fizycznego przełącznika, jako wyzwalacza funkcji. Każdy z nich oblicza skonfigurowany warunek na podstawie swoich wejść (innych przełączników, wartości telemetrycznych, wartości miksów, wartości timerów, kanałów żyroskopu/trenera i innych), przyjmując stan Prawda lub Fałsz. Obsługiwanych jest do 100 przełączników; domyślnie nie istnieje żaden. Nowy dodaje się przyciskiem **+**; etykieta zdefiniowanego przełącznika w menu jest zielona, gdy ma on stan Prawda, i czerwona, gdy Fałsz. Dotknięcie istniejącego pozycji udostępnia opcje **Edytuj**/**Przenieś**/**Kopiuj-wklej**/**Klonuj**/**Usuń**.

![Dodawanie przełącznika logicznego](../assets/model-lsw-add.png)

## Funkcja

Każda funkcja obsługuje wyjście normalne lub odwrócone.

- **A ~ X** — prawda, gdy źródło `A` jest *w przybliżeniu* równe (z dokładnością do ok. 10%) wartości stałej `X`. Zwykle korzystniejsze niż dokładna równość —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — ponieważ przy warunku `A = X` odczyt telemetryczny wahający się na przykład między 8,5 V a 8,35 V wokół wartości docelowej 8,4 V może po prostu nigdy nie osiągnąć dokładnie 8,4 V, więc przełącznik nigdy by się nie załączył.
- **A = X** — prawda tylko wtedy, gdy `A` jest dokładnie równe `X`.
- **A > X** / **A < X** — prawda, gdy `A` jest większe/mniejsze od `X`.
- **|A| > X** / **|A| < X** — jak wyżej, ale porównywana jest wartość bezwzględna `A` (znak pomijany).
- **Δ > X** — prawda, gdy zmiana `A` (delta) w czasie **interwału kontroli** osiągnie co najmniej `X`. Interwał `---` oznacza nieskończone okno czasowe.

  ![Delta większa niż X](../assets/model-lsw-delta-gtX.png)
  ![Bezwzględna delta większa niż X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — jak wyżej, z użyciem wartości bezwzględnej zmiany.
- **Range** — prawda, gdy `A` mieści się w zadanym zakresie.

  ![Zakres](../assets/model-lsw-range.png)

- **AND** — prawda tylko wtedy, gdy każde z wymienionych źródeł (Wartość 1…N) ma stan prawda.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — prawda, gdy co najmniej jedno z wymienionych źródeł ma stan prawda.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (alternatywa wykluczająca) — prawda, gdy *dokładnie jedno* z wymienionych źródeł ma stan prawda.

  ![XOR](../assets/model-lsw-XOR.png)

- **Timer generator** — pracuje w sposób ciągły, cyklicznie załączając i wyłączając wyjście: załączone przez **Czas aktywności**, wyłączone przez **Czas nieaktywności**.

  ![Generator timera](../assets/model-lsw-timer-generator.png)

- **Sticky** — zatrzask (przerzutnik SR); patrz [poniżej](#sticky).
- **Edge** — impuls chwilowy; patrz [poniżej](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Zatrzaskuje stan **Prawda** z chwilą spełnienia warunku **Wyzwalacz ON** i utrzymuje go do momentu spełnienia warunku **Wyzwalacz OFF** — opcjonalnie z bramkowaniem przez **Warunek aktywności** (dopóki jest on Fałszywy, wyjście jest utrzymywane w stanie Fałsz niezależnie od reszty; wewnętrzny zatrzask Sticky działa w tle i zostaje ponownie przekazany na wyjście, gdy tylko Warunek aktywności wróci do stanu Prawda, z uwzględnieniem opóźnień).

Od wersji Ethos 1.6.2 oba wyzwalacze przyjmują modyfikator **Edge** (długie przytrzymanie `ENT` na warunku wyzwalacza, wybór Edge — oznaczany prefiksem `†`), co daje znacznie precyzyjniejszą kontrolę:

![Sticky z modyfikatorem edge](../assets/model-lsw-sticky-with-edge.png)
![Wybór opcji Edge](../assets/model-lsw-sticky-edge-select.png)

- **Wyzwalacz ON `SA` (bez opóźnienia)** — zatrzask przechodzi w stan Prawda w chwili załączenia SA.
- **Wyzwalacz ON `SA` (opóźnienie = 1 s)** — zatrzask przechodzi w stan Prawda 1 s po załączeniu SA, *pod warunkiem* że SA jest nadal załączony po upływie tej sekundy.
- **Wyzwalacz ON `†SA` (opóźnienie = 1 s)** — zatrzask przechodzi ze stanu Prawda→Fałsz 1 s po załączeniu SA, **niezależnie** od tego, czy SA jest wtedy nadal załączony (zbocze już wystąpiło; opóźnienie jedynie odmierza czas do wyniku).

Wyzwalacz OFF działa analogicznie, w odwrotnym kierunku. Opóźnienia stosowane są **po** Warunku aktywności — zatem zmiana Warunku aktywności ponownie uruchamia odliczanie opóźnienia, zanim zatrzaśnięta wartość ponownie trafi na wyjście. Jednoczesna zmiana obu wyzwalaczy z Fałsz→Prawda powoduje jednorazowe **przełączenie** (toggle) wyjścia Sticky. Patrz również [Parametry wspólne](#shared-parameters) poniżej.

### Edge

![Edge](../assets/model-lsw-edge.png)

Impuls chwilowy: stan Prawda przez czas **Duration**, po spełnieniu warunku wyzwalacza. **During** to para `[t1:t2]` określająca dokładnie, kiedy to następuje:

- **Zbocze narastające, During = 0,0 s** — załącza się w chwili przejścia Wyzwalacza ON z Fałsz→Prawda.

  ![Zbocze narastające](../assets/model-lsw-edge-rising-edge.png)
  ![During = 0](../assets/model-lsw-edge-during-eq0.png)

- **Zbocze narastające, During ≥ 0,0 s (np. 5,0 s)** — załącza się 5 s po przejściu Wyzwalacza ON w stan Prawda, ignorując krótsze „szpilki” w tym 5-sekundowym oknie.

  ![During > 0, zbocze narastające](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![During > 0](../assets/model-lsw-edge-during-gt0.png)

- **Zbocze opadające, During = 0,0 s** — załącza się w chwili przejścia Wyzwalacza ON z Prawda→Fałsz.
- **Zbocze opadające, During ≥ 0,0 s (np. 3,0 s)** — załącza się przy przejściu Prawda→Fałsz, ale tylko wtedy, gdy stan Prawda utrzymywał się wcześniej przez co najmniej 3 s.
- **Impuls (ustawione oba parametry t1 i t2)** — załącza się tylko wtedy, gdy Wyzwalacz ON przejdzie Fałsz→Prawda→Fałsz w tym oknie czasowym (np. między 2 s a 5 s później).

## Parametry wspólne {: #shared-parameters }

![Parametry wspólne](../assets/model-lsw-common-parameters.png)

- **Warunek aktywności** — bramkuje wyjście przełącznika w ten sam sposób jak w opisanej wyżej funkcji Sticky. Opcje: zawsze załączony, pozycje przełącznika / przełącznika funkcyjnego / przełącznika logicznego / trymu, Telemetria, Tryby lotu lub zdarzenie systemowe (Blokada gazu, Odcięcie gazu, Gaz aktywny, Telemetria aktywna, Niski RSSI, Trener aktywny, Reset lotu).
- **Opóźnienie przed aktywacją** / **Opóźnienie przed dezaktywacją** — jak długo warunek musi utrzymywać stan Prawda (lub Fałsz), zanim wyjście podąży za nim; do 60 s. Nie dotyczy funkcji Timer generator ani Edge. (Patrz [Poradnik: Ostrzeżenie o pojemności akumulatora](../how-to/battery-capacity-warning.md), gdzie opóźnienie służy do eliminacji chwilowych spadków napięcia.)
- **Potwierdzenie przed aktywacją** / **dezaktywacją** — wyświetla prośbę o potwierdzenie przez użytkownika, zanim stan faktycznie się zmieni (z opcją Anuluj, na wypadek gdy zdarzenie występuje zbyt często, by było użyteczne) — przydatne przy bramkowaniu ryzykownych działań, np. potwierdzeniu przed zdalnym wyłączeniem zasilania pojazdu naziemnego.

  ![Potwierdzenie prawda](../assets/model-lsw-confirm-lsw-true.png)
  ![Potwierdzenie fałsz](../assets/model-lsw-confirm-lsw-false.png)

- **Min Duration** — po przejściu w stan Prawda utrzymuje ten stan przynajmniej przez podany czas. Przy wartości `---` wyjście może mieć stan Prawda tylko przez jeden cykl miksera — zbyt krótko, by choćby zauważyć pogrubienie wiersza w interfejsie.
- **Max Duration** — po przejściu w stan Prawda automatycznie wraca do stanu Fałsz po upływie tego czasu, jeśli nadal jest ustawiony. Oba czasy można ustawić do 60 s.
- **Komentarz** — dowolny tekst, wyświetlany wszędzie tam, gdzie ten przełącznik zostanie dodany do widgetu wartości, służący do udokumentowania jego przeznaczenia.

## Zastosowanie z telemetrią

Zdarzenie systemowe **Telemetria aktywna** (lub przełącznik, którego źródłem jest czujnik telemetryczny, aktywny wyłącznie wtedy, gdy ten czujnik przesyła dane) obsługuje warunki typu „czy telemetria jest aktualnie odbierana”.

!!! warning
    [Miks](mixes.md) bramkowany przełącznikiem logicznym opartym na telemetrii wymaga **drugiej** akcji miksu używającej tego samego przełącznika w wersji **odwróconej**, tak aby miks nadal miał prawidłową wartość po utracie telemetrii — należy pamiętać, że nieaktywny miks daje na wyjściu wartość neutralną (0% / 1500 µs, czyli **połowę gazu** na kanale gazu). Alternatywnie można użyć akcji **Offset**, która ma już wbudowane osobne wartości dla stanu aktywnego i nieaktywnego — np. źródło **0** (wartość specjalna) z offsetem ustawionym tak, aby miks dawał +100%, gdy `LS3` jest aktywny, i −100%, gdy jest nieaktywny, obsługuje oba przypadki w jednej akcji.

## Porównywanie źródeł

Źródło jest zwykle porównywane z wartością stałą, ale zamiast tego można bezpośrednio porównać dwa źródła *tego samego* typu — np. dwa timery, dwa napięcia lub dwa czujniki obrotów.

## Ignorowanie sygnału trenera od ucznia

![Ignorowanie sygnału trenera](../assets/model-lsw-ignore-trainer-input.png)

[Opcje](../getting-started/user-interface-and-navigation.md#choosing-a-source) źródła pozwalają wykluczyć sygnał trenera pochodzący z podłączonego nadajnika ucznia (slave) — stosuje się to zwykle w przełączniku logicznym obserwującym ruch drążka **instruktora** (np. w celu natychmiastowej interwencji, gdy coś pójdzie nie tak), tak aby wejścia ucznia go nie wyzwalały. Często łączy się to z przełącznikiem trenera bramkującym Warunek aktywności po stronie instruktora.
