---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Limites de configuration

- **2 Mo** pour les bitmaps (un seul bitmap plein écran sur le X20 occupe
  à lui seul environ 768 Ko).
- **2 Mo** pour les scripts Lua — un budget largement suffisant en pratique.

!!! tip "Bitmaps dans les scripts"
    Évitez de conserver de grandes quantités de données bitmap en RAM. Privilégiez
    le **chargement différé** (lazy loading) — ne chargez un bitmap que lorsqu'il est
    réellement nécessaire, puis conservez-le en cache mémoire pour la fois suivante
    plutôt que de le relire répétitivement depuis la SD card/eMMC.
