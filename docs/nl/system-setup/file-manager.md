---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Bestandsbeheer

![Bestandsbeheer - zender](../assets/system-filemanager-radio.png)

Bestandsbeheer doorzoekt de opslag van de zender en flasht firmware naar de
interne RF-module, apparaten die via S.Port zijn aangesloten, OTA-apparaten
(Over-The-Air) en externe modules.

## Opslagindeling

Tik op **Flash** (of druk op `PAGE` om tussen schijven te wisselen) om het
interne virtuele USB-flashstation van de zender te doorzoeken, dat wordt gebruikt
voor systeembitmaps en lettertypen:

![Flash-opslag](../assets/system-filemanager-flash.png)

- `bitmaps/system` — de bitmaps die worden gebruikt voor schermweergaven en pictogrammen
- `fonts/` — lettertypen voor de verschillende taalkeuzes

Zowel de bootloader als de systeemfirmware zelf staan in dit interne
flashgeheugen, op elke FrSky-zender terug tot de oorspronkelijke X9D.

De **X20/X20S/X20HD**-serie gebruikt een FAT32-geformatteerde SD card van 32GB of
kleiner (een SanDisk Ultra Micro SDHC Class 10 16GB-kaart is een goede keuze).
De **X18** en **X20 Pro/R/RS** gebruiken standaard een interne eMMC (daarnaast kan
een externe SD card worden toegevoegd) — tik op **Radio** om die te doorzoeken.
Ethos maakt `Logs/`, `models/` en `screenshots/` automatisch aan als ze
ontbreken; `Firmware/` is een handmatige conventie voor firmwarebestanden van
apparaten zoals ontvangers.

## Mappen op het hoogste niveau {: #top-level-folders }

- **`audio/`** — gebruikers- en systeemgeluidsbestanden, gesplitst per stem
  (`audio/en/gb`, `audio/en/us`, `audio/en/default`). Gebruikersbestanden worden
  afgespeeld door de [speciale functie Play Audio](../model-setup/special-functions.md);
  systeembestanden omvatten `hello.wav` (de begroeting "Welcome to Ethos" — een
  `bye.wav` kan worden toegevoegd maar wordt niet meegeleverd). Formaat: 16kHz of
  32kHz PCM, lineair 16-bit, of A-law (EU)/µ-law (US) 8-bit; bestandsnamen tot 31
  tekens plus extensie. Alle drie de stemmappen worden door Ethos Suite
  gesynchroniseerd gehouden, ongeacht welke daadwerkelijk is geselecteerd.

  ![Audio-map](../assets/system-filemanager-audio.png)

- **`bitmaps/`** — `bitmaps/models/` bevat de modelafbeeldingen van de gebruiker
  (ingesteld in [Model Edit](../model-setup/model-edit.md) of in de wizards voor
  nieuwe modellen); `bitmaps/user/` bevat al het overige. Aanbevolen formaat:
  32-bit BMP, 8 bits per kleur, met alfakanaal, 300×280px — dit houdt het
  decoderen aan boord van de zender goedkoop. Ethos schaalt BMP's direct, maar
  geen PNG/JPEG. Bestandsnamen mogen alleen `A-Z a-z 0-9 ()!-_@#;[]+=` en spaties
  gebruiken, en moeten 11 tekens of minder lang zijn (plus een extensie van 4
  tekens) om in de modelafbeeldingkiezer te verschijnen — langere namen zijn nog
  wel te zien in Bestandsbeheer, maar kunnen daar niet worden geselecteerd. De
  hulpmiddelen voor afbeeldingsconversie van Ethos Suite verzorgen de
  formaatconversie voor u.

  ![Bitmaps-map](../assets/system-filemanager-bitmaps.png)

- **`documents/user/`** — tekstdocumenten van de gebruiker, opgeroepen vanuit de
  **Text**-displaywidget.

