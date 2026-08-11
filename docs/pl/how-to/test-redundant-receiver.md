---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Test konfiguracji odbiornika redundantnego

Redundancja ma sens tylko wtedy, gdy zostanie faktycznie przetestowana przed lotem —
przyjmujemy, że [odbiornik redundantny](../model-setup/rf-system.md#redundant-receivers)
jest już skonfigurowany.

!!! note "Zrzuty ekranu w przygotowaniu"
    Ta strona nie zawiera jeszcze zrzutów ekranu z symulatora — zobacz [Proces
    tworzenia zrzutów ekranu](../contributing/screenshot-pipeline.md).

## A. Test w warunkach rzeczywistych

Gdy odbiornik główny pracuje na 2,4 GHz, a redundantny na 900 MHz, uruchom
[Test zasięgu](../model-setup/rf-system.md#range-check) i oddalaj się od
modelu, aż nastąpi utrata łącza 2,4 GHz (po przekroczeniu alarmu RSSI Critical).
W tym momencie kontrolę powinien przejąć redundantny odbiornik 900 MHz.

## B. Test na stole

1. **Sprawdź normalną konfigurację** — oba odbiorniki zbindowane, obie diody
   LED świecą na zielono, sterowanie działa prawidłowo.
2. **Zbinduj odbiornik główny do innego Model ID** — utwórz tymczasowy
   model testowy (np. „TestRx") z innym Model ID i zbinduj z nim
   *główny* odbiornik. Wróć do testowanego modelu: dioda LED głównego
   odbiornika powinna teraz świecić na **czerwono** (zbindowany gdzie indziej),
   a dioda odbiornika redundantnego pozostaje **zielona** — sterowanie
   nadal powinno działać, co dowodzi, że sam odbiornik redundantny
   utrzymuje model w stanie zdatnym do lotu.
3. **Zbinduj ponownie odbiornik główny** z jego normalnym Model ID. Przed
   uznaniem testu za zakończony upewnij się, że obie diody LED znów świecą
   na zielono, a sterowanie działa prawidłowo.
