---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Butterfly-Mischer (Krokodil)

Die Butterfly-Bremsstellung (auch Krähenstellung genannt) steuert die
Sinkgeschwindigkeit, hauptsächlich bei Seglern: Die Querruder fahren
geringfügig nach oben, während die Wölbklappen weit nach unten
ausschlagen, wodurch erheblicher Widerstand entsteht — ideal, um den
Landeanflug zu kontrollieren. Diese Anleitung geht von einem Segler aus,
dessen Klappenkanäle bereits vorhanden sind (angelegt durch den Assistenten
der [Modellauswahl](../model-setup/model-select.md)), und verwendet den
Gasknüppel als Bremseingang: kein Butterfly bei Knüppel oben, zunehmend
mehr, je weiter er nach unten bewegt wird, mit Höhenruderkompensation,
damit der Segler beim Ausfahren der Krähenstellung nicht aufbäumt.

## 1. Den standardmäßigen Klappenmischer deaktivieren

![Klappenmischer deaktivieren](../assets/how-to-butterfly-flaps-disable.png)

Setzen Sie die **Aktivierungsbedingung** des vom Assistenten erstellten
Klappenmischers auf `---` — er wird nicht verwendet.

## 2. Den Butterfly-Mischer anlegen

![Butterfly-Mischer hinzugefügt](../assets/how-to-butterfly-mix-added.png)

