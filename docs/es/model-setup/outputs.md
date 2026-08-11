---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Salidas

![Salidas](../assets/model-outputs.png)

Las salidas son la frontera entre la "lógica" pura de las [Mezclas](mixes.md) y
el mundo físico: servos, varillajes, superficies de control, actuadores,
transductores. Es donde los recorridos finales, la inversión, el centrado y las
curvas de corrección se adaptan a lo que el modelo realmente necesita
mecánicamente. Cada canal de salida corresponde a una salida de servo del
receptor (CH1 → conector de servo n.º 1, con la configuración de protocolo
predeterminada).

Ethos trabaja en porcentajes, pero los servos se accionan en última instancia
mediante el ancho de pulso PWM en microsegundos:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Un canal **sin ninguna mezcla activa** emite el valor neutro (0% / 1500µs);
    esto incluye un canal cuya única mezcla (o mezclas) esté inactiva en ese
    momento. Asegúrate de que todo canal que realmente utilices tenga siempre
    una mezcla activa que lo respalde. En un canal de acelerador en particular,
    el neutro significa **medio gas**.

La pantalla de Salidas muestra dos barras por canal: la barra inferior (verde)
es el valor del mezclador para ese canal, y la barra superior (naranja) es el
valor posterior a las Salidas que realmente se envía al receptor (tanto en %
como en µs). Los límites Mín/Máx aparecen como secciones atenuadas de la barra
naranja. Los canales que no se están transmitiendo en ese momento al módulo de
RF tienen un fondo más oscuro. En un canal aparecen pequeños iconos cuando sus
ajustes de Dirección, Curva, Lento o Balance se han modificado respecto al
valor predeterminado, como forma de identificar de un vistazo los canales no
predeterminados.

!!! tip
    Una pulsación larga de `ENT` desde la pantalla de Mezclas o de Fases de
    vuelo lleva directamente aquí.

## Edición de un canal {: #editing-a-channel }

![Editar la salida de profundidad](../assets/model-outputs-elevator-edit.png)
![Editar la salida de acelerador](../assets/model-outputs-throttle-edit.png)

Toca un canal para abrirlo. Una vista previa en la parte superior muestra el
valor de la mezcla (verde) frente al valor de salida (naranja), con un pequeño
marcador blanco para los puntos Mín/Máx.

- **Nombre**: editable.
- **Dirección**: invierte la salida del canal, normalmente para invertir el
  sentido de giro del servo. Se muestra como un icono de doble flecha en el
  canal. Esto **no** afecta a las mezclas que lo alimentan y **no** intercambia
  los límites Mín/Máx.
