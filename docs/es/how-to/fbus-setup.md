---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Configurar un sistema FBUS

El protocolo [FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works)
(antes F.Port2) integra en una sola línea el control y la telemetría, lo que
permite que varios dispositivos FBUS compartan una única conexión en cadena
con configuración inalámbrica completa. En este ejemplo configuraremos dos
servos Xact en los canales de los alerones (1 y 5) del [Ejemplo básico de
avión de ala fija](../tutorials/basic-fixed-wing.md).

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas del simulador — consulta [Proceso de
    capturas de pantalla](../contributing/screenshot-pipeline.md).

## 1. Descargar el firmware más reciente

FBUS requiere el uso del firmware más reciente tanto en receptores como en
dispositivos — por ejemplo, el firmware de los servos Xact debe ser al menos
v2.0.1. Descargue las actualizaciones pertinentes de la
[sección de descargas de la web de FrSky](https://www.frsky-rc.com/download/).

## 2. Actualizar el firmware

Copie los archivos de firmware en la carpeta `Firmware/` de la SD card/eMMC.
En el [Gestor de Archivos](../system-setup/file-manager.md), enchufe el cable
del servo en la conexión S.Port de la parte superior de la radio (el cable
blanco o amarillo va al lado que tiene una muesca), seleccione el archivo de
firmware y elija **Flashear dispositivo externo**.

## 3 / 5. Configurar las IDs Físicas

Ambos servos vienen por defecto con la ID Física `0C` hex y la ID de
Aplicación `6800` hex — entrarán en conflicto en el bus compartido a menos que
se cambie uno de ellos. Hay dos formas de hacerlo, según el tipo de receptor:

**Mediante el conector S.Port de la radio** (cualquier receptor):

1. Conecte el servo 1, vaya a **Conf. Dispositivos → XAct** y ajuste
   **Módulo** al **conector S.Port**. Deje la ID Física `0C`/ID de Aplicación
   `6800` y el canal `CH1` con sus valores por defecto, y después seleccione
   el botón **Guardar en flash**.
2. Conecte ahora el servo 2 en su lugar, en el mismo menú. Cambie la **ID
   Física** a `0D` hex y la **ID de Aplicación** a `6801` hex (consulte la
   [Tabla de ID Física](../model-setup/telemetry.md#how-frsky-telemetry-works)
   en la sección de Telemetría para ver qué opciones están libres), cambie el
   **Canal** a `CH5` y seleccione **Guardar en flash**.

**Directamente a través del receptor** (por ejemplo, un TD-R18 Tandem, con
ambos servos conectados a la vez — vea el [Paso
4](#4-configure-the-receiver-for-fbus)):

1. Teniendo solamente el primer servo conectado (por ejemplo, al Pin1 del
   receptor), vaya a **Conf. Dispositivos → XAct**, **Módulo** → **Módulo
   Interno**. Confirme los valores por defecto (`0C`/`6800`/`CH1`) y
   seleccione **Guardar en flash**.
2. Con sólo el segundo servo conectado (Pin5), en el mismo menú (Conf.
   Dispositivos sólo puede conectarse a un servo a la vez) — cambie a
   `0D`/`6801`/`CH5` y seleccione **Guardar en flash**. Después, vuelva a
   seleccionar Conf. Dispositivos para confirmar que el cambio se ha guardado.

## 4. Configurar el receptor para FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [Sistema RF](../model-setup/rf-system.md) → el botón del
receptor → **Opciones** → ajuste el **Puerto de Telemetría** a **FBUS**. Los
servos Xact pueden conectarse en cadena desde ese puerto; como cada servo
sólo tiene un conector, un extensor multicanal F.Port 2.0 (FP2CH4/6/8)
permite ampliar el circuito a varios servos.

**TD-R18 Tandem**: Sistema RF → el botón del receptor → **Opciones** →
ajuste los pines individuales (por ejemplo, **Pin1** y **Pin5**) a **FBUS**
— puede reasignar a FBUS tantos pines como requiera, con lo que se evita
usar alargadores multicanales por completo; todos los pines programados
como FBUS llevan exactamente la misma señal FBUS.

## 5. Comprobar el control FBUS de los servos

Conecte el servo 1 en la posición Pin1 y el servo 2 en la posición Pin5 (los
canales de los alerones del ejemplo de ala fija), encienda el sistema y
compruebe que los canales 1 y 5 operan los servos correctos.

## 6. Comprobar la telemetría FBUS

Con ambos servos enchufados, borre todos los sensores `SRV` existentes en
[Telemetría](../model-setup/telemetry.md) y vuelva a descubrirlos. Cada servo
informa de 4 sensores: amperaje, voltaje, temperatura y estado (`OK` con
todo normal).

## 7. Hacer cambios de configuración más adelante

En un modelo ya completamente cableado, no es práctico aislar un servo para
reconfigurarlo a través de Conf. Dispositivos. En lugar de eso: vaya a
Telemetría, busque un sensor correspondiente al servo que desea reconfigurar
(por ejemplo, `SRV1 curr`) y seleccione **Configurar** — se abrirá
directamente la pantalla de configuración de ese servo. Acuérdese de
seleccionar **Guardar en flash** después de hacer cualquier cambio.

!!! warning
    Tenga cuidado de no cambiar por accidente la ID Física ni la ID de
    Aplicación desde esta pantalla — son las que permiten que cada servo
    siga siendo direccionable en el bus compartido.
