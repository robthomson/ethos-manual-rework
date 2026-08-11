---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Generelt

![Generelle innstillinger](../assets/system-general.png)

Omfatter skjermegenskaper, lyd, vario, haptikk og den øvre verktøylinjen.

## Skjermegenskaper

- **Språk** — menyspråket på skjermen (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português med flere).
- **Tastatur** — tastaturoppsettet for det virtuelle tastaturet: QWERTY,
  QWERTZ eller AZERTY.
- **Lysstyrke** — en glidebryter for bakgrunnslysets lysstyrke; hold `ENT`
  inne for å styre den fra en kilde i stedet (f.eks. en glidebryter, som i
  eksempelet nedenfor), eller tvinge den til minimum/maksimum.

  ![Lysstyrkemeny](../assets/system-general-brightness-menu.png)
  ![Glidebryter for lysstyrke](../assets/system-general-brightness-slider.png)

  !!! note
      Hvis **Lysstyrke** er lik **Lysstyrke i hvilemodus**, forblir
      berøringsskjermen aktiv også når senderen «sover».

- **Vekking** — hva som vekker bakgrunnslyset fra hvilemodus (flere kan
  være aktivert samtidig): **Alltid på** (går aldri i hvilemodus),
  **Spaker**, **Brytere**, **Gyro** (ved å vippe senderen). Tastene vekker
  den alltid, uavhengig av disse innstillingene.
- **Hvilemodus** — hvor lenge senderen skal være inaktiv før
  bakgrunnslyset slås av (nedtonet dersom Vekking er satt til Alltid på).
- **Lysstyrke i hvilemodus** — bakgrunnslysets lysstyrke i hvilemodus.
- **Mørk modus** — lyst eller mørkt skjermtema.
- **Uthevingsfarge** — brukergrensesnittets aksentfarge (standard
  `#F8B038`).

## Lydinnstillinger {: #audio-settings }

![Lydinnstillinger](../assets/system-general-audio.png)

- **Lydspråk** — språk for taleopplesning.
- **Valg av stemmer** — Ethos støtter flere samtidige stemmepakker:

  - **Stemme 1 (hoved)** — brukes til alle innebygde systemmeldinger. For
    engelsk er standardvalget mellom amerikansk (`us`) og britisk (`gb`)
    pakke, som leses fra `audio/en/us/system` og `audio/en/gb/system`.
    Egne lydfiler for [spesialfunksjonen Play
    Audio](../model-setup/special-functions.md) legges i `audio/en/us/`
    eller `audio/en/gb/` tilsvarende.
  - **Stemme 2 / Stemme 3** — ytterligere pakker, for eksempel en egen
    TTS-stemme. Hver av dem trenger samme mappestruktur som Stemme 1 —
    f.eks. trenger en stemme kalt «Susan» mappen `audio/en/Susan/` for
    egne lyder og `audio/en/Susan/system` for sine systemlyder (hver
    stemme trenger en `/system`-mappe, siden det er derfra **Play Value**
    og timeropplesninger hentes; en `.csv`-liste over de standard
    systemlydfilene følger med hver lydutgivelse). Når en stemme er
    installert, kan den tilordnes per timer og per Play Audio-funksjon —
    eller til og med settes som Stemme 1 for å erstatte systemmeldingene
    helt.
  - **Stemmen «default»** — installeres automatisk som en trygg
    reserveløsning (og brukes for å unngå konverteringsproblemer fra
    1.4.x-installasjoner): hvis Stemme 1 ikke allerede er satt under en
    installasjon/oppgradering, settes den til `default` og leser fra
    `audio/en/default/system`. Ofte etterspurte egne lydfiler for Play
    Audio ligger i `audio/en/default/`.

- **Hovedvolum** — en glidebryter for det generelle lydvolumet (hold `ENT`
  inne for å styre det fra et potensiometer); det spilles pipetoner under
  justeringen slik at du kan bedømme nivået på øret.
