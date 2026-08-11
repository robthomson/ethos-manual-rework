---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Timer

![Timer](../assets/model-timers.png)

Acht vollständig programmierbare Timer, die jeweils aufwärts oder abwärts
zählen. Ein Timer wird mit dem **+** neben den Spaltenüberschriften oder über
**Hinzufügen** darunter angelegt. Ein Tippen auf einen Timer öffnet die
Optionen zum Zurücksetzen, Bearbeiten, Hinzufügen, Verschieben und
Kopieren/Einfügen.

![Timer bearbeiten](../assets/model-timer1-edit.png)

## Gemeinsame Felder (abwärts und aufwärts zählend)

- **Wert** — der aktuelle Stand des Timers.
- **Name** — editierbar.
- **Modus** — **Aufwärts** oder **Abwärts**.
- **Startwert** (nur abwärts zählend) — der Wert, von dem heruntergezählt wird.
- **Alarmwert** (nur aufwärts zählend) — der Wert, ab dem der Timer als
  abgelaufen gilt; er zählt darüber hinaus weiter, wird in Timer-Widgets
  jedoch rot dargestellt.
- **Startbedingung** — startet den Timer. Bleibt die **Stoppbedingung** auf
  dem Standardwert, steuert die Startbedingung allein Start *und* Stopp.
  Andernfalls startet der Timer, sobald die Startbedingung zum ersten Mal
  wahr wird, und läuft von da an weiter.
- **Stoppbedingung** — sofern nicht auf dem Standardwert belassen, steuert
  sie den laufenden Timer: gestoppt, solange sie wahr ist, laufend, solange
  sie falsch ist. Im folgenden Beispiel startet ein Timer, wenn
  `ThrottleActive` wahr wird, und stoppt, sobald die Telemetrie nicht mehr
  aktiv ist:

  ![Stoppbedingung](../assets/model-timer1-edit-stop.png)

- **Proportionale Zeitquelle** — `---` zählt in Echtzeit. Jede andere Quelle
  (z. B. der Gasknüppel oder der Gaskanal) skaliert die Geschwindigkeit des
  Timers: bei −100 % steht der Timer, bei +100 % läuft er in
  Echtzeitgeschwindigkeit, dazwischen wird proportional skaliert.
- **Reset** — ein Schalter, Funktionsschalter, logischer Schalter oder eine
  Trimmposition, die den Timer zurücksetzt; er bleibt zurückgesetzt, solange
  die Bedingung wahr ist.
- **Persistent** — erhält den Wert des Timers über das Ausschalten oder einen
  Modellwechsel hinaus und lädt ihn beim nächsten Einsatz des Modells wieder.
- **Stimme** — welches
  [Sprachpaket](../system-setup/general.md#audio-settings) diesen Timer
  ansagt.

## Audio-Aktionen

![Audio-Aktion hinzufügen](../assets/model-timer1-add-action.png)
![Aktionstyp](../assets/model-timer1-action-type-select.png)
![Countdown-Aktion](../assets/model-timer1-action-countdown.png)

Vollständig flexible, timerspezifische Konfiguration der Warnmeldungen. Jede
Aktion besitzt einen Typ — **Countdown** (gesprochen), **Piep-Countdown**
(Pieptöne statt Sprache), **Datei abspielen** oder **Wert ansagen** — sowie:

- **Start** — der Wert, ab dem der Countdown dieser Aktion beginnt.
- **Schritt** — Ansageintervall, bis zu 10 Minuten (600 s).
- **Haptik** — die Ansage mit Vibration begleiten.

Eine typische Kombination aus drei Aktionen:

![Übersicht der Aktionen](../assets/model-timer1-actions-summary.png)
![Aktionen von Timer 2](../assets/model-timer2-actions-summary.png)

1. Gesprochener Countdown ab 2:00 Restzeit, alle 30 s, mit Haptik.
2. Piep-Countdown ab 0:10 Restzeit, jede Sekunde, mit Haptik.
3. Eine eigene Datei (z. B. `timer-1-elapsed`), die beim Ablauf abgespielt
   wird, mit Haptik.

Weitere Aktionen werden über **Hinzufügen** ergänzt; die Liste wird in der
Reihenfolge der Priorität abgearbeitet, wobei die **höchste Priorität zuletzt**
steht.

Siehe auch das [Anzeige-Widget Timer-Log](../displays/index.md#widget-types)
für ein laufendes Protokoll vergangener Timerläufe.

![Timer-Widget](../assets/model-timers-widget.png)
