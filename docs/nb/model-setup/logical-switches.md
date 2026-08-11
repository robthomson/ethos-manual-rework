---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Logiske brytere

![Meny for logiske brytere](../assets/model-lsw-menu.png)

Logiske brytere er brukerprogrammerte *virtuelle* brytere — ikke fysiske
betjeningsorganer, men brukbare overalt der en fysisk bryter kan brukes, som
utløser for en programfunksjon. Hver av dem evaluerer sin konfigurerte
betingelse mot inngangene sine (andre brytere, telemetriverdier, miksverdier,
timerverdier, gyro-/trenerkanaler og mer) og blir sann eller falsk. Opptil 100
støttes; ingen finnes som standard. Legg til en med **+**; menyetiketten til en
definert bryter vises grønn når den er sann, og rød når den er falsk. Trykk på
en eksisterende for **Edit**/**Move**/**Copy-paste**/**Clone**/**Delete**.

![Legg til logisk bryter](../assets/model-lsw-add.png)

## Funksjon

Alle funksjoner støtter normal eller invertert utgang.

- **A ~ X** — sann når kilden `A` er *omtrent* lik (innenfor ca. 10 %) en fast
  verdi `X`. Vanligvis å foretrekke framfor eksakt likhet —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — for med `A = X` kan en telemetriverdi som varierer mellom for eksempel
  8,5 V og 8,35 V rundt et mål på 8,4 V rett og slett aldri treffe nøyaktig
  8,4 V, slik at bryteren aldri utløses.
- **A = X** — sann bare når `A` er nøyaktig lik `X`.
- **A > X** / **A < X** — sann når `A` er større/mindre enn `X`.
- **|A| > X** / **|A| < X** — som over, men sammenligner absoluttverdien til
  `A` (fortegn ignoreres).
