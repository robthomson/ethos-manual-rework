---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# RF-systeem

Configureert de interne en/of externe RF-module(s) van het model, het
Owner Registration ID, het binden van de ontvanger en de
ontvangeropties. Hier wordt ook de keuze tussen de interne en externe
module van een model vastgelegd — in tegenstelling tot vrijwel al het
andere in [Systeeminstellingen](../system-setup/index.md) is de keuze van
RF-hardware **per model** en niet zenderbreed.

!!! note "Schermafbeeldingen volgen nog"
    De set schermafbeeldingen voor dit hoofdstuk is nog niet vastgelegd
    (zie [Screenshot-pipeline](../contributing/screenshot-pipeline.md)) —
    de inhoud hieronder is correct, maar voorlopig alleen tekst.

## Owner registration ID {: #owner-registration-id }

Een unieke code van 8 tekens (een mix van hoofdletters, kleine letters en
cijfers, geen speciale tekens) die bij registratie het
**Registration ID** van een ontvanger wordt. Stel *dezelfde* code in op
meerdere zenders om **Smart Share** tussen die zenders te kunnen
gebruiken — doe dit vóór het aanmaken van het model dat je wilt delen.
Compatibel met EdgeTX; slechts gedeeltelijk compatibel met OpenTX.

## RF-uitgang uitschakelen

Houd `PAGE` ingedrukt tijdens het opstarten om zowel de interne als de
externe RF-uitgang voor die sessie uit te schakelen (een waarschuwing
bevestigt dat deze uit is). De instelling **State** van de module zelf
blijft op ON staan — een normale herstart herstelt de normale zending.

## Modi van de interne module

De interne module van de X18/X20/X20S/X20HD (TD-ISRM) werkt in een van
drie modi — de TD-ISRM Pro-module van de X20 Pro/R/RS is vergelijkbaar,
maar voegt LoRa- en tandem-dualbandvarianten toe. Welke modus je ook
kiest, deze **moet overeenkomen met wat de ontvanger ondersteunt**,
anders mislukt het binden; controleer na het wisselen van modus zorgvuldig
elk kanaal en vooral het failsafe-gedrag.

- **ACCESS** — de 2,4GHz- en 900MHz-paden werken in tandem onder één set
  ACCESS-instellingen. Maximaal drie ontvangers in totaal, in elke
  combinatie van 2,4GHz (24 kanalen) en 900MHz (16 kanalen); telemetrie
  van beide banden is gelijktijdig actief en wordt per band gelabeld. Een
  telemetriebron **RX** geeft aan welke ontvanger momenteel de actieve
  telemetriebron is.
- **ACCST D16** — één enkel 2,4GHz-pad, voor oudere ontvangers uit de
  "X"-serie.
- **TD mode** — tandem 2,4GHz + 900MHz met lage latentie en groot bereik
  voor Tandem-ontvangers, 24 kanalen op elke band.

**Flex-firmware**-builds voegen een tweede kolom Type toe om onder elk
van de drie bovenstaande modi te wisselen tussen FLEX915M-modulatie
(FCC-stijl, 915MHz) en FLEX868M (LBT-stijl, 868MHz) — voor de gekozen
variant moeten de juiste antennes zijn gemonteerd. Gebruikers in de EU
kunnen 200/500mW op 868MHz gebruiken; bij 25mW loopt telemetrie via
868MHz, bij 200/500mW schakelt deze naar 2,4GHz om aan de regelgeving te
voldoen.

Elke keuze van modus/kanaalbereik gaat gepaard met een compromis in
verversingssnelheid — bijvoorbeeld onder ACCESS worden 8 kanalen elke 7ms
bijgewerkt, 16 kanalen elke 14ms en 24 kanalen elke 21ms (roterend in
blokken van 8), en een **Racing mode** van 4ms is beschikbaar op kanaal
1-8 met compatibele ontvangers (RS-serie, v2.1.7+).

## Een ontvanger registreren en binden (ACCESS) {: #registering-and-binding-a-receiver-access }

Het binden van een ACCESS-ontvanger bestaat uit twee fasen —
**registratie** hoeft slechts eenmaal per combinatie van
ontvanger/zender te gebeuren; **binden** kan daarna draadloos worden
herhaald zonder bindknop.

**Fase 1 — Registreren**:

1. Tik op **Register** (sla dit volledig over als de ontvanger al
   geregistreerd is).
