---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Die Ethos Suite ist die begleitende Windows-/Mac-Anwendung zur Verwaltung
eines Senders, auf dem Ethos läuft und der über USB angeschlossen ist.

!!! note "Screenshots ausstehend"
    Die Ethos Suite ist eine eigenständige PC-Anwendung und nicht der Sender
    selbst, daher verwendet dieser Abschnitt nicht die im Simulator
    aufgenommenen Screenshots wie der Rest des Handbuchs — siehe
    [Screenshot-Pipeline](../contributing/screenshot-pipeline.md).

Nach dem Verbinden kann die Ethos Suite:

1. Typ, ID und installierte Versionen des Senders auslesen — Firmware,
   Bootloader, internes HF-Modul, Dateien im Flash-Speicher sowie Dateien
   auf SD card/eMMC.
2. Den Sender vom Bootloader-Modus in den Ethos-Modus umschalten, mit der
   Möglichkeit, wieder zurückzuschalten.
3. Installierte Versionen mit den aktuellen vergleichen und automatisch
   aktualisieren — nur veraltete Komponenten, alle Komponenten unabhängig
   vom Stand oder einzelne Komponenten.
4. Modelle über die **Modell Verwaltung** auf der Festplatte sichern oder
   eine zuvor gespeicherte Sicherung wiederherstellen (erforderlich, da
   Modelldateien zwischen Firmware-Versionen nicht abwärtskompatibel sind).
5. Über das **Download-Center** jede Firmware von der FrSky Download-Seite
   herunterladen und den Sender als Proxy verwenden, um ein Modul, einen
   Sensor, ein Servo oder einen Empfänger direkt zu flashen.
6. Bilder und Audiodateien in die Ethos-eigenen Formate umwandeln.
7. **Lua-Entwicklungswerkzeuge** bereitstellen — API-Dokumentation,
   Demo-Skripte und ein Debug-Terminal.
8. Den Bootloader des Senders im DFU-Modus über eine ausgeschaltete
   Verbindung flashen, unabhängig davon, ob die Firmware des Senders noch
   läuft.
9. Den internen Speicher der Sendertypen X18/S, TW Lite, XE und
   X20 Pro/R/RS über die **Reparatur-Werkzeuge** reparieren, wenn der
   Sender nicht vom NAND lesen kann oder die Einstellungen nicht
   gespeichert werden können.
10. Die USB-Laufwerke des Senders sauber auswerfen.
11. Beim Start benachrichtigen, wenn ein Update für die Suite selbst
    verfügbar ist (wird beim Beenden installiert).

## Verbindungsmodi

Neben ihren Hilfsprogrammen arbeitet die Suite in drei verschiedenen
Verbindungszuständen des Senders:

- **Sender im Bootloader-Modus** — die Registerkarte **Sender** prüft und
  aktualisiert die Firmware sowie die Dateien in Flash/SD card/eMMC; die
  **Modell Verwaltung** sichert den Sender oder stellt ihn wieder her.
- **Sender im Ethos-Modus** — die Suite verwendet den Sender als Proxy
  (über die Werkzeuge **FRSK Flasher**/Download-Center), um das interne
  Modul oder einen beliebigen angeschlossenen Sensor, ein Servo oder einen
  Empfänger direkt zu flashen.
- **Sender im DFU-Modus** — Verbindung bei ausgeschaltetem Sender,
  verwendet vom **DFU Flasher**, um den Bootloader selbst zu flashen,
  z. B. wenn eine beschädigte Firmware das normale Einschalten des Senders
  verhindert.

Siehe [Migration](migration.md) für die erstmalige Umstellung eines
vorhandenen Senders auf die Ethos Suite und [Bedienung](operation.md) für
die Oberfläche der Suite selbst.
