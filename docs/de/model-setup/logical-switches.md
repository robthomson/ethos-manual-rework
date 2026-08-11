---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Logische Schalter

![Menü der logischen Schalter](../assets/model-lsw-menu.png)

Logische Schalter sind benutzerprogrammierte *virtuelle* Schalter — keine
physischen Bedienelemente, aber überall dort einsetzbar, wo auch ein
physischer Schalter als Auslöser für eine Funktion verwendet werden kann.
Jeder logische Schalter wertet die konfigurierte Bedingung anhand seiner
Eingänge aus (andere Schalter, Telemetriewerte, Mischerwerte, Timer-Werte,
Gyro-/Trainerkanäle und weitere) und wird dadurch Wahr oder Falsch. Bis zu
100 werden unterstützt; standardmäßig existiert keiner. Mit **+** fügen Sie
einen hinzu; die Menübezeichnung eines definierten Schalters wird grün
dargestellt, wenn er Wahr ist, und rot, wenn er Falsch ist. Tippen Sie einen
vorhandenen Schalter an für **Bearbeiten**/**Verschieben**/**Kopieren-Einfügen**/**Duplizieren**/**Löschen**.

![Logischen Schalter hinzufügen](../assets/model-lsw-add.png)

## Funktion

Jede Funktion unterstützt einen normalen oder invertierten Ausgang.

- **A ~ X** — wahr, wenn die Quelle `A` *näherungsweise* (innerhalb von
  ca. 10 %) einem festen Wert `X` entspricht. Grundsätzlich der exakten
  Gleichheit vorzuziehen —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — denn bei `A = X` kann ein Telemetriewert, der etwa zwischen 8,5 V und
  8,35 V um einen Zielwert von 8,4 V schwankt, schlicht nie exakt 8,4 V
  erreichen, sodass der Schalter niemals auslösen würde.
- **A = X** — wahr nur dann, wenn `A` exakt `X` entspricht.
- **A > X** / **A < X** — wahr, wenn `A` größer/kleiner als `X` ist.
- **|A| > X** / **|A| < X** — wie oben, jedoch wird der Absolutwert von
  `A` verglichen (Vorzeichen wird ignoriert).
