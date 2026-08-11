---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Spesialfunksjoner

![Meny for spesialfunksjoner](../assets/model-sf-menu.png)

Spesialfunksjoner utløser en handling — spille av lyd, ta et
skjermbilde, skrive logger, haptisk tilbakemelding og mer — når en
betingelse blir sann. Opptil 100 støttes; ingen finnes som standard. Legg
til en med **+**; trykk på en eksisterende for **Rediger**/**Flytt**/
**Kopier-lim inn**/**Klone**/**Slett**.

![Legg til spesialfunksjon](../assets/model-sf-add.png)
![Flytt](../assets/model-sf-move.png)

## Felter som er felles for alle handlinger

- **Status** — aktiver/deaktiver denne funksjonen uten å slette den.
- **Aktiv betingelse** — **Alltid på**, eller styrt av bryter/
  funksjonsbryter/logisk bryter/trimposisjoner eller flymoduser. Hold
  `ENT` inne på en bryter og merk av **Negativ** for å invertere den
  (f.eks. blir `SG-up` til `!SG-up`, aktiv når SG *ikke* er opp).
- **Global** — legger denne funksjonen til i **alle** modeller,
  eksisterende og fremtidige. Hvis en modell allerede har en identisk
  konfigurert lokal funksjon, legger Global den til som en ekstra
  oppføring; slår du Global av igjen, fjernes den fra alle modeller
  bortsett fra den som er valgt nå. Globale funksjoner ligger i
  `radio.bin`; lokale ligger i modellfilen.

## Handlinger {: #actions }

**Nullstill** — nullstiller **Flydata** (telemetri + timere), **Alle
timere** eller **Hele telemetrien**.

![Nullstill](../assets/model-sf-reset.png)

**Skjermbilde** — lagrer et skjermbilde i `screenshots/` på SD card/eMMC.

![Skjermbilde](../assets/model-sf-screenshot.png)

**Sett failsafe** — lagrer de gjeldende kanalposisjonene som failsafe, via
enten den interne eller den eksterne RF-**modulen**.

![Sett failsafe](../assets/model-sf-set-failsafe.png)

**Spill lyd** — den mest omfattende handlingen, med støtte for en
fullstendig sekvens:

![Spill lyd](../assets/model-sf-play-audio.png)

