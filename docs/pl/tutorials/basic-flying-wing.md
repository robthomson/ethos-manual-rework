---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Przykład podstawowego latającego skrzydła (elewony)

Latające skrzydło z elewonami na dwóch serwach, wykorzystujące zalecane przez producenta modelu Dreamflight Weasel wartości rat, Expo i proporcji miksów jako konkretny, przepracowany przykład. Najpierw wykonaj [Wstępną konfigurację nadajnika](initial-radio-setup.md).

## Krok 1. Sprawdź ustawienia systemu {: #step-1-confirm-system-settings }

Domyślna kolejność **AETR**, z opcją **[Pierwsze cztery kanały stałe](../system-setup/controls.md#first-four-channels-fixed)** ustawioną na **OFF**. Przed przejściem dalej zarejestruj (jeśli ACCESS) i zbinduj odbiornik poprzez [System RF](../model-setup/rf-system.md).

## Krok 2. Określ wymagane serwa/kanały

W konstrukcji z elewonami [miksy](../model-setup/mixes.md) łączą sygnał lotek i steru wysokości na obu fizycznych powierzchniach sterowych — łącznie tylko 2 kanały, z których każdy stanowi mieszankę obu sygnałów wejściowych.

## Krok 3. Utwórz nowy model

![Tworzenie modelu samolotu](../assets/tut-wing-eg-wiz-create-airplane.png)

W [Wyborze modelu](../model-setup/model-select.md) uruchom kreatora **Airplane** i wybierz **Non stabilized receiver** (odbiornik bez stabilizacji).

![Brak napędu](../assets/tut-wing-eg-wiz-no-engine.png)

Wybierz **No engine** (brak napędu), zaakceptuj domyślne 2 kanały lotek i wybierz **No flaps** (brak klap).

![Brak usterzenia](../assets/tut-wing-eg-wiz-no-tail.png)

Jako typ usterzenia wybierz **None** — to właśnie ta opcja powoduje, że Ethos automatycznie zbuduje miks elewonów (sygnały lotek + steru wysokości, oba na tych samych dwóch kanałach). Nadaj modelowi nazwę (np. „Weasel”), wybierz bitmapę i zakończ — model stanie się aktywny w kategorii Airplane.

## Krok 4. Przejrzyj i skonfiguruj miksy

![Przegląd miksów](../assets/tut-wing-eg-mixes.png)

Kreator tworzy miks Ailerons na kanałach 1+2, a następnie miks Elevators *również* na kanałach 1+2 — oba sygnały wejściowe działają na oba kanały elewonów, co stanowi istotę miksowania elewonów.

### Lotki

![Miks lotek](../assets/tut-wing-eg-mixes-ail-mix.png)

**Weight/Rates** — zgodnie z instrukcją modelu Weasel wychylenie lotek powinno być około 3× większe niż steru wysokości, a suma obu powinna wynosić 100%: **75%** lotki, **25%** ster wysokości. Rate niskie to około połowa wartości wysokich: **36%** lotki low, **12%** ster wysokości low.

![Waga miksu lotek](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — zalecane dla Weasela 35% high / 20% low, aktywowane przełącznikiem SB w dolnym położeniu, spłaszczające charakterystykę wokół środka drążka.

**Różnicowanie** — w tej konstrukcji niewielkie, około **4%**:

![Różnicowanie lotek](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Zobacz [Przykład podstawowego modelu ze stałym płatem](basic-fixed-wing.md#ailerons), aby poznać znaczenie różnicowania — obowiązuje tu ta sama zasada dotycząca odwrotnego odchylania.)

### Ster wysokości

![Miks steru wysokości](../assets/tut-wing-eg-mixes-ele-mix.png)

Ten sam schemat: rate **25%**/**12%** high/low, te same wartości Expo co dla lotek.

### Ster kierunku

![Miks steru kierunku](../assets/tut-wing-eg-mixes-rud-mix.png)

Weasel go nie posiada — latające skrzydła zwykle go nie potrzebują. Jeżeli w modelu z elewonami ster kierunku *jest* potrzebny, dodaj go jako [Miks wolny](../model-setup/mixes.md#mix-libraries) na kanale 3.

## Krok 5. Zbinduj odbiornik

Tak jak w [Kroku 1](#step-1-confirm-system-settings) — zarejestruj/zbinduj przed dalszymi czynnościami; rozważ też odłączenie popychaczy serw lub zmniejszenie wychyleń do czasu ustawienia limitów Min/Max, aby uniknąć przeciążenia mechaniki.

## Krok 6. Przejrzyj miksy

Kanały wyjściowe 1/2 można przemianować na **Elevon1**/**Elevon2**. Przy pełnym wychyleniu lotek w prawo kanał 1 (prawy, wychylający się w górę) wskazuje 75%, natomiast kanał 2 (lewy, wychylający się w dół) wskazuje 72% — ta różnica 3% *to właśnie* działanie różnicowania. Po dodaniu pełnego wychylenia steru wysokości w dół kanał 1 osiąga 75+25 = 100%, a kanał 2 72−25 = 47%.

## Krok 7. Skonfiguruj maksymalne wychylenia serw

![Pełne wychylenie lotek](../assets/tut-wing-eg-outputs-full-ail.png)
![Pełne lotki + pełny ster wysokości](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Najpierw wyśrodkuj każde serwo za pomocą **PWM center**. Zalecane maksymalne wychylenie dla Weasela to 25 mm dla lotek + 10 mm dla steru wysokości = 35 mm łącznie — zadaj pełne wychylenia lotek i steru wysokości zarówno w zgodnym, *jak i* w przeciwnym kierunku i sprawdź, czy żadne z nich nie przekracza limitów mechanicznych ani limitów serwa, zanim ustalisz ostateczne wychylenia.

- **Min/Max** — twarde limity, nigdy nienadpisywane; ich zmniejszenie ogranicza wychylenie, zamiast je obcinać. Domyślnie ±100%, w razie potrzeby rozszerzalne do ±150%.
- **Curve** — często szybsza i bardziej elastyczna metoda niż bezpośrednie żonglowanie wartościami Min/Max/Subtrim, z dodatkową zaletą w postaci wykresu na żywo. Krzywa 3-punktowa wystarcza dla większości wyjść; krzywa 5-punktowa na drugim elewonie ułatwia zsynchronizowanie wychyleń w 5 punktach względem pierwszego. Stosując do tego celu krzywą, pozostaw Min/Max/Subtrim na wartościach przelotowych (−100/100/0 lub −150/150/0 przy rozszerzonych limitach) i pozwól, aby kształtowanie realizowała krzywa.
