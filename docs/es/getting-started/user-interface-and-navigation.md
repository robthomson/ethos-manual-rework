---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Interfaz de usuario y navegación

Ethos puede manejarse por completo con el **selector rotatorio** de la derecha
(gírelo para mover el remarcado, presiónelo para `ENT`) y la tecla `RTN` para
salir de un menú: la pantalla táctil, en las radios que la incorporan, es un
atajo para las mismas acciones, no una forma de trabajo distinta. `MDL`,
`DISP` y `SYS` acceden directamente a Configuración del modelo, Configurar
pantallas y Configuración del sistema respectivamente (los mismos tres
cuadrados de la barra inferior); una pulsación larga de `RTN` desde cualquier
lugar devuelve directamente a la pantalla de inicio.

## El menú de reinicio

![Menú contextual](../assets/resetmenu.png)

Una pulsación larga de `ENT` desde la pantalla de inicio abre un menú de
reinicio:

- **Reset flight** — reinicia la telemetría, los cronómetros y los
  interruptores de función, y vuelve a ejecutar la [lista de
  comprobación](../model-setup/checklist.md) previa al vuelo.
- **Reset telemetry** — reinicia únicamente la telemetría.
- **Reset timers** — reinicia únicamente los cronómetros.
- **Lock touchscreen** — también accesible presionando `ENT` + `PAGE`
  simultáneamente durante un segundo desde la pantalla de inicio, o como
  disparador de una [función
  especial](../model-setup/special-functions.md).

## Controles de edición

**Añadir elementos funcionales** — pueden crearse nuevos elementos
funcionales, como cronómetros, interruptores lógicos, funciones especiales,
curvas o variables, seleccionando el símbolo **+** situado junto a la cabecera
de la columna del menú correspondiente. En las radios sin pantalla táctil,
seleccione un elemento existente, presione `ENT` y elija **Add** en el diálogo
que se habrá abierto; por supuesto, esta forma de hacerlo también funciona en
las radios con pantalla táctil.

### Teclado virtual

![Teclado de texto](../assets/keyboard-text-azerty.png)

