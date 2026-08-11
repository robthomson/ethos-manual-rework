---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Benutzerdefinierte Widgets

Über die [integrierten Widget-Typen](index.md) hinaus können Lua-Skripte
auch vollständig eigene Widgets bereitstellen — in der Regel eine einzelne
Datei `main.lua`, die in einem Unterordner liegt, der nach der jeweiligen
Funktion benannt ist.

## Ein Widget installieren

Kopieren Sie den Unterordner des Widgets in den Ordner `scripts/` auf der
SD card/eMMC (siehe
[Dateimanager](../system-setup/file-manager.md#top-level-folders)). Das
Widget registriert sich beim nächsten Start automatisch und erscheint von da
an in der Kategorieauswahl **Widget wechseln** unter [Bildschirme
konfigurieren](additional-displays.md) neben den integrierten Typen — die
Konfiguration erfolgt auf genau die gleiche Weise.

## Ein Widget schreiben

Im Abschnitt [Lua-Skripte → Grundlegender Widget-Aufbau](../lua-scripts/basic-widget-layout.md)
finden Sie die Code-Struktur, die ein Widget-Skript umsetzen muss.
