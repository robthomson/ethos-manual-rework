---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Flugphasen

![Flugphasen](../assets/model-fm.png)

Flugphasen (Flight Modes) ermöglichen es, über einen Schalter zwischen
unterschiedlichen Verhaltensweisen desselben Modells umzuschalten — bei
Segelflugzeugen z. B. Start/Strecke/Speed/Thermik, bei Motorflugzeugen
Normal/Start/Landung, bei Hubschraubern Normal (Hochlaufen, Start/Landung) /
Idle Up 1 (Kunstflug) / Idle Up 2 (3D). Sie nehmen dem Piloten den größten
Teil des manuellen Umschaltens und Nachtrimmens ab: Eine Flugphase kann
eigene, unabhängige Trimmungen besitzen und sowohl [Variablen](variables.md)
als auch [Mischer](mixes.md) freischalten — zusammen genügt das für
wirklich komplexe Konfigurationen. Ein Beispiel für Flugphasen an einem
realen Modell finden Sie unter [Einfaches Beispiel für
Flächenmodelle](../tutorials/basic-fixed-wing.md).

Standardmäßig sind keine Flugphasen definiert. Tippen Sie auf die
Standard-Flugphase und wählen Sie **bearbeiten**, um sie umzubenennen, oder
**add./hinzuf.**, um eine neue anzulegen — bis zu 20 insgesamt.

## Name

Ein aussagekräftiger Name — Strecke, Speed, Thermik, Start, Landung, was
immer passt.

## Aktive Bedingung

![Flugphasen-Formular](../assets/model-fm-form.png)

Eine neu angelegte Flugphase ist zunächst inaktiv (`---`). Nach dem
Festlegen kann sie durch die Auswahl von Schalter- oder Tastenpositionen,
Funktionsschaltern, Logikschaltern, einem Systemereignis wie Gasabschaltung
oder -haltung oder Trimmpositionen bedingt werden.

Die **Standard**-Flugphase besitzt überhaupt keine aktive Bedingung —
sie ist immer dann aktiv, wenn die Bedingung keiner anderen Flugphase
erfüllt ist. Es ist stets nur eine Flugphase gleichzeitig aktiv: die erste
(in der Prioritätsreihenfolge), deren Bedingung aktuell erfüllt ist. Die
aktive Flugphase wird fett dargestellt.

!!! warning "Eine Flugphase zu einem bestehenden Modell hinzufügen"
    Eine neu hinzugefügte Flugphase ist standardmäßig in jedem Mischer
    aktiv, der bereits flugphasenabhängig ist — prüfen Sie, ob sich jeder
    dieser Mischer weiterhin korrekt verhält, insbesondere ein Mischer mit
    der Operation **sperren**, der einen Kanal an eine bestimmte Flugphase
    bindet.

## Ein-, Ausblenden

Übergangszeiten für das weiche Überblenden zwischen den Flugphasen (z. B. 1
Sekunde in jede Richtung) — dies wirkt sich nur auf Mischer aus, die selbst
flugphasenabhängig sind.

## Verwaltung der Flugphasen

![Flugphase verschieben](../assets/model-fm-move.png)
![Zum Verschieben auswählen](../assets/model-fm-move-select.png)
![Phasen 0–3](../assets/model-fm-0to3.png)

Tippen Sie auf eine Flugphase, um **bearbeiten**, **add./hinzuf.**,
**klonen** oder **löschen** zu wählen. Eine **geklonte** Flugphase
übernimmt die Einstellungen ihrer Ausgangsphase in jedem Mischer, der
Flugphasen verwendet — gleiches Verhalten, gleicher Aktiv-/Inaktiv-Zustand
— daher wird ein Klon standardmäßig als letzte Flugphase hinzugefügt, um
bestehende Phasen nicht zu beeinträchtigen. Mit **verschieben** ändern Sie
die Priorität einer Flugphase: Die Priorität verläuft in aufsteigender
Reihenfolge, und (wie oben beschrieben) ist diejenige aktiv, deren
Bedingung als erste erfüllt ist.
