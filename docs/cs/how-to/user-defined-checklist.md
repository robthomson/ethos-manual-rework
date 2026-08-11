---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Kontrolní seznam s uživatelským textem

![Text uživatelského kontrolního seznamu](../assets/model-checklist-user-checklist.png)

Funkce [Kontrolní seznam](../model-setup/checklist.md) umí při spuštění
zobrazit vlastní text — jako čistý text nebo formátovaný pomocí Markdownu —
automaticky při každém načtení daného modelu.

## 1. Vytvoření textu kontrolního seznamu

**Čistý text** — napište jej v libovolném textovém editoru (Notepad++ nebo
i MS Word s uložením jako čistý text) a uložte jako `<model name>.txt`.

**Rozšířený text (Markdown)** — Ethos podporuje formátování Markdown, např.
`##` pro nadpis, `**bold**` pro tučný text. Použijte libovolný textový editor
(se ručně vloženou syntaxí Markdown) nebo specializovaný editor Markdownu
(Nextpad, MarkText atd.) a uložte jako `<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Zkopírování do vysílače

Zkopírujte soubor do stejné složky `models/`, ve které se nachází vlastní
soubor `.bin` daného modelu (viz [Správce souborů](../system-setup/file-manager.md#top-level-folders)),
a poté před odpojením bezpečně odeberte disky vysílače.

## 3. Kontrola

Načtěte model — text kontrolního seznamu se nyní automaticky zobrazí jako
součást kontrol při spuštění, a pokud je delší než jedna obrazovka, lze jím
posouvat.