Tippen Sie auf einen beliebigen Mischer, **Mischer hinzufügen** →
**Butterfly** aus der
[Mischerbibliothek](../model-setup/mixes.md#mix-libraries), platziert nach
dem (nun deaktivierten) Klappenmischer.

## 3. Den Eingang konfigurieren

![Gas als Eingang](../assets/how-to-butterfly-mix-source-thr.png)

Setzen Sie **Eingang** auf **Gas**. Da Gas bei Knüppel oben normalerweise
den Maximalwert liefert, Butterfly bei Knüppel oben aber 0 sein muss,
drücken Sie lange `ENT` auf Gas und wählen Sie **Invertieren**:

![Gas invertieren](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Invertiertes Gas](../assets/how-to-butterfly-mix-source-thr-neg.png)

Der Eingang liefert nun 0 bei ganz nach oben gestelltem Knüppel, und das
Feld zeigt `-Throttle` zur Bestätigung der Invertierung. Setzen Sie die
**Aktivierungsbedingung** auf eine Lande-Flugphase (oder einen anderen
Schalter), falls Butterfly nicht immer verfügbar sein soll.

## 4. Eine Kurve mit Totzone hinzufügen

![Kurvenauswahl](../assets/how-to-butterfly-mix-curve-select.png)

Eine kleine Totzone am Nullende des Knüppels verhindert ein
versehentliches Ausfahren durch geringfügige Knüppelbewegungen nahe dem
Endanschlag. Fügen Sie eine benutzerdefinierte 3-Punkt-Kurve hinzu (z. B.
mit dem Namen „Crowdb“) und schalten Sie den **Einfachen Modus** aus,
damit die X-Punkte verschoben werden können:

![3-Punkt-Kurve](../assets/how-to-butterfly-mix-curve-3pt.png)
![Kurvenpunkte](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    Das Hinzufügen einer benutzerdefinierten Kurve zum Butterfly-Mischer
    hebt dessen internen 0–100-Offset auf (der normalerweise automatisch
    angewendet wird) — die Kurve selbst muss diese 0–100-Transformation
    nun nachbilden. In diesem Beispiel bleibt der Ausgang bei 0 %, bis der
    Gasknüppel −90 % erreicht, und steigt dann linear auf 100 %:

    ![Kurve hinzugefügt](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Querruder und Wölbklappen konfigurieren

![Querruderausgang](../assets/how-to-butterfly-mix-ailerons.png)

Ein moderater Querruderausschlag nach oben (z. B. 20 %) in Kombination mit
einem großen Klappenausschlag ist die übliche Aufteilung. Wölbklappen
benötigen typischerweise weit mehr Weg nach unten als nach oben — dies
wird üblicherweise dadurch erreicht, dass die Servohebel der Klappen in
der Anlenkung selbst um 20–30° aus der Neutralstellung versetzt werden,
wodurch die Klappen bei Servo-Neutralstellung etwa halb nach unten stehen:

![Klappen oben](../assets/how-to-butterfly-mix-flaps-up.png)
![Klappen unten](../assets/how-to-butterfly-mix-flaps-down.png)

Setzen Sie die Gewichtung des Klappenmischers hoch (z. B. −180 %) für
maximalen Weg; der tatsächliche mechanische Weg wird über Min/Max in den
[Ausgängen](../model-setup/outputs.md) bestimmt.

!!! tip
    Um ein Überfahren der Servos zu vermeiden, beginnen Sie bei Min/Max
    der Ausgänge konservativ (z. B. ±30 %) und erweitern Sie die Werte
    beim finalen Einstellen vorsichtig, wobei Sie auf Klemmen achten.

## 6. Einen Offset-Mischer „Klappen Neutral“ hinzufügen

![Offset-Mischer mit 80 %](../assets/how-to-butterfly-offset-mix-80.png)

Da die versetzten Servohebel die Klappen bei Servo-Neutralstellung um etwa
20–30 % ausgelenkt lassen, bringt ein **Offset-Mischer** sie für den
normalen Flug wieder in die tatsächliche Flügel-Neutralstellung. Beginnen
Sie mit einem Offset von 80 % (der noch abgestimmt wird) und zwei
Ausgangskanälen, die beiden Klappenkanälen zugeordnet sind:

![Klappen oben mit Offset](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Klappen unten mit Offset](../assets/how-to-butterfly-offset-mix-flaps-down.png)

Prüfen Sie bei ganz nach oben gestelltem Gasknüppel (Butterfly-Mischer
inaktiv), dass die Werte des Klappenmischers auf dem Offset (80 %) liegen;
das Bewegen des Klappenknüppels bis zum vollen Ausschlag sollte den
Mischerausgang um die gesamte Gewichtung verändern (z. B. von 80 % auf
−100 %, also 180 % Hub). Die tatsächlichen Wegbegrenzungen werden in den
Ausgängen über Min/Max oder eine Kurve feinabgestimmt.

## 7. Kompensationskurve und Mischer für das Höhenruder hinzufügen {: #7-add-the-elevator-compensation-curve-and-mix }

![Kompensationskurve](../assets/how-to-butterfly-comp-curve.png)
![Punkte der Kompensationskurve](../assets/how-to-butterfly-comp-curve-points.png)

Da die erforderliche Kompensation nicht linear ist, verwenden Sie eine
Kurve anstelle einer festen Gewichtung. Definieren Sie eine
benutzerdefinierte 5-Punkt-Kurve (z. B. „EleComp“) — dieses Beispiel
beginnt mit 12 %/10 %/8 %/5 %/0 % über die Punkte hinweg; ohne bekannten
Ausgangswert für Ihre Zelle müssen diese empirisch ermittelt werden.

Wandeln Sie diese Kurve anschließend in einen Wert um, der als
**Gewichtung** eines Mischers nutzbar ist: Fügen Sie einen
[Freien Mischer](../model-setup/mixes.md#mix-libraries) („EleCompx“) mit
Gas als Quelle und der angehängten EleComp-Kurve hinzu, mit Ausgang auf
einen hohen, ungenutzten Kanal (z. B. CH20):

![Kompensationsmischer auf CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

Drücken Sie zurück im Butterfly-Mischer lange `ENT` auf der
**Gewichtung** des Höhenruderausgangs, wählen Sie **Quelle verwenden** und
anschließend CH20 (EleCompx) aus der Kategorie „Kanäle“:

![Höhenruder verwendet CH20 als Quelle](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Quelle auswählen](../assets/how-to-butterfly-mix-ele-use-source.png)

Der Butterfly-Mischer ist nun vollständig konfiguriert:

![Höhenruderkompensation konfiguriert](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Mit der Kanalansicht überprüfen

![Ansicht nach Kanal](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Wechseln Sie beim Höhenruder zur
[Ansicht nach Kanal](../model-setup/mixes.md#per-channel-view), um zu
beobachten, wie sich alle beteiligten Mischer (Knüppeleingabe +
Butterfly-Kompensation) gemeinsam aktualisieren, während der Gas-/Brems­knüppel
bewegt wird — deutlich einfacher zur Fehlersuche als die flache
Tabellenansicht.

!!! tip
    Daten zum erforderlichen Höhenruderweg im Verhältnis zum
    Klappenausschlag (vom Hersteller der Zelle oder aus
    Community-Quellen) sind vor dem Einstellen der Startwerte der
    Kompensationskurve sehr hilfreich. Fehlen diese, beginnen Sie mit
    wenigen Millimetern Höhenruderweg bei voll ausgefahrenen Klappen und
    verfeinern Sie von dort aus.
