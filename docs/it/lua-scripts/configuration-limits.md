---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Limiti di configurazione

- **2MB** per le bitmap (una singola bitmap a schermo intero sull'X20 occupa da sola
  circa 768K).
- **2MB** per gli script Lua — un budget in pratica generoso.

!!! tip "Bitmap negli script"
    Evita di tenere grandi quantità di dati bitmap nella RAM. È preferibile il
    **caricamento differito** (lazy loading): carica una bitmap solo quando serve
    davvero, quindi mantienila nella cache in memoria per gli usi successivi,
    invece di rileggerla ripetutamente dalla SD card/eMMC.
