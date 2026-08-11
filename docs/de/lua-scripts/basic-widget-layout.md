---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Grundlegender Widget-Aufbau

Ein eigenes Lua-Widget (siehe [Eigene Widgets](../displays/custom-widgets.md)
zur Installation) besteht aus einer kleinen Anzahl benannter Felder bzw.
Handler:

- **`key`** *(String)* — ein eindeutiger Bezeichner für das Widget.
- **`name`** *(String oder Funktion)* — der Anzeigename des Widgets. Entweder
  ein einfacher String oder eine Funktion ohne Argumente, die einen solchen
  zurückgibt — nützlich für einen Namen, der je nach Sprache unterschiedlich
  ausfällt.
- **`create`** *(Funktion)* — wird einmalig beim Erstellen des Widgets ohne
  Argumente aufgerufen. Gibt eine **Widget-Tabelle** zurück, die anschließend
  an alle nachfolgenden Handler übergeben wird — initialisieren Sie hier Ihren
  Zustand und speichern Sie ihn in dieser Tabelle.
- **`configure`** *(Funktion)* — wird aufgerufen, wenn der Benutzer die
  Konfigurationsseite des Widgets öffnet; erhält als einziges Argument die
  Widget-Tabelle aus `create()` und gibt nichts zurück. Erstellen Sie hier das
  Konfigurationsformular und aktualisieren Sie damit die Werte in der
  Widget-Tabelle.
- **`wakeup`** *(Funktion)* — wird in jedem Durchlauf aufgerufen (etwa alle
  50 ms), erhält die Widget-Tabelle und gibt nichts zurück. Prüfen Sie hier,
  ob sich etwas geändert hat; falls ja, rufen Sie `invalidateWindow()` auf, um
  über `paint()` ein Neuzeichnen auszulösen. Halten Sie diesen Handler schnell
  — im Idealfall tut er bei den meisten Aufrufen überhaupt nichts.
- **`event`** *(Funktion)* — wird aufgerufen, wenn das Widget ein Ereignis
  empfängt; Ethos leitet beliebige Ereignisse über diesen Handler an ein
  Widget weiter.
- **`paint`** *(Funktion)* — zeichnet das Widget, erhält die Widget-Tabelle und
  gibt nichts zurück. Wird automatisch aufgerufen, sobald `lcd.invalidate()`
  ausgelöst wurde. Darf vergleichsweise langsam sein, sollte aber dennoch nur
  dann tatsächlich neu zeichnen, wenn sich etwas geändert hat.
- **`read`** *(Funktion, optional)* — liest den dauerhaft gespeicherten
  Widget-Speicher.
- **`write`** *(Funktion, optional)* — schreibt den dauerhaft gespeicherten
  Widget-Speicher.
- **`init`** *(Funktion)* — meldet das Widget und seine Callbacks bei Ethos an.
  Üblicherweise das Letzte im Skript:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` muss über alle installierten Widgets hinweg eindeutig sein; die übrigen
Felder greifen wie oben beschrieben in den Lebenszyklus des Widgets ein.

Skripte liegen unter `scripts/` auf der SD card bzw. dem eMMC, idealerweise in
Ordnern pro Widget organisiert (siehe [Dateimanager](../system-setup/file-manager.md#top-level-folders)
und [Beispielhafte Skript-Speicherorte](example-script-locations.md)). Weitere
ausgearbeitete Beispiele finden Sie im Thread *FrSky ETHOS Lua Script
Programming* auf rcgroups.
