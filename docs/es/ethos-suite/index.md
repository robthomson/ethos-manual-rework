---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite es la aplicación complementaria para Windows/Mac que permite gestionar una radio con Ethos, conectada por USB.

![Pestaña Radio de Ethos Suite](../assets/ethos-suite-radio-tab.png)

Una vez conectada, la Ethos Suite puede:

1. Leer el tipo de radio, su ID y las versiones instaladas: firmware, bootloader, módulo interno de RF, archivos de la memoria flash y archivos de la tarjeta SD o eMMC.
2. Cambiar la radio del modo bootloader al modo Ethos, y volver a cambiar.
3. Comparar las versiones instaladas con las actuales y actualizar de forma automática: sólo los componentes obsoletos, todos los componentes, o cada componente de forma individual.
4. Guardar en disco una copia de seguridad de los modelos mediante el **Gestor de Modelos**, o restaurar una copia de seguridad anterior (necesario porque los archivos de modelos no son compatibles entre versiones de firmware).
5. Descargar cualquier firmware desde el sitio de descargas de FrSky a través del **Centro de descargas**, y usar la radio como proxy para escribir directamente el firmware de un módulo, sensor, servo o receptor.
6. Convertir imágenes y archivos de audio a los formatos nativos de Ethos.
7. Ofrecer **herramientas de desarrollo Lua**: documentación de la API, scripts de demostración y un terminal de depuración.
8. Escribir el bootloader de la radio en modo DFU (conexión con la radio apagada), independientemente de que el firmware de la radio siga funcionando.
9. Reparar el almacenamiento interno de las radios X18/S, TW Lite, XE y X20 Pro/R/RS mediante la **herramienta de reparación**, si la NAND no se puede leer o los ajustes no se guardan.
10. Expulsar de forma segura las unidades de disco de la radio.
11. Avisar al inicio cuando hay disponible una actualización de la propia Suite (se instala al salir).

## Modos de conexión

Además de sus herramientas, la Suite funciona con la radio en tres estados de conexión distintos:

- **Radio en modo bootloader**: la pestaña **Radio** comprueba y actualiza el firmware y los archivos de la memoria flash, de la tarjeta SD o eMMC; el **Gestor de Modelos** realiza o restaura la copia de seguridad de la radio.
- **Radio en modo Ethos**: la Suite usa la radio como proxy (mediante las herramientas **FRSK Flasher**/Centro de descargas) para escribir directamente el firmware del módulo interno o de cualquier sensor, servo o receptor conectado.
- **Radio en modo DFU**: conexión con la radio apagada, empleada por el **DFU Flasher** para escribir el propio bootloader, por ejemplo cuando una corrupción del firmware impide que la radio arranque con normalidad.

Vea [Migración](migration.md) para pasar por primera vez una radio existente a Ethos Suite, y [Funcionamiento](operation.md) para conocer la interfaz de la Suite en sí.