- **`Firmware/`** — firmwarebestanden voor de interne RF-module, externe modules
  en andere apparaten (ontvangers enz.), die hiervandaan via S.Port of OTA worden
  geflasht. Kopieer nieuwe firmware hierheen terwijl de zender in
  [bootloader-modus](../getting-started/usb-connection-modes.md) staat en via USB
  is verbonden; op een firmwarebestand tikken en **Flash** kiezen start de update:

  ![Interne RF-module flashen](../assets/system-filemanager-flash.png)
  ![S8R-ontvanger flashen via S.Port](../assets/system-filemanager-flash-S8R.png)
  ![TD-R18-ontvanger OTA flashen](../assets/system-filemanager-flash-TD-ISRM.png)
  ![De bootloader flashen](../assets/system-filemanager-flash-bootloader.png)

- **`I18n/`** — bestanden met taalvertalingen.

- **`Logs/`** — datalogs.

- **`models/`** — de modelbestanden zelf. Deze kunnen hier niet direct worden
  bewerkt, alleen geback-upt of gedeeld. Sinds Ethos v1.2.11 wordt een model
  vernoemd naar zijn modelnaam in plaats van `model01.bin` en verder (een model
  met de naam "Extra" wordt bijvoorbeeld `Extra.bin`; een tweede "Extra" wordt
  `Extra01.bin`). Een model hernoemen in [Model Edit](../model-setup/model-edit.md)
  hernoemt ook het bestand — altijd in kleine letters (de weergavenaam met
  hoofd- en kleine letters wordt in het bestand opgeslagen), en niet elk teken uit
  een modelnaam blijft in de bestandsnaam bewaard. Sinds v1.1.0 Alpha 17 krijgt
  elke door de gebruiker aangemaakte modelcategorie zijn eigen submap.

- **`screenshots/`** — de uitvoer van de [speciale functie
  Screenshot](../model-setup/special-functions.md).

- **`scripts/`** — Lua-scripts, eventueel georganiseerd in eigen submappen met
  ondersteunende bestanden. Scripttypen zijn **widgets** (zie
  [Displays](../displays/index.md)), **tasks en sources** (aangepaste sensoren of
  acties na de vlucht — hier geïnstalleerd verschijnen ze onder het
  [Lua](../model-setup/lua-scripts.md)-menu van het model) en **tools** (bijv. de
  configuratiehulpmiddelen voor gestabiliseerde ontvangers onder de
  Systeemmenu's). Externe modules van derden krijgen elk hun eigen script en map,
  bijv. `scripts/multi`, `scripts/elrs`, `scripts/ghost`,
  `scripts/crossfire`.

  !!! warning
      Lua-scripts verlengen de opstarttijd van de zender. De vertraging van een
      goed geschreven script is niet merkbaar — een slecht geschreven script kan
      het opstarten nagenoeg onbeperkt vertragen.

- **`radio.bin`** (hoofdmap) — het bestand met systeeminstellingen, dat door de
  zender zelf tijdens de initialisatie wordt geschreven. Maak hiervan samen met
  `models/` een back-up vóór een firmware-update, zodat u indien nodig kunt
  terugkeren naar een oudere versie.

- **`firmware.bin`** (hoofdmap) — plaats hier een nieuw firmwarebestand voor de
  zender om het automatisch te laten flashen zodra de zender de volgende keer van
  de pc wordt losgekoppeld. Mogelijk moet de inhoud van de SD card/eMMC en van
  het interne flashstation in dezelfde ronde worden bijgewerkt.

- **`sdcard.version`** (hoofdmap) — de versie van de SD card-inhoud, bijgehouden
  door Ethos Suite.

## Bestanden delen via Bluetooth

Ethos kan bestanden van zender naar zender overdragen via Bluetooth. Navigeer op
de **ontvangende** zender in Bestandsbeheer naar de doelmap, houd `ENT` lang
ingedrukt en kies **Receive file here**:

![Bluetooth ontvangen](../assets/system-filemanager-bluetooth-receive.png)

Tik op de **verzendende** zender op het bestand, kies **Send file** en volg de
aanwijzingen op beide zenders:

![Bluetooth verzenden](../assets/system-filemanager-bluetooth-send.png)

Als een van beide zenders al een actieve Bluetooth-verbinding heeft (telemetrie,
trainerverbinding of — op de X20S/Pro — audio), wordt gevraagd of dat apparaat
eerst moet worden losgekoppeld.
