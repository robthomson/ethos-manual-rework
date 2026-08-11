---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Scripts Lua

Los scripts Lua permiten crear [widgets de pantalla personalizados](../displays/custom-widgets.md)
para mostrar información que Ethos no cubre de forma nativa y, por modelo,
[fuentes y tareas personalizadas](../model-setup/lua-scripts.md) — una base que
está previsto ampliar aún más, hacia funciones personalizadas especializadas y
la integración con controladoras de vuelo.

Lua es, en sí mismo, un lenguaje de programación de propósito general ligero e
integrable (utilizado en todo tipo de entornos, desde videojuegos hasta
aplicaciones web); Ethos lo integra precisamente para este tipo de
personalización en la emisora.

!!! warning
    Los scripts Lua aumentan el tiempo de arranque de la emisora. El retardo de
    un script bien escrito debería ser imperceptible; uno mal escrito puede
    retrasar el arranque casi indefinidamente.

- [Intérprete Lua](lua-interpreter.md) — qué versión de Lua y qué bibliotecas
  integra Ethos.
- [Documentación Lua de Ethos](ethos-lua-documentation.md) — dónde se encuentra
  la referencia completa de la API.
- [Ubicación de scripts de ejemplo](example-script-locations.md) — dónde
  encontrar y descargar ejemplos funcionales.
- [Límites de configuración](configuration-limits.md) — presupuestos de memoria
  para mapas de bits y scripts.
- [Estructura básica de un widget](basic-widget-layout.md) — la estructura de
  código que necesita un script de widget personalizado.
