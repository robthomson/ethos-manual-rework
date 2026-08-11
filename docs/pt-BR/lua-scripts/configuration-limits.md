---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Limites de configuração

- **2MB** para bitmaps (um único bitmap em tela cheia no X20 já consome
  cerca de 768K).
- **2MB** para scripts Lua — na prática, um orçamento generoso.

!!! tip "Bitmaps em scripts"
    Evite manter grandes quantidades de dados de bitmap na RAM. Prefira o
    **carregamento tardio** (lazy loading) — carregue um bitmap somente quando
    ele for realmente necessário e, em seguida, mantenha-o em cache na memória
    para o próximo uso, em vez de relê-lo repetidamente do SD card/eMMC.
