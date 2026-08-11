---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Wybór modelu

![Kreator modelu — samolot](../assets/model-modelselect-model-wizard-airplane.png)

Tworzy, wybiera, klonuje i usuwa modele oraz zarządza zdefiniowanymi przez
użytkownika folderami kategorii, w których są one uporządkowane.

## Zarządzanie folderami modeli

![Foldery modeli](../assets/model-modelselect-folders.png)

Ethos pozwala grupować modele we własnych folderach — typowo są to takie
kategorie jak Samolot, Szybowiec, Helikopter, Quad, Warbird, Łódź, Samochód,
Szablon czy Archiwum. Dopóki nie utworzysz żadnego folderu, modele znajdują
się w automatycznym folderze **Uncategorized** (bez kategorii), tworzonym po
aktualizacji do Ethos 1.1.0 alpha 17+ lub gdy plik modelu zostanie skopiowany
do katalogu `\Models` z innego miejsca; Ethos usuwa ten folder, gdy tylko
stanie się pusty.

Aby utworzyć folder, dotknij **+** obok pozycji „Uncategorized” (lub
przytrzymaj `PAGE` w górę/w dół), nadaj mu nazwę (maksymalnie 15 znaków) i
zatwierdź. Foldery są sortowane alfabetycznie, przy czym **Uncategorized**
zawsze znajduje się na końcu, i odpowiadają bezpośrednio podfolderom katalogu
`\Models` na karcie SD/eMMC. Dotknięcie nazwy folderu otwiera opcje zmiany
nazwy/usunięcia — usunięcie folderu przenosi znajdujące się w nim modele z
powrotem do folderu Uncategorized.

![Zmiana folderu](../assets/model-modelselect-folder-change-select.png)

Aby przenieść model, dotknij jego ikony, wybierz **Zmień folder**, a następnie
dotknij folderu docelowego:

![Wybór folderu](../assets/model-modelselect-folder-airplane-select.png)

## Dodawanie nowego modelu

![Tworzenie modelu](../assets/model-modelselect-model-create.png)

Wybierz kategorię, w której ma zostać utworzony model, dotknij **+**, a
następnie **Utwórz model**, aby uruchomić kreatora (jeśli kategoria jeszcze
nie istnieje, utwórz ją najpierw). Dostępne są kreatory dla typów **Samolot**,
**Szybowiec**, **Helikopter**, **Wielowirnikowiec** oraz **Inny**; każdy z nich
prowadzi przez podstawową konfigurację danego typu płatowca, łącznie z
opcjonalnymi, wstępnie zdefiniowanymi miksami dla stabilizowanych odbiorników
FrSky (wzmocnienie, tryb stabilizacji). Nazwy modeli mogą mieć do 15 znaków.

### Odbiorniki stabilizowane i kolejność kanałów

![Kreator: samolot](../assets/model-modelselect-model-wizard-airplane.png)

Stabilizowane odbiorniki FrSky wymagają konkretnie kolejności kanałów
**AETR** — pozostaw [Drążki → Kolejność kanałów](../system-setup/controls.md)
w domyślnym ustawieniu AETR z włączoną opcją **Pierwsze cztery kanały stałe**,
aby wynik pracy kreatora odpowiadał temu, czego oczekuje odbiornik.

Kreator przypisuje kanały od prawej do lewej. Dla 2 lotek + 1 steru wysokości
+ 1 steru kierunku + 1 silnika daje to:

| Kan. | Funkcja |
|---|---|
| 1 | Lotka 1 (prawa lotka) |
| 2 | Ster wysokości |
| 3 | Gaz |
| 4 | Ster kierunku |
| 5 | Lotka 2 (lewa lotka) |

Przy takim przypisaniu różnicowanie lotek jest **dodatnie** w typowym
przypadku (większy wychył w górę niż w dół). Instrukcje odbiorników FrSky
dokumentują obecnie *przeciwną* konwencję (od lewej do prawej, czyli Kan.1 =
lewa lotka, Kan.5 = prawa lotka) — w takim przypadku dla uzyskania tego samego
efektu fizycznego różnicowanie musiałoby być **ujemne**.

!!! tip
    Zaleca się konsekwentne stosowanie konwencji Ethos — wszystkie funkcje
    stabilizacji działają poprawnie w obu przypadkach, ponieważ kierunek
    kompensacji ustawia się podczas konfiguracji stabilizacji. Jeśli
    rzeczywiście musisz dopasować się do konwencji z instrukcji odbiornika,
    najprostszym sposobem jest zbudowanie modelu kreatorem w normalny sposób,
    a następnie użycie funkcji **Zamień kanały** w [Wyjściach](outputs.md), aby
    zamienić miejscami oba kanały lotek — dzięki temu znak różnicowania w
    mikserze lotek pozostaje dodatni.

