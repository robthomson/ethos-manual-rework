---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Wyjścia

![Wyjścia](../assets/model-outputs.png)

Wyjścia stanowią granicę pomiędzy czystą „logiką” [Miksów](mixes.md) a
światem fizycznym — serwami, cięgnami, powierzchniami sterowymi,
siłownikami i przetwornikami. To tutaj punkty krańcowe, odwracanie,
centrowanie i krzywe korekcyjne są dopasowywane do rzeczywistych
mechanicznych potrzeb modelu. Każdy kanał wyjściowy odpowiada wyjściu
serwa w odbiorniku (CH1 → gniazdo serwa nr 1, przy domyślnych ustawieniach
protokołu).

Ethos operuje na procentach, ale serwa są ostatecznie sterowane szerokością
impulsu PWM w mikrosekundach:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Kanał **bez aktywnego miksu** wystawia wartość neutralną (0% / 1500 µs) —
    dotyczy to również kanału, którego jedyne miksy są w danej chwili
    nieaktywne. Upewnij się, że każdy faktycznie używany kanał zawsze ma
    obsługujący go aktywny miks. W przypadku kanału gazu wartość neutralna
    oznacza **połowę gazu**.

Ekran Wyjść pokazuje dwa paski dla każdego kanału: dolny (zielony) to
wartość miksera dla danego kanału, górny (pomarańczowy) to wartość po
przetworzeniu przez Wyjścia, faktycznie wysyłana do odbiornika (zarówno
w % , jak i w µs). Ograniczenia Min/Max są widoczne jako wyszarzone
fragmenty pomarańczowego paska. Kanały aktualnie nietransmitowane do modułu
RF mają ciemniejsze tło. Na kanale pojawiają się małe ikony, gdy jego
ustawienia Kierunku, Krzywej, Spowolnienia lub Balansu zostały zmienione
względem domyślnych — pozwala to jednym rzutem oka rozpoznać kanały
o niedomyślnych ustawieniach.

!!! tip
    Długie naciśnięcie `ENT` na ekranie Miksów lub Trybów lotu przenosi
    bezpośrednio tutaj.

## Edycja kanału {: #editing-a-channel }

![Edycja wyjścia steru wysokości](../assets/model-outputs-elevator-edit.png)
![Edycja wyjścia gazu](../assets/model-outputs-throttle-edit.png)

Dotknij kanału, aby go otworzyć. Podgląd u góry pokazuje wartość miksu
(zielona) na tle wartości wyjściowej (pomarańczowa), z małym białym
znacznikiem punktów Min/Max.

- **Nazwa** — do edycji.
- **Kierunek** — odwraca wyjście kanału, zwykle w celu odwrócenia kierunku
  obrotu serwa. Wyświetlany jako ikona podwójnej strzałki przy kanale. **Nie**
  wpływa na zasilające go miksy i **nie** zamienia ograniczeń Min/Max.
