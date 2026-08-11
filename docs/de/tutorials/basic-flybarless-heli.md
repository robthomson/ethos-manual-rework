---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Beispiel: Einfacher Flybarless-Heli

Eine grundlegende Konfiguration für einen Flybarless-Helikopter (FBL), am
Beispiel eines Reglers wie dem Spirit. Anders als ein Flächenmodell ist ein
Helikopter von Natur aus instabil — die FBL-Einheit verwendet Gyros
(Drehrate) und Beschleunigungssensoren (Bewegung/Lage), um Korrekturen für
Gier, Nick und Roll über einen abgestimmten PID-Regelkreis (Proportional-
Integral-Differential) zu berechnen. Dabei werden Stabilität, Reaktions-
freudigkeit und Überschwingen anhand der konkreten physikalischen und
elektrischen Eigenschaften des jeweiligen Helikopters ausbalanciert.

Dieses Tutorial behandelt ausschließlich die Seite der
**Senderprogrammierung** — für alles Weitere ziehen Sie die Dokumentation
Ihrer FBL-Einheit heran; solide allgemeine Helikopterkenntnisse werden
vorausgesetzt.

!!! danger
    Entfernen Sie aus Sicherheitsgründen vor Beginn die Rotorblätter.

## Schritt 1. Systemeinstellungen prüfen

