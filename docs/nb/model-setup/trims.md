---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trim

![Trim](../assets/model-trims.png)

Konfigurerer trimområde, stegstørrelse og oppførsel for hver spak, i
tillegg til krysstrim og øyeblikkelig trim. **X20 Pro/R/RS** og **X18** har
to ekstra trimbrytere, **T5**/**T6**, som er nyttige for justeringer under
flyging utover de fire hovedspakene:

![T5/T6-trim](../assets/model-trims-pro-t5-t6.png)

Hver spak har sitt eget uavhengige sett med triminnstillinger.

## Triminnstillinger {: #trim-settings }

- **Område** – standard ±25 %, justerbart opp til spakens fulle ±100 %. På
  hovedskjermen viser en trim med standardområde −100 til 100; en trim med
  fullt område (100 %) viser −400 til 400 (4× det normale området).

  !!! warning
      Et større område betyr at det å holde en trimtast for lenge kan legge
      inn nok trim til at modellen blir uflybar.

- **Steg** – oppløsningen til trimbryteren: **Ekstra fin**, **Fin**,
  **Medium**, **Grov**, **Eksponentiell** (fin nær senter, grov lenger ut)
  eller **Egendefinert** (en bestemt prosentandel per klikk).

  ![Stegvalg](../assets/model-trims-step-options.png)

  | Steg | µs per klikk (25 % område) |
  |---|---|
  | Ekstra fin | 0,5 |
  | Fin | 1 |
  | Medium | 2 |
  | Grov | 4 |
  | Eksponentiell | 0,3–16 |

  Egendefinert, med 25 % område: 1 % steg = 1 µs/klikk, 100 % steg =
  128 µs/klikk. Med 100 % område: 1 % steg = 5 µs/klikk, 100 % steg =
  512 µs/klikk.

## Modus

![Trimmodus for høyderor](../assets/model-trims-mode-elevator.png)

Som standard er en trim alltid aktiv, men **Modus** endrer denne
oppførselen. Å endre modus nullstiller trimmen til 0.

- **OFF** – deaktiverer trimmen fullstendig.

  ![Modus: av](../assets/model-trims-mode-option-off.png)

  Nyttig for eksempel på en elektrisk modell uten behov for gasstrim – den
  frigjorte trimkontrollen kan da [brukes til å justere en
  Var i stedet](variables.md).

- **Easy** – én felles trimverdi på tvers av alle flymoduser. Det vanlige
  valget for krengeror og sideror, siden disse sjelden trenger å variere
  med flymodus.

  ![Modus: easy](../assets/model-trims-mode-option-easy.png)

- **Uavhengig per flymodus** – trimmen påvirker bare den aktive flymodusen.
  Det vanlige valget for høyderorstrim, siden høyderorstrim ofte må være
  forskjellig fra flymodus til flymodus (f.eks. ved endringer i
  vingeprofilens kamber) – dette er faktisk ofte hovedgrunnen til å sette
  opp flymoduser i det hele tatt.

  ![Modus: uavhengig per flymodus](../assets/model-trims-mode-option-fm.png)

- **Egendefinert** – helt egendefinert oppførsel, satt sammen av
  **oppførsler** du legger til selv.

### Egendefinerte trimoppførsler

![Legg til en oppførsel](../assets/model-trims-mode-elevator-add-behaviour.png)
![Valg for oppførsel](../assets/model-trims-mode-elevator-edit-behaviour.png)

Hver oppførselsrad har en betingelse og ett av følgende:

- **Unplugged** – deaktiverer trimmen selektivt under denne betingelsen
  (i stedet for å slå den helt av med Modus = OFF).

  ![Unplugged](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Betingelse for unplugged](../assets/model-trims-mode-unplugged-select.png)

- **Normal** (standard) – vanlig trimoppførsel.
- **Equal (til en annen trim)** – denne trimmen følger trimverdien til en
  annen betingelse nøyaktig.

  ![Equal](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Offset + (en annen trim)** – denne trimmen legges oppå trimverdien til
  en annen betingelse.

  ![Offset](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Gjennomgått eksempel** – et seilfly med en grunnleggende
høyderorstrim for **Cruise**, og avhengige trim for **Speed** og
**Thermal**:

![Velg FM5 Speed](../assets/model-trims-mode-elevator-custom-select.png)
![Velg FM4 Thermal](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Trim for horisontal flyging i standardmodusen (Cruise).
2. Legg til en oppførsel: **Offset + Default**, betingelse `FM5(Speed)`. Nå
   lagres enhver trimjustering gjort i Speed-modus som en forskyvning oppå
   grunnverdien for Cruise – separat, men fortsatt avhengig av den.

   ![Offset for Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Legg til en andre oppførsel: **Offset + Default**, betingelse
   `FM4(Thermal)`, på samme måte. (Så snart den første oppførselen finnes,
   tilbyr dialogen også `Equal FM5(Speed)` og `Offset + FM5(Thermal)` som
   alternativer, siden den nå også kan referere til den oppførselen.)

   ![Offset for Speed og Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Med dette oppsettet vil en senere justering av grunntrimmen for Cruise
(for eksempel etter en endring av tyngdepunktet) automatisk forskyve
trimmen for Speed og Thermal med samme mengde, siden de er forskyvninger
oppå den og ikke uavhengige verdier.

- **Audio** – slå av den vanlige trimannonseringen for en trim som er
  brukt til noe annet, dersom det ikke lenger er meningsfullt å høre den.

## Ekstra trim

![Legg til ekstra trim](../assets/model-trims-add-trim-select.png)
![Innstillinger for ekstra trim](../assets/model-trims-add-trim-edit.png)

**Legg til en ekstra trim** oppretter en trim utover de fire
standardspakene (og T5/T6): **Navn**, **Opp**/**Ned**-kilder som styrer
den, i tillegg til de samme valgene for **Område**, **Steg**, **Modus** og
**Audio** som over.

