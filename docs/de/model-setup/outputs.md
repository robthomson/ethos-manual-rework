---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Ausgänge

![Ausgänge](../assets/model-outputs.png)

Die Ausgänge bilden die Schnittstelle zwischen der reinen „Logik" der
[Mischer](mixes.md) und der physischen Welt — Servos, Gestänge,
Ruderflächen, Aktuatoren, Messwandler. Hier werden Endpunkte, Umkehrung,
Zentrierung und Korrekturkurven an das angepasst, was das Modell
mechanisch tatsächlich benötigt. Jeder Ausgangskanal entspricht einem
Servoausgang des Empfängers (CH1 → Servoanschluss Nr. 1, bei
Standard-Protokolleinstellungen).

Ethos arbeitet mit Prozentwerten, Servos werden letztlich jedoch über die
PWM-Impulsbreite in Mikrosekunden angesteuert:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Ein Kanal **ohne aktiven Mischer** gibt die Neutralstellung aus
    (0% / 1500 µs) — das gilt auch für einen Kanal, dessen einzige
    Mischer derzeit inaktiv sind. Stellen Sie sicher, dass jeder
    tatsächlich genutzte Kanal stets von einem aktiven Mischer
    unterstützt wird. Speziell bei einem Gaskanal bedeutet Neutralstellung
    **Halbgas**.

Der Bildschirm „Ausgänge" zeigt zwei Balken pro Kanal: Der untere (grüne)
Balken ist der Wert des Mischers für diesen Kanal, der obere (orange)
Balken ist der nach der Ausgangsverarbeitung tatsächlich an den Empfänger
gesendete Wert (jeweils in % und µs). Min-/Max-Begrenzungen erscheinen als
ausgegraute Abschnitte des orangen Balkens. Kanäle, die derzeit nicht an
das HF-Modul übertragen werden, haben einen dunkleren Hintergrund. Kleine
Symbole erscheinen bei einem Kanal, wenn dessen Einstellungen für
Richtung, Kurve, Verzögerung oder Balance vom Standard abweichen — so
lassen sich nicht standardmäßige Kanäle auf einen Blick erkennen.

!!! tip
    Ein langer Druck auf `ENT` im Bildschirm „Mischer" oder „Flugphasen"
    führt direkt hierher.

## Einen Kanal bearbeiten {: #editing-a-channel }

![Höhenruder-Ausgang bearbeiten](../assets/model-outputs-elevator-edit.png)
![Gas-Ausgang bearbeiten](../assets/model-outputs-throttle-edit.png)

Tippen Sie auf einen Kanal, um ihn zu öffnen. Eine Vorschau am oberen Rand
zeigt den Mischerwert (grün) gegenüber dem Ausgangswert (orange), mit
einer kleinen weißen Markierung für die Min-/Max-Punkte.

- **Name** — editierbar.
- **Richtung** — kehrt den Ausgang des Kanals um, üblicherweise um die
  Drehrichtung des Servos umzukehren. Wird als Doppelpfeil-Symbol am Kanal
  angezeigt. Dies wirkt sich **nicht** auf die zuführenden Mischer aus und
  vertauscht **nicht** die Min-/Max-Begrenzungen.
