---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Ejemplo básico de ala fija

Un recorrido completo para un avión con motor + 2 alerones + 2 flaps +
profundidad + dirección, con un servo por superficie, construido de principio a
fin con el asistente. Complete primero la [Configuración inicial de la emisora](initial-radio-setup.md).

## Paso 1. Confirmar los ajustes del sistema

Este ejemplo utiliza el orden de canales predeterminado **AETR**.

## Paso 2. Identificar los servos/canales necesarios

[Mezclas](../model-setup/mixes.md) es el corazón de la emisora: hasta 100
canales de mezcla, normalmente con los números más bajos asignados a los servos
(ya que los números de canal se corresponden directamente con los canales del
receptor; el módulo de RF interno del X20 admite hasta 24 canales de salida).
Los canales superiores quedan libres para canales virtuales o canales reales
adicionales mediante varios módulos de RF y SBUS. Nuestro modelo:

| Función | Canales |
|---|---|
| Motor | 1 |
| Alerones | 2 |
| Flaps | 2 |
| Profundidad | 1 |
| Dirección | 1 |

(El tren retráctil se añade más adelante, en el [Paso 10](#step-10-add-a-mix-for-retracts).)

## Paso 3. Crear un modelo nuevo

![Crear modelo de avión](../assets/tut-fw-eg-wiz-create-airplane.png)

Desde [Selección de modelo](../model-setup/model-select.md), elija una
categoría, toque **+** e inicie el asistente **Airplane**. Seleccione **Receptor
no estabilizado** para este ejemplo.

![Canales del motor](../assets/tut-fw-eg-wiz-engine.png)
![Canales de alerones/flaps](../assets/tut-fw-eg-wiz-ail-flaps.png)

Acepte 1 canal de motor, después 2 canales de alerones y seleccione 2 canales de
flaps.

![Tipo de cola](../assets/tut-fw-eg-wiz-tail.png)
![Canales de profundidad/dirección](../assets/tut-fw-eg-wiz-ele-rudd.png)

Acepte la opción predeterminada **Traditional Tail**, con 1 canal de
profundidad y 1 de dirección.

![Nombre del modelo](../assets/tut-fw-eg-wiz-name.png)
![Receptor](../assets/tut-fw-eg-wiz-rx.png)

Asígnele un nombre (por ejemplo, "FWexample", hasta 15 caracteres), finalice el
asistente y pasará a ser el modelo activo, creado en la categoría Airplane.

## Paso 4. Revisar y configurar las mezclas

![Vista general de mezclas](../assets/tut-fw-eg-mixes.png)

El asistente ya ha creado las mezclas de alerones (canales 1 y 5), profundidad,
acelerador, dirección y flaps (los flaps muestran `---`: aún no tienen fuente
asignada).

### Alerones {: #ailerons }

![Mezcla de alerones](../assets/tut-fw-eg-mixes-ail-mix.png)
![Editar mezcla de alerones](../assets/tut-fw-eg-mixes-ail-edit.png)

**Peso/Rates**: configure los rates antes de volar algo nuevo; un recorrido
moderado (por ejemplo, 30%) es adecuado para vuelo deportivo, y el 100% completo
para 3D. Añada un rate del 60% para el interruptor SB en posición central y un
rate del 30% para SB abajo; el valor predeterminado (SB arriba) se mantiene al
100%:

![Rates de peso](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo**: una respuesta lineal puede resultar nerviosa alrededor del centro;
añada rates de Expo (por ejemplo, 60%/40%/20% en las mismas posiciones de SB)
para suavizar la respuesta cerca del centro sin reducir el recorrido máximo:

![Rates de Expo](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Diferencial**: un recorrido igual de alerón hacia arriba y hacia abajo genera
más resistencia en el alerón que baja que en el que sube, lo que guiña el modelo
hacia el exterior del viraje ("guiñada adversa"). Un diferencial positivo (50%
es habitual) reduce el recorrido hacia abajo respecto al de subida para
contrarrestarlo:

![Diferencial del 50%](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Para ajustar el diferencial en vuelo, mantenga pulsado `ENT` sobre el valor,
elija **Usar una fuente** y seleccione Pot1:

![Usar una fuente](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Pot1 seleccionado](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Cuando el valor obtenido en vuelo sea satisfactorio, mantenga pulsado de nuevo y
elija **Convertir a valor** para fijarlo de forma permanente:

![Convertir a valor](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim**: permite desvincular esta mezcla de su trim asociado sin desactivar el
propio trim, dejándolo libre para otro uso:

![Trim de alerones](../assets/tut-fw-eg-mixes-ail-trim.png)

### Profundidad y dirección

El mismo esquema de triple rate + Expo, en este caso con el interruptor SC:

![Rates de Expo de profundidad](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Acelerador

![Mezcla de acelerador](../assets/tut-fw-eg-mixes-thr-edit.png)

Deje la entrada en el stick de acelerador (no se necesitan rates ni Expo), pero
un interruptor de seguridad es imprescindible; un motor de explosión o eléctrico
que arranque de forma inesperada puede causar lesiones graves.

**Trim en posición baja** (motores glow/gasolina): ajusta el ralentí de forma
independiente del acelerador a fondo:

![Trim en posición baja](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Con esta opción activada, el canal de acelerador se sitúa en −75% con el stick
en ralentí; la palanca de trim de acelerador ajusta entonces el ralentí entre
−100% y −50%.

**Corte de gas**: un enclavamiento de seguridad. Con el interruptor SA abajo
como condición activa (se muestra en negrita cuando está activa), la salida de
acelerador se mantiene en −100% en cuanto el stick baja de −85%:

![Corte de gas](../assets/tut-fw-eg-mixes-thr-cut.png)

Con **Sticky** activado, en cambio, el acelerador se corta en el **instante** en
que SA se pone abajo, independientemente de la posición del stick:

![Corte de gas con Sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

En cualquier caso, una vez que la condición activa desaparece, el stick debe
volver por debajo de −85% antes de que el acelerador pueda aumentar de nuevo,
lo que evita que el motor salte a una posición de gas alto en el momento en que
se suelta el interruptor de corte.

**Retención de gas**: un corte de emergencia desde *cualquier* posición del
stick, que lleva la salida directamente a −100% (o a un valor configurado) en el
instante en que se cumple su condición:

![Retención de gas](../assets/tut-fw-eg-mixes-thr-hold.png)

### Flaps

![Entrada de flaps](../assets/tut-fw-eg-mixes-flaps-input.png)

Asigne los flaps al interruptor SE y ajuste el peso de ambos canales de salida
al 100%:

![Pesos de los flaps](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Paso 5. Vincular el receptor

Registre (si es ACCESS) y vincule desde [Sistema RF](../model-setup/rf-system.md).
Antes de pasar a Salidas, considere desconectar los varillajes de los servos o
reducir temporalmente su recorrido, para evitar forzar algo mientras establece
los límites Mín/Máx.

## Paso 6. Configurar las salidas

![Salidas](../assets/tut-fw-eg-outputs.png)

[Salidas](../model-setup/outputs.md) adapta la lógica del mezclador a la
mecánica real del modelo.

**Alerón 1**: centre el servo con **Centro PWM** después de optimizar el
varillaje mecánico y, a continuación, ajuste **Mín**/**Máx**. Asignar
temporalmente un potenciómetro a Mín (y después a Máx, del mismo modo que en el
ejemplo del diferencial anterior) hace que el ajuste sea más rápido:

![Editar salida de alerón](../assets/tut-fw-eg-outputs-edit-ail.png)

**Flaps**: los flaps suelen necesitar una gran deflexión hacia abajo para frenar
de forma efectiva; se sacrifica parte del recorrido hacia arriba en el varillaje
para conseguirlo, de modo que el flap quede a media bajada con el servo
centrado, y después se usan Mín/Máx para fijar las posiciones reales de arriba y
de bajada total. Una curva de 5 puntos es una forma habitual de corregir
cualquier desajuste resultante en el seguimiento entre flaps y alerones. Termine
con **[Balancear canales](../model-setup/outputs.md#balance-channels)** para
sincronizar los alerones y flaps izquierdo y derecho.

## Paso 7. Introducción a las fases de vuelo

Las [fases de vuelo](../model-setup/flight-modes.md) permiten que un modelo
disponga de ajustes por tarea, como cambiar de marcha. De las 20 disponibles,
este ejemplo utiliza tres: **Default**, **Flaps Half** (interruptor SE en
posición central) y **Flaps Full** (SE arriba). Está activa la primera fase de
vuelo cuya condición sea verdadera; la fase **Default** no tiene ninguna
condición y actúa siempre que ninguna otra sea aplicable, razón por la cual no
dispone de opción de selección de interruptor. Un fundido de entrada/salida de
1 segundo suaviza la transición al desplegar los flaps.

## Paso 8. Configurar los trims

Dos formas de gestionar la variación del trim de profundidad según la posición
de los flaps:

**Trims independientes por fase de vuelo**: la opción más sencilla; el trim de
profundidad pasa a ser totalmente independiente en cada fase de vuelo,
cambiando automáticamente al mover SE. Como cada fase se trima desde cero, el
[Trim instantáneo](../model-setup/trims.md#instant-trim) resulta útil: trime
primero para el vuelo normal, aterrice y utilice ese valor como punto de partida
para las fases con flaps.

**Trim base con offset**: se trima una vez en Default, y la compensación de
profundidad de cada fase con flaps se superpone como un offset:

1. Ajuste el **Paso** de trim a Medio (para un trimado inicial más rápido;
   redúzcalo después para el ajuste fino), el **Modo** a Personalizado y añada un
   nuevo comportamiento.
2. **Condición activa**: `FM1(Flaps Half)`, modo **Offset + Default**: el trim
   de Flaps Half pasa a ser el trim base más el offset que se introduzca
   mientras esa fase está activa:

   ![Añadir comportamiento](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Repita el proceso para `FM2(Flaps Full)`:

   ![Seleccionar FM](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Ahora cada fase con flaps puede trimarse de forma independiente, pero si más
adelante se ajusta el trim base de Default (por ejemplo, para corregir la deriva
térmica de un servo), los trims de ambas fases con flaps se desplazan
automáticamente en la misma medida.

![Selección de trim personalizado](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Paso 9. Configurar un temporizador de batería de vuelo

En [Temporizadores](../model-setup/timers.md), edite el Temporizador 1: modo
**Descendente**, valor inicial de 5 minutos, en funcionamiento siempre que
**Acelerador activo** sea verdadero (y no esté retenido en reinicio).
Opcionalmente, asigne una fuente de temporización proporcional (por ejemplo, el
stick de acelerador) para que el temporizador avance a velocidad real con el
acelerador a fondo y se ralentice al reducir gas.

## Paso 10. Añadir una mezcla para el tren retráctil {: #step-10-add-a-mix-for-retracts }

![Fuente de la mezcla del tren retráctil](../assets/tut-fw-eg-retracts-source.png)

Toque una mezcla, **Añadir mezcla** → **Mezcla libre**, asígnele el nombre
"Retracts", establezca la condición en Siempre y la fuente en el interruptor SF.
La acción predeterminada con Peso = 100% es adecuada; esto asigna, por ejemplo,
el canal 8 al tren retráctil:

![Salida del tren retráctil](../assets/tut-fw-eg-retracts-outputs.png)
