---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Spezialfunktionen

![Menü der Spezialfunktionen](../assets/model-sf-menu.png)

Spezialfunktionen lösen eine Aktion aus – Audio abspielen, Screenshot,
Logs schreiben, haptisches Feedback und mehr –, sobald eine Bedingung
wahr wird. Es werden bis zu 100 Spezialfunktionen unterstützt; es gibt
keine voreingestellten. Mit **+** fügen Sie eine hinzu; tippen Sie eine
vorhandene an, um sie zu **bearbeiten**/**verschieben**/**kopieren und
einzufügen**/**klonen**/**löschen**.

![Spezialfunktion hinzufügen](../assets/model-sf-add.png)
![Verschieben](../assets/model-sf-move.png)

## Felder, die alle Aktionen gemeinsam haben

- **Zustand** – aktiviert oder deaktiviert diese Sonderfunktion, ohne sie
  zu löschen.
- **Aktiviert durch** – **Immer an** (EIN), oder aktiviert durch
  Schalterstellungen, Funktionsschalter, Logikschalter, Trimmstellungen
  oder Flugmodi. Drücken Sie lange `ENT` auf dem Schalternamen und
  aktivieren Sie das Kontrollkästchen **Negativ**, um den Schalter zu
  invertieren (z. B. wird aus `SG-up` dann `!SG-up`, aktiv also immer
  dann, wenn sich SG *nicht* in der oberen Position befindet).
- **Global** – fügt diese Funktion **allen** bestehenden Modellen und
  allen neuen Modellen hinzu, die in Zukunft erstellt werden. Wenn ein
  bestehendes Modell eine identisch konfigurierte lokale Funktion bereits
  hat, wird die globale Funktion als neue Funktion hinzugefügt; wenn Sie
  die globale Funktion wieder deaktivieren, wird die Funktion von allen
  Modellen mit Ausnahme des aktuell ausgewählten Modells entfernt.
  Globale Spezialfunktionen werden in der Datei `radio.bin` gespeichert,
  lokale Funktionen in der Modelldatei.

## Aktionen {: #actions }

**Zurücksetzen** – setzt **Flugdaten** (Telemetrie und Timer),
**Stoppuhren alle** oder **Telemetrie gesamt** zurück.

![Zurücksetzen](../assets/model-sf-reset.png)

**Screenshot** – speichert einen Screenshot im Ordner `screenshots/` auf
der SD card oder dem eMMC.

![Screenshot](../assets/model-sf-screenshot.png)

**Failsafe setzen** – übernimmt die aktuellen Kanalpositionen als
Failsafe, entweder über das interne oder das externe HF-**Modul**.

![Failsafe setzen](../assets/model-sf-set-failsafe.png)

**AUDIO abspielen** – die umfangreichste Aktion, die eine vollständige
Sequenz unterstützt:

![AUDIO abspielen](../assets/model-sf-play-audio.png)

