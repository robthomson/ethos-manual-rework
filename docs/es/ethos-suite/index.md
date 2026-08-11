---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite es la aplicación complementaria para Windows/Mac que permite gestionar una emisora con Ethos, conectada por USB.

!!! note "Capturas de pantalla pendientes"
    Ethos Suite es una aplicación de PC independiente, no la emisora en sí, por lo que esta sección no utiliza las capturas de pantalla obtenidas del simulador que emplea el resto del manual — consulte [Proceso de capturas de pantalla](../contributing/screenshot-pipeline.md).

Una vez conectada, Ethos Suite puede:

1. Leer el tipo de emisora, su ID y las versiones instaladas: firmware, bootloader, módulo de RF interno, archivos de la memoria flash y archivos de la SD card/eMMC.
2. Alternar la emisora entre el modo bootloader y la ejecución de Ethos, y volver atrás.
3. Comparar las versiones instaladas con las actuales y actualizar automáticamente: solo los componentes desactualizados, todo sin excepción, o los componentes de forma individual.
4. Respaldar los modelos en disco mediante el **Model Manager**, o restaurar una copia de seguridad anterior (necesario porque los archivos de modelo no son retrocompatibles entre versiones de firmware).
5. Descargar cualquier firmware desde el sitio de descargas de FrSky a través del **Download center**, y usar la emisora como intermediario para actualizar directamente un módulo, sensor, servo o receptor.
6. Convertir imágenes y archivos de audio a los formatos nativos de Ethos.
7. Ofrecer **herramientas de desarrollo Lua**: documentación de la API, scripts de demostración y un terminal de depuración.
8. Actualizar el bootloader de la emisora en modo DFU (conexión con la emisora apagada), con independencia de que el firmware de la emisora siga funcionando.
9. Reparar el almacenamiento interno en las emisoras X18/S, TW Lite, XE y X20 Pro/R/RS mediante el **Repair Tool**, si la NAND no se puede leer o los ajustes no se guardan.
10. Expulsar de forma segura las unidades USB de la emisora.
11. Avisar al inicio cuando hay disponible una actualización de la propia Suite (se instala al salir).

## Modos de conexión

Además de sus herramientas, Suite funciona con la emisora en tres estados de conexión distintos:

- **Emisora en modo bootloader**: la pestaña **Radio** comprueba y actualiza el firmware y los archivos de la flash/SD card/eMMC; el **Model Manager** respalda o restaura la emisora.
- **Emisora en modo Ethos**: Suite utiliza la emisora como intermediario (mediante las herramientas **FRSK Flasher**/Download center) para actualizar directamente el módulo interno o cualquier sensor, servo o receptor conectado.
- **Emisora en modo DFU**: conexión con la emisora apagada, empleada por el **DFU Flasher** para actualizar el propio bootloader, por ejemplo cuando una corrupción del firmware impide que la emisora arranque con normalidad.

Consulte [Migración](migration.md) para trasladar por primera vez una emisora existente a Ethos Suite, y [Funcionamiento](operation.md) para conocer la interfaz de Suite en sí.
