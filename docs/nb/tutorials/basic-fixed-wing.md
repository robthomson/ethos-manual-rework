---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Grunnleggende eksempel med fastvinge

En komplett gjennomgang for et fly med motor + 2 krengeror + 2 flaps +
høyderor + sideror, ett servo per rorflate, bygget fra start til slutt med
veiviseren. Fullfør [Første oppsett av senderen](initial-radio-setup.md) først.

## Steg 1. Bekreft systeminnstillingene

Dette eksempelet bruker standard kanalrekkefølge **AETR**.

## Steg 2. Kartlegg nødvendige servoer/kanaler

[Mikser](../model-setup/mixes.md) er hjertet i senderen — opptil 100
mikskanaler, normalt med de laveste numrene tilordnet servoer (siden
kanalnumrene svarer direkte til mottakerkanalene; den interne RF-modulen i
X20 støtter opptil 24 utgangskanaler). Høyere kanaler er ledige for
virtuelle kanaler eller flere reelle kanaler via flere RF-moduler og
SBUS. Vårt flystell:

| Funksjon | Kanaler |
|---|---|
| Motor | 1 |
| Krengeror | 2 |
| Flaps | 2 |
| Høyderor | 1 |
| Sideror | 1 |

(Inntrekkbart understell legges til senere, i [Steg 10](#step-10-add-a-mix-for-retracts).)

## Steg 3. Opprett en ny modell

![Opprett flymodell](../assets/tut-fw-eg-wiz-create-airplane.png)

Fra [Modellvalg](../model-setup/model-select.md) velger du en kategori,
trykker **+** og starter veiviseren **Airplane**. Velg **Non stabilized
receiver** for dette eksempelet.

![Motorkanaler](../assets/tut-fw-eg-wiz-engine.png)
![Kanaler for krengeror/flaps](../assets/tut-fw-eg-wiz-ail-flaps.png)

Godta 1 motorkanal, deretter 2 kanaler for krengeror, og velg 2 kanaler
for flaps.

![Haletype](../assets/tut-fw-eg-wiz-tail.png)
![Kanaler for høyderor/sideror](../assets/tut-fw-eg-wiz-ele-rudd.png)

Godta standardvalget **Traditional Tail**, med 1 kanal for høyderor og 1
for sideror.

![Modellnavn](../assets/tut-fw-eg-wiz-name.png)
![Mottaker](../assets/tut-fw-eg-wiz-rx.png)

Gi den et navn (f.eks. «FWexample» — opptil 15 tegn), fullfør veiviseren,
og den blir den aktive modellen, opprettet i kategorien Airplane.

## Steg 4. Gjennomgå og konfigurer miksene

![Oversikt over mikser](../assets/tut-fw-eg-mixes.png)

Veiviseren har allerede laget mikser for krengeror (kanal 1 og 5),
høyderor, gass, sideror og flaps (flaps viser `---` — ingen kilde er
tilordnet ennå).

### Krengeror {: #ailerons }

![Miks for krengeror](../assets/tut-fw-eg-mixes-ail-mix.png)
![Rediger miks for krengeror](../assets/tut-fw-eg-mixes-ail-edit.png)

**Weight/Rates** — sett opp utslagsnivåene før du flyr noe nytt: moderat
utslag (f.eks. 30 %) passer til sportsflyging, fulle 100 % passer til 3D.
Legg til et nivå på 60 % for bryter SB i midtstilling, og 30 % for SB ned —
standardverdien (SB opp) forblir 100 %:

![Utslagsnivåer](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — en lineær respons kan føles nervøs rundt senter; legg til
Expo-nivåer (f.eks. 60 %/40 %/20 % på de samme SB-posisjonene) for å flate
ut responsen nær senter uten å redusere maksimalt utslag:

![Expo-nivåer](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Differensial** — like store utslag opp/ned på krengerorene gir mer
motstand på det krengeroret som går ned enn på det som går opp, noe som
girer modellen bort fra svingen («ugunstig gir»). Et positivt differensial
(50 % er vanlig) reduserer utslaget nedover i forhold til oppover for å
motvirke dette:

![50 % differensial](../assets/tut-fw-eg-mixes-ail-diff-50.png)

For å justere differensialet under flyging kan du holde inne `ENT` på
verdien, velge **Use a source** og velge Pot1:

![Bruk en kilde](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Pot1 valgt](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Når du er fornøyd med verdien fra flygingen, holder du inne igjen og velger
**Convert to value** for å låse den permanent:

![Konverter til verdi](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim** — kan kobles fra denne miksen uten å deaktivere trimmen selv, slik
at den frigjøres til et annet formål:

![Trim for krengeror](../assets/tut-fw-eg-mixes-ail-trim.png)

### Høyderor og sideror

Samme mønster med tre utslagsnivåer + Expo, her på bryter SC:

![Expo-nivåer for høyderor](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Gass

![Gassmiks](../assets/tut-fw-eg-mixes-thr-edit.png)

La inngangen stå på gasspaken — ingen utslagsnivåer eller Expo er nødvendig
— men en sikkerhetsbryter er helt avgjørende; en modellmotor som starter
uventet kan forårsake alvorlig personskade.

**Low position trim** (glødeplugg-/bensinmotorer) — justerer
tomgangsturtallet uavhengig av full gass:

![Low position trim](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Når den er aktivert, ligger gasskanalen på −75 % med spaken i tomgang;
gasstrimmen justerer da tomgangen mellom −100 % og −50 %.

**Gasskutt** — en sikkerhetssperre. Med bryter SA ned som aktiv betingelse
(vises i fet skrift når den er aktiv), holdes gassutgangen på −100 % så
snart spaken kommer under −85 %:

![Gasskutt](../assets/tut-fw-eg-mixes-thr-cut.png)

Med **Sticky** aktivert i stedet kuttes gassen **umiddelbart** når SA
settes ned, uavhengig av spakposisjonen:

![Sticky gasskutt](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

Uansett metode må spaken føres tilbake under −85 % etter at den aktive
betingelsen opphører, før gassen kan økes igjen — dette hindrer at motoren
hopper til en høy gassposisjon i det øyeblikket kuttbryteren slippes.

**Gasshold** — et nødkutt fra *enhver* spakposisjon, som senker utgangen
direkte til −100 % (eller en konfigurert verdi) i det øyeblikket
betingelsen er oppfylt:

![Gasshold](../assets/tut-fw-eg-mixes-thr-hold.png)

### Flaps

![Inngang for flaps](../assets/tut-fw-eg-mixes-flaps-input.png)

Tilordne flaps til bryter SE, og sett vekten på begge utgangskanalene til
100 %:

![Vekter for flaps](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Steg 5. Bind mottakeren

Registrer (hvis ACCESS) og bind via [RF System](../model-setup/rf-system.md).
Før du går videre til Utganger, bør du vurdere å koble fra
servoforbindelsene eller redusere servovandringen midlertidig, for å unngå
å overbelaste noe mens du setter Min/Max-grensene.

## Steg 6. Konfigurer utgangene

![Utganger](../assets/tut-fw-eg-outputs.png)

[Utganger](../model-setup/outputs.md) tilpasser mikserens logikk til
modellens faktiske mekanikk.

**Aileron 1** — sentrer servoen med **PWM center** etter at du har
optimalisert den mekaniske forbindelsen, og sett deretter **Min**/**Max**.
Å midlertidig tilordne et potensiometer til Min (og deretter Max, på samme
måte som i differensial-eksempelet ovenfor) gjør dette raskere å finjustere:

![Rediger utgang for krengeror](../assets/tut-fw-eg-outputs-edit-ail.png)

**Flaps** — flaps trenger vanligvis et stort utslag nedover for effektiv
bremsing; man ofrer noe utslag oppover i forbindelsen for å oppnå det, slik
at flapsen står halvveis nede når servoen står i senter, og bruker deretter
Min/Max for å sette de faktiske posisjonene opp og helt ned. En kurve med 5
punkter er en vanlig måte å korrigere eventuelle avvik mellom flaps og
krengeror. Avslutt med **[Balance
channels](../model-setup/outputs.md#balance-channels)** for å synkronisere
venstre/høyre krengeror og flaps.

## Steg 7. Introduksjon til flymoduser

[Flymoduser](../model-setup/flight-modes.md) lar en modell ha innstillinger
per oppgave — som å skifte gir. Av de 20 tilgjengelige bruker dette
eksempelet tre: **Default**, **Flaps Half** (bryter SE i midtstilling) og
**Flaps Full** (SE opp). Den første flymodusen med oppfylt betingelse er
aktiv; modusen **Default** har ingen betingelse i det hele tatt, og tar
over når ingen andre gjelder — derfor har den ingen valgmulighet for
bryter. Inn-/uttoning på 1 sekund gjør overgangen mykere når flapsen kjøres
ut.

## Steg 8. Konfigurer trimmene

To måter å håndtere at høyderortrimmen varierer med flapsposisjonen:

**Uavhengige trimmer per flymodus** — det enkleste alternativet:
høyderortrimmen blir helt uavhengig per flymodus, og skifter automatisk når
SE flyttes. Siden hver modus trimmes fra bunnen av, er [Instant
trim](../model-setup/trims.md#instant-trim) nyttig — trim først for normal
flyging, land deretter og bruk dette som utgangspunkt for flaps-modusene.

**Grunntrim med forskyvning** — trim én gang i Default, med hver
flaps-modus' høyderorkompensasjon lagt på toppen som en forskyvning:

1. Sett trimmens **Step** til Medium (for raskere innledende trimming;
   reduser senere for finjustering), **Mode** til Custom, og legg til en ny
   virkemåte.
2. **Active condition**: `FM1(Flaps Half)`, modus **Offset + Default** —
   trimmen for Flaps Half blir grunntrim + den forskyvningen som stilles
   inn mens denne modusen er aktiv:

   ![Legg til virkemåte](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Gjenta for `FM2(Flaps Full)`:

   ![Velg FM](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Hver flaps-modus kan nå trimmes uavhengig, men å justere grunntrimmen i
Default senere (f.eks. for å korrigere termisk drift i servoen) forskyver
begge flaps-modustrimmene like mye automatisk.

![Valg av egendefinert trim](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Steg 9. Sett opp en timer for flybatteriet

I [Timers](../model-setup/timers.md) redigerer du Timer 1: modus **Down**,
startverdi 5 minutter, som går når **Throttle active** er sann (og den ikke
holdes i nullstilling). Du kan eventuelt tilordne en proporsjonal
tidskilde (f.eks. gasspaken) slik at timeren går i sanntid ved full gass og
går saktere når gassen reduseres.

## Steg 10. Legg til en miks for inntrekkbart understell {: #step-10-add-a-mix-for-retracts }

![Kilde for understellsmiks](../assets/tut-fw-eg-retracts-source.png)

Trykk på en miks, **Add Mix** → **Free Mix**, gi den navnet «Retracts»,
sett betingelsen til Always, og kilden til bryter SF. Standardhandlingen
med Weight = 100 % er greit — dette tilordner f.eks. kanal 8 til det
inntrekkbare understellet:

![Utgang for understell](../assets/tut-fw-eg-retracts-outputs.png)
