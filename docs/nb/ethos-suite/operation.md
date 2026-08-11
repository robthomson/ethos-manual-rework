---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Bruk

## Velkomstseksjonen

**Update News** — utgivelsesnotater og anbefalinger om sikkerhetskopiering
før oppdatering. Ethos 1.6.0+ krever at den interne RF-modulen og
TD/TW/AP/AP Plus-mottakere kjører v3.0.1+ for å kunne bruke
forbedringene. Hvis du aktiverer **Pre-releases** (med serveren satt til
GitHub — se [Innstillinger for Suite](#suite-settings)), listes også
forhåndsversjoner opp her, sammen med den fullstendige
utgivelseshistorikken.

**Ethos web page** — en innebygd visning av ethos.frsky-rc.com: ressurser,
lenker til modellmaler og listen over støttede sendere.

## Senderseksjonen

Håndterer den tilkoblede senderen. Slå den på i
[bootloader-modus](../getting-started/usb-connection-modes.md#bootloader-mode)
og koble til via USB — Suite viser sendertypen (f.eks. «X20») så snart den
er oppdaget.

### Informasjon om senderen

- **Ethos** — installerte versjoner av fastvare/bootloader; **Manage
  Ethos** tar deg til oppdatering av dem hvis de er utdaterte.
- **RF Module** — installert fastvare for den interne RF-modulen; **Manage
  internal module** tar deg til oppdatering av den hvis den er utdatert.
- **Model manager** / **Lua library** / **Download center** — snarveier
  til disse verktøyene.

### Oppdatere Ethos {: #updating-ethos }

Fanen **Ethos** viser versjonene for fastvare, bootloader, SD card/eMMC
(lydfiler) og flash-minne (systembitmaps) side om side — systemfiler i
flash oppdateres nå sammen med fastvaren og håndteres ikke lenger separat.

- **Write outdated components** — oppdaterer bare det som er utdatert.
- **Write all components** — oppdaterer alt uavhengig av versjon.
- Enkeltvalgene **Write firmware**, **Write bootloader** og **Write audio
  files**, som hver startes ved å klikke på den mørkegrå knappen ved siden
  av det valgte alternativet.
- **Flash from a local file** — hopper over nedlastingen og bruker en
  fastvarefil som allerede ligger på disken.

Å velge en utgivelse innebærer først å velge en **branch**
(Stable/Testing) og deretter en versjon. Ved oppdatering blir du først bedt
om å ta en sikkerhetskopi (**Go to backup page**) — ta den. Hvis den
interne RF-modulen ikke kjører v3.0.1+, krever Ethos 1.6.0+ at den
oppgraderes før du fortsetter (**Go to Module manager** flasher den
automatisk, og deretter fortsetter Ethos-oppdateringen) — og for
TD/TW/AP/AP Plus-mottakere må telemetrien slettes og oppdages på nytt
etterpå for å få inn oppdaterte sensornavn.

Oppdateringsforløpet vises trinn for trinn (bytte til bootloader,
nedlasting, kopiering, utløsing av disker, skriving, oppdatering, «Update
successful!») — senderens egen skjerm viser også skriveforløpet.

!!! note "Oppdatering til forhåndsversjoner"
    Filene i en forhåndsversjon kan endres uten at versjonsnummeret
    endres, noe Suite ikke kan oppdage — flash alltid på nytt en
    forhåndsversjon du allerede kjører når den blir en full utgivelse.
    Sjekk fastvaredatoen under [System →
    Info](../system-setup/information.md) hvis du er i tvil.

!!! note "Oppdatering fra Ethos 1.2.8 eller tidligere"
    Suite kan være ute av stand til å flashe fastvare/bootloader helt
    automatisk fra en så gammel versjon — i stedet vises en veiledet
    dialog for manuell flashing. Løs ut diskene manuelt før du kobler fra
    USB uansett.

Systembitmap-filer oppdateres nå automatisk sammen med fastvaren (ingen
separat håndtering nødvendig); lydfiler oppdateres via **Write all
components** eller **Write audio files** (laster ned den valgte
språkpakken, f.eks. «English audio pack»).

### RF Module Manager

Velg en versjon (normalt den nyeste) og **Flash module** for å oppdatere
fastvaren i den interne RF-modulen direkte — bekrefter «...has been flashed
successfully» når den er ferdig. Dette utløses også automatisk av den
obligatoriske oppgraderingen til v3.0.1 som er beskrevet ovenfor.

### Ethos-modus

**Switch to Ethos** starter senderen på nytt ut av bootloader-modus og over
til å kjøre Ethos (vises med et grønt USB-ikon på senderen, og «(Bootloader
Mode)» forsvinner fra Suite-overskriften). Dette er nødvendig for at
**Download center** skal kunne bruke senderen som mellomledd ved flashing
av moduler, mottakere, sensorer og servoer. Knappen blir deretter **Switch
to Bootloader** for å reversere dette. **Eject Drives** kobler senderen fra
på en trygg måte.

### Model Manager

Sikkerhetskopierer modellfiler og innstillinger til disk, eller
gjenoppretter en tidligere sikkerhetskopi.

!!! warning
    Gjenoppretting gjenoppretter **ikke** fastvaren — etter at du har
    gjenopprettet modeller/innstillinger må du separat flashe den
    fastvareversjonen som faktisk hører til den sikkerhetskopien (se
    [Oppdatere Ethos](#updating-ethos)), siden modellfiler ikke er
    bakoverkompatible.

- **Backup Location** — naviger til en mappe (huskes per sendertype);
  dato/klokkeslett for den siste sikkerhetskopien vises under.
- **Backup** — lagrer modellfiler og registrerer gjeldende Ethos-versjon
  sammen med dem.
- **Restore** — velg hvilke komponenter som skal hentes tilbake: Audio (av
  som standard), Scripts, Screenshots, System Bitmaps (av som standard —
  håndteres nå sammen med fastvaren), Models (inkludert eventuelle
  tekstfiler for [brukerdefinert
  sjekkliste](../how-to/user-defined-checklist.md) som er lagret sammen med
  dem), Language, User Bitmaps, Logs og System Settings.

### Lua library

Bla gjennom og installer Lua-skript/-verktøy fra FrSkys eksterne bibliotek
med ett klikk (eller installer fra en lokal zip-fil). Installerte skript
vises sammen med den eksterne katalogen så snart det finnes noen.

## Verktøyseksjonen

- **Download center** — last ned all fastvare fra FrSkys nettsted, og bruk
  (mens senderen er i Ethos-modus) senderen som mellomledd for å flashe en
  modul, sensor, servo eller mottaker som er tilkoblet via en
  S.Port-oppgraderingstilkobling. Velg produktet fra listen (f.eks. en TW
  SR8-mottaker), bla gjennom tilgjengelige **assets**, bruk **Download**
  for å lagre lokalt eller **Flash** for å skrive direkte til den
  tilkoblede enheten — en fremdriftsindikator følger flashingen og avsluttes
  med «...has been flashed successfully!»

- **Image manager** — konverterer bilder til Ethos' eget format (32-bits
  BMP, RGB, alfakanal legges bare til ved behov) i valgt størrelse, med
  bevart sideforhold. Referansestørrelser: modellbilder 300×280 (X20) /
  180×168 (X18); fullskjermbilder 800×480 (X20) / 480×320 (X18) — se
  [Filbehandler](../system-setup/file-manager.md#top-level-folders) for
  navneregler for bitmaps. Verktøyet kan også bla direkte i senderens
  mapper `bitmaps/gps`, `bitmaps/models` og `bitmaps/user`, med støtte for
  opplasting. Legg til bilder i konverteringslisten med **+** (TIFF støttes
  ikke), velg en utdatabane (en lokal mappe; direkte til senderen under
  modell-/bruker-/GPS-bilder; eller den senderens mappe som er åpen), og
  velg eventuelt å åpne utdatamappen automatisk eller å tvinge fram en
  alfakanal.

- **Audio manager** — konverterer lyd til Ethos' format (PCM lineær, 32 kHz,
  mono, 16-bit little-endian). Legg til filer med **+**, velg en lokal
  mappe eller send filene direkte til senderens `audio`-mappe (og flytt dem
  deretter inn i riktig undermappe for stemme), og velg eventuelt å åpne
  målmappen automatisk.

- **Lua development tools** — **Lua Docs** lenker til referanseveiledningen
  for Ethos Lua (se også rcgroups-tråden *FrSky - ETHOS Lua Script
  Programming*); **Lua Demo Scripts** lenker til eksempelskript på
  Ethos-Feedback-Community på GitHub; **Debug** åpner et sanntidsvindu for
  Lua `print()`-utskrifter sendt over USB-Serial mens senderen er i
  Serial-modus:

  1. Koble senderen til Suite på vanlig måte og bytt til Ethos-modus.
  2. Rediger Lua-skript direkte på senderens monterte disk, i en valgfri
     kodeeditor.
  3. Åpne **Lua Development Tools** → **START DEBUG** — dette starter
     senderen på nytt i Serial-/feilsøkingsmodus og initialiserer skriptene
     på nytt.
  4. Utskriften fra `print()` i alle aktive skript strømmes til Suites
     terminal.
  5. **STOP DEBUG** bytter tilbake til normal Ethos-modus for videre
     redigering.

- **DFU Flasher** — flasher bootloaderen via en USB-tilkobling med senderen
  avslått (DFU), og fungerer selv med helt ødelagt fastvare, siden den
  underliggende ST-bootloaderen ligger i ROM. Bruk **Select Bootloader** for
  å velge en nedlastet fil (Suite rapporterer versjon/egnethet), koble til
  den **avslåtte** senderen, og velg deretter **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Vanligvis en manglende eller feil DFU-driver. De fleste PC-er med
      Windows 10+ håndterer Tandem-systemer med standard USB DFU-driver,
      men Windows Update erstatter den av og til med en generisk driver som
      ikke fungerer — sjekk Enhetsbehandling, og vurder et verktøy som
      Impulse Driver Fixer. Spesielt Horus X10-brukere kan måtte installere
      USB-driveren for STM32-bootloaderen manuelt (Impulse Driver Fixer
      eller Zadig), siden Windows 10 ikke installerer den som standard.

- **Repair Tool** — for X18/S, TW Lite, XE og X20 Pro/R/RS: formaterer den
  interne lagringen på nytt når senderen ikke kan lese NAND eller lagre
  innstillinger.

## Øvrig-seksjonen

- **Documentation** — lenker til Ethos-Feedback-Community på GitHub, de
  offisielle Ethos-manualene (nedlastbare) og en FAQ for Ethos Suite.
- **Ethos Github** — utgivelser og feilsporing (søk i eksisterende saker før
  du oppretter en ny).

### Innstillinger for Suite {: #suite-settings }

- **Language** — tsjekkisk, tysk, engelsk, spansk, fransk, hebraisk,
  italiensk, nederlandsk, norsk, portugisisk, slovensk, kinesisk.
- **Server location** — **FrSky server** eller **GitHub** (nødvendig for
  tilgang til forhåndsversjoner, som beskrevet ovenfor).
- **Debug options** — slå av/på popup-vinduet for fatale feil; aktiver full
  feilsøkingslogging for Suite (ikke bare krasj); åpne loggmappen.
- **Version** / **Update Suite** — gjeldende versjon, og en manuell
  oppdateringssjekk.
- **About** — krediteringer for gjenbrukte komponenter.

## Bruk fra kommandolinjen

Ethos Suite kan kjøres fra en terminal:

| Flagg | Virkning |
|---|---|
| `--help` | Vis hjelp for kommandolinjen. |
| `--version` | Vis den installerte Suite-versjonen. |
| `--list-radios` | List opp alle støttede FrSky-sendere. |
| `--radio-components --radio {RADIO}` (eller `--radio auto`) | List opp komponentene til en tilkoblet sender og banene deres. `auto` oppdager automatisk; angi `{RADIO}` hvis mer enn én er tilkoblet. |
| `--get-path {COMPONENT}` | Hent banen til en komponent — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` eller `I18N`. |
| `--serial start` \| `--serial stop` | Aktiver/deaktiver seriell feilsøkingsmodus. |

!!! note
    Suite starter ikke i det hele tatt med mindre den gjenkjenner en gyldig
    kommando.
