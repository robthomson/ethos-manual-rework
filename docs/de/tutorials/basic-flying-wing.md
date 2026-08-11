---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Beispiel für ein Nurflügel-Flugzeug (Elevon)

Ein Nurflügler mit 2 Servos für die Elevons, wobei wir die von Dreamflight
Weasel empfohlenen Raten, Expo- und Mischungsverhältnisse als konkretes
durchgerechnetes Beispiel verwenden. Führen Sie zuvor die
[Ersteinrichtung des Senders](initial-radio-setup.md) durch.

## Schritt 1. Bestätigen Sie die Systemeinstellungen {: #step-1-confirm-system-settings }

Standard-Kanalreihenfolge **AETR**, wobei die Einstellung **[Erste vier Kanäle
fest](../system-setup/controls.md#first-four-channels-fixed)** auf **AUS**
stehen sollte. Verwenden Sie die Funktion
[HF-System](../model-setup/rf-system.md), um Ihren Empfänger zu registrieren
(wenn Ihr Empfänger ACCESS ist) und zu binden, bevor Sie fortfahren.

## Schritt 2. Identifizieren Sie die benötigten Servos/Kanäle

Bei einem Nurflügelmodell werden die [Mischer](../model-setup/mixes.md)
verwendet, um die Querruder- und Höhenrudereingänge zu kombinieren, damit beide
auf die beiden Ruderflächen wirken — insgesamt also nur 2 Kanäle, von denen
jeder eine Mischung beider Eingänge darstellt.

## Schritt 3. Erstellen Sie ein neues Modell

![Flugzeugmodell erstellen](../assets/tut-wing-eg-wiz-create-airplane.png)

Starten Sie aus der [Modellauswahl](../model-setup/model-select.md) heraus den
Assistenten **Flugzeug** und wählen Sie die Option **Nicht stabilisierter
Empfänger**.

![Kein Motor](../assets/tut-wing-eg-wiz-no-engine.png)

Wählen Sie für den Motor **Kein Motor**, akzeptieren Sie die Standardeinstellung
von 2 Kanälen für die Querruder und wählen Sie **Keine Klappen**.

![Kein Leitwerk](../assets/tut-wing-eg-wiz-no-tail.png)

Wählen Sie **Keine Auswahl** für den Leitwerk-Typ — dadurch erstellt Ethos
automatisch die Elevon-Mischung (Querruder- und Höhenrudereingänge, beide auf
dieselben zwei Kanäle). Geben Sie dem Modell einen Namen (z. B. „Weasel"),
wählen Sie ein Bitmap-Bild dafür aus und folgen Sie dem Assistenten bis zum
Ende — das Modell wird zum aktiven Modell in der Gruppe „Flugzeug".

## Schritt 4. Überprüfung und Konfiguration der Mischer

![Übersicht der Mischer](../assets/tut-wing-eg-mixes.png)

Der Assistent hat einen Querrudermischer auf den Kanälen 1 und 2 erstellt,
gefolgt von einem Höhenrudermischer, *ebenfalls* auf den Kanälen 1 und 2. Das
bedeutet, dass beide Eingangssteuerungen auf die beiden Elevon-Kanäle wirken —
und genau darin besteht der Trick der Elevon-Mischung.

### Querruder

![Querrudermischer](../assets/tut-wing-eg-mixes-ail-mix.png)

**Gewichtung/Anteile** — im Weasel-Handbuch sind die empfohlenen Ausschläge für
das Querruder etwa dreimal größer als für das Höhenruder, und beide zusammen
sollen 100 % ergeben: **75 %** Querruder, **25 %** Höhenruder. Die niedrigen
Werte betragen etwa 50 % der hohen Werte: **36 %** für die niedrigen Raten des
Querruders und **12 %** für die niedrigen Raten des Höhenruders.

![Gewichtung des Querrudermischers](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — die von Weasel empfohlenen Expo-Werte sind 35 % für hoch und 20 %
für niedrig, aktiv in der SB-Schalterstellung nach unten; die Reaktion wird
dadurch in der Knüppelmitte flacher.

**Differenzierung** — bei dieser Zelle recht klein, etwa **4 %**:

![Querruderdifferenzierung](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Warum die Differenzierung wichtig ist, erläutert das [Grundlegende Beispiel
für ein Flächenflugzeug](basic-fixed-wing.md#ailerons) — die Überlegungen zum
negativen Gieren gelten hier ebenso.)

### Höhenruder

![Höhenrudermischer](../assets/tut-wing-eg-mixes-ele-mix.png)

Nach demselben Schema: **25 %**/**12 %** für hohe und niedrige Raten, und wir
verwenden die gleichen Expo-Werte wie für die Querruder.

### Seitenruder

![Seitenrudermischer](../assets/tut-wing-eg-mixes-rud-mix.png)

Der Weasel hat kein Seitenruder, er braucht auch keines — Nurflügel-Modelle
benötigen in der Regel keines. Wird bei einem Elevon-Modell *doch* eines
benötigt, verwenden Sie einen [Freien
Mischer](../model-setup/mixes.md#mix-libraries), um ein Seitenruder auf Kanal 3
hinzuzufügen.

## Schritt 5. Binden des Empfängers

Wie in [Schritt 1](#step-1-confirm-system-settings) — registrieren und binden
Sie den Empfänger, bevor Sie fortfahren. Um Schäden durch versehentliches
Übersteuern Ihrer Servos zu vermeiden, wäre es ratsam, Ihre Servoanlenkungen zu
trennen oder den Servoweg zu reduzieren, bis Sie bereit sind, die
Servo-Min/Max-Grenzen zu konfigurieren.

## Schritt 6. Überprüfen Sie die Mischer

Die Ausgangskanäle 1 und 2 können in **Elevon1** und **Elevon2** umbenannt
werden. Bei vollem Querruderausschlag nach rechts steht Kanal 1 (rechts, nach
oben) auf 75 %, während Kanal 2 (links, nach unten) 72 % beträgt — die Differenz
von 3 % *ist* die wirkende Querruderdifferenz. Kommt zusätzlich voller
Höhenruderausschlag nach unten hinzu, liegt Kanal 1 bei 75+25 = 100 % und
Kanal 2 bei 72−25 = 47 %.

## Schritt 7. Konfigurieren Sie die maximalen Servowege

![Voller Querruderausschlag](../assets/tut-wing-eg-outputs-full-ail.png)
![Voller Querruder- und voller Höhenruderausschlag](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Beginnen Sie mit der Einstellung der Servo-Mittelpunkte mit Hilfe der
**PWM-Mitte**-Einstellung. Die vom Weasel empfohlenen maximalen Ausschläge sind
25 mm (Querruder) + 10 mm (Höhenruder) = 35 mm gesamt — geben Sie sowohl volle
gleichsinnige *als auch* volle gegensinnige Querruder-/Höhenrudereingaben und
achten Sie darauf, dass die Servo- und Anlenkungsgrenzen nicht überschritten
werden, bevor Sie die endgültigen Ausschläge festlegen.

- **Min/Max** — „harte" Grenzwerte, die nicht überschrieben werden können; eine
  Verringerung dieser Grenzwerte verringert den Weg und führt nicht zum
  Abschneiden der oberen Werte. Standardmäßig ±100 %, bei Bedarf erweiterbar
  auf ±150 %.
- **Kurve** — oft schneller und flexibler, als direkt mit Min/Max/Subtrim zu
  jonglieren, und Sie erhalten eine schöne Grafik. Verwenden Sie eine
  3-Punkt-Kurve für die meisten Ausgänge; eine 5-Punkt-Kurve auf dem zweiten
  Elevon erleichtert es, den Weg an 5 Punkten mit dem ersten zu synchronisieren.
  Bei Verwendung einer Kurve empfiehlt es sich, Min, Max und Subtrim auf ihren
  neutralen Werten zu belassen (−100/100/0 bzw. −150/150/0, wenn Sie erweiterte
  Grenzwerte verwenden), und die Formgebung der Kurve zu überlassen.
