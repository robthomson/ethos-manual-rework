---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# RF-system

Konfigurerer modellens interne og/eller eksterne RF-modul(er), eierens registrerings-ID, binding av mottaker og mottakeralternativer. Det er også her modellens valg mellom intern og ekstern modul ligger — i motsetning til nesten alt annet i [Systeminnstillinger](../system-setup/index.md) er valg av RF-maskinvare **per modell**, ikke felles for hele senderen.

!!! note "Skjermbilder kommer"
    Skjermbildene for denne delen er ennå ikke tatt (se
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)) — innholdet
    nedenfor er korrekt, men foreløpig kun i tekstform.

## Eierens registrerings-ID {: #owner-registration-id }

En unik kode på 8 tegn (blanding av store og små bokstaver og siffer, ingen spesialtegn) som blir mottakerens **Registration ID** når den registreres. Sett *samme* kode på flere sendere for å bruke **Smart Share** mellom dem — gjør dette før du oppretter modellen du vil dele. Kompatibel med EdgeTX; bare delvis kompatibel med OpenTX.

## Deaktivere RF-utgang

Hold `PAGE` inne under oppstart for å deaktivere både intern og ekstern RF-utgang for den økten (en advarsel bekrefter at den er av). Modulens egen **State**-innstilling forblir ON — en normal omstart gjenoppretter normal sending.

## Moduser for intern modul

Den interne modulen i X18/X20/X20S/X20HD (TD-ISRM) kjører i én av tre moduser — TD-ISRM Pro-modulen i X20 Pro/R/RS er tilsvarende, men har i tillegg LoRa og tandem dualbånd-varianter. Uansett hvilken modus som velges, **må den samsvare med det mottakeren støtter**, ellers vil bindingen mislykkes. Etter bytte av modus må du nøye kontrollere alle kanaler på nytt, og spesielt failsafe-oppførselen.

- **ACCESS** — 2,4 GHz- og 900 MHz-banene arbeider i tandem under ett sett ACCESS-innstillinger. Opptil tre mottakere totalt, i valgfri kombinasjon av 2,4 GHz (24 kanaler) og 900 MHz (16 kanaler); telemetri fra begge bånd er aktiv samtidig, merket med bånd. En **RX**-telemetrikilde viser hvilken mottaker som er aktiv telemetrikilde til enhver tid.
- **ACCST D16** — én enkelt 2,4 GHz-bane, for eldre mottakere i «X»-serien.
- **TD mode** — 2,4 GHz + 900 MHz i tandem med lav latens og lang rekkevidde for Tandem-mottakere, 24 kanaler på hvert bånd.

Utgaver med **Flex-firmware** legger til en ekstra Type-kolonne for å bytte mellom FLEX915M (915 MHz av FCC-typen) og FLEX868M (868 MHz av LBT-typen) modulasjon under alle de tre modusene over — riktige antenner må være montert for det som velges. Brukere i EU kan bruke 200/500 mW på 868 MHz; ved 25 mW går telemetrien på 868 MHz, ved 200/500 mW flyttes den til 2,4 GHz av regelverkshensyn.

Hvert valg av modus/kanalområde innebærer et kompromiss med oppdateringsraten — f.eks. under ACCESS oppdateres 8 kanaler hver 7. ms, 16 hver 14. ms og 24 hver 21. ms (rullerende i blokker på 8), og en **Racing mode** med 4 ms er tilgjengelig på kanal 1–8 med kompatible mottakere (RS-serien, v2.1.7+).

## Registrere og binde en mottaker (ACCESS) {: #registering-and-binding-a-receiver-access }

Binding av en ACCESS-mottaker skjer i to faser — **registrering** trenger bare å gjøres én gang per par av mottaker og sender; **binding** kan deretter gjentas trådløst uten bruk av bindingsknapp.

**Fase 1 — Register**:

