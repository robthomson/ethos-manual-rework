---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sistema RF

Configura el/los módulo(s) RF interno y/o externo del modelo, el ID de
registro del propietario, el binding del receptor y las opciones del
receptor. Aquí también reside la elección entre módulo interno y externo
de cada modelo: a diferencia de casi todo lo demás en
[Configuración del sistema](../system-setup/index.md), la selección del
hardware RF es **por modelo**, no global de la emisora.

!!! note "Capturas de pantalla pendientes"
    El conjunto de capturas de pantalla de esta sección aún no se ha
    obtenido (véase
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)): el
    contenido siguiente es correcto, pero por ahora solo es texto.

## ID de registro del propietario {: #owner-registration-id }

Un código único de 8 caracteres (combinación de letras mayúsculas y
minúsculas y dígitos, sin caracteres especiales) que pasa a ser el
**ID de registro** de un receptor al registrarlo. Configura el *mismo*
código en varias emisoras para poder usar **Smart Share** entre ellas;
hazlo antes de crear el modelo que quieras compartir. Compatible con
EdgeTX; solo parcialmente compatible con OpenTX.

## Desactivar la salida RF

Mantén pulsado `PAGE` durante el encendido para desactivar la salida RF
interna y externa durante esa sesión (un aviso confirma que está
desactivada). El ajuste **Estado** del módulo permanece en ON: un
reinicio normal restablece la transmisión normal.

## Modos del módulo interno

El módulo interno de la X18/X20/X20S/X20HD (TD-ISRM) funciona en uno de
tres modos; el módulo TD-ISRM Pro de la X20 Pro/R/RS es similar, pero
añade LoRa y variantes tándem de doble banda. Cualquiera que sea el modo
seleccionado, **debe coincidir con lo que admita el receptor** o el
binding fallará; después de cambiar de modo, vuelve a verificar
cuidadosamente cada canal y, en especial, el comportamiento del failsafe.

- **ACCESS**: las rutas de 2.4GHz y 900MHz funcionan en tándem bajo un
  único conjunto de controles ACCESS. Hasta tres receptores en total, en
  cualquier combinación de 2.4GHz (24 canales) y 900MHz (16 canales); la
  telemetría de ambas bandas está activa simultáneamente, etiquetada por
  banda. Una fuente de telemetría **RX** indica qué receptor es la fuente
  de telemetría activa en ese momento.
- **ACCST D16**: una única ruta de 2.4GHz, para receptores heredados de
  la serie "X".
- **Modo TD**: tándem 2.4GHz + 900MHz de baja latencia y largo alcance
  para receptores Tandem, 24 canales en cada banda.

Las compilaciones del **firmware Flex** añaden una segunda columna Tipo
para alternar entre la modulación FLEX915M (915MHz estilo FCC) y FLEX868M
(868MHz estilo LBT) bajo cualquiera de los tres modos anteriores; deben
instalarse las antenas correspondientes a la opción seleccionada. Los
usuarios de la UE pueden emplear 200/500mW en 868MHz; a 25mW la
telemetría viaja por 868MHz, y a 200/500mW pasa a 2.4GHz por motivos de
conformidad.

Cada combinación de modo y rango de canales implica un compromiso en la
tasa de actualización: por ejemplo, con ACCESS, 8 canales se actualizan
cada 7ms, 16 cada 14ms y 24 cada 21ms (rotando en bloques de 8), y hay
disponible un **modo Racing** de 4ms en los canales 1-8 con receptores
compatibles (serie RS, v2.1.7 o superior).

## Registro y binding de un receptor (ACCESS) {: #registering-and-binding-a-receiver-access }

El binding de un receptor ACCESS consta de dos fases: el **registro**
solo hay que realizarlo una vez por cada pareja receptor/emisora; el
**binding** puede repetirse después de forma inalámbrica sin necesidad
del botón de bind.

**Fase 1 — Registro**:

1. Pulsa **Register** (omite este paso por completo si el receptor ya
   está registrado).
