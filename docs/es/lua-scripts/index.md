---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua Scripts

Los scripts Lua permiten crear [widgets personalizados](../displays/custom-widgets.md)
para mostrar información que Ethos no contempla de forma nativa y, para cada
modelo, [fuentes y tareas personalizadas](../model-setup/lua-scripts.md) — una
base que está previsto ampliar en el futuro hacia funciones especializadas para
tareas personalizadas y la interacción con controladores de vuelo.

El lenguaje de programación Lua es un lenguaje ligero e integrable diseñado para
todo tipo de aplicaciones, desde juegos hasta aplicaciones web, y en este caso
para implementar funciones personalizadas en la radio.

!!! warning
    Tenga en cuenta que los scripts Lua aumentan el tiempo de arranque de la
    radio. Si están bien implementados, el retraso no debería ser perceptible,
    pero si no es el caso, el retraso puede ser casi indefinido.

- [Intérprete Lua](lua-interpreter.md) — qué versión de Lua y qué librerías
  integra Ethos.
- [Documentación Lua de Ethos](ethos-lua-documentation.md) — dónde se encuentra
  la referencia completa de la API.
- [Ubicación de los scripts de ejemplo](example-script-locations.md) — dónde
  encontrar y descargar ejemplos que funcionan.
- [Límites de configuración](configuration-limits.md) — la memoria disponible
  para mapas de bits y scripts.
- [Diseño básico de un widget](basic-widget-layout.md) — la estructura de código
  que necesita un script de widget personalizado.
