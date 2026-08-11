---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telemetri

![Oppdagede sensorer](../assets/model-telemetry-discovered-new-sensors.png)

Telemetri sender informasjon tilbake fra modellen til piloten — link-
kvalitet (RSSI, VFR), spenninger og strømmer, samt alt annet en tilkoblet
sensor rapporterer (GPS-posisjon, høyde og så videre). Opptil 100 sensorer
støttes per modell; oppdagelse og konfigurasjon skjer her, men telemetri
*vises* faktisk som [widgeter på skjermene](../displays/index.md), som
konfigureres separat under Konfigurer skjermer.

## Hvordan FrSky-telemetri fungerer {: #how-frsky-telemetry-works }

FrSkys sensorer krever ingen hub: **Smart Port (S.Port)** er en buss med
tre ledere (Gnd, V+, signal), som seriekobles i vilkårlig rekkefølge inn i
S.Port-tilkoblingen på mottakere fra X/S-serien og senere, og som kjører
halv duplex på 57 600 bps (F.Port og FBUS er raskere).

- **Physical ID** — opptil 28 noder (inkludert mottakeren) deler bussen,
  og hver av dem må ha en unik Physical ID (00–1B heksadesimalt).
  FrSky-enheter leveres med fornuftige standardverdier (f.eks.
  Vario = 00, FLVSS = 01, Current = 02, GPS = 03) — kobler du til to av
  samme enhet, må Physical ID på den andre endres via [Enhetsoppsett](../system-setup/devices.md).
- **Application ID** — uavhengig av Physical ID: én sensor kan rapportere
  flere verdier, hver med sin egen Application ID. En Vario har én
  Physical ID, men to Application ID-er (høyde, vertikalhastighet); en
  FLVSS har én Physical ID og én Application ID (spenning). Skal du
  overvåke to 6S-pakker med to FLVSS-sensorer, må **begge** ID-ene endres
  på den andre — Physical ID for eksklusiv kommunikasjon på bussen, og
  Application ID slik at mottakeren kan skille Lipo 1 fra Lipo 2 (f.eks.
  `0300` → `0301`). Det er normalt det fjerde heksadesimale sifferet som
  varieres, 0–F.

  !!! note
      At sensorer deler Application ID men har forskjellige Physical
      ID-er, er kun gyldig når [deteksjon av
      sensorkonflikter](../system-setup/alerts.md) er deaktivert — et
      spesialtilfelle, ikke normalsituasjonen.

