---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Bedienung

## Bereich „Willkommen“

**Aktuelle Nachrichten** – Versionshinweise und Backup-Empfehlungen vor
dem Update. Ethos 1.6.0 oder höher setzt voraus, dass das interne
HF-Modul sowie TD/TW/AP/AP-Plus-Empfänger mindestens auf v3.0.1 sind, um
dessen Verbesserungen nutzen zu können. Wird **Pre-releases** aktiviert
(mit GitHub als Server – siehe
[Suite-Einstellungen](#suite-settings)), werden hier zusätzlich zur
vollständigen Versionshistorie auch Vorabversionen aufgeführt.

**ethos.frsky-rc.com** – eine eingebettete Ansicht der Webseite:
Ressourcen, Links zu Modellvorlagen und die Liste der unterstützten
Sender.

## Bereich „Sender“

Verwaltet den angeschlossenen Sender. Schalten Sie ihn in den
[Bootloader-Modus](../getting-started/usb-connection-modes.md#bootloader-mode)
ein und verbinden Sie ihn per USB – die Suite zeigt nach der Erkennung
den Sendertyp an (z. B. „X20“).

### Sender-Informationen

- **Ethos** – installierte Firmware- und Bootloader-Version; über
  **Ethos verwalten** gelangen Sie direkt zur Aktualisierung, falls diese
  veraltet sind.
- **HF-Modul** – installierte Firmware des internen HF-Moduls; über
  **Internes Modul verwalten** gelangen Sie direkt zur Aktualisierung,
  falls diese veraltet ist.
- **Modell Verwaltung** / **Lua-Bibliothek** / **Software Bereich** –
  Verknüpfungen zu diesen Werkzeugen.

### Ethos aktualisieren {: #updating-ethos }

Die Registerkarte **Ethos** zeigt die Versionen von Firmware, Bootloader,
SD card/eMMC (Audiodateien) und Flash-Speicher (System-Bitmaps)
nebeneinander an – die Systemdateien im Flash werden jetzt von der Ethos
Suite zusammen mit der Firmware verwaltet und nicht mehr separat.

- **Flashe veraltete Komponenten** – aktualisiert nur die veralteten
  Komponenten.
- **Flashe alle Komponenten** – aktualisiert alles, unabhängig von der
  Version.
- Einzelne Optionen **Flashe Firmware**, **Flashe Bootloader** und
  **Flashe Audiodateien**, die jeweils über die dunkelgraue Schaltfläche
  neben der gewählten Option ausgeführt werden.
- **Flash Sender von lokaler Datei** – umgeht den Download und verwendet
  eine bereits auf dem PC vorhandene Firmware-Datei.

Bei der Auswahl einer Release wird zunächst eine **Vorauswahl Version**
(Stabil/Testing) und anschließend eine Version gewählt. Vor dem Update
wird zu einer Sicherung aufgefordert (**Zur Backup-Seite gehen**) –
nutzen Sie diese Möglichkeit. Ist das interne HF-Modul nicht auf v3.0.1
oder neuer, verlangt Ethos 1.6.0 oder höher vor dem Fortfahren dessen
Aktualisierung (**Zum Modulmanager gehen** flasht es automatisch, danach
wird das Ethos-Update fortgesetzt) – bei TD/TW/AP/AP-Plus-Empfängern muss
anschließend die Telemetrie gelöscht und neu erkannt werden, damit die
aktualisierten Sensornamen übernommen werden.

Der Fortschritt des Updates wird Schritt für Schritt angezeigt (Wechsel
in den Bootloader, Herunterladen, Kopieren, Aushängen, Schreiben,
Aktualisieren, „Update erfolgreich!“) – der Schreibfortschritt wird
zusätzlich auf dem Display des Senders angezeigt.

!!! note "Updates auf Vorabversionen"
    Die Dateien einer Vorabversion können sich ändern, ohne dass sich
    deren Versionsnummer ändert; die Suite kann dies nicht erkennen –
    flashen Sie eine bereits installierte Vorabversion daher erneut,
    sobald sie als vollwertige Version veröffentlicht wird. Prüfen Sie im
    Zweifel das Firmware-Datum unter [System →
    Info](../system-setup/information.md).

!!! note "Update von Ethos 1.2.8 oder älter"
    Von einer derart alten Version aus kann die Suite Firmware und
    Bootloader möglicherweise nicht vollautomatisch flashen – stattdessen
    erscheint ein geführter Dialog für das manuelle Flashen. Es wäre auch
    ratsam, die Laufwerke in jedem Fall manuell auszuwerfen, bevor Sie das
    USB-Kabel abziehen.

Die System-Bitmaps (Bilder) werden jetzt automatisch zusammen mit der
Firmware aktualisiert und müssen nicht mehr separat verwaltet werden;
Audiodateien werden über **Flashe alle Komponenten** oder **Flashe
Audiodateien** aktualisiert (dabei wird das gewählte Sprachpaket
heruntergeladen, z. B. „Audio English“).

### HF-Modul-Verwaltung

Wählen Sie die gewünschte Version (normalerweise die neueste) und klicken
Sie auf **Modul flashen**, um die Firmware auf das interne HF-Modul zu
schreiben – nach Abschluss wird der Dialog „... wurde erfolgreich
geflasht“ angezeigt. Dies wird auch durch das oben beschriebene
obligatorische Upgrade auf v3.0.1 automatisch ausgelöst.

### Ethos-Modus

Mit **Wechsel zu Ethos** wird der Sender vom Bootloader-Modus in den
Ethos-Modus umgeschaltet (erkennbar an einem runden grünen USB-Symbol auf
dem Sender und daran, dass in der Kopfzeile der Suite „(Bootloader
Modus)“ entfällt). Der Ethos-Modus ist erforderlich, damit die Ethos
Suite den Sender als Proxy verwenden und die Registerkarte **Software
Bereich** zum Flashen von Modulen, Empfängern, Sensoren und Servos nutzen
kann. Die Schaltfläche wird anschließend zu **Wechsel zu Bootloader**, um
wieder zurückzuschalten. **Laufwerke auswerfen** trennt die
USB-Verbindung zum Sender sauber.

### Modell Verwaltung

Mit dem Modell-Manager kann eine Sicherung der Modelldateien und
Einstellungen des Senders auf der Festplatte gespeichert oder eine zuvor
gespeicherte Sicherung im Sender wiederhergestellt werden.

!!! warning
    Die Wiederherstellung stellt **nicht** die Firmware wieder her!
    Nachdem Sie Ihre Modelle und Einstellungen wiederhergestellt haben,
    müssen Sie die Firmware separat mit der Version neu schreiben, die
    Ihrer Sicherung entspricht (siehe [Ethos
    aktualisieren](#updating-ethos)), denn die Modelldateien sind nicht
    abwärtskompatibel.

- **Sicherungsort** – klicken Sie auf das Ordnersymbol, um den
  gewünschten Ordner auszuwählen (der Sicherungspfad wird für jeden
  Sendertyp gespeichert); darunter werden Datum und Uhrzeit der letzten
  Sicherung angezeigt.
- **Backup** – erstellt eine Sicherungskopie der Modelldateien; die
  aktuelle Ethos-Version wird dabei mit aufgezeichnet.
- **Wiederherstellen** – Auswahl der wiederherzustellenden Komponenten:
  Audio (standardmäßig nicht ausgewählt), Skripte, Bildschirmfotos,
  System-Bitmaps (standardmäßig nicht ausgewählt – werden jetzt mit der
  Firmware verwaltet), Modelle (einschließlich der dort abgelegten
  Textdateien einer [benutzerdefinierten
  Checkliste](../how-to/user-defined-checklist.md)), Sprache,
  Benutzer-Bitmaps, Protokolle, System-Einstellungen.

### Lua-Bibliothek

Die Lua-Bibliothek enthält Download-Links und Installationsoptionen für
verschiedene Lua-Tools und -Skripte (oder installiert Lua-Skripte aus
einer lokalen Zip-Datei auf Ihrem Sender). Sobald Sie einige Skripte auf
dem Sender installiert haben, zeigt das Lua-Bibliothekstool die
installierten Skripte im linken Fenster und die Remote-Bibliothek im
rechten Fenster an.

## Bereich „Hilfsprogramme“

- **Software Bereich** – hier kann jede Firmware von der FrSky
  Download-Seite heruntergeladen werden, und der Sender kann (solange er
  sich im Ethos-Modus befindet) als Proxy verwendet werden, um ein Modul,
  einen Sensor, ein Servo oder einen Empfänger zu flashen, der über eine
  S.Port-Upgrade-Verbindung angeschlossen ist. Wählen Sie in der
  Produktliste das Gerät aus, das geflasht werden soll (z. B. einen
  TW-SR8-Empfänger); der Software Bereich listet dann die verfügbaren
  **Firmwareversionen** (Assets) auf. Mit **Download** speichern Sie die
  Datei lokal, mit **Flash** wird direkt auf das angeschlossene Gerät
  geschrieben – ein Fortschrittsbalken zeigt den Flash-Vorgang an und
  endet mit „... wurde erfolgreich geflasht!“.

- **Bilder Verwaltung** – wandelt Ihre Bilder in das native Format von
  Ethos um (32bit BMP, Farbraum RGB, Alphakanal nur bei Bedarf) in einer
  gewählten Größe, jedoch unter Beibehaltung des Seitenverhältnisses.
  Referenzgrößen: Modellbilder 300×280 (X20) / 180×168 (X18); Vollbilder
  800×480 (X20) / 480×320 (X18) – die Regeln für die Benennung von
  Bitmaps finden Sie im
  [Dateimanager](../system-setup/file-manager.md#top-level-folders).
  Außerdem lassen sich die Ordner `bitmaps/gps`, `bitmaps/models` und
  `bitmaps/user` des Senders direkt öffnen, inklusive Upload-Funktion.
  Fügen Sie Bilder mit **+** zur Liste der zu wandelnden Dateien hinzu
  (das TIFF-Format wird nicht unterstützt), wählen Sie einen Ausgabepfad
  (einen lokalen PC-Ordner; direkt an den Sender als Modell-, Benutzer-
  oder GPS-Bild; oder den aktuell im rechten Fenster geöffneten Ordner)
  und aktivieren Sie optional das Öffnen des Ordners nach der Umwandlung
  oder das Hinzufügen eines Alphakanals für die Transparenz.

- **Audio Verwaltung** – konvertiert Ihre Audiodateien in das
  Ethos-Format (PCM linear, Abtastrate 32kHz, 1 Kanal (mono), 16 Bits
  Low-Endian). Fügen Sie Dateien mit **+** hinzu, wählen Sie einen
  lokalen PC-Ordner oder senden Sie sie direkt in den Audio-Ordner des
  Senders (anschließend müssen Sie sie in den Ordner mit Ihren eigenen
  Audiodateien verschieben), optional mit Öffnen des Verzeichnisses nach
  der Konvertierung.

- **Lua-Entwicklungs-Werkzeuge** – **Lua Doku** verlinkt das Ethos Lua
  Referenzhandbuch (lesen Sie auch den rcgroups-Thread *FrSky - ETHOS Lua
  Script Programming*); **Lua Demo-Scripte** verlinkt Beispielskripte auf
  der Webseite der Ethos-Feedback-Community auf GitHub; **Debug log**
  bietet ein Live-Protokollfenster für Lua-`print()`-Ausgaben, die an
  USB-Serial gesendet werden, während sich der Sender im seriellen Modus
  befindet:

  1. Verbinden Sie den Sender wie gewohnt mit der Suite und wechseln Sie
     in den Ethos-Modus.
  2. Bearbeiten Sie die Lua-Skripte direkt auf dem eingebundenen Laufwerk
     des Senders mit Ihrem bevorzugten Code-Editor.
  3. Öffnen Sie **Lua-Entwicklungs-Werkzeuge** → **START DEBUG** –
     dadurch wird der Sender in den Debug-Modus (den seriellen Modus)
     geschaltet, startet neu und die Skripte werden neu initialisiert.
  4. Alle Druckausgaben (`print()`) der aktiven Skripte werden an das
     integrierte Terminalfenster der Suite gesendet.
  5. **STOP DEBUG** wechselt zurück in den normalen Ethos-Modus, um
     weiterzuarbeiten.

- **DFU flasher** – flasht den Bootloader über eine ausgeschaltete
  USB-Verbindung (DFU-Modus) und funktioniert selbst dann, wenn die
  Firmware des Senders vollständig beschädigt wurde, da sich der
  STM-Bootloader im ROM befindet. Klicken Sie auf **Bootloader
  auswählen**, um Ihre heruntergeladene Bootloader-Datei auszuwählen (die
  Ethos Suite erstellt einen Bericht über Version und Eignung der Datei),
  verbinden Sie den **ausgeschalteten** Sender und klicken Sie dann auf
  **Flash**.

  !!! note "\"Funkverbindung wird nicht erkannt!\""
      Meist liegt ein fehlender oder falscher DFU-Treiber vor. Auf den
      meisten PCs mit Windows 10 oder höher werden die Tandem-Systeme mit
      dem Standard-Windows-USB-DFU-Treiber verbunden, Windows-Updates
      ersetzen ihn jedoch häufig durch einen generischen Treiber, der
      nicht funktioniert – überprüfen Sie den Gerätemanager und ziehen
      Sie ein Programm wie den Impulse Driver Fixer in Betracht. Speziell
      Horus X10 Benutzer müssen den STM32bootloader USB-Gerätetreiber
      unter Umständen manuell installieren (Impulse Driver Fixer oder
      Zadig), da Windows 10 ihn standardmäßig nicht installiert.

- **Reparatur-Werkzeuge** – für die Sendertypen X18/S, TW Lite, XE und
  X20 Pro/R/RS: Wenn Ihr Sender nicht vom NAND lesen kann oder die
  Einstellungen nicht gespeichert werden können, formatiert dieses Tool
  den internen Speicher neu.

## Bereich „Weitere Infos“

- **Dokumentationen** – Links zur Ethos-Feedback-Community auf GitHub, zu
  den offiziellen Ethos-Handbüchern (zum Herunterladen) und zu einer
  Ethos Suite FAQ.
- **Ethos GitHub** – Zugriff auf die Ethos-Versionen und den
  Issue-Tracker (um Überschneidungen zu vermeiden, durchsuchen Sie bitte
  die bestehenden Issues, bevor Sie einen neuen Beitrag schreiben).

### Suite-Einstellungen {: #suite-settings }

- **Sprache** – Tschechisch, Deutsch, Englisch, Spanisch, Französisch,
  Hebräisch, Italienisch, Niederländisch, Norwegisch, Portugiesisch,
  Slowenisch und Chinesisch.
- **Standort des Servers** – **FrSky Server** oder **GitHub**
  (erforderlich für den oben beschriebenen Zugriff auf Vorabversionen).
- **Debug Optionen** – Popup-Dialog beim Auftreten eines fatalen Fehlers
  aktivieren oder deaktivieren; den Suite-Debug-Modus aktivieren, der
  alle Spuren protokolliert (nicht nur die Abstürze); den Ordner logs
  öffnen.
- **Version** / **Suite aktualisieren** – aktuelle Suite-Version sowie
  manuelle Suche nach Updates.
- **Über uns** – eine Bestätigungsseite für alle wiederverwendeten
  Komponenten.

## Befehlszeilenoperation

Die Ethos Suite kann über eine Terminal-Befehlszeile ausgeführt werden:

| Flag | Wirkung |
|---|---|
| `--help` | Hilfetext für das Ethos Suite-Befehlszeilentool. |
| `--version` | Zeigt die Version der installierten Ethos Suite an. |
| `--list-radios` | Listet alle unterstützten FrSky-Sender auf. |
| `--radio-components --radio {RADIO}` (oder `--radio auto`) | Listet alle Komponenten eines angeschlossenen Senders und ihre Pfade auf. `auto` erkennt automatisch; geben Sie `{RADIO}` an, wenn mehrere Sender angeschlossen sind. |
| `--get-path {COMPONENT}` | Ruft den Pfad der angegebenen Komponente ab – `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` oder `I18N`. |
| `--serial start` \| `--serial stop` | Aktiviert/deaktiviert den seriellen Debug-Modus. |

!!! note
    Die Suite-App wird nur gestartet, wenn sie einen Befehl erfolgreich
    erkennt.