- **Min/Max** — twarde ograniczenia, które nigdy nie są przekraczane —
  ustawiane, aby uniknąć blokowania mechanicznego. Działają jak ustawienia
  punktów krańcowych / wzmocnienia: ich zmniejszenie redukuje wychylenie,
  zamiast powodować obcinanie sygnału. Domyślnie ±100%, z możliwością
  regulacji do ±150%. Podczas regulacji ten koniec zakresu, w którego stronę
  aktualnie następuje ruch, jest wyświetlany pogrubioną czcionką (np. wychyl
  drążek steru wysokości do przodu, a wartość Max zostanie pogrubiona,
  potwierdzając, że ustawiasz właśnie ten koniec).

  ![Ostrzeżenie o redundancji SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Redundancja SBUS"
      Konfiguracja redundancji wykorzystująca SBUS nie może wysterować serwa
      poza mniej więcej ±125%. Same pola Min/Max mają asymetryczne zakresy
      (−150–0% oraz 0–150%) — jeśli sterujesz nimi ze [Zmiennej](variables.md),
      nadaj tej zmiennej identyczny zakres lub ustaw **Ignoruj zakres** (zob.
      [opcje źródła](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      w przeciwnym razie automatyczna konwersja zakresu da nieoczekiwane
      wartości. Jeśli wyjście głównego odbiornika przekracza 125% i odbiornik
      przejdzie w tryb failsafe, odbiornik redundantny przejmujący sterowanie
      przez SBUS ograniczy je z powrotem do 125%.

- **Środek/Subtrim** — przesuwa wyjście, zwykle w celu wycentrowania orczyka
  serwa; punkty krańcowe pozostają bez zmian.

  !!! warning
      Nie używaj subtrimu do dużych przesunięć — wprowadza on znaczne
      różnicowanie w odpowiedzi serwa. Do czegokolwiek wykraczającego poza
      precyzyjne centrowanie użyj zamiast tego **miksu offsetu**.

- **Środek PWM** — działa podobnie do subtrimu, ale przesuwa *cały* zakres
  pracy serwa łącznie z twardymi ograniczeniami; odbywa się to efektywnie
  wewnątrz samego serwa i nie jest pokazywane na monitorze kanałów. Dzięki temu
  centrowanie mechaniczne pozostaje oddzielone od trymowania.
- **Krzywa** — przypisuje krzywą Expo lub niestandardową (istniejącą lub nową,
  ze skrótem **Edytuj** po ustawieniu) w celu skorygowania rzeczywistej
  odpowiedzi — np. utrzymania dokładnej zgodności lewej i prawej klapy.
  Wyświetlana jako ikona krzywej przy kanale.
- **Spowolnienie góra/dół** — spowalnia reakcję wyjścia na zmiany sygnału
  wejściowego, w sekundach potrzebnych na przejście 0→100% — np. spowolnienie
  podwozia chowanego zwykłym serwem proporcjonalnym. Wyświetlane jako ikona
  zegara przy kanale. (**Opóźnienie**, w odróżnieniu od spowolnienia, jest
  dostępne w [przełącznikach logicznych](logical-switches.md)).

## Zamiana kanałów {: #swap-channels }

![Zamiana kanałów](../assets/model-outputs-swap-channels.png)
![Wybór kanału do zamiany](../assets/model-outputs-swap-channels-select.png)

Zamienia miejscami dwa kanały wyjściowe. Okno dialogowe otwiera się
z wypełnionym bieżącym kanałem; wybierz drugi i zatwierdź — zamiana
następuje natychmiast, a każdy miks odwołujący się do któregokolwiek z tych
kanałów zostaje odpowiednio zaktualizowany.

## Reset ustawień

![Reset kanału](../assets/model-outputs-reset-select.png)

Przywraca wszystkie parametry kanału do wartości domyślnych — przydatne przed
przeznaczeniem kanału do innego celu; okno potwierdzenia zapobiega
przypadkowemu użyciu.

## Balansowanie kanałów {: #balance-channels }

![Wybór kanałów do zbalansowania](../assets/model-outputs-balance-choose_channels.png)
![Wybór CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Balansuje parę (lub maksymalnie 4) kanałów, tak aby poruszały się zgodnie —
np. klapy, które nie pracują równo, mogą wywoływać niepożądany przechył;
niezbalansowane silniki w modelu wielosilnikowym mogą wywoływać niepożądane
odchylenie. Ethos tworzy krzywą różnicowania balansu dla każdego wybranego
kanału; porównanie fizycznych położeń powierzchni sterowych w każdym punkcie
krzywej pozwala je dopasować, uzyskując idealnie zgodną pracę powierzchni.

**Przed balansowaniem**, w kolejności:

1. Ustaw kierunki serw dla prawidłowego wychylenia.
2. Przy miksach w położeniu neutralnym opcjonalnie użyj **Środka PWM**, aby
   ustawić orczyki serw prostopadle.
3. Ustaw Min/Max oraz Subtrim.
4. Skonfiguruj wszelkie pozostałe krzywe.
5. Skonfiguruj Spowolnienie.
6. *Dopiero potem* zbalansuj i wyrównaj w całym zakresie wychyleń.

**Użycie**: wybierz kanały do zbalansowania oraz kolejność ich wyświetlania —

![Wybrane CH7/CH6](../assets/model-outputs-balance-ch7-and-ch6.png)

— wartość miksu na osi X, różnicowa korekta balansu na osi Y. Dotknij wykresu
kanału (lub zaznacz go i naciśnij `ENT`), aby edytować jego krzywą balansu;
`PAGE` przełącza pomiędzy kanałami w trakcie edycji:

![Edytor krzywej balansu](../assets/model-outputs-balance-curve-edit.png)

Elementy sterujące edytora:

- **Źródło** — zwykle własne źródło (źródła) miksu lub dowolne inne wygodne
  wejście analogowe; **Automatyczne wejście analogowe** przechwytuje jako oś X
  pierwszy poruszony drążek/suwak/potencjometr, zarówno na wykresie, jak
  i w samym modelu.
- **Magnes** — automatycznie przyciąga regulację enkoderem obrotowym do
  najbliższego punktu krzywej na osi X:

  ![Magnes wyłączony](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Magnes włączony](../assets/model-outputs-balance-ch6-magnet-on.png)

  Wejście nadal trzeba poruszyć, aby ustawić X na punkcie krzywej przed jego
  regulacją.
- **Blokada** — przełączana dotknięciem ikony lub naciśnięciem `ENT` w trybie
  edycji wykresu; blokuje wszystkie wejścia, dzięki czemu można puścić drążek
  i obserwować powierzchnie sterowe podczas modyfikowania krzywej.
- **Konfiguracja** — zmiana liczby punktów dla kanału (wszystkich lub
  pojedynczo) oraz tego, czy dana krzywa jest wygładzana.
- **Pomoc** (`?`, także klawisz `MDL`) — otwiera wbudowaną pomoc.

**Wielokanałowo**: jednocześnie można zbalansować do 4 kanałów —

![Balansowanie 4 kanałów](../assets/model-outputs-balance-ch2-9-8-1.png)

Po ustawieniu krzywą balansu można przejrzeć, edytować lub usunąć na stronie
konfiguracji danego kanału — ikona balansu oznacza ją na wykresie kanału
(obok ikony Kierunku, jeśli ten również jest niedomyślny).