2. Houd de bindknop van de ontvanger ingedrukt terwijl je deze inschakelt;
   wacht tot beide LED's oplichten. Het dialoogvenster verandert van
   "Waiting for receiver…" naar "Receiver connected" en vult automatisch
   de naam van de ontvanger in.
3. Bevestig of wijzig het **Registration ID** (standaard het hierboven
   ingestelde Owner Registration ID — overeenkomende ID's op meerdere
   zenders zijn precies wat Smart Share laat werken), de **Rx name** en
   het **UID**. Het UID onderscheidt meerdere ontvangers die samen in één
   model worden gebruikt — laat dit op 0 staan bij één ontvanger; bij
   meerdere (bijvoorbeeld één per blok van 8 kanalen) is het gebruikelijk
   om 0/1/2 te gebruiken. Het UID kan naderhand niet uit de ontvanger
   worden uitgelezen, dus label de ontvanger fysiek.
4. Tik op **Register**, bevestig "Registration ok" en schakel de ontvanger
   daarna uit — deze is nu geregistreerd, maar nog niet gebonden.

**Fase 2 — Binden**:

!!! warning
    Bind nooit met een aangesloten elektromotor of een draaiende
    brandstofmotor.

1. Ontvanger uit; controleer of je in de juiste modulemodus staat.
2. Tik op **RX1** (of 2/3) → **Bind**. Een terugkerende
   spraakmelding "Bind" bevestigt de bindmodus.
3. Schakel de ontvanger in **zonder** de bindknop aan te raken; selecteer
   deze in de lijst "Select device" die verschijnt.
4. Bevestig "Bind successful". Schakel zowel de zender als de ontvanger
   uit en weer in — een groene LED aan en rode LED uit op de ontvanger
   betekent dat de verbinding tot stand is gekomen. Binden hoeft niet te
   worden herhaald, tenzij een van beide zijden wordt vervangen.
5. Herhaal dit voor eventuele extra ontvangers (RX2, RX3).

## Ontvangeropties

Tik met de ontvanger ingeschakeld op de bijbehorende RX-knop voor:

