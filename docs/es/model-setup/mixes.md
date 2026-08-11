---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mezclas

![Icono de Mezclas](../assets/model-icon-mixes.png)

Las mezclas son el núcleo de la programación de modelos en Ethos: aquí es donde
las entradas (sticks, interruptores, sensores, cualquier cosa que una
[fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source)
pueda alcanzar) se enrutan, se moldean y se combinan sobre los canales de
salida. Se pueden definir hasta 120 mezclas por modelo.

![Tabla de mezclas](../assets/model-mixes.png)

Si el modelo se creó con el asistente de **Selección de modelo**, sus mezclas
básicas (alerones, profundidad, acelerador, dirección y cualquier otra que
requiera la célula) ya están cargadas aquí. Al seleccionar una mezcla y pulsar
`ENT` se abre un menú contextual para editarla, añadir una nueva mezcla, pasar
a la [vista por canal](#per-channel-view), reordenarla, duplicarla o
eliminarla. Las mezclas inactivas aparecen atenuadas, y al eliminar una siempre
se solicita confirmación previa.

## Anatomía de una mezcla {: #anatomy-of-a-mix }

Todas las mezclas comparten el mismo conjunto de campos, independientemente de
la categoría de la que provengan. La mezcla de **alerones** es un ejemplo
representativo: las mezclas de profundidad y dirección tienen una disposición
idéntica.

![Mezcla de alerones](../assets/model-mixes-ail-edit.png)

![Editor de la mezcla de alerones](../assets/model-mixes-ail.png)

**Nombre**: por defecto es el tipo de mezcla, editable.

**Condición**: por defecto *Always*. Puede restringirse a la posición de un
interruptor, un interruptor de función, un interruptor lógico, una fase de
vuelo, un evento del sistema (corte de gas/retención de gas) o la posición de un
trim, en cuyo caso la mezcla solo se aplica mientras la condición sea verdadera.

**Fases de vuelo**: si hay fases de vuelo definidas, la mezcla puede además
restringirse a una o varias de ellas.

**Curva**: por defecto está disponible una curva **Expo** (0 = lineal; los
valores positivos suavizan la respuesta en torno al centro, los negativos la
hacen más agresiva):

![Curva Expo](../assets/model-mixes-ail-expo.png)

En su lugar se puede seleccionar cualquier curva definida previamente en
[Curvas](curves.md). Se pueden apilar hasta 6 curvas en una misma mezcla, cada
una con su propia condición; si más de una condición es verdadera
simultáneamente, prevalece la curva situada más arriba en la lista. Las curvas
se aplican **antes** de los ratios.

**Ratios**: una o varias filas de peso, cada una condicionable opcionalmente
por un interruptor, un interruptor de función, un interruptor lógico, la
posición de un trim o una fase de vuelo. La primera fila es la predeterminada y
está activa siempre que no se cumpla la condición de ninguna otra fila:

![Ratios de alerones](../assets/model-mixes-ail-weight.png)

En lugar de un porcentaje fijo, un ratio puede gobernarse desde una
[fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source)
—por ejemplo un potenciómetro, para ajustar el ratio en vuelo:

![Ratio gobernado desde una fuente](../assets/model-mixes-ail-diff.png)

**Diferencial** (-100 a 100, por defecto 0): proporciona más recorrido en un
sentido que en el otro. En los alerones se trata del recurso clásico de dar más
recorrido hacia arriba que hacia abajo para reducir la guiñada adversa. Solo se
muestra cuando la mezcla tiene más de un canal de salida; en concreto, el
diferencial requiere una configuración de salidas tipo cola en V o doble alerón
para tener sentido.

**Número de canales / salidas**: cuántos canales de salida gobierna esta mezcla
y a qué salidas físicas se asignan:

![Número de canales](../assets/model-mixes-ail-ch-count.png)

Una pulsación larga de `ENT` sobre un canal de salida en otra parte de la
interfaz (por ejemplo en [Salidas](outputs.md)) lleva directamente de vuelta a
esta página.

## La mezcla de acelerador

La mezcla de acelerador es una mezcla de alerones/profundidad/dirección más
opciones de seguridad específicas del motor.

![Mezcla de acelerador](../assets/model-mixes-thr.png)

**Entrada**: la fuente del acelerador, normalmente el stick de acelerador, pero
puede sustituirse por un potenciómetro, un deslizador, un interruptor, un trim,
un canal, un eje del giróscopo, un canal de escuela o cualquier otra fuente.

**Trim de ralentí**: para motores de combustión, permite que un trim dedicado
ajuste el régimen de ralentí sin alterar la posición de máximo gas. Con el trim
de ralentí activado, el canal de acelerador se sitúa al -75 % con el stick en
ralentí bajo, y el trim de acelerador ajusta entonces el ralentí entre -100 % y
-50 %:

![Menú de trim de ralentí](../assets/model-mixes-thr-trim-menu.png)

![Trim de ralentí en posición baja](../assets/model-mixes-thr-trim-low-position.png)

**Corte de gas**: un enclavamiento de seguridad estricto: el canal solo se
activa una vez que el stick de acelerador ha pasado por ralentí, de modo que un
accionamiento accidental de un interruptor no pueda arrancar el motor desde una
posición de gas alto:

![Corte de gas](../assets/model-mixes-thr-cut.png)

**Retención de gas**: mantiene el canal en un valor fijo independientemente de
la posición del stick, sin el enclavamiento de seguridad que aporta el corte de
gas:

![Retención de gas](../assets/model-mixes-thr-hold.png)

El acelerador también expone su propio número de canales de salida, igual que
cualquier otra mezcla:

![Número de canales del acelerador](../assets/model-mixes-thr-ch-count.png)

!!! note "Enclavamiento del acelerador"
    Ethos requiere que la entrada de la mezcla de acelerador pase por -100 %
    antes de armar, independientemente de la configuración de corte/retención
    de gas; un modelo creado con el asistente de selección de modelo ya lo
    tiene en cuenta, pero las mezclas de acelerador construidas a mano también
    deberían hacerlo.

## Bibliotecas de mezclas {: #mix-libraries }

La biblioteca de mezclas predefinidas del cuadro de diálogo **Add mix** se
adapta a la categoría de modelo elegida al crearlo: avión, planeador,
helicóptero y multirrotor exponen cada uno un conjunto diferente:

![Biblioteca de mezclas de avión](../assets/model-mixes-library-airplane.png)

![Biblioteca de mezclas de planeador](../assets/model-mixes-library-glider.png)

![Biblioteca de mezclas de helicóptero](../assets/model-mixes-library-heli.png)

![Biblioteca de mezclas de multirrotor](../assets/model-mixes-library-multirotor.png)

Todas las bibliotecas incluyen además **Free Mix**: un tipo de mezcla de uso
general sin entrada/salida predefinida, más flexible que las entradas
especializadas pero que requiere más configuración para llegar al mismo
resultado.

## Vista por canal {: #per-channel-view }

Con suficientes mezclas apiladas sobre la misma salida, puede resultar difícil
apreciar su efecto combinado en la tabla plana anterior. Al seleccionar una
mezcla y elegir **View by channel** se agrupan en su lugar todas las mezclas que
afectan a una misma salida:

![Cambiar a la vista por canal](../assets/model-mixes-chview-select.png)

![Canal contraído](../assets/model-mixes-chview-collapsed.png)

![Canal de profundidad expandido](../assets/model-mixes-chview-elevator.png)

Al expandir la fila de resumen de un canal se muestran todas las mezclas que
contribuyen a él, cada una con su salida numérica y gráfica en tiempo real:
resulta útil para confirmar exactamente cuánto está aportando una mezcla
secundaria (por ejemplo, la compensación de flaps a profundidad) por encima de
la entrada principal del stick:

![Detalle de la vista del canal de profundidad](../assets/model-mixes-chview-elevator-channel.png)

![Canal de profundidad, mezcla resaltada](../assets/model-mixes-chview-elevator-channel-view.png)

Seleccionar una submezcla en lugar de la fila de resumen abre el mismo menú
contextual que en la tabla plana (editar, volver a la vista de tabla,
eliminar):

![Seleccionar la vista de tabla desde la vista por canal](../assets/model-mixes-chview-table-view-select.png)

![De vuelta a la vista de tabla](../assets/model-mixes-chview-back-at-mixes-view.png)
