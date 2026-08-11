---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Vlastní widgety

Kromě [vestavěných typů widgetů](index.md) mohou Lua skripty implementovat
zcela vlastní widgety — typicky jde o jediný soubor `main.lua` umístěný
v podsložce pojmenované podle jeho funkce.

## Instalace

Zkopírujte podsložku widgetu do složky `scripts/` na SD card/eMMC (viz
[Správce souborů](../system-setup/file-manager.md#top-level-folders)).
Widget se při dalším spuštění zaregistruje automaticky a od té doby se
objeví ve výběru kategorií **Change widget** v [Konfiguraci
obrazovek](additional-displays.md) společně s vestavěnými typy — konfiguruje
se úplně stejným způsobem.

## Vytvoření vlastního widgetu

Struktura kódu, kterou musí skript widgetu implementovat, je popsána v části
[Lua skripty → Základní rozvržení widgetu](../lua-scripts/basic-widget-layout.md).