- **Mín/Máx**: límites absolutos que nunca se sobrepasan; ajústalos para evitar
  bloqueos mecánicos. Actúan como ajustes de recorrido final/ganancia: al
  reducirlos se reduce el recorrido en lugar de provocar recortes. El valor
  predeterminado es ±100%, ajustable hasta ±150%. Durante el ajuste, el extremo
  hacia el que se está moviendo en ese momento se muestra en negrita (por
  ejemplo, empuja el stick de profundidad hacia delante y el valor Máx se pone
  en negrita, para confirmar que ese es el extremo que estás ajustando).

  ![Advertencia de redundancia SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Redundancia SBUS"
      Una configuración de redundancia que use SBUS no puede mover un servo más
      allá de aproximadamente ±125%. Los propios campos Mín/Máx tienen rangos
      asimétricos (−150–0% y 0–150%): si los accionas desde una
      [Variable](variables.md), asigna a esa variable un rango idéntico o activa
      **Ignorar rango** (consulta [opciones de
      fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      o la conversión automática de rango producirá valores inesperados. Si la
      salida del receptor principal supera el 125% y este entra en failsafe, el
      receptor redundante que toma el control mediante SBUS la limitará de nuevo
      al 125%.

- **Centro/Subtrim**: desplaza la salida, normalmente para centrar el brazo de
  un servo; los recorridos finales no se ven afectados.

  !!! warning
      No uses el subtrim para desplazamientos grandes: introduce un diferencial
      considerable en la respuesta del servo. Utiliza en su lugar una **mezcla
      de offset** para cualquier cosa que vaya más allá de un centrado fino.

- **Centro PWM**: similar al subtrim, pero desplaza *toda* la banda de recorrido
  del servo, incluidos los límites absolutos, de forma efectiva dentro del
  propio servo en lugar de mostrarse en el monitor de canales. Esto mantiene el
  centrado mecánico separado del trimado.
- **Curva**: asocia una curva Expo o personalizada (existente o nueva, con un
  atajo **Editar** una vez asignada) para corregir la respuesta real; por
  ejemplo, para que los flaps izquierdo y derecho se sigan con precisión. Se
  muestra como un icono de curva en el canal.
- **Lento subida/bajada**: ralentiza la respuesta de la salida a los cambios de
  entrada, en segundos para recorrer 0→100%; por ejemplo, para ralentizar un
  tren retráctil accionado por un servo proporcional ordinario. Se muestra como
  un icono de reloj en el canal. (Un **retardo**, distinto de "lento", está
  disponible en los [interruptores lógicos](logical-switches.md)).

## Intercambiar canales {: #swap-channels }

![Intercambiar canales](../assets/model-outputs-swap-channels.png)
![Elegir el canal a intercambiar](../assets/model-outputs-swap-channels-select.png)

Intercambia dos canales de salida. El diálogo se abre con el canal actual ya
seleccionado; elige el otro y confirma. El intercambio es inmediato y todas las
mezclas que hagan referencia a cualquiera de los dos canales se actualizan en
consecuencia.

## Restablecer ajustes

![Restablecer canal](../assets/model-outputs-reset-select.png)

Borra todos los parámetros de un canal y los devuelve a sus valores
predeterminados; resulta útil antes de reutilizar un canal para otra función, y
cuenta con un diálogo de confirmación para evitar accidentes.

## Balancear canales {: #balance-channels }

![Elegir los canales a balancear](../assets/model-outputs-balance-choose_channels.png)
![Elegir CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Balancea una pareja (o hasta 4) de canales para que se muevan al unísono; por
ejemplo, unos flaps que no se mueven de forma solidaria pueden inducir un
alabeo no deseado, y unos aceleradores desequilibrados en un modelo
multimotor pueden inducir una guiñada no deseada. Ethos crea una curva de
balance diferencial por cada canal seleccionado; comparar las posiciones
físicas de las superficies en cada punto de la curva permite ajustarlas para
que coincidan, logrando finalmente un seguimiento perfecto entre superficies.

**Antes de balancear**, en este orden:

1. Ajusta las direcciones de los servos para un recorrido correcto.
2. Con las mezclas en neutro, utiliza opcionalmente el **Centro PWM** para
   escuadrar los brazos de los servos.
3. Ajusta Mín/Máx y Subtrim.
4. Configura cualquier otra curva.
5. Configura Lento.
6. *Entonces* balancea e iguala a lo largo de todo el rango de recorrido.

**Uso**: elige los canales a balancear y el orden en que se mostrarán:

![CH7/CH6 seleccionados](../assets/model-outputs-balance-ch7-and-ch6.png)

La salida de la mezcla se representa en el eje X y el diferencial de ajuste de
balance en el eje Y. Toca el gráfico de un canal (o selecciónalo y pulsa `ENT`)
para editar su curva de balance; `PAGE` cambia entre canales durante la
edición:

![Editor de curva de balance](../assets/model-outputs-balance-curve-edit.png)

Controles del editor:

- **Fuente**: normalmente la propia fuente (o fuentes) de la mezcla, o
  cualquier otra entrada analógica que resulte cómoda; **Entrada analógica
  automática** toma como X el primer stick/deslizador/potenciómetro que muevas,
  tanto en el gráfico como en el propio modelo.
- **Imán**: hace que el ajuste del encoder rotativo se enganche automáticamente
  al punto de curva más cercano del eje X:

  ![Imán desactivado](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Imán activado](../assets/model-outputs-balance-ch6-magnet-on.png)

  Aún es necesario mover la entrada para alinear X con un punto de la curva
  antes de poder ajustarlo.
- **Bloqueo**: se activa tocando su icono o pulsando `ENT` en el modo de edición
  del gráfico; bloquea todas las entradas para que puedas soltar el stick y
  observar las superficies de control mientras ajustas la curva.
- **Configuración**: permite cambiar el número de puntos por canal (todos o
  individualmente) y si cada curva se suaviza.
- **Ayuda** (`?`, también la tecla `MDL`): abre la ayuda integrada.

**Multicanal**: se pueden balancear hasta 4 canales conjuntamente:

![Balance de 4 canales](../assets/model-outputs-balance-ch2-9-8-1.png)

Una vez configurada, una curva de balance se puede revisar, editar o borrar
desde la propia página de configuración del canal; un icono de balance la
identifica en el gráfico del canal (junto con un icono de Dirección, si este
también difiere del valor predeterminado).