## Krysstrim

![Krysstrim](../assets/model-trims-cross.png)
![Redigering av krysstrim](../assets/model-trims-cross-edit.png)

Angir hvilken trimbryter som faktisk justerer hver spak – det vil si at en
spaks trim kan styres av en annen fysisk trimkontroll enn normalt. (T5/T6
er bare tilgjengelig på X20 Pro og X18.)

## Øyeblikkelig trim {: #instant-trim }

![Øyeblikkelig trim](../assets/model-trims-instant-trim.png)

Så lenge funksjonen er aktiv, legges de gjeldende spakposisjonene inn i de
tilsvarende standardtrimmene (og krysstrimmene). Bør legges på en bryter du
kan nå uten å slippe spakene – aktiver den mens du flyr rett og
horisontalt for å sette trimmen umiddelbart, i stedet for å klikke gjentatte
ganger på en trimtast når trimmen er svært feil. Slå den av igjen etter
trimflygingen for å unngå å forstyrre trimmen ved et uhell senere.

!!! note
    Øyeblikkelig trim er bare aktiv mens du ser på en av hovedvisningene.

## Flytt trim til subtrim

![Flytt trim til subtrim](../assets/model-trims-move-trims-to-subtrims.png)

Etter at du har trimmet for horisontal flyging, flytter denne funksjonen en
kanals trimverdi (f.eks. høyderor) inn i kanalens
[Subtrim](outputs.md)-innstilling og nullstiller trimmen på skjermen – en
ryddig måte å bekrefte at flytrimmen ikke har endret seg siden sist.

Med flymoduser i bruk kan en kanal ha mer enn én relevant trimverdi, mens
Subtrim under Utganger er én global innstilling som gjelder for alle
flymoduser. Denne funksjonen tar hensyn til det: den tar trimmen for den
**valgte** flymodusen, flytter den inn i Subtrim, nullstiller den trimmen
og justerer trimmen i alle *andre* flymoduser på samme kanal for å
kompensere – slik at den faktiske roroverflateposisjonen i hver flymodus
totalt sett blir uendret.

!!! tip
    Kjør alltid dette fra samme «grunnleggende» flymodus (f.eks. Cruise på
    et seilfly) for konsistens – så lenge du gjør det, kan funksjonen
    gjentas trygt.

Store trim- eller subtrimverdier gir svært asymmetriske utslag – det er
bedre å rette årsaken mekanisk. Sikt mot at styrestagene står i 90° når
rorflatene er nøytrale (flaps er unntaket, der du bytter noe oppvandring
mot mer nedvandring), og bruk deretter **PWM center** for å finjustere til
nøyaktig 90° når koblingen er nær nok.