### Kroki kreatora

![Kreator: typ usterzenia](../assets/model-modelselect-model-wizard-tail.png)
![Kreator: liczba lotek/klap](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Kreator: liczba sterów wysokości/kierunku](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Kreator: napęd](../assets/model-modelselect-model-wizard-engine.png)
![Kreator: zmiana przypisania kanałów](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Kreator: nazwa](../assets/model-modelselect-model-wizard-name.png)
![Kreator: odbiornik](../assets/model-modelselect-model-wizard-rx.png)

W przypadku **Samolotu** po wyborze typu usterzenia i liczby powierzchni
sterowych kreator przechodzi do liczby kanałów napędu, a następnie do liczby
kanałów lotek/klap.

**Konfiguracja usterzenia** to wybór pomiędzy klasycznym usterzeniem
krzyżowym, usterzeniem motylkowym (V) lub brakiem usterzenia (delta/latające
skrzydło):

- **Delta/latające skrzydło** — utworzenie modelu typu Samolot z 2 lotkami i
  bez powierzchni usterzenia automatycznie tworzy miksowanie elevonów, z
  domyślnymi wagami 50%, dzięki czemu jednoczesne pełne wychylenie lotek i
  steru wysokości nadal daje w sumie 100%.
- **Delta z miksowaniem realizowanym przez stabilizowany odbiornik** — wybierz
  zamiast tego 1 lotkę i 1 ster wysokości; miksowanie elevonów odbywa się w
  odbiorniku, zgodnie z jego instrukcją.
- **Delta z osobnymi powierzchniami lotek i steru wysokości** — pozwól
  kreatorowi działać tak, jakby model miał usterzenie; skonfiguruje on
  wymagane kanały lotek i steru wysokości (z lub bez steru kierunku), a
  miksowanie elevonów nie zostanie utworzone.

Krok **zmiany przypisania kanałów** pozwala nadpisać domyślne przypisanie
kreatora, przy czym należy pamiętać, że stabilizowane odbiorniki wymagają
kanałów w określonej kolejności (sprawdź instrukcję odbiornika). Ostatni krok
ustawia nazwę modelu i przypisuje obrazek.

Gotowy model trafia do folderu kategorii, który był aktywny w momencie
uruchomienia kreatora, i jest w nim sortowany alfabetycznie. Pełny przykład
krok po kroku znajdziesz w [Podstawowym przykładzie modelu
stałopłata](../tutorials/basic-fixed-wing.md).

## Odbieranie modelu z innego nadajnika Ethos

![Odbieranie modelu](../assets/model-modelselect-model-receive.png)

Wybierz kategorię docelową, dotknij **+**, a następnie **Odbierz model** —
nadajnik oczekuje na transmisję i wyświetla swój adres Bluetooth, dzięki
czemu urządzenie wysyłające może go odnaleźć. Na nadajniku wysyłającym dotknij
modelu i wybierz **Wyślij model**; nadajnik odbierający przed przyjęciem
poprosi o potwierdzenie przychodzącej nazwy pliku.

## Wybieranie modelu

Dotknij **Wybór modelu**, aby wyświetlić listę modeli.

!!! note "Konwersja modeli po aktualizacji Ethos"
    Ethos konwertuje każdy model indywidualnie przy pierwszym jego *wybraniu*
    po aktualizacji wersji, a nie wszystkie naraz podczas aktualizacji — nie
    powoduje to zauważalnego opóźnienia i jest bezpieczne w dowolnym
    późniejszym momencie, nawet pod jeszcze nowszą wersją Ethos. Data
    **Ostatnia modyfikacja** u dołu ekranu wyboru aktualizuje się w momencie
    wykonania konwersji (lub podczas edycji modelu — w przeciwnym razie
    pozostaje niezmieniona).

**Szybki wybór** — długie dotknięcie lub długie naciśnięcie `ENT` na ikonie
modelu powoduje natychmiastowe przełączenie się na niego.

**Menu zarządzania modelem** — dotknij modelu, aby go podświetlić, a następnie
dotknij ponownie, aby otworzyć menu:

- **Ustaw jako bieżący model**
- **Klonuj** — tworzy duplikat modelu. Klon otrzymuje automatycznie nowy numer
  odbiornika; jeśli zamiast tego przypiszesz mu numer odbiornika oryginału,
  będzie działał bez konieczności ponownego bindowania.
- **Zmień folder**
- **Wyślij**/**Odbierz** — do lub z innego nadajnika, jak opisano powyżej.
- **Usuń** — dostępne tylko dla modelu, który nie jest aktualnie wybrany.
