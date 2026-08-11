---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Sonderfunktionen

![Menü der Sonderfunktionen](../assets/model-sf-menu.png)

Sonderfunktionen lösen eine Aktion aus – Audioausgabe, Bildschirmfoto,
Schreiben von Logs, haptisches Feedback und mehr –, sobald eine Bedingung
wahr wird. Bis zu 100 werden unterstützt; standardmäßig ist keine
vorhanden. Mit **+** fügen Sie eine hinzu; tippen Sie auf eine
vorhandene, um **Bearbeiten**/**Verschieben**/**Kopieren-Einfügen**/
**Klonen**/**Löschen** aufzurufen.

![Sonderfunktion hinzufügen](../assets/model-sf-add.png)
![Verschieben](../assets/model-sf-move.png)

## Für jede Aktion gemeinsame Felder

- **Status** – aktiviert/deaktiviert diese Funktion, ohne sie zu löschen.
- **Aktive Bedingung** – **Immer an**, oder gesteuert durch Schalter/
  Funktionsschalter/logische Schalter/Trimmungspositionen oder Flugphasen.
  Halten Sie `ENT` auf einem Schalter lange gedrückt und aktivieren Sie
  **Negativ**, um ihn zu invertieren (z. B. wird aus `SG-up` dann
  `!SG-up`, aktiv immer dann, wenn SG *nicht* oben ist).
- **Global** – fügt diese Funktion **jedem** Modell hinzu, sowohl
  bestehenden als auch künftigen. Besitzt ein Modell bereits eine
  identisch konfigurierte lokale Funktion, fügt Global sie als
  zusätzlichen Eintrag hinzu; wird Global wieder abgeschaltet, wird die
  Funktion aus allen Modellen außer dem aktuell ausgewählten entfernt.
  Globale Funktionen werden in `radio.bin` gespeichert, lokale in der
  Modelldatei.

## Aktionen {: #actions }

**Zurücksetzen** – setzt **Flugdaten** (Telemetrie + Timer), **Alle
Timer** oder die **Gesamte Telemetrie** zurück.

![Zurücksetzen](../assets/model-sf-reset.png)

**Bildschirmfoto** – speichert ein Bildschirmfoto im Verzeichnis
`screenshots/` auf der SD card/eMMC.

![Bildschirmfoto](../assets/model-sf-screenshot.png)

**Failsafe setzen** – übernimmt die aktuellen Kanalpositionen als
Failsafe, entweder über das interne oder das externe HF-**Modul**.

![Failsafe setzen](../assets/model-sf-set-failsafe.png)

**Audio abspielen** – die umfangreichste Aktion, die eine vollständige
Sequenz unterstützt:

![Audio abspielen](../assets/model-sf-play-audio.png)

- **Stimme** – welche der bis zu 3 konfigurierten Stimmen verwendet wird
  (siehe [Allgemein](../system-setup/general.md#audio-settings)).
- **Wiederholung** – einmalig abspielen oder in einem einstellbaren
  Intervall wiederholen (bis zu 10 Minuten).
- **Beim Start überspringen** – unterdrückt das Auslösen dieser Funktion
  während des Startvorgangs.
- **Sequenz** – bis zu 100 Schritte, jeweils einer von:

  - **Datei abspielen** – spielt eine ausgewählte Audiodatei ab.

    ![Datei abspielen](../assets/model-sf-play-audio-add-play-file.png)

  - **Wert ansagen** – sagt den Wert einer Quelle an: Analogwerte,
    Schalter, logische Schalter, Trimmungen, Kanäle, Gyro, Systemuhr,
    Trainer, Timer oder Telemetrie.

    ![Wert ansagen](../assets/model-sf-play-audio-add-play-value.png)

  - **Wartedauer** – eine feste Pause von bis zu 10 Minuten.
  - **Wartebedingung** – pausiert die Sequenz, bis eine Bedingung
    erfüllt ist.

  ![Sequenzzeile hinzufügen](../assets/model-sf-play-audio-add-line.png)
  ![Typ der Sequenzzeile](../assets/model-sf-play-audio-add-line-type.png)

  Zum Beispiel: `vfrlow.wav` abspielen, sobald der logische Schalter
  `VFRlow` aktiv wird, und anschließend den aufgezeichneten minimalen
  VFR-Wert ansagen –

  ![Wert nach Datei ansagen](../assets/model-sf-play-audio-add-play-value-add-line.png)

  – oder eine Sequenz anhalten, bis Schalter SH nach unten bewegt wird,
  bevor es weitergeht:

  ![Sequenz mit Wartebedingung](../assets/model-sf-play-audio-add-sequence.png)

  Tippen Sie auf eine beliebige Sequenzzeile, um sie zu bearbeiten,
  hinzuzufügen, umzusortieren oder zu löschen:

  ![Sequenzverwaltung](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptik** – Vibrationsfeedback:

![Haptik](../assets/model-sf-haptic.png)

- **Muster** – einfach, doppelt, dreifach, fünffach oder sehr kurz.

  ![Haptikmuster](../assets/model-sf-haptic-pattern.png)

- **Stärke** – 1–10 (Standard 5).
- **Wiederholung** – einmalig oder in einem festgelegten Intervall.
- **Haptikmotoren auswählen** – bei Sendern mit Haptikmotoren in den
  Steuerknüppeleinheiten (X20 Pro AW, X20RS oder ein X20 Pro/X20R, der
  mit MC20R-Gimbals nachgerüstet wurde – siehe
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Standard** (interne Haptik), **Alle Motoren**, **Linker
  Steuerknüppel** oder **Rechter Steuerknüppel**.

  ![Haptik beim X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Logs schreiben** – schreibt `.csv`-Logs in das Verzeichnis `Logs/` auf
der SD card/eMMC, mit Zeitstempel aus der RTC (unverzichtbar, um
Flugsitzungen später auseinanderhalten zu können):

![Logs schreiben](../assets/model-sf-write-logs.png)

- **Schreibintervall** – 100–500 ms.
- **Steuerknüppel/Potentiometer/Schieberegler**, **Schalter**, **Logische
  Schalter**, **Kanäle** – unabhängig voneinander schaltbare
  Protokollierungskategorien.

  **Logs ansehen**: Öffnen Sie eine Logdatei aus `/Logs` im
  Dateimanager. Wählen Sie aus, welche Kanäle dargestellt werden sollen
  (RSSI ist standardmäßig ausgewählt); verschieben Sie den Ausschnitt mit
  dem Drehgeber oder per Wischgeste und zoomen Sie, indem Sie den
  Drehgeber bei gedrückter `PAGE`-Taste drehen. `DISP` setzt den Fokus
  auf die erste Schaltfläche in der rechten Spalte.

**Text ansagen** (nur X20 Pro) – geräteinterne Sprachsynthese anstelle
einer vorab aufgezeichneten Datei:

![Text ansagen](../assets/model-sf-x20pro-play-text.png)

- **Text** – die anzusagende Zeichenkette. GROSSBUCHSTABEN werden
  buchstabiert (z. B. „OFF“ → „O-F-F“), Kleinbuchstaben werden als Wort
  ausgesprochen („off“).
- **Wiederholung**, **Beim Start überspringen** – wie oben.

**Zu Bildschirm wechseln** – schaltet die Anzeige auf einen ausgewählten
Bildschirm um, z. B. Sprung zur Flugdatenaufzeichnung eines Empfängers
per Tastendruck:

![Zu Bildschirm wechseln](../assets/model-sf-go-to-screen.png)
![Bildschirmoptionen](../assets/model-sf-go-to-screen-options.png)

**Touchscreen sperren** – sperrt den Touchscreen gegen unbeabsichtigte
Eingaben (auch direkt erreichbar, indem `ENT` + `PAGE` vom
Startbildschirm aus 1 s lang gemeinsam gedrückt gehalten werden):

![Touchscreen sperren](../assets/model-sf-lock-touchscreen.png)

**Modell laden** – lädt beim Auslösen ein festgelegtes **Modell**,
optional mit einer **Bestätigungsabfrage**, bevor tatsächlich
umgeschaltet wird:

![Modell laden](../assets/model-sf-load-model.png)

**Vario ausgeben** – steuert die Vario-Audioausgabe anhand einer
gewählten Quelle (normalerweise der VSpeed-Sensor eines FrSky-Varios,
aber jeder Sensor mit der Einheit m/s funktioniert):

![Vario ausgeben](../assets/model-sf-play-vario.png)
![Vario-Quelle: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Bereich** – Steig-/Sinkrate, die auf die Tonhöhe abgebildet wird,
  Standard ±10 m/s (bis zu ±100 m/s). Oberhalb von **Mitte** steigt die
  Tonhöhe linear mit der Steigrate bis zum maximalen Bereichswert an (die
  Tonhöhe bei maximaler Rate wird unter [Allgemein →
  Vario](../system-setup/general.md#vario) eingestellt); beim Sinken
  ertönt ein durchgehender Ton, dessen Tonhöhe zum minimalen
  Bereichswert hin abfällt.
- **Mitte** – das Band für „kein Steigen“, Standard ±0,3 m/s (bis zu
  ±2 m/s); innerhalb dieses Bandes bleibt die Tonhöhe konstant (die
  Tonhöhe bei Rate null wird ebenfalls unter Allgemein → Vario
  eingestellt). Schalten Sie **Ton**→**Stumm**, um den Ton vollständig
  stummzuschalten.

  ![Optionen für Vario-Bereich/Mitte](../assets/model-sf-play-vario-options.png)
