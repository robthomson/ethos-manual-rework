# Ejemplo de configuración inicial de la radio

Esta sección describe los pasos iniciales para configurar la radio en sí, antes de programar cualquier modelo específico. Una vez completados, se puede seguir cualquiera de los ejemplos de programación de las secciones siguientes.

Nota: Estos ejemplos no son de tipo "receta de cocina". Suponen que el usuario tiene un conocimiento básico del vocabulario de los modelos de radiocontrol y está familiarizado con la navegación por la estructura de menús de Ethos. Si en algún momento se siente confuso, consulte las secciones anteriores de este manual para refrescar la memoria. En particular, consulte la sección  [Interface de Usuario y Navegación](../getting-started/user-interface-and-navigation.md) para familiarizarse con la interfaz de usuario de la radio, de modo que pueda encontrar fácilmente la página de configuración que necesita.

## Paso 1. Cargue la radio y las baterias de vuelo.

Cargue la batería de la radio siguiendo las instrucciones que recibió con la radio. Cargue también las baterías del avión que vaya a utilizar, utilizando un cargador adecuado para el tipo o tipos de batería, observando todas las precauciones de seguridad, especialmente cuando utilice baterías de Litio.

## Paso 2. Calibrar el hardware.

Asegúrese de haber realizado la calibración del hardware durante el arranque inicial de la radio, incluidos los giróscopos, para confirmar que la radio sabe exactamente dónde están los centros y los límites de cada palanca, potenciómetro y deslizador. También debería repetirse cada vez que se actualice el firmware y siguiendo las instrucciones que se encuentran en la sección System \\ Hardware \\ [Calibración](../system-setup/hardware.md) de este manual.

## Paso 3. Realice la configuración del sistema de la emisora.

La Configuración del sistema de la emisora se utiliza para configurar aquellas partes del hardware del sistema de la radio que son comunes a todos los modelos. Se diferencia de las funciones de 'Configuración del modelo' en que configuran los ajustes específicos para cada modelo.

Lea la sección Configuración del sistema para familiarizarse con todos los ajustes de esta sección.

Muchos ajustes pueden dejarse (al menos inicialmente) en sus valores predeterminados, pero conviene revisar los siguientes:

### Fecha & Hora

Ajuste la hora y la fecha actuales.

### Audio

Ajuste los anuncios y avisos por voz de la radio, incluidos sus anuncios personalizados. Vaya a la sección [General / Audio / Elección de Voces](#Choice of Voices).

### Palancas

#### Modos de las palancas

Seleccione el modo predeterminado de las palancas que prefiera. El modo 1 tiene el acelerador y los alerones en el mando derecho, y la profundidad y el timón de dirección en el izquierdo. El modo 2 tiene el acelerador y el timón de dirección en la palanca izquierda, y el alerón y el elevador en el derecho.

**Nota:** El modo 2 es el predeterminado.

**Precaución**: si un modelo está configurado en modo 2 y la radio está en mod 1, es posible que en modelos eléctricos el motor acelere repentinamente cuando se encienda la radio.

#### Orden de los Canales

El orden de canales por defecto para Ethos es AETR (es decir, Alerón, Elevador, Acelerador, Timón). Es posible que prefiera establecer el orden de canales por defecto en el orden al que esté acostumbrado. TAER es el predeterminado para Spektrum/JR, y AETR es el predeterminado para Futaba/Hitec. Este ajuste define el orden en el que se insertan las cuatro entradas de las palancas cuando se crea un nuevo modelo. Por supuesto, pueden cambiarse posteriormente.

##### Receptores estabilizados FrSky

Tenga en cuenta que AETR es el orden requerido si desea utilizar cualquiera de los receptores estabilizados de FrSky. Sin embargo, para modelos con más de una superficie en alerones, profundidad, dirección, flaps, etc. el asistente normalmente agrupará estas superficies, así que por ejemplo obtendrías AAETR si usas 2 canales de Alerones.

Los receptores SRx esperan un orden de canales de AETRA o AETRAE, por lo que se puede indicar al asistente (en Sistema / palancas) que mantenga los 'Cuatro primeros canales fijos'.

### Batería

Revise las especificaciones de la batería de su radio y configure el 'Voltaje principal', 'Voltaje bajo' y 'Rango de voltaje de la pantalla' como se describe en la sección [Systema / Bater](../system-setup/battery.md)ía de este manual.

### ID de registro del propietario

El ID de registro de propietario se utiliza con los sistemas ACCESS. Este ID se convierte en el ID de registro durante el proceso de registro de un receptor. Introduzca el mismo ID de Registro de Propietario de los otros transmisores con los que desee utilizar la función SmartShareTM. Consulte la sección de configuración del modelo / [RF System](../model-setup/rf-system.md) de este manual (aunque se configura en la sección Configuración del modelo, el ID de registro del propietario se utilizará para cada nuevo modelo y puede considerarse un ajuste del sistema. Tenga en cuenta también que el ID de Registro de Propietario puede cambiarse para un receptor en particular durante el proceso de registro).

### Unidades

Tenga en cuenta que en Ethos las unidades de telemetría se configuran por sensor. No existe una configuración global métrica o imperial.
