---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Checklist con testo definito dall'utente

![Testo della checklist utente](../assets/model-checklist-user-checklist.png)

La funzione [Checklist](../model-setup/checklist.md) può visualizzare all'avvio
un testo personalizzato — testo semplice oppure formattato in Markdown — in
modo automatico, ogni volta che quel modello viene caricato.

## 1. Crea il testo della checklist

**Testo semplice** — scrivilo con un qualsiasi editor di testo (Notepad++, o
anche MS Word salvando in formato testo semplice) e salvalo come
`<model name>.txt`.

**Testo avanzato (Markdown)** — Ethos supporta la formattazione Markdown, ad
esempio `##` per un titolo, `**bold**` per il testo in grassetto. Utilizza un
qualsiasi editor di testo (inserendo a mano la sintassi Markdown) oppure un
editor Markdown dedicato (Nextpad, MarkText, ecc.) e salva il file come
`<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Copialo sulla radio

Copia il file nella stessa cartella `models/` in cui si trova il file `.bin`
del modello (vedi [File Manager](../system-setup/file-manager.md#top-level-folders)),
quindi espelli in modo sicuro le unità della radio prima di scollegarla.

## 3. Verificalo

Carica il modello: il testo della checklist compare ora automaticamente come
parte dei controlli di avvio ed è scorrevole se supera la lunghezza di una
schermata.
