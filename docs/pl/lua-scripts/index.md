---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Skrypty Lua

Skrypty Lua pozwalają tworzyć własne [widgety wyświetlacza](../displays/custom-widgets.md),
prezentujące informacje, których Ethos natywnie nie obsługuje, a także (dla każdego modelu)
własne [źródła i zadania](../model-setup/lua-scripts.md) — jest to podstawa, która ma być
dalej rozwijana, w kierunku specjalizowanych funkcji własnych oraz integracji z kontrolerami
lotu.

Samo Lua jest lekkim, osadzalnym językiem skryptowym ogólnego przeznaczenia (stosowanym
wszędzie, od gier po aplikacje internetowe); Ethos osadza go właśnie z myślą o tego typu
personalizacji nadajnika.

!!! warning
    Skrypty Lua wydłużają czas uruchamiania nadajnika. Opóźnienie powodowane przez dobrze
    napisany skrypt powinno być niezauważalne — źle napisany skrypt może opóźnić start
    niemal w nieskończoność.

- [Interpreter Lua](lua-interpreter.md) — jaką wersję Lua i jakie biblioteki
  osadza Ethos.
- [Dokumentacja Lua dla Ethos](ethos-lua-documentation.md) — gdzie znajduje się
  pełna dokumentacja API.
- [Lokalizacje przykładowych skryptów](example-script-locations.md) — gdzie znaleźć
  i pobrać działające przykłady.
- [Ograniczenia konfiguracji](configuration-limits.md) — limity pamięci dla
  bitmap i skryptów.
- [Podstawowy układ widgetu](basic-widget-layout.md) — struktura kodu wymagana
  przez skrypt własnego widgetu.