- **Options** — **Telemetry** (aan/uit voor deze ontvanger), **Reduced
  telemetry power 25mW** (in plaats van de normale 100mW — nuttig als
  servo's in de buurt RF-storing oppikken), **High PWM Speed**
  (servo-update van 7ms in plaats van 18ms — controleer of je servo's dit
  aankunnen), **Telemetry port** (S.Port/F.Port/FBUS), **SBUS** (16 of 24
  kanalen — elk aangesloten SBUS-apparaat moet SBUS-24 ondersteunen
  voordat je dit inschakelt) en **Channel Mapping** om kanalen naar
  specifieke ontvangerpinnen toe te wijzen.
- **Share** — draagt de ontvanger over aan een andere ACCESS-zender met
  een *ander* Owner Registration ID. Tik op de bronzender op Share (de
  groene LED gaat uit); bind op de doelzender zoals gewoonlijk — Share
  slaat de herregistratie over omdat het ID automatisch wordt
  overgedragen. Verlaat Share op de bronzender om het delen te
  beëindigen; opnieuw binden brengt de ontvanger terug. (Helemaal niet
  nodig als alle zenders al hetzelfde Owner Registration ID hebben — bind
  dan simpelweg direct op de zender die de controle moet krijgen.)
- **Reset bind** — ruimt op na een Share en herstelt je eigen bind;
  schakel de ontvanger daarna uit en weer in.
- **Factory reset** — reset de ontvanger en wist het UID, waarmee de
  ontvanger volledig wordt gederegistreerd.

Met de ontvanger **uit** biedt dezelfde RX-knop **Options** (wacht tot de
ontvanger verbinding maakt), **Bind** (bijvoorbeeld om een ontvanger
opnieuw te binden die eerder elders gebonden was) en **Clear**
(gelijkwaardig aan Reset bind).

## Redundante ontvangers {: #redundant-receivers }

Een tweede ontvanger kan aan een ongebruikt RX-slot worden gebonden voor
redundantie — 2,4G en 900M kunnen elkaar beide als back-up dienen. De
FrSky-redundantie beoordeelt **per frame** en gebruikt altijd het beste
beschikbare frame (active/active-failover), zodat de besturing indien
nodig van frame tot frame tussen ontvangers kan wisselen.

1. Verbind de SBUS Out van de redundante ontvanger met de SBUS In van de
   hoofdontvanger.
2. Schakel de bijbehorende interne RF-module in (bijvoorbeeld 900M) en
   stel de antenne/het zendvermogen in.
3. Registreer de nieuwe ontvanger (indien nog niet gedaan) en bind deze
   vervolgens aan het vrije RX-slot zoals hierboven beschreven.
4. Controleer of de groene LED brandt — de ontvanger staat nu vermeld als
   redundante ontvanger.

## Failsafe {: #failsafe }

Failsafe-gegevens worden ongeveer elke 10 seconden opnieuw door de zender
verzonden; bij TD/TW/AP/AP Plus-ontvangers worden ze ook in de ontvanger
zelf opgeslagen, zodat ze een herstart van de ontvanger overleven.
Controleer failsafe zorgvuldig opnieuw na elke firmware-upgrade van de
ontvanger die dit gedrag toevoegt.

- **Hold** — houdt de laatst ontvangen kanaalposities vast.
- **Custom** — per kanaal: **Not Set**, **Hold**, **Custom** (een vaste
  waarde — tik op het pijlicoon om de huidige waarde over te nemen, of
  voer er direct één in) of **No Pulses**.
- **No Pulses** — stopt de pulsen volledig, voor flightcontrollers met
  hun eigen return-to-home-gedrag bij signaalverlies.
- **Receiver** — (ontvangers uit de X-serie of nieuwer) stelt failsafe in
  op de ontvanger zelf.

!!! warning
    Test de door jou gekozen failsafe-instelling zorgvuldig voordat je
    erop vertrouwt.

## Bereiktest {: #range-check }

Voer deze op het veld uit vóór elke vliegsessie met een nieuwe of
gewijzigde configuratie. Het selecteren van **Range Check** verlaagt
bewust het zendvermogen (een terugkerende spraakmelding bevestigt de
modus) en toont live VFR%/RSSI om de verbindingskwaliteit te beoordelen.
Het zendvermogen van FrSky's bereiktest ligt ongeveer −10dB onder het
normale bedrijfsniveau van +20dB; op 1m hoogte voor zowel zender als
ontvanger mag je rond de 30m een kritiek alarm verwachten — dichterbij dan
dat kan onder normale omstandigheden op een probleem wijzen.

Bij meerdere gebonden ontvangers worden de bereiktestgegevens per band
voor één actieve ontvanger tegelijk weergegeven — door de momenteel
actieve ontvanger uit te schakelen neemt de volgende (in prioriteit
0/1/2, zichtbaar via de sensor **RX**) het over, zodat elke ontvanger op
zijn beurt kan worden getest.

## Externe en RF-modules van derden

Externe FrSky-modules (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
volgen hetzelfde Register/Bind-patroon als de interne module, met
protocolspecifieke kanaalaantallen, zendvermogens en antenne-eisen —
raadpleeg de handleiding van de betreffende module voor de exacte
gegevens.

**ELRS** (ExpressLRS) wordt ondersteund via zowel de ELRS-modus van de
TWIN Lite Pro-module als via echte ELRS-modules (waarvoor het ELRS
Lua-script in `scripts/elrs` geïnstalleerd moet zijn voordat ze als
module-optie verschijnen). Twaalf kanalen; de belangrijkste instellingen
zijn **Packet Rate** (afweging tussen latentie en bereik), **Telemetry
Ratio** (hoe vaak telemetrie wordt verzonden, 1:1 tot 1:128), **Switch
Mode** (**Hybrid** — de meeste hulpkanalen teruggebracht tot 2–3 posities
voor lagere latentie — of **Wide** — volledige resolutie van 64–128
stappen), **Model Match** en **Tx Power** (10mW–1000mW, optioneel
**Dynamic Power** om automatisch met de verbindingskwaliteit mee te
schalen — vereist ingeschakelde telemetrie).

**Modules van derden** (momenteel Ghost, Multi-protocol en Crossfire,
naast ELRS) hebben elk hun eigen, door de gebruiker te installeren
Lua-script nodig — zie de opmerkingen over `scripts/` in
[Screenshot-pipeline](../contributing/screenshot-pipeline.md) en de
thread *Third-Party External Modules* op rcgroups. Het item van een
module verschijnt pas op het RF-scherm zodra het bijbehorende script is
geïnstalleerd. De Multi-protocol-module (IRX4 Lite) kan bovendien direct
vanuit [Bestandsbeheer](../system-setup/file-manager.md) van nieuwe
firmware worden voorzien: kopieer het firmwarebestand naar `Firmware/` en
kies vervolgens **Flash external multimodule**.
