---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Nouzový režim

Nouzový režim je reakcí Ethos na neočekávanou nízkoúrovňovou závadu, například
na reset od watchdogu. Watchdog je časovač, který je průběžně restartován
různými částmi systému; pokud něco jeho restartování zabrání, časovač vyprší
a vyvolá hardwarový reset. Nouzový režim poté restartuje vysílač co nejrychleji,
přičemž vynechá všechny běžné kontroly při spuštění, takže je řízení modelu
předáno zpět s minimálním zdržením. SD card/eMMC se v tomto režimu vůbec
nepoužívá.

Dostupné jsou pouze základní funkce nezbytné pro udržení kontroly nad modelem —
žádné funkce vyšší úrovně. Obrazovka je prázdná až na text **EMERGENCY MODE**,
doprovázený opakovaným 300ms pípnutím každé 3 sekundy; hlasová hlášení, Lua
skripty, logování a telemetrie se zcela zastaví. Pokud k tomu dojde ve vzduchu,
přistávejte co nejdříve.

Nejčastější příčinou je porucha SD card.

## Testování nouzového režimu

Pro záměrné vyvolání nouzového režimu za účelem testování lze přidat
**Systémový nástroj**, abyste se s tímto režimem nemuseli poprvé setkat až
za letu. Klepnutím na ikonu Emergency Test se zobrazí výzva k potvrzení a poté
se vysílač přepne do nouzového režimu přesně tak, jako při skutečné závadě.
