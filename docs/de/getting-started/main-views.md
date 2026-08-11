---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Hauptansichten

## Startbildschirm

![Startbildschirm](../assets/mainview.png)

Der Startbildschirm ist das, was Sie sehen, solange kein Menü geöffnet ist — ein
Stapel von bis zu **acht** Hauptansichten, die Sie selbst konfigurieren können
(siehe [Bildschirme konfigurieren](../displays/index.md)) und zwischen denen Sie
mit der Taste `PAGE` oder mit einer Touch-Wisch-Geste blättern. Ein neu
angelegtes Modell beginnt mit nur einer Ansicht, die ein Modellbild, drei
Stoppuhr-Widgets sowie die Anzeige der Trimmungen und Potis enthält; alles darauf
kann vom Benutzer frei konfiguriert werden.

Die Hauptansichten teilen sich normalerweise die nachfolgend beschriebene obere
und untere Leiste, eine Ansicht kann jedoch auch auf Vollbild gesetzt werden,
wodurch beide ausgeblendet werden.

## Die obere Leiste

In der oberen Leiste wird links der Name des Modells angezeigt (sowie der aktive
Flugmodus, sofern konfiguriert), auf der rechten Seite befindet sich eine Reihe
von Statussymbolen:

- ob die Datenaufzeichnung aktiv ist
- Trainersymbol für Master oder Slave
- RSSI 2.4G
- RSSI 900M (sofern ein Dualband-/Long-Range-Modul eingebaut ist)
- Lautstärke des Lautsprechers
- Batteriezustand des Senders

Wenn Sie die Lautsprecher- oder Batteriesymbole berühren, werden direkt die
entsprechenden Bedienfelder [Allgemein](../system-setup/general.md) (Audio usw.)
bzw. [Batterie](../system-setup/battery.md) angezeigt.

### Fehlermeldung

Wenn Ethos einen Fehler feststellt, wird in der oberen Leiste ein rotes Dreieck
als Fehlerwarnung angezeigt — häufige Ursachen sind ein Lua-Skript-Fehler, ein
RAM-Backup-Fehler oder das Ausführen einer nächtlichen Firmware-Version
(Nightlies). Die Einzelheiten zu der Warnung finden Sie stets unter
**System → Info**, auf derselben Seite wie die Laufzeit des Senders und die
[Fehlerprotokolle](../system-setup/information.md).

## Die untere Leiste

![Untere Leiste](../assets/bottombar.png)

Die untere Leiste hat vier Registerkarten für den Zugriff auf die Funktionen der
obersten Ebene — **Hauptansicht**, **Model Setup**, **Einstellung Ansichten**,
**System Setup** — die Systemzeit wird auf der rechten Seite angezeigt (wenn Sie
die Uhrzeit berühren, gelangen Sie direkt zu
[Datum & Uhrzeit](../system-setup/date-and-time.md)).

## Der Widgets-Bereich

Der mittlere Bereich jeder Ansicht besteht aus **Widgets**: Modellbild,
Stoppuhren, Telemetrieanzeigen, Trimm- und Poti-Balken und mehr, alle von Ihnen
platziert und konfiguriert. Unter
[Bildschirme konfigurieren](../displays/index.md) erfahren Sie, wie Sie Widgets
hinzufügen, verschieben und konfigurieren, und unter
[Hinzufügen von weiteren Bildschirmen](../displays/additional-displays.md), wie
Sie mehr als die standardmäßig vorhandene einzelne Ansicht anlegen.
