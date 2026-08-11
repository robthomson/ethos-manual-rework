---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Grundlegendes Beispiel für ein Flächenflugzeug

Eine vollständige Schritt-für-Schritt-Anleitung für ein Flugzeug mit Motor + 2 Querrudern + 2 Klappen + Höhenruder + Seitenruder, mit einem Servo für jede Fläche, komplett mit dem Assistenten aufgebaut.
Führen Sie zuvor die [Ersteinrichtung des Senders](initial-radio-setup.md) durch.

## Schritt 1. Bestätigen Sie die Systemeinstellungen

Für dieses Beispiel verwenden wir die standardmäßige Kanalreihenfolge **AETR**.

## Schritt 2. Identifizieren Sie die benötigten Servos/Kanäle

Die [Mischer-Funktion](../model-setup/mixes.md) bildet das Herzstück des Senders — bis zu 100
Mischer-Kanäle, wobei normalerweise die Kanäle mit der niedrigsten Nummer den Servos zugewiesen werden (da
die Kanalnummern direkt den Kanälen im Empfänger zugeordnet sind; das interne HF-Modul des X20
hat bis zu 24 Ausgangskanäle zur Verfügung). Die oberen Kanäle stehen als
virtuelle Kanäle oder als zusätzliche echte Kanäle unter Verwendung mehrerer HF-Module und
SBus zur Verfügung. Unser Beispielflugzeug:

| Funktion | Kanäle |
|---|---|
| Motor | 1 |
| Querruder | 2 |
| Klappen | 2 |
| Höhenruder | 1 |
| Seitenruder | 1 |

