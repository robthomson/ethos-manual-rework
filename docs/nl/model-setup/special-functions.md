---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Speciale functies

![Menu Speciale functies](../assets/model-sf-menu.png)

Speciale functies activeren een actie — audio weergeven, een schermafbeelding
maken, logs schrijven, haptische feedback en meer — zodra een voorwaarde waar
wordt. Er worden maximaal 100 ondersteund; standaard bestaat er geen enkele.
Voeg er een toe met **+**; tik op een bestaande voor **Wijzigen**/**Verplaatsen**/
**Kopiëren-plakken**/**Klonen**/**Verwijderen**.

![Speciale functie toevoegen](../assets/model-sf-add.png)
![Verplaatsen](../assets/model-sf-move.png)

## Velden die voor elke actie gelden

- **Status** — schakel deze functie in of uit zonder haar te verwijderen.
- **Actieve voorwaarde** — **Altijd aan**, of afhankelijk van standen van
  schakelaars/functieschakelaars/logische schakelaars/trims of van
  vluchtmodi. Houd `ENT` lang ingedrukt op een schakelaar en vink
  **Negatief** aan om deze te inverteren (bijv. `SG-up` wordt `!SG-up`,
  actief zodra SG *niet* omhoog staat).
- **Globaal** — voegt deze functie toe aan **elk** model, bestaand en
  toekomstig. Heeft een model al een identiek geconfigureerde lokale
  functie, dan voegt Globaal deze als extra vermelding toe; wanneer je
  Globaal weer uitschakelt, wordt de functie uit elk model verwijderd
  behalve uit het momenteel geselecteerde. Globale functies staan in
  `radio.bin`; lokale in het modelbestand.

## Acties {: #actions }

**Reset** — reset **Vluchtgegevens** (telemetrie + timers), **Alle timers**
of **Volledige telemetrie**.

![Reset](../assets/model-sf-reset.png)

**Schermafbeelding** — slaat een schermafbeelding op in `screenshots/` op de
SD card/eMMC.

![Schermafbeelding](../assets/model-sf-screenshot.png)

**Failsafe instellen** — legt de huidige kanaalstanden vast als failsafe, via
de interne of externe RF-**Module**.

![Failsafe instellen](../assets/model-sf-set-failsafe.png)

**Audio afspelen** — de meest uitgebreide actie, die een volledige reeks
ondersteunt:

![Audio afspelen](../assets/model-sf-play-audio.png)

