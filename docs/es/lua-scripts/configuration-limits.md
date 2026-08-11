---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Límites de configuración

- **2MB** para mapas de bits (un único mapa de bits a pantalla completa en la
  X20 consume por sí solo unos 768K).
- **2MB** para scripts Lua, un presupuesto generoso en la práctica.

!!! tip "Mapas de bits en los scripts"
    Evite mantener grandes cantidades de datos de mapas de bits en la RAM. Es
    preferible la **carga diferida**: cargue un mapa de bits únicamente cuando
    sea realmente necesario y manténgalo después en la caché de memoria para la
    próxima vez, en lugar de releerlo repetidamente desde la SD card/eMMC.
