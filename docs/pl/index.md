---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Podręcznik Ethos

**Ethos** to system operacyjny działający na nadajnikach FrSky z rodziny Ethos
(X20S, X20 Pro, X20 Pro AW, X18S i innych). Niniejszy podręcznik obejmuje konfigurację
modelu od podstaw, ustawienia systemowe nadajnika,
tworzenie własnych ekranów telemetrii oraz środowisko skryptowe Lua, które
działa ponad tym wszystkim.

!!! note "Prace w toku"
    Podręcznik został zbudowany od nowa w oparciu o oficjalny podręcznik Ethos 1.6.3
    oraz istniejący zestaw zrzutów ekranu. Kilka stron (Ethos
    Suite, System RF oraz kilka poradników) jest kompletnych, ale nie
    posiada jeszcze zrzutów ekranu — zobacz [Proces tworzenia zrzutów
    ekranu](contributing/screenshot-pipeline.md) oraz
    [Współtworzenie](contributing/index.md), jeśli chcesz pomóc.

## Od czego zacząć

- Zaczynasz przygodę z Ethos? Rozpocznij od [Pierwszych kroków](getting-started/index.md) —
  układ ekranu głównego i zasady nawigacji, zanim zmienisz jakiekolwiek
  ustawienia.
- Konfigurujesz nowy nadajnik? Zobacz [Ustawienia systemu](system-setup/index.md), gdzie
  opisano jednorazowe ustawienia obejmujące cały nadajnik (kalibracja sprzętu, alarmy, akumulator).
- Programujesz model? [Konfiguracja modelu](model-setup/index.md) obejmuje miksy,
  wyjścia, tryby lotu i wszystko inne, co jest zapisywane per model, a
  [Samouczki](tutorials/index.md) krok po kroku prowadzą przez budowę modeli klasycznych,
  latających skrzydeł i helikopterów.
- Tworzysz ekran telemetrii? Zobacz [Wyświetlacze](displays/index.md).
- Chcesz szybko rozwiązać konkretne zadanie? Sprawdź [Poradniki](how-to/index.md).
- Piszesz lub instalujesz skrypty/widgety Lua? Zobacz [Skrypty Lua](lua-scripts/index.md).

## Obsługiwane nadajniki

Podręcznik został napisany przede wszystkim w oparciu o **X20S**, a różnice
specyficzne dla poszczególnych nadajników (X20 Pro, X20 Pro AW, X18S) wskazano w
[Uwagach dotyczących nadajnika](radio-notes/index.md) tam, gdzie interfejs użytkownika się różni.