Basta con tocar cualquier campo de texto (o presionar `ENT` sobre él) para que
aparezca el teclado en pantalla. La tecla de borrado hacia atrás borra los
caracteres a la izquierda del cursor; `PAGE` borra los caracteres a la derecha
del cursor y, una vez que se llega al final del texto, empieza a borrar los
restantes que estén a la izquierda. Toque el propio campo de texto para mover
el cursor a la posición deseada; alternativamente, use `SYS`/`DISP` para
moverlo hacia la izquierda o hacia la derecha sin pantalla táctil. La tecla
**?123**/**abc** alterna con el teclado numérico, que también incluye
caracteres especiales:

![Teclado numérico](../assets/keyboard-text-numbers.png)

En las **radios sin pantalla táctil**, presione `ENT` en un campo de texto
para entrar directamente en el modo de edición: rote el selector rotatorio
para moverse a través de las minúsculas, las mayúsculas y los números,
seguidos de los caracteres especiales, y presione `ENT` para insertar cada
carácter. `MDL` cambia la caja del carácter que esté inmediatamente a la
derecha del cursor (y cualquier carácter que se introduzca a partir de ahí
mantendrá ese estado hasta que se cambie de nuevo). `PAGE` borra los
caracteres a la derecha del cursor; `SYS`/`DISP` mueven el cursor hacia la
izquierda o hacia la derecha.

## Controles de valores numéricos

![Introducción de números](../assets/keyboard-numbers.png)

Al tocar un campo que contenga un valor numérico, aparece en la parte de abajo
de la pantalla un cuadro de diálogo con controles: las teclas **`<`**/**`>`**
cambian el tamaño de cada paso (en decimales, por ejemplo 0,01/0,1/1,0/10,0),
las teclas **`-`**/**`+`** (o el selector rotatorio) incrementan o reducen el
valor en función del tamaño del paso, y **More** proporciona opciones
adicionales:

![Opciones de introducción de números](../assets/keyboard-numbers-options.png)

- El valor por defecto del campo
- Ajuste al mínimo / ajuste al máximo
- Reemplazar los controles con un **slider**

![Introducción con deslizador](../assets/keyboard-numbers-slider.png)

El slider (que también se puede ajustar con el selector rotatorio) permite
ajustar los valores más rápidamente; **Disable slider** vuelve a los controles
de ajuste normales. Los valores de Rango de Telemetría se editan de forma
similar:

![Deslizador desactivado](../assets/keyboard-numbers-options-disable-slider.png)

## La característica Options {: #the-options-feature }

Casi en cualquier lugar en el que se espere introducir un valor o una
[fuente](#choosing-a-source), una pulsación larga de `ENT` hará aparecer un
cuadro de diálogo de **Options**: los campos con esta función se identifican
por el pequeño icono de menú (símbolo de hamburguesa) en la esquina superior
izquierda del campo.

### Opciones con valor

![Opciones de fuente](../assets/source-with-options.png)

El cuadro de diálogo para Opciones con valor muestra qué parámetro se está
configurando y ofrece la opción de configurarlo al mínimo o al máximo, o bien
utilizar una **fuente** (por ejemplo, un pot, lo que permitiría ajustar el
valor en vuelo). Si mantiene pulsado en un campo que ya ha sido modificado
para utilizar una fuente, aparecerá en su lugar un cuadro de diálogo que le
permitirá convertir el valor actual de la fuente en un valor fijo:

![Convertir fuente en valor](../assets/source-convert-to-value.png)

### Elegir una fuente {: #choosing-a-source }

Al seleccionar **Choose a source** se abre un selector de dos columnas:
primero una **categoría** (analógicos, interruptores, interruptores lógicos,
compensadores, canales, un eje del giróscopo, un canal de entrenador, un
cronómetro, un sensor de telemetría o un puñado de valores especiales) y
después el elemento concreto dentro de ella:

![Menú de fuentes](../assets/source-menu.png)

Una vez definida la fuente, la misma pulsación larga abre opciones específicas
según el tipo de fuente:

**Cualquier fuente** —

- **Invert** — permite negar o invertir la fuente (por ejemplo, estaría activa
  cuando el interruptor *no* está arriba, en lugar de cuando sí lo está).
- **Edge** — efectúa una única acción cuando la fuente pasa de Falso a
  Verdadero o de Verdadero a Falso, en lugar de actuar sobre todo el estado;
  un símbolo `†` aparecerá delante de la fuente. Estará disponible en los
  interruptores en general y, en particular, en la condición de activación del
  [interruptor lógico Sticky](../model-setup/logical-switches.md).

**Fuentes de palanca** — opciones de tipo calibración/subtrim:

![Opciones de fuente de palanca](../assets/source-stick-options.png)

**Opciones de fuentes para interruptores** —

![Opciones de interruptor de 2 posiciones](../assets/source-2pos-options.png)
![Opciones de interruptor](../assets/switch-options.png)

- **Negative** — la opción negativo permite invertir la acción del
  interruptor.
- **HalfRange** — estará disponible cuando se use un interruptor de 2
  posiciones o un interruptor lógico como fuente: el movimiento será de
  0–100 % en lugar de ±100 %.

**Fuentes de compensador** —

![Opciones de fuente de compensador](../assets/source-trim-options.png)

- **Negative** — permite invertir la acción del compensador, útil en las
  mezclas con Actions.
- **Full range** — los compensadores tienen un régimen de movimiento por
  defecto de ±25 %; cuando se seleccionan como fuente, se pueden cambiar para
  que tengan un recorrido total de ±100 %.
- **Ignore trainer input** — en un [interruptor
  lógico](../model-setup/logical-switches.md), las fuentes pueden tener esta
  opción configurada para ignorar las fuentes procedentes de la entrada del
  alumno. Una aplicación típica es cuando se configura un interruptor lógico
  para que detecte el movimiento de las palancas del maestro (por ejemplo,
  para permitir la intervención instantánea si las cosas van mal) sin que las
  entradas de palanca del alumno activen el interruptor lógico.

**Fuentes de variable** —

![Opciones de fuente de variable](../assets/source-var-options.png)

- **Negative** — convierte el valor del Var a negativo para esa selección.
- **Ignore range** — algunos parámetros tienen rangos asimétricos, como los
  parámetros Mín/Max en las Salidas, que tienen márgenes de −150 % a 0 % y de
  0 % a +150 % respectivamente. A menos que la
  [variable](../model-setup/variables.md) usada como fuente de ese campo tenga
  unos márgenes idénticos, active esta opción para que se ignoren y así evitar
  valores inesperados debidos a la conversión de esos márgenes.

**Fuentes de sensor de telemetría** — en una fuente de Telemetría, el cuadro
de diálogo de Opciones permite utilizar los valores máximo o mínimo del sensor
en lugar de la lectura instantánea (algunos sensores tendrán opciones
adicionales específicas para ese sensor):

![Opciones de mínimo/máximo del sensor](../assets/source-sensor-options.png)
![Máximo del sensor seleccionado](../assets/source-sensor-maxi.png)
