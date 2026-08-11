---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Beispiel: Einfacher Nurflügler (Elevon)

Ein Nurflügler mit 2-Servo-Elevon-Ansteuerung, mit den vom Hersteller
empfohlenen Rates/Expo/Mischverhältnissen des Dreamflight Weasel als
konkretes durchgerechnetes Beispiel. Führen Sie zuvor die
[Grundeinrichtung des Senders](initial-radio-setup.md) durch.

## Schritt 1. Systemeinstellungen prüfen {: #step-1-confirm-system-settings }

Standardreihenfolge **AETR**, mit **[Erste vier Kanäle
fixiert](../system-setup/controls.md#first-four-channels-fixed)** auf
**AUS**. Registrieren Sie den Empfänger (bei ACCESS) und binden Sie ihn
über [RF-System](../model-setup/rf-system.md), bevor Sie fortfahren.

## Schritt 2. Benötigte Servos/Kanäle bestimmen

Bei einer Elevon-Zelle kombinieren [Mischer](../model-setup/mixes.md) die
Querruder- und Höhenrudereingaben auf beide physischen Ruderflächen — insgesamt
also nur 2 Kanäle, von denen jeder eine Mischung beider Eingaben darstellt.

## Schritt 3. Neues Modell anlegen

![Flugzeugmodell anlegen](../assets/tut-wing-eg-wiz-create-airplane.png)

Starten Sie aus der [Modellauswahl](../model-setup/model-select.md) heraus den
Assistenten **Flugzeug** und wählen Sie **Nicht stabilisierter Empfänger**.

![Kein Motor](../assets/tut-wing-eg-wiz-no-engine.png)

Wählen Sie **Kein Motor**, übernehmen Sie die voreingestellten 2
Querruderkanäle und wählen Sie **Keine Klappen**.

![Kein Leitwerk](../assets/tut-wing-eg-wiz-no-tail.png)

Wählen Sie als Leitwerkstyp **Keines** — genau dadurch erzeugt Ethos
automatisch die Elevon-Mischung (Querruder- und Höhenrudereingaben, beide auf
dieselben zwei Kanäle). Benennen Sie das Modell (z. B. „Weasel"), wählen Sie
eine Bitmap und schließen Sie den Assistenten ab — das Modell wird zum aktiven
Modell in der Kategorie Flugzeug.

## Schritt 4. Mischer prüfen und konfigurieren

![Übersicht der Mischer](../assets/tut-wing-eg-mixes.png)

Der Assistent legt einen Querruder-Mischer auf den Kanälen 1+2 an, gefolgt von
einem Höhenruder-Mischer *ebenfalls* auf den Kanälen 1+2 — beide Eingaben
wirken auf beide Elevon-Kanäle, und genau darin besteht der Trick der
Elevon-Mischung.

### Querruder

![Querruder-Mischer](../assets/tut-wing-eg-mixes-ail-mix.png)

**Gewichtung/Rates** — laut Anleitung des Weasel sollte der Querruderausschlag
etwa 3× so groß sein wie der des Höhenruders, und beide zusammen sollten 100 %
ergeben: **75 %** Querruder, **25 %** Höhenruder. Die niedrigen Rates
entsprechen etwa der Hälfte der hohen: **36 %** Querruder niedrig, **12 %**
Höhenruder niedrig.

![Gewichtung des Querruder-Mischers](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — vom Weasel empfohlen sind 35 % hoch / 20 % niedrig, aktiv bei
Schalter SB unten; dadurch wird die Reaktion um die Knüppelmitte herum
abgeflacht.

**Differential** — bei dieser Zelle gering, etwa **4 %**:

![Querruder-Differential](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Warum Differential wichtig ist, erläutert das [Beispiel: Einfaches
Flächenmodell](basic-fixed-wing.md#ailerons) — die Überlegungen zum negativen
Wendemoment gelten hier ebenso.)

### Höhenruder

![Höhenruder-Mischer](../assets/tut-wing-eg-mixes-ele-mix.png)

Dasselbe Schema: **25 %**/**12 %** für hohe/niedrige Rates, dieselben
Expo-Werte wie beim Querruder.

### Seitenruder

![Seitenruder-Mischer](../assets/tut-wing-eg-mixes-rud-mix.png)

Der Weasel hat keines — Nurflügler benötigen in der Regel kein Seitenruder.
Wird bei einem Elevon-Modell *doch* eines benötigt, fügen Sie es als [Freien
Mischer](../model-setup/mixes.md#mix-libraries) auf Kanal 3 hinzu.

## Schritt 5. Empfänger binden

Wie in [Schritt 1](#step-1-confirm-system-settings) — registrieren/binden Sie
den Empfänger, bevor Sie fortfahren. Erwägen Sie außerdem, die
Servoanlenkungen auszuhängen oder die Wege zu reduzieren, bis die Min-/Max-Grenzen
eingestellt sind, um Überlastungen zu vermeiden.

## Schritt 6. Mischer überprüfen

Die Ausgangskanäle 1/2 können in **Elevon1**/**Elevon2** umbenannt werden. Bei
vollem Querruderausschlag nach rechts zeigt Kanal 1 (rechts, nach oben) 75 %
an, Kanal 2 (links, nach unten) dagegen 72 % — die Differenz von 3 % *ist* das
wirkende Differential. Kommt zusätzlich voller Höhenruderausschlag nach unten
hinzu, ergibt sich für Kanal 1 75+25 = 100 % und für Kanal 2 72−25 = 47 %.

## Schritt 7. Maximale Servowege einstellen

![Voller Querruderausschlag](../assets/tut-wing-eg-outputs-full-ail.png)
![Voller Querruder- + voller Höhenruderausschlag](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Zentrieren Sie zunächst jedes Servo mit **PWM-Mitte**. Der vom Weasel
empfohlene Maximalausschlag beträgt 25 mm Querruder + 10 mm Höhenruder =
35 mm gesamt — geben Sie sowohl volle gleichsinnige *als auch* volle
gegensinnige Querruder-/Höhenrudereingaben und prüfen Sie, dass weder
mechanische noch Servogrenzen überschritten werden, bevor Sie die endgültigen
Ausschläge festlegen.

- **Min/Max** — feste Grenzen, die nie überschritten werden; ein Verringern
  reduziert den Weg, anstatt ihn abzuschneiden. Standard ±100 %, bei Bedarf
  erweiterbar auf ±150 %.
- **Kurve** — oft schneller und flexibler, als direkt mit Min/Max/Subtrim zu
  jonglieren, mit dem Vorteil einer Live-Grafik. Für die meisten Ausgänge
  genügt eine 3-Punkt-Kurve; eine 5-Punkt-Kurve auf dem zweiten Elevon
  erleichtert es, den Weg an 5 Punkten mit dem ersten abzugleichen. Wenn Sie
  hierfür eine Kurve verwenden, belassen Sie Min/Max/Subtrim auf ihren
  neutralen Werten (−100/100/0 bzw. −150/150/0 bei erweiterten Grenzen) und
  überlassen Sie die Formgebung der Kurve.
