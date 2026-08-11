---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Rediger modell

![Rediger modell](../assets/model-editmodel.png)

Redigerer parameterne på modellnivå som veiviseren satte opp
innledningsvis — hovedsakelig identitet, men også noen overstyringer og
verktøy per modell.

## Navn, bilde

Gi modellen nytt navn eller endre bildet; når du blar etter et bilde,
vises en forhåndsvisning som miniatyrbilde.

## Modelltype

![Modelltype](../assets/model-edit-modeltype.png)

!!! warning
    Å endre modelltypen nullstiller **alle** mikser.

## Kanaltilordninger

Å endre halетype eller (på en heli) swashplate-type nullstiller også alle
mikser. For andre kanaler kan tilordnet antall endres, eller de kan gjøres
utilordnet.

## Analogfilter

![Analogfilter](../assets/model-edit-analog-filter.png)

[Systeminnstillinger → Maskinvare](../system-setup/hardware.md) har et
globalt analog-til-digital-filter som kan redusere flimmer rundt
spaksenter; denne innstillingen per modell overstyrer det bare for denne
modellen.

![Alternativer for analogfilter](../assets/model-edit-analog-filter-select.png)

## Funksjonsbrytere {: #function-switches }

![Funksjonsbrytere](../assets/model-edit-fn-switches.png)

De seks funksjonsbryterne er tilgjengelige overalt der en parameter for
**Aktiv betingelse** finnes, men kan — i motsetning til vanlige brytere —
ikke brukes som en generell kilde. De konfigureres som én av følgende:

- **6-Pos with OFF** — et trykk på en funksjonsbryter låser den på; et nytt
  trykk på *samme* bryter slår av alle seks.
- **6-POS** — et trykk på en funksjonsbryter låser den på til en *annen*
  bryter trykkes, som da tar over.
- **2 × 3-Pos** — deler de seks inn i to grupper på tre, med én aktiv
  bryter per gruppe.
- **6 × 2-Pos** — seks uavhengige låsende av/på-brytere.
- **Momentary** — seks uavhengige brytere, hver aktiv bare så lenge den
  holdes inne.
- **Persistent** — hvis aktivert, beholder en funksjonsbryter tilstanden
  sin ved avslåing/ny innlasting av modellen i stedet for å nullstilles.

![Alternativer for funksjonsbrytere](../assets/model-edit-fn-switches-select.png)

## SPort-kontakt

5V-pinnen på senderens S.Port-kontakt kan slås av og på per modell —
nyttig for eksempel til å forsyne en ekstern mottaker i et
lærer/elev-oppsett.

## Modellens driftstid

![Modellens driftstid](../assets/model-edit-model-runtime.png)

Holder oversikt over den totale tiden denne modellen har vært
fløyet/kjørt.

## Nullstill alle mikser

![Nullstill alle mikser](../assets/model-edit-model-reset_all_mixes.png)

Nullstiller hver enkelt miks på modellen tilbake til standardtilstanden.
