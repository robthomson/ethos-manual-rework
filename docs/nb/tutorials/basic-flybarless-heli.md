---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Eksempel på enkelt flybarless-helikopter

Et enkelt oppsett for et flybarless (FBL) helikopter, med en kontroller
som Spirit som eksempel. I motsetning til en fastvingemodell er et
helikopter grunnleggende ustabilt — FBL-kontrolleren bruker gyroer
(rotasjonshastighet) og akselerometre (bevegelse/orientering) for å
beregne korreksjoner for yaw/pitch/roll via en innstilt PID-sløyfe
(Proportional-Integral-Derivative), som balanserer stabilitet,
responsivitet og oversving ut fra det enkelte helikopterets fysiske og
elektriske egenskaper.

Denne veiledningen dekker bare **programmeringen av senderen** — se
dokumentasjonen til din egen FBL-enhet for resten, og sørg for å ha solid
generell helikopterkunnskap på plass først.

!!! danger
    Fjern rotorbladene før du begynner, av sikkerhetshensyn.

## Trinn 1. Kontroller systeminnstillingene

Kanalrekkefølgen **AETR**, **[Første fire kanaler
låst](../system-setup/controls.md#first-four-channels-fixed)** **AV**
— Spirit FBL-enheter forventer SBUS-kanaler i nøyaktig denne rekkefølgen
(selv om de bruker TAER internt i sin egen konfigurasjon). Registrer (hvis
ACCESS) og bind mottakeren via [RF System](../model-setup/rf-system.md).

## Trinn 2. Kartlegg nødvendige servoer/kanaler

| Funksjon | Kanal |
|---|---|
| Roll (krengeror) | — |
| Pitch (høyderor) | — |
| Gass | — |
| Yaw (sideror) | — |
| Gyroforsterkning | 5 |
| Kollektiv pitch | 6 |
| Innstillingsbank | 7 |
| Rescue | 8 |

## Trinn 3. Opprett en ny modell

![Opprett helikoptermodell](../assets/tut-heli-eg-wiz-create-heli.png)

Fra [Modellvalg](../model-setup/model-select.md) oppretter/velger du en
Heli-kategori, starter veiviseren og velger **Flybarless**:

![Valg av FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Modellnavn](../assets/tut-heli-eg-wiz-name.png)

Gi modellen navn og velg et bilde.

## Trinn 4. Gjennomgå og konfigurer miksene

![Oversikt over mikser](../assets/tut-heli-eg-mixes.png)

Veiviseren oppretter Krengeror/Høyderor/Gass/Sideror i AETR-rekkefølge,
Pitch på kanal 6 og FBL Bank på kanal 7:

![Pitch-miks](../assets/tut-heli-eg-mixes-pitch.png)

Bekreft at kanal 6 er kollektiv pitch. To flere kanaler må legges til
manuelt som [frie mikser](../model-setup/mixes.md#mix-libraries):
**Gyroforsterkning** (kanal 5) og **Rescue/Stabi** (kanal 8).

**Krengeror/Høyderor/Sideror** — ingenting å legge til; rater og Expo er
FBL-enhetens oppgave, så senderen sender bare rene, lineære inngangsverdier
videre.

![Krengeror-miks](../assets/tut-heli-eg-mixes-ail.png)

**Kollektiv pitch** — en rett, lineær kurve; bekreft bare utgangskanalen
(normalt 6). Som over håndteres rater/Expo av FBL-enheten, ikke her.

**FBL Bank** — Spirits tre innstillingsbanker (ulike flystiler,
sensorforsterkning ved forskjellige turtall, eller Beginner/Acro/3D —
eller rett og slett forhåndsinnstillinger for finjustering) tilordnet en
3-posisjonsbryter, f.eks. SE:

![Bank-miks](../assets/tut-heli-eg-mixes-bank.png)

**Gyroforsterkning** — legges til som en fri miks etter siste kanal.
Forsterkningen er vanligvis en fast verdi: sett **Kilde** til Special
Value 0, still inn forsterkningen med **Offset** (finjusteres senere under
flyging), og send til kanal 5:

![Miks for gyroforsterkning](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Konfigurer flymoduser

![Flymoduser](../assets/tut-heli-eg-flight-modes.png)

Tre [flymoduser](../model-setup/flight-modes.md): gi standardmodusen nytt
navn til **Normal**, og legg til **Idle Up 1**/**Idle Up 2** på bryter SD.

### Konfigurer gassmiksen

Tre gasskurver, én per flymodus, hver av dem en [egendefinert
kurve](../model-setup/curves.md):

- **Normal** — oppspinning/avgang: starter på −100 % (motor av) og stiger
  jevnt. En 7-punktskurve med **Smooth** aktivert fungerer godt; de
  eksakte verdiene må finjusteres under flyging.

  ![Normal-kurve](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1** — vanlig flyging: en rettlinjet kurve som gir en konstant
  gassinnstilling og holder jevn rotorhastighet, der bevegelsen i stedet
  kommer fra kollektiv pitch, krengeror (roll) og høyderor (pitch). Hold
  overgangen fra Normal jevn — uten store sprang. (De fleste FBL-enheter
  har også en **Governor**-funksjon som holder rotorhastigheten konstant
  gjennom aggressive manøvrer — se FBL-enhetens egen bruksanvisning.)

  ![Idle Up 1-kurve](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2** — aggressiv flyging (akrobatikk, 3D); også denne
  finjusteres under flyging.

  ![Idle Up 2-kurve](../assets/tut-heli-eg-curves-iup2.png)

![Gasskurver i mikser](../assets/tut-heli-eg-mixes-thr-curves.png)

**Gasskutt** — tilordne f.eks. bryter SG opp med **Sticky** aktivert: å
vippe SG opp kutter gassen umiddelbart, og (på grunn av Sticky) kan den
bare aktiveres igjen når gasspaken først står lavt/av.

![Gasskutt](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescue/Stabi** — tilordnes på samme måte, f.eks. til bryter SA på kanal 8.

![Ferdige mikser](../assets/tut-heli-eg-mixes-final.png)

## Trinn 5. FBL-oppsett

1. **Installer konfigurasjonsverktøyet for FBL-enheten** — f.eks. Spirit
   Settings, på en PC.
2. **Koble mottakeren til FBL-enheten** i henhold til koblingsskjemaet —
   typisk mottakerens SBUS Out til FBL-enhetens RUD-port (noen
   Spirit-modeller trenger en SBUS-adapter), eller via F.Port1/FBUS i
   stedet.
3. **Koble FBL-enheten til PC-en** — med kabel eller Bluetooth, i henhold
   til bruksanvisningen.

   !!! danger
       Ikke koble til noen servoer ennå.

4. **Oppdater FBL-fastvaren** om nødvendig, fra Update-fanen i verktøyet.
5. **Generelt oppsett** (General-fanen i Spirit Settings):
   - Mottakertype: **Futaba SBUS** eller **FrSky F.Port** etter behov,
     deretter omstart.
   - Kanaltilordning (med AETR fra veiviseren):

     | Funksjon | Kanal |
     |---|---|
     | Gass | 1 |
     | Krengeror | 2 |
     | Høyderor | 3 |
     | Sideror | 4 |
     | Gyro | 5 |
     | Pitch | 6 |
     | Bank | 7 |
     | Rescue/Stabi | 8 |

     (Denne tilordningen følger av hvordan Spirit-enheten tolker
     posisjonene i SBUS-datastrømmen.)

6. **Kanalgrenser** (Diagnostic-fanen) — FBL-enheten trenger kalibrerte
   kanalgrenser fra senderen og verifiserte nøytralpunkter:

   - Nullstill først all subtrim og trim i senderen.
   - Sentrer spaken for kollektiv pitch slik at den viser nøyaktig 1500 µs
     i [Utganger](../model-setup/outputs.md).
   - Slå på FBL-enheten og bekreft at krengeror/høyderor/pitch/sideror alle
     viser 0 % i Diagnostic-fanen (FBL-enheten registrerer nøytralpunktet
     automatisk ved hver oppstart).
   - Beveg hvert styreorgan til endeutslagene og juster tilhørende **Min**/
     **Max** i Utganger til Diagnostic-fanen viser nøyaktig +100 %/
     −100 %, og bekreft samtidig at søyleretningen stemmer med
     spakretningen.

   !!! warning
       Bruk aldri subtrim eller trim på disse kanalene — Spirit
       FBL-enheten tolker dem som styrekommandoer, ikke som kalibrering.

7. Juster **Offset** i gyroforsterkningsmiksen for å oppnå Heading Lock.

Når dette er gjort, er senderdelen fullt konfigurert — fortsett med resten
av oppsettet i henhold til FBL-enhetens egen bruksanvisning.
