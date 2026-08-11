---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Limiti di configurazione

- **2MB** per le bitmap (una singola bitmap a schermo intero sul solo X20 occupa
  circa 768K).
- **2MB** per gli script Lua — un budget generoso nella pratica.

!!! tip "Bitmap negli script"
    Evitare di mantenere grandi quantità di dati bitmap nella RAM. È preferibile il
    **caricamento differito** (lazy loading): caricare una bitmap solo quando è
    effettivamente necessaria, quindi mantenerla nella cache in memoria per gli usi
    successivi, invece di rileggerla ripetutamente dalla SD card/eMMC.