2. Mantén pulsado el botón de bind del receptor mientras lo enciendes;
   espera a que se iluminen ambos LED. El diálogo cambia de "Waiting for
   receiver…" a "Receiver connected" y completa automáticamente el nombre
   del receptor.
3. Confirma o edita el **ID de registro** (por defecto, el ID de registro
   del propietario indicado arriba: que los ID coincidan entre emisoras
   es lo que hace funcionar Smart Share), el **nombre del Rx** y el
   **UID**. El UID distingue varios receptores usados juntos en un mismo
   modelo: déjalo en 0 para un único receptor; con varios (por ejemplo,
   uno por cada bloque de 8 canales) lo habitual es usar 0/1/2. El UID no
   se puede leer del receptor después, así que etiquétalo físicamente.
4. Pulsa **Register**, confirma "Registration ok" y apaga el receptor:
   está registrado pero aún no vinculado.

**Fase 2 — Binding**:

!!! warning
    Nunca realices el binding con un motor eléctrico conectado o un motor
    de explosión en marcha.

1. Receptor apagado; confirma que estás en el modo de módulo correcto.
2. Pulsa **RX1** (o 2/3) → **Bind**. Un aviso de voz repetido "Bind"
   confirma el modo de binding.
3. Enciende el receptor **sin** tocar su botón de bind; selecciónalo en
   la lista "Select device" que aparece.
4. Confirma "Bind successful". Apaga y enciende tanto la emisora como el
   receptor: LED verde del receptor encendido y rojo apagado significa
   que está vinculado. No es necesario repetir el binding salvo que se
   sustituya uno de los dos elementos.
5. Repite el proceso para receptores adicionales (RX2, RX3) si los usas.

## Opciones del receptor

Con el receptor encendido, pulsa su botón RX para acceder a:

- **Options**: **Telemetry** (activada/desactivada para este receptor),
  **Reduced telemetry power 25mW** (frente a los 100mW normales; útil si
  servos cercanos captan interferencias RF), **High PWM Speed**
  (actualización de servo de 7ms en lugar de 18ms; comprueba que tus
  servos puedan seguir ese ritmo), **Telemetry port**
  (S.Port/F.Port/FBUS), **SBUS** (16 o 24 canales; todos los
  dispositivos SBUS conectados deben admitir SBUS-24 antes de activarlo)
  y **Channel Mapping** para reasignar canales a pines concretos del
  receptor.
- **Share**: cede el receptor a otra emisora ACCESS con un ID de registro
  del propietario *distinto*. En la emisora de origen, pulsa Share (su
  LED verde se apaga); en la emisora de destino, realiza el Bind
  normalmente: Share omite el nuevo registro porque el ID se transfiere
  automáticamente. Sal en la emisora de origen para finalizar la
  compartición; volver a hacer el binding lo devuelve. (No es necesario
  en absoluto si todas las emisoras ya comparten un mismo ID de registro
  del propietario: basta con hacer el binding directamente en la emisora
  que deba controlarlo.)
- **Reset bind**: limpia el estado tras un Share y restaura tu propio
  binding; apaga y enciende el receptor después.
- **Factory reset**: restablece el receptor y borra su UID,
  desregistrándolo por completo.

Con el receptor **apagado**, el mismo botón RX ofrece **Options**
(espera a que el receptor se conecte), **Bind** (por ejemplo, para volver
a vincular un receptor previamente vinculado en otro lugar) y **Clear**
(equivalente a Reset bind).

## Receptores redundantes {: #redundant-receivers }

Se puede vincular un segundo receptor a una ranura RX libre para lograr
redundancia: 2.4G y 900M pueden respaldarse mutuamente. La redundancia de
FrSky se evalúa **trama a trama**, usando siempre la mejor trama
disponible (conmutación activo/activo), por lo que el control puede
alternar entre receptores de una trama a otra según sea necesario.

1. Conecta la salida SBUS Out del receptor redundante a la entrada SBUS
   In del receptor principal.
2. Activa el módulo RF interno correspondiente (por ejemplo, 900M) y
   configura su antena y potencia.
