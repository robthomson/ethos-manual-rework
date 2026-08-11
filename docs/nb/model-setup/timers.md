---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Timer

![Timer](../assets/model-timers.png)

Åtte fullt programmerbare timere, hver med opp- eller nedtelling. Legg til
en med **+** ved siden av kolonneoverskriftene, eller via **Legg til**
nedenfor. Ved å berøre en timer åpnes valg for nullstilling, redigering,
tillegg, flytting og kopier/lim inn.

![Redigering av timer](../assets/model-timer1-edit.png)

## Felles felter (nedtelling og opptelling)

- **Verdi** — timerens gjeldende visning.
- **Navn** — kan redigeres.
- **Modus** — **Opp** eller **Ned**.
- **Startverdi** (kun nedtelling) — verdien det telles ned fra.
- **Alarmverdi** (kun opptelling) — verdien der timeren regnes som utløpt;
  den fortsetter å telle forbi denne, men vises rødt i
  timer-widgeter.
- **Startbetingelse** — starter timeren. Hvis **Stoppbetingelse** står på
  standardverdien, styrer startbetingelsen alene både start *og* stopp.
  Ellers starter timeren første gang startbetingelsen blir sann, og
  fortsetter å gå derfra.
- **Stoppbetingelse** — hvis den ikke står på standardverdien, styrer den
  timeren når den går: stoppet så lenge den er sann, i gang så lenge den er
  falsk. I eksempelet nedenfor starter en timer når `ThrottleActive` blir
  sann, og stopper når telemetri ikke lenger er aktiv:

  ![Stoppbetingelse](../assets/model-timer1-edit-stop.png)

- **Proporsjonal tidskilde** — `---` teller i sanntid. Enhver annen kilde
  (f.eks. gasspaken eller gasskanalen) skalerer timerens hastighet: ved
  −100 % står timeren stille, ved +100 % går den i sanntidshastighet, og
  den skalerer proporsjonalt mellom disse.
- **Nullstill** — en bryter, funksjonsbryter, logisk bryter eller
  trimposisjon som nullstiller timeren; den holdes nullstilt så lenge
  betingelsen er sann.
- **Vedvarende** — beholder timerens verdi etter avslåing eller
  modellbytte, og laster den inn igjen neste gang modellen brukes.
- **Stemme** — hvilken [stemmepakke](../system-setup/general.md#audio-settings)
  som annonserer denne timeren.

## Lydhandlinger

![Legg til lydhandling](../assets/model-timer1-add-action.png)
![Handlingstype](../assets/model-timer1-action-type-select.png)
![Nedtellingshandling](../assets/model-timer1-action-countdown.png)

Helt fleksibel varselkonfigurasjon per timer. Hver handling har en type —
**Nedtelling** (opplest), **Pipende nedtelling** (piping i stedet for tale),
**Spill fil** eller **Spill verdi** — i tillegg til:

- **Start** — verdien nedtellingen for denne handlingen begynner på.
- **Trinn** — intervall mellom annonseringene, opptil 10 minutter (600 s).
- **Haptisk** — følg annonseringen med vibrasjon.

En typisk oppstilling med tre handlinger:

![Oversikt over handlinger](../assets/model-timer1-actions-summary.png)
![Handlinger for timer 2](../assets/model-timer2-actions-summary.png)

1. Opplest nedtelling som starter ved 2:00 gjenstående, hvert 30. sekund, med haptikk.
2. Pipende nedtelling som starter ved 0:10 gjenstående, hvert sekund, med haptikk.
3. En egen fil (f.eks. `timer-1-elapsed`) som spilles ved utløp, med haptikk.

Legg til flere handlinger med **Legg til**; listen kjøres i
prioritetsrekkefølge, med **høyeste prioritet sist**.

Se også [skjermwidgeten Timer Log](../displays/index.md#widget-types) for en
løpende logg over tidligere timerkjøringer.

![Timer-widget](../assets/model-timers-widget.png)
