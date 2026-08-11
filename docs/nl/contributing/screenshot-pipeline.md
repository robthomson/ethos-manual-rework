---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Screenshot-pijplijn

Elke screenshot in deze handleiding (momenteel ongeveer 590 stuks, onder
`docs/en/assets/`) is vastgelegd door de echte Ethos-simulator te scripten, niet
handmatig. De opzet staat in de oude
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual)-repository, onder
`english/manual/`, en is **nog niet overgezet naar deze repository** — deze
pagina documenteert hoe het werkt, zodat dat kan gebeuren en zodat screenshots
in de tussentijd opnieuw gegenereerd of uitgebreid kunnen worden zonder helemaal
opnieuw te beginnen.

## Hoe het is opgebouwd

Voor elk menu/elke sectie van de handleiding bestaat er een paar bestanden:

- `manual/macros/<name>.lua` — een script geschreven tegen de Lua-API van de
  simulator (hieronder) dat naar een specifiek scherm navigeert en op elk punt
  dat het vastleggen waard is `simulator.screenshot(path)` aanroept.
- `manual/<name>.sh` — een wrapper van één regel die het simulatorprogramma
  voor een specifieke zender start, gericht op die macro, bijvoorbeeld:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` voert elke macro achtereenvolgens uit om de volledige
set opnieuw te genereren. Er bestaan afzonderlijke `.sh`-bestanden per sectie,
zodat de screenshots van één pagina opnieuw gegenereerd kunnen worden zonder
alles opnieuw uit te voeren (elke macro duurt van enkele seconden tot ruim een
minuut).

Belangrijke CLI-opties:

- `--read-only` — bewaar geen wijzigingen die tijdens de run zijn gemaakt.
- `--no-gui` / `--no-audio` — min of meer headless; sommige macro's hebben de
  GUI toch nodig, omdat de simulator er zonder "overslaat" (zie de opmerking in
  `screenshots.sh`).
- `--radio-settings <file>.bin` — met welke opgeslagen zenderinstellingen moet
  worden opgestart (dit maakt de screenshots taal- en zenderspecifiek — een
  Duitse run gebruikt een Duitse `.bin`).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — verwijs de simulator naar de modellen/firmware/documenten/audio
  die hij moet zien, zodat screenshots bewust voorbereide inhoud weergeven in
  plaats van wat er toevallig op een echte SD card staat.
- `--exec <script>.lua` — de macro die na het opstarten moet worden uitgevoerd.

Elke zenderfamilie (X20S, X20 PRO, X20 PRO AW, X18S) heeft zijn eigen
simulatorprogramma en heeft per taal een eigen `--radio-settings`-bestand nodig
(bijv. `x20s-en.bin`, `x20pro-en.bin`), omdat de gebruikersinterface tussen
zenders licht verschilt en het instellingenbestand ook de taal bevat.

## De macro-API

Macro's zijn gewoon Lua en besturen een globale `simulator`:

| Aanroep | Doel |
|---|---|
| `simulator.loadModel("name.bin")` | Laad een specifiek modelbestand voordat er genavigeerd wordt — elke sectie van de handleiding gebruikt een model dat is ingericht om die sectie te demonstreren (zie de modellijst hieronder). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Druk op een hardwaretoets — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE`, enz. Een vasthoudduur veroorzaakt een lange druk (opent contextmenu's). |
| `simulator.turnRotaryEncoder(n)` | Verplaats de encoder `n` klikken (negatief = omgekeerd) — de belangrijkste manier om de cursor tussen velden te verplaatsen. |
| `simulator.touch(x, y)` | Tik op een specifieke schermcoördinaat — gebruikt waar aanraking de enige manier is om iets te bereiken (bijv. het omschakelen van de toetsenbordindeling). |
| `simulator.setAnalog(channel, value)` | Stel direct een stick-/potentiometer-/schuifregelaarpositie in (`0`-`3` zijn de vier hoofdsticks, `ANALOG_LAST_SLIDER` de laatste schuifregelaar), zodat screenshots een bewuste, reproduceerbare waarde tonen in plaats van de standaardwaarde van de simulator. |
| `simulator.setSwitch(n, position)` | Stel de positie van een fysieke schakelaar in. |
| `simulator.setDateTime({...})` | Zet de klok van de simulator vast, zodat tijdstempels in screenshots (en alles wat tijdafhankelijk is) tussen runs reproduceerbaar zijn. |
| `simulator.screenshot(path)` | Leg het huidige scherm vast als PNG, relatief ten opzichte van de werkmap van de macro (vandaar de `../assets/...`-paden in elke macro). |
| `simulator.connectUsb()` | Simuleer het aansluiten via USB, om het USB-menu vast te leggen. |
| `simulator.sleep(seconds)` | Wacht tot een animatie- of telemetriewaarde is gestabiliseerd voordat er wordt vastgelegd. |

`manual/macros/common.lua` wordt vanuit de meeste macro's met `dofile`
ingeladen en zet alleen de datum/tijd vast, zodat elke macro vanaf hetzelfde
gesimuleerde moment start.

## Modellen per sectie

`manual/notes.txt` (informeel meegenomen, nog niet naar deze repository
gekopieerd) koppelt elke macro aan het `.bin`-modelbestand waarvan die afhangt
en waarom — bijvoorbeeld: `model-mixes.lua` gebruikt `rarebear.bin`,
`model-fm.lua` gebruikt `zblank.bin` (een model met een opzettelijk lege
vluchtmodus-instelling), `model-trims.lua` gebruikt `blaster.bin` (ingericht
met verschoven trims om het trimbereik te demonstreren). Het overzetten van de
aantekeningen uit dit bestand naar volwaardige documentatie hier maakt deel uit
van het fase-2-werk hieronder.

## Wat het overzetten naar de nieuwe repository inhoudt (nog niet gedaan)

- Beslissen of macro's direct vanuit deze repository opnieuw worden uitgevoerd
  (waarvoor een lokale installatie van de Ethos-simulator nodig is, zoals in de
  oude repository) of via CI met de simulator meegeleverd/gedownload in de
  workflow.
- Het herstructureren van de platte `../assets/...`-uitvoerpaden zodat ze
  overeenkomen met de asset-indeling per pagina en per locale van deze
  repository (`docs/<locale>/assets/`).
- Eén `--radio-settings ... .bin` en één screenshot-run per locale, zodra er een
  andere locale dan `en` bestaat — screenshots zijn specifiek voor de
  UI-taal en kunnen niet tussen locales worden gedeeld.
- Beslissen hoeveel van de circa 40 bestaande macro's ongewijzigd worden
  overgenomen en hoeveel wordt herschreven tegen de huidige navigatiestructuur
  in deze repository (sommige macro's produceren screenshots voor secties die
  niet langer één-op-één overeenkomen met de pagina-indeling van deze
  handleiding).
