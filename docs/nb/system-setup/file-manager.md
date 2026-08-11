---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Filbehandler

![Filbehandler – sender](../assets/system-filemanager-radio.png)

Filbehandleren lar deg utforske senderens lagringsområder og flashe firmware til
den interne RF-modulen, enheter tilkoblet via S.Port, OTA-enheter (Over-The-Air)
og eksterne moduler.

## Lagringsstruktur

Trykk på **Flash** (eller trykk `PAGE` for å bytte disk) for å utforske senderens
interne virtuelle USB-flashdisk, som brukes til systembitmaps og fonter:

![Flash-lagring](../assets/system-filemanager-flash.png)

- `bitmaps/system` — bitmaps som brukes til skjermvisninger og ikoner
- `fonts/` — fonter for de ulike språkvalgene

Både bootloaderen og selve systemfirmwaren ligger i dette interne
flashminnet, på alle FrSky-sendere helt tilbake til den opprinnelige X9D.

**X20/X20S/X20HD**-serien bruker et FAT32-formatert SD card på 32 GB eller
mindre (et SanDisk Ultra Micro SDHC Class 10 16 GB-kort er et godt valg).
**X18** og **X20 Pro/R/RS** bruker en intern eMMC som standard (et
eksternt SD card kan legges til i tillegg) — trykk på **Radio** for å utforske det.
Ethos oppretter `Logs/`, `models/` og `screenshots/` automatisk dersom de
mangler; `Firmware/` er en manuell konvensjon for firmwarefiler til enheter
som for eksempel mottakere.

## Mapper på toppnivå {: #top-level-folders }

- **`audio/`** — bruker- og systemlydfiler, delt inn etter stemme
  (`audio/en/gb`, `audio/en/us`, `audio/en/default`). Brukerfiler spilles av
  med [spesialfunksjonen Play Audio](../model-setup/special-functions.md);
  systemfiler inkluderer `hello.wav` (velkomsthilsenen «Welcome to Ethos» — en
  `bye.wav` kan legges til, men følger ikke med). Format: 16 kHz eller 32 kHz PCM,
  lineær 16-bit, eller A-law (EU)/µ-law (US) 8-bit; filnavn på opptil 31
  tegn pluss filendelse. Alle tre stemmemappene holdes synkronisert av
  Ethos Suite uavhengig av hvilken som faktisk er valgt.

  ![Audio-mappen](../assets/system-filemanager-audio.png)

- **`bitmaps/`** — `bitmaps/models/` inneholder brukerens modellbilder (angis i
  [Model Edit](../model-setup/model-edit.md) eller i veiviserne for nye modeller);
  `bitmaps/user/` inneholder alt annet. Anbefalt format: 32-bit BMP,
  8 bit per farge, med alfakanal, 300×280 px — dette holder senderens
  interne dekoding lett. Ethos skalerer BMP-filer fortløpende, men ikke
  PNG/JPEG. Filnavn kan bare inneholde `A-Z a-z 0-9 ()!-_@#;[]+=` og mellomrom,
  og må være 11 tegn eller kortere (pluss en filendelse på 4 tegn) for å
  vises i modellbildevelgeren — lengre navn vises fortsatt i
  Filbehandler, men kan ikke velges der. Verktøyene for bildekonvertering i
  Ethos Suite håndterer formatkonverteringen for deg.

  ![Bitmaps-mappen](../assets/system-filemanager-bitmaps.png)

- **`documents/user/`** — brukerens tekstdokumenter, som hentes fram fra
  widgeten **Text** på skjermene.

- **`Firmware/`** — firmwarefiler for den interne RF-modulen, eksterne
  moduler og andre enheter (mottakere osv.), som flashes herfra via
  S.Port eller OTA. Kopier ny firmware hit mens senderen er i
  [bootloader-modus](../getting-started/usb-connection-modes.md) og tilkoblet via USB;
  når du trykker på en firmwarefil og velger **Flash**, starter oppdateringen:

  ![Flash intern RF-modul](../assets/system-filemanager-flash.png)
  ![Flash S8R-mottaker via S.Port](../assets/system-filemanager-flash-S8R.png)
  ![Flash TD-R18-mottaker via OTA](../assets/system-filemanager-flash-TD-ISRM.png)
  ![Flash bootloaderen](../assets/system-filemanager-flash-bootloader.png)

- **`I18n/`** — filer for språkoversettelser.

- **`Logs/`** — datalogger.

- **`models/`** — selve modellfilene. Disse kan ikke redigeres
  direkte her, bare sikkerhetskopieres eller deles. Fra Ethos v1.2.11 får en modell
  navn etter modellnavnet i stedet for `model01.bin` og videre (f.eks. blir en modell
  som heter «Extra» til `Extra.bin`; en andre «Extra» blir
  `Extra01.bin`). Når du gir en modell nytt navn i [Model Edit](../model-setup/model-edit.md),
  endres også filnavnet — alltid med små bokstaver (visningsnavnet med store og små
  bokstaver lagres inne i filen), og ikke alle tegn i et modellnavn
  overføres til filnavnet. Fra v1.1.0 Alpha 17 får hver brukeropprettede
  modellkategori sin egen undermappe.

- **`screenshots/`** — resultatet av [spesialfunksjonen
  Screenshot](../model-setup/special-functions.md).

- **`scripts/`** — Lua-skript, eventuelt organisert i egne
  undermapper med støttefiler. Skripttypene er **widgets** (se
  [Skjermer](../displays/index.md)), **tasks og sources** (egendefinerte
  sensorer eller handlinger etter flyging — når de er installert her, vises de under
  modellens [Lua](../model-setup/lua-scripts.md)-meny) og **tools** (f.eks.
  konfigurasjonsverktøyene for stabiliserte mottakere under SYS-menyene).
  Eksterne moduler fra tredjeparter får hver sitt eget skript og sin egen mappe,
  f.eks. `scripts/multi`, `scripts/elrs`, `scripts/ghost`,
  `scripts/crossfire`.

  !!! warning
      Lua-skript øker senderens oppstartstid. Forsinkelsen fra et godt skrevet
      skript er umerkelig — et dårlig skrevet skript kan forsinke oppstarten
      nærmest i det uendelige.

- **`radio.bin`** (rotmappen) — filen med systeminnstillinger, som skrives av
  senderen selv ved initialisering. Ta sikkerhetskopi av den sammen med `models/`
  før en firmwareoppdatering, slik at du kan gå tilbake til en tidligere versjon om nødvendig.

- **`firmware.bin`** (rotmappen) — legg en ny firmwarefil for senderen hit
  for at den skal flashes automatisk neste gang senderen
  kobles fra PC-en. Innholdet på SD card/eMMC og på den interne flashdisken
  må kanskje oppdateres i samme omgang.

- **`sdcard.version`** (rotmappen) — versjonen av SD card-innholdet, som
  vedlikeholdes av Ethos Suite.

## Dele filer via Bluetooth

Ethos kan overføre filer fra sender til sender via Bluetooth. På den
**mottakende** senderen navigerer du til målmappen i Filbehandler,
holder inne `ENT` og velger **Receive file here**:

![Bluetooth-mottak](../assets/system-filemanager-bluetooth-receive.png)

På den **sendende** senderen trykker du på filen, velger **Send file** og følger
instruksjonene på begge sendere:

![Bluetooth-sending](../assets/system-filemanager-bluetooth-send.png)

Hvis en av senderne allerede har en aktiv Bluetooth-tilkobling (telemetri,
trenerforbindelse eller — på X20S/Pro — lyd), blir du spurt om denne enheten
skal kobles fra først.
