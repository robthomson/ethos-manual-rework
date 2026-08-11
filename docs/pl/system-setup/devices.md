---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Urządzenia

![Urządzenia](../assets/system-devices.png)

W menu pozycja ta nosi nazwę **Device config** — narzędzia do konfiguracji urządzeń peryferyjnych podłączonych przez S.Port/FBUS: czujników, odbiorników, „gas suite", serw, VTX oraz ESC. Pozycja **DIY sensors** pojawia się automatycznie po wykryciu czujnika DIY. Szczegółowe informacje znajdują się w instrukcjach poszczególnych urządzeń; niniejsza strona opisuje elementy wspólne dla wszystkich.

!!! note
    Nie ma to związku z wyborem modułu RF (wewnętrznego lub zewnętrznego), przez który nadaje dany *model* — jest to ustawienie indywidualne dla modelu, opisane w rozdziale [System RF](../model-setup/rf-system.md).

Device Config jest rozszerzalny: zarówno użytkownicy, jak i FrSky mogą dodawać tutaj strony za pomocą skryptów Lua.

## Zmiana przypisania identyfikatorów czujników

Ekrany Device config w Ethos umożliwiają bezpośrednią zmianę **Physical ID** oraz **Application ID** urządzenia w magistrali S.Port. Jeśli posiadasz więcej niż jedno urządzenie o tej samej funkcji, podłączaj je **pojedynczo**: wykryj każde z nich w menu [Telemetria → Wykryj nowe czujniki](../model-setup/telemetry.md), zmień jego Physical ID i Application ID tutaj, w Device config, a następnie wróć i wykryj je ponownie pod nowym identyfikatorem.

## Przykład: odbiorniki

![Wybór modułu](../assets/system-devices-module-choice.png)

Odbiorniki stabilizowane FrSky można konfigurować w tym miejscu po zainstalowaniu odpowiedniego skryptu Lua (jedno kliknięcie w bibliotece Lua w Ethos Suite). Dostępne są dwie ścieżki konfiguracji, zależne od generacji odbiornika:

- **Stabilizer config** — nowsze odbiorniki z funkcją „Advanced stabilization" (regulacja czułości na kanale 13). Udostępniane są dwie niezależne grupy stabilizacji: Grupa 1 obejmuje kanały 1–6, Grupa 2 obejmuje kanały 7–11 — wyłącz Grupę 2, jeśli nie używasz pinów 7–11 do stabilizacji. Wbudowana jest kalibracja 6-osiowa, którą należy wykonać jednokrotnie na nowym odbiorniku oraz ponownie po każdej aktualizacji firmware'u do wersji v3.0.x (po przywróceniu ustawień fabrycznych). W ramach kalibracji każdej grupy dawny krok „self-check" został zastąpiony niezależną kalibracją poziomu modelu, punktu neutralnego kanału oraz punktów krańcowych kanału, a każdy kanał można indywidualnie włączyć lub wyłączyć. Konfiguracje (ale nie dane kalibracyjne) można zapisywać na komputerze i z niego przywracać.
- **SxR** — starsze odbiorniki, w tym urządzenia z poprzednich generacji oraz Archer/Archer Pro, a także odbiorniki takie jak SR10 Pro, które (mimo nazwy „SRx") mają regulację czułości na kanale 9, a nie 13.

  ![Bieżące urządzenie](../assets/system-devices-current.png)

!!! warning "Po aktualizacji firmware'u odbiornika do wersji v3.0.x"
    Wykonaj przywrócenie ustawień fabrycznych (dostępne w opcjach odbiornika w konfiguracji RF), następnie ponownie zbinduj i skonfiguruj odbiornik od podstaw — w szczególności funkcje stabilizacji oraz kalibrację 6-osiową. Jest to wymagane z powodu nowej funkcji zapisu danych failsafe wprowadzonej w wersji v3.0.x; po zakończeniu dokładnie sprawdź działanie funkcji failsafe.

FrSky North America publikuje szczegółowy przewodnik konfiguracji odbiorników stabilizowanych, a Juan Sanchez Garcia, pilot zespołu FrSky, przygotował film instruktażowy obejmujący ten sam zakres zagadnień.

## Konfiguracja przez złącze S.Port nadajnika

Urządzenia S.Port i FBUS można także konfigurować bezpośrednio przez złącze S.Port na górze nadajnika, bez pośrednictwa zbindowanego odbiornika.

1. Podłącz urządzenie do złącza S.Port nadajnika (przewód biały/żółty od strony wycięcia).
2. Przejdź do **System → Device config**, przewiń do wybranego urządzenia (np. czujnika prądu FAS40 ADV) i naciśnij `ENT`.
3. Na stronie konfiguracji ustaw **Module** na **S.Port connector**.
4. Wprowadź zmiany — Physical ID oraz Application ID muszą być unikalne — następnie przewiń w dół i wybierz **Save to flash**.

Dotyczy to zarówno urządzeń FBUS (zobacz także [Poradnik: konfiguracja systemu FBUS](../how-to/fbus-setup.md)), jak i zwykłych urządzeń S.Port, takich jak wariometr.
