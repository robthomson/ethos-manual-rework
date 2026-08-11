---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Gebruik

## Welkomstgedeelte

**Update News** — release notes en aanbevelingen voor back-ups voordat je
gaat updaten. Ethos 1.6.0+ vereist dat de interne RF-module en TD/TW/AP/AP
Plus ontvangers op v3.0.1+ staan om de verbeteringen te kunnen gebruiken.
Wanneer je **Pre-releases** inschakelt (met de server ingesteld op GitHub —
zie [Suite-instellingen](#suite-settings)), worden hier ook pre-release
builds vermeld, naast de volledige releasegeschiedenis.

**Ethos web page** — een ingebedde weergave van ethos.frsky-rc.com:
documentatie, links naar modeltemplates en de lijst met ondersteunde
zenders.

## Zendergedeelte

Beheert de aangesloten zender. Schakel deze in de
[bootloadermodus](../getting-started/usb-connection-modes.md#bootloader-mode)
in en verbind via USB — Suite toont het zendertype (bijv. "X20") zodra het
is gedetecteerd.

### Zenderinformatie

- **Ethos** — geïnstalleerde firmware-/bootloaderversies; **Manage Ethos**
  gaat direct naar het bijwerken ervan als ze verouderd zijn.
- **RF Module** — geïnstalleerde firmware van de interne RF-module;
  **Manage internal module** gaat direct naar het bijwerken ervan als deze
  verouderd is.
- **Model manager** / **Lua library** / **Download center** — snelkoppelingen
  naar die hulpmiddelen.

### Ethos bijwerken {: #updating-ethos }

Het tabblad **Ethos** toont de versies van Firmware, Bootloader, SD card/eMMC
(audiobestanden) en flashgeheugen (systeembitmaps) naast elkaar —
systeembestanden in flash worden nu samen met de firmware bijgewerkt en niet
langer afzonderlijk beheerd.

- **Write outdated components** — werkt alleen bij wat achterloopt.
- **Write all components** — werkt alles bij, ongeacht de versie.
- Afzonderlijke opties **Write firmware**, **Write bootloader** en **Write
  audio files**, die elk worden uitgevoerd door op de donkergrijze knop naast
  de gekozen optie te klikken.
- **Flash from a local file** — omzeilt de download en gebruikt een
  firmwarebestand dat al op schijf staat.

Bij het selecteren van een release kies je eerst een **branch**
(Stable/Testing) en daarna een versie. Bij het updaten wordt eerst om een
back-up gevraagd (**Go to backup page**) — maak die ook. Als de interne
RF-module niet op v3.0.1+ staat, vereist Ethos 1.6.0+ dat deze eerst wordt
bijgewerkt voordat je verder kunt (**Go to Module manager** flasht de module
automatisch, waarna de Ethos-update wordt voortgezet) — en bij TD/TW/AP/AP
Plus ontvangers moet daarna de telemetrie worden verwijderd en opnieuw
gedetecteerd om de bijgewerkte sensornamen over te nemen.

De voortgang van de update wordt stap voor stap weergegeven (overschakelen
naar bootloader, downloaden, kopiëren, ontkoppelen, schrijven, verversen,
"Update successful!") — het scherm van de zender zelf toont de
schrijfvoortgang eveneens.

!!! note "Pre-release-updates"
    De bestanden van een pre-release kunnen wijzigen zonder dat het
    versienummer verandert, wat Suite niet kan detecteren — flash een
    pre-release-versie die je al gebruikt altijd opnieuw zodra deze een
    volledige release wordt. Controleer bij twijfel de firmwaredatum bij
    [System → Info](../system-setup/information.md).

!!! note "Updaten vanaf Ethos 1.2.8 of eerder"
    Suite kan firmware/bootloader mogelijk niet volledig automatisch
    flashen vanaf zo'n oude versie — in dat geval verschijnt een dialoog
    die je door een handmatige flash begeleidt. Werp in beide gevallen de
    drives handmatig uit voordat je de USB-verbinding verbreekt.

Systeembitmapbestanden worden nu automatisch samen met de firmware
bijgewerkt (geen afzonderlijk beheer nodig); audiobestanden worden
bijgewerkt via **Write all components** of **Write audio files** (downloadt
het geselecteerde taalpakket, bijv. "English audio pack").

### RF Module Manager

Selecteer een versie (normaal de nieuwste) en **Flash module** om de
firmware van de interne RF-module direct bij te werken — na afloop volgt de
bevestiging "...has been flashed successfully". Dit wordt ook automatisch
gestart door het hierboven beschreven verplichte upgradetraject naar v3.0.1.

### Ethos-modus

**Switch to Ethos** start de zender opnieuw op uit de bootloadermodus naar
een draaiende Ethos (te zien aan een groen USB-pictogram op de zender, en
doordat "(Bootloader Mode)" uit de Suite-kopregel verdwijnt). Dit is nodig om
het **Download center** de zender als proxy te laten gebruiken voor het
flashen van modules, ontvangers, sensoren en servo's. De knop wordt daarna
**Switch to Bootloader** om dit terug te draaien. **Eject Drives** verbreekt
de verbinding met de zender op een veilige manier.

### Model Manager

Maakt een back-up van modelbestanden en instellingen naar schijf, of zet een
eerdere back-up terug.

!!! warning
    Terugzetten herstelt **niet** de firmware — flash na het terugzetten van
    modellen/instellingen afzonderlijk de firmwareversie die daadwerkelijk
    bij die back-up hoort (zie [Ethos bijwerken](#updating-ethos)), omdat
    modelbestanden niet achterwaarts compatibel zijn.

- **Backup Location** — kies een map (wordt per zendertype onthouden);
  datum/tijd van de laatste back-up wordt eronder weergegeven.
- **Backup** — slaat modelbestanden op en registreert daarbij de actuele
  Ethos-versie.
- **Restore** — selecteer welke onderdelen worden teruggezet: Audio
  (standaard uit), Scripts, Screenshots, System Bitmaps (standaard uit — wordt
  nu met de firmware beheerd), Models (inclusief eventuele tekstbestanden van
  een [gebruikersgedefinieerde
  checklist](../how-to/user-defined-checklist.md) die daarbij zijn
  opgeslagen), Language, User Bitmaps, Logs, System Settings.

### Lua library

Doorzoek en installeer met één klik Lua-scripts/tools uit de externe
bibliotheek van FrSky (of installeer vanuit een lokaal zipbestand);
geïnstalleerde scripts worden naast de externe catalogus weergegeven zodra
er scripts aanwezig zijn.

## Gedeelte Tools

- **Download center** — download willekeurige firmware van de FrSky-site en
  gebruik (terwijl de zender in Ethos-modus staat) de zender als proxy om
  een module, sensor, servo of ontvanger te flashen die via een
  S.Port-upgradeverbinding is aangesloten. Kies het product uit de lijst
  (bijv. een TW SR8 ontvanger), bekijk de beschikbare **assets**, gebruik
  **Download** om lokaal op te slaan of **Flash** om direct naar het
  aangesloten apparaat te schrijven — een voortgangsbalk volgt de flash en
  eindigt met "...has been flashed successfully!"

- **Image manager** — converteert afbeeldingen naar het eigen formaat van
  Ethos (32-bits BMP, RGB, alfakanaal wordt alleen toegevoegd indien nodig)
  in een gekozen formaat, met behoud van de beeldverhouding. Referentiematen:
  modelafbeeldingen 300×280 (X20) / 180×168 (X18); schermvullende
  afbeeldingen 800×480 (X20) / 480×320 (X18) — zie
  [Bestandsbeheer](../system-setup/file-manager.md#top-level-folders) voor de
  naamgevingsregels voor bitmaps. Je kunt ook direct door de mappen
  `bitmaps/gps`, `bitmaps/models` en `bitmaps/user` van de zender bladeren,
  met ondersteuning voor uploaden. Voeg afbeeldingen toe aan de
  transcodeerlijst met **+** (TIFF wordt niet ondersteund), kies een
  uitvoerpad (een lokale map; direct naar de zender onder model-, gebruikers-
  of GPS-afbeeldingen; of de momenteel geopende zendermap) en open eventueel
  automatisch de uitvoermap of forceer een alfakanaal.

- **Audio manager** — converteert audio naar het Ethos-formaat (PCM lineair,
  32 kHz, mono, 16-bits little-endian). Voeg bestanden toe met **+**, kies
  een lokale map of stuur ze rechtstreeks naar de map `audio` van de zender
  (verplaats ze daarna naar de juiste stemsubmap) en open eventueel
  automatisch de bestemming.

- **Lua development tools** — **Lua Docs** verwijst naar de Ethos
  Lua-referentiegids (zie ook de rcgroups-thread *FrSky - ETHOS Lua Script
  Programming*); **Lua Demo Scripts** verwijst naar voorbeeldscripts op de
  GitHub van Ethos-Feedback-Community; **Debug** opent een live logvenster
  voor Lua `print()`-uitvoer die via USB-Serial wordt verzonden terwijl de
  zender in de Serial-modus staat:

  1. Verbind de zender normaal met Suite en schakel over naar de
     Ethos-modus.
  2. Bewerk Lua-scripts rechtstreeks op de aangekoppelde drive van de
     zender, in een willekeurige code-editor.
  3. Open **Lua Development Tools** → **START DEBUG** — hiermee wordt de
     zender opnieuw opgestart in de Serial-/debugmodus en worden de scripts
     opnieuw geïnitialiseerd.
  4. De `print()`-uitvoer van elk actief script wordt naar de terminal van
     Suite gestreamd.
  5. **STOP DEBUG** schakelt terug naar de normale Ethos-modus om verder te
     bewerken.

- **DFU Flasher** — flasht de bootloader via een USB-verbinding met
  uitgeschakelde zender (DFU) en werkt zelfs bij volledig beschadigde
  firmware, omdat de onderliggende ST-bootloader in ROM staat. Gebruik
  **Select Bootloader** om een gedownload bestand te kiezen (Suite meldt de
  versie/geschiktheid ervan), sluit de **uitgeschakelde** zender aan en klik
  vervolgens op **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Meestal een ontbrekende/onjuiste DFU-driver. De meeste pc's met
      Windows 10+ werken met Tandem-systemen via de standaard USB
      DFU-driver, maar Windows Update vervangt deze soms door een
      generieke driver die niet werkt — controleer Apparaatbeheer en
      overweeg een hulpmiddel zoals Impulse Driver Fixer. Specifiek
      gebruikers van de Horus X10 moeten mogelijk de STM32
      bootloader-USB-driver handmatig installeren (met Impulse Driver Fixer
      of Zadig), omdat Windows 10 deze niet standaard installeert.

- **Repair Tool** — voor X18/S, TW Lite, XE en X20 Pro/R/RS: formatteert de
  interne opslag opnieuw wanneer de zender de NAND niet kan lezen of
  instellingen niet kan opslaan.

## Gedeelte Others

- **Documentation** — links naar de GitHub van Ethos-Feedback-Community, de
  officiële Ethos-handleidingen (te downloaden) en een FAQ over Ethos Suite.
- **Ethos Github** — releases en issue tracker (zoek in bestaande issues
  voordat je een nieuwe aanmaakt).

### Suite-instellingen {: #suite-settings }

- **Language** — Tsjechisch, Duits, Engels, Spaans, Frans, Hebreeuws,
  Italiaans, Nederlands, Noors, Portugees, Sloveens, Chinees.
- **Server location** — **FrSky server** of **GitHub** (nodig voor de
  hierboven genoemde toegang tot pre-releases).
- **Debug options** — schakel de pop-up bij fatale fouten in of uit; schakel
  volledige debuglogging van Suite in (niet alleen bij crashes); open de
  logmap.
- **Version** / **Update Suite** — huidige versie en een handmatige controle
  op updates.
- **About** — vermeldingen voor hergebruikte componenten.

## Gebruik via de commandoregel

Ethos Suite kan vanaf een terminal worden uitgevoerd:

| Vlag | Effect |
|---|---|
| `--help` | Toont de commandoregelhulp. |
| `--version` | Toont de geïnstalleerde Suite-versie. |
| `--list-radios` | Toont alle ondersteunde FrSky-zenders. |
| `--radio-components --radio {RADIO}` (of `--radio auto`) | Toont de componenten van een aangesloten zender en hun paden. `auto` detecteert automatisch; geef `{RADIO}` op als er meer dan één is aangesloten. |
| `--get-path {COMPONENT}` | Vraagt het pad van een component op — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` of `I18N`. |
| `--serial start` \| `--serial stop` | Schakelt de seriële debugmodus in/uit. |

!!! note
    Suite start helemaal niet op tenzij een geldig commando wordt herkend.
