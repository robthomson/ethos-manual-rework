---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Estructura básica de un widget

Un widget Lua personalizado (consulte [Widgets personalizados](../displays/custom-widgets.md)
para instalar uno) se construye a partir de un pequeño conjunto de campos/manejadores con nombre:

- **`key`** *(cadena)* — un identificador único para el widget.
- **`name`** *(cadena o función)* — el nombre visible del widget. Puede ser una
  cadena simple o una función que no recibe argumentos y devuelve una —
  útil para un nombre que varíe según el idioma.
- **`create`** *(función)* — se llama una única vez cuando se crea el widget,
  sin recibir argumentos. Devuelve una **tabla del widget**, que a su vez se pasa
  a todos los demás manejadores descritos a continuación — inicialice aquí su estado y almacénelo
  en esa tabla.
- **`configure`** *(función)* — se llama cuando el usuario abre la pantalla de
  configuración del widget, recibiendo como único argumento la tabla del widget devuelta por
  `create()` y sin devolver nada. Construya aquí el formulario de configuración y
  utilícelo para actualizar los valores de la tabla del widget.
- **`wakeup`** *(función)* — se llama en cada ciclo (aproximadamente cada 50 ms),
  recibiendo la tabla del widget y sin devolver nada. Compruebe aquí si algo
  ha cambiado; en tal caso, llame a `invalidateWindow()` para provocar un repintado mediante
  `paint()`. Mantenga este manejador rápido — idealmente sin hacer nada en absoluto la mayoría
  de las veces que se le llama.
- **`event`** *(función)* — se llama cuando el widget recibe un evento;
  Ethos encamina eventos arbitrarios hacia el widget a través de este manejador.
- **`paint`** *(función)* — dibuja el widget, recibiendo la tabla del widget y
  sin devolver nada. Se llama automáticamente siempre que se haya disparado `lcd.invalidate()`.
  Puede ser comparativamente lento, pero aun así solo debería redibujar realmente
  cuando algo haya cambiado.
- **`read`** *(función, opcional)* — lee el almacenamiento persistente del widget.
- **`write`** *(función, opcional)* — escribe el almacenamiento persistente del widget.
- **`init`** *(función)* — registra el widget y sus retrollamadas en
  Ethos. Normalmente es lo último del script:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` debe ser único entre todos los widgets instalados; los demás campos se
integran en el ciclo de vida del widget tal como se describe más arriba.

Los scripts se ubican en `scripts/` en la SD card/eMMC, idealmente organizados en
carpetas por widget (consulte [Gestor de archivos](../system-setup/file-manager.md#top-level-folders) y [Ubicaciones
de ejemplo para scripts](example-script-locations.md)). Consulte el hilo *FrSky ETHOS Lua
Script Programming* en rcgroups para más ejemplos desarrollados.
