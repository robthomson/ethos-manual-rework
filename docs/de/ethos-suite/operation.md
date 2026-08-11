---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Bedienung

## Bereich „Willkommen“

**Update News** – Versionshinweise und Backup-Empfehlungen vor dem
Update. Ethos 1.6.0+ setzt voraus, dass das interne HF-Modul sowie
TD/TW/AP/AP-Plus-Empfänger mindestens auf v3.0.1 sind, um dessen
Verbesserungen nutzen zu können. Wird **Pre-releases** aktiviert (mit
GitHub als Server – siehe [Suite-Einstellungen](#suite-settings)), werden
hier zusätzlich zur vollständigen Versionshistorie auch Vorabversionen
aufgeführt.

**Ethos-Webseite** – eine eingebettete Ansicht von ethos.frsky-rc.com:
Ressourcen, Links zu Modellvorlagen und die Liste der unterstützten
Sender.

## Bereich „Sender“

Verwaltet den angeschlossenen Sender. Schalten Sie ihn in den
[Bootloader-Modus](../getting-started/usb-connection-modes.md#bootloader-mode)
ein und verbinden Sie ihn per USB – die Suite zeigt nach der Erkennung
den Sendertyp an (z. B. „X20“).

### Senderinformationen

- **Ethos** – installierte Firmware- und Bootloader-Versionen; **Manage
  Ethos** führt direkt zur Aktualisierung, falls diese veraltet sind.
- **RF Module** – installierte Firmware des internen HF-Moduls; **Manage
  internal module** führt direkt zur Aktualisierung, falls diese veraltet
  ist.
- **Model manager** / **Lua library** / **Download center** – Verknüpfungen
  zu diesen Werkzeugen.

### Ethos aktualisieren {: #updating-ethos }

Die Registerkarte **Ethos** zeigt die Versionen von Firmware, Bootloader,
SD card/eMMC (Audiodateien) und Flash-Speicher (System-Bitmaps)
nebeneinander an – Systemdateien im Flash werden inzwischen gemeinsam mit
der Firmware aktualisiert und nicht mehr separat verwaltet.

- **Write outdated components** – aktualisiert nur die veralteten
  Komponenten.
- **Write all components** – aktualisiert alles, unabhängig von der
  Version.
- Einzelne Optionen **Write firmware**, **Write bootloader** und **Write
  audio files**, die jeweils über die dunkelgraue Schaltfläche neben der
  gewählten Option ausgeführt werden.
- **Flash from a local file** – umgeht den Download und verwendet eine
  bereits lokal vorhandene Firmware-Datei.

Bei der Auswahl einer Version wird zunächst ein **Branch**
(Stable/Testing) und anschließend eine Version gewählt. Vor dem Update
wird zu einem Backup aufgefordert (**Go to backup page**) – nutzen Sie
diese Möglichkeit. Ist das interne HF-Modul nicht auf v3.0.1 oder neuer,
verlangt Ethos 1.6.0+ vor dem Fortfahren dessen Aktualisierung (**Go to
Module manager** flasht es automatisch, danach wird das Ethos-Update
fortgesetzt) – bei TD/TW/AP/AP-Plus-Empfängern muss anschließend die
Telemetrie gelöscht und neu erkannt werden, damit die aktualisierten
Sensornamen übernommen werden.

Der Fortschritt des Updates wird Schritt für Schritt angezeigt (Wechsel
in den Bootloader, Herunterladen, Kopieren, Aushängen, Schreiben,
Aktualisieren, „Update successful!“) – der Schreibfortschritt wird
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
    erscheint ein geführter Dialog für das manuelle Flashen. Werfen Sie
    die Laufwerke in jedem Fall manuell aus, bevor Sie das USB-Kabel
    abziehen.

System-Bitmap-Dateien werden nun automatisch zusammen mit der Firmware
aktualisiert (keine separate Verwaltung erforderlich); Audiodateien
werden über **Write all components** oder **Write audio files**
aktualisiert (dabei wird das gewählte Sprachpaket heruntergeladen, z. B.
„English audio pack“).

### RF Module Manager

Wählen Sie eine Version (normalerweise die neueste) und **Flash module**,
um die Firmware des internen HF-Moduls direkt zu aktualisieren – nach
Abschluss wird „...has been flashed successfully“ bestätigt. Dies wird
auch durch das oben beschriebene verpflichtende Upgrade auf v3.0.1
automatisch ausgelöst.

### Ethos-Modus

**Switch to Ethos** startet den Sender aus dem Bootloader-Modus neu, sodass
Ethos läuft (erkennbar an einem grünen USB-Symbol auf dem Sender und
daran, dass in der Kopfzeile der Suite „(Bootloader Mode)“ entfällt). Dies
ist erforderlich, damit das **Download center** den Sender als Proxy zum
Flashen von Modulen, Empfängern, Sensoren und Servos verwenden kann. Die
Schaltfläche wird anschließend zu **Switch to Bootloader**, um den
Vorgang umzukehren. **Eject Drives** trennt den Sender sauber.

### Model Manager

Sichert Modelldateien und Einstellungen auf dem Datenträger oder stellt
ein früheres Backup wieder her.

!!! warning
    Beim Wiederherstellen wird die Firmware **nicht** wiederhergestellt –
    flashen Sie nach dem Wiederherstellen von Modellen/Einstellungen
    separat diejenige Firmware-Version, die tatsächlich zu diesem Backup
    passt (siehe [Ethos aktualisieren](#updating-ethos)), da Modelldateien
    nicht abwärtskompatibel sind.

- **Backup Location** – Ordner auswählen (wird je Sendertyp gespeichert);
  darunter werden Datum und Uhrzeit des letzten Backups angezeigt.
- **Backup** – speichert die Modelldateien und hält die aktuelle
  Ethos-Version dazu fest.
- **Restore** – Auswahl der wiederherzustellenden Komponenten: Audio
  (standardmäßig aus), Scripts, Screenshots, System Bitmaps
  (standardmäßig aus – wird jetzt mit der Firmware verwaltet), Models
  (einschließlich der dort abgelegten Textdateien einer
  [benutzerdefinierten
  Checkliste](../how-to/user-defined-checklist.md)), Language, User
  Bitmaps, Logs, System Settings.

### Lua library

Durchsuchen und Installieren von Lua-Skripten und -Tools aus der
Remote-Bibliothek von FrSky mit einem Klick (oder Installation aus einer
lokalen ZIP-Datei); installierte Skripte werden neben dem
Remote-Katalog angezeigt, sobald welche vorhanden sind.

## Bereich „Tools“

- **Download center** – lädt beliebige Firmware von der FrSky-Website
  herunter und nutzt den Sender (während er sich im Ethos-Modus befindet)
  als Proxy, um ein Modul, einen Sensor, ein Servo oder einen Empfänger zu
  flashen, der über eine S.Port-Upgrade-Verbindung angeschlossen ist.
  Wählen Sie das Produkt aus der Liste (z. B. einen TW-SR8-Empfänger),
  sehen Sie sich die verfügbaren **assets** an, und wählen Sie
  **Download**, um lokal zu speichern, oder **Flash**, um direkt auf das
  angeschlossene Gerät zu schreiben – ein Fortschrittsbalken zeigt den
  Flash-Vorgang an und endet mit „...has been flashed successfully!“.

- **Image manager** – konvertiert Bilder in das native Format von Ethos
  (32-Bit-BMP, RGB, Alphakanal nur bei Bedarf) in einer gewählten Größe
  unter Beibehaltung des Seitenverhältnisses. Referenzgrößen: Modellbilder
  300×280 (X20) / 180×168 (X18); Vollbilder 800×480 (X20) / 480×320 (X18)
  – siehe [Dateimanager](../system-setup/file-manager.md#top-level-folders)
  für die Benennungsregeln von Bitmaps. Außerdem lassen sich die Ordner
  `bitmaps/gps`, `bitmaps/models` und `bitmaps/user` des Senders direkt
  durchsuchen, inklusive Upload-Funktion. Fügen Sie Bilder mit **+** zur
  Konvertierungsliste hinzu (TIFF wird nicht unterstützt), wählen Sie
  einen Ausgabepfad (einen lokalen Ordner; direkt auf den Sender unter
  Modell-, Benutzer- oder GPS-Bilder; oder den aktuell geöffneten
  Senderordner) und aktivieren Sie optional das automatische Öffnen des
  Ausgabeordners oder das Erzwingen eines Alphakanals.

- **Audio manager** – konvertiert Audiodateien in das Ethos-Format (PCM
  linear, 32 kHz, mono, 16 Bit Little Endian). Fügen Sie Dateien mit **+**
  hinzu, wählen Sie einen lokalen Ordner oder senden Sie sie direkt in den
  Ordner `audio` des Senders (anschließend in den passenden
  Stimmen-Unterordner verschieben), optional mit automatischem Öffnen des
  Zielordners.

- **Lua development tools** – **Lua Docs** verlinkt das
  Ethos-Lua-Referenzhandbuch (siehe auch den rcgroups-Thread *FrSky -
  ETHOS Lua Script Programming*); **Lua Demo Scripts** verlinkt
  Beispielskripte auf dem GitHub der Ethos-Feedback-Community; **Debug**
  öffnet ein Live-Protokollfenster für Lua-`print()`-Ausgaben, die über
  USB-Serial gesendet werden, während sich der Sender im Serial-Modus
  befindet:

  1. Verbinden Sie den Sender wie gewohnt mit der Suite und wechseln Sie
     in den Ethos-Modus.
  2. Bearbeiten Sie die Lua-Skripte direkt auf dem eingebundenen Laufwerk
     des Senders in einem beliebigen Code-Editor.
  3. Öffnen Sie **Lua Development Tools** → **START DEBUG** – dadurch
     startet der Sender im Serial-/Debug-Modus neu und die Skripte werden
     neu initialisiert.
  4. Die `print()`-Ausgabe jedes aktiven Skripts läuft im Terminal der
     Suite ein.
  5. **STOP DEBUG** wechselt zurück in den normalen Ethos-Modus, um
     weiterzuarbeiten.

- **DFU Flasher** – flasht den Bootloader über eine USB-Verbindung im
  ausgeschalteten Zustand (DFU) und funktioniert auch bei vollständig
  beschädigter Firmware, da der zugrunde liegende ST-Bootloader im ROM
  liegt. Wählen Sie mit **Select Bootloader** eine heruntergeladene Datei
  aus (die Suite meldet deren Version und Eignung), schließen Sie den
  **ausgeschalteten** Sender an und wählen Sie dann **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Meist liegt ein fehlender oder falscher DFU-Treiber vor. Die
      meisten PCs mit Windows 10 oder neuer kommen mit Tandem-Systemen
      über den Standard-USB-DFU-Treiber zurecht, doch Windows Update
      ersetzt ihn gelegentlich durch einen generischen Treiber, der nicht
      funktioniert – prüfen Sie den Geräte-Manager und ziehen Sie ein
      Werkzeug wie Impulse Driver Fixer in Betracht. Speziell Nutzer der
      Horus X10 müssen den STM32-Bootloader-USB-Treiber unter Umständen
      manuell installieren (Impulse Driver Fixer oder Zadig), da Windows
      10 ihn nicht standardmäßig installiert.

- **Repair Tool** – für X18/S, TW Lite, XE und X20 Pro/R/RS: formatiert
  den internen Speicher neu, wenn der Sender den NAND nicht lesen oder
  keine Einstellungen speichern kann.

## Bereich „Sonstiges“

- **Documentation** – Links zum GitHub der Ethos-Feedback-Community, zu
  den offiziellen Ethos-Handbüchern (zum Herunterladen) und zu einer FAQ
  zur Ethos Suite.
- **Ethos Github** – Releases und Issue-Tracker (suchen Sie nach
  bestehenden Issues, bevor Sie einen neuen anlegen).

### Suite-Einstellungen {: #suite-settings }

- **Language** – Tschechisch, Deutsch, Englisch, Spanisch, Französisch,
  Hebräisch, Italienisch, Niederländisch, Norwegisch, Portugiesisch,
  Slowenisch, Chinesisch.
- **Server location** – **FrSky server** oder **GitHub** (erforderlich für
  den oben beschriebenen Zugriff auf Vorabversionen).
- **Debug options** – Popup bei schwerwiegenden Fehlern ein-/ausschalten;
  vollständiges Debug-Logging der Suite aktivieren (nicht nur bei
  Abstürzen); Log-Ordner öffnen.
- **Version** / **Update Suite** – aktuelle Version sowie manuelle
  Update-Prüfung.
- **About** – Danksagungen für verwendete Komponenten.

## Bedienung über die Kommandozeile

Die Ethos Suite kann von einem Terminal aus gestartet werden:

| Flag | Wirkung |
|---|---|
| `--help` | Zeigt die Hilfe zur Kommandozeile an. |
| `--version` | Zeigt die installierte Suite-Version an. |
| `--list-radios` | Listet alle unterstützten FrSky-Sender auf. |
| `--radio-components --radio {RADIO}` (oder `--radio auto`) | Listet die Komponenten eines angeschlossenen Senders und deren Pfade auf. `auto` erkennt automatisch; geben Sie `{RADIO}` an, wenn mehrere Sender angeschlossen sind. |
| `--get-path {COMPONENT}` | Gibt den Pfad einer Komponente aus – `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` oder `I18N`. |
| `--serial start` \| `--serial stop` | Aktiviert/deaktiviert den seriellen Debug-Modus. |

!!! note
    Die Suite startet überhaupt nur, wenn sie einen gültigen Befehl
    erkennt.
