---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Maskinvare

![Maskinvaresjekk](../assets/system-hardware-check-x20s.png)

Testing og kalibrering av senderens fysiske betjeningsorganer, definisjon av
bryktertyper og tastekartet for hjemmetastene.

## Maskinvaresjekk {: #hardware-check }

Aktiverer hver enkelt fysisk inngang slik at du kan bekrefte at alle
registreres korrekt.

![Maskinvaresjekk X20 Pro](../assets/system-hardware-check-x20pro.png)
![Maskinvaresjekk X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — sjekker også de to låsende trykkbryterne **K** og **L**
  på baksiden av skuldrene, samt tilleggstrimmene **T5**/**T6**.
- **X18** — sjekker også tilleggstrimmene **T5**/**T6**.

## Kalibrering av analoge innganger {: #analogs-calibration }

![Kalibrering av analoge innganger](../assets/system-hardware-analogs-calibration.png)

Lærer senderen nøyaktig hvor senterposisjonen og endeutslagene til hver
spakenhet, hvert potensiometer og hver glidebryter befinner seg. Kjøres
automatisk ved første oppstart; gjenta prosedyren etter at en spakenhet, et
potensiometer eller en glidebryter er byttet ut.

## Gyrokalibrering

![Gyrokalibrering](../assets/system-hardware-gyro-calibration.png)

Kalibrerer den innebygde gyroen slik at vinkelbaserte innganger reagerer
korrekt når senderen vippes — «vannrett» posisjon blir den måten du normalt
holder senderen på. Kjøres også automatisk ved første oppstart.

## Filter for analoge innganger

Et av/på ADC-filter for spakene, aktivert som standard — reduserer flimmer
rundt spaksenter. Dette er den **globale** innstillingen; det finnes også en
overstyring **per modell** av filteret for analoge innganger under
[Model Edit](../model-setup/model-edit.md).

## Innstillinger for potensiometre/glidebrytere {: #potssliders-settings }

Gi nye navn til potensiometrene og glidebryterne. **X20 Pro/R/RS** støtter i
tillegg to ekstra potensiometre, **Ext1**/**Ext2**, som vanligvis brukes til
3-akse spakenheter.

![ADC-verdier, potensiometre](../assets/system-hardware-pots-x20s.png)
![ADC-verdier, potensiometre (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Bryterinnstillinger {: #switches-settings }

![Brytere](../assets/system-hardware-switches.png)

- **Forsinkelse for deteksjon av midtstilling** — hindrer at en rask
  omlegging opp→ned (eller ned→opp) av en 3-posisjonsbryter et øyeblikk
  registreres som midtstilling; midtstillingen skal bare registreres når
  bryteren faktisk stopper der. Standardverdien er 0 ms, valgt for å passe
  «selvtest»-deteksjonen på CH12 i FrSkys stabiliserte mottakere.
- **Brytertype** — SA–SJ kan hver defineres som **None**, **Momentary**,
  **2 POS** eller **3 POS**, slik at du kan bytte funksjonalitet mellom
  fysiske brytere (f.eks. gi den momentane bryteren SH rollen som normalt
  ivaretas av 2-posisjonsbryteren SF) — begrenset av hva senderens faktiske
  kablingsopplegg støtter (en 3-posisjonsrolle kan som regel ikke tilordnes
  maskinvare som ikke er kablet for det).

  ![Brytervalg](../assets/system-hardware-switches-options.png)
  ![Ekstra brytere](../assets/system-hardware-switches-2.png)

- **Navneendring** — brytere kan endres fra SA–SJ til egendefinerte navn;
  navnene er globale for alle modeller.
- **X20 Pro** — har i tillegg trykkbryterne **K**/**L** på baksiden av
  skuldrene, samt posisjonene **M**/**N** dersom de er kablet (vanligvis
  for brytere i spakenden).

## Hjem-tastekart

Endrer hva hjemmetastene `SYS`, `MDL` og `DISP` (`TELE` på eldre sendere)
hopper til.

- **`DISP`** — både kort og langt trykk kan tilordnes en vilkårlig
  modellside, systemside, Konfigurer skjermer, Hjem eller flydataloggen.
  For konsistens med X10-serien settes langt trykk på `DISP` vanligvis til
  Konfigurer skjermer.
- **`SYS`/`MDL`** — bare langt trykk kan tilordnes på nytt (til samme
  utvalg av destinasjoner); et kort trykk åpner alltid henholdsvis system-
  eller modelldelen.

## Maskinvarealternativer for spesifikke sendere {: #radio-specific-hardware-options }

- **Aktivere oppgradering til haptiske spakenheter** (X20 Pro, X20R) —
  X20 Pro AW og X20RS leveres med MC20R-spakenheter som har haptiske
  vibrasjonsmotorer; dersom MC20R-spakenheter er ettermontert i en X20 Pro
  eller X20R, aktiverer du dem her (se
  [Special Functions](../model-setup/special-functions.md) for konfigurering
  av selve vibrasjonsmønstrene).

  ![Haptisk (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptisk (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Alternativ for rotasjonsbryter** (X20 Pro AW, X20R/RS) — disse senderne
  har en mer følsom rotasjonsbryter; aktiver **halve steg** for å dempe den.

  ![Alternativ for rotasjonsbryter (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## ADC-verdiinspektør {: #adc-value-inspector }

Viser de rå verdiene fra analog-til-digital-konverteringen som CPU-en leser
for hver analoge inngang:

![ADC-sjekk (X20S)](../assets/system-hardware-adc-check-x20s.png)
![ADC-sjekk (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 venstre spak vannrett, 2 venstre spak loddrett, 3 høyre spak
loddrett, 4 høyre spak vannrett, 5 Pot 1, 6 Pot 2, 7 midtre glidebryter,
8 venstre glidebryter, 9 høyre glidebryter.

**X20 Pro**: som over, men med to ekstra kanaler for eksterne
potensiometre (7 Ext1, 8 Ext2 — f.eks. spakmonterte potensiometre) satt inn
før glidebryterne, som dermed forskyves til 9 midtre glidebryter,
10 venstre glidebryter, 11 høyre glidebryter.
