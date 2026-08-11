---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Model bewerken

![Model bewerken](../assets/model-editmodel.png)

Hier bewerkt u de parameters op modelniveau die de wizard oorspronkelijk heeft
ingesteld — hoofdzakelijk de identiteit, maar ook enkele overrides per model en
enkele hulpprogramma's.

## Naam, afbeelding

Wijzig de naam van het model of de bijbehorende afbeelding; bij het zoeken naar
een afbeelding wordt een voorbeeldminiatuur weergegeven.

## Modeltype

![Modeltype](../assets/model-edit-modeltype.png)

!!! warning
    Bij het wijzigen van het modeltype worden **alle** mixen gereset.

## Kanaaltoewijzingen

Het wijzigen van het staarttype of (bij een heli) het type tuimelschijf reset
eveneens alle mixen. Bij andere kanalen kan het toegewezen aantal worden
gewijzigd, of kan de toewijzing worden opgeheven.

## Filter voor analoge ingangen

![Filter voor analoge ingangen](../assets/model-edit-analog-filter.png)

[Systeeminstellingen → Hardware](../system-setup/hardware.md) bevat een globaal
analoog-naar-digitaal filter dat jitter rond het middelpunt van de stick kan
verminderen; deze instelling per model overschrijft dat filter uitsluitend voor
dit model.

![Opties voor analoog filter](../assets/model-edit-analog-filter-select.png)

## Functieschakelaars {: #function-switches }

![Functieschakelaars](../assets/model-edit-fn-switches.png)

De zes functieschakelaars zijn beschikbaar op elke plek waar een parameter
**Actieve voorwaarde** voorkomt, maar kunnen — in tegenstelling tot gewone
schakelaars — niet als algemene bron worden gebruikt. Ze worden geconfigureerd
als een van de volgende opties:

- **6-Pos met OFF** — het indrukken van een functieschakelaar vergrendelt deze
  in de aan-stand; wanneer u *dezelfde* schakelaar opnieuw indrukt, worden alle
  zes uitgeschakeld.
- **6-POS** — het indrukken van een functieschakelaar vergrendelt deze in de
  aan-stand totdat een *andere* schakelaar wordt ingedrukt, die de functie
  overneemt.
- **2 × 3-Pos** — verdeelt de zes schakelaars in twee groepen van drie, met één
  actieve schakelaar per groep.
- **6 × 2-Pos** — zes onafhankelijke vergrendelende aan/uit-schakelaars.
- **Momentary** — zes onafhankelijke schakelaars, elk alleen actief zolang deze
  ingedrukt wordt gehouden.
- **Persistent** — indien ingeschakeld, behoudt een functieschakelaar zijn
  toestand na uitschakelen of het opnieuw laden van het model in plaats van te
  worden gereset.

![Opties voor functieschakelaars](../assets/model-edit-fn-switches-select.png)

## SPort-connector

De 5V-pin van de S.Port-connector van de zender kan per model worden geschakeld —
handig om bijvoorbeeld een externe ontvanger in een leraar/leerling-opstelling te
voeden.

## Modelbedrijfstijd

![Modelbedrijfstijd](../assets/model-edit-model-runtime.png)

Houdt de totale tijd bij dat dit model is gevlogen of gebruikt.

## Alle mixen resetten

![Alle mixen resetten](../assets/model-edit-model-reset_all_mixes.png)

Zet elke mix van het model terug naar de standaardtoestand.
