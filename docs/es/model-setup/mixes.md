---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mezclas

![Icono de Mezclas](../assets/model-icon-mixes.png)

Las mezclas son el núcleo de la programación de modelos en Ethos: aquí es donde
las entradas (palancas, interruptores, sensores, cualquier cosa que pueda
alcanzar una [fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source))
se encaminan, se modelan y se combinan sobre los canales de salida. Se pueden
definir hasta 120 mezclas por modelo.

![Tabla de mezclas](../assets/model-mixes.png)

Si el modelo se creó con el asistente de **Selección de modelo**, sus mezclas
básicas (alerón, elevador, acelerador, timón y cualquier otra que necesite la
célula) ya están definidas aquí. Al seleccionar una mezcla y pulsar `ENT` se
abre un menú contextual para editarla, agregar una nueva mezcla, pasar a la
[vista por canal](#per-channel-view), reordenarla, duplicarla o eliminarla. Las
mezclas inactivas aparecen atenuadas y, al eliminar una, siempre se pide
confirmación previa.

## Anatomía de una mezcla {: #anatomy-of-a-mix }

Todas las mezclas comparten el mismo conjunto de campos, sea cual sea la
categoría de la que provengan. La mezcla de **alerón** es un ejemplo
representativo: las mezclas de elevador y timón tienen una disposición
idéntica.

![Mezcla de alerón](../assets/model-mixes-ail-edit.png)

![Editor de la mezcla de alerón](../assets/model-mixes-ail.png)

**Nombre**: por defecto es el tipo de mezcla; se puede editar.

**Condición activa**: por defecto es *Siempre encendido*. Puede hacerse
condicional eligiendo una posición de interruptor, un interruptor de función,
un interruptor lógico, un modo de vuelo, un evento del sistema (corte o
retención del acelerador) o una posición de compensado; en ese caso la mezcla
sólo se aplica mientras la condición sea verdadera.

**Modos de vuelo**: si se ha definido algún modo de vuelo, la mezcla puede
además hacerse condicional a uno o más de ellos.

**Curva**: por defecto está disponible una curva **Expo**, cuyo valor 0
significa que la respuesta es lineal; un valor positivo suavizará la respuesta
en torno al centro, mientras que un valor negativo la agudizará:

![Curva Expo](../assets/model-mixes-ail-expo.png)

En su lugar se puede seleccionar cualquier curva definida previamente en
[Curvas](curves.md). Pueden especificarse hasta 6 curvas en una misma mezcla,
cada una con una condición diferente; si más de una condición se hace verdadera
a la vez, prevalecerá la curva que está más arriba en la lista. Las curvas se
aplican **antes** que los recorridos.

**Recorridos**: una o más líneas de peso, cada una condicionable opcionalmente
por un interruptor, un interruptor de función, un interruptor lógico, una
posición de compensado o un modo de vuelo. La primera línea es la que está por
defecto y actúa siempre que no se cumpla la condición de ninguna otra:

![Recorridos de alerón](../assets/model-mixes-ail-weight.png)

En lugar de un porcentaje fijo, un recorrido puede gobernarse desde una
[fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source),
por ejemplo un pot, para ajustar el recorrido en vuelo:

![Recorrido gobernado desde una fuente](../assets/model-mixes-ail-diff.png)

**Diferencial** (de -100 a 100, por defecto 0): da más recorrido en un sentido
que en el otro. En los alerones es el recurso clásico de dar más recorrido
hacia arriba que hacia abajo para reducir la guiñada adversa. Sólo se muestra
cuando la mezcla tiene más de un canal de salida; en concreto, el diferencial
necesita una configuración de salidas de tipo cola en V o de doble alerón para
tener sentido.

**Recuento de canales / salidas**: cuántos canales de salida gobierna esta
mezcla y a qué salidas físicas se asignan:

![Recuento de canales](../assets/model-mixes-ail-ch-count.png)

Una pulsación larga de `ENT` sobre un canal de salida en otra parte de la
interfaz (por ejemplo en [Salidas](outputs.md)) lleva directamente de vuelta a
esta página.

## La mezcla de acelerador

La mezcla del acelerador es una mezcla de alerón/elevador/timón a la que se
añaden opciones de seguridad específicas para el control del motor.

![Mezcla de acelerador](../assets/model-mixes-thr.png)

**Entrada**: la fuente del acelerador, normalmente la palanca de motor, aunque
puede sustituirse por un pot, un deslizador, un interruptor, un compensador, un
canal, un eje giroscópico, un canal del entrenador, un cronómetro o cualquier
otra fuente.

**Compensador de ralentí**: para motores de combustión, permite que un
compensador específico ajuste el régimen de ralentí sin alterar la posición de
motor a fondo. Con el compensador de ralentí activado, el canal del acelerador
se sitúa en -75 % con la palanca en ralentí bajo, y el compensador del
acelerador ajusta entonces el ralentí entre -100 % y -50 %:

![Menú del compensador de ralentí](../assets/model-mixes-thr-trim-menu.png)

![Compensador de ralentí en la posición baja](../assets/model-mixes-thr-trim-low-position.png)

**Corte del acelerador**: un enclavamiento de seguridad estricto; el canal sólo
se activa una vez que la palanca de motor ha pasado por ralentí, de modo que un
accionamiento accidental de un interruptor no pueda arrancar el motor desde una
posición de gas alto:

![Corte del acelerador](../assets/model-mixes-thr-cut.png)

**Retención del acelerador**: mantiene el canal en un valor fijo
independientemente de la posición de la palanca, sin el enclavamiento de
seguridad que aporta el corte del acelerador:

![Retención del acelerador](../assets/model-mixes-thr-hold.png)

El acelerador también dispone de su propio recuento de canales de salida, igual
que cualquier otra mezcla:

![Recuento de canales del acelerador](../assets/model-mixes-thr-ch-count.png)

!!! note "Enclavamiento del acelerador"
    Ethos exige que la entrada de la mezcla del acelerador pase por -100 %
    antes de armar, independientemente de la configuración de corte o
    retención del acelerador. Un modelo creado con el asistente de selección
    de modelo ya lo tiene en cuenta, pero las mezclas de acelerador hechas a
    mano también deberían hacerlo.

## Bibliotecas de mezclas {: #mix-libraries }

La biblioteca de mezclas predefinidas del cuadro de diálogo **Agregar mezcla**
se adapta a la categoría de modelo elegida al crear el modelo: avión,
planeador, helicóptero y multirrotor ofrecen cada uno un conjunto distinto:

![Biblioteca de mezclas para aviones](../assets/model-mixes-library-airplane.png)

![Biblioteca de mezclas para planeadores](../assets/model-mixes-library-glider.png)

![Biblioteca de mezclas para helicópteros](../assets/model-mixes-library-heli.png)

![Biblioteca de mezclas para multirrotores](../assets/model-mixes-library-multirotor.png)

Todas las bibliotecas incluyen además la **Mezcla libre**: un tipo de mezcla de
uso general, sin entrada ni salida predefinidas, más flexible que las mezclas
especializadas pero que requiere más configuración para conseguir el mismo
resultado.

## Vista por canal {: #per-channel-view }

Cuando hay muchas mezclas acumuladas sobre la misma salida, puede resultar
difícil apreciar su efecto combinado en la tabla anterior. Al seleccionar una
mezcla y elegir **Ver por canal**, se agrupan todas las mezclas que afectan a
una misma salida:

![Cambiar a la vista por canal](../assets/model-mixes-chview-select.png)

![Canal contraído](../assets/model-mixes-chview-collapsed.png)

![Canal de elevador expandido](../assets/model-mixes-chview-elevator.png)

Al expandir la línea de resumen de un canal se muestran todas las mezclas que
contribuyen a él, cada una con su salida numérica y gráfica en tiempo real:
resulta útil para comprobar exactamente cuánto está aportando una mezcla
secundaria (por ejemplo, la mezcla de Flap a Elevador) por encima de la entrada
principal de la palanca:

![Detalle de la vista del canal de elevador](../assets/model-mixes-chview-elevator-channel.png)

![Canal de elevador con una mezcla resaltada](../assets/model-mixes-chview-elevator-channel-view.png)

Si se selecciona una submezcla en lugar de la línea de resumen, se abre el
mismo menú contextual que en la vista de tabla (editar, volver a la vista de
tabla, eliminar):

![Seleccionar la vista de tabla desde la vista por canal](../assets/model-mixes-chview-table-view-select.png)

![De vuelta a la vista de tabla](../assets/model-mixes-chview-back-at-mixes-view.png)