Hver mottatt verdi følges som en egen sensor: verdi, Physical/Application
ID, et redigerbart navn, enhet, antall desimaler, et valgfritt flagg for
logging til SD-kort, samt sine egne løpende min/maks-verdier. Sensorer
oppdages automatisk ved hver oppstart når de først er satt opp, men må
oppdages **manuelt** første gang. Når en sensor er oppdaget, kan den leses
opp med tale, brukes i [beregnede sensorer](#calculated-sensors),
[logiske brytere](logical-switches.md), [Vars](variables.md) eller
[mikser](mixes.md), vises på en egendefinert telemetriskjerm, eller leses
direkte fra denne oppsettsiden uten at du lager en skjerm i det hele tatt.

**FBUS** (tidligere F.Port2) tar dette et steg videre ved å slå sammen
SBUS-styring og S.Port-telemetri på én linje med 460 800 bps (mot F.Ports
115 200 og S.Ports 57 600 — de tre bitratene er innbyrdes inkompatible),
og gjør det mulig for én vert å snakke med flere slaveenheter på den samme
linjen, alt konfigurerbart trådløst fra senderen.

### Telemetri med flere mottakere (ACCESS Trio)

Med opptil tre mottakere registrert under [RF-system](rf-system.md#registering-and-binding-a-receiver-access)
kan hver bundet mottaker konfigureres individuelt (portpinner osv.) via
RX1/RX2/RX3. Normalt finnes det én innkommende telemetribane per RF-link —
Tandem/TD-systemene er unntaket, med 2,4 GHz og 900 MHz som to baner på én
modul. Den aktive telemetrikilden kan endres midt i flyturen avhengig av
RF-forholdene; sensoren **RX** rapporterer i sanntid hvilken mottaker som
sender telemetri (og logger det).

Det vanlige oppsettet: seriekoble S.Port-sensorbussen gjennom alle tre
mottakerne med felles strømforsyning, og deretter registrere/binde hver
mottaker og oppdage sensorer som normalt — telemetrikilden bytter
automatisk når den aktive mottakeren endres, og data fra *eksterne*
S.Port-sensorer følger transparent med. (Mottakerinterne sensorer — RSSI,
VFR, RxBatt, ADC2 og RX selv — kobles ikke på denne måten; de rapporteres
alltid for den mottakeren som er kilden akkurat da. Samtidig telemetri fra
alle tre er planlagt, men ikke tilgjengelig ennå.)

## Sensorer for linkkvalitet

- **RSSI** (Receiver Signal Strength Indicator) — hvor sterk senderens
  utsending er ved mottakeren. Standardalarmer: **ACCESS**/**TD**/**TW**
  35 (lav) / 32 (kritisk), kontrolltap rundt 28; **ACCST** 45 / 42,
  kontrolltap rundt 38. «Telemetri tapt» utløses når linken er helt borte
  — på det tidspunktet **kan ingen flere alarmer lyde**, siden senderen
  ikke har noen telemetri å vurdere; se det som et signal om å snu
  umiddelbart. (Ved under ca. 1 m avstand kan mottakeren bli overmettet og
  gi falske løkker med tapt/gjenopprettet-alarmer — det er ikke en reell
  feil.) RSSI gir en god tilnærming til effektiv rekkevidde, men VFR er
  den mer pålitelige indikatoren for linkkvalitet.

  ![RSSI-sensor](../assets/model-telemetry-edit-rssi-sensor.png)

  TD-mottakere rapporterer RSSI per bånd (2.4G, 900M); TW-mottakere
  rapporterer også én per bånd (2.4FSK, 2.4LoRa, 900M) — aktiver
  **Individuelt RSSI-varsel per bånd** for å få separate talevarsler for
  hvert bånd i stedet for ett samlet varsel:

  ![Individuelt RSSI-varsel](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — gyldige pakker per 100 mottatte;
  erstatningen etter ACCESS 2.1 for å legge tapt rammerate inn i RSSI.
  Standard **Varsel ved lav verdi** er 50 %.

  ![VFR-sensor](../assets/model-telemetry-edit-vfr-sensor.png)

  TD/TW-mottakere rapporterer to VFR-strømmer (én per bånd); **Rx VFR**
  (på TD/TW/AP/AP Plus-mottakere) teller derimot alle gode rammer
  uavhengig av hvilket bånd de kom inn på — den du bør følge dersom du kun
  overvåker én VFR-verdi.

- **RxBatt** — mottakerens batterispenning.
- **ADC2** — en ekstra analog spenningsinngang, på mottakere som støtter
  det.
- **SWR** — antennens SWR, ved bruk av ekstern antenne.
- Sensorer for stilling/bevegelse, der det støttes: **R.Angle**,
  **P.Angle**, **AccX/Y/Z**.

Alle numeriske sensorer får også automatiske min/maks-sensorer
`<name>-`/`<name>+`, selv om de ikke vises i hovedlisten over sensorer.

## Oppdage sensorer {: #discovering-sensors }

![Oppdag nye sensorer: på](../assets/model-telemetry-discover-new-sensors-on.png)

Når alt er bundet og har strøm, aktiverer du **Oppdag nye sensorer** — en
blinkende prikk (eller en rød verdi, dersom det ennå ikke finnes data)
markerer hver sensor etter hvert som den blir funnet, og skjermen fylles
automatisk. Dette må gjentas **per modell**, og på nytt hver gang en ny
sensor legges til.

![Oppdag nye sensorer: av](../assets/model-telemetry-discover-new-sensors-off.png)

- Slå oppdagelsen **Av** igjen når du er ferdig.
- **Slett alle** fjerner alle sensorer, slik at du kan starte på nytt.

  ![Sensorer slettet](../assets/model-telemetry-sensors-deleted.png)

- **Konkurransemodus** reduserer telemetrien til kun RSSI og RxBatt — for
  konkurranser som bare tillater sensorer for linkstatus. Slår du modusen
  av igjen, kreves en av- og påslåing før sensorer kan oppdages på nytt.

  ![Bekreft konkurransemodus](../assets/model-telemetry-comp-only-confirm.png)

- Telemetrimodusen **Bluetooth** parer med FrSkys FreeLink-app for
  mobiltelefon, som kan vise telemetri i sanntid og også konfigurere
  FrSky-enheter som stabiliserte mottakere.

  ![Bluetooth-telemetri](../assets/model-telemetry-bt-option.png)

## Redigere en sensor {: #editing-a-sensor }

![Valg av redigeringsalternativ](../assets/model-telemetry-edit-option-select.png)

Trykk på en sensor for **Rediger**, **Flytt**, **Nullstill** eller
**Slett**. Vanlige felt: **Verdi** (skrivebeskyttet), **ID** (Physical +
Application ID, samt sendende mottaker), **Navn**, **Enhet**,
**Desimaler**, **Område** (faste skaleringsgrenser — hovedsakelig relevant
når sensoren brukes som kanalkilde), **Skriv logger**, **Nullstill** (en
kilde som nullstiller denne sensoren) og **Forsinkelse for varsel om tapt
sensor** (kan deaktiveres helt, eller settes til 1–30 s, standard 10 s,
for å filtrere korte utfall — vær klar over risikoen ved å sette denne for
høyt; meldingen om tapt sensor spilles bare én gang selv om mange sensorer
faller ut samtidig; deaktivert som standard for mottakerinterne sensorer,
siden disse sjelden forsvinner).

Noen sensorer har egne tilleggsfelt:

- **ADC2** — **Ratio** og **Offset**, for å korrigere skaleringen.

  ![Redigering av ADC2-sensor](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — terskler for **Kritisk verdi** og **Varsel ved lav verdi**.
- **VFR** — **Varsel ved lav verdi** (standard 50 %).
- **VSpeed** (vertikalhastighet fra vario) — **Område** opptil ±100 m/s
  (standard ±10 m/s). Selve lydoppførselen for vario ligger nå under
  [spesialfunksjonen Play Vario](special-functions.md), ikke her.

  ![Redigering av VSpeed-sensor](../assets/model-telemetry-edit-vspeed-sensor.png)

## DIY-sensorer / tredjepartssensorer

![Opprett DIY-sensor](../assets/model-telemetry-diy-sensor-select.png)

**Opprett DIY-sensor** legger til en sensor som ikke er fra FrSky,
manuelt: **Automatisk gjenkjenning** (fyller ut Physical ID, Application
ID og modul automatisk, om mulig), eller sett dem manuelt, i tillegg til
**Protokolldesimaler/-enhet** (innkommende presisjon, 0–3 desimaler, og
sensorens egen enhet) og **Visningsdesimaler/-enhet** (uavhengig av
protokollens egne), sammen med de samme feltene **Område**/**Ratio**/
**Offset**/**Skriv logger**/**Nullstill**/**Forsinkelse for varsel om tapt
sensor** som for alle andre sensorer.

![Automatisk gjenkjenning av DIY-sensor](../assets/model-telemetry-diy-sensor-auto-detect.png)

## Beregnede sensorer {: #calculated-sensors }

![Opprett beregnet sensor](../assets/model-telemetry-calculated-sensor-select.png)

Lag en ny sensor utledet fra én eller flere eksisterende:

- **Forbruk** — brukt energi, integrert fra en strømsensor (f.eks.
  FAS-serien). Enhet mAh/Ah, område opptil 1000 Ah.

  ![Forbrukssensor](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Avstand** — fra en GPS-kilde (pluss en høydekilde, for 3D-avstand).
  Enheter cm/m/km/ft, opptil 20 km.

  ![Avstandssensor](../assets/model-telemetry-calculated-sensor-distance.png)

- **Tur** — akkumulert avstand mellom påfølgende GPS-posisjoner. Samme
  enheter, opptil 1000 km.

  ![Tursensor](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — kobler to eller flere Lipo-spenningssensorer i kaskade
  for å overvåke pakker større enn 6S (opptil 67,2 V/8S). Velg hver
  cellesensor fra lav til høy; hver ekstra Lipo-sensor må først få både
  Physical **og** Application ID endret i
  [Enhetsoppsett](../system-setup/devices.md) (oppsettsverktøyet for
  Lipo Voltage der er til hjelp), oppdages én om gangen og gis nytt navn
  slik at de kan skilles fra hverandre.

  ![Multi Lipo-sensor](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Prosent** — skalerer en sensor om til 0–100 %, med et
  **Inverter**-alternativ (f.eks. for å vise *gjenstående* prosent i
  stedet for forbrukt).

  ![Prosentsensor](../assets/model-telemetry-calculated-sensor-percent.png)

- **Effekt** — watt fra et par av en **Strøm**- og en **Spenning**-kilde,
  opptil 1 000 000 W.

  ![Effektsensor](../assets/model-telemetry-calculated-sensor-power.png)

- **Egendefinert** — en vilkårlig formel satt sammen fra én eller flere
  kilder.

Alle beregnede sensorer har også **Vedvarende** (beholdes ved
avslåing/modellbytte, og lastes inn igjen ved neste bruk) samt en
**Nullstill**-knapp direkte på redigeringsskjermen.

### Egendefinerte sensorer

![Egendefinert sensor](../assets/model-telemetry-edit-custom-sensor.png)

Starter med én kilde, og med **Legg til** kobles flere operasjoner på:
**Add(+)**, **Minus(-)**, **Multiply(×)**, **Divide(/)**, **Min**,
**Max**, **Sqrt**. Enheter velges fra en lang liste som dekker spenning,
strøm, kapasitet, effekt, avstand, hastighet, tid, temperatur, prosent,
vinkler, trykk og mer; område −1 000 000 til 1 000 000, 0–4 desimaler.

![Legg til en beregningslinje](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "Topp-effekt"
    Multipliser en spenningssensor (`VFAS`) med en strømsensor
    (`Current`), og legg deretter til et **Max**-trinn som refererer til
    sensorens egen aktuelle verdi (`MaxPower`) for å følge den høyeste
    målte verdien — 288 W i dette eksempelet:

    ![MaxPower-eksempel](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "Regning mot en konstant"
    Kilden er satt til `RSSI 2.4G` (viser 64 dB), deretter en
    **Subtract**-handling der dens egen kilde langtrykkes og **Konverter
    til verdi** brukes, slik at den blir en redigerbar konstant (20) i
    stedet for en levende kilde — resultatet er stabile 44 dB (64 − 20):

    ![Subtract-eksempel](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![Konverter til verdi](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "En kildes interne verdi"
    Hver [kilde](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    har et internt heltallsområde på ±1024 som tilsvarer det viste
    området ±100 % — dette kan ses direkte ved å peke en egendefinert
    sensor mot for eksempel Gass: full gass viser internt **+1024**, full
    revers viser **−1024**.

    ![Intern verdi ved maks](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![Intern verdi ved min](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
