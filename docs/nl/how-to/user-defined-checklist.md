---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Checklist met eigen tekst

![Checklisttekst van gebruiker](../assets/model-checklist-user-checklist.png)

De functie [Checklist](../model-setup/checklist.md) kan bij het opstarten
automatisch eigen tekst weergeven — platte tekst of Markdown-opgemaakte tekst —
elke keer dat dat model wordt geladen.

## 1. De checklisttekst maken

**Platte tekst** — schrijf deze in een willekeurige teksteditor (Notepad++, of
zelfs MS Word opgeslagen als platte tekst) en sla het bestand op als
`<model name>.txt`.

**Uitgebreide tekst (Markdown)** — Ethos ondersteunt Markdown-opmaak, bijv.
`##` voor een kop en `**bold**` voor vetgedrukte tekst. Gebruik een willekeurige
teksteditor (waarbij u de Markdown-syntaxis handmatig invoert) of een speciale
Markdown-editor (Nextpad, MarkText, enz.) en sla het bestand op als
`<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Het bestand naar de zender kopiëren

Kopieer het bestand naar dezelfde map `models/` waarin ook het `.bin`-bestand
van het model staat (zie [Bestandsbeheer](../system-setup/file-manager.md#top-level-folders)),
en werp daarna de schijven van de zender veilig uit voordat u de verbinding
verbreekt.

## 3. Controleren

Laad het model — de checklisttekst verschijnt nu automatisch als onderdeel van
de opstartcontroles, en is scrollbaar als deze langer is dan één schermvulling.