- **Stimme** – welche der bis zu 3 konfigurierten Stimmen verwendet werden
  soll (siehe [Allgemein](../system-setup/general.md#audio-settings)).
- **wiederholen** – einmal abspielen oder in einem einstellbaren Intervall
  wiederholen (bis zu 10 Minuten).
- **Nicht beim Start** – verhindert, dass diese Funktion beim Starten
  ausgelöst wird.
- **Sequenz** – bis zu 100 Schritte, jeweils einer von:

  - **Datei abspielen** – gibt die ausgewählte Audiodatei wieder.

    ![Datei abspielen](../assets/model-sf-play-audio-add-play-file.png)

  - **Wert ansagen** – gibt den Wert der ausgewählten Quelle wieder:
    Analogwerte, Schalter, Logische Schalter, Trimmungen, Kanäle, Kreisel,
    Systemuhr, Trainer, Stoppuhren oder Telemetrie.

    ![Wert ansagen](../assets/model-sf-play-audio-add-play-value.png)

  - **Wartezeit** – fügt eine feste Verzögerung von bis zu 10 Minuten ein.
  - **Bedingung abwarten** – hält die Sequenz an, bis die Wartebedingung
    erfüllt ist.

  ![Sequenzzeile hinzufügen](../assets/model-sf-play-audio-add-line.png)
  ![Typ der Sequenzzeile](../assets/model-sf-play-audio-add-line-type.png)

  Zum Beispiel: `vfrlow.wav` abspielen, sobald der Logikschalter
  `VFRlow` aktiv wird, und anschließend den (von der Telemetrie)
  aufgezeichneten minimalen VFR-Wert ansagen –

  ![Wert nach Datei ansagen](../assets/model-sf-play-audio-add-play-value-add-line.png)

  – oder eine Sequenz anhalten, bis der Schalter SH in die untere Position
  gebracht wird, bevor es weitergeht:

  ![Sequenz mit Wartebedingung](../assets/model-sf-play-audio-add-sequence.png)

  Wenn Sie auf eine Sequenzzeile tippen, können Sie die Zeile bearbeiten,
  eine neue Zeile hinzufügen, die Reihenfolge ändern oder die Zeile
  löschen:

  ![Verwaltung der Sequenzen](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptik** – haptische Vibrationen als Rückmeldung:

![Haptik](../assets/model-sf-haptic.png)

- **Muster** – einfach, doppelt, dreifach, fünffach oder sehr kurz.

  ![Vibrationsmuster](../assets/model-sf-haptic-pattern.png)

- **Intensität** – 1 bis 10 (Standardeinstellung 5).
- **wiederholen** – einmalig oder in der hier eingegebenen Häufigkeit.
- **Haptikmotoren auswählen** – bei Sendern mit Haptikmotoren in den
  Steuerknüppeln (X20 Pro AW, X20RS oder ein X20 Pro/X20R, der mit
  MC20R-Gimbals nachgerüstet wurde – siehe
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Standard** (interne Haptik), **Alle Motoren**, **Haptik linker
  Knüppel** oder **Haptik rechter Knüppel**.

  ![Haptik beim X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Logs schreiben** – schreibt Protokolldateien im „.csv“-Format in den
Ordner `Logs/` auf der SD card oder dem eMMC. Die Zeit und das Datum der
RTC werden zusammen mit den Daten protokolliert und sind wichtig, um die
Flugsitzungen später auseinanderhalten zu können:

![Logs schreiben](../assets/model-sf-write-logs.png)

- **Schreibe Intervall** – 100 bis 500 ms.
- **Steuerknüppel/Potis/Sliders**, **Schalter**, **Logische Schalter**,
  **Kanäle** – unabhängig voneinander schaltbare
  Protokollierungskategorien.

  **Log Viewer**: Um Protokolldateien anzuzeigen, öffnen Sie im
  Datei-Manager eine Protokolldatei im Ordner `/Logs`. Wählen Sie die
  Kanäle aus, die dargestellt werden sollen (RSSI ist standardmäßig
  ausgewählt); die Anzeige kann mit dem Drehgeber oder durch Wischen
  verschoben und durch Drehen des Drehgebers bei gedrückter
  `PAGE`-Taste vergrößert oder verkleinert werden. Mit `DISP` wird der
  Fokus auf die erste Schaltfläche in der rechten Spalte gesetzt.

**Text abspielen** (nur X20 Pro) – erzeugt gesprochenen Text direkt im
Sender, anstatt eine zuvor vorbereitete Datei abzuspielen:

![Text abspielen](../assets/model-sf-x20pro-play-text.png)

- **Text** – die vom Benutzer angegebene Textfolge, die gesprochen werden
  soll. Die Verwendung von Großbuchstaben führt dazu, dass das Wort
  Buchstabe für Buchstabe buchstabiert wird (z. B. wird „OFF“ als
  „O-F-F“ wiedergegeben); Kleinbuchstaben werden als Wort ausgesprochen
  („off“).
- **wiederholen**, **Nicht beim Start** – wie oben.

**Weiter zum Bildschirm** – schaltet die Anzeige auf eine ausgewählte
Bildschirmseite um, z. B. auf den Flugdatensatz eines Empfängers, wenn
eine Drucktaste gedrückt wird:

![Weiter zum Bildschirm](../assets/model-sf-go-to-screen.png)
![Bildschirmoptionen](../assets/model-sf-go-to-screen-options.png)

**Bildschirm sperren** – sperrt den Touchscreen, um eine versehentliche
Bedienung zu verhindern (auch direkt verfügbar durch gleichzeitiges
Drücken von `ENT` und `PAGE` für 1 Sekunde auf dem Startbildschirm):

![Bildschirm sperren](../assets/model-sf-lock-touchscreen.png)

**Modell laden** – lädt beim Auslösen ein bestimmtes **Modell**, optional
mit einer **Bestätigung**, bevor tatsächlich umgeschaltet wird:

![Modell laden](../assets/model-sf-load-model.png)

**Vario abspielen** – steuert die Vario-Tonausgabe anhand einer
ausgewählten Quelle (normalerweise der VSpeed-Sensor eines FrSky-Varios,
es funktioniert aber jeder Sensor mit der Einheit m/s):

![Vario abspielen](../assets/model-sf-play-vario.png)
![Vario-Quelle: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Bereich** – die Steig-/Sinkrate, die auf die Tonhöhe abgebildet wird,
  standardmäßig ±10 m/s (bis zu ±100 m/s). Oberhalb der **Mitte** steigt
  die Tonhöhe linear mit der Steigrate bis zum maximalen Bereichswert an
  (die Tonhöhe bei maximaler Rate wird unter [Allgemein →
  Vario](../system-setup/general.md#vario) eingestellt); beim Sinken
  ertönt ein durchgehender Ton, dessen Tonhöhe zum minimalen
  Bereichswert hin abfällt.
- **Mitte** – der Bereich für „kein Steigen“, standardmäßig ±0,3 m/s (bis
  zu ±2 m/s); innerhalb dieses Bereichs bleibt die Tonhöhe konstant (die
  Tonhöhe bei Rate null wird ebenfalls unter Allgemein → Vario
  eingestellt). Schalten Sie von **Ton** auf **Stumm** um, um den Ton
  vollständig abzuschalten.

  ![Optionen für Vario-Bereich/Mitte](../assets/model-sf-play-vario-options.png)
