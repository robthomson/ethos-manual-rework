---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Førstegangs oppsett av senderen

Engangsoppsettet som bør gjennomføres før du programmerer noen modell.
[Veiledningene](index.md) som følger, forutsetter alle at dette er gjort først.

!!! note
    Disse veiledningene er ingen streng oppskrift — de forutsetter grunnleggende
    RC-vokabular og at du er komfortabel med å navigere i Ethos-menyene. Er noe
    her uklart, se først [Brukergrensesnitt og
    navigasjon](../getting-started/user-interface-and-navigation.md).

## Steg 1. Lad senderen og flybatteriene

Lad senderbatteriet i henhold til retningslinjene som fulgte med senderen, og
flybatteriene med en lader tilpasset deres kjemi — vær særlig påpasselig med
litiumpakker.

## Steg 2. Kalibrer maskinvaren

Kontroller at [maskinvarekalibrering](../system-setup/hardware.md#analogs-calibration)
er utført (den kjøres automatisk ved første oppstart), slik at senderen kjenner
den nøyaktige senterposisjonen og ytterpunktene for hver gimbal, hvert
potensiometer og hver glidebryter. Gjenta kalibreringen under
**System → Maskinvare** hver gang en gimbal, et potensiometer eller en
glidebryter byttes.

## Steg 3. Utfør systemoppsettet av senderen

[Systeminnstillinger](../system-setup/index.md) dekker alt som er felles for
alle modeller, i motsetning til de modellspesifikke innstillingene i
[Modelloppsett](../model-setup/index.md). De fleste standardverdiene er greie å
starte med, men gjennomgå følgende:

- **[Dato og klokke](../system-setup/date-and-time.md)** — still inn riktig.
- **[Lyd → Valg av
  stemmer](../system-setup/general.md#audio-settings)** — sett opp
  taleopplesninger, inkludert eventuelle egendefinerte lydfiler.
- **[Kontroller (spaker)](../system-setup/controls.md)**:
  - **Spakmodus** — Modus 1 (gass/krengeror høyre, høyderor/sideror
    venstre) eller Modus 2 (gass/sideror venstre, krengeror/høyderor høyre —
    Ethos' standard).

    !!! warning
        Hvis en modell er konfigurert for én spakmodus mens senderen er satt
        til den andre, kan en elektrisk motor starte i det øyeblikket
        mottakeren får strøm.

  - **Kanalrekkefølge** — Ethos bruker som standard **AETR** (krengeror,
    høyderor, gass, sideror); Spektrum/JR-konvensjonen er **TAER**, mens
    Futaba/Hitec bruker **AETR**. Dette bestemmer rekkefølgen spakinngangene
    tilordnes i når en ny modell opprettes — modeller kan fremdeles justeres
    individuelt i etterkant.

    !!! note "FrSky stabiliserte mottakere"
        Disse krever spesifikt **AETR**. Med mer enn én flate per funksjon
        (f.eks. 2 krengeror) grupperer veiviseren dem normalt (som gir
        **AAETR**) — men SRx-mottakere forventer i stedet **AETRA**/**AETRAE**,
        så aktiver **[De fire første kanalene
        låst](../system-setup/controls.md#first-four-channels-fixed)**
        under Spaker for å holde de fire første kanalene i streng AETR-rekkefølge
        uansett.

- **[Batteri](../system-setup/battery.md)** — still inn **Hovedspenning**,
  **Lav spenning** og **Visningsområde for spenning** slik at det stemmer med
  senderens faktiske batteri.
- **[Eier-registrerings-ID](../model-setup/rf-system.md#owner-registration-id)**
  — brukes av ACCESS-mottakere, og deles mellom sendere for Smart Share.
  Konfigureres under Modelloppsett, men fungerer i praksis som en
  systemomfattende innstilling, siden hver ny modell bruker den (den kan
  fremdeles endres per mottaker under registrering ved behov).

!!! note "Enheter"
    Ethos har ingen global veksling mellom metrisk og imperisk — [enheter for
    telemetrisensorer](../model-setup/telemetry.md#editing-a-sensor) stilles inn
    individuelt, per sensor.
