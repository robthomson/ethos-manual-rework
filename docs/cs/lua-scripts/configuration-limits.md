---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Omezení konfigurace

- **2 MB** pro bitmapy (jediná celoobrazovková bitmapa na X20 sama zabere
  přibližně 768 K).
- **2 MB** pro Lua skripty — v praxi velmi štědrý limit.

!!! tip "Bitmapy ve skriptech"
    Vyhněte se držení velkého množství bitmapových dat v RAM. Dejte přednost
    **opožděnému načítání** (lazy loading) — bitmapu načtěte teprve tehdy, když
    je skutečně potřeba, a poté ji uchovávejte v paměti pro další použití,
    místo opakovaného čtení z SD card/eMMC.
