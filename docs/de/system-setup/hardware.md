---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Hardware-Prüfung](../assets/system-hardware-check-x20s.png)

Prüfen und Kalibrieren der physischen Bedienelemente des Senders, Festlegen
der Schaltertypen sowie der Belegung der Home-Tasten.

## Hardware-Prüfung {: #hardware-check }

Hier lässt sich jedes physische Eingabeelement betätigen, um zu überprüfen,
ob es korrekt erkannt wird.

![Hardware-Prüfung X20 Pro](../assets/system-hardware-check-x20pro.png)
![Hardware-Prüfung X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — prüft zusätzlich die beiden rastenden Drucktaster **K**
  und **L** an den hinteren Schultern sowie die zusätzlichen Trimmungen
  **T5**/**T6**.
- **X18** — prüft zusätzlich die Trimmungen **T5**/**T6**.

## Kalibrierung der Analoggeber {: #analogs-calibration }

![Kalibrierung der Analoggeber](../assets/system-hardware-analogs-calibration.png)

Teilt dem Sender exakt mit, wo Mitte und Endpunkte jedes Steuerknüppels,
Potentiometers und Schiebereglers liegen. Läuft beim ersten Start
automatisch ab; nach dem Austausch eines Steuerknüppels, Potentiometers oder
Schiebereglers ist die Kalibrierung zu wiederholen.

## Gyro-Kalibrierung

![Gyro-Kalibrierung](../assets/system-hardware-gyro-calibration.png)

Kalibriert den eingebauten Gyro, damit neigungsbasierte Eingaben korrekt auf
das Kippen des Senders reagieren — als „waagerecht“ gilt dabei die Haltung,
in der Sie den Sender normalerweise halten. Läuft ebenfalls beim ersten
Start automatisch ab.

## Analogfilter

Ein ein-/ausschaltbarer ADC-Filter für die Steuerknüppel, standardmäßig
aktiv — er reduziert das Zittern um die Knüppelmitte. Dies ist die
**globale** Einstellung; unter [Modell bearbeiten](../model-setup/model-edit.md)
gibt es zusätzlich eine **modellspezifische** Übersteuerung des Analogfilters.

## Einstellungen für Potentiometer/Schieberegler {: #potssliders-settings }

Hier lassen sich die Potentiometer und Schieberegler umbenennen. Der
**X20 Pro/R/RS** unterstützt zusätzlich zwei weitere Potentiometer,
**Ext1**/**Ext2**, die typischerweise für 3-Achs-Steuerknüppel verwendet
werden.

![ADC-Werte, Potentiometer](../assets/system-hardware-pots-x20s.png)
![ADC-Werte, Potentiometer (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Schaltereinstellungen {: #switches-settings }

![Schalter](../assets/system-hardware-switches.png)

- **Verzögerung der Mittenerkennung** — verhindert, dass ein schnelles
  Umlegen eines 3-Positionen-Schalters von oben nach unten (oder umgekehrt)
  kurzzeitig die Mittelstellung auslöst; die Mittelstellung soll nur dann
  registriert werden, wenn der Schalter dort tatsächlich stehen bleibt. Der
  Standardwert beträgt 0 ms und ist auf die „Selbsttest“-Erkennung von
  FrSky-Stabilisierungsempfängern auf CH12 abgestimmt.
- **Schaltertyp** — SA–SJ können jeweils als **Kein**, **Taster**,
  **2 POS** oder **3 POS** definiert werden, sodass sich Funktionen
  zwischen physischen Schaltern tauschen lassen (z. B. dem Taster SH die
  Rolle des sonst üblichen 2-Positionen-Schalters SF zuweisen) — abhängig
  davon, was die Verdrahtung des Senders tatsächlich zulässt (eine
  3-Positionen-Funktion lässt sich in der Regel keiner Hardware zuweisen,
  die dafür nicht verdrahtet ist).

  ![Schalteroptionen](../assets/system-hardware-switches-options.png)
  ![Zusätzliche Schalter](../assets/system-hardware-switches-2.png)

- **Umbenennen** — Schalter können von SA–SJ auf eigene Namen umbenannt
  werden; die Namen gelten global für alle Modelle.
- **X20 Pro** — bietet zusätzlich die Drucktaster **K**/**L** an den
  hinteren Schultern sowie die Positionen **M**/**N**, sofern verdrahtet
  (typischerweise für Schalter an den Knüppelenden).

## Belegung der Home-Tasten

Legt neu fest, wohin die Home-Tasten `SYS`, `MDL` und `DISP` (`TELE` bei
älteren Sendern) springen.

- **`DISP`** — sowohl kurzer als auch langer Tastendruck lassen sich einer
  beliebigen Modellseite, Systemseite, Bildschirme konfigurieren, Start oder
  der Flugdatenaufzeichnung zuweisen. Aus Konsistenzgründen zur X10-Serie
  wird der lange Druck auf `DISP` üblicherweise auf Bildschirme konfigurieren
  gelegt.
- **`SYS`/`MDL`** — nur der lange Tastendruck ist frei belegbar (mit
  denselben Zielen); ein kurzer Druck öffnet stets den System- bzw.
  Modellbereich.

## Senderspezifische Hardware-Optionen {: #radio-specific-hardware-options }

- **Aktivieren von Haptik-Upgrades der Steuerknüppel** (X20 Pro, X20R) — der
  X20 Pro AW und der X20RS werden mit MC20R-Steuerknüppeln ausgeliefert, die
  über haptische Vibrationsmotoren verfügen; wurden MC20R-Steuerknüppel in
  einen X20 Pro oder X20R nachgerüstet, sind sie hier zu aktivieren (die
  Konfiguration der Haptikmuster selbst ist unter
  [Sonderfunktionen](../model-setup/special-functions.md) beschrieben).

  ![Haptik (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptik (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Encoder-Option** (X20 Pro AW, X20R/RS) — diese Sender besitzen einen
  empfindlicheren Drehgeber; aktivieren Sie **Halbschritte**, um ihn
  unempfindlicher zu machen.

  ![Encoder-Option (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## ADC-Werteanzeige {: #adc-value-inspector }

Zeigt die rohen Analog-Digital-Wandlerwerte an, die die CPU für jeden
Analogeingang einliest:

![ADC-Prüfung (X20S)](../assets/system-hardware-adc-check-x20s.png)
![ADC-Prüfung (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 linker Steuerknüppel horizontal, 2 linker Steuerknüppel
vertikal, 3 rechter Steuerknüppel vertikal, 4 rechter Steuerknüppel
horizontal, 5 Poti 1, 6 Poti 2, 7 mittlerer Schieberegler, 8 linker
Schieberegler, 9 rechter Schieberegler.

**X20 Pro**: wie oben, jedoch mit zwei zusätzlichen Kanälen für externe
Potentiometer (7 Ext1, 8 Ext2 — z. B. knüppelmontierte Potentiometer), die
vor den Schiebereglern eingefügt sind; diese verschieben sich auf
9 mittlerer Schieberegler, 10 linker Schieberegler, 11 rechter
Schieberegler.
