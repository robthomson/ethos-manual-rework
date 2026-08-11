---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Comprobación del hardware](../assets/system-hardware-check-x20s.png)

Comprobación y calibración de los controles físicos de la emisora, definición
del tipo de interruptores y asignación de las teclas de inicio.

## Comprobación del hardware {: #hardware-check }

Permite accionar cada entrada física para confirmar que todas se registran
correctamente.

![Comprobación del hardware en X20 Pro](../assets/system-hardware-check-x20pro.png)
![Comprobación del hardware en X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — comprueba también los dos pulsadores con enclavamiento
  **K** y **L** situados en los hombros traseros, además de los
  compensadores adicionales **T5**/**T6**.
- **X18** — comprueba también los compensadores adicionales **T5**/**T6**.

## Calibración de los analógicos {: #analogs-calibration }

![Calibración de los analógicos](../assets/system-hardware-analogs-calibration.png)

Indica a la emisora exactamente dónde están el centro y los límites de cada
gimbal, pot y slider. Se ejecuta automáticamente en el primer arranque;
repítala después de sustituir un gimbal, un pot o un slider.

## Calibración del giróscopo

![Calibración del giróscopo](../assets/system-hardware-gyro-calibration.png)

Calibra el giróscopo interno para que las entradas basadas en la inclinación
respondan correctamente al inclinar la emisora: la posición «nivelada» pasa a
ser la forma en que usted la sujeta normalmente. También se ejecuta
automáticamente en el primer arranque.

## Filtro de analógicos

Filtro ADC para las palancas, que se puede activar o desactivar y que viene
activado por defecto: reduce las oscilaciones alrededor del centro de la
palanca. Este es el ajuste **global**; existe además un filtro de analógicos
**por modelo** que lo sustituye, en
[Edición del modelo](../model-setup/model-edit.md).

## Ajustes de pots/sliders {: #potssliders-settings }

Permite renombrar los pots y los sliders. Las emisoras **X20 Pro/R/RS**
admiten además dos pots extra, **Ext1**/**Ext2**, empleados habitualmente
para gimbals de 3 ejes.

![Valores ADC, pots](../assets/system-hardware-pots-x20s.png)
![Valores ADC, pots (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Ajustes de los interruptores {: #switches-settings }

![Interruptores](../assets/system-hardware-switches.png)

- **Retardo de detección de la posición central** — evita que un cambio
  rápido de arriba→abajo (o de abajo→arriba) en un interruptor de 3
  posiciones registre momentáneamente la posición central; la posición
  central solo debería registrarse cuando el interruptor se detenga
  realmente en ella. El valor por defecto es 0 ms, elegido para adaptarse a
  la detección de «autocomprobación» de los receptores estabilizados de
  FrSky en el CH12.
- **Tipo de interruptor** — cada interruptor SA–SJ puede definirse como
  **None**, **Momentary**, **2 POS** o **3 POS**, lo que permite
  intercambiar funcionalidades entre interruptores físicos (por ejemplo,
  asignar al interruptor momentáneo SH la función que normalmente
  desempeña el SF de 2 posiciones), siempre dentro de lo que el cableado de
  la emisora admita realmente (por lo general no puede asignarse una
  función de 3 posiciones a un hardware que no está cableado para ello).

  ![Opciones de interruptor](../assets/system-hardware-switches-options.png)
  ![Interruptores adicionales](../assets/system-hardware-switches-2.png)

- **Renombrado** — los interruptores se pueden renombrar de SA–SJ a nombres
  personalizados; los nombres son globales para todos los modelos.
- **X20 Pro** — añade los pulsadores **K**/**L** en los hombros traseros,
  además de las posiciones **M**/**N** si están cableadas (normalmente para
  interruptores en el extremo de las palancas).

## Asignación de teclas de inicio

Reasigna el destino al que saltan las teclas de inicio `SYS`, `MDL` y
`DISP` (`TELE` en emisoras más antiguas).

- **`DISP`** — tanto la pulsación corta como la larga se pueden reasignar a
  cualquier página de Modelo, página de Sistema, Configurar pantallas,
  Inicio o al Registro de datos de vuelo. Por coherencia con la serie X10,
  la pulsación larga de `DISP` se suele configurar en Configurar pantallas.
- **`SYS`/`MDL`** — solo la pulsación larga es reasignable (al mismo
  conjunto de destinos); una pulsación corta abre siempre la sección de
  Sistema o de Modelo, respectivamente.

## Opciones de hardware específicas de cada emisora {: #radio-specific-hardware-options }

- **Habilitar actualización para vibración en los gimbal** (X20 Pro, X20R) —
  las emisoras X20 Pro AW y X20RS se suministran con gimbals MC20R que
  incorporan motores de vibración háptica en las palancas; si se han
  instalado gimbals MC20R en una X20 Pro o una X20R, actívelos aquí (vaya a
  la sección [Funciones especiales](../model-setup/special-functions.md)
  para configurar los propios patrones de vibración háptica).

  ![Vibración háptica (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Vibración háptica (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Opción del encoder** (X20 Pro AW, X20R/RS) — estas emisoras disponen de
  un selector rotatorio más sensible; active los **medios pasos** para
  suavizarlo.

  ![Opción del encoder (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Inspector de valores ADC {: #adc-value-inspector }

Muestra los valores brutos de la conversión analógico-digital que la CPU lee
para cada entrada analógica:

![Comprobación ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Comprobación ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 palanca izquierda horizontal, 2 palanca izquierda vertical, 3
palanca derecha vertical, 4 palanca derecha horizontal, 5 Pot 1, 6 Pot 2, 7
slider central, 8 slider izquierdo, 9 slider derecho.

**X20 Pro**: igual que lo anterior, pero con dos canales adicionales de pots
externos (7 Ext1, 8 Ext2 — por ejemplo, pots montados en las palancas)
insertados antes de los sliders, que pasan a ser 9 slider central, 10 slider
izquierdo, 11 slider derecho.
