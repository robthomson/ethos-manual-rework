---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Fases de vuelo

![Fases de vuelo](../assets/model-fm.png)

Las fases de vuelo (flight modes) permiten que un interruptor seleccione
entre comportamientos distintos para un mismo modelo: los veleros pueden
usar Lanzamiento/Crucero/Velocidad/Térmica, los aviones a motor
Normal/Despegue/Aterrizaje, y los helicópteros Normal (arranque,
despegue/aterrizaje) / Idle Up 1 (acrobacia) / Idle Up 2 (3D). Liberan al
piloto de la mayor parte del trabajo de conmutación manual y de reajuste de
trims: una fase de vuelo puede llevar sus propios trims independientes y
puede condicionar tanto las [Variables](variables.md) como las
[Mezclas](mixes.md); en conjunto, eso basta para lograr una complejidad
real. Consulte el [Ejemplo básico de ala
fija](../tutorials/basic-fixed-wing.md) para ver las fases de vuelo
aplicadas a un modelo real.

Por defecto no hay ninguna fase de vuelo definida. Toque la fase de vuelo
predeterminada y elija **Editar** para cambiarle el nombre, o **Añadir**
para crear una nueva: hasta 20 en total.

## Nombre

Un nombre descriptivo: Crucero, Velocidad, Térmica, Despegue, Aterrizaje,
lo que mejor encaje.

## Condición de activación

![Formulario de fase de vuelo](../assets/model-fm-form.png)

Una fase de vuelo nueva comienza inactiva (`---`). Una vez configurada,
puede accionarse mediante la posición de un interruptor o botón, un
interruptor de función, un interruptor lógico, un evento del sistema (corte
o retención de gas) o la posición de un trim.

La fase de vuelo **predeterminada** no tiene ninguna condición de
activación: es la que está activa siempre que no se cumpla la condición de
ninguna otra fase de vuelo. Solo puede haber una fase de vuelo activa a la
vez: la primera (en orden de prioridad) cuya condición sea verdadera en ese
momento. La fase activa se muestra en negrita.

!!! warning "Añadir una fase de vuelo a un modelo existente"
    Una fase de vuelo recién añadida está, por defecto, activa en todas las
    mezclas que ya dependen de fases de vuelo; compruebe que cada una de
    esas mezclas sigue comportándose correctamente, en particular una
    mezcla **Lock** que bloquee un canal en una fase de vuelo concreta.

## Fade in, out

Tiempos de transición para fundir suavemente entre fases de vuelo (por
ejemplo, 1 segundo en cada sentido); esto solo afecta a las mezclas que a su
vez dependen de las fases de vuelo.

## Gestión de las fases de vuelo

![Mover fase de vuelo](../assets/model-fm-move.png)
![Seleccionar para mover](../assets/model-fm-move-select.png)
![Fases 0-3](../assets/model-fm-0to3.png)

Toque una fase de vuelo para **Editar**, **Añadir**, **Clonar** o
**Eliminar**. Una fase de vuelo **clonada** hereda los ajustes de su origen
en todas las mezclas que utilizan fases de vuelo —mismo comportamiento,
mismo estado activo/inactivo—, por lo que un clon se añade por defecto como
última fase de vuelo, para evitar interferir con las existentes. **Mover**
cambia la prioridad de una fase de vuelo: la prioridad sigue un orden
ascendente y, como se indicó arriba, la primera cuya condición sea
verdadera es la que está activa.