- **Min/Max** — harte Grenzwerte, die niemals überschritten werden — so
  einzustellen, dass mechanisches Blockieren vermieden wird. Sie wirken
  als Endpunkt-/Verstärkungseinstellung: Ein Verringern reduziert den
  Ausschlag, statt ein Abschneiden zu verursachen. Standard ist ±100%,
  einstellbar bis ±150%. Während der Einstellung wird jeweils das Ende
  fett dargestellt, in dessen Richtung gerade bewegt wird (bewegen Sie
  z. B. den Höhenruderknüppel nach vorn, wird der Max-Wert fett — zur
  Bestätigung, dass Sie dieses Ende einstellen).

  ![SBUS-Redundanzwarnung](../assets/model-outputs-sbus-warning.png)

  !!! warning "SBUS-Redundanz"
      Ein Redundanz-Setup über SBUS kann ein Servo nicht über etwa ±125%
      hinaus bewegen. Die Min-/Max-Felder selbst haben asymmetrische
      Bereiche (−150–0% und 0–150%) — werden sie von einer
      [Variablen](variables.md) angesteuert, geben Sie dieser Variablen
      einen identischen Bereich oder setzen Sie **Bereich ignorieren**
      (siehe [Quellenoptionen](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      andernfalls erzeugt die automatische Bereichsumrechnung unerwartete
      Werte. Überschreitet der Ausgang des Hauptempfängers 125% und geht
      dieser in Failsafe, begrenzt der über SBUS übernehmende
      Redundanzempfänger den Wert wieder auf 125%.

- **Center/Subtrimm** — verschiebt den Ausgang, typischerweise um einen
  Servoarm zu zentrieren; die Endpunkte bleiben unverändert.

  !!! warning
      Verwenden Sie den Subtrimm nicht für große Verschiebungen — er
      erzeugt ein erhebliches Differential im Servoverhalten. Nutzen Sie
      für alles, was über eine feine Zentrierung hinausgeht, stattdessen
      einen **Offset-Mischer**.

- **PWM-Mitte** — wie der Subtrimm, verschiebt jedoch den *gesamten*
  Servoweg einschließlich der harten Grenzen. Dies geschieht faktisch im
  Servo selbst und wird nicht im Kanalmonitor angezeigt. So bleibt die
  mechanische Zentrierung von der Trimmung getrennt.
- **Kurve** — verknüpft eine Expo- oder benutzerdefinierte Kurve
  (vorhanden oder neu, mit einem **Bearbeiten**-Kürzel, sobald gesetzt),
  um das reale Verhalten zu korrigieren — z. B. damit linke und rechte
  Landeklappe exakt gleich laufen. Wird als Kurvensymbol am Kanal
  angezeigt.
- **Verzögerung auf/ab** — verlangsamt die Reaktion des Ausgangs auf
  Eingangsänderungen, angegeben in Sekunden für den Weg 0→100% — z. B. um
  ein von einem gewöhnlichen Proportionalservo angetriebenes Fahrwerk zu
  verlangsamen. Wird als Uhrensymbol am Kanal angezeigt. (Eine
  **Verzögerung** im Sinne eines Einschaltverzugs — im Unterschied zum
  langsamen Lauf — steht bei den [Logischen
  Schaltern](logical-switches.md) zur Verfügung.)

## Kanäle tauschen {: #swap-channels }

![Kanäle tauschen](../assets/model-outputs-swap-channels.png)
![Zu tauschenden Kanal wählen](../assets/model-outputs-swap-channels-select.png)

Tauscht zwei Ausgangskanäle. Der Dialog öffnet sich mit dem aktuellen
Kanal vorbelegt; wählen Sie den anderen und bestätigen Sie — der Tausch
erfolgt sofort, und jeder Mischer, der einen der beiden Kanäle
referenziert, wird entsprechend aktualisiert.

## Einstellungen zurücksetzen

![Kanal zurücksetzen](../assets/model-outputs-reset-select.png)

Setzt sämtliche Parameter eines Kanals auf die Standardwerte zurück —
nützlich, bevor ein Kanal für etwas anderes verwendet wird. Ein
Bestätigungsdialog verhindert versehentliches Zurücksetzen.

## Kanäle abgleichen {: #balance-channels }

![Abzugleichende Kanäle wählen](../assets/model-outputs-balance-choose_channels.png)
![CH7/CH6 wählen](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Gleicht ein Paar (oder bis zu 4) Kanäle so ab, dass sie synchron laufen —
z. B. können nicht synchron laufende Landeklappen ein unerwünschtes Rollen
verursachen; ungleich laufende Gaskanäle eines mehrmotorigen Modells
können ein unerwünschtes Gieren hervorrufen. Ethos erzeugt für jeden
ausgewählten Kanal eine Differential-Balancekurve; durch Vergleich der
tatsächlichen Ruderstellungen an jedem Kurvenpunkt lassen sich diese
aneinander angleichen, bis die Ruderflächen perfekt synchron laufen.

**Vor dem Abgleich**, in dieser Reihenfolge:

1. Servorichtungen für den korrekten Ausschlag festlegen.
2. Bei Mischern in Neutralstellung optional die **PWM-Mitte** verwenden,
   um die Servohebel rechtwinklig auszurichten.
3. Min/Max und Subtrimm einstellen.
4. Alle weiteren Kurven konfigurieren.
5. Verzögerung konfigurieren.
6. *Danach* über den gesamten Weg abgleichen und angleichen.

**Anwendung**: Wählen Sie die abzugleichenden Kanäle und die
Anzeigereihenfolge —

![CH7/CH6 ausgewählt](../assets/model-outputs-balance-ch7-and-ch6.png)

— Mischerausgang auf der X-Achse, Balance-Korrekturdifferential auf der
Y-Achse. Tippen Sie auf den Graphen eines Kanals (oder wählen Sie ihn aus
und drücken Sie `ENT`), um dessen Balancekurve zu bearbeiten; mit `PAGE`
wechseln Sie während der Bearbeitung zwischen den Kanälen:

![Balancekurven-Editor](../assets/model-outputs-balance-curve-edit.png)

Bedienelemente des Editors:

- **Quelle** — normalerweise die Quelle(n) des Mischers selbst oder ein
  beliebiger anderer geeigneter Analogeingang; **Automatischer
  Analogeingang** übernimmt den ersten bewegten
  Steuerknüppel/Schieberegler/Potentiometer als X — sowohl im Graphen als
  auch im Modell selbst.
- **Magnet** — lässt die Einstellung über den Drehgeber automatisch auf
  den nächstgelegenen Kurvenpunkt der X-Achse einrasten:

  ![Magnet aus](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Magnet ein](../assets/model-outputs-balance-ch6-magnet-on.png)

  Der Eingang muss dennoch bewegt werden, um X vor der Anpassung mit einem
  Kurvenpunkt in Deckung zu bringen.
- **Sperre** — wird durch Antippen des Symbols oder Drücken von `ENT` im
  Graph-Bearbeitungsmodus umgeschaltet; sperrt alle Eingänge, sodass Sie
  den Knüppel loslassen und die Ruderflächen beobachten können, während
  Sie die Kurve anpassen.
- **Konfiguration** — ändert die Anzahl der Punkte je Kanal (für alle oder
  einzeln) sowie, ob die jeweilige Kurve geglättet wird.
- **Hilfe** (`?`, ebenso die Taste `MDL`) — öffnet die integrierte Hilfe.

**Mehrkanalig**: Bis zu 4 Kanäle können gemeinsam abgeglichen werden —

![4-Kanal-Abgleich](../assets/model-outputs-balance-ch2-9-8-1.png)

Einmal eingerichtet, kann eine Balancekurve auf der Konfigurationsseite
des jeweiligen Kanals überprüft, bearbeitet oder gelöscht werden — ein
Balance-Symbol kennzeichnet sie im Kanalgraphen (gegebenenfalls neben
einem Richtungssymbol, falls auch diese Einstellung vom Standard
abweicht).
