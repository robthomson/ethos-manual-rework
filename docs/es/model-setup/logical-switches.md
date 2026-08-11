---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Interruptores lógicos

![Menú de interruptores lógicos](../assets/model-lsw-menu.png)

Los interruptores lógicos son interruptores *virtuales* programados por el
usuario: no son mandos físicos, pero pueden emplearse en cualquier sitio
donde quepa un interruptor físico, como disparador de programas. Cada uno
evalúa la condición configurada frente a sus entradas (otros interruptores,
valores de telemetría, valores de mezclas, valores de cronómetros, canales
de giróscopo/entrenador y más) para hacerse Verdadero o Falso. Se admiten
hasta 100; no hay ninguno por defecto. Pulse **+** para añadir uno; la
etiqueta de un interruptor ya definido se muestra en verde cuando es
Verdadero y en rojo cuando es Falso. Pulse sobre uno existente para
**Editar**/**Mover**/**Copiar-pegar**/**Clonar**/**Eliminar**.

![Añadir interruptor lógico](../assets/model-lsw-add.png)

## Función

Todas las funciones admiten una salida normal o invertida.

- **A ~ X** — Verdadera cuando la fuente `A` es *aproximadamente* igual
  (dentro de un ~10 %) a un valor fijo `X`. Generalmente preferible a la
  igualdad exacta —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — ya que con `A = X`, una lectura de telemetría que oscile entre, por
  ejemplo, 8,5 V y 8,35 V en torno a un objetivo de 8,4 V puede que nunca
  coincida exactamente con 8,4 V, con lo que el interruptor nunca se
  activaría.
- **A = X** — Verdadera sólo cuando `A` es exactamente igual a `X`.
- **A > X** / **A < X** — Verdadera cuando `A` es mayor/menor que `X`.
- **|A| > X** / **|A| < X** — igual que lo anterior, pero comparando el
  valor absoluto de `A` (se ignora el signo).
