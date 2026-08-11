---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite ist die Begleitanwendung für Windows/Mac zur Verwaltung eines
Senders, auf dem Ethos läuft und der über USB verbunden ist.

!!! note "Screenshots ausstehend"
    Ethos Suite ist eine eigenständige PC-Anwendung und nicht der Sender
    selbst, daher verwendet dieser Abschnitt nicht die im Simulator
    aufgenommenen Screenshots wie der Rest des Handbuchs — siehe
    [Screenshot-Pipeline](../contributing/screenshot-pipeline.md).

Nach dem Verbinden kann Ethos Suite:

1. Typ, ID und installierte Versionen des Senders auslesen — Firmware,
   Bootloader, internes HF-Modul, Dateien im Flash-Speicher sowie Dateien
   auf SD card/eMMC.
2. Den Sender zwischen Bootloader-Modus und laufendem Ethos hin- und
   herschalten.
3. Installierte Versionen mit den aktuellen vergleichen und automatisch
   aktualisieren — nur veraltete Komponenten, alles unabhängig vom Stand
   oder einzelne Komponenten.
4. Modelle über den **Model Manager** auf Datenträger sichern oder eine
   frühere Sicherung wiederherstellen (erforderlich, da Modelldateien
   zwischen Firmware-Versionen nicht abwärtskompatibel sind).
5. Über das **Download center** beliebige Firmware von der FrSky-Download-Seite
   herunterladen und den Sender als Proxy verwenden, um ein Modul, einen
   Sensor, ein Servo oder einen Empfänger direkt zu flashen.
6. Bilder und Audiodateien in die nativen Formate von Ethos konvertieren.
7. **Lua-Entwicklungswerkzeuge** bereitstellen — API-Dokumentation,
   Demo-Skripte und ein Debug-Terminal.
8. Den Bootloader des Senders im DFU-Modus flashen (Verbindung bei
   ausgeschaltetem Sender), unabhängig davon, ob die eigene Firmware des
   Senders noch läuft.
9. Den internen Speicher von X18/S, TW Lite, XE und X20 Pro/R/RS über das
   **Repair Tool** reparieren, wenn NAND nicht gelesen werden kann oder
   Einstellungen nicht gespeichert werden.
10. Die USB-Laufwerke des Senders sauber auswerfen.
11. Beim Start benachrichtigen, wenn ein Update für die Suite selbst
    verfügbar ist (wird beim Beenden installiert).

## Verbindungsmodi

Neben ihren Werkzeugen arbeitet die Suite in drei verschiedenen
Verbindungszuständen des Senders:

- **Sender im Bootloader-Modus** — der Reiter **Radio** prüft und
  aktualisiert die Firmware sowie die Dateien in Flash/SD card/eMMC; der
  **Model Manager** sichert den Sender oder stellt ihn wieder her.
- **Sender im Ethos-Modus** — die Suite nutzt den Sender als Proxy (über
  die Werkzeuge **FRSK Flasher**/Download center), um das interne Modul
  oder einen beliebigen angeschlossenen Sensor/Servo/Empfänger direkt zu
  flashen.
- **Sender im DFU-Modus** — Verbindung bei ausgeschaltetem Sender,
  verwendet vom **DFU Flasher**, um den Bootloader selbst zu flashen,
  z. B. wenn eine beschädigte Firmware das normale Einschalten des
  Senders verhindert.

Siehe [Migration](migration.md) für die erstmalige Umstellung eines
vorhandenen Senders auf Ethos Suite und [Bedienung](operation.md) für die
Oberfläche der Suite selbst.
