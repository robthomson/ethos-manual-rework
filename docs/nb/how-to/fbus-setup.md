---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Konfigurere et FBUS-system

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (tidligere
F.Port2) legger både styring og telemetri på én ledning, slik at flere FBUS-enheter
kan dele en enkelt kjedekoblet forbindelse med full trådløs
konfigurasjon. Denne gjennomgangen kobler to Xact-servoer til krengerorkanalene
(1 og 5) i [eksempelet med enkelt fastvingefly](../tutorials/basic-fixed-wing.md).

!!! note "Skjermbilder kommer"
    Denne siden har ennå ikke skjermbilder fra simulatoren — se [Skjermbilde-arbeidsflyt](../contributing/screenshot-pipeline.md).

## 1. Last ned nyeste fastvare

FBUS krever oppdatert fastvare både i mottakeren og i enhetene — Xact-servoer
trenger f.eks. v2.0.1 eller nyere. Hent de aktuelle oppdateringene fra
[FrSkys nedlastingsside](https://www.frsky-rc.com/download/).

## 2. Installer fastvaren

Kopier fastvarefilene til `Firmware/` på SD card/eMMC. I [Filbehandler](../system-setup/file-manager.md)
kobler du servoen til senderens S.Port-kontakt (hvit/gul ledning mot hakket),
velger fastvarefilen og trykker **Flash External Device**.

## 3 / 5. Konfigurere fysiske ID-er

Begge servoene har som standard fysisk ID `0C` hex / applikasjons-ID `6800` hex —
de vil komme i konflikt på den delte bussen med mindre én av dem endres. Det finnes
to måter å gjøre dette på, avhengig av mottakertype:

**Via senderens S.Port-kontakt** (alle mottakere):

1. Koble til servo 1, gå til **Device Config → XAct** og sett **Module** til
   **S.Port connector**. La fysisk ID `0C`/applikasjons-ID `6800` og
   kanal `CH1` stå på standardverdiene, og velg deretter **Save to flash**.
2. Koble til servo 2 i stedet, samme meny. Endre **Physical ID** til `0D` hex
   og **Application ID** til `6801` hex (se [tabellen over fysiske ID-er](../model-setup/telemetry.md#how-frsky-telemetry-works)
   for å se hvilke plasser som er ledige), sett **Channel** til `CH5` og velg **Save to flash**.

**Via mottakeren direkte** (f.eks. TD-R18 Tandem, med begge servoene tilkoblet
samtidig — se [trinn 4](#4-configure-the-receiver-for-fbus)):

1. Med bare servo 1 tilkoblet (f.eks. Pin1 på mottakeren): **Device Config →
   XAct**, **Module** → **Internal module**. Bekreft standardverdiene (`0C`/
   `6800`/`CH1`), og velg **Save to flash**.
2. Med bare servo 2 tilkoblet (Pin5), samme meny (Device Config kommuniserer med
   én servo om gangen) — endre til `0D`/`6801`/`CH5`, og velg **Save to flash**.
   Velg Device Config på nytt etterpå for å bekrefte at endringen ble lagret.

## 4. Konfigurere mottakeren for FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [RF System](../model-setup/rf-system.md) → knappen for mottakeren
→ **Options** → sett **Telemetry Port** til **FBUS**. Xact-servoene kjedekobles
deretter fra denne porten; siden hver servo bare har én kontakt, fordeler en
F.Port2 flerkanalsutvider (FP2CH4/6/8) signalet til flere servoer.

**TD-R18 Tandem**: RF System → knappen for mottakeren → **Options** → sett
enkeltpinner (f.eks. **Pin1**, **Pin5**) til **FBUS** — så mange pinner som
nødvendig kan omdefineres på denne måten, slik at utvidere blir helt unødvendige;
hver FBUS-tilordnet pinne fører det identiske FBUS-signalet.

## 5. Kontroller FBUS-styring av servoene

Koble servo 1 til Pin1 og servo 2 til Pin5 (krengerorkanalene i fastvinge-eksempelet),
slå på strømmen og bekreft at kanal 1 og 5 beveger de riktige servoene.

## 6. Kontroller FBUS-telemetri

Med begge servoene tilkoblet sletter du eventuelle eksisterende `SRV`-sensorer under
[Telemetri](../model-setup/telemetry.md) og søker etter sensorer på nytt. Hver servo
rapporterer 4 sensorer: strøm, spenning, temperatur og status (`OK` ved normal drift).

## 7. Gjøre konfigurasjonsendringer senere

Når en modell er ferdig montert, er det ikke praktisk å isolere én servo for å
konfigurere den på nytt via Device Config. Gjør i stedet følgende: gå til Telemetri,
finn en sensor som tilhører den aktuelle servoen (f.eks. `SRV1 curr`) og velg
**Configure** — dette åpner konfigurasjonen for den servoen direkte.
Velg **Save to flash** etter hver endring.

!!! warning
    Ikke endre fysisk ID eller applikasjons-ID fra denne skjermen ved et
    uhell — det er disse som gjør hver servo adresserbar på den delte
    bussen.
