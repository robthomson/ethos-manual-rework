---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Hauptansichten

## Startbildschirm

![Startbildschirm](../assets/mainview.png)

Der Startbildschirm ist das, was Sie sehen, wenn kein Menü geöffnet ist — ein Stapel
von bis zu **acht** Anzeigebildschirmen, die Sie selbst konfigurieren (siehe
[Anzeigen](../displays/index.md)) und zwischen denen Sie mit der Taste `PAGE`
oder per Wischgeste blättern. Ein neu angelegtes Modell beginnt mit nur einem
Bildschirm, der ein Modellbild, drei Timer-Widgets sowie die Trimmungs- und
Potentiometeranzeigen zeigt; alles darauf ist von dort aus frei konfigurierbar.

Bildschirme verwenden normalerweise die unten beschriebene obere und untere
Leiste gemeinsam, ein Bildschirm kann jedoch auch auf Vollbild gesetzt werden,
wodurch beide ausgeblendet werden.

## Die obere Leiste

Die obere Leiste zeigt links den Modellnamen (sowie die aktive Flugphase, sofern
eine konfiguriert ist) und rechts eine Reihe von Statussymbolen:

- Datenaufzeichnung aktiv
- Trainer-Status (Master oder Slave, je nach Fall)
- RSSI — 2,4-GHz-Verbindung
- RSSI — 900-MHz-Verbindung (sofern ein Dualband-/Long-Range-Modul eingebaut ist)
- Lautstärke
- Akkustatus des Senders

Durch Berühren des Lautsprecher- oder Akkusymbols gelangen Sie direkt zum
zugehörigen Einstellungsbereich [Allgemein](../system-setup/general.md) (Audio)
bzw. [Akku](../system-setup/battery.md).

### Fehlerwarnung

Ein rotes Dreieck erscheint in der oberen Leiste, sobald Ethos einen Fehler
erkennt — ein Lua-Skriptfehler, ein RAM-Backup-Fehler oder der Betrieb einer
Nightly-/instabilen Firmware-Version sind die häufigsten Ursachen. Die Details
zu der Warnung finden Sie stets unter **System → Info**, auf derselben Seite wie
die Betriebszeit des Senders und die
[Fehlerprotokolle](../system-setup/information.md).

## Die untere Leiste

![Untere Leiste](../assets/bottombar.png)

Am unteren Rand befinden sich vier Reiter für die obersten Bereiche — **Start**,
**Modellkonfiguration**, **Bildschirme konfigurieren**, **Systemeinstellungen** —
sowie rechts die Systemuhr (Berühren führt direkt zu
[Datum & Uhrzeit](../system-setup/date-and-time.md)).

## Der Widget-Bereich

Die Mitte jedes Bildschirms wird von **Widgets** ausgefüllt: Modellbild, Timer,
Telemetrieanzeigen, Trimmungs- und Potentiometerbalken und mehr, alle von Ihnen
platziert und konfiguriert. Unter [Anzeigen](../displays/index.md) erfahren Sie,
wie Sie Widgets hinzufügen, verschieben und konfigurieren, und unter
[Zusätzliche Anzeigen](../displays/additional-displays.md), wie Sie mehr als den
standardmäßig vorhandenen einzelnen Bildschirm anlegen.
