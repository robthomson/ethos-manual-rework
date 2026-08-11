---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Hardware-controle](../assets/system-hardware-check-x20s.png)

Testen en kalibreren van de fysieke bedieningselementen van de zender, de
definities van het schakelaartype en de toewijzing van de start-toetsen.

## Hardware-controle {: #hardware-check }

Doorloopt elke fysieke ingang, zodat u kunt controleren of ze allemaal
correct worden geregistreerd.

![Hardware-controle X20 Pro](../assets/system-hardware-check-x20pro.png)
![Hardware-controle X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — controleert ook de twee vergrendelende
  drukknopschakelaars **K** en **L** op de achterzijde, plus de extra trims
  **T5**/**T6**.
- **X18** — controleert ook de extra trims **T5**/**T6**.

## Kalibratie analoge ingangen {: #analogs-calibration }

![Analoge kalibratie](../assets/system-hardware-analogs-calibration.png)

Leert de zender precies waar het midden en de eindposities van elke gimbal,
potentiometer en schuifregelaar liggen. Dit wordt bij de eerste opstart
automatisch uitgevoerd; herhaal het na het vervangen van een gimbal,
potentiometer of schuifregelaar.

## Gyrokalibratie

![Gyrokalibratie](../assets/system-hardware-gyro-calibration.png)

Kalibreert de ingebouwde gyro, zodat op kanteling gebaseerde ingangen
correct reageren wanneer u de zender kantelt — de "waterpas"-positie wordt
de manier waarop u de zender normaal vasthoudt. Wordt eveneens bij de
eerste opstart automatisch uitgevoerd.

## Analoge filter

Een ADC-filter voor de sticks dat aan of uit kan, standaard aan — vermindert
jitter rond het stickmidden. Dit is de **globale** instelling; er bestaat
ook een instelling **per model** onder [Model bewerken](../model-setup/model-edit.md)
die deze overschrijft.

## Instellingen potentiometers/schuifregelaars {: #potssliders-settings }

Hier kunt u de potentiometers en schuifregelaars een andere naam geven. De
**X20 Pro/R/RS** ondersteunt daarnaast twee extra potentiometers,
**Ext1**/**Ext2**, doorgaans gebruikt voor 3-assige gimbals.

![ADC-waarden, potentiometers](../assets/system-hardware-pots-x20s.png)
![ADC-waarden, potentiometers (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Instellingen schakelaars {: #switches-settings }

![Schakelaars](../assets/system-hardware-switches.png)

- **Vertraging middenpositiedetectie schakelaar** — voorkomt dat een snelle
  omschakeling van boven naar beneden (of omgekeerd) van een
  3-positieschakelaar kortstondig de middenpositie registreert; het midden
  mag alleen worden geregistreerd wanneer de schakelaar daar daadwerkelijk
  stopt. De standaardwaarde is 0 ms, gekozen om aan te sluiten op de
  "self-check"-detectie van FrSky gestabiliseerde ontvangers op CH12.
- **Schakelaartype** — SA–SJ kunnen elk worden gedefinieerd als **None**,
  **Momentary**, **2 POS** of **3 POS**, waarmee u de functionaliteit tussen
  fysieke schakelaars kunt verwisselen (u kunt bijvoorbeeld de momentschakelaar
  SH de rol geven die normaal door de 2-positieschakelaar SF wordt vervuld) —
  afhankelijk van wat de bedrading van de zender daadwerkelijk ondersteunt
  (een 3-positierol kan doorgaans niet worden toegewezen aan hardware die
  daarvoor niet is bedraad).

  ![Schakelaaropties](../assets/system-hardware-switches-options.png)
  ![Extra schakelaars](../assets/system-hardware-switches-2.png)

- **Naam wijzigen** — schakelaars kunnen van SA–SJ worden omgenoemd naar
  eigen namen; de namen gelden globaal voor alle modellen.
- **X20 Pro** — voegt de drukknopschakelaars **K**/**L** op de achterzijde
  toe, plus de posities **M**/**N** indien bedraad (doorgaans voor
  schakelaars op de stickuiteinden).

## Toewijzing start-toetsen

Wijzigt waar de start-toetsen `SYS`, `MDL` en `DISP` (`TELE` op oudere
zenders) naartoe springen.

- **`DISP`** — zowel de korte als de lange druk kan worden toegewezen aan
  elke modelpagina, systeempagina, Schermen configureren, Start of de
  Vluchtgegevensregistratie. Voor consistentie met de X10-serie wordt een
  lange druk op `DISP` conventioneel ingesteld op Schermen configureren.
- **`SYS`/`MDL`** — alleen de lange druk is opnieuw toe te wijzen (aan
  dezelfde reeks bestemmingen); een korte druk opent altijd respectievelijk
  het systeem- of modelgedeelte.

## Zenderspecifieke hardware-opties {: #radio-specific-hardware-options }

- **Haptische gimbal-upgrades activeren** (X20 Pro, X20R) — de X20 Pro AW en
  X20RS worden geleverd met MC20R-gimbals met haptische stick-shaker-motoren;
  als er MC20R-gimbals zijn ingebouwd in een X20 Pro of X20R, activeert u ze
  hier (zie [Speciale functies](../model-setup/special-functions.md) voor het
  configureren van de haptische patronen zelf).

  ![Haptisch (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptisch (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Encoderoptie** (X20 Pro AW, X20R/RS) — deze zenders hebben een
  gevoeliger draai-encoder; activeer **halve stappen** om hem minder
  gevoelig te maken.

  ![Encoderoptie (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## ADC-waarden inspecteren {: #adc-value-inspector }

Toont de ruwe analoog-naar-digitaal-omzettingswaarden die de CPU voor elke
analoge ingang uitleest:

![ADC-controle (X20S)](../assets/system-hardware-adc-check-x20s.png)
![ADC-controle (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 linkerstick horizontaal, 2 linkerstick verticaal, 3 rechterstick
verticaal, 4 rechterstick horizontaal, 5 Pot 1, 6 Pot 2, 7 middelste
schuifregelaar, 8 linker schuifregelaar, 9 rechter schuifregelaar.

**X20 Pro**: als hierboven, maar met twee extra kanalen voor externe
potentiometers (7 Ext1, 8 Ext2 — bijvoorbeeld potentiometers op de sticks)
ingevoegd vóór de schuifregelaars, die daardoor opschuiven naar 9 middelste
schuifregelaar, 10 linker schuifregelaar, 11 rechter schuifregelaar.
