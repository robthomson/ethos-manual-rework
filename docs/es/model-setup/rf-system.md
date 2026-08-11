---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sistema RF

Configura el módulo o los módulos de RF internos y/o externos del modelo,
el ID de registro de propietario, la vinculación de los receptores y las
opciones de receptor. Aquí reside también la elección entre módulo interno
y externo de cada modelo: a diferencia de casi todo lo demás en
[Configuración del sistema](../system-setup/index.md), la selección del
hardware de RF se realiza **por modelo**, no de forma global para la
emisora.

!!! note "Capturas de pantalla pendientes"
    El conjunto de capturas de pantalla de esta sección aún no se ha
    obtenido (véase
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)): el
    contenido siguiente es correcto, pero por ahora solo es texto.

## ID de registro del propietario {: #owner-registration-id }

Un código único de 8 caracteres (mezcla de mayúsculas, minúsculas y
números, sin caracteres especiales) que se convierte en el **ID de
Registro** del receptor al registrarlo. Introduzca el *mismo* código en
los otros transmisores con los que desee utilizar la función **Smart
Share**; esto debe hacerse antes de crear el modelo en el que desea
utilizarla. Es compatible con EdgeTX, pero solo parcialmente compatible
con OpenTX.

## Desactivar el módulo de RF

Los módulos internos y externos de RF se pueden desactivar manteniendo
pulsada la tecla `PAGE` mientras se enciende la radio (recibirá un aviso
de que el módulo está apagado). Sin embargo, el ajuste **Estado** de los
módulos de RF seguirá activo: si se reinicia la radio, se recuperará el
estado normal de emisión.

## Modos del módulo interno

El módulo interno de las radios X18/X20/X20S/X20HD (TD-ISRM) puede
funcionar en 3 modos; el módulo TD-ISRM Pro de la X20 Pro/R/RS es similar,
pero añade LoRa y variantes tándem de doble banda. El modo de transmisión
elegido **debe corresponderse con el que admite el receptor**, o no será
posible vincularlo. Después de cambiar el modo de operación, deberá
comprobar con mucho cuidado todos y cada uno de los canales del receptor y,
muy especialmente, el funcionamiento del Failsafe.

- **ACCESS**: las emisiones de RF de 2,4GHz y 900MHz trabajan en tándem
  con un único conjunto de controles ACCESS. Puede haber hasta tres
  receptores en total, en cualquier combinación de 2,4GHz (24 canales) y
  900MHz (16 canales); la telemetría de ambas bandas está activa al mismo
  tiempo, y los sensores se identifican por banda. Una fuente de
  telemetría denominada **RX** indica qué receptor es el que envía la
  telemetría en cada momento.
- **ACCST D16**: una única emisión en la banda de 2,4GHz, para los
  receptores de la serie "X".
- **Modo TD**: modo de largo alcance y baja latencia que utiliza en tándem
  los enlaces de 2,4GHz y 900MHz con los receptores Tandem, con 24 canales
  en ambas bandas.

Las versiones de **firmware Flex** añaden una segunda columna en el tipo de
modulación para alternar entre FLEX915M (915MHz, modulación FCC) y FLEX868M
(868MHz, modulación LBT europea) en cualquiera de los tres modos
anteriores; las antenas deberían cambiarse para ajustarse a la frecuencia
seleccionada. Los usuarios europeos pueden emplear 200mW y 500mW en la
banda de 868MHz: para cumplimiento de la normativa, si selecciona 25mW los
datos de telemetría se transmitirán vía 868MHz, pero con 200mW o 500mW la
telemetría se enviará por la banda de 2,4GHz.

La elección del modo y del rango de canales afecta al ritmo de
actualización de la información transmitida: por ejemplo, en ACCESS 8
canales se actualizan cada 7ms, 16 canales cada 14ms y 24 canales cada 21ms
(enviados en rotación por bloques de 8), y existe un **modo Carrera** de
4ms con el rango Ch1-8 y receptores compatibles (serie RS, v2.1.7 o
superior).

## Registro y vinculación de un receptor (ACCESS) {: #registering-and-binding-a-receiver-access }

La vinculación de un receptor ACCESS se realiza en dos fases: el
**registro** solo se necesita realizar una vez entre el receptor y el
transmisor; la **vinculación** puede repetirse después de forma
inalámbrica, sin necesidad de pulsar el botón de emparejamiento del
receptor.

**Primera fase — Registro**:

