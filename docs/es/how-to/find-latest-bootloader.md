---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Encontrar el bootloader más reciente u otro componente

Las versiones publicadas del firmware de Ethos incluyen un archivo `components.json` que indica la versión actual de cada componente para cada radio, lo que resulta útil para confirmar si una determinada versión del bootloader, del firmware, de los archivos de audio o de los archivos de sistema está realmente actualizada antes de escribirla en la radio.

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas de pantalla del simulador; vea [Flujo de trabajo de capturas de pantalla](../contributing/screenshot-pipeline.md).

1. Descargue el archivo `components.json` de la última versión de Ethos.
2. Ábralo en un editor de texto (VS Code, Notepad, etc.).
3. Busque la sección correspondiente a su radio, por ejemplo `X20`:

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

   (Se trata de un ejemplo puntual: consulte siempre el archivo de la versión *actual* para conocer los números de versión reales).

4. Lea la versión del componente que necesite; en el ejemplo anterior, el bootloader más reciente para la familia X20 es el `1.4.15`.

Vea la sección [Gestor de archivos](../system-setup/file-manager.md#top-level-folders) para saber dónde colocar el archivo de firmware descargado, y [Modos de conexión USB](../getting-started/usb-connection-modes.md#bootloader-mode) para poner la radio en modo bootloader y actualizarla; o bien utilice [Ethos Suite](../ethos-suite/index.md), que se encarga automáticamente de comprobar las versiones y de escribir el firmware.