- **Lydmodus**:
  - **Stille** — ingen lyd (utløser fortsatt [varselet for
    stillemodus](alerts.md) ved oppstart, hvis aktivert).
  - **Kun alarmer** — bare alarmer er hørbare.
  - **Standard** — normale lyder.
  - **Ofte** — legger til feilpip når en verdi forsøkes satt utenfor sitt
    minimum/maksimum.
  - **Alltid** — legger i tillegg til Ofte også pip ved vanlig
    menynavigasjon.
  - **Bluetooth** (kun X20S/HD/Pro/R/RS) — sender lyden videre til en
    sammenkoblet Bluetooth-enhet (hodesett o.l.). Velg **Search Devices**,
    sett målenheten i sammenkoblingsmodus, og velg den når den blir
    funnet:

    ![Bluetooth-sammenkobling](../assets/system-general-audio-bluetooth.png)
    ![Bluetooth-søk](../assets/system-general-audio-bluetooth-searching.png)
    ![Bluetooth-enhet valgt](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Bluetooth kobler til](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth tilkoblet](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Demping av høyttaler** styrer deretter den innebygde høyttaleren —
    alltid på, kun når telemetri er aktiv, eller styrt av en kilde (f.eks.
    en bryter). Senderen husker den sammenkoblede enheten; slå på senderen
    før Bluetooth-enheten for normal drift, og la det gå noen sekunder
    etter at den er tilkoblet før høyttalerdempingen aktiveres igjen.

## Vario {: #vario }

![Vario-lyd](../assets/system-general-audio-vario.png)

- **Volum** — vario-tonens relative volum.
- **Tonehøyde null** — tonehøyde ved null stigehastighet.
- **Tonehøyde maks** — tonehøyde ved maksimal stigehastighet.
- **Gjentakelse** — forsinkelse mellom pipene ved tonehøyde null.

Se også VSpeed-sensoren under [Telemetri](../model-setup/telemetry.md) og
[spesialfunksjonen Play Vario](../model-setup/special-functions.md) for
ytterligere vario-oppførsel.

## Haptikk

- **Styrke** — en glidebryter for vibrasjonsstyrke.
- **Modus** — samme valgmuligheter som for Lydmodus ovenfor.

## Lagringssted (X18 og X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Disse senderne har en intern 8 GB eMMC. Ethos bruker den som standard, slik
at et SD card er valgfritt — men du kan velge eMMC, et SD card eller en
kombinasjon av begge. Hvis du flytter systemet og modellene til et SD card,
må du kopiere over de aktuelle mappene/filene (inkludert lyd og punktgrafikk)
**før** du bytter lagringssted.

![Lagringssted](../assets/system-general-storage.png)

## Øvre verktøylinje

![Innstillinger for øvre verktøylinje](../assets/system-general-topbar.png)

- **Digital spenning** — viser senderbatteriets spenning som et tall i
  stedet for som en søyle i den øvre verktøylinjen.
- **Digital RSSI** — det samme, for RSSI på 2,4 GHz og 900 MHz.
- **Velg modell ved oppstart** — viser skjermen for modellvalg ved
  oppstart, før sjekklistevarslene for den forrige modellen vises, slik at
  du kan bytte modell uten å måtte lukke dem først. Den sist brukte
  modellen er uthevet som standard.

  ![Velg modell ved oppstart](../assets/system-general-model-start.png)

## Forvalg av USB-modus

![USB-modus](../assets/system-general-usb.png)

Hva som skjer automatisk når senderen kobles til en PC via USB:

- **Ikke satt** — spør om et valg ved tilkobling.
- **Joystick** — går umiddelbart i joystick-modus for en RC-simulator.
- **Ethos Suite** — går umiddelbart i Ethos-modus for [Ethos
  Suite](../ethos-suite/index.md).
- **Serial** — går umiddelbart i Serial-modus og sender Lua-feilsøkingsspor
  over USB-Serial med 115200 bps (det kan være nødvendig med en driver for
  virtuell COM-port i Windows).
