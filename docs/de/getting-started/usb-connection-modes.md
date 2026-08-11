---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Modi für USB-Verbindung zum PC

![USB-Menü](../assets/usbmenu.png)

Was eine USB-Verbindung zum PC bewirkt, hängt davon ab, wie der Sender beim
Einstecken mit Strom versorgt war.

## Modus „Ausgeschaltet“

Schließen Sie den Sender **im ausgeschalteten Zustand** über USB an einen PC
an, so wechselt er in den DFU-Modus, der zum Flashen des Bootloaders selbst
dient.

## Bootloader-Modus {: #bootloader-mode }

Der Sender wird in den Bootloader-Modus versetzt, indem er **mit gedrückter
`ENT`-Taste** eingeschaltet wird (auf dem Bildschirm erscheint die
Statusmeldung „Bootloader“). Wird nun USB angeschlossen, ändert sich die
Statusmeldung in „USB Plugged“, und der PC zeigt **zwei** externe Laufwerke
an: den Flash-Speicher des Senders sowie den Inhalt der SD card/eMMC. Dieser
Modus wird zum direkten Lesen und Schreiben von Dateien auf beide
Speicherbereiche verwendet, und über ihn aktualisiert auch [Ethos
Suite](../ethos-suite/index.md) die Firmware des Senders — siehe den
Abschnitt „Bootloader-Modus“ im Abschnitt Ethos Suite.

## Modus „Eingeschaltet“

Wird der Sender im eingeschalteten Zustand über USB mit einem PC verbunden,
erscheint der folgende Auswahldialog:

- **Joystick** — meldet den Sender als USB-HID-Joystick an und kann so für
  die Steuerung von RC-Simulatoren am PC verwendet werden.
- **FrSky Suite** — versetzt den Sender in den „Ethos-Modus“ für die
  Kommunikation mit [Ethos Suite](../ethos-suite/index.md).
- **Serial** — im seriellen Modus werden Lua-Fehlersuch-Spuren an
  USB-Serial gesendet (115200 bps). Die Registerkarte „Lua Development
  Tools“ in der Ethos Suite verfügt über ein integriertes Terminalfenster
  zur Anzeige; unter Umständen wird ein Windows Virtual COM Port Treiber
  benötigt.
