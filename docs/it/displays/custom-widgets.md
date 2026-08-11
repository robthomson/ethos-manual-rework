---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widget personalizzati

Oltre ai [tipi di widget integrati](index.md), gli script Lua possono realizzare
widget completamente personalizzati: in genere un singolo file `main.lua`
conservato in una sottocartella con un nome che ne suggerisce la funzionalità.

## Installazione

Copia la sottocartella del widget nella cartella `scripts/` della scheda SD o
eMMC (vedi [Gestione file](../system-setup/file-manager.md#top-level-folders)).
Il widget verrà registrato automaticamente al successivo avvio e da quel momento
comparirà nel selettore di categoria **Cambia widget** in [Configura
schermate](additional-displays.md) insieme ai tipi integrati, e potrà essere
configurato esattamente come qualsiasi altro.

## Creazione

Consulta [Script Lua → Layout di base di un widget Lua](../lua-scripts/basic-widget-layout.md)
per la struttura del codice che uno script widget deve implementare.
