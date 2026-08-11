---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Sjekkliste med egendefinert tekst

![Egendefinert sjekklistetekst](../assets/model-checklist-user-checklist.png)

Funksjonen [Sjekkliste](../model-setup/checklist.md) kan vise egendefinert
tekst ved oppstart – som ren tekst eller Markdown-formatert – automatisk,
hver gang den aktuelle modellen lastes.

## 1. Lag sjekklisteteksten

**Ren tekst** – skriv den i et vilkårlig tekstredigeringsprogram (Notepad++,
eller til og med MS Word lagret som ren tekst) og lagre den som `<model name>.txt`.

**Utvidet tekst (Markdown)** – Ethos støtter Markdown-formatering, f.eks.
`##` for en overskrift og `**bold**` for fet tekst. Bruk et vanlig
tekstredigeringsprogram (der du skriver inn Markdown-syntaksen manuelt) eller
et dedikert Markdown-redigeringsprogram (Nextpad, MarkText osv.), og lagre den
som `<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Kopier den til senderen

Kopier filen til samme `models/`-mappe som modellens egen `.bin`-fil
(se [Filbehandler](../system-setup/file-manager.md#top-level-folders)),
og løs deretter ut senderens diskstasjoner på en sikker måte før du kobler fra.

## 3. Gå gjennom den

Last inn modellen – sjekklisteteksten vises nå automatisk som en del av
oppstartskontrollene, og kan rulles dersom den er lengre enn én skjerm.
