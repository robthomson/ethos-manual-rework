---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Encontrar el bootloader más reciente u otro componente

Las versiones publicadas del firmware Ethos incluyen un archivo `components.json` que enumera la versión actual de cada componente para cada emisora, lo que resulta útil para confirmar si una determinada versión de bootloader/firmware/audio/archivos de sistema es realmente la actual antes de instalarla.

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas de pantalla del simulador; consulte [Flujo de trabajo de capturas de pantalla](../contributing/screenshot-pipeline.md).

1. Descargue `components.json` de la última versión de Ethos.
2. Ábralo en un editor de texto (VS Code, Notepad, etc.).
3. Localice la sección correspondiente a su emisora, por ejemplo `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (Se trata de un ejemplo puntual: consulte siempre el archivo de la versión *actual* para obtener los números de versión reales).

4. Consulte la versión del componente que necesite; en el ejemplo anterior, el último bootloader para la familia X20 es `1.4.15`.

Consulte [Gestor de archivos](../system-setup/file-manager.md#top-level-folders) para saber dónde colocar el archivo de firmware descargado, y [Modos de conexión USB](../getting-started/usb-connection-modes.md#bootloader-mode) para poner la emisora en modo bootloader e instalarlo; o bien utilice [Ethos Suite](../ethos-suite/index.md), que se encarga automáticamente de comprobar las versiones y realizar la instalación.
