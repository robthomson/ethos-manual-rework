---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Egendefinerte widgeter

I tillegg til de [innebygde widget-typene](index.md) kan Lua-skript implementere
helt egendefinerte widgeter — vanligvis en enkelt `main.lua`-fil som ligger i en
undermappe navngitt etter hva den gjør.

## Installere en widget

Kopier widgetens undermappe til `scripts/` på SD card/eMMC (se
[Filbehandler](../system-setup/file-manager.md#top-level-folders)). Den
registrerer seg automatisk ved neste oppstart, og vises deretter i
kategorivelgeren **Endre widget** i [Konfigurer
skjermer](additional-displays.md) sammen med de innebygde typene — og
konfigureres på helt samme måte.

## Lage en widget

Se [Lua-skript → Grunnleggende widget-oppsett](../lua-scripts/basic-widget-layout.md)
for kodestrukturen et widget-skript må implementere.
