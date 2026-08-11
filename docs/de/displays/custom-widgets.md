---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Benutzerdefinierte Widgets

Über die [integrierten Widget-Typen](index.md) hinaus können Lua-Skripte
vollständig benutzerdefinierte Widgets bereitstellen — typischerweise eine
einzelne Datei `main.lua`, die in einem Unterordner mit einem der Funktion
entsprechenden Namen abgelegt ist.

## Installation

Kopieren Sie den Unterordner des Widgets in den Ordner `scripts/` auf der
SD card/eMMC (siehe
[Dateimanager](../system-setup/file-manager.md#top-level-folders)). Das
Widget registriert sich beim nächsten Start automatisch und erscheint
fortan in der Kategorieauswahl **Widget wechseln** unter [Bildschirme
konfigurieren](additional-displays.md) neben den integrierten Typen — die
Konfiguration erfolgt auf genau dieselbe Weise.

## Eigene Widgets erstellen

Unter [Lua-Skripte → Grundlegender Widget-Aufbau](../lua-scripts/basic-widget-layout.md)
finden Sie die Code-Struktur, die ein Widget-Skript implementieren muss.
