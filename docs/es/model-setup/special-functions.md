---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Funciones especiales

![Menú de funciones especiales](../assets/model-sf-menu.png)

Las Funciones Especiales disparan una acción —reproducir audio, hacer una
captura de pantalla, escribir registros, vibración háptica y más— cuando se
cumple una condición. Se admiten hasta 100 y no hay ninguna por defecto.
Pulse **+** para añadir una; toque una ya existente para
**Editar**/**Mover**/**Copiar-pegar**/**Clonar**/**Eliminar**.

![Añadir función especial](../assets/model-sf-add.png)
![Mover](../assets/model-sf-move.png)

## Campos comunes a todas las acciones

- **Estado** — activa o desactiva esta Función Especial sin eliminarla.
- **Condición activa** — **Siempre encendida**, o activada por posiciones de
  interruptores, interruptores de función, interruptores lógicos, posiciones
  de compensado o modos de vuelo. Si mantiene pulsado `ENT` sobre el nombre
  del interruptor y marca la casilla **Negativa**, el valor se invierte (por
  ejemplo, `SG-up` pasa a `!SG-up`, activo siempre que SG *no* esté en la
  posición arriba).
- **Global** — añade esta función a **todos** los modelos existentes y a
  cualquier modelo nuevo que se cree en el futuro. Si un modelo existente ya
  tiene la función, la función Global se añade como una nueva entrada; al
  desactivar Global en cualquier modelo, la función se elimina de todos los
  modelos excepto del modelo actual seleccionado. Las funciones especiales
  globales se almacenan en `radio.bin`, mientras que las normales se
  almacenan en el archivo del modelo.

## Acciones {: #actions }

**Restablecer** — restablece los **Datos de vuelo** (telemetría +
cronómetros), **Todos los cronómetros** o **Toda la telemetría**.

![Restablecer](../assets/model-sf-reset.png)

**Captura de pantalla** — guarda una captura de pantalla en la carpeta
`screenshots/` de la SD card o de la eMMC.

![Captura de pantalla](../assets/model-sf-screenshot.png)

**Ajustar el failsafe** — captura las posiciones actuales de los canales
como failsafe, a través del **Módulo** de RF interno o externo de la radio.

![Ajustar el failsafe](../assets/model-sf-set-failsafe.png)

**Reproducir audio** — la acción más completa, que admite una secuencia
entera:

![Reproducir audio](../assets/model-sf-play-audio.png)

