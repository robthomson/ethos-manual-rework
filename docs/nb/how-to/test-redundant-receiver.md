---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Test av oppsett med redundant mottaker

Redundans er bare verdt å ha hvis den faktisk testes før flyging —
dette forutsetter at en [redundant mottaker](../model-setup/rf-system.md#redundant-receivers)
allerede er konfigurert.

!!! note "Skjermbilder kommer"
    Denne siden har ennå ikke skjermbilder fra simulatoren — se [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## A. Test i praksis

Med hovedmottakeren på 2,4 GHz og den redundante på 900 MHz, start en
[rekkeviddetest](../model-setup/rf-system.md#range-check) og gå bort fra
modellen til 2,4 GHz faller ut (forbi varselet RSSI Critical). Den
redundante 900 MHz-mottakeren skal da ta over kontrollen.

## B. Benketest

1. **Bekreft normalt oppsett** — begge mottakere bundet, begge grønne lysdioder
   lyser, og styringen reagerer normalt.
2. **Bind hovedmottakeren til en annen Model ID** — opprett en midlertidig
   testmodell (f.eks. «TestRx») med en annen Model ID, og bind
   *hovedmottakeren* til den. Bytt tilbake til modellen som testes:
   lysdioden på hovedmottakeren skal nå være **rød** (bundet et annet sted),
   mens lysdioden på den redundante mottakeren fortsatt er **grønn** — og
   styringen skal fortsatt fungere, noe som beviser at den redundante
   mottakeren alene holder modellen flybar.
3. **Bind hovedmottakeren på nytt** til sin normale Model ID. Kontroller at
   begge lysdiodene er grønne igjen og at styringen fungerer før du regner
   testen som fullført.