Kanalreihenfolge **AETR**, **[Erste vier Kanäle
fest](../system-setup/controls.md#first-four-channels-fixed)** **AUS**
— Spirit-FBL-Einheiten erwarten die SBUS-Kanäle genau in dieser
Reihenfolge (obwohl sie intern in ihrer eigenen Konfiguration TAER
verwenden). Registrieren Sie den Empfänger (bei ACCESS) und binden Sie ihn
über [RF System](../model-setup/rf-system.md).

## Schritt 2. Benötigte Servos/Kanäle ermitteln

| Funktion | Kanal |
|---|---|
| Roll (Querruder) | — |
| Nick (Höhenruder) | — |
| Gas | — |
| Gier (Seitenruder) | — |
| Gyro-Gain | 5 |
| Kollektivpitch | 6 |
| Einstellungsbank | 7 |
| Rescue | 8 |

## Schritt 3. Neues Modell anlegen

![Heli-Modell anlegen](../assets/tut-heli-eg-wiz-create-heli.png)

Legen Sie in der [Modellauswahl](../model-setup/model-select.md) eine
Heli-Kategorie an bzw. wählen Sie eine aus, starten Sie den Assistenten und
wählen Sie **Flybarless**:

![FBL-Auswahl](../assets/tut-heli-eg-wiz-fbl.png)
![Modellname](../assets/tut-heli-eg-wiz-name.png)

Vergeben Sie einen Namen und wählen Sie ein Bild.

## Schritt 4. Mischer prüfen und konfigurieren

![Mischer-Übersicht](../assets/tut-heli-eg-mixes.png)

Der Assistent erstellt Querruder/Höhenruder/Gas/Seitenruder in
AETR-Reihenfolge, Pitch auf Kanal 6 und FBL-Bank auf Kanal 7:

![Pitch-Mischer](../assets/tut-heli-eg-mixes-pitch.png)

Prüfen Sie, ob Kanal 6 dem Kollektivpitch zugeordnet ist. Zwei weitere
Kanäle müssen manuell als [Freie
Mischer](../model-setup/mixes.md#mix-libraries) hinzugefügt werden:
**Gyro-Gain** (Kanal 5) und **Rescue/Stabi** (Kanal 8).

**Querruder/Höhenruder/Seitenruder** — hier ist nichts zu ergänzen; Raten
und Expo sind Aufgabe der FBL-Einheit, der Sender gibt lediglich ein
sauberes lineares Signal weiter.

![Querruder-Mischer](../assets/tut-heli-eg-mixes-ail.png)

**Kollektivpitch** — eine gerade lineare Kurve; prüfen Sie lediglich den
Ausgangskanal (normalerweise 6). Wie oben werden Raten/Expo von der
FBL-Einheit verarbeitet, nicht hier.

**FBL-Bank** — die drei Einstellungsbänke des Spirit (unterschiedliche
Flugstile, Sensor-Gains bei verschiedenen Drehzahlen oder
Beginner/Acro/3D — oder schlicht Tuning-Presets), zugewiesen auf einen
3-Stufen-Schalter, z. B. SE:

![Bank-Mischer](../assets/tut-heli-eg-mixes-bank.png)

**Gyro-Gain** — als Freien Mischer nach dem letzten Kanal hinzufügen. Der
Gain ist typischerweise ein fester Wert: Setzen Sie die **Quelle** auf
Spezialwert 0, stellen Sie den Gain über den **Offset** ein (Feinabstimmung
später im Flug) und geben Sie ihn auf Kanal 5 aus:

![Gyro-Gain-Mischer](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Flugphasen konfigurieren

![Flugphasen](../assets/tut-heli-eg-flight-modes.png)

Drei [Flugphasen](../model-setup/flight-modes.md): Benennen Sie die
Standardphase in **Normal** um und fügen Sie **Idle Up 1**/**Idle Up 2**
auf Schalter SD hinzu.

### Gasmischer konfigurieren

Drei Gaskurven, eine je Flugphase, jeweils als [benutzerdefinierte
Kurve](../model-setup/curves.md):

- **Normal** — Hochlauf/Abheben: beginnt bei −100 % (Motor aus) und steigt
  gleichmäßig an. Eine 7-Punkt-Kurve mit aktiviertem **Smooth** funktioniert
  gut; die genauen Werte müssen im Flug abgestimmt werden.

  ![Normal-Kurve](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1** — allgemeines Fliegen: eine geradlinige Kurve für eine
  konstante Gasstellung, die die Rotordrehzahl konstant hält; die Bewegung
  entsteht stattdessen über Kollektivpitch, Querruder (Roll) und Höhenruder
  (Nick). Halten Sie den Übergang von Normal weich — kein großer Sprung.
  (Die meisten FBL-Einheiten bieten zudem eine **Governor**-Funktion, die
  die Rotordrehzahl auch bei aggressiven Manövern konstant hält — siehe das
  Handbuch der FBL-Einheit.)

  ![Idle-Up-1-Kurve](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2** — aggressives Fliegen (Kunstflug, 3D); ebenfalls im Flug
  abzustimmen.

  ![Idle-Up-2-Kurve](../assets/tut-heli-eg-curves-iup2.png)

![Gaskurven in den Mischern](../assets/tut-heli-eg-mixes-thr-curves.png)

**Gas-Abschaltung** — weisen Sie z. B. Schalter SG-oben mit aktiviertem
**Sticky** zu: Das Umlegen von SG nach oben schaltet das Gas sofort ab, und
(wegen Sticky) kann es erst wieder scharfgeschaltet werden, wenn der
Gasknüppel zuvor auf niedrig/aus steht.

![Gas-Abschaltung](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescue/Stabi** — analog zuweisen, z. B. auf Schalter SA und Kanal 8.

![Fertige Mischer](../assets/tut-heli-eg-mixes-final.png)

## Schritt 5. FBL-Einrichtung

1. **Konfigurationssoftware der FBL-Einheit installieren** — z. B. Spirit
   Settings auf einem PC.
2. **Empfänger gemäß Anschlussplan mit der FBL-Einheit verbinden** —
   typischerweise SBUS Out des Empfängers an den RUD-Port der FBL-Einheit
   (einige Spirit-Modelle benötigen einen SBUS-Adapter) oder alternativ über
   F.Port1/FBUS.
3. **FBL-Einheit mit dem PC verbinden** — per Kabel oder Bluetooth, gemäß
   deren Handbuch.

   !!! danger
       Schließen Sie noch keine Servos an.

4. **FBL-Firmware aktualisieren**, falls erforderlich, über den Update-Tab
   der Software.
5. **Allgemeine Einrichtung** (Tab „General“ in Spirit Settings):
   - Empfängertyp: **Futaba SBUS** oder **FrSky F.Port**, je nach Bedarf,
     anschließend neu starten.
   - Kanalzuordnung (mit AETR aus dem Assistenten):

     | Funktion | Kanal |
     |---|---|
     | Gas | 1 |
     | Querruder | 2 |
     | Höhenruder | 3 |
     | Seitenruder | 4 |
     | Gyro | 5 |
     | Pitch | 6 |
     | Bank | 7 |
     | Rescue/Stabi | 8 |

     (Diese Zuordnung ergibt sich daraus, wie die Spirit-Einheit die
     Positionen im SBUS-Datenstrom interpretiert.)

6. **Kanalgrenzen** (Tab „Diagnostic“) — die FBL-Einheit benötigt
   kalibrierte Kanalgrenzen des Senders sowie überprüfte Mittelstellungen:

   - Setzen Sie zunächst sämtliche Subtrimmungen und Trimmungen am Sender
     auf null.
   - Zentrieren Sie den Kollektivpitch-Knüppel so, dass er in den
     [Ausgängen](../model-setup/outputs.md) exakt 1500 µs anzeigt.
   - Schalten Sie die FBL-Einheit ein und prüfen Sie, ob
     Querruder/Höhenruder/Pitch/Seitenruder im Tab „Diagnostic“ jeweils 0 %
     anzeigen (die FBL-Einheit erkennt die Neutralstellung bei jeder
     Initialisierung automatisch).
   - Bewegen Sie jedes Steuerorgan bis an seine Endpunkte und passen Sie die
     zugehörigen Werte **Min**/**Max** in den Ausgängen so an, dass der Tab
     „Diagnostic“ exakt +100 %/−100 % anzeigt; prüfen Sie dabei auch, ob die
     Balkenrichtung mit der Knüppelrichtung übereinstimmt.

   !!! warning
       Verwenden Sie auf diesen Kanälen niemals Subtrimmung oder Trimmung —
       die Spirit-FBL-Einheit interpretiert diese als Steuerbefehle, nicht
       als Kalibrierung.

7. Passen Sie den **Offset** des Gyro-Gain-Mischers an, um Heading Lock zu
   erreichen.

Damit ist die Senderseite vollständig konfiguriert — fahren Sie mit der
weiteren Einrichtung gemäß dem Handbuch der FBL-Einheit fort.
