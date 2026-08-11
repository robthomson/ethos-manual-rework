---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Interruptores lógicos

![Menú de interruptores lógicos](../assets/model-lsw-menu.png)

Los interruptores lógicos son interruptores *virtuales* programados por el
usuario: no son mandos físicos, pero pueden emplearse en cualquier lugar
donde quepa un interruptor físico, como disparador de programas. Cada uno
evalúa la condición configurada respecto a sus entradas (otros
interruptores, valores de telemetría, valores de mezcla, valores de
temporizador, canales de giróscopo/entrenador y más) para resultar
verdadero o falso. Se admiten hasta 100; de forma predeterminada no existe
ninguno. Añada uno con **+**; la etiqueta de menú de un interruptor
definido se muestra en verde cuando es verdadero y en rojo cuando es
falso. Toque uno existente para acceder a
**Editar**/**Mover**/**Copiar-pegar**/**Clonar**/**Eliminar**.

![Añadir interruptor lógico](../assets/model-lsw-add.png)

## Función

Todas las funciones admiten una salida normal o invertida.

- **A ~ X** — verdadero cuando la fuente `A` es *aproximadamente* igual
  (dentro de ~10 %) a un valor fijo `X`. Generalmente preferible a la
  igualdad exacta —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — ya que con `A = X`, una lectura de telemetría que fluctúa entre, por
  ejemplo, 8,5 V y 8,35 V en torno a un objetivo de 8,4 V puede que nunca
  coincida exactamente con 8,4 V, por lo que el interruptor nunca se
  activaría.
- **A = X** — verdadero solo cuando `A` es exactamente igual a `X`.
- **A > X** / **A < X** — verdadero cuando `A` es mayor/menor que `X`.
- **|A| > X** / **|A| < X** — igual que lo anterior, pero comparando el
  valor absoluto de `A` (se ignora el signo).
