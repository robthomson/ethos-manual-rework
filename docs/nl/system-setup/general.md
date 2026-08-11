---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Algemeen

![Algemene instellingen](../assets/system-general.png)

Behandelt weergave-eigenschappen, audio, vario, haptische feedback en de bovenste werkbalk.

## Weergave-eigenschappen

- **Taal** — de taal van de displaymenu's (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português en andere).
- **Toetsenbord** — indeling van het virtuele toetsenbord: QWERTY, QWERTZ
  of AZERTY.
- **Helderheid** — een schuifregelaar voor de helderheid van de
  achtergrondverlichting; houd `ENT` lang ingedrukt om deze in plaats
  daarvan door een bron te laten regelen (bijv. een schuifregelaar, zoals
  in het onderstaande voorbeeld), of om deze op minimum/maximum te forceren.

  ![Menu Helderheid](../assets/system-general-brightness-menu.png)
  ![Schuifregelaar helderheid](../assets/system-general-brightness-slider.png)

  !!! note
      Als **Helderheid** gelijk is aan **Helderheid slaapstand**, blijft
      het touchscreen actief, zelfs tijdens de "slaapstand".

- **Wekken** — welke van deze acties de achtergrondverlichting uit de
  slaapstand halen (er kan meer dan één worden ingeschakeld): **Altijd aan**
  (nooit in slaapstand), **Sticks**, **Schakelaars**, **Gyro** (de zender
  kantelen). Toetsen wekken de zender altijd, ongeacht deze instellingen.
- **Slaap** — de inactiviteitstijd voordat de achtergrondverlichting
  uitgaat (grijs weergegeven als Wekken op Altijd aan staat).
- **Helderheid slaapstand** — helderheid van de achtergrondverlichting
  tijdens de slaapstand.
- **Donkere modus** — licht of donker weergavethema.
- **Accentkleur** — de accentkleur van de gebruikersinterface (standaard
  `#F8B038`).

## Audio-instellingen {: #audio-settings }

![Audio-instellingen](../assets/system-general-audio.png)

- **Audiotaal** — taal voor de spraakmeldingen.
- **Keuze van stemmen** — Ethos ondersteunt meerdere gelijktijdige
  stempakketten:

  - **Stem 1 (hoofd)** — wordt gebruikt voor alle ingebouwde
    systeemmeldingen. Voor Engels is de standaardkeuze tussen het
    Amerikaanse (`us`) en het Britse (`gb`) pakket, die worden gelezen uit
    `audio/en/us/system` en `audio/en/gb/system`. Eigen geluidsbestanden
    voor de [speciale functie Play
    Audio](../model-setup/special-functions.md) komen respectievelijk in
    `audio/en/us/` of `audio/en/gb/`.
  - **Stem 2 / Stem 3** — aanvullende pakketten, bijvoorbeeld een eigen
    TTS-stem. Elk pakket heeft dezelfde mapstructuur nodig als Stem 1 —
    een stem met de naam "Susan" heeft bijvoorbeeld `audio/en/Susan/` nodig
    voor eigen geluiden en `audio/en/Susan/system` voor de systeemgeluiden
    (elke stem heeft een map `/system` nodig, want daaruit lezen **Play
    Value** en de timermeldingen; bij elke audiorelease wordt een
    `.csv`-lijst van de standaard systeemgeluidsbestanden meegeleverd).
    Na installatie kan een stem per timer en per Play Audio-functie worden
    toegewezen — of zelfs als Stem 1 worden ingesteld om de
    systeemmeldingen volledig te vervangen.
  - **Stem "default"** — wordt automatisch geïnstalleerd als veilige
    terugvaloptie (en gebruikt om conversieproblemen bij installaties
    vanuit 1.4.x te voorkomen): als Stem 1 tijdens een
    installatie/upgrade nog niet is ingesteld, wordt deze op `default`
    gezet en gelezen uit `audio/en/default/system`. Veelgevraagde eigen
    geluidsbestanden voor Play Audio staan in `audio/en/default/`.

- **Hoofdvolume** — een schuifregelaar voor het algemene audiovolume (houd
  `ENT` lang ingedrukt om deze door een potentiometer te laten regelen);
  tijdens het aanpassen klinken pieptonen zodat u het niveau op het gehoor
  kunt beoordelen.
