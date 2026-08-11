---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modelloppsett for SR8/SR10 og omorganisering av kanaler

FrSkys stabiliserte SRx-mottakere forventer en bestemt kanalrekkefølge. To
scenarier: å bygge en ny modell for en slik mottaker fra grunnen av, eller å
konvertere en eksisterende modell slik at den passer.

!!! note "Skjermbilder kommer"
    Denne siden har ennå ikke skjermbilder fra simulatoren — se [Skjermbilde-
    pipeline](../contributing/screenshot-pipeline.md).

## Opprette en ny modell

Veiviseren i [Modellvalg](../model-setup/model-select.md) grupperer som standard
ror med samme funksjon (f.eks. 2 krengeror → `AAETR`), men SRx-mottakere krever
at de fire første kanalene er låst som **AETRA** i stedet.

1. Kontroller i [Kontroller](../system-setup/controls.md) at **Kanalrekkefølge**
   er `AETR`.
2. Slå på **[Fire første kanaler
   låst](../system-setup/controls.md#first-four-channels-fixed)** — dette
   hindrer veiviseren fra å gruppere de fire første kanalene, slik at de holdes
   strengt i rekkefølgen `AETRA…` uansett hvor mange av hvert ror flyet har.
3. Kjør veiviseren for modelloppretting som normalt — de 5 første kanalene
   kommer ut som `AETRA`.

!!! note "Selvtest for Archer-mottakere"
    Selvtest for Archer-mottakere kjøres nå via [Enhetskonfigurasjon →
    SxR](../system-setup/devices.md) (firmware v2.1.10+), og ikke gjennom en
    egen selvtestprosedyre. Gasskanalen må stå på −100 %, ellers starter ikke
    selvtesten.

## Omorganisere en eksisterende modell

Å konvertere en eksisterende modell (f.eks. med nåværende rekkefølge `AAETRFF`)
til rekkefølgen for stabiliserte mottakere (`AETRAE`, deretter kanal 9 Gain,
10/11 flymoduser, 12 selvtest på eldre SxR-enheter) består av en serie
kanalbytter i [Utganger](../model-setup/outputs.md#swap-channels).

Utgangspunkt:

| Kanal | Funksjon |
|---|---|
| 1 | Krengeror1 (høyre) |
| 2 | Krengeror2 (venstre) |
| 3 | Høyderor |
| 4 | Gass |
| 5 | Sideror |
| 6 | Flaps1 (høyre) |
| 7 | Flaps2 (venstre) |
| 8 | Inntrekkbart understell |

Målrekkefølge: `AETRAE` — CH1 Krengeror1, CH2 Høyderor, CH3 Gass,
CH4 Sideror, CH5 Krengeror2, CH6 Høyderor2/AUX2 (deretter Gain/flymoduser/
selvtest på 9–12).

1. **Flytt Krengeror2 ut av veien først**: velg CH2 (Krengeror2) i Utganger,
   trykk på nytt, velg **Bytt kanaler**, og bytt den med en ubrukt kanal (f.eks.
   CH9). Byttet skjer umiddelbart — alle mikser som refererer til én av
   kanalene, oppdateres automatisk.
2. **Bytt CH3 (Høyderor) → CH2.**
3. **Bytt CH4 (Gass) → CH3.**
4. **Bytt CH5 (Sideror) → CH4.**
5. **Bytt CH9 (Krengeror2, parkert i trinn 1) → CH5.**

Resultat:

| Kanal | Funksjon |
|---|---|
| 1 | Krengeror1 (høyre) |
| 2 | Høyderor |
| 3 | Gass |
| 4 | Sideror |
| 5 | Krengeror2 (venstre) |
| 6 | Flaps1 (høyre) |
| 7 | Flaps2 (venstre) |
| 8 | Inntrekkbart understell |

— nå i den rekkefølgen FrSkys stabiliserte mottakere forventer.
