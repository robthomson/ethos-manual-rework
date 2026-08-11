---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# USB-Verbindungsmodi

![USB-Menü](../assets/usbmenu.png)

Was eine USB-Verbindung zu einem PC bewirkt, hängt davon ab, wie der Sender
beim Einstecken mit Strom versorgt wurde.

## Modus bei ausgeschaltetem Sender

Wird der Sender **im ausgeschalteten Zustand** per USB mit einem PC
verbunden, wechselt er in den DFU-Modus, der zum Flashen des Bootloaders
selbst dient.

## Bootloader-Modus {: #bootloader-mode }

Schalten Sie den Sender **mit gedrückter `ENT`-Taste** ein, um in den
Bootloader-Modus zu starten (auf dem Bildschirm erscheint „Bootloader“).
Wird nun USB angeschlossen, wechselt der Status auf „USB Plugged“, und der
PC bindet **zwei** Laufwerke ein: den internen Flash-Speicher des Senders
sowie den Inhalt der SD card/eMMC. Dies ist der Modus zum direkten Lesen
und Schreiben von Dateien in beiden Speicherbereichen, und auf diese Weise
aktualisiert auch [Ethos Suite](../ethos-suite/index.md) die Firmware des
Senders — siehe den Abschnitt „Bootloader-Modus“ von Ethos Suite.

## Modus bei eingeschaltetem Sender

Wird USB angeschlossen, während der Sender **normal eingeschaltet** ist,
erscheint eine Modus-Auswahl:

- **Joystick** — meldet den Sender als USB-HID-Joystick an, zur Steuerung
  von PC-Flugsimulatoren.
- **FrSky Suite** — versetzt den Sender in den „Ethos-Modus“ zur
  Kommunikation mit [Ethos Suite](../ethos-suite/index.md).
- **Serial** — leitet Lua-Debug-Ausgaben über USB-Seriell (115200 bps)
  weiter. Der Reiter „Lua Development Tools“ von Ethos Suite verfügt über
  ein integriertes Terminal zur Anzeige; unter Windows kann ein Treiber für
  einen virtuellen COM-Port erforderlich sein.