- **Δ > X** — verdadero cuando la variación de `A` (delta) durante el
  **intervalo de comprobación** alcanza al menos `X`. Un intervalo de
  `---` significa una ventana infinita.

  ![Delta mayor que X](../assets/model-lsw-delta-gtX.png)
  ![Delta absoluto mayor que X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — igual que lo anterior, usando el valor absoluto de la
  variación.
- **Rango** — verdadero cuando `A` se encuentra dentro de un rango
  especificado.

  ![Rango](../assets/model-lsw-range.png)

- **AND** — verdadero solo si todas las fuentes indicadas (Valor 1…N) son
  verdaderas.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — verdadero si al menos una de las fuentes indicadas es
  verdadera.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (OR exclusivo) — verdadero si *exactamente una* de las fuentes
  indicadas es verdadera.

  ![XOR](../assets/model-lsw-XOR.png)

- **Generador de temporizador** — conmuta libremente entre activo e
  inactivo de forma continua: activo durante **Duración activa** e
  inactivo durante **Duración inactiva**.

  ![Generador de temporizador](../assets/model-lsw-timer-generator.png)

- **Sticky** — un enclavamiento (biestable SR); véase
  [más abajo](#sticky).
- **Edge** — un pulso momentáneo; véase [más abajo](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Se enclava en **Verdadero** en cuanto se cumple su condición **Trigger
ON**, y permanece verdadero hasta que se cumple **Trigger OFF**,
condicionado opcionalmente por la **Condición activa** (mientras esta sea
falsa, la salida se mantiene en falso independientemente de todo; el
enclavamiento interno de Sticky sigue evaluándose en segundo plano y se
transmite de nuevo a la salida en cuanto la condición activa vuelve a ser
verdadera, sujeto a los retardos).

Desde Ethos 1.6.2, ambos disparadores admiten un modificador **Edge**
(pulsación larga de `ENT` sobre la condición del disparador y seleccionar
Edge, que se muestra con el prefijo `†`) para un control mucho más
preciso:

![Sticky con edge](../assets/model-lsw-sticky-with-edge.png)
![Selección de la opción Edge](../assets/model-lsw-sticky-edge-select.png)

- **Trigger ON `SA` (sin retardo)** — se enclava en verdadero en el
  instante en que SA pasa a nivel alto.
- **Trigger ON `SA` (retardo = 1 s)** — se enclava en verdadero 1 s
  después de que SA pase a nivel alto, *siempre que* SA siga en nivel
  alto al final de ese segundo.
- **Trigger ON `†SA` (retardo = 1 s)** — se enclava en Verdadero→Falso
  1 s después de que SA pase a nivel alto, **independientemente** de si SA
  sigue en nivel alto en ese momento (el flanco ya se produjo; el retardo
  solo temporiza el resultado).

Trigger OFF se comporta de la misma manera a la inversa. Los retardos se
aplican **después** de la condición activa, por lo que un cambio en la
condición activa vuelve a disparar la temporización del retardo antes de
que el valor enclavado llegue de nuevo a la salida. Si ambos disparadores
pasan de falso a verdadero simultáneamente, la salida del Sticky
**conmuta** una vez. Véase también [Parámetros
comunes](#shared-parameters) más abajo.

### Edge

![Edge](../assets/model-lsw-edge.png)

Un pulso momentáneo: verdadero durante **Duración**, una vez que se
cumple su condición de disparo. **Durante** es un par `[t1:t2]` que
controla exactamente cuándo:

- **Flanco de subida, Durante = 0,0 s** — se dispara en el instante en
  que Trigger ON pasa de falso a verdadero.

  ![Flanco de subida](../assets/model-lsw-edge-rising-edge.png)
  ![Durante = 0](../assets/model-lsw-edge-during-eq0.png)

- **Flanco de subida, Durante ≥ 0,0 s (p. ej. 5,0 s)** — se dispara 5 s
  después de que Trigger ON pase a verdadero, ignorando cualquier «pico»
  más corto durante esa ventana de 5 s.

  ![Durante > 0, flanco de subida](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![Durante > 0](../assets/model-lsw-edge-during-gt0.png)

- **Flanco de bajada, Durante = 0,0 s** — se dispara en el instante en
  que Trigger ON pasa de verdadero a falso.
- **Flanco de bajada, Durante ≥ 0,0 s (p. ej. 3,0 s)** — se dispara en la
  transición de verdadero a falso, pero solo si antes había estado
  verdadero durante al menos 3 s.
- **Pulso (t1 y t2 ambos definidos)** — se dispara solo si Trigger ON
  pasa de falso a verdadero y de nuevo a falso dentro de esa ventana
  (p. ej. entre 2 s y 5 s después).

## Parámetros comunes {: #shared-parameters }

![Parámetros comunes](../assets/model-lsw-common-parameters.png)

- **Condición activa** — condiciona la salida del interruptor del mismo
  modo que la de Sticky, más arriba. Opciones: siempre activa, posiciones
  de interruptor/interruptor de función/interruptor lógico/trim,
  Telemetría, Fases de vuelo o un evento del sistema (Retención de gas,
  Corte de gas, Acelerador activo, Telemetría activa, RSSI bajo,
  Entrenador activo, Reinicio de vuelo).
- **Retardo antes de activar** / **Retardo antes de desactivar** —
  cuánto tiempo debe mantenerse la condición como verdadera (o falsa)
  antes de que la salida la siga, hasta 60 s. No aplicable al generador
  de temporizador ni a Edge. (Véase [Guía práctica: aviso de capacidad de
  batería](../how-to/battery-capacity-warning.md) para un retardo
  utilizado para filtrar una caída de tensión.)
- **Confirmación antes de activar** / **de desactivar** — solicita
  confirmación al usuario antes de que el estado cambie realmente (con
  opción de Cancelar, para casos en que se dispare demasiado a menudo
  para resultar útil); resulta práctico para condicionar algo
  arriesgado, p. ej. confirmar antes de apagar remotamente un vehículo
  terrestre.

  ![Confirmar verdadero](../assets/model-lsw-confirm-lsw-true.png)
  ![Confirmar falso](../assets/model-lsw-confirm-lsw-false.png)

- **Duración mínima** — una vez verdadero, permanece verdadero al menos
  este tiempo. Si se deja en `---`, la salida puede ser verdadera solo
  durante un único ciclo del mezclador, demasiado breve incluso para ver
  que la línea se resalte en negrita en la interfaz.
- **Duración máxima** — una vez verdadero, vuelve automáticamente a falso
  después de este tiempo, si sigue activo. Ambas duraciones admiten hasta
  60 s.
- **Comentario** — texto libre, mostrado en cualquier lugar donde este
  interruptor se añada a un widget de valor, para documentar su
  propósito.

## Uso con telemetría

Un evento del sistema **Telemetría activa** (o un interruptor cuya fuente
sea un sensor de telemetría, activo solo mientras ese sensor comunique
datos) cubre las condiciones del tipo «¿se está recibiendo telemetría
actualmente?».

!!! warning
    Una [mezcla](mixes.md) condicionada por un interruptor lógico basado
    en telemetría necesita una **segunda** acción de mezcla que use el
    mismo interruptor **invertido**, para que la mezcla siga teniendo un
    valor válido cuando se pierda la telemetría; recuerde que una mezcla
    inactiva emite el valor neutro (0 % / 1500 µs, o **medio gas** en un
    canal de acelerador). Como alternativa, use una acción **Offset**,
    que ya incorpora valores separados para activo/inactivo; p. ej. la
    fuente **0** (el valor especial) con el offset ajustado para que la
    mezcla dé +100 % mientras `LS3` está activo y −100 % mientras está
    inactivo cubre ambos casos en una sola acción.

## Comparación de fuentes

Normalmente una fuente se compara con un valor fijo, pero también pueden
compararse directamente dos fuentes del *mismo* tipo, p. ej. dos
temporizadores, dos tensiones o dos sensores de RPM.

## Ignorar la entrada de entrenador del esclavo

![Ignorar la entrada de entrenador](../assets/model-lsw-ignore-trainer-input.png)

Las [opciones](../getting-started/user-interface-and-navigation.md#choosing-a-source)
de una fuente permiten excluir la entrada de entrenador procedente de una
emisora de alumno (esclava) conectada; se emplea normalmente en un
interruptor lógico que vigila el movimiento del stick del **maestro**
(p. ej. para intervenir al instante si algo va mal), sin que las entradas
del alumno lo activen también. Suele combinarse con un interruptor de
entrenador que condiciona la propia condición activa del maestro.
