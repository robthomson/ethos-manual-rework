---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widgets personalizados

Más allá de los [tipos de widget integrados](index.md), los scripts Lua pueden implementar
widgets completamente personalizados; normalmente se trata de un único archivo `main.lua` alojado en una
subcarpeta cuyo nombre indica su función.

## Instalación

Copie la subcarpeta del widget en `scripts/` de la SD card/eMMC (consulte
[Gestor de archivos](../system-setup/file-manager.md#top-level-folders)). El widget
se registra automáticamente en el siguiente arranque y, a partir de entonces,
aparece en el selector de categorías **Cambiar widget** de [Configurar
pantallas](additional-displays.md) junto a los tipos integrados, y se configura
exactamente de la misma manera.

## Creación

Consulte [Scripts Lua → Estructura básica de un widget](../lua-scripts/basic-widget-layout.md)
para conocer la estructura de código que debe implementar un script de widget.
