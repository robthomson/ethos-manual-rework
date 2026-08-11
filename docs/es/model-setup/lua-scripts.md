---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Scripts Lua (Modelo)

![Configuración de Lua](../assets/model-lua-config.png)

Este menú solo aparece una vez que se ha instalado un script Lua de
**fuente** o de **tarea** en la carpeta `scripts/` de la SD card/eMMC
(consulte [Gestor de
archivos](../system-setup/file-manager.md#top-level-folders)): sirve para
activar y configurar dichos scripts **por modelo**, no para instalarlos.
Una vez instalada, una fuente o una tarea está disponible de forma global
para todos los modelos; en esta página es donde cada modelo la habilita y
establece su propia configuración. En el sitio de la
Ethos-Feedback-Community se publican ejemplos de scripts de fuente y de
tarea (`/lua/examples/task`, `/lua/examples/source`).

## Tareas Lua

Todas las tareas instaladas aparecen listadas con un conmutador de
activación por modelo. Al activar una de ellas se despliega su formulario
de configuración (si lo tiene): el script de la tarea proporciona sus
propias funciones de lectura/escritura, de modo que cada modelo puede
guardar sus propios ajustes. Por ejemplo, una tarea puede ofrecer un
rango numérico configurable que se establece de forma independiente en
cada modelo.

## Fuentes Lua

El mismo esquema se aplica a las fuentes: se activan por modelo y después
se configuran mediante el formulario que proporcione el script de la
fuente. Una fuente registrada de este modo pasa a estar disponible como
una
[fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source)
normal en cualquier otra parte de Ethos, exactamente igual que una
integrada.

## Para autores de scripts

Las fuentes y las tareas se registran desde Lua mediante
`system.registerSource()` y `system.registerTask()`: consulte la Ethos
Lua Reference Guide y el apartado [Scripts
Lua](../lua-scripts/index.md) de este manual para conocer el entorno
general de programación de scripts (los widgets son un mecanismo
distinto, aunque relacionado; consulte [Widgets
personalizados](../displays/custom-widgets.md)).
