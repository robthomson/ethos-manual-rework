---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Podstawowy przykład modelu stałopłata

Kompletny przewodnik dla samolotu z silnikiem + 2 lotki + 2 klapy + ster
wysokości + ster kierunku, z jednym serwem na powierzchnię sterową,
zbudowany od początku do końca za pomocą kreatora. Najpierw wykonaj
[Wstępną konfigurację nadajnika](initial-radio-setup.md).

## Krok 1. Sprawdzenie ustawień systemowych

W tym przykładzie zastosowano domyślną kolejność kanałów **AETR**.

## Krok 2. Określenie wymaganych serw/kanałów

[Miksy](../model-setup/mixes.md) są sercem nadajnika — do 100 kanałów
miksera, przy czym najniższe numery są zwykle przypisywane do serw
(ponieważ numery kanałów odwzorowują się bezpośrednio na kanały
odbiornika; wewnętrzny moduł RF X20 obsługuje do 24 kanałów wyjściowych).
Wyższe kanały pozostają wolne dla kanałów wirtualnych lub dodatkowych
kanałów rzeczywistych realizowanych przez wiele modułów RF i SBUS. Nasz
płatowiec:

| Funkcja | Kanały |
|---|---|
| Silnik | 1 |
| Lotki | 2 |
| Klapy | 2 |
| Ster wysokości | 1 |
| Ster kierunku | 1 |

