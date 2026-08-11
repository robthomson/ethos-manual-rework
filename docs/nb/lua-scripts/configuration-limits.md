---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Konfigurasjonsgrenser

- **2 MB** for bitmap-bilder (et enkelt fullskjermsbilde bruker alene omtrent
  768 K på X20).
- **2 MB** for Lua-skript – i praksis et romslig budsjett.

!!! tip "Bitmap-bilder i skript"
    Unngå å holde store mengder bitmap-data i RAM. Foretrekk **lazy
    loading** – last inn et bilde først når det faktisk er nødvendig, og
    behold det deretter i hurtigbufferen i minnet til neste gang i stedet
    for å lese det gjentatte ganger fra SD card/eMMC.