(Einziehfahrwerke werden später eingebaut, in [Schritt 10](#step-10-add-a-mix-for-retracts).)

## Schritt 3. Erstellen Sie ein neues Modell

![Flugzeugmodell erstellen](../assets/tut-fw-eg-wiz-create-airplane.png)

Wählen Sie in der [Modellauswahl](../model-setup/model-select.md) die Modellkategorie,
tippen Sie auf **+** und starten Sie den Assistenten **Airplane**. Für dieses Beispiel wählen wir die Option **Non stabilized
receiver** (nicht stabilisierter Empfänger).

![Motorkanäle](../assets/tut-fw-eg-wiz-engine.png)
![Querruder-/Klappenkanäle](../assets/tut-fw-eg-wiz-ail-flaps.png)

Übernehmen Sie die Voreinstellung von 1 Kanal für den Motor, akzeptieren Sie dann die Standardeinstellung von 2 Kanälen für Querruder und wählen Sie 2 Kanäle für Klappen.

![Leitwerk-Typ](../assets/tut-fw-eg-wiz-tail.png)
![Höhen-/Seitenruderkanäle](../assets/tut-fw-eg-wiz-ele-rudd.png)

Akzeptieren Sie die Voreinstellung **Traditional Tail** (traditionelles Heck) mit 1 Kanal für Höhenruder und 1 Kanal für Seitenruder.

![Modellname](../assets/tut-fw-eg-wiz-name.png)
![Empfänger](../assets/tut-fw-eg-wiz-rx.png)

Vergeben Sie einen Namen (z. B. "FWexample" — Modellnamen können bis zu 15 Zeichen lang sein) und folgen Sie dem Assistenten bis zum Ende. Das Modell wird in der Kategorie Airplane erstellt und zum aktiven Modell gemacht.

## Schritt 4. Überprüfung und Konfiguration der Mischer

![Mischerübersicht](../assets/tut-fw-eg-mixes.png)

Der Assistent hat bereits die Mischer für Querruder (Kanäle 1 und 5), Höhenruder,
Gas, Seitenruder und Klappen erstellt (bei den Klappen bedeutet das `---`, dass ihnen noch keine
Steuerquelle zugewiesen wurde).

### Querruder {: #ailerons }

![Querrudermischer](../assets/tut-fw-eg-mixes-ail-mix.png)
![Querrudermischer bearbeiten](../assets/tut-fw-eg-mixes-ail-edit.png)

**Gewichtung/Anteile** — es ist eine gute Idee, verschiedene Gewichtungen einzustellen, bevor Sie ein neues Modell fliegen: relativ geringe Ausschläge
(z. B. 30 %) eignen sich für sportliches Fliegen, volle 100 % für das 3D-Fliegen. Fügen Sie eine Rate von 60 % für
den Schalter SB in der mittleren Position und 30 % für SB in der unteren Position hinzu — die Voreinstellung (SB oben) bleibt
bei 100 %:

![Gewichtungen](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — bei linearem Ausgangsverhalten kann die Reaktion in der Knüppelmitte zu unruhig sein; fügen Sie Expo-Raten
hinzu (z. B. 60 %/40 %/20 % an denselben SB-Schalterpositionen), um die Reaktion in der Knüppelmitte abzuflachen,
ohne den maximalen Ausschlag zu verringern:

![Expo-Raten](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Differenzierung** — bewegen sich linkes und rechtes Querruder um den gleichen Betrag nach oben oder unten, verursacht das sich nach unten
bewegende Querruder mehr Widerstand als das sich nach oben bewegende, wodurch der Flügel in die entgegengesetzte
Richtung der Kurve giert ("negatives Gieren"). Ein positiver Wert in der Differenzialeinstellung (50 % ist üblich) führt zu einer
geringeren Abwärtsbewegung des Querruders gegenüber der Aufwärtsbewegung und wirkt dem entgegen:

![50 % Differenzierung](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Um die Differenzierung im Flug zu optimieren, drücken Sie lange `ENT` auf dem Wert, wählen **Use a
source** (Signalquelle verwenden) und dann Pot1:

![Use a source](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Pot1 ausgewählt](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Nachdem Sie den Wert im Flug optimiert haben, drücken Sie erneut lange und wählen **Convert to
value** (in Wert umwandeln), um ihn dauerhaft zu Ihrer Einstellung zu machen:

![Convert to value](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim** — bietet die Möglichkeit, den zugehörigen Trimmer eines Mischers zu trennen, ohne ihn
zu deaktivieren, damit er anderweitig verwendet werden kann:

![Querrudertrimmung](../assets/tut-fw-eg-mixes-ail-trim.png)

### Höhen- und Seitenruder

Ähnlich wie bei den Querrudern dreifache Raten und Expo, hier am Schalter SC:

![Höhenruder-Expo-Raten](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Gas

![Gasmischer](../assets/tut-fw-eg-mixes-thr-edit.png)

Für das Gas belassen wir den Eingang auf dem Gasknüppel — wir brauchen keine Raten oder Expo —, aber wir brauchen einen
Sicherheitsschalter; das ist extrem wichtig, denn ein unerwartet anspringender Modellmotor
kann zu schweren Verletzungen führen.

**Leerlauf-Trimmung** (Glüh- und Benzinmotoren) — stellt die Leerlaufdrehzahl
ein, ohne die Vollgasposition zu beeinflussen:

![Leerlauf-Trimmung](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Ist sie aktiviert, geht der Gaskanal auf −75 %, wenn der Gasknüppel in der unteren Position steht;
mit dem Gasknüppel-Trimmhebel kann die Leerlaufdrehzahl dann zwischen −100 % und −50 % eingestellt werden.

**Motor AUS** — ein Sicherheitsverriegelungsmechanismus. Ist der Schalter SA unten die aktive
Bedingung (fett dargestellt, wenn er aktiv ist), wird der Gasausgang auf −100 % gehalten, sobald
der Knüppel unter −85 % fällt:

![Motor AUS](../assets/tut-fw-eg-mixes-thr-cut.png)

Ist stattdessen **Sticky** (SR FlipFlop) aktiviert, wird das Gas in dem Moment abgeschaltet, in dem der Schalter SA nach unten
geht, unabhängig von der Knüppelstellung:

![Motor AUS mit Sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

In beiden Fällen muss der Gasknüppel, sobald der aktive Zustand aufgehoben ist, wieder unter
−85 % gebracht werden, bevor das Gas erhöht werden kann — dadurch wird verhindert, dass der Motor
unerwartet in einer hohen Gasposition anläuft, wenn der Abschaltschalter zurückgeschaltet wird.

**Gasstellung halten** — eine Notabschaltung aus *jeder* Knüppelstellung heraus, die den Ausgang
sofort auf −100 % (oder den eingegebenen Wert) reduziert, sobald die Bedingung erfüllt ist:

![Gasstellung halten](../assets/tut-fw-eg-mixes-thr-hold.png)

### Klappen

![Klappeneingang](../assets/tut-fw-eg-mixes-flaps-input.png)

Weisen Sie die Klappen dem Schalter SE zu und erhöhen Sie die Gewichtung beider Ausgangskanäle auf 100 %:

![Klappengewichtungen](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Schritt 5. Binden des Empfängers

Verwenden Sie die Funktion [HF-System](../model-setup/rf-system.md), um Ihren Empfänger zu registrieren (wenn Ihr Empfänger ACCESS ist) und zu binden.
Bevor Sie mit den Ausgängen fortfahren, wäre es ratsam, die Servoanlenkungen zu trennen oder
den Servoweg vorübergehend zu reduzieren, um Schäden durch versehentliches Übersteuern zu vermeiden, während Sie die Min/Max-Grenzen konfigurieren.

## Schritt 6. Konfigurieren der Ausgänge

![Ausgänge](../assets/tut-fw-eg-outputs.png)

Der Abschnitt [Ausgänge](../model-setup/outputs.md) passt die Logik des Mischers an die tatsächlichen
mechanischen Eigenschaften des Modells an.

**Querruder 1** — beginnen Sie mit der Einstellung des Servo-Mittelpunkts über **PWM Mitte**, nachdem Sie die
mechanische Anlenkung optimiert haben, und konfigurieren Sie dann **Min**/**Max**. Zur Vereinfachung können Sie vorübergehend
ein Potentiometer für Min (und danach Max, wie im obigen Beispiel für die Querruderdifferenzierung gezeigt) zuweisen:

![Querruderausgang bearbeiten](../assets/tut-fw-eg-outputs-edit-ail.png)

**Klappen** — Klappen benötigen normalerweise einen großen Ausschlag nach unten, um wirksam zu bremsen;
dafür können Sie bei der Herstellung der Anlenkungen einen Teil des Ausschlags nach oben opfern, sodass die Klappe in der Servomitte
halb ausgefahren steht, und anschließend mit Min/Max die gewünschte Klappenstellung nach oben
und die volle Klappenstellung einstellen. Eine 5-Punkt-Kurve ist ein übliches Mittel, um einen daraus resultierenden
Versatz zwischen Klappen und Querrudern zu korrigieren. Verwenden Sie abschließend **[Kanäle
ausgleichen](../model-setup/outputs.md#balance-channels)**, um die Bewegung von linken und rechten Querrudern und Klappen zu synchronisieren.

## Schritt 7. Einführung in die Flugphasen

[Flugphasen](../model-setup/flight-modes.md) sind eine hervorragende Möglichkeit, ein Modell für verschiedene
Aufgaben zu konfigurieren — ein bisschen wie das Schalten beim Auto. Von den 20 verfügbaren nutzt dieses
Beispiel drei: **Default**, **Flaps Half** (Schalter SE Mitte) und
**Flaps Full** (SE oben). Die erste Flugphase, bei der die aktive Bedingung eingeschaltet ist, ist der aktive Modus; der
Standardmodus **Default** hat überhaupt keine Bedingung und ist immer dann aktiv, wenn keine andere zutrifft —
dies erklärt, warum er nicht über eine Schalterauswahloption verfügt. Ein- und Ausblendzeiten von 1 Sekunde verlangsamen den Übergang beim Ausfahren der Klappen.

## Schritt 8. Konfigurieren Sie die Trimmungen

Es gibt zwei Möglichkeiten, eine mit der Klappenstellung wechselnde Höhenrudertrimmung zu handhaben:

**Unabhängige Trimmungen pro Flugmodus** — die einfachste Variante: Die Höhenrudertrimmung wird
pro Flugphase völlig unabhängig und schaltet automatisch um, wenn Sie SE betätigen. Da Sie in jedem
Flugmodus sozusagen "von Grund auf" trimmen müssen, hilft die Funktion [Sofortige Trimmung](../model-setup/trims.md#instant-trim) — trimmen Sie
zuerst für den Normalflug, landen Sie dann und nutzen Sie diesen Wert als Starttrimmwert für die Klappenmodi.

**Basis Trimmung mit Offset** — einmal in Default trimmen, wobei die Höhenruderkompensation jeder
Klappenstellung als Offset darübergelegt wird:

1. Stellen Sie die Trimm-**Schrittweite** auf Mittel (damit es einfacher ist, die gewünschte Trimmung schnell zu
   erreichen; für die Feinabstimmung später verringern), den **Mode** auf Benutzerdefiniert und fügen Sie ein neues Verhalten hinzu.
2. **Aktive Bedingung**: `FM1(Flaps Half)`, Modus **Offset + Default** —
   der Trimmwert für Flaps Half ist dann die Summe aus der Basistrimmung plus der Offset-Trimmung, die sich
   aus den Trimmeinstellungen in diesem Flugmodus ergibt:

   ![Verhalten hinzufügen](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Wiederholen Sie dies für `FM2(Flaps Full)`:

   ![Flugphase auswählen](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Jede Klappenstellung kann nun unabhängig getrimmt werden, doch wird die im Flugmodus Default verwendete
Basistrimmung später verstellt (z. B. um thermische Drift des Servos auszugleichen), werden auch beide
Klappenmodus-Trimmungen automatisch um den gleichen Betrag verändert.

![Auswahl der benutzerdefinierten Trimmung](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Schritt 9. Einrichten einer Motorlaufzeit-Zeitschaltuhr

Bearbeiten Sie unter [Stoppuhren](../model-setup/timers.md) den Timer 1: Modus **Down** (abwärts zählend), Startwert fünf
Minuten, laufend, wenn das Systemereignis **Throttle active** (Drossel aktiv) wahr ist (vorausgesetzt, er wird nicht in der Reset-Stellung gehalten).
Optional können Sie eine proportionale Zeitquelle zuweisen (z. B. den Gasknüppel), sodass der Timer bei
Vollgas in Echtzeit zählt und langsamer wird, wenn das Gas reduziert wird.

## Schritt 10. Hinzufügen eines Mischers für Einziehfahrwerke {: #step-10-add-a-mix-for-retracts }

![Quelle des Fahrwerksmischers](../assets/tut-fw-eg-retracts-source.png)

Tippen Sie auf einen Mischer und wählen Sie **Add Mix** → **Free Mix** (Freier Mischer), benennen Sie ihn "Retracts", setzen Sie die
Bedingung auf Always (immer eingeschaltet) und die Quelle auf den Schalter SF. Die Standard-Mischaktion von Weight = 100 % ist
in Ordnung — damit wird dem Einziehfahrwerk z. B. Kanal 8 zugewiesen:

![Fahrwerksausgang](../assets/tut-fw-eg-retracts-outputs.png)
