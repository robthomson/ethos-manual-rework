---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Edycja modelu

![Edycja modelu](../assets/model-editmodel.png)

Umożliwia edycję parametrów na poziomie modelu, które zostały wstępnie
ustawione przez kreatora — głównie danych identyfikacyjnych, ale także kilku
nadpisań i narzędzi właściwych dla danego modelu.

## Nazwa, obraz

Zmiana nazwy modelu lub jego obrazu; podczas przeglądania obrazów wyświetlana
jest miniatura podglądu.

## Typ modelu

![Typ modelu](../assets/model-edit-modeltype.png)

!!! warning
    Zmiana typu modelu resetuje **wszystkie** miksy.

## Przypisania kanałów

Zmiana typu usterzenia lub (w przypadku helikoptera) typu tarczy sterującej
również resetuje wszystkie miksy. W przypadku pozostałych kanałów można zmienić
przypisaną liczbę kanałów lub usunąć przypisanie.

## Filtr analogowy

![Filtr analogowy](../assets/model-edit-analog-filter.png)

W sekcji [Ustawienia systemu → Sprzęt](../system-setup/hardware.md) dostępny
jest globalny filtr analogowo-cyfrowy, który może ograniczyć drgania wokół
środkowego położenia drążka; niniejsze ustawienie nadpisuje go wyłącznie dla
tego modelu.

![Opcje filtru analogowego](../assets/model-edit-analog-filter-select.png)

## Przełączniki funkcyjne {: #function-switches }

![Przełączniki funkcyjne](../assets/model-edit-fn-switches.png)

Sześć przełączników funkcyjnych jest dostępnych wszędzie tam, gdzie występuje
parametr **Warunek aktywacji**, jednak — w odróżnieniu od zwykłych
przełączników — nie mogą być używane jako źródło ogólnego przeznaczenia.
Konfiguruje się je jako jedną z opcji:

- **6-pozycyjny z OFF** — naciśnięcie przełącznika funkcyjnego zatrzaskuje go
  w pozycji włączonej; ponowne naciśnięcie *tego samego* przełącznika wyłącza
  wszystkie sześć.
- **6-POS** — naciśnięcie przełącznika funkcyjnego zatrzaskuje go w pozycji
  włączonej do momentu naciśnięcia *innego* przełącznika, który przejmuje jego
  funkcję.
- **2 × 3-poz.** — dzieli sześć przełączników na dwie grupy po trzy, z jednym
  aktywnym przełącznikiem w każdej grupie.
- **6 × 2-poz.** — sześć niezależnych przełączników zatrzaskowych wł./wył.
- **Chwilowy** — sześć niezależnych przełączników, każdy aktywny tylko podczas
  przytrzymania.
- **Trwały** — jeśli opcja jest włączona, przełącznik funkcyjny zachowuje swój
  stan po wyłączeniu zasilania lub ponownym wczytaniu modelu zamiast się
  resetować.

![Opcje przełączników funkcyjnych](../assets/model-edit-fn-switches-select.png)

## Złącze SPort

Pin 5V złącza S.Port nadajnika może być przełączany indywidualnie dla każdego
modelu — przydatne na przykład do zasilania zewnętrznego odbiornika w
konfiguracji trenerskiej.

## Czas pracy modelu

![Czas pracy modelu](../assets/model-edit-model-runtime.png)

Rejestruje łączny czas lotów/pracy tego modelu.

## Resetuj wszystkie miksy

![Resetuj wszystkie miksy](../assets/model-edit-model-reset_all_mixes.png)

Przywraca wszystkie miksy modelu do stanu domyślnego.
