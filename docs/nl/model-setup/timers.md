---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Timers

![Timers](../assets/model-timers.png)

Acht volledig programmeerbare timers, die elk op- of aflopen. Voeg er een toe
met de **+** naast de kolomkoppen, of via **Toevoegen** hieronder. Door een
timer aan te raken verschijnen opties voor resetten/bewerken/toevoegen/
verplaatsen/kopiëren-plakken.

![Timer bewerken](../assets/model-timer1-edit.png)

## Gemeenschappelijke velden (aflopend en oplopend)

- **Waarde** — de huidige stand van de timer.
- **Naam** — aanpasbaar.
- **Modus** — **Omhoog** of **Omlaag**.
- **Startwaarde** (alleen bij aflopen) — de waarde waarvan wordt afgeteld.
- **Alarmwaarde** (alleen bij oplopen) — de waarde waarbij de timer als
  verstreken wordt beschouwd; hij loopt hierna door, maar wordt rood
  weergegeven in timer-widgets.
- **Startvoorwaarde** — start de timer. Als de **Stopvoorwaarde** op de
  standaardinstelling blijft staan, bepaalt de startvoorwaarde alleen zowel
  het starten *als* het stoppen. Anders start de timer de eerste keer dat de
  startvoorwaarde waar wordt en blijft hij vanaf dat moment lopen.
- **Stopvoorwaarde** — indien niet op de standaardinstelling gelaten, bepaalt
  deze de timer zodra hij loopt: gestopt zolang de voorwaarde waar is, lopend
  zolang deze onwaar is. In het onderstaande voorbeeld start een timer wanneer
  `ThrottleActive` waar wordt en stopt hij zodra de telemetrie niet langer
  actief is:

  ![Stopvoorwaarde](../assets/model-timer1-edit-stop.png)

- **Proportionele tijdbron** — `---` telt in realtime. Elke andere bron
  (bijv. de gasstick of het gaskanaal) schaalt de snelheid van de timer: bij
  −100% staat de timer stil, bij +100% loopt hij op realtime-snelheid, en
  daartussen schaalt hij proportioneel.
- **Reset** — een schakelaar, functieschakelaar, logische schakelaar of
  trimpositie die de timer reset; hij blijft in reset zolang de voorwaarde
  waar is.
- **Permanent** — behoudt de waarde van de timer na uitschakelen of een
  modelwissel, en laadt deze opnieuw wanneer het model de volgende keer wordt
  gebruikt.
- **Stem** — welk [stempakket](../system-setup/general.md#audio-settings)
  deze timer omroept.

## Audio-acties

![Audio-actie toevoegen](../assets/model-timer1-add-action.png)
![Actietype](../assets/model-timer1-action-type-select.png)
![Aftel-actie](../assets/model-timer1-action-countdown.png)

Volledig flexibele instelling van waarschuwingen per timer. Elke actie heeft
een type — **Aftellen** (gesproken), **Piep-aftellen** (piepjes in plaats van
spraak), **Bestand afspelen** of **Waarde afspelen** — plus:

- **Start** — de waarde waarbij het aftellen van deze actie begint.
- **Stap** — het meldingsinterval, tot maximaal 10 minuten (600 s).
- **Haptisch** — laat de melding gepaard gaan met vibratie.

Een typische stapel van drie acties:

![Overzicht van acties](../assets/model-timer1-actions-summary.png)
![Acties van timer 2](../assets/model-timer2-actions-summary.png)

1. Gesproken aftelling vanaf 2:00 resterend, elke 30 s, met haptische
   terugkoppeling.
2. Piep-aftelling vanaf 0:10 resterend, elke 1 s, met haptische
   terugkoppeling.
3. Een eigen bestand (bijv. `timer-1-elapsed`) dat wordt afgespeeld bij het
   verstrijken, met haptische terugkoppeling.

Voeg extra acties toe met **Toevoegen**; de lijst wordt in volgorde van
prioriteit doorlopen, waarbij de **hoogste prioriteit als laatste** komt.

Zie ook de [Timer Log display-widget](../displays/index.md#widget-types) voor
een doorlopend logboek van eerdere timerlopen.

![Timer-widget](../assets/model-timers-widget.png)