- **Δ > X** — sann når endringen i `A` (delta) i løpet av **Kontrollintervall**
  når minst `X`. Et intervall på `---` betyr et uendelig tidsvindu.

  ![Delta større enn X](../assets/model-lsw-delta-gtX.png)
  ![Absolutt delta større enn X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — som over, men med absoluttverdien av endringen.
- **Range** — sann når `A` ligger innenfor et angitt område.

  ![Range](../assets/model-lsw-range.png)

- **AND** — sann bare hvis alle oppførte kilder (Value 1…N) er sanne.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — sann hvis minst én oppført kilde er sann.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (eksklusiv ELLER) — sann hvis *nøyaktig én* oppført kilde er sann.

  ![XOR](../assets/model-lsw-XOR.png)

- **Timer-generator** — går fritt på/av kontinuerlig: på i **Varighet aktiv**,
  av i **Varighet inaktiv**.

  ![Timer-generator](../assets/model-lsw-timer-generator.png)

- **Sticky** — en lås (SR-vippe); se [nedenfor](#sticky).
- **Edge** — en momentan puls; se [nedenfor](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Låser seg **sann** så snart betingelsen **Utløser PÅ** er oppfylt, og forblir
sann til **Utløser AV** er oppfylt — eventuelt begrenset av **Aktiv betingelse**
(så lenge denne er falsk, holdes utgangen falsk uansett; Sticky-låsen fortsetter
å evaluere i bakgrunnen og kobles gjennom til utgangen igjen så snart Aktiv
betingelse blir sann, med forbehold om forsinkelser).

Fra Ethos 1.6.2 godtar begge utløserne en **Edge**-modifikator (langt trykk på
`ENT` på utløserbetingelsen, velg Edge — vises med prefikset `†`) for mye
finere kontroll:

![Sticky med edge](../assets/model-lsw-sticky-with-edge.png)
![Valg av Edge-alternativ](../assets/model-lsw-sticky-edge-select.png)

- **Utløser PÅ `SA` (ingen forsinkelse)** — låses sann i samme øyeblikk SA går
  høy.
- **Utløser PÅ `SA` (forsinkelse = 1 s)** — låses sann 1 s etter at SA går høy,
  *forutsatt* at SA fremdeles er høy når sekundet er omme.
- **Utløser PÅ `†SA` (forsinkelse = 1 s)** — låses sann→falsk 1 s etter at SA
  går høy, **uavhengig** av om SA fremdeles er høy da (flanken har allerede
  inntruffet; forsinkelsen tidfester bare resultatet).

Utløser AV virker på samme måte i omvendt rekkefølge. Forsinkelser gjelder
**etter** Aktiv betingelse — så en endring i Aktiv betingelse utløser
forsinkelsestiden på nytt før den låste verdien når utgangen igjen. Hvis begge
utløserne går fra falsk→sann samtidig, **veksler** Sticky-utgangen én gang. Se
også [Felles parametere](#shared-parameters) nedenfor.

### Edge

![Edge](../assets/model-lsw-edge.png)

En momentan puls: sann i **Varighet**, når utløserbetingelsen er oppfylt.
**I løpet av** er et `[t1:t2]`-par som styrer nøyaktig når:

- **Stigende flanke, I løpet av = 0,0 s** — utløses i samme øyeblikk Utløser PÅ
  går falsk→sann.

  ![Stigende flanke](../assets/model-lsw-edge-rising-edge.png)
  ![I løpet av = 0](../assets/model-lsw-edge-during-eq0.png)

- **Stigende flanke, I løpet av ≥ 0,0 s (f.eks. 5,0 s)** — utløses 5 s etter at
  Utløser PÅ blir sann, og ignorerer kortere «spiker» innenfor de 5 sekundene.

  ![I løpet av > 0, stigende flanke](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![I løpet av > 0](../assets/model-lsw-edge-during-gt0.png)

- **Fallende flanke, I løpet av = 0,0 s** — utløses i samme øyeblikk Utløser PÅ
  går sann→falsk.
- **Fallende flanke, I løpet av ≥ 0,0 s (f.eks. 3,0 s)** — utløses ved
  overgangen sann→falsk, men bare hvis den først har vært sann i minst 3 s.
- **Puls (både t1 og t2 satt)** — utløses bare hvis Utløser PÅ går
  falsk→sann→falsk innenfor det vinduet (f.eks. mellom 2 s og 5 s senere).

## Felles parametere {: #shared-parameters }

![Felles parametere](../assets/model-lsw-common-parameters.png)

- **Aktiv betingelse** — begrenser bryterens utgang på samme måte som for
  Sticky ovenfor. Alternativer: Alltid på, posisjoner for
  bryter/funksjonsbryter/logisk bryter/trim, Telemetri, Flymoduser, eller en
  systemhendelse (Gasshold, Gasskutt, Gass aktiv, Telemetri aktiv, RSSI lav,
  Trener aktiv, Flynullstilling).
- **Forsinkelse før aktiv** / **Forsinkelse før inaktiv** — hvor lenge
  betingelsen må holde seg sann (eller falsk) før utgangen følger, opptil 60 s.
  Ikke relevant for Timer-generator eller Edge. (Se [Praktisk guide:
  Kapasitetsvarsel for batteri](../how-to/battery-capacity-warning.md) for en
  forsinkelse brukt til å filtrere bort et spenningsfall.)
- **Bekreftelse før aktiv** / **inaktiv** — ber om bekreftelse fra brukeren før
  tilstanden faktisk endres (med et Avbryt-alternativ, for tilfeller der den
  utløses så ofte at den blir ubrukelig) — praktisk for å sikre noe risikabelt,
  f.eks. bekreftelse før man slår av et bakkekjøretøy via fjernstyring.

  ![Bekreft sann](../assets/model-lsw-confirm-lsw-true.png)
  ![Bekreft falsk](../assets/model-lsw-confirm-lsw-false.png)

- **Min. varighet** — når bryteren er blitt sann, forblir den sann i minst så
  lenge. Står den på `---`, kan utgangen være sann i bare én mikssyklus — for
  kort til at man i det hele tatt ser linjen bli uthevet i grensesnittet.
- **Maks. varighet** — når bryteren er blitt sann, går den automatisk tilbake
  til falsk etter så lang tid, dersom den fortsatt er satt. Begge varighetene
  går opp til 60 s.
- **Kommentar** — fritekst som vises overalt der denne bryteren legges til i en
  verdi-widget, for å dokumentere formålet.

## Bruk med telemetri

En systemhendelse av typen **Telemetri aktiv** (eller en bryter med en
telemetrisensor som kilde, aktiv bare mens sensoren rapporterer data) dekker
betingelser av typen «mottas det telemetri nå».

!!! warning
    En [miks](mixes.md) som styres av en telemetribasert logisk bryter trenger
    en **ekstra** miks-handling som bruker samme bryter **invertert**, slik at
    miksen fortsatt har en gyldig verdi når telemetrien mistes — husk at en
    inaktiv miks gir nøytral utgang (0 % / 1500 µs, eller **halv gass** på en
    gasskanal). Alternativt kan du bruke en **Offset**-handling, som allerede
    har egne aktive/inaktive verdier innebygd — f.eks. kilde **0**
    (spesialverdien) med offset satt slik at miksen leser +100 % mens `LS3` er
    aktiv og −100 % mens den er inaktiv, dekker begge tilfeller i én handling.

## Sammenligning av kilder

En kilde sammenlignes normalt med en fast verdi, men to kilder av *samme* type
kan i stedet sammenlignes direkte — f.eks. to timere, to spenninger eller to
turtallssensorer.

## Ignorer trenerinngang fra elev

![Ignorer trenerinngang](../assets/model-lsw-ignore-trainer-input.png)

En kildes [alternativer](../getting-started/user-interface-and-navigation.md#choosing-a-source)
kan utelate trenerinngang fra en tilkoblet elevsender (slave) — brukes
typisk på en logisk bryter som overvåker **instruktørens** egen
spakbevegelse (f.eks. for å gripe inn umiddelbart hvis noe går galt), uten at
elevens innganger også utløser den. Kombineres ofte med en trenerbryter som
styrer instruktørens egen Aktiv betingelse.
