---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lista kontrolna

![Lista kontrolna](../assets/model-checklist.png)

Zestaw przedstartowych kontroli bezpieczeństwa uruchamianych przy włączeniu
nadajnika i/lub po wczytaniu modelu. Wbudowane kontrole obejmują tryb cichy,
nieustawiony failsafe, położenia przełączników/potencjometrów, akumulator
nadajnika oraz baterię RTC — kontrola przełączników pokazuje, w którym
kierunku należy przestawić każdy przełącznik, co jest oznaczone czerwonymi
kropkami na ekranie ostrzeżenia:

![Lista kontrolna przy starcie](../assets/model-checklist-at_start.png)

!!! note
    Zarówno `OK`, jak i `RTN` całkowicie pomija kontrole przedstartowe,
    niezależnie od tego, co sugeruje ostrzeżenie na ekranie.

## Kontrola gazu

![Funkcja kontroli](../assets/model-checklist-check_function.png)

Włącz i wybierz operator — `<` (mniejsze niż), `~` (w przybliżeniu równe)
lub `>` (większe niż) — względem wartości; ostrzeżenie pojawia się, gdy
drążek gazu znajduje się poza zakresem dopuszczonym przez to porównanie.

## Kontrola failsafe

Ostrzega, jeśli [failsafe](rf-system.md#failsafe) nie został ustawiony dla
bieżącego modelu.

!!! tip
    Zdecydowanie zalecane jest pozostawienie tej opcji włączonej.

## Kontrola przełączników

![Przełączniki](../assets/model-checklist-switches.png)
![Opcje kontroli przełącznika](../assets/model-checklist-switches-options.png)

Dla każdego przełącznika można wymagać określonego położenia przy starcie
(przełączniki z własnymi nazwami z [Ustawień systemu →
Sprzęt](../system-setup/hardware.md#switches-settings) są wyświetlane pod
tymi nazwami). **Wczytaj wszystkie położenia przełączników** przechwytuje
*bieżące* fizyczne położenia jako wymagane dla każdego przełącznika, który
nie został oznaczony jako **Brak kontroli**.

## Kontrola przełączników funkcyjnych

![Przełączniki funkcyjne](../assets/model-checklist-function-switches.png)
![Opcje kontroli przełącznika funkcyjnego](../assets/model-checklist-function-switches-options.png)

Ta sama zasada, zastosowana do sześciu [przełączników
funkcyjnych](model-edit.md#function-switches). **Wczytaj wszystkie położenia
przełączników funkcyjnych** działa tak samo jak powyżej.

## Kontrola potencjometrów / suwaków

![Potencjometry](../assets/model-checklist-pots.png)
![Opcje kontroli potencjometru](../assets/model-checklist-pots-options.png)

Wymaga określonych położeń potencjometrów/suwaków przy starcie, indywidualnie
dla każdego elementu sterującego (`~`/`<`/`>`, tak jak w kontroli gazu).
**Wczytaj wszystkie położenia potencjometrów** przechwytuje bieżące położenia
automatycznie — należy następnie dokładnie sprawdzić automatycznie wybrane
operatory, ponieważ `~` w porównaniu z `<`/`>` może nie odpowiadać rzeczywistym
zamierzeniom.

## Tekst zdefiniowany przez użytkownika

![Tekst listy kontrolnej użytkownika](../assets/model-checklist-user-checklist.png)

Wyświetla plik tekstowy zwykły lub wzbogacony jako część startowej listy
kontrolnej, po zainstalowaniu go dla danego modelu. Pełną procedurę
konfiguracji opisano w [Poradniku: Lista kontrolna z tekstem zdefiniowanym
przez użytkownika](../how-to/user-defined-checklist.md).