1. Trykk på **Register** (hopp helt over dette hvis mottakeren allerede er registrert).
2. Hold mottakerens bindingsknapp inne mens du slår den på; vent til begge LED-ene lyser. Dialogen endres fra «Waiting for receiver…» til «Receiver connected» og fyller inn mottakernavnet automatisk.
3. Bekreft/rediger **Registration ID** (standardverdien er eierens registrerings-ID over — det er samsvarende ID-er på tvers av sendere som gjør at Smart Share fungerer), **Rx name** og **UID**. UID skiller mellom flere mottakere som brukes sammen i én modell — la den stå på 0 for én enkelt mottaker; ved flere (f.eks. én per blokk på 8 kanaler) er det vanlig å bruke 0/1/2. UID kan ikke leses tilbake fra mottakeren i ettertid, så merk den fysisk.
4. Trykk på **Register**, bekreft «Registration ok», og slå deretter av mottakeren — den er registrert, men ennå ikke bundet.

**Fase 2 — Bind**:

!!! warning
    Bind aldri med en elektrisk motor tilkoblet eller en motor i gang.

1. Mottakeren av; kontroller at du er i riktig modulmodus.
2. Trykk på **RX1** (eller 2/3) → **Bind**. En gjentakende taleopplysning «Bind» bekrefter bindingsmodus.
3. Slå på mottakeren **uten** å trykke på bindingsknappen; velg den fra listen «Select device» som vises.
4. Bekreft «Bind successful». Slå både senderen og mottakeren av og på — grønn LED på mottakeren lyser og rød er av når den er tilkoblet. Bindingen trenger ikke gjentas med mindre en av delene byttes.
5. Gjenta for eventuelle flere mottakere (RX2, RX3).

## Mottakeralternativer

Med mottakeren påslått trykker du på dens RX-knapp for:

- **Options** — **Telemetry** (av/på for denne mottakeren), **Reduced telemetry power 25mW** (kontra normale 100 mW — nyttig hvis nærliggende servoer plukker opp RF-støy), **High PWM Speed** (7 ms servooppdatering i stedet for 18 ms — kontroller at servoene dine tåler det), **Telemetry port** (S.Port/F.Port/FBUS), **SBUS** (16 eller 24 kanaler — alle tilkoblede SBUS-enheter må støtte SBUS-24 før dette aktiveres) og **Channel Mapping** for å tilordne kanaler til bestemte pinner på mottakeren.
- **Share** — overlater mottakeren til en annen ACCESS-sender med en *annen* eier-registrerings-ID. På kildesenderen trykker du på Share (dens grønne LED slukker); på målsenderen binder du som normalt — Share hopper over ny registrering, siden ID-en overføres automatisk. Avslutt på kildesenderen for å avslutte delingen; ny binding flytter den tilbake. (Dette er ikke nødvendig i det hele tatt hvis alle sendere allerede deler samme eier-registrerings-ID — da binder du bare direkte på den senderen som skal styre den.)
- **Reset bind** — rydder opp etter en Share og gjenoppretter din egen binding; slå mottakeren av og på etterpå.
- **Factory reset** — nullstiller mottakeren og sletter dens UID, slik at den avregistreres helt.

Med mottakeren **av** gir samme RX-knapp tilgang til **Options** (venter på at mottakeren kobler seg til), **Bind** (f.eks. for å binde en mottaker som tidligere var bundet et annet sted) og **Clear** (tilsvarer Reset bind).

## Redundante mottakere {: #redundant-receivers }

En ekstra mottaker kan bindes til en ubrukt RX-plass for redundans — 2,4G og 900M kan hver fungere som reserve for den andre. FrSkys redundans vurderes **per ramme** og bruker alltid den beste tilgjengelige rammen (aktiv/aktiv-omkobling), slik at styringen kan veksle mellom mottakerne fra ramme til ramme etter behov.

