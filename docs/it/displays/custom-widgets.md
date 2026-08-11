---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widget personalizzati

Oltre ai [tipi di widget integrati](index.md), gli script Lua possono realizzare
widget completamente personalizzati — in genere un singolo file `main.lua` contenuto
in una sottocartella il cui nome ne indica la funzione.

## Installazione

Copiare la sottocartella del widget in `scripts/` sulla SD card/eMMC (vedere
[Gestione file](../system-setup/file-manager.md#top-level-folders)). Il widget
si registra automaticamente al successivo avvio e, da quel momento, compare nel
selettore di categoria **Cambia widget** in [Configura
schermate](additional-displays.md) insieme ai tipi integrati — e si configura
esattamente allo stesso modo.

## Creazione

Consultare [Script Lua → Struttura base di un widget](../lua-scripts/basic-widget-layout.md)
per la struttura del codice che uno script widget deve implementare.