1. Pulse **Register** (omita este paso si el receptor ya está registrado).
2. Mientras mantiene pulsado el botón de enlace del receptor, enciéndalo y
   espere a que se activen ambos LED. El mensaje "Waiting for receiver…"
   cambia a "Receiver connected" y el campo con el nombre del receptor se
   rellena automáticamente.
3. Confirme o edite el **ID de registro** (su valor predeterminado es el
   ID de registro de propietario descrito anteriormente: que los ID
   coincidan entre transmisores es lo que hace funcionar Smart Share), el
   **nombre RX** y el **UID**. El UID se utiliza para distinguir entre
   varios receptores usados simultáneamente en un mismo modelo: puede
   dejarse en 0 para un solo receptor; con varios (por ejemplo, uno por
   cada bloque de 8 canales) lo habitual es usar 0/1/2. Tenga en cuenta
   que este UID no puede leerse de nuevo desde el receptor, por lo que es
   una buena idea etiquetarlo.
4. Pulse **Register**, confirme "Registration ok" y apague el receptor:
   está registrado, pero aún debe vincularse.

**Segunda fase — Vinculación**:

!!! warning
    No realice la operación de emparejamiento con un motor eléctrico
    conectado o un motor de combustión interna en marcha.

1. Receptor apagado; confirme que se encuentra en el modo de módulo
   correcto.
2. Pulse **RX1** (o 2/3) → **Bind**. Cada pocos segundos una alerta de voz
   anunciará "Bind" para confirmar que se encuentra en modo de
   vinculación.
3. Encienda el receptor **sin** tocar su botón de enlace; selecciónelo en
   la lista "Select device" que aparece.
4. Confirme "Bind successful". Apague y encienda tanto el transmisor como
   el receptor: si el LED verde del receptor está encendido y el rojo
   apagado, el receptor está enlazado. No será necesario repetir la
   vinculación, a menos que se sustituya uno de los dos.
5. Repita la operación para los receptores adicionales (RX2, RX3), si
   procede.

## Opciones del receptor

Con el receptor encendido, pulse sobre su botón RX para acceder a:

- **Options**: **Telemetry** (la telemetría se puede desactivar para este
  receptor), **Reduced telemetry power 25mW** (frente a los 100mW
  normales; puede ser necesaria si, por ejemplo, los servos experimentan
  interferencias de RF enviada cerca de ellos), **High PWM Speed**
  (velocidad de actualización PWM de 7ms en lugar de 18ms; asegúrese de
  que sus servos pueden manejar esta velocidad), **Telemetry port**
  (S.Port/F.Port/FBUS), **SBUS** (modo de canal de 16 o 24 canales; todos
  los dispositivos SBUS conectados tienen que soportar el modo SBUS-24
  para activarlo) y **Channel Mapping** para reasignar canales a los pines
  del receptor.
- **Share**: permite mover el receptor a otra radio ACCESS que tenga un ID
  de Registro de Propietario *diferente*. En la radio de origen, pulse
  Share (el LED verde del receptor se apaga); en la radio de destino,
  seleccione Vincular como de costumbre: el proceso Compartir omite el
  paso Registro, ya que el ID de registro del propietario se transfiere
  automáticamente. Pulse el botón EXIT de la radio de origen para detener
  el proceso Compartir; el receptor se puede volver a mover
  re-enlazándolo. (No es necesario utilizar Compartir si todas sus radios
  usan el mismo ID de propietario: basta con poner en modo de enlace la
  radio que desea utilizar y vincular el receptor directamente en ella.)
- **Reset bind**: limpia y restaura su vinculación después de un
  Compartir; reinicie el receptor a continuación.
- **Factory reset**: restablece el receptor a los ajustes de fábrica y
  borra su UID, con lo que también pierde el registro.

Con el receptor **apagado**, el mismo botón RX ofrece **Options** (la
radio intentará conectarse y esperará al receptor), **Bind** (por ejemplo,
para volver a vincular un receptor que había sido emparejado con otra
emisora) y **Clear** (equivalente a Reset bind).

## Receptores redundantes {: #redundant-receivers }

Se puede vincular un segundo receptor a un hueco RX no utilizado para
proporcionar redundancia: un receptor 2.4G o 900M puede ser el respaldo del
otro. La redundancia para el control que proporciona FrSky es siempre
evaluada "per-frame", eligiéndose siempre la mejor trama disponible
(activa/activa conmutada por fallo), por lo que el control puede alternarse
entre receptores con cada trama según sea necesario.

1. Conecte el puerto SBUS Out del receptor redundante al puerto SBUS In del
   receptor principal.
