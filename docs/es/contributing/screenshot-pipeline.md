---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Flujo de generación de capturas de pantalla

Todas las capturas de pantalla de este manual (actualmente ~590, en
`docs/en/assets/`) se obtuvieron mediante scripts que controlan el simulador real
de Ethos, no de forma manual. El sistema reside en el antiguo repositorio
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), en
`english/manual/`, y **todavía no se ha trasladado a este repositorio** — esta
página documenta su funcionamiento para que pueda trasladarse, y para que
mientras tanto las capturas puedan regenerarse o ampliarse sin empezar de cero.

## Cómo está estructurado

Para cada menú/sección del manual existe un par de archivos:

- `manual/macros/<name>.lua` — un script escrito contra la API Lua del
  simulador (más abajo) que navega hasta una pantalla concreta y llama a
  `simulator.screenshot(path)` en cada punto que merece capturarse.
- `manual/<name>.sh` — un envoltorio de una sola línea que lanza el binario del
  simulador para una emisora concreta, apuntando a esa macro, por ejemplo:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` ejecuta todas las macros en secuencia para regenerar el
conjunto completo. Existen archivos `.sh` individuales por sección, de modo que
las capturas de una sola página puedan regenerarse sin volver a ejecutarlo todo
(cada macro tarda desde unos pocos segundos hasta más de un minuto).

Opciones CLI principales:

- `--read-only` — no conservar ningún cambio realizado durante la ejecución.
- `--no-gui` / `--no-audio` — modo casi sin interfaz; algunas macros aún
  necesitan la GUI porque, sin ella, el simulador «se salta» pasos (véase el
  comentario en `screenshots.sh`).
- `--radio-settings <file>.bin` — con qué ajustes guardados de emisora arrancar
  (esto es lo que hace que las capturas sean específicas de un idioma y una
  emisora — una ejecución en alemán usa un `.bin` en alemán).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — indican al simulador qué modelos/firmware/documentos/audio
  debe ver, de forma que las capturas reflejen contenido preparado
  deliberadamente y no lo que haya en una SD card real.
- `--exec <script>.lua` — la macro que se ejecutará tras el arranque.

Cada familia de emisoras (X20S, X20 Pro, X20 Pro AW, X18S) tiene su propio
binario de simulador y necesita su propio archivo `--radio-settings` por idioma
(por ejemplo, `x20s-en.bin`, `x20pro-en.bin`), ya que la interfaz difiere
ligeramente entre emisoras y el archivo de ajustes también determina el idioma.

## La API de macros

Las macros son Lua puro y controlan una variable global `simulator`:

| Llamada | Finalidad |
|---|---|
| `simulator.loadModel("name.bin")` | Cargar un archivo de modelo concreto antes de navegar — cada sección del manual usa un modelo preparado para demostrar esa sección (véase la lista de modelos más abajo). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Pulsar una tecla física — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE`, etc. Una duración de mantenimiento provoca una pulsación larga (abre menús contextuales). |
| `simulator.turnRotaryEncoder(n)` | Mover el encoder `n` clics (negativo = sentido inverso) — la forma principal de desplazar el cursor entre campos. |
| `simulator.touch(x, y)` | Tocar una coordenada concreta de la pantalla — se usa donde el táctil es la única forma de llegar a algo (por ejemplo, cambiar la distribución del teclado). |
| `simulator.setAnalog(channel, value)` | Fijar directamente la posición de un stick/potenciómetro/deslizador (`0`-`3` son los cuatro sticks principales, `ANALOG_LAST_SLIDER` el último deslizador), de modo que las capturas muestren un valor deliberado y reproducible en lugar del valor por defecto del simulador. |
| `simulator.setSwitch(n, position)` | Fijar la posición de un interruptor físico. |
| `simulator.setDateTime({...})` | Fijar el reloj del simulador, de modo que las marcas de tiempo de las capturas (y cualquier elemento dependiente del tiempo) sean reproducibles entre ejecuciones. |
| `simulator.screenshot(path)` | Capturar la pantalla actual en un PNG, con ruta relativa al directorio de trabajo de la macro (de ahí las rutas `../assets/...` dentro de cada macro). |
| `simulator.connectUsb()` | Simular la conexión por USB, para capturar el menú USB. |
| `simulator.sleep(seconds)` | Esperar a que una animación o un valor de telemetría se estabilice antes de capturar. |

`manual/macros/common.lua` se carga con `dofile` desde la mayoría de las macros y
simplemente fija la fecha y la hora, de modo que todas las macros parten del
mismo instante simulado.

## Modelos usados por sección

`manual/notes.txt` (heredado de manera informal, aún no copiado a este
repositorio) relaciona cada macro con el archivo de modelo `.bin` del que
depende y por qué — por ejemplo, `model-mixes.lua` usa `rarebear.bin`,
`model-fm.lua` usa `zblank.bin` (un modelo con una configuración de fases de
vuelo deliberadamente vacía), `model-trims.lua` usa `blaster.bin` (configurado
con trims desplazados para demostrar el rango de trim). Trasladar las notas de
este archivo a documentación propia aquí forma parte del trabajo de la fase 2
descrito más abajo.

## Qué implica trasladar esto al nuevo repositorio (aún sin hacer)

- Decidir si las macros se ejecutan directamente desde este repositorio
  (lo que requiere una instalación local del simulador de Ethos, como hacía el
  repositorio antiguo) o mediante CI con el simulador incluido o descargado en
  el flujo de trabajo.
- Reestructurar las rutas de salida planas `../assets/...` para que coincidan con
  la organización de recursos por página y por idioma de este repositorio
  (`docs/<locale>/assets/`).
- Un archivo `--radio-settings ... .bin` y una ejecución de capturas por idioma,
  en cuanto exista un idioma distinto de `en` — las capturas son específicas del
  idioma de la interfaz y no pueden compartirse entre idiomas.
- Decidir qué parte de las ~40 macros existentes se traslada tal cual y qué
  parte se reescribe conforme a la estructura de navegación actual de este
  repositorio (algunas macros producen capturas para secciones que ya no se
  corresponden 1:1 con la organización de páginas de este manual).
