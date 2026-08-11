---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modos de vuelo

![Modos de vuelo](../assets/model-fm.png)

Los modos de vuelo (fases de vuelo) permiten que un interruptor seleccione
entre comportamientos distintos para un mismo modelo: los veleros pueden
usar Lanzamiento/Crucero/Velocidad/Térmica, los aviones a motor
Normal/Despegue/Aterrizaje, y los helicópteros Normal (arranque,
despegue/aterrizaje) / Idle Up 1 (acrobacia) / Idle Up 2 (3D). Liberan al
piloto de la mayor parte del trabajo de conmutación manual y de reajuste de
los compensadores: un modo de vuelo puede tener sus propios compensadores
independientes y puede condicionar tanto las [Variables](variables.md) como
las [Mezclas](mixes.md); combinando ambas cosas hay de sobra para una
complejidad real. Consulte el [Ejemplo básico de ala
fija](../tutorials/basic-fixed-wing.md) para ver los modos de vuelo
aplicados a un modelo real.

Por defecto no hay definido ningún modo de vuelo. Toque en el modo de vuelo
predeterminado y seleccione **Editar** para cambiarle el nombre, o
**Agregar** para crear uno nuevo: hasta 20 en total.

## Nombre

Un nombre descriptivo: Crucero, Velocidad, Térmica, Despegue, Aterrizaje,
lo que mejor encaje.

## Condición activa

![Formulario del modo de vuelo](../assets/model-fm-form.png)

Un modo de vuelo nuevo comienza inactivo (`---`). Una vez definida, la
condición puede establecerse eligiendo entre posiciones de interruptores o
botones, interruptores de función, interruptores lógicos, un evento del
sistema (como el corte o la retención del acelerador) o posiciones de
trimado.

El modo de vuelo **predeterminado** no tiene ninguna condición activa: es el
que está activo siempre que no se cumpla la condición de ningún otro modo de
vuelo. Solo puede haber un modo de vuelo activo a la vez: el primero (en
orden de prioridad) cuya condición sea cierta en ese momento. El modo activo
se muestra en negrita.

!!! warning "Añadir un modo de vuelo a un modelo existente"
    Un modo de vuelo recién añadido está, por defecto, activo en todas las
    mezclas que ya dependen de los modos de vuelo; compruebe que cada una de
    esas mezclas sigue comportándose correctamente, en particular una mezcla
    de **Bloqueo** que fije un canal a un modo de vuelo concreto.

## Fade in, out

Tiempos de transición para pasar suavemente de un modo de vuelo a otro (por
ejemplo, 1 segundo en cada sentido); esto solo tiene efecto sobre las
mezclas que a su vez dependen de los modos de vuelo.

## Gestión de los modos de vuelo

![Mover modo de vuelo](../assets/model-fm-move.png)
![Seleccionar para mover](../assets/model-fm-move-select.png)
![Modos 0-3](../assets/model-fm-0to3.png)

Toque en un modo de vuelo para **Editar**, **Agregar**, **Clonar** o
**Eliminar**. Un modo de vuelo **clonado** hereda los ajustes de su origen
en todas las mezclas que utilizan modos de vuelo —mismo comportamiento,
mismo estado activo/inactivo—, por lo que el clon se añade por defecto como
último modo de vuelo, para no interferir con los ya existentes. **Mover**
cambia la prioridad de un modo de vuelo: la prioridad sigue un orden
ascendente y, como se ha indicado arriba, el primero cuya condición sea
cierta es el que está activo.
