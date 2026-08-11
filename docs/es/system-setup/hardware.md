---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Comprobación del hardware](../assets/system-hardware-check-x20s.png)

Prueba y calibración de los controles físicos de la emisora, definición del
tipo de interruptores y asignación de las teclas de inicio.

## Comprobación del hardware {: #hardware-check }

Ejercita cada entrada física para que puedas confirmar que todas se
registran correctamente.

![Comprobación del hardware en X20 Pro](../assets/system-hardware-check-x20pro.png)
![Comprobación del hardware en X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — comprueba también los dos pulsadores con enclavamiento
  **K** y **L** situados en los hombros traseros, además de los trims
  adicionales **T5**/**T6**.
- **X18** — comprueba también los trims adicionales **T5**/**T6**.

## Calibración de los analógicos {: #analogs-calibration }

![Calibración de los analógicos](../assets/system-hardware-analogs-calibration.png)

Enseña a la emisora exactamente dónde están el centro y los límites de cada
gimbal, potenciómetro y deslizador. Se ejecuta automáticamente en el primer
arranque; repítela tras sustituir un gimbal, un potenciómetro o un
deslizador.

## Calibración del giróscopo

![Calibración del giróscopo](../assets/system-hardware-gyro-calibration.png)

Calibra el giróscopo integrado para que las entradas basadas en la
inclinación respondan correctamente al inclinar la emisora: la posición
«nivelada» pasa a ser la forma en que normalmente la sujetas. También se
ejecuta automáticamente en el primer arranque.

## Filtro de analógicos

Filtro ADC de activación/desactivación para los sticks, activado por
defecto: reduce las oscilaciones alrededor del centro del stick. Este es el
ajuste **global**; existe además una anulación **por modelo** del filtro de
analógicos en [Edición del modelo](../model-setup/model-edit.md).

## Ajustes de potenciómetros/deslizadores {: #potssliders-settings }

Permite renombrar los potenciómetros y los deslizadores. El **X20 Pro/R/RS**
admite además dos potenciómetros extra, **Ext1**/**Ext2**, empleados
habitualmente para gimbals de 3 ejes.

![Valores ADC, potenciómetros](../assets/system-hardware-pots-x20s.png)
![Valores ADC, potenciómetros (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Ajustes de los interruptores {: #switches-settings }

![Interruptores](../assets/system-hardware-switches.png)

- **Retardo de detección de la posición central** — evita que un cambio
  rápido arriba→abajo (o abajo→arriba) de un interruptor de 3 posiciones
  registre momentáneamente la posición central; la posición central solo
  debería registrarse cuando el interruptor se detiene realmente en ella. El
  valor por defecto es 0 ms, elegido para adaptarse a la detección de
  «autocomprobación» de los receptores estabilizados de FrSky en el CH12.
- **Tipo de interruptor** — cada interruptor SA–SJ puede definirse como
  **None**, **Momentary**, **2 POS** o **3 POS**, lo que permite
  intercambiar funcionalidades entre interruptores físicos (por ejemplo,
  asignar al interruptor momentáneo SH la función que normalmente
  desempeña el SF de 2 posiciones), siempre dentro de lo que el cableado de
  la emisora admita realmente (por lo general no puede asignarse una
  función de 3 posiciones a un hardware que no está cableado para ello).

  ![Opciones de interruptor](../assets/system-hardware-switches-options.png)
  ![Interruptores adicionales](../assets/system-hardware-switches-2.png)

- **Renombrado** — los interruptores pueden renombrarse de SA–SJ a nombres
  personalizados; los nombres son globales para todos los modelos.
- **X20 Pro** — añade los pulsadores **K**/**L** en los hombros traseros,
  además de las posiciones **M**/**N** si están cableadas (normalmente para
  interruptores en el extremo de los sticks).

## Asignación de teclas de inicio

Reasigna el destino al que saltan las teclas de inicio `SYS`, `MDL` y
`DISP` (`TELE` en emisoras más antiguas).

- **`DISP`** — tanto la pulsación corta como la larga pueden reasignarse a
  cualquier página de Modelo, página de Sistema, Configurar pantallas,
  Inicio o el Registro de datos de vuelo. Por coherencia con la serie X10,
  la pulsación larga de `DISP` se ajusta convencionalmente a Configurar
  pantallas.
- **`SYS`/`MDL`** — solo la pulsación larga es reasignable (al mismo
  conjunto de destinos); una pulsación corta abre siempre la sección de
  Sistema o de Modelo, respectivamente.

## Opciones de hardware específicas de cada emisora {: #radio-specific-hardware-options }

- **Activación de mejoras de gimbal háptico** (X20 Pro, X20R) — el X20 Pro AW
  y el X20RS se suministran con gimbals MC20R que incorporan motores de
  vibración («stick-shaker») hápticos; si se han retroadaptado gimbals MC20R
  a un X20 Pro o X20R, actívalos aquí (consulta
  [Funciones especiales](../model-setup/special-functions.md) para
  configurar los propios patrones hápticos).

  ![Háptico (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Háptico (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Opción del encoder** (X20 Pro AW, X20R/RS) — estas emisoras disponen de
  un encoder rotativo más sensible; activa los **medios pasos** para
  atenuarlo.

  ![Opción del encoder (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Inspector de valores ADC {: #adc-value-inspector }

Muestra los valores brutos de la conversión analógico-digital que la CPU lee
para cada entrada analógica:

![Comprobación ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Comprobación ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 stick izquierdo horizontal, 2 stick izquierdo vertical, 3 stick
derecho vertical, 4 stick derecho horizontal, 5 Pot 1, 6 Pot 2, 7 deslizador
central, 8 deslizador izquierdo, 9 deslizador derecho.

**X20 Pro**: igual que lo anterior, pero con dos canales adicionales de
potenciómetros externos (7 Ext1, 8 Ext2 — por ejemplo, potenciómetros
montados en los sticks) insertados antes de los deslizadores, que pasan a
ser 9 deslizador central, 10 deslizador izquierdo, 11 deslizador derecho.
