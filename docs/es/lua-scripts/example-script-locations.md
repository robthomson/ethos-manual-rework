---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ubicación de los scripts de ejemplo

Los scripts de ejemplo oficiales se publican en
[github.com/FrSkyRC/ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/tree/main/lua)
(en particular `/lua/examples/task` y `/lua/examples/source`). La mayoría de
los ejemplos son widgets Lua (que se configuran en [Configurar
pantallas](../displays/custom-widgets.md)); el ejemplo **`servo`**
concretamente demuestra una **Herramienta del sistema**: un script que aparece
después de **Info** en el menú System, en lugar de como widget de pantalla.

## Descargar un script

1. Abra el enlace del repositorio anterior en un navegador y navegue hasta la
   carpeta y, a continuación, hasta el archivo `main.lua` que desee.
2. Haga clic en el archivo para verlo y luego en **Raw**.
3. Haga clic con el botón derecho en la página → **Guardar página como…**, y guárdela como `main.lua`.
4. Para evitar conflictos con el `main.lua` de otros scripts, muévalo a una
   carpeta con un nombre acorde: el propio nombre de la carpeta de origen es
   una opción razonable.

Para cualquier otro archivo que necesite el script (imágenes, etc.): haga clic
en el archivo, haga clic en **Download** y después haga clic con el botón derecho y
**Guardar imagen como…** (o equivalente) para guardarlo junto al script.

Los scripts se instalan en `scripts/` en la SD card/eMMC — consulte [Gestor de
archivos](../system-setup/file-manager.md#top-level-folders).

Consulte también el hilo *FrSky ETHOS Lua Script Programming* en rcgroups para
scripts de la comunidad y debates más allá de los ejemplos oficiales.
