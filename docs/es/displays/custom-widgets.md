---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widgets personalizados

Además de los [tipos de widget integrados](index.md), los scripts Lua pueden implementar
widgets totalmente personalizados: normalmente se trata de un único archivo `main.lua` alojado en una
subcarpeta cuyo nombre indica su función.

## Cómo instalar uno

Copie la subcarpeta del widget en `scripts/` de la SD card/eMMC (véase
[Gestor de archivos](../system-setup/file-manager.md#top-level-folders)). El widget
se registra automáticamente en el siguiente arranque y, a partir de ese momento,
aparece en el selector de categorías **Cambiar widget** de [Configurar
pantallas](additional-displays.md) junto a los tipos integrados, y se configura
exactamente de la misma forma.

## Cómo crear uno

Vaya a [Scripts Lua → Estructura básica de un widget](../lua-scripts/basic-widget-layout.md)
para conocer la estructura de código que debe implementar el script de un widget.
