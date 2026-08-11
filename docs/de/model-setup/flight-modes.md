---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Flugphasen

![Flugphasen](../assets/model-fm.png)

Flugphasen (Flight Modes) ermöglichen es, über einen Schalter zwischen
unterschiedlichen Verhaltensweisen desselben Modells umzuschalten — bei
Segelflugzeugen etwa Start/Strecke/Speed/Thermik, bei Motorflugzeugen
Normal/Start/Landung, bei Hubschraubern Normal (Hochlaufen, Start/Landung) /
Idle Up 1 (Kunstflug) / Idle Up 2 (3D). Sie nehmen dem Piloten den größten
Teil des manuellen Umschaltens und Nachtrimmens ab: Eine Flugphase kann
eigene, unabhängige Trimmungen besitzen und sowohl [Variablen](variables.md)
als auch [Mischer](mixes.md) freischalten — zusammen genügt das für
wirklich komplexe Konfigurationen. Siehe [Einfaches Beispiel für
Flächenmodelle](../tutorials/basic-fixed-wing.md) für Flugphasen an einem
realen Modell.

Standardmäßig sind keine Flugphasen definiert. Tippen Sie auf die
Standard-Flugphase und wählen Sie **Bearbeiten**, um sie umzubenennen, oder
**Hinzufügen**, um eine neue anzulegen — bis zu 20 insgesamt.

## Name

Ein aussagekräftiger Name — Strecke, Speed, Thermik, Start, Landung, was
immer passt.

## Aktivierungsbedingung

![Flugphasen-Formular](../assets/model-fm-form.png)

Eine neu angelegte Flugphase ist zunächst inaktiv (`---`). Nach dem
Festlegen kann sie durch eine Schalter- oder Tastenstellung, einen
Funktionsschalter, einen logischen Schalter, ein Systemereignis
(Gas-Abschaltung/Leerlaufsperre) oder eine Trimmposition ausgelöst werden.

Die **Standard**-Flugphase besitzt überhaupt keine Aktivierungsbedingung —
sie ist immer dann aktiv, wenn die Bedingung keiner anderen Flugphase
erfüllt ist. Es ist stets nur eine Flugphase gleichzeitig aktiv: die erste
(in der Prioritätsreihenfolge), deren Bedingung aktuell erfüllt ist. Die
aktive Flugphase wird fett dargestellt.

!!! warning "Eine Flugphase zu einem bestehenden Modell hinzufügen"
    Eine neu hinzugefügte Flugphase ist standardmäßig in jedem Mischer
    aktiv, der bereits flugphasenabhängig ist — prüfen Sie, ob sich jeder
    dieser Mischer weiterhin korrekt verhält, insbesondere ein
    **Lock**-Mischer, der einen Kanal auf eine bestimmte Flugphase festlegt.

## Ein-, Ausblenden

Übergangszeiten für das weiche Überblenden zwischen Flugphasen (z. B. 1
Sekunde in jede Richtung) — dies wirkt sich nur auf Mischer aus, die selbst
flugphasenabhängig sind.

## Verwaltung der Flugphasen

![Flugphase verschieben](../assets/model-fm-move.png)
![Zum Verschieben auswählen](../assets/model-fm-move-select.png)
![Phasen 0–3](../assets/model-fm-0to3.png)

Tippen Sie eine Flugphase an für **Bearbeiten**, **Hinzufügen**,
**Klonen** oder **Löschen**. Eine **geklonte** Flugphase übernimmt die
Einstellungen ihrer Ausgangsphase in jedem Mischer, der Flugphasen
verwendet — gleiches Verhalten, gleicher Aktiv-/Inaktiv-Zustand — daher
wird ein Klon standardmäßig als letzte Flugphase hinzugefügt, um bestehende
Phasen nicht zu beeinträchtigen. **Verschieben** ändert die Priorität einer
Flugphase: Die Priorität verläuft in aufsteigender Reihenfolge, und (wie
oben beschrieben) ist diejenige aktiv, deren Bedingung als erste erfüllt
ist.
