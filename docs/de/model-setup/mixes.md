---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mischer

![Mischer-Symbol](../assets/model-icon-mixes.png)

Mischer sind der Kern der Modellprogrammierung in Ethos – hier werden Eingänge
(Knüppel, Schalter, Sensoren, alles, was eine [Quelle](../getting-started/user-interface-and-navigation.md#choosing-a-source)
erreichen kann) auf Ausgangskanäle geleitet, geformt und kombiniert. Pro Modell
können bis zu 120 Mischer definiert werden.

![Mischertabelle](../assets/model-mixes.png)

Wurde ein Modell mit dem Assistenten der **Modellauswahl** erstellt, sind die
grundlegenden Mischer (Querruder, Höhenruder, Gas, Seitenruder und was die
Zelle sonst noch benötigt) hier bereits angelegt. Wenn Sie einen Mischer
auswählen und `ENT` drücken, öffnet sich ein Kontextmenü, um ihn zu bearbeiten,
einen neuen Mischer hinzuzufügen, in die [kanalweise Ansicht](#per-channel-view)
zu wechseln, ihn zu verschieben, zu klonen oder zu löschen. Inaktive Mischer
werden ausgegraut dargestellt, und vor dem Löschen wird stets eine Bestätigung
verlangt.

## Aufbau eines Mischers {: #anatomy-of-a-mix }

Jeder Mischer verfügt über denselben Satz an Feldern, unabhängig davon, aus
welcher Kategorie er stammt. Der **Querruder**-Mischer dient hier als
repräsentatives Beispiel – Höhenruder- und Seitenruder-Mischer sind identisch
aufgebaut.

![Querruder-Mischer](../assets/model-mixes-ail-edit.png)

![Querruder-Mischer-Editor](../assets/model-mixes-ail.png)

**Name** – standardmäßig der Mischertyp; es kann ein beschreibender Name
eingegeben werden.

**aktiviert** – die standardmäßig aktive Bedingung ist *Immer an*. Sie kann
durch die Auswahl von Schalter- oder Tastenpositionen, Funktionsschaltern,
Logikschaltern, Flugmodi, einem Systemereignis wie Gasabschaltung oder -haltung
oder Trimmpositionen bedingt werden; der Mischer wirkt dann nur, solange die
Bedingung erfüllt ist.

**Flugphasen** – wenn Flugmodi definiert wurden, kann der Mischer zusätzlich von
einem oder mehreren Flugmodi abhängig gemacht werden.

**Kurve** – standardmäßig steht eine **Expo**-Kurve zur Verfügung (0 = linear;
ein positiver Wert macht die Reaktion um 0 herum weicher, ein negativer Wert
macht sie schärfer):

![Expo-Kurve](../assets/model-mixes-ail-expo.png)

Anstelle der Expo-Kurve kann auch jede zuvor unter [Kurven](curves.md)
definierte Kurve ausgewählt werden. Sie können bis zu 6 Kurven mit jeweils einer
Bedingung festlegen – wenn mehrere Bedingungen zutreffen, hat die Kurve mit der
höheren Position in der Liste Vorrang. Kurven werden **vor** den Gewichtungen
angewendet.

**Gewichtung / Anteile** – eine oder mehrere Gewichtungszeilen, die jeweils
optional durch einen Schalter, einen Funktionsschalter, einen Logikschalter,
eine Trimmposition oder einen Flugmodus bedingt sind. Die erste Zeile ist der
Standardwert und immer dann aktiv, wenn die Bedingung keiner anderen Zeile
zutrifft:

![Querruder-Gewichtungen](../assets/model-mixes-ail-weight.png)

Statt eines festen Prozentwerts kann eine Gewichtung auch von einer
[Quelle](../getting-started/user-interface-and-navigation.md#choosing-a-source)
gesteuert werden – beispielsweise von einem Poti, um die Gewichtung im Flug
anzupassen:

![Von einer Quelle gesteuerte Gewichtung](../assets/model-mixes-ail-diff.png)

**Differenzierung** (-100 bis 100, Standardwert 0) – ergibt in der einen
Richtung mehr Hub als in der anderen. Bei Querrudern ist dies der klassische
Kniff, mehr Aufwärtshub als Abwärtshub zu geben, um das negative Wendemoment zu
verringern. Wird erst angezeigt, wenn der Mischer mehr als einen Ausgangskanal
besitzt; sinnvoll ist die Differenzierung nur bei einer Ausgangskonfiguration im
Stil eines V-Leitwerks oder zweier getrennter Querruder.

**Anzahl der Kanäle / Ausgänge** – die Kanalanzahl legt fest, wie viele
Ausgangskanäle dieser Mischer ansteuert und welchen physischen Ausgängen sie
zugewiesen werden:

![Kanalanzahl](../assets/model-mixes-ail-ch-count.png)

Ein langer Druck auf `ENT` bei einem Ausgangskanal an anderer Stelle in der
Oberfläche (z. B. unter [Ausgänge](outputs.md)) springt direkt auf diese Seite
zurück.

## Der Gas-Mischer

Der Gas-Mischer entspricht einem Querruder-/Höhenruder-/Seitenruder-Mischer
zuzüglich motorspezifischer Sicherheitsoptionen.

![Gas-Mischer](../assets/model-mixes-thr.png)

**Eingang** – die Gasquelle, normalerweise der Gasknüppel, austauschbar gegen
ein Poti, einen Schieberegler, einen Schalter, einen Trimmtaster, einen Kanal,
eine Kreiselachse, einen Trainerkanal, einen Zeitgeber oder jede andere Quelle.

**Leerlauftrimmung** – erlaubt bei Verbrennungsmotoren, die Leerlaufdrehzahl
über eine eigene Trimmung einzustellen, ohne die Vollgasstellung zu verändern.
Bei aktivierter Leerlauftrimmung liegt der Gaskanal bei -75 %, wenn der Knüppel
im unteren Leerlauf steht; die Gastrimmung stellt den Leerlauf dann zwischen
-100 % und -50 % ein:

![Menü Leerlauftrimmung](../assets/model-mixes-thr-trim-menu.png)

![Leerlauftrimmung in unterer Position](../assets/model-mixes-thr-trim-low-position.png)

**Gasabschaltung** – eine harte Sicherheitsverriegelung: Der Kanal wird erst
aktiv, nachdem der Gasknüppel den Leerlauf durchlaufen hat, sodass ein
versehentliches Umlegen eines Schalters den Motor nicht aus einer
Vollgasstellung heraus anlaufen lassen kann:

![Gasabschaltung](../assets/model-mixes-thr-cut.png)

**Gashaltung** – hält den Kanal unabhängig von der Knüppelstellung auf einem
festen Wert, allerdings ohne die Sicherheitsverriegelung der Gasabschaltung:

![Gashaltung](../assets/model-mixes-thr-hold.png)

Auch der Gas-Mischer verfügt über eine eigene Kanalanzahl, genau wie jeder
andere Mischer:

![Kanalanzahl Gas](../assets/model-mixes-thr-ch-count.png)

!!! note "Gas-Verriegelung"
    Ethos verlangt, dass der Eingang des Gas-Mischers unabhängig von den
    Einstellungen für Gasabschaltung bzw. -haltung einmal -100 % durchläuft,
    bevor scharfgeschaltet wird – ein über den Modellauswahl-Assistenten
    erstelltes Modell berücksichtigt dies bereits, von Hand erstellte
    Gas-Mischer sollten es ebenfalls tun.

## Mischerbibliotheken {: #mix-libraries }

Die Bibliothek vordefinierter Mischer im Dialog **Mischer hinzufügen** richtet
sich nach der Modellkategorie, die bei der Modellerstellung gewählt wurde –
Flächenmodell, Segler, Hubschrauber und Multicopter bieten jeweils einen
eigenen Satz:

![Mischerbibliothek Flächenmodell](../assets/model-mixes-library-airplane.png)

![Mischerbibliothek Segler](../assets/model-mixes-library-glider.png)

![Mischerbibliothek Hubschrauber](../assets/model-mixes-library-heli.png)

![Mischerbibliothek Multicopter](../assets/model-mixes-library-multirotor.png)

Jede Bibliothek enthält außerdem den **Freien Mischer** – einen
Allzweck-Mischertyp ohne vorgegebenen Ein-/Ausgang, flexibler als die
spezialisierten Einträge, aber mit mehr Einrichtungsaufwand verbunden, um
dasselbe Ergebnis zu erzielen.

## Kanalweise Ansicht {: #per-channel-view }

Sind viele Mischer auf denselben Ausgang gelegt, lässt sich ihre Gesamtwirkung
in der einfachen Tabelle oben nur schwer erkennen. Wählen Sie einen Mischer aus
und rufen Sie **Nach Kanal anzeigen** auf, so werden stattdessen alle Mischer,
die einen Ausgang beeinflussen, gemeinsam gruppiert:

![Zur Kanalansicht wechseln](../assets/model-mixes-chview-select.png)

![Eingeklappter Kanal](../assets/model-mixes-chview-collapsed.png)

![Höhenruderkanal aufgeklappt](../assets/model-mixes-chview-elevator.png)

Das Aufklappen der Übersichtszeile eines Kanals zeigt jeden daran beteiligten
Mischer mit seiner aktuellen numerischen und grafischen Ausgabe – nützlich, um
genau zu prüfen, wie viel ein zusätzlicher Mischer (z. B. eine
Klappen-Höhenruder-Kompensation) über den primären Knüppeleingang hinaus
beisteuert:

![Detail der Höhenruder-Kanalansicht](../assets/model-mixes-chview-elevator-channel.png)

![Höhenruderkanal, Mischer hervorgehoben](../assets/model-mixes-chview-elevator-channel-view.png)

Wählen Sie einen Untermischer anstelle der Übersichtszeile aus, so öffnet sich
dasselbe Kontextmenü wie in der Tabelle (Bearbeiten, zurück zur Tabellenansicht
wechseln, Löschen):

![Tabellenansicht aus der Kanalansicht wählen](../assets/model-mixes-chview-table-view-select.png)

![Zurück zur Tabellenansicht](../assets/model-mixes-chview-back-at-mixes-view.png)
