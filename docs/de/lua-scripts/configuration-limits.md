---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Konfigurationsgrenzen

- **2 MB** für Bitmaps (allein ein einzelnes bildschirmfüllendes Bitmap
  belegt auf dem X20 rund 768 K).
- **2 MB** für Lua-Skripte — in der Praxis ein großzügiges Budget.

!!! tip "Bitmaps in Skripten"
    Vermeiden Sie es, große Mengen an Bitmap-Daten im RAM zu halten. Bevorzugen
    Sie **Lazy Loading** — laden Sie ein Bitmap erst dann, wenn es tatsächlich
    benötigt wird, und halten Sie es anschließend für das nächste Mal im
    Speicher zwischengespeichert, anstatt es wiederholt von der SD card/eMMC
    einzulesen.
