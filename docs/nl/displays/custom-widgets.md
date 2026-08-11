---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Aangepaste widgets

Naast de [ingebouwde widgettypen](index.md) kunnen Lua-scripts volledig
aangepaste widgets implementeren — doorgaans één enkel `main.lua`-bestand dat
in een submap staat met een naam die de functie beschrijft.

## Een widget installeren

Kopieer de submap van de widget naar `scripts/` op de SD card/eMMC (zie
[Bestandsbeheer](../system-setup/file-manager.md#top-level-folders)). De widget
registreert zichzelf automatisch bij de volgende keer opstarten en verschijnt
vanaf dat moment in de categoriekiezer **Widget wijzigen** in [Schermen
configureren](additional-displays.md), naast de ingebouwde typen — en wordt op
precies dezelfde manier geconfigureerd.

## Een widget schrijven

Zie [Lua-scripts → Basisopbouw van een widget](../lua-scripts/basic-widget-layout.md)
voor de codestructuur die een widgetscript moet implementeren.