(Podwozie chowane dodamy później, w [Kroku 10](#step-10-add-a-mix-for-retracts).)

## Krok 3. Utworzenie nowego modelu

![Tworzenie modelu samolotu](../assets/tut-fw-eg-wiz-create-airplane.png)

W [Wyborze modelu](../model-setup/model-select.md) wybierz kategorię,
dotknij **+** i uruchom kreator **Airplane**. W tym przykładzie wybierz
**Non stabilized receiver**.

![Kanały silnika](../assets/tut-fw-eg-wiz-engine.png)
![Kanały lotek/klap](../assets/tut-fw-eg-wiz-ail-flaps.png)

Zaakceptuj 1 kanał silnika, następnie 2 kanały lotek i wybierz 2 kanały
klap.

![Typ usterzenia](../assets/tut-fw-eg-wiz-tail.png)
![Kanały steru wysokości/kierunku](../assets/tut-fw-eg-wiz-ele-rudd.png)

Zaakceptuj domyślne **Traditional Tail**, z 1 kanałem steru wysokości
i 1 kanałem steru kierunku.

![Nazwa modelu](../assets/tut-fw-eg-wiz-name.png)
![Odbiornik](../assets/tut-fw-eg-wiz-rx.png)

Nadaj mu nazwę (np. „FWexample” — do 15 znaków), zakończ pracę kreatora,
a model stanie się modelem aktywnym, utworzonym w kategorii Airplane.

## Krok 4. Przegląd i konfiguracja miksów

![Przegląd miksów](../assets/tut-fw-eg-mixes.png)

Kreator utworzył już miksy lotek (kanały 1 i 5), steru wysokości, gazu,
steru kierunku oraz klap (klapy pokazują `---` — nie przypisano jeszcze
źródła).

### Lotki {: #ailerons }

![Miks lotek](../assets/tut-fw-eg-mixes-ail-mix.png)
![Edycja miksu lotek](../assets/tut-fw-eg-mixes-ail-edit.png)

**Weight/Rates** — przed pierwszym lotem nowego modelu skonfiguruj
wychylenia: umiarkowany zakres (np. 30%) sprawdza się w lataniu
sportowym, pełne 100% w lataniu 3D. Dodaj wartość 60% dla środkowej
pozycji przełącznika SB oraz 30% dla SB w dół — wartość domyślna (SB
w górę) pozostaje na poziomie 100%:

![Wartości Weight](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — liniowa charakterystyka może sprawiać wrażenie nerwowej wokół
neutrum; dodaj wartości Expo (np. 60%/40%/20% dla tych samych pozycji
SB), aby spłaszczyć odpowiedź w pobliżu neutrum bez zmniejszania
maksymalnego wychylenia:

![Wartości Expo](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Różnicowanie** — jednakowe wychylenia lotek w górę i w dół powodują
większy opór na lotce wychylającej się w dół niż na tej wychylającej się
w górę, co odchyla model na zewnątrz zakrętu („odwrotne odchylenie”).
Dodatnie różnicowanie (powszechnie 50%) zmniejsza wychylenie w dół
względem wychylenia w górę, przeciwdziałając temu zjawisku:

![Różnicowanie 50%](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Aby regulować różnicowanie w locie, przytrzymaj `ENT` na wartości,
wybierz **Use a source** i wskaż Pot1:

![Use a source](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Wybrany Pot1](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Gdy wartość ustalona w locie będzie zadowalająca, przytrzymaj ponownie
i wybierz **Convert to value**, aby zapisać ją na stałe:

![Convert to value](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trym** — można odłączyć ten miks od przypisanego trymu bez wyłączania
samego trymu, uwalniając go do innego zastosowania:

![Trym lotek](../assets/tut-fw-eg-mixes-ail-trim.png)

### Ster wysokości i ster kierunku

Ten sam schemat trzech wartości wychyleń + Expo, tutaj na przełączniku SC:

![Wartości Expo steru wysokości](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Gaz

![Miks gazu](../assets/tut-fw-eg-mixes-thr-edit.png)

Pozostaw wejście na drążku gazu — wychylenia ani Expo nie są tu
potrzebne — natomiast przełącznik bezpieczeństwa jest niezbędny;
nieoczekiwane uruchomienie silnika modelarskiego lub elektrycznego może
spowodować poważne obrażenia.

**Low position trim** (silniki spalinowe/żarowe) — reguluje obroty biegu
jałowego niezależnie od pełnego gazu:

![Low position trim](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Po włączeniu tej opcji kanał gazu przy drążku w pozycji biegu jałowego
znajduje się na poziomie −75%; dźwignia trymu gazu reguluje wówczas bieg
jałowy w zakresie od −100% do −50%.

**Odcięcie gazu** — zatrzask bezpieczeństwa. Przy przełączniku SA w dół
jako warunku aktywnym (wyświetlanym pogrubioną czcionką, gdy jest
aktywny) wyjście gazu utrzymuje się na poziomie −100%, gdy drążek spadnie
poniżej −85%:

![Odcięcie gazu](../assets/tut-fw-eg-mixes-thr-cut.png)

Po włączeniu opcji **Sticky** gaz zostaje odcięty **natychmiast** po
przestawieniu SA w dół, niezależnie od pozycji drążka:

![Odcięcie gazu z opcją Sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

W obu przypadkach po ustaniu warunku aktywnego drążek musi zostać
sprowadzony poniżej −85%, zanim gaz będzie mógł ponownie wzrosnąć — co
zapobiega gwałtownemu przejściu silnika na wysokie obroty w chwili
zwolnienia przełącznika odcięcia.

**Blokada gazu** — awaryjne odcięcie z *dowolnej* pozycji drążka,
sprowadzające wyjście bezpośrednio do −100% (lub skonfigurowanej
wartości) w chwili spełnienia warunku:

![Blokada gazu](../assets/tut-fw-eg-mixes-thr-hold.png)

### Klapy

![Wejście klap](../assets/tut-fw-eg-mixes-flaps-input.png)

Przypisz klapy do przełącznika SE i ustaw wagę obu kanałów wyjściowych na
100%:

![Wagi klap](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Krok 5. Bindowanie odbiornika

Zarejestruj (w przypadku ACCESS) i zbinduj odbiornik przez [System
RF](../model-setup/rf-system.md). Przed przejściem do Wyjść rozważ
odłączenie cięgien serw lub tymczasowe zmniejszenie ich zakresu ruchu,
aby uniknąć przesterowania mechaniki podczas ustawiania limitów Min/Max.

## Krok 6. Konfiguracja wyjść

![Wyjścia](../assets/tut-fw-eg-outputs.png)

[Wyjścia](../model-setup/outputs.md) dopasowują logikę miksera do
rzeczywistej mechaniki modelu.

**Lotka 1** — wyśrodkuj serwo za pomocą **PWM center** po zoptymalizowaniu
cięgna mechanicznego, a następnie ustaw **Min**/**Max**. Tymczasowe
przypisanie potencjometru do Min (a potem do Max, tak samo jak
w przykładzie z różnicowaniem powyżej) przyspiesza dostrajanie:

![Edycja wyjścia lotki](../assets/tut-fw-eg-outputs-edit-ail.png)

**Klapy** — klapy zwykle wymagają dużego wychylenia w dół dla skutecznego
hamowania; poświęca się część wychylenia w górę w cięgnie, aby to
osiągnąć, tak by przy serwie w pozycji neutralnej klapa była wychylona do
połowy w dół, a następnie ustawia się rzeczywiste położenia „góra”
i „pełne wychylenie w dół” za pomocą Min/Max. Krzywa 5-punktowa to
powszechny sposób korygowania wynikającej z tego niezgodności ruchu klap
i lotek. Na koniec użyj funkcji **[Balance
channels](../model-setup/outputs.md#balance-channels)**, aby
zsynchronizować lewe i prawe lotki oraz klapy.

## Krok 7. Wprowadzenie do trybów lotu

[Tryby lotu](../model-setup/flight-modes.md) pozwalają modelowi
przechowywać ustawienia przypisane do konkretnych zadań — na zasadzie
zmiany biegów. Spośród 20 dostępnych w tym przykładzie wykorzystano trzy:
**Default**, **Flaps Half** (przełącznik SE w pozycji środkowej) oraz
**Flaps Full** (SE w górę). Aktywny jest pierwszy tryb lotu, którego
warunek jest spełniony; tryb **Default** nie ma żadnego warunku i
przejmuje sterowanie zawsze, gdy nie obowiązuje żaden inny — dlatego nie
posiada opcji wyboru przełącznika. Narastanie/zanikanie 1 s wygładza
przejście podczas wypuszczania klap.

## Krok 8. Konfiguracja trymów

Istnieją dwa sposoby obsługi trymu steru wysokości zmieniającego się wraz
z położeniem klap:

**Niezależne trymy dla każdego trybu lotu** — najprostsza opcja: trym
steru wysokości staje się w pełni niezależny dla każdego trybu lotu
i przełącza się automatycznie wraz ze zmianą pozycji SE. Ponieważ każdy
tryb trymuje się od zera, pomocna jest funkcja [Instant
trim](../model-setup/trims.md#instant-trim) — najpierw wytrymuj model do
normalnego lotu, następnie wyląduj i wykorzystaj te ustawienia jako punkt
wyjścia dla trybów z klapami.

**Trym bazowy z przesunięciem** — trymowanie raz w trybie Default,
a kompensacja steru wysokości dla każdego trybu klap nakładana na wierzch
jako przesunięcie:

1. Ustaw **Step** trymu na Medium (dla szybszego wstępnego trymowania;
   później zmniejsz go do precyzyjnej regulacji), **Mode** na Custom
   i dodaj nowe zachowanie.
2. **Warunek aktywny**: `FM1(Flaps Half)`, tryb **Offset + Default** —
   trym dla Flaps Half staje się trymem bazowym powiększonym o dowolne
   przesunięcie ustawione podczas aktywności tego trybu:

   ![Dodanie zachowania](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Powtórz dla `FM2(Flaps Full)`:

   ![Wybór FM](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Każdy tryb klap można teraz trymować niezależnie, ale późniejsza
korekta bazowego trymu Default (np. w celu skompensowania dryfu
termicznego serwa) automatycznie przesuwa oba trymy trybów klap o tę samą
wartość.

![Wybór trymu Custom](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Krok 9. Konfiguracja timera pakietu lotniczego

W [Timerach](../model-setup/timers.md) edytuj Timer 1: tryb **Down**,
wartość początkowa 5 minut, działający zawsze, gdy spełniony jest warunek
**Throttle active** (i timer nie jest przytrzymywany w stanie
zerowania). Opcjonalnie przypisz proporcjonalne źródło odmierzania czasu
(np. drążek gazu), aby timer odliczał w tempie rzeczywistym przy pełnym
gazie i zwalniał wraz z redukcją gazu.

## Krok 10. Dodanie miksu dla podwozia chowanego {: #step-10-add-a-mix-for-retracts }

![Źródło miksu podwozia](../assets/tut-fw-eg-retracts-source.png)

Dotknij miksu, wybierz **Add Mix** → **Free Mix**, nazwij go „Retracts”,
ustaw warunek Always, a jako źródło wskaż przełącznik SF. Domyślne
działanie Weight = 100% jest odpowiednie — w ten sposób podwoziu
chowanemu przydzielony zostaje np. kanał 8:

![Wyjście podwozia chowanego](../assets/tut-fw-eg-retracts-outputs.png)