- **Stem** — welke van de maximaal 3 geconfigureerde stemmen wordt gebruikt
  (zie [Algemeen](../system-setup/general.md#audio-settings)).
- **Herhalen** — eenmalig afspelen, of herhalen met een instelbaar interval
  (tot 10 minuten).
- **Overslaan bij opstarten** — voorkomt dat deze functie tijdens het
  opstarten wordt geactiveerd.
- **Reeks** — maximaal 100 stappen, elk van het type:

  - **Bestand afspelen** — speelt een gekozen audiobestand af.

    ![Bestand afspelen](../assets/model-sf-play-audio-add-play-file.png)

  - **Waarde afspelen** — spreekt de waarde van een bron uit: analoge
    bedieningen, schakelaars, logische schakelaars, trims, kanalen, gyro,
    systeemklok, trainer, timers of telemetrie.

    ![Waarde afspelen](../assets/model-sf-play-audio-add-play-value.png)

  - **Wachttijd** — een vaste pauze, tot 10 minuten.
  - **Wachtvoorwaarde** — pauzeert de reeks totdat een voorwaarde is voldaan.

  ![Reeksregel toevoegen](../assets/model-sf-play-audio-add-line.png)
  ![Type reeksregel](../assets/model-sf-play-audio-add-line-type.png)

  Bijvoorbeeld: speel `vfrlow.wav` af wanneer de logische schakelaar
  `VFRlow` actief wordt, en spreek daarna de opgeslagen minimale
  VFR-waarde uit —

  ![Waarde afspelen na bestand](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — of pauzeer een reeks totdat schakelaar SH omlaag gaat voordat er wordt
  vervolgd:

  ![Reeks met wachtvoorwaarde](../assets/model-sf-play-audio-add-sequence.png)

  Tik op een willekeurige reeksregel om deze te wijzigen, toe te voegen, te
  herordenen of te verwijderen:

  ![Beheer van de reeks](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptisch** — trillingsfeedback:

![Haptisch](../assets/model-sf-haptic.png)

- **Patroon** — enkel, dubbel, drievoudig, vijfvoudig of zeer kort.

  ![Haptisch patroon](../assets/model-sf-haptic-pattern.png)

- **Sterkte** — 1–10 (standaard 5).
- **Herhalen** — eenmalig, of met een ingesteld interval.
- **Haptische motoren selecteren** — op zenders met haptische motoren in de
  gimbals (X20 Pro AW, X20RS, of een X20 Pro/X20R die is uitgebreid met
  MC20R-gimbals — zie
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Standaard** (interne haptiek), **Alle motoren**, **Linkerstick** of
  **Rechterstick**.

  ![Haptisch op de X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Logs schrijven** — schrijft `.csv`-logs naar `Logs/` op de SD card/eMMC,
met tijdstempel van de RTC (essentieel om vliegsessies achteraf van elkaar te
kunnen onderscheiden):

![Logs schrijven](../assets/model-sf-write-logs.png)

- **Schrijfinterval** — 100–500 ms.
- **Sticks/Potentiometers/Schuifregelaars**, **Schakelaars**, **Logische
  schakelaars**, **Kanalen** — onafhankelijk in- en uitschakelbare
  logcategorieën.

  **Logs bekijken**: open een logbestand uit `/Logs` in de bestandsbeheerder.
  Kies welke kanalen worden weergegeven (RSSI is standaard geselecteerd);
  verschuif met de draaiknop of een veegbeweging, en zoom door de draaiknop te
  draaien terwijl je `PAGE` ingedrukt houdt. `DISP` verplaatst de focus naar de
  eerste knop in de rechterkolom.

**Tekst voorlezen** (alleen X20 Pro) — tekst-naar-spraak op het toestel zelf in
plaats van een vooraf opgenomen bestand:

![Tekst voorlezen](../assets/model-sf-x20pro-play-text.png)

- **Tekst** — de uit te spreken tekenreeks. VOLLEDIG HOOFDLETTERS wordt
  letter voor letter gespeld (bijv. "OFF" → "O-F-F"); kleine letters worden als
  woord uitgesproken ("off").
- **Herhalen**, **Overslaan bij opstarten** — zoals hierboven.

**Ga naar scherm** — schakelt het display naar een gekozen scherm, bijv.
rechtstreeks naar de vluchtgegevensregistratie van een ontvanger wanneer op een
knop wordt gedrukt:

![Ga naar scherm](../assets/model-sf-go-to-screen.png)
![Schermopties](../assets/model-sf-go-to-screen-options.png)

**Touchscreen vergrendelen** — vergrendelt het touchscreen tegen onbedoelde
invoer (ook direct te bereiken door `ENT` + `PAGE` 1 s samen ingedrukt te
houden vanaf het startscherm):

![Touchscreen vergrendelen](../assets/model-sf-lock-touchscreen.png)

**Model laden** — laadt een opgegeven **Model** wanneer de functie wordt
geactiveerd, met een optionele **Bevestiging** voordat er daadwerkelijk wordt
gewisseld:

![Model laden](../assets/model-sf-load-model.png)

**Vario afspelen** — stuurt de vario-audio aan vanaf een gekozen bron
(normaliter de VSpeed-sensor van een FrSky-vario, maar elke sensor met de
eenheid m/s werkt):

![Vario afspelen](../assets/model-sf-play-vario.png)
![Variobron: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Bereik** — de klim-/daalsnelheid die op de toonhoogte wordt afgebeeld,
  standaard ±10 m/s (tot ±100 m/s). Boven **Midden** stijgt de toonhoogte
  lineair met de klimsnelheid tot de maximale Bereik-waarde (de toonhoogte bij
  maximale snelheid wordt ingesteld in [Algemeen →
  Vario](../system-setup/general.md#vario)); bij dalen klinkt een continue toon
  die in toonhoogte zakt naar de minimale Bereik-waarde.
- **Midden** — de band voor "nul klimsnelheid", standaard ±0,3 m/s (tot
  ±2 m/s); binnen deze band is de toonhoogte constant (de toonhoogte bij
  snelheid nul wordt eveneens ingesteld in Algemeen → Vario). Zet **Beep** op
  **Stil** om de toon volledig te dempen.

  ![Opties voor variobereik/midden](../assets/model-sf-play-vario-options.png)