- **Stemme** — hvilken av opptil 3 konfigurerte stemmer som skal brukes
  (se [Generelt](../system-setup/general.md#audio-settings)).
- **Gjenta** — spill av én gang, eller gjenta med et konfigurerbart
  intervall (opptil 10 minutter).
- **Hopp over ved oppstart** — hindrer at denne funksjonen utløses under
  oppstart.
- **Sekvens** — opptil 100 trinn, hvert av typen:

  - **Spill fil** — spiller av en valgt lydfil.

    ![Spill fil](../assets/model-sf-play-audio-add-play-file.png)

  - **Spill verdi** — leser opp verdien til en kilde: analoge innganger,
    brytere, logiske brytere, trim, kanaler, gyro, systemklokke, trener,
    timere eller telemetri.

    ![Spill verdi](../assets/model-sf-play-audio-add-play-value.png)

  - **Vent varighet** — en fast pause, opptil 10 minutter.
  - **Vent betingelse** — pauser sekvensen til en betingelse er oppfylt.

  ![Legg til sekvenslinje](../assets/model-sf-play-audio-add-line.png)
  ![Type sekvenslinje](../assets/model-sf-play-audio-add-line-type.png)

  Eksempel: spill `vfrlow.wav` når den logiske bryteren `VFRlow` blir
  aktiv, og les deretter opp den registrerte minimumsverdien for VFR —

  ![Spill verdi etter fil](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — eller pause en sekvens til bryteren SH settes ned før den fortsetter:

  ![Sekvens med ventebetingelse](../assets/model-sf-play-audio-add-sequence.png)

  Trykk på en sekvenslinje for å redigere, legge til, endre rekkefølge på
  eller slette den:

  ![Håndtering av sekvens](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptikk** — vibrasjonstilbakemelding:

![Haptikk](../assets/model-sf-haptic.png)

- **Mønster** — enkel, dobbel, trippel, femdobbel eller svært kort.

  ![Haptisk mønster](../assets/model-sf-haptic-pattern.png)

- **Styrke** — 1–10 (standard 5).
- **Gjenta** — én gang, eller med et fast intervall.
- **Velg haptiske motorer** — på sendere med haptiske motorer i spakene
  (X20 Pro AW, X20RS, eller en X20 Pro/X20R oppgradert med MC20R-spaker —
  se
  [Maskinvare](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Standard** (intern haptikk), **Alle motorer**, **Venstre spak** eller
  **Høyre spak**.

  ![Haptikk på X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Skriv logger** — skriver `.csv`-logger til `Logs/` på SD card/eMMC, med
tidsstempel fra RTC-en (avgjørende for å kunne skille flyøktene fra
hverandre i ettertid):

![Skriv logger](../assets/model-sf-write-logs.png)

- **Skriveintervall** — 100–500 ms.
- **Spaker/potensiometre/glidebrytere**, **Brytere**, **Logiske brytere**,
  **Kanaler** — loggkategorier som slås av og på uavhengig av hverandre.

  **Vise logger**: åpne en loggfil fra `/Logs` i Filbehandler. Velg
  hvilke kanaler som skal plottes (RSSI er valgt som standard); panorér
  med dreieknappen eller ved å sveipe, og zoom ved å vri dreieknappen mens
  du holder `PAGE`. `DISP` flytter fokus til den første knappen i kolonnen
  til høyre.

**Spill tekst** (kun X20 Pro) — tekst-til-tale i senderen i stedet for en
forhåndsinnspilt fil:

![Spill tekst](../assets/model-sf-x20pro-play-text.png)

- **Tekst** — teksten som skal leses opp. STORE BOKSTAVER staves bokstav
  for bokstav (f.eks. «OFF» → «O-F-F»); små bokstaver leses som ord
  («off»).
- **Gjenta**, **Hopp over ved oppstart** — som over.

**Gå til skjerm** — bytter visningen til en valgt skjerm, f.eks. ved å
hoppe til en mottakers flydataregistrering når en knapp trykkes:

![Gå til skjerm](../assets/model-sf-go-to-screen.png)
![Skjermvalg](../assets/model-sf-go-to-screen-options.png)

**Lås berøringsskjerm** — låser berøringsskjermen mot utilsiktede
inntastinger (kan også nås direkte ved å holde `ENT` + `PAGE` inne
samtidig i 1 s fra hjemskjermen):

![Lås berøringsskjerm](../assets/model-sf-lock-touchscreen.png)

**Last modell** — laster en angitt **Modell** når den utløses, med en
valgfri **Bekreftelse** før byttet faktisk skjer:

![Last modell](../assets/model-sf-load-model.png)

**Spill vario** — styrer variolyd fra en valgt kilde (normalt VSpeed-
sensoren i en FrSky-vario, men enhver sensor med enheten m/s fungerer):

![Spill vario](../assets/model-sf-play-vario.png)
![Variokilde: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Område** — stige-/synkehastighet omsatt til tonehøyde, standard
  ±10 m/s (opptil ±100 m/s). Over **Senter** øker tonehøyden lineært med
  stigehastigheten opp til maksverdien for Område (tonehøyden ved maksimal
  hastighet settes i [Generelt →
  Vario](../system-setup/general.md#vario)); ved synking gis en
  kontinuerlig tone som synker i tonehøyde mot minimumsverdien for Område.
- **Senter** — båndet for «null stigning», standard ±0,3 m/s (opptil
  ±2 m/s); tonehøyden er konstant innenfor dette (tonehøyden ved null
  hastighet settes også i Generelt → Vario). Bytt **Pip**→**Stille** for å
  dempe tonen helt.

  ![Valg for varioområde/senter](../assets/model-sf-play-vario-options.png)