- **Δ > X** — wahr, wenn die Änderung von `A` (Delta) über das
  **Prüfintervall** mindestens `X` erreicht. Ein Intervall von `---`
  bedeutet ein unendliches Zeitfenster.

  ![Delta größer als X](../assets/model-lsw-delta-gtX.png)
  ![Absolutes Delta größer als X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — wie oben, jedoch mit dem Absolutwert der Änderung.
- **Range** — wahr, wenn `A` innerhalb eines angegebenen Bereichs liegt.

  ![Range](../assets/model-lsw-range.png)

- **AND** — wahr nur dann, wenn jede aufgeführte Quelle (Wert 1…N) wahr ist.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — wahr, wenn mindestens eine der aufgeführten Quellen wahr ist.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (exklusives ODER) — wahr, wenn *genau eine* der aufgeführten
  Quellen wahr ist.

  ![XOR](../assets/model-lsw-XOR.png)

- **Timer generator** — läuft frei und schaltet fortlaufend ein und aus:
  eingeschaltet für **Duration active**, ausgeschaltet für **Duration
  inactive**.

  ![Timer generator](../assets/model-lsw-timer-generator.png)

- **Sticky** — eine Verriegelung (SR-Flipflop); siehe [unten](#sticky).
- **Edge** — ein kurzzeitiger Impuls; siehe [unten](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Verriegelt auf **Wahr**, sobald die Bedingung **Trigger ON** erfüllt ist,
und bleibt Wahr, bis **Trigger OFF** erfüllt ist — optional freigegeben
durch die **Active condition** (solange diese Falsch ist, wird der Ausgang
unabhängig davon auf Falsch gehalten; die interne Verriegelung von Sticky
wird im Hintergrund weiterhin ausgewertet und wird, sobald die Active
condition wieder Wahr wird, erneut an den Ausgang durchgeschaltet —
vorbehaltlich der Verzögerungen).

Seit Ethos 1.6.2 akzeptieren beide Trigger einen **Edge**-Modifikator
(langer Druck auf `ENT` bei der Trigger-Bedingung, dann Edge auswählen —
angezeigt mit einem vorangestellten `†`) für eine deutlich feinere
Steuerung:

![Sticky mit Edge](../assets/model-lsw-sticky-with-edge.png)
![Auswahl der Edge-Option](../assets/model-lsw-sticky-edge-select.png)

- **Trigger ON `SA` (keine Verzögerung)** — verriegelt in dem Moment auf
  Wahr, in dem SA auf High geht.
- **Trigger ON `SA` (Verzögerung = 1 s)** — verriegelt 1 s nach dem
  High-Wechsel von SA auf Wahr, *sofern* SA am Ende dieser Sekunde noch
  immer High ist.
- **Trigger ON `†SA` (Verzögerung = 1 s)** — verriegelt 1 s nach dem
  High-Wechsel von SA von Wahr→Falsch, **unabhängig** davon, ob SA zu
  diesem Zeitpunkt noch High ist (die Flanke ist bereits aufgetreten; die
  Verzögerung bestimmt lediglich den zeitlichen Ablauf des Ergebnisses).

Trigger OFF verhält sich in umgekehrter Richtung genauso. Verzögerungen
wirken **nach** der Active condition — eine Änderung der Active condition
löst also die Verzögerungszeit erneut aus, bevor der verriegelte Wert
wieder den Ausgang erreicht. Wechseln beide Trigger gleichzeitig von
Falsch→Wahr, so wird der Ausgang von Sticky einmal **umgeschaltet**. Siehe
auch [Gemeinsame Parameter](#shared-parameters) weiter unten.

### Edge

![Edge](../assets/model-lsw-edge.png)

Ein kurzzeitiger Impuls: Wahr für die Dauer **Duration**, sobald die
Trigger-Bedingung erfüllt ist. **During** ist ein Wertepaar `[t1:t2]`, das
genau festlegt, wann dies geschieht:

- **Steigende Flanke, During = 0,0 s** — löst in dem Moment aus, in dem
  Trigger ON von Falsch→Wahr wechselt.

  ![Steigende Flanke](../assets/model-lsw-edge-rising-edge.png)
  ![During = 0](../assets/model-lsw-edge-during-eq0.png)

- **Steigende Flanke, During ≥ 0,0 s (z. B. 5,0 s)** — löst 5 s nach dem
  Wechsel von Trigger ON auf Wahr aus und ignoriert kürzere „Spitzen“
  innerhalb dieses 5-s-Fensters.

  ![During > 0, steigende Flanke](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![During > 0](../assets/model-lsw-edge-during-gt0.png)

- **Fallende Flanke, During = 0,0 s** — löst in dem Moment aus, in dem
  Trigger ON von Wahr→Falsch wechselt.
- **Fallende Flanke, During ≥ 0,0 s (z. B. 3,0 s)** — löst beim Übergang
  Wahr→Falsch aus, jedoch nur, wenn der Zustand zuvor mindestens 3 s lang
  Wahr war.
- **Impuls (sowohl t1 als auch t2 gesetzt)** — löst nur aus, wenn Trigger
  ON innerhalb dieses Fensters von Falsch→Wahr→Falsch wechselt (z. B.
  zwischen 2 s und 5 s später).

## Gemeinsame Parameter {: #shared-parameters }

![Gemeinsame Parameter](../assets/model-lsw-common-parameters.png)

- **Active condition** — gibt den Ausgang des Schalters auf dieselbe Weise
  frei wie oben bei Sticky beschrieben. Optionen: Immer ein,
  Schalter-/Funktionsschalter-/Logikschalter-/Trimmpositionen, Telemetrie,
  Flugphasen oder ein Systemereignis (Leerlaufsperre, Gas-Abschaltung, Gas
  aktiv, Telemetrie aktiv, RSSI niedrig, Trainer aktiv, Flug-Reset).
- **Delay before active** / **Delay before inactive** — wie lange die
  Bedingung Wahr (bzw. Falsch) bleiben muss, bevor der Ausgang folgt, bis
  zu 60 s. Für Timer generator und Edge nicht relevant. (Siehe [Anleitung:
  Warnung bei Akkukapazität](../how-to/battery-capacity-warning.md) für
  eine Verzögerung zum Entprellen eines Spannungseinbruchs.)
- **Confirmation before active** / **inactive** — fordert eine
  Benutzerbestätigung an, bevor der Zustand tatsächlich wechselt (mit einer
  Abbrechen-Option, für Fälle, in denen sie zu häufig ausgelöst wird, um
  nützlich zu sein) — praktisch zur Absicherung von riskanten Aktionen,
  z. B. zur Bestätigung, bevor ein Landfahrzeug per Fernsteuerung
  abgeschaltet wird.

  ![Bestätigung Wahr](../assets/model-lsw-confirm-lsw-true.png)
  ![Bestätigung Falsch](../assets/model-lsw-confirm-lsw-false.png)

- **Min Duration** — bleibt nach dem Wechsel auf Wahr mindestens für diese
  Zeit Wahr. Bleibt der Wert auf `---`, kann der Ausgang unter Umständen
  nur für einen einzigen Mischerzyklus Wahr sein — zu kurz, um die Zeile in
  der Benutzeroberfläche überhaupt fett werden zu sehen.
- **Max Duration** — wechselt nach dieser Zeit automatisch zurück auf
  Falsch, sofern noch gesetzt. Beide Zeiten gehen bis zu 60 s.
- **Comment** — freier Text, der überall dort angezeigt wird, wo dieser
  Schalter einem Wert-Widget hinzugefügt wird, um seinen Zweck zu
  dokumentieren.

## Verwendung mit Telemetrie

Ein Systemereignis **Telemetrie aktiv** (oder ein Schalter, dessen Quelle
ein Telemetriesensor ist und der nur aktiv ist, solange dieser Sensor Daten
liefert) deckt Bedingungen der Art „wird derzeit Telemetrie empfangen“ ab.

!!! warning
    Ein [Mischer](mixes.md), der über einen telemetriebasierten logischen
    Schalter freigegeben wird, benötigt eine **zweite** Mischeraktion mit
    demselben Schalter in **invertierter** Form, damit der Mischer auch bei
    Verlust der Telemetrie noch einen gültigen Wert liefert — denken Sie
    daran, dass ein inaktiver Mischer neutral ausgibt (0 % / 1500 µs bzw.
    **Halbgas** auf einem Gaskanal). Alternativ können Sie eine
    **Offset**-Aktion verwenden, die bereits über getrennte Werte für aktiv
    und inaktiv verfügt — z. B. deckt die Quelle **0** (der spezielle Wert)
    mit einem so eingestellten Offset, dass der Mischer +100 % liefert,
    während `LS3` aktiv ist, und −100 %, während er inaktiv ist, beide Fälle
    in einer einzigen Aktion ab.

## Vergleich von Quellen

Eine Quelle wird normalerweise mit einem festen Wert verglichen, es können
aber auch zwei Quellen *desselben* Typs direkt miteinander verglichen
werden — z. B. zwei Timer, zwei Spannungen oder zwei Drehzahlsensoren.

## Trainer-Eingaben vom Slave ignorieren

![Trainer-Eingabe ignorieren](../assets/model-lsw-ignore-trainer-input.png)

Die [Optionen](../getting-started/user-interface-and-navigation.md#choosing-a-source)
einer Quelle können Trainer-Eingaben von einem angeschlossenen
Schüler-Sender (Slave) ausschließen — dies wird typischerweise bei einem
logischen Schalter verwendet, der die Knüppelbewegung des **Lehrers**
überwacht (z. B. um sofort eingreifen zu können, wenn etwas schiefgeht),
ohne dass auch die Eingaben des Schülers ihn auslösen. Häufig kombiniert
mit einem Trainer-Schalter, der die Active condition des Lehrers freigibt.
