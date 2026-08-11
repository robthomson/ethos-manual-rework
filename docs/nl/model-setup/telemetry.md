---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telemetrie

![Gevonden sensoren](../assets/model-telemetry-discovered-new-sensors.png)

Telemetrie stuurt informatie van het model terug naar de piloot —
verbindingskwaliteit (RSSI, VFR), spanningen en stromen, en al het andere
dat een aangesloten sensor rapporteert (GPS-positie, hoogte, enzovoort).
Er worden tot 100 sensoren per model ondersteund; het zoeken en
configureren gebeurt hier, maar telemetrie wordt daadwerkelijk
*weergegeven* als [widgets op displayschermen](../displays/index.md), die
apart worden geconfigureerd onder Schermen configureren.

## Hoe FrSky-telemetrie werkt {: #how-frsky-telemetry-works }

De sensoren van FrSky werken zonder hub: **Smart Port (S.Port)** is een
3-draadsbus (Gnd, V+, Signaal) die in willekeurige volgorde in serie
(daisy-chain) op de S.Port-aansluiting van ontvangers uit de X/S-serie en
later wordt aangesloten, en half-duplex werkt op 57.600 bps (F.Port en
FBUS zijn sneller).

- **Physical ID** — tot 28 knooppunten (inclusief de ontvanger) delen de
  bus, elk met een uniek Physical ID (00–1B hex). FrSky-apparaten worden
  geleverd met zinvolle standaardwaarden (bijv. Vario = 00, FLVSS = 01,
  Current = 02, GPS = 03) — sluit je twee identieke apparaten aan, dan
  moet het Physical ID van het tweede worden gewijzigd via [Device
  Config](../system-setup/devices.md).
- **Application ID** — onafhankelijk van het Physical ID: één sensor kan
  meerdere waarden rapporteren, elk met een eigen Application ID. Een
  Vario heeft één Physical ID maar twee Application ID's (hoogte,
  verticale snelheid); een FLVSS heeft één Physical ID en één Application
  ID (spanning). Het bewaken van twee 6S-packs met twee FLVSS-sensoren
  betekent dat **beide** ID's van de tweede gewijzigd moeten worden — het
  Physical ID voor exclusieve buscommunicatie, het Application ID zodat de
  ontvanger Lipo 1 en Lipo 2 kan onderscheiden (bijv. `0300` → `0301`).
  Normaal wordt alleen het 4e hexcijfer gevarieerd, 0–F.

  !!! note
      Sensoren die een Application ID delen maar verschillende Physical
      ID's hebben, zijn alleen toegestaan met [detectie van
      sensorconflicten](../system-setup/alerts.md) uitgeschakeld — een
      opstelling voor speciale doeleinden, niet het standaardgeval.

Elke ontvangen waarde wordt als een eigen sensor bijgehouden: waarde,
Physical/Application ID, een aanpasbare naam, eenheid, aantal decimalen,
een optionele markering voor logging op de SD card, en een eigen
lopende min/max. Sensoren worden na de eerste instelling bij elke
inschakeling automatisch gevonden, maar de eerste keer moeten ze
**handmatig** worden gezocht. Zodra een sensor is gevonden, kan hij door
een spraakmelding worden uitgesproken, worden gebruikt in [berekende
sensoren](#calculated-sensors), in [logische
schakelaars](logical-switches.md), [Vars](variables.md) of
[mixen](mixes.md), op een aangepast telemetriescherm worden weergegeven, of
direct vanaf deze instelpagina worden uitgelezen zonder dat er een scherm
gebouwd hoeft te worden.

**FBUS** (voorheen F.Port2) gaat nog een stap verder door SBUS-besturing
en S.Port-telemetrie op één lijn te combineren op 460.800 bps (tegenover
115.200 bij F.Port en 57.600 bij S.Port — de drie bitsnelheden zijn
onderling incompatibel), en maakt het mogelijk dat één host op die ene
lijn met meerdere slave-accessoires communiceert, allemaal draadloos
configureerbaar vanaf de zender.

### Telemetrie met meerdere ontvangers (ACCESS Trio)

