---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Tryby lotu

![Tryby lotu](../assets/model-fm.png)

Tryby lotu (fazy lotu) pozwalają przełącznikowi wybierać pomiędzy różnymi
zachowaniami tego samego modelu — szybowce mogą używać trybów Start/Przelot/
Szybkość/Termika, samoloty silnikowe Normalny/Start/Lądowanie, a helikoptery
Normalny (rozkręcanie wirnika, start/lądowanie) / Idle Up 1 (akrobacja) /
Idle Up 2 (3D). Zdejmują one z pilota większość obciążenia związanego
z ręcznym przełączaniem i korygowaniem trymów: tryb lotu może mieć własne,
niezależne trymy oraz może warunkować zarówno [Zmienne](variables.md), jak
i [Miksy](mixes.md) — razem daje to wystarczające możliwości do budowy
naprawdę złożonych konfiguracji. Zobacz [Podstawowy przykład dla modelu
stałopłata](../tutorials/basic-fixed-wing.md), aby poznać zastosowanie trybów
lotu w rzeczywistym modelu.

Domyślnie nie zdefiniowano żadnych trybów lotu. Dotknij domyślnego trybu lotu
i wybierz **Edytuj**, aby zmienić jego nazwę, albo **Dodaj**, aby utworzyć
nowy — łącznie do 20.

## Nazwa

Opisowa nazwa — Przelot, Szybkość, Termika, Start, Lądowanie, dowolna
pasująca.

## Warunek aktywacji

![Formularz trybu lotu](../assets/model-fm-form.png)

Nowy tryb lotu jest początkowo nieaktywny (`---`). Po ustawieniu może być
sterowany położeniem przełącznika lub przycisku, przełącznikiem funkcyjnym,
przełącznikiem logicznym, zdarzeniem systemowym (odcięcie gazu / blokada gazu)
lub położeniem trymu.

**Domyślny** tryb lotu nie ma w ogóle warunku aktywacji — jest aktywny zawsze
wtedy, gdy nie jest spełniony warunek żadnego innego trybu lotu. W danej chwili
aktywny jest tylko jeden tryb lotu: pierwszy (w kolejności priorytetów),
którego warunek jest aktualnie prawdziwy. Aktywny tryb wyświetlany jest
pogrubioną czcionką.

!!! warning "Dodawanie trybu lotu do istniejącego modelu"
    Nowo dodany tryb lotu jest domyślnie aktywny w każdym miksie, który już
    jest zależny od trybów lotu — sprawdź, czy każdy taki miks nadal działa
    poprawnie, w szczególności miks **Lock** blokujący kanał na określonym
    trybie lotu.

## Narastanie, zanikanie

Czasy przejścia zapewniające płynne przenikanie pomiędzy trybami lotu (np.
1 sekunda w każdą stronę) — ma to wpływ wyłącznie na miksy, które same są
zależne od trybów lotu.

## Zarządzanie trybami lotu

![Przenoszenie trybu lotu](../assets/model-fm-move.png)
![Wybór do przeniesienia](../assets/model-fm-move-select.png)
![Tryby 0-3](../assets/model-fm-0to3.png)

Dotknij trybu lotu, aby wybrać **Edytuj**, **Dodaj**, **Klonuj** lub
**Usuń**. **Sklonowany** tryb lotu dziedziczy ustawienia trybu źródłowego
w każdym miksie korzystającym z trybów lotu — takie samo zachowanie, taki sam
stan aktywny/nieaktywny — dlatego klon jest domyślnie dodawany jako ostatni
tryb lotu, aby nie kolidował z istniejącymi. **Przenieś** zmienia priorytet
trybu lotu: priorytety obowiązują w kolejności rosnącej i (jak wyżej) aktywny
jest pierwszy tryb, którego warunek jest prawdziwy.