- **Voz** — cuál de las hasta 3 voces configuradas en Ethos se usará
  (consulte [General](../system-setup/general.md#audio-settings)).
- **Repetir** — reproducir una vez, o repetirse con la frecuencia
  introducida aquí, con una duración de hasta 10 minutos.
- **Saltar al inicio** — si se activa, el audio no se reproducirá al
  encender la radio.
- **Secuencia** — hasta 100 líneas, cada una de ellas:

  - **Reproducir fichero** — reproduce el archivo de audio seleccionado.

    ![Reproducir fichero](../assets/model-sf-play-audio-add-play-file.png)

  - **Reproducir valor** — reproduce el valor de la fuente seleccionada:
    analógicas (palancas, pots o sliders), interruptores, interruptores
    lógicos, compensadores, canales, giróscopo, reloj del sistema,
    entrenador, cronómetros o telemetría.

    ![Reproducir valor](../assets/model-sf-play-audio-add-play-value.png)

  - **Tiempo de espera** — un retraso fijo, de hasta 10 minutos.
  - **Condición de espera** — pausa la secuencia hasta que se cumpla la
    condición de espera.

  ![Añadir línea de secuencia](../assets/model-sf-play-audio-add-line.png)
  ![Tipo de línea de secuencia](../assets/model-sf-play-audio-add-line-type.png)

  Por ejemplo: reproducir `vfrlow.wav` cuando se active el interruptor
  lógico `VFRlow` y, a continuación, reproducir el valor mínimo de VFR que
  se ha grabado —

  ![Reproducir valor tras el fichero](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — o pausar la secuencia hasta que el interruptor SH se mueva a la posición
  más baja antes de continuar:

  ![Secuencia con condición de espera](../assets/model-sf-play-audio-add-sequence.png)

  Tocando en una línea de la secuencia podrá editarla, añadir una nueva,
  moverla hacia arriba o abajo, o borrarla:

  ![Administración de secuencias](../assets/model-sf-play-audio-add-sequence-management.png)

**Vibración (Haptic)** — asigna vibración háptica a una acción:

![Vibración](../assets/model-sf-haptic.png)

- **Patrón** — simple, doble, triple, quíntuple o muy breve.

  ![Patrón de vibración](../assets/model-sf-haptic-pattern.png)

- **Fuerza** — entre 1 y 10 (el valor predeterminado es 5).
- **Repetir** — una vez, o repetirse con la frecuencia introducida aquí.
- **Seleccionar motores de vibración** — en las emisoras con motores de
  vibración en las palancas (X20 Pro AW, X20RS, o una X20 Pro/X20R
  actualizada con motores MC20R en las palancas — vaya a
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Por defecto** (vibración interna), **Todos los motores**, **Vibración en
  la palanca izquierda** o **Vibración en la palanca derecha**.

  ![Vibración en la X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Escribir registros** — guarda los registros en formato `.csv` en la
carpeta `Logs/` de la SD card o de la eMMC, con la hora y la fecha del RTC
(imprescindible para separar después los datos de registro en sesiones):

![Escribir registros](../assets/model-sf-write-logs.png)

- **Intervalo de escritura** — de 100 a 500 ms.
- **Palancas/Pots/Sliders**, **Interruptores**, **Interruptores lógicos**,
  **Canales** — categorías de registro que se activan de forma
  independiente.

  **Visor de registros**: abra un archivo de registro de la carpeta `/Logs`
  con el explorador de archivos. Seleccione los canales que se van a ver (la
  RSSI se selecciona por defecto); desplace la pantalla con el selector
  rotatorio o moviendo el dedo, y amplíe o aleje girando el selector
  rotatorio mientras mantiene presionada la tecla `PAGE`. El botón `DISP`
  mueve el foco al primer botón de la columna de la derecha.

**Reproducir texto** (sólo en X20 Pro) — utiliza el procesador interno TTS
(Text-To-Speech) de la radio en lugar de un archivo pregrabado:

![Reproducir texto](../assets/model-sf-x20pro-play-text.png)

- **Texto** — el texto que se va a convertir en audio y reproducir. Escrito
  todo en mayúsculas se deletrea letra por letra (por ejemplo, "OFF" →
  "O-F-F"); en minúsculas se pronuncia como palabra ("off").
- **Repetir**, **Saltar al inicio** — como más arriba.

**Ir a la página** — cambia la pantalla a la página seleccionada, por
ejemplo para mostrar la grabación de datos de vuelo de un receptor al
presionar un botón:

![Ir a la página](../assets/model-sf-go-to-screen.png)
![Opciones de página](../assets/model-sf-go-to-screen-options.png)

**Bloquear pantalla táctil** — bloquea la pantalla táctil de la radio para
prevenir su operación inadvertida (también se puede activar presionando
`ENT` y `PAGE` simultáneamente durante 1 segundo en la pantalla de inicio):

![Bloquear pantalla táctil](../assets/model-sf-lock-touchscreen.png)

**Cargar modelo** — carga el **Modelo** especificado cuando se cumplan las
condiciones determinadas, con una petición de **Confirmación** opcional
antes de cambiar realmente de modelo:

![Cargar modelo](../assets/model-sf-load-model.png)

**Reproducir vario** — genera el audio del vario a partir de la fuente
seleccionada (normalmente el sensor VSpeed de un vario FrSky, aunque sirve
cualquier sensor que use m/s como unidad de medida):

![Reproducir vario](../assets/model-sf-play-vario.png)
![Fuente del vario: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Rango** — el régimen de subida o bajada asociado al tono; por defecto
  ±10 m/s (hasta ±100 m/s). Cuando el régimen de subida está por encima del
  valor de **Centro**, el tono de los pitidos se incrementa linealmente
  hasta que se alcanza el máximo valor de Rango (el tono al máximo régimen
  de subida se configura en [General →
  Vario](../system-setup/general.md#vario)); al bajar, el tono se hace
  continuo y decrece linealmente hasta el mínimo régimen de bajada.
- **Centro** — la banda que define un régimen cero de subida o bajada, por
  defecto ±0,3 m/s (hasta ±2 m/s); dentro de ella el tono se mantiene
  continuo (el tono a régimen cero también se configura en General → Vario).
  Seleccione **Silencio** en lugar de **Pitido** para silenciar los pitidos
  por completo.

  ![Opciones de rango y centro del vario](../assets/model-sf-play-vario-options.png)