Met tot drie ontvangers geregistreerd onder [RF
System](rf-system.md#registering-and-binding-a-receiver-access) kan elke
gebonden ontvanger afzonderlijk worden geconfigureerd (poortpinnen, enz.)
via RX1/RX2/RX3. Normaal is er één inkomend telemetriepad per RF-link —
de Tandem/TD-systemen zijn de uitzondering, met 2.4GHz en 900MHz als twee
paden op één module. De actieve telemetriebron kan tijdens de vlucht
wisselen afhankelijk van de RF-omstandigheden; de sensor **RX** meldt in
realtime welke ontvanger op dat moment telemetrie verzendt (en logt dit).

De gebruikelijke opstelling: schakel de S.Port-sensorbus in serie door
alle drie ontvangers, met een gemeenschappelijke voeding, registreer/bind
daarna elke ontvanger en zoek de sensoren zoals gebruikelijk — de
telemetriebron wisselt automatisch mee met de actieve RX, en *externe*
S.Port-sensorgegevens volgen transparant mee. (Interne sensoren van de
ontvanger — RSSI, VFR, RxBatt, ADC2 en RX zelf — worden niet op deze
manier gekoppeld; ze worden altijd gerapporteerd voor de ontvanger die op
dat moment de bron is. Gelijktijdige telemetrie van alle drie tegelijk is
gepland maar nog niet beschikbaar.)

## Sensoren voor verbindingskwaliteit

- **RSSI** (Receiver Signal Strength Indicator) — hoe sterk de uitzending
  van de zender bij de ontvanger aankomt. Standaardalarmen:
  **ACCESS**/**TD**/**TW** 35 (laag) / 32 (kritiek), verlies van controle
  rond 28; **ACCST** 45 / 42, verlies van controle rond 38. "Telemetry
  Lost" wordt gemeld wanneer de verbinding volledig weg is — op dat moment
  **kunnen er geen verdere alarmen meer klinken**, omdat de zender geen
  telemetrie meer heeft om te evalueren; beschouw dit als het signaal om
  onmiddellijk terug te keren. (Bij minder dan ongeveer 1 m afstand kan de
  ontvanger overbelast worden en valse Lost/Recovered-alarmlussen
  produceren — dat is geen echte storing.) RSSI benadert het effectieve
  bereik goed, maar VFR is de betrouwbaarder indicator voor
  verbindingskwaliteit.

  ![RSSI-sensor](../assets/model-telemetry-edit-rssi-sensor.png)

  TD-ontvangers rapporteren een RSSI per band (2.4G, 900M); TW-ontvangers
  ook één per band (2.4FSK, 2.4LoRa, 900M) — schakel **Individual RSSI
  alert per band** in om afzonderlijke spraakmeldingen per band te krijgen
  in plaats van één gecombineerde melding:

  ![Individuele RSSI-melding](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — geldige pakketten per 100 ontvangen
  pakketten; de vervanging, sinds ACCESS 2.1, van het verwerken van de
  frameverliesratio in de RSSI-waarde. De standaardwaarde voor **Low value
  warning** is 50%.

  ![VFR-sensor](../assets/model-telemetry-edit-vfr-sensor.png)

  TD/TW-ontvangers rapporteren twee VFR-stromen (één per band); **Rx VFR**
  (op TD/TW/AP/AP Plus-ontvangers) telt in plaats daarvan elk goed frame,
  ongeacht op welke band het aankwam — dat is de waarde om in de gaten te
  houden als je slechts één VFR-waarde volgt.

- **RxBatt** — accuspanning van de ontvanger.
- **ADC2** — een tweede analoge spanningsingang, op ontvangers die dit
  ondersteunen.
- **SWR** — antenne-SWR, bij gebruik van een externe antenne.
- Sensoren voor houding/beweging, waar ondersteund: **R.Angle**,
  **P.Angle**, **AccX/Y/Z**.

Elke numerieke sensor krijgt ook automatisch min/max-sensoren
`<naam>-`/`<naam>+`, ook al worden die niet in de hoofdsensorlijst
weergegeven.

## Sensoren zoeken {: #discovering-sensors }

![Nieuwe sensoren zoeken: aan](../assets/model-telemetry-discover-new-sensors-on.png)

Wanneer alles gebonden en ingeschakeld is, activeer je **Discover new
sensors** — een knipperende punt (of een rode waarde, als er nog geen data
is) markeert elke sensor zodra deze gevonden wordt, en het scherm vult
zich automatisch. Dit moet **per model** worden herhaald, en opnieuw
telkens wanneer er een nieuwe sensor wordt toegevoegd.

![Nieuwe sensoren zoeken: uit](../assets/model-telemetry-discover-new-sensors-off.png)

- Zet het zoeken weer **Off** wanneer je klaar bent.
- **Delete all** verwijdert alle sensoren zodat je opnieuw kunt beginnen.

  ![Sensoren verwijderd](../assets/model-telemetry-sensors-deleted.png)

- **Competition mode** beperkt de telemetrie tot alleen RSSI en RxBatt —
  voor wedstrijden waarbij uitsluitend sensoren voor de verbindingsstatus
  zijn toegestaan. Om deze modus weer uit te schakelen moet de zender
  worden uit- en ingeschakeld voordat sensoren opnieuw gevonden kunnen
  worden.

  ![Bevestiging competitiemodus](../assets/model-telemetry-comp-only-confirm.png)

- De telemetriemodus **Bluetooth** koppelt met de FrSky FreeLink-app voor
  de telefoon, die telemetrie live kan weergeven en ook FrSky-apparaten
  zoals gestabiliseerde ontvangers kan configureren.

  ![Bluetooth-telemetrie](../assets/model-telemetry-bt-option.png)

## Een sensor bewerken {: #editing-a-sensor }

![Optiekeuze bewerken](../assets/model-telemetry-edit-option-select.png)

Tik op een sensor voor **Edit**, **Move**, **Reset** of **Delete**.
Gebruikelijke velden: **Value** (alleen lezen), **ID** (Physical +
Application ID, en de verzendende ontvanger), **Name**, **Unit**,
**Decimals**, **Range** (vaste schaalgrenzen — vooral relevant wanneer de
sensor als kanaalbron wordt gebruikt), **Write logs**, **Reset** (een bron
die deze sensor terugzet) en **Sensor lost warning delay** (volledig
uitschakelen, of 1–30 s, standaard 10 s, om korte uitvallen te filteren —
besef het risico van een te hoge instelling; de melding "sensor lost"
wordt slechts eenmaal afgespeeld, ook als er meerdere sensoren tegelijk
wegvallen; standaard uitgeschakeld voor interne sensoren van de ontvanger,
omdat die zelden wegvallen).

Sommige sensoren voegen eigen velden toe:

- **ADC2** — **Ratio** en **Offset**, om de schaling te corrigeren.

  ![ADC2-sensor bewerken](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — drempelwaarden **Critical value** en **Low value warning**.
- **VFR** — **Low value warning** (standaard 50%).
- **VSpeed** (verticale snelheid van de vario) — **Range** tot ±100 m/s
  (standaard ±10 m/s). Het geluidsgedrag van de vario zelf valt nu onder
  de [speciale functie Play Vario](special-functions.md), niet hier.

  ![VSpeed-sensor bewerken](../assets/model-telemetry-edit-vspeed-sensor.png)

## DIY-sensoren / sensoren van derden

![DIY-sensor aanmaken](../assets/model-telemetry-diy-sensor-select.png)

**Create DIY Sensor** voegt handmatig een niet-FrSky-sensor toe: **Auto
detect** (vult indien mogelijk automatisch Physical ID, Application ID en
Module in), of stel deze handmatig in, plus **Protocol decimals/unit**
(de precisie van het inkomende signaal, 0–3 decimalen, en de eigen
eenheid) en **Display decimals/unit** (onafhankelijk van die van het
protocol zelf), naast dezelfde velden **Range**/**Ratio**/**Offset**/**Write
logs**/**Reset**/**Sensor lost warning delay** als bij elke andere sensor.

![DIY-sensor automatisch detecteren](../assets/model-telemetry-diy-sensor-auto-detect.png)

## Berekende sensoren {: #calculated-sensors }

![Berekende sensor aanmaken](../assets/model-telemetry-calculated-sensor-select.png)

Leid een nieuwe sensor af uit een of meer bestaande sensoren:

- **Consumption** — verbruikte energie, geïntegreerd uit een
  stroomsensor (bijv. de FAS-serie). Eenheid mAh/Ah, bereik tot 1000 Ah.

  ![Consumption-sensor](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Distance** — vanaf een GPS-bron (plus een hoogtebron, voor
  3D-afstand). Eenheden cm/m/km/ft, tot 20 km.

  ![Distance-sensor](../assets/model-telemetry-calculated-sensor-distance.png)

- **Trip** — opgetelde afstand tussen opeenvolgende GPS-fixes. Dezelfde
  eenheden, tot 1000 km.

  ![Trip-sensor](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — schakelt twee of meer Lipo-spanningssensoren in cascade
  om packs groter dan 6S te bewaken (tot 67,2 V/8S). Selecteer elke
  celsensor van laag naar hoog; bij elke extra Lipo-sensor moeten eerst
  zowel het Physical **als** het Application ID worden gewijzigd in
  [Device Config](../system-setup/devices.md) (de tool Lipo Voltage setup
  daar helpt hierbij), moet elke sensor één voor één worden gevonden, en
  moeten ze een eigen naam krijgen zodat ze te onderscheiden zijn.

  ![Multi Lipo-sensor](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Percent** — schaalt een sensor naar 0–100%, met een optie **Invert**
  (bijv. om het *resterende* percentage weer te geven in plaats van het
  verbruikte).

  ![Percent-sensor](../assets/model-telemetry-calculated-sensor-percent.png)

- **Power** — wattage uit een paar bronnen **Current** en **Voltage**, tot
  1.000.000 W.

  ![Power-sensor](../assets/model-telemetry-calculated-sensor-power.png)

- **Custom** — een willekeurige formule, geketend vanaf een of meer
  bronnen.

Elke berekende sensor heeft ook **Persistent** (blijft bewaard bij
uitschakelen/modelwissel, en wordt bij het volgende gebruik opnieuw
geladen) en een knop **Reset** direct op het bewerkscherm.

### Aangepaste sensoren

![Aangepaste sensor](../assets/model-telemetry-edit-custom-sensor.png)

Begint bij één bron, waarna **Add** verdere bewerkingen aan de keten
toevoegt: **Add(+)**, **Minus(-)**, **Multiply(×)**, **Divide(/)**,
**Min**, **Max**, **Sqrt**. Eenheden zijn te kiezen uit een lange lijst
met spanning, stroom, capaciteit, vermogen, afstand, snelheid, tijd,
temperatuur, percentage, hoeken, druk en meer; bereik −1.000.000 tot
1.000.000, 0–4 decimalen.

![Een rekenregel toevoegen](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "Piekvermogen"
    Multipliceer een spanningssensor (`VFAS`) met een stroomsensor
    (`Current`) en voeg daarna een stap **Max** toe die verwijst naar de
    eigen actuele waarde van de sensor (`MaxPower`), om de hoogst gemeten
    waarde bij te houden — 288 W in dit voorbeeld:

    ![MaxPower-voorbeeld](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "Rekenen met een constante"
    Bron ingesteld op `RSSI 2.4G` (meting 64 dB), daarna een actie
    **Subtract** waarvan de eigen bron lang wordt ingedrukt en waarop
    **Convert to value** wordt toegepast, zodat die in een aanpasbare
    constante (20) verandert in plaats van een live bron — het resultaat is
    een constante 44 dB (64 − 20):

    ![Subtract-voorbeeld](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![Convert to value](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "De interne waarde van een bron"
    Elke [bron](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    heeft een intern geheel-getalbereik van ±1024, dat overeenkomt met het
    weergegeven bereik van ±100% — direct te zien door een aangepaste
    sensor bijvoorbeeld op Gas te richten: vol gas leest intern **+1024**,
    volledig omgekeerd leest **−1024**.

    ![Interne waarde bij maximum](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![Interne waarde bij minimum](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
