---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Timery

![Timery](../assets/model-timers.png)

Osiem w pełni programowalnych timerów, z których każdy odlicza w górę lub
w dół. Nowy dodasz przyciskiem **+** obok nagłówków kolumn albo poleceniem
**Dodaj** poniżej. Dotknięcie timera otwiera opcje resetowania, edycji,
dodawania, przenoszenia oraz kopiowania i wklejania.

![Edycja timera](../assets/model-timer1-edit.png)

## Pola wspólne (odliczanie w dół i w górę)

- **Wartość** — bieżące wskazanie timera.
- **Nazwa** — do edycji.
- **Tryb** — **W górę** lub **W dół**.
- **Wartość początkowa** (tylko odliczanie w dół) — wartość, od której
  następuje odliczanie.
- **Wartość alarmu** (tylko odliczanie w górę) — wartość, po osiągnięciu
  której timer uznaje się za upłynięty; odlicza dalej powyżej niej, ale
  w widgetach timera wyświetla się na czerwono.
- **Warunek startu** — uruchamia timer. Jeśli **Warunek zatrzymania**
  pozostaje domyślny, sam warunek startu steruje uruchomieniem *i*
  zatrzymaniem. W przeciwnym razie timer startuje przy pierwszym spełnieniu
  warunku startu i od tego momentu działa nieprzerwanie.
- **Warunek zatrzymania** — jeśli nie pozostawiono wartości domyślnej,
  steruje timerem po jego uruchomieniu: zatrzymany, gdy warunek jest
  prawdziwy, działający, gdy jest fałszywy. W poniższym przykładzie timer
  startuje, gdy `ThrottleActive` staje się prawdziwy, i zatrzymuje się, gdy
  telemetria przestaje być aktywna:

  ![Warunek zatrzymania](../assets/model-timer1-edit-stop.png)

- **Proporcjonalne źródło odliczania** — `---` oznacza odliczanie w czasie
  rzeczywistym. Dowolne inne źródło (np. drążek gazu lub kanał gazu) skaluje
  szybkość timera: przy −100% timer jest zatrzymany, przy +100% działa
  z szybkością rzeczywistą, a pomiędzy tymi wartościami skaluje się
  proporcjonalnie.
- **Reset** — przełącznik, przełącznik funkcyjny, przełącznik logiczny lub
  pozycja trymu, która zeruje timer; timer pozostaje wyzerowany tak długo,
  jak warunek jest spełniony.
- **Trwały** — zachowuje wartość timera po wyłączeniu zasilania lub zmianie
  modelu i wczytuje ją przy kolejnym użyciu modelu.
- **Głos** — [pakiet głosowy](../system-setup/general.md#audio-settings),
  który zapowiada ten timer.

## Akcje dźwiękowe

![Dodawanie akcji dźwiękowej](../assets/model-timer1-add-action.png)
![Typ akcji](../assets/model-timer1-action-type-select.png)
![Akcja odliczania](../assets/model-timer1-action-countdown.png)

W pełni elastyczna konfiguracja powiadomień dla każdego timera z osobna.
Każda akcja ma swój typ — **Odliczanie** (zapowiedzi głosowe),
**Odliczanie sygnałem** (sygnały dźwiękowe zamiast mowy),
**Odtwórz plik** lub **Odtwórz wartość** — oraz parametry:

- **Start** — wartość, od której rozpoczyna się odliczanie danej akcji.
- **Krok** — odstęp między zapowiedziami, maksymalnie 10 minut (600 s).
- **Wibracja** — zapowiedzi towarzyszy wibracja.

Typowy zestaw trzech akcji:

![Podsumowanie akcji](../assets/model-timer1-actions-summary.png)
![Akcje timera 2](../assets/model-timer2-actions-summary.png)

1. Odliczanie głosowe rozpoczynane 2:00 przed końcem, co 30 s, z wibracją.
2. Odliczanie sygnałem dźwiękowym rozpoczynane 0:10 przed końcem, co 1 s,
   z wibracją.
3. Własny plik (np. `timer-1-elapsed`) odtwarzany po upłynięciu czasu,
   z wibracją.

Kolejne akcje dodasz poleceniem **Dodaj**; lista działa w kolejności
priorytetów, przy czym **najwyższy priorytet ma pozycja ostatnia**.

Zobacz również [widget wyświetlacza Dziennik timera](../displays/index.md#widget-types),
który prowadzi bieżący dziennik poprzednich przebiegów timera.

![Widget timera](../assets/model-timers-widget.png)
