---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuratielimieten

- **2MB** voor bitmaps (één enkele schermvullende bitmap gebruikt op de X20 al
  ongeveer 768K).
- **2MB** voor Lua-scripts — in de praktijk een ruim budget.

!!! tip "Bitmaps in scripts"
    Vermijd het vasthouden van grote hoeveelheden bitmapdata in RAM. Geef de
    voorkeur aan **lazy loading** — laad een bitmap pas wanneer die daadwerkelijk
    nodig is en houd deze daarna in het geheugen gecachet voor de volgende keer,
    in plaats van hem herhaaldelijk opnieuw van de SD card/eMMC te lezen.
