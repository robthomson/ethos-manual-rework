---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ograniczenia konfiguracji

- **2 MB** na bitmapy (sama pojedyncza pełnoekranowa bitmapa w X20 zajmuje
  około 768 K).
- **2 MB** na skrypty Lua — w praktyce jest to hojny limit.

!!! tip "Bitmapy w skryptach"
    Unikaj przechowywania dużych ilości danych bitmapowych w pamięci RAM. Stosuj
    **leniwe ładowanie** — wczytuj bitmapę dopiero wtedy, gdy jest rzeczywiście
    potrzebna, a następnie przechowuj ją w pamięci podręcznej na przyszłość,
    zamiast wielokrotnie odczytywać ją z SD card/eMMC.
