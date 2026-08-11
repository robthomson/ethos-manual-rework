---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migración

Traslado de una emisora desde las antiguas herramientas de actualización
independientes para PC a Ethos Suite, por primera vez.

1. **Confirme que la versión de Ethos sea ≥ 1.1.4** — la versión mínima capaz de
   grabar el nuevo bootloader compatible con Suite (formato FRSK) directamente
   desde el [Administrador de archivos](../system-setup/file-manager.md).
   Actualice manualmente a 1.1.4 primero si es necesario.
2. **Haga una copia de seguridad de la SD card/eMMC** — copie todo el contenido a
   una carpeta en un PC.
3. **Descargue el bootloader más reciente** desde
   [las publicaciones de ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   y descomprímalo. Cada publicación incluye un archivo `components.json` que
   indica la versión actual de cada componente — consulte [Guía práctica:
   Encontrar el bootloader más reciente](../how-to/find-latest-bootloader.md)
   para saber cómo interpretarlo.
4. Busque la emisora en la entrada `targets` de ese archivo para conocer la
   versión exacta de bootloader que debe utilizar, y localice el archivo
   correspondiente entre los recursos de esa publicación.
5. Arranque la emisora en [modo bootloader](../getting-started/usb-connection-modes.md#bootloader-mode)
   (mantenga pulsado `ENT` y luego encienda) y conéctela por USB.
6. Copie el archivo del bootloader a la SD card/eMMC (normalmente en
   `Firmware/`), luego expulse las unidades y desconecte.
7. Inicie la emisora con normalidad, vaya a **System → File Manager**, toque el
   archivo `bootloader.frsk` que acaba de copiar y seleccione **Flash bootloader**.
8. Descargue e instale Ethos Suite — [Funcionamiento](operation.md) explica cómo
   actualizar el firmware y los archivos, así como el resto de las funciones de
   Suite a partir de este punto.
9. Si Ethos Suite no lo hace automáticamente, puede ser necesario renombrar la
   carpeta `bitmaps/user` de la SD card/eMMC como `bitmaps/models` (que es donde
   se almacenan los bitmaps de modelos del usuario).