3. Registra el nuevo receptor (si no lo está ya) y vincúlalo a la ranura
   RX libre como se ha descrito arriba.
4. Comprueba que su LED verde esté encendido: ya aparece como receptor
   redundante.

## Failsafe {: #failsafe }

Los datos de failsafe se reenvían desde la emisora aproximadamente cada
10 segundos; en los receptores TD/TW/AP/AP Plus también se guardan en el
propio receptor, por lo que se conservan tras un reinicio del receptor.
Vuelve a comprobar cuidadosamente el failsafe después de cualquier
actualización de firmware del receptor que añada este comportamiento.

- **Hold**: mantiene las últimas posiciones de canal recibidas.
- **Custom**: por canal: **Not Set**, **Hold**, **Custom** (un valor
  fijo; pulsa el icono de flecha para capturar el valor actual o
  introduce uno directamente) o **No Pulses**.
- **No Pulses**: detiene los pulsos por completo, para controladoras de
  vuelo que tienen su propio comportamiento de retorno al punto de
  origen ante pérdida de señal.
- **Receiver**: (receptores serie X o posteriores) configura el failsafe
  en el propio receptor.

!!! warning
    Prueba cuidadosamente la configuración de failsafe que elijas antes
    de confiar en ella.

## Prueba de alcance {: #range-check }

Realízala en el campo de vuelo antes de cada sesión con una configuración
nueva o modificada. Al seleccionar **Range Check** se reduce
deliberadamente la potencia de transmisión (un aviso de voz repetido
confirma el modo) y se muestran VFR%/RSSI en tiempo real para evaluar la
calidad del enlace. El nivel de potencia de la prueba de alcance de FrSky
es de aproximadamente −10dB respecto al nivel de funcionamiento normal de
+20dB; a 1m de altura tanto para la emisora como para el receptor, cabe
esperar una alarma crítica en torno a los 30m; una distancia menor en
condiciones normales puede indicar un problema.

Con varios receptores vinculados, los datos de la prueba de alcance se
muestran para un receptor activo a la vez por banda: al apagar el que
está activo, el siguiente (en prioridad 0/1/2, indicada mediante el
sensor **RX**) toma el relevo, de modo que puede comprobarse cada uno por
turno.

## Módulos RF externos y de terceros

Los módulos externos de FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN
Lite Pro) siguen el mismo patrón de registro/binding que el módulo
interno, con recuentos de canales, niveles de potencia y requisitos de
antena específicos de cada protocolo; consulta el manual del módulo
concreto para conocer las cifras exactas.

**ELRS** (ExpressLRS) es compatible tanto a través del modo ELRS del
módulo TWIN Lite Pro como mediante módulos ELRS genuinos (que requieren
el script Lua de ELRS instalado en `scripts/elrs` para aparecer como
opción de módulo). Doce canales; los ajustes principales son
**Packet Rate** (compromiso entre latencia y alcance),
**Telemetry Ratio** (con qué frecuencia se envía la telemetría, de 1:1 a
1:128), **Switch Mode** (**Hybrid**: la mayoría de los canales auxiliares
se reducen a 2–3 posiciones para menor latencia; o **Wide**: resolución
completa de 64–128 pasos), **Model Match** y **Tx Power** (10mW–1000mW,
con **Dynamic Power** opcional para escalar automáticamente según la
calidad del enlace; requiere la telemetría activada).

Los **módulos de terceros** (actualmente Ghost, Multi-protocol,
Crossfire, además de ELRS) requieren cada uno su propio script Lua
instalado por el usuario; consulta las notas sobre `scripts/` en
[Screenshot Pipeline](../contributing/screenshot-pipeline.md) y el hilo
*Third-Party External Modules* en rcgroups. La entrada de un módulo solo
aparece en la pantalla RF una vez instalado su script. El módulo
Multi-protocol (IRX4 Lite) puede además actualizarse su firmware
directamente desde el
[Gestor de archivos](../system-setup/file-manager.md): copia el archivo
de firmware en `Firmware/` y selecciona **Flash external multimodule**.