- **Δ > X** — Verdadera cuando la variación de `A` (delta) durante el
  **intervalo de comprobación** alcanza al menos `X`. Un intervalo `---`
  significa una ventana infinita.

  ![Delta mayor que X](../assets/model-lsw-delta-gtX.png)
  ![Delta absoluto mayor que X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — igual que lo anterior, usando el valor absoluto de la
  variación.
- **Rango** — Verdadera cuando `A` se encuentra dentro de un rango
  especificado.

  ![Rango](../assets/model-lsw-range.png)

- **AND** — Verdadera sólo si todas las fuentes seleccionadas (Valor 1 …
  Valor(n)) son verdaderas.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — Verdadera si al menos una de las fuentes seleccionadas es
  verdadera.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (O Exclusivo) — Verdadera si *sólo una* de las fuentes
  seleccionadas es verdadera.

  ![XOR](../assets/model-lsw-XOR.png)

- **Generador de cronómetros** — el interruptor lógico se activa y
  desactiva continuamente: se enciende durante el tiempo **Duración
  activa** y se apaga durante el tiempo **Duración inactiva**.

  ![Generador de cronómetros](../assets/model-lsw-timer-generator.png)

- **Sticky** — una función de enganche/desenganche (SR Flip-flop); véase
  [más abajo](#sticky).
- **Edge** — un pulso momentáneo; véase [más abajo](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Se engancha en **Verdadero** en cuanto se cumple su condición de
activación (**Trigger ON**), y mantiene su valor hasta que se cumple la
condición de desenganche (**Trigger OFF**), todo ello regulado
opcionalmente por la **Condición activa** (mientras ésta sea Falsa, el
resultado del interruptor lógico se mantendrá en Falso; el enganche
interno de Sticky continúa operando en segundo plano y se conmuta de
nuevo a la salida tan pronto como la condición activa vuelve a ser
Verdadera, sujeto a los retrasos que se le introduzcan).

Desde Ethos 1.6.2, ambas condiciones admiten la opción **Borde**
(mantenga pulsada la tecla `ENT` sobre la condición de activación y
seleccione Borde; aparecerá un símbolo `†` delante de la fuente elegida)
para un control mucho más flexible:

![Sticky con borde](../assets/model-lsw-sticky-with-edge.png)
![Selección de la opción Borde](../assets/model-lsw-sticky-edge-select.png)

- **Condición para ON `SA` (sin retraso)** — se engancha en Verdadero tan
  pronto como el interruptor SA se mueve hacia arriba.
- **Condición para ON `SA` (retraso = 1 s)** — se engancha en Verdadero
  1 segundo después de que SA se haya movido hacia arriba, *siempre que*
  ese interruptor SA permanezca arriba durante el retraso.
- **Condición para ON `†SA` (retraso = 1 s)** — cambia de Verdadero a
  Falso 1 segundo después de que SA esté arriba, **incluso si** SA no
  permanece arriba durante el retraso (el borde ya se ha producido; el
  retraso sólo temporiza el resultado).

La condición para OFF se comporta del mismo modo, a la inversa. Los
retrasos se aplican **DESPUÉS** de la condición activa: si la condición
activa cambia, los periodos de retardo se aplicarán antes de que el valor
enganchado se conmute de nuevo a la salida. Cambios simultáneos de las
condiciones de activación y desactivación de Falso a Verdadero harán que
el resultado de Sticky **cambie su estado** sólo una vez. Vaya también a
la sección [Parámetros compartidos](#shared-parameters) más abajo.

### Edge

![Edge](../assets/model-lsw-edge.png)

Es un interruptor momentáneo que se convierte en Verdadero durante el
periodo especificado en **Duración**, cuando se cumplen sus condiciones de
activación. **During** está dividido en dos partes, `[t1:t2]`, que
controlan exactamente cuándo:

- **Borde ascendente, During = 0,0 s** — se activa en el instante en que
  la condición de activación pasa de Falso a Verdadero.

  ![Borde ascendente](../assets/model-lsw-edge-rising-edge.png)
  ![During = 0](../assets/model-lsw-edge-during-eq0.png)

- **Borde ascendente, During ≥ 0,0 s (p. ej. 5,0 s)** — se activa
  5 segundos después de que la condición de activación pase a Verdadero,
  ignorando cualquier «pico» adicional durante ese periodo de 5 s.

  ![During > 0, borde ascendente](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![During > 0](../assets/model-lsw-edge-during-gt0.png)

- **Borde descendente, During = 0,0 s** — se activa en el instante en que
  la condición de activación pasa de Verdadero a Falso.
- **Borde descendente, During ≥ 0,0 s (p. ej. 3,0 s)** — se activa en la
  transición de Verdadero a Falso, pero sólo si antes había sido
  Verdadera durante al menos 3 segundos.
- **Pulso (t1 y t2 con valores)** — se activa sólo si la condición de
  activación pasa de Falsa a Verdadera y luego de Verdadera a Falsa
  dentro de esa ventana (p. ej. entre 2 y 5 segundos después).

## Parámetros compartidos {: #shared-parameters }

![Parámetros compartidos](../assets/model-lsw-common-parameters.png)

- **Condición activa** — regula la salida del interruptor lógico del
  mismo modo que en Sticky, más arriba. Puede elegirse entre: Siempre
  activada, Posiciones de interruptor, Interruptores de Función,
  Interruptores Lógicos, Posiciones de compensador, Telemetría, Modos de
  vuelo o un evento del sistema (Throttle hold, Throttle cut, Throttle
  active, Telemetría activa, RSSI baja, Entrenador activo,
  Restablecimiento del vuelo).
- **Retraso antes de activarse** / **Retraso antes de inactividad** —
  determinan el tiempo durante el cual las condiciones del interruptor
  lógico tienen que ser Verdaderas (o Falsas) antes de que la salida las
  siga; los retardos pueden ser de hasta 60,0 s. No es relevante para el
  Generador de cronómetros ni para Edge. (Véase [Cómo hacerlo: aviso de
  capacidad de batería](../how-to/battery-capacity-warning.md) para un
  retardo usado para filtrar una caída de tensión.)
- **Confirmación antes de activarse** / **antes de desactivarse** — pide
  confirmación al usuario antes de que el estado cambie realmente (existe
  la opción de Cancelar para situaciones donde el diálogo de confirmación
  se active con demasiada frecuencia); resulta muy útil para condicionar
  algún evento peligroso, por ejemplo pedir confirmación antes de apagar
  a distancia una máquina terrestre.

  ![Confirmar verdadero](../assets/model-lsw-confirm-lsw-true.png)
  ![Confirmar falso](../assets/model-lsw-confirm-lsw-false.png)

- **Duración Mínima** — una vez que el interruptor lógico se convierte en
  Verdadero, permanecerá así al menos durante el tiempo especificado. Si
  se deja el valor predeterminado `---`, sólo se convertirá en Verdadero
  durante un ciclo de procesamiento de la mezcla, demasiado corto para
  verlo, por lo que la línea LSW no se pondrá en negrita.
- **Duración Máxima** — una vez que el interruptor lógico se convierte en
  Verdadero, sólo permanecerá verdadero hasta que alcance la duración
  máxima especificada, si se ha ajustado. Ambas duraciones se pueden
  establecer hasta 60,0 s.
- **Comentario** — texto libre para explicar su uso o función. El
  comentario se muestra cuando se añade el interruptor lógico a un widget
  con valor.

## Uso con telemetría

El evento del sistema **Telemetría activa** (o un interruptor lógico cuya
Fuente sea un sensor de telemetría, activo sólo mientras ese sensor esté
enviando datos) cubre las condiciones del tipo «se está recibiendo
telemetría».

!!! warning
    Cuando se usa en una [mezcla](mixes.md) un interruptor lógico que
    dependa de la telemetría, se debe añadir una **segunda** acción de
    mezcla que use el mismo interruptor lógico pero **invertido**, para
    asegurar que la mezcla tenga valores válidos incluso cuando se pierda
    la telemetría. Recuerde que cuando una mezcla está inactiva su canal
    de salida estará en neutral = 0 % = 1500 µs, ¡o **con el motor a
    mitad** si estamos hablando del acelerador! Alternativamente, se puede
    usar una acción de desplazamiento (**Offset**), que ya tiene dos
    valores por defecto, uno cuando está activa y otro cuando está
    inactiva: por ejemplo, con la fuente ajustada al valor especial **0**
    y el desplazamiento configurado para que la salida de la mezcla sea
    del +100 % cuando `LS3` esté activo y del −100 % cuando esté
    inactivo, se cubren ambos casos en una sola acción.

## Comparación de fuentes

Normalmente, una fuente se compara con un valor fijo. Sin embargo, se
permite una comparación directa entre dos fuentes que tengan el *mismo*
formato, por ejemplo 2 cronos, 2 voltajes o 2 fuentes de RPM.

## Opción de ignorar la entrada del alumno

![Ignorar entrada entrenador](../assets/model-lsw-ignore-trainer-input.png)

En las [opciones](../getting-started/user-interface-and-navigation.md#choosing-a-source)
de una fuente se puede ignorar cualquier entrada procedente de la radio
esclava del alumno. Una aplicación típica es cuando un interruptor lógico
está configurado para detectar el movimiento de las palancas del
**instructor** (por ejemplo, para permitir la intervención instantánea si
las cosas van mal), evitando que las entradas del alumno activen también
el interruptor lógico. Normalmente se usa en conjunción con un interruptor
de entrenador que habilita/deshabilita la ‘condición activa’ en la radio
del maestro.