2. Active el módulo de RF interno correspondiente (por ejemplo, 900M) y
   configure su antena y su potencia.
3. Registre el nuevo receptor (si no lo estuviera ya) y vincúlelo al hueco
   RX libre como se ha descrito arriba.
4. Asegúrese de que su LED verde está encendido: el receptor redundante ya
   aparece en la lista.

## Failsafe {: #failsafe }

Los datos del modo a prueba de fallos se envían desde el transmisor cada 10
segundos aproximadamente; en los receptores TD, TW, AP y AP Plus los datos
se guardan además en el propio receptor, lo que significa que el failsafe
estará disponible inmediatamente si el receptor se reinicia por cualquier
razón. Tenga en cuenta que el modo a prueba de fallos debe restablecerse y
comprobarse después de actualizar los receptores con esta característica.

- **Hold**: mantendrá las últimas posiciones de mando recibidas.
- **Custom**: por canal, con las opciones **Not Set**, **Hold**, **Custom**
  (un valor fijo: pulse el icono Set con una flecha para utilizar el valor
  actual del canal, o introduzca uno directamente) o **No Pulses**.
- **No Pulses**: desactiva los pulsos, para uso con controladores de vuelo
  que tienen GPS de retorno a casa en caso de pérdida de señal.
- **Receiver**: (receptores de la serie X o posteriores) permite configurar
  el failsafe directamente en el receptor.

!!! warning
    Asegúrese de probar cuidadosamente los ajustes de Failsafe elegidos
    antes de confiar en ellos.

## Comprobación de alcance {: #range-check }

Se debe realizar en el campo antes de cada sesión de vuelo con una
configuración nueva o modificada. Al seleccionar **Range Check** se reduce
deliberadamente la potencia del transmisor (una alerta de voz repetida
confirma que se encuentra en ese modo) y se muestran los valores VFR% y
RSSI en tiempo real para evaluar cómo se está comportando la calidad de
recepción. El nivel de la comprobación de alcance de FrSky es de unos
−10dB respecto al nivel normal de funcionamiento de +20dB; en condiciones
ideales, con la radio y el receptor a 1 m del suelo, sólo debería obtener
una alarma crítica a unos 30 m de distancia: una distancia menor en
condiciones normales puede indicar un problema.

Con varios receptores vinculados, los datos de la comprobación de alcance
se proporcionan para un receptor a la vez en cada banda: si apaga el
receptor activo, el siguiente (en una prioridad de 0, 1 y luego 2, mostrada
por el sensor **RX**) se convertirá en el receptor de telemetría activo, de
modo que cada uno de ellos puede ser comprobado por turno.

## Módulos RF externos y de terceros

Los módulos externos de FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite
Pro) siguen el mismo patrón de registro y vinculación que el módulo
interno, con números de canales, niveles de potencia y requisitos de antena
propios de cada protocolo; consulte el manual del módulo correspondiente
para conocer las cifras exactas.

**ELRS** (ExpressLRS) es compatible tanto a través del modo ELRS del módulo
TWIN Lite Pro como mediante módulos ELRS de verdad (que necesitan el
correspondiente script Lua instalado en `scripts/elrs` para que aparezcan
como módulo opcional). Se admiten doce canales; los ajustes principales son
**Packet Rate** (compromiso entre alcance y latencia), **Telemetry Ratio**
(la frecuencia con la que se envían los datos de telemetría, de 1:1 a
1:128), **Switch Mode** (**Hybrid**: la mayoría de los canales auxiliares
sólo serán de 2 o 3 posiciones, para reducir la latencia; o **Wide**:
resolución completa de 64 a 128 pasos), **Model Match** y **Tx Power**
(10mW–1000mW, con **Dynamic Power** opcional para ajustar automáticamente
la potencia según la calidad del enlace; para ello debe tener activada la
telemetría).

Los **módulos de terceros** (actualmente Ghost, Multi-protocol y Crossfire,
además de ELRS) requieren cada uno su propio script Lua instalado
manualmente por el usuario; consulte las notas sobre `scripts/` en
[Screenshot Pipeline](../contributing/screenshot-pipeline.md) y el hilo
*Third-Party External Modules* en rcgroups. La selección de un módulo sólo
aparece en la pantalla de RF una vez instalado su script Lua. El módulo
Multi-protocol (IRX4 Lite) puede además actualizarse por firmware
directamente desde el
[Gestor de archivos](../system-setup/file-manager.md): copie el archivo de
firmware a la carpeta `Firmware/` y seleccione **Flash external
multimodule**.