1. Koble SBUS Out på den redundante mottakeren til SBUS In på hovedmottakeren.
2. Aktiver den tilsvarende interne RF-modulen (f.eks. 900M) og angi antenne/effekt.
3. Registrer den nye mottakeren (hvis den ikke allerede er registrert), og bind den deretter til den ledige RX-plassen som beskrevet over.
4. Kontroller at den grønne LED-en lyser — den er nå oppført som redundant mottaker.

## Failsafe {: #failsafe }

Failsafe-data sendes fra senderen på nytt omtrent hvert 10. sekund; på TD/TW/AP/AP Plus-mottakere lagres de også i mottakeren, slik at de beholdes etter en omstart av mottakeren. Kontroller failsafe nøye på nytt etter en firmwareoppgradering av mottakeren som legger til denne oppførselen.

- **Hold** — holder de sist mottatte kanalposisjonene.
- **Custom** — per kanal: **Not Set**, **Hold**, **Custom** (en fast verdi — trykk på pilikonet for å hente inn gjeldende verdi, eller skriv inn en verdi direkte) eller **No Pulses**.
- **No Pulses** — stopper pulsene helt, for flykontrollere som har sin egen return-to-home-oppførsel ved signaltap.
- **Receiver** — (mottakere i X-serien eller nyere) setter failsafe i mottakeren i stedet.

!!! warning
    Test den failsafe-innstillingen du velger nøye før du stoler på den.

## Rekkeviddetest {: #range-check }

Utfør denne på flyplassen før hver flyøkt med et nytt eller endret oppsett. Ved å velge **Range Check** reduseres sendeeffekten bevisst (en gjentakende taleopplysning bekrefter modusen), og live VFR %/RSSI vises for å vurdere linkkvaliteten. FrSkys effektnivå ved rekkeviddetest er omtrent −10 dB i forhold til det normale driftsnivået på +20 dB; med 1 m høyde for både sender og mottaker kan du forvente kritisk alarm ved rundt 30 m — kortere avstand enn dette under normale forhold kan tyde på et problem.

Med flere bundne mottakere vises rekkeviddetestdata for én aktiv mottaker per bånd om gangen — ved å slå av den som er aktiv, tar den neste over (i prioritet 0/1/2, vist via **RX**-sensoren), slik at hver av dem kan kontrolleres etter tur.

## Eksterne og tredjeparts RF-moduler

FrSkys eksterne moduler (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro) følger samme mønster med Register/Bind som den interne modulen, med protokollspesifikke kanalantall, effektnivåer og antennekrav — se håndboken for den aktuelle modulen for eksakte verdier.

**ELRS** (ExpressLRS) støttes både via ELRS-modusen i TWIN Lite Pro-modulen og via ekte ELRS-moduler (som krever at ELRS Lua-skriptet er installert i `scripts/elrs` før de vises som et modulvalg). Tolv kanaler; sentrale innstillinger er **Packet Rate** (kompromiss mellom latens og rekkevidde), **Telemetry Ratio** (hvor ofte telemetri sendes, 1:1 til 1:128), **Switch Mode** (**Hybrid** — de fleste hjelpekanaler reduseres til 2–3 posisjoner for lavere latens — eller **Wide** — full oppløsning på 64–128 trinn), **Model Match** og **Tx Power** (10 mW–1000 mW, eventuelt **Dynamic Power** for å skalere automatisk etter linkkvalitet — krever at telemetri er aktivert).

**Tredjepartsmoduler** (foreløpig Ghost, Multi-protocol og Crossfire, i tillegg til ELRS) krever hver sitt eget brukerinstallerte Lua-skript — se merknadene om `scripts/` i [Screenshot Pipeline](../contributing/screenshot-pipeline.md) og tråden *Third-Party External Modules* på rcgroups. En moduls oppføring vises først på RF-skjermen når skriptet er installert. Multi-protocol-modulen (IRX4 Lite) kan i tillegg få firmware flashet direkte fra [Filbehandler](../system-setup/file-manager.md): kopier firmwarefilen til `Firmware/`, og velg deretter **Flash external multimodule**.