- **Audiomodus**:
  - **Stil** — geen audio (activeert bij het opstarten nog steeds de
    [waarschuwing voor de stille modus](alerts.md), indien ingeschakeld).
  - **Alleen alarmen** — alleen alarmen zijn hoorbaar.
  - **Standaard** — normale geluiden.
  - **Vaak** — voegt foutpieptonen toe wanneer een waarde voorbij het
    minimum/maximum wordt geduwd.
  - **Altijd** — voegt bovenop Vaak ook pieptonen toe voor gewone
    menunavigatie.
  - **Bluetooth** (alleen X20S/HD/Pro/R/RS) — geeft de audio door aan een
    gekoppeld Bluetooth-apparaat (headset, enz.). Kies **Apparaten
    zoeken**, zet het doelapparaat in de koppelmodus en selecteer het
    zodra het is gevonden:

    ![Bluetooth koppelen](../assets/system-general-audio-bluetooth.png)
    ![Bluetooth zoeken](../assets/system-general-audio-bluetooth-searching.png)
    ![Bluetooth-apparaat geselecteerd](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Bluetooth verbinden](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth verbonden](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Luidspreker dempen** regelt vervolgens de ingebouwde luidspreker —
    altijd aan, alleen wanneer telemetrie actief is, of geregeld door een
    bron (bijv. een schakelaar). De zender onthoudt het gekoppelde
    apparaat; zet voor een normale werking de zender aan vóór het
    Bluetooth-apparaat en geef na het verbinden enkele seconden de tijd
    voordat het dempen van de luidspreker weer actief wordt.

## Vario {: #vario }

![Vario-audio](../assets/system-general-audio-vario.png)

- **Volume** — relatief volume van de variotoon.
- **Toonhoogte nul** — toonhoogte bij een stijgsnelheid van nul.
- **Toonhoogte max** — toonhoogte bij de maximale stijgsnelheid.
- **Herhalen** — vertraging tussen de pieptonen bij toonhoogte nul.

Zie ook de VSpeed-sensor onder [Telemetrie](../model-setup/telemetry.md) en
de [speciale functie Play Vario](../model-setup/special-functions.md) voor
verder variogedrag.

## Haptische feedback

- **Sterkte** — een schuifregelaar voor de trilintensiteit.
- **Modus** — dezelfde opties als bij Audiomodus hierboven.

## Opslaglocatie (X18 en X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Deze zenders hebben een interne eMMC van 8 GB. Ethos gebruikt deze
standaard, waardoor een SD card optioneel is — maar u kunt kiezen tussen de
eMMC, een SD card of een combinatie van beide. Als u het systeem en de
modellen naar een SD card verplaatst, kopieer dan de betreffende
mappen/bestanden (inclusief audio en bitmaps) **voordat** u de
opslaglocatie wijzigt.

![Opslaglocatie](../assets/system-general-storage.png)

## Bovenste werkbalk

![Instellingen bovenste werkbalk](../assets/system-general-topbar.png)

- **Digitale spanning** — toont de accuspanning van de zender als getal in
  plaats van als balk in de bovenste werkbalk.
- **Digitale RSSI** — hetzelfde, voor de RSSI van 2,4 GHz en 900 MHz.
- **Model selecteren bij opstarten** — toont bij het opstarten het
  modelkeuzescherm, vóórdat de checklistmeldingen van het vorige model
  verschijnen, zodat u van model kunt wisselen zonder deze eerst te
  bevestigen. Het laatst gebruikte model is standaard gemarkeerd.

  ![Model selecteren bij opstarten](../assets/system-general-model-start.png)

## Voorselectie USB-modus

![USB-modus](../assets/system-general-usb.png)

Wat er automatisch gebeurt wanneer de zender via USB op een pc wordt
aangesloten:

- **Niet ingesteld** — vraagt bij het verbinden om een keuze.
- **Joystick** — schakelt onmiddellijk over naar de joystickmodus voor een
  RC-simulator.
- **Ethos Suite** — schakelt onmiddellijk over naar de Ethos-modus voor
  [Ethos Suite](../ethos-suite/index.md).
- **Serieel** — schakelt onmiddellijk over naar de seriële modus, waarbij
  Lua-debugtraces via USB-Serial op 115200 bps worden doorgegeven (mogelijk
  is een virtuele COM-poortdriver voor Windows nodig).
