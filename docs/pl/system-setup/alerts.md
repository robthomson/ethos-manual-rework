---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Alerty

![Alerty](../assets/system-alerts.png)

Cztery ostrzeżenia obejmujące cały nadajnik, każde włączane niezależnie — odrębne od
[funkcji specjalnych](../model-setup/special-functions.md)
i [przełączników logicznych](../model-setup/logical-switches.md) definiowanych dla poszczególnych modeli.

- **Tryb cichy** — komunikat głosowy przy uruchomieniu, gdy ta kontrola jest włączona,
  a [Ogólne → Tryb audio](general.md) jest ustawiony na Cichy — jako przypomnienie, że
  nadajnik jest wyciszony.
- **Napięcie główne** — „Radio battery is low”, gdy napięcie głównego akumulatora nadajnika
  spadnie poniżej progu **Niskie napięcie** ustawionego w sekcji [Akumulator](battery.md).
- **Napięcie RTC** — „RTC battery is low”, gdy napięcie baterii pastylkowej RTC spadnie
  poniżej 2,5 V (próg domyślny). Rejestrowanie danych opiera się na zegarze czasu
  rzeczywistego; nieprawidłowy czas utrudnia odczyt logów, zwłaszcza rozróżnienie
  poszczególnych sesji lotów. Ostrzeżenie można tymczasowo wyciszyć w oczekiwaniu na
  wymianę baterii, ale nie należy pozostawiać go wyłączonego na stałe.
- **Ostrzeżenie o konflikcie czujników** — wykrywa konflikty identyfikatorów czujników
  telemetrycznych. Wyłączenie ma sens tylko wtedy, gdy używasz czujników niezgodnych ze
  specyfikacją S.Port.
- **Bezczynność** — komunikat głosowy „Prolonged inactivity” (wraz z wibracją, na wypadek
  ściszenia głośności) po tym, jak nadajnik pozostaje nieużywany dłużej niż przez
  skonfigurowany czas — domyślnie 10 minut.
