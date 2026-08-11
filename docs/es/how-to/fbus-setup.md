---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Configurar un sistema FBUS

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (antes
F.Port2) reúne el control y la telemetría en una sola línea, lo que permite
que varios dispositivos FBUS compartan una única conexión en cadena (daisy
chain) con configuración inalámbrica completa. Este recorrido conecta dos
servos Xact a los canales de alerones (1 y 5) del [Ejemplo básico de ala
fija](../tutorials/basic-fixed-wing.md).

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas del simulador — consulta [Proceso de
    capturas de pantalla](../contributing/screenshot-pipeline.md).

## 1. Descargar el firmware más reciente

FBUS requiere firmware actualizado tanto en el receptor como en los
dispositivos — por ejemplo, los servos Xact necesitan la versión v2.0.1 o
posterior. Obtén las actualizaciones correspondientes en la
[página de descargas de FrSky](https://www.frsky-rc.com/download/).

## 2. Instalar el firmware

Copia los archivos de firmware a la carpeta `Firmware/` de la SD card/eMMC.
En el [Gestor de archivos](../system-setup/file-manager.md), conecta el
servo al conector S.Port de la emisora (el cable blanco/amarillo hacia la
muesca), selecciona el archivo de firmware y elige **Flash External
Device**.

## 3 / 5. Configurar los Physical ID

Ambos servos vienen de fábrica con el Physical ID `0C` hex / Application ID
`6800` hex — entrarán en conflicto en el bus compartido a menos que se
cambie uno de ellos. Hay dos formas de hacerlo, según el tipo de receptor:

**Mediante el conector S.Port de la emisora** (cualquier receptor):

1. Conecta el servo 1, ve a **Device Config → XAct** y ajusta **Module** a
   **S.Port connector**. Deja el Physical ID `0C`/Application ID `6800` y el
   canal `CH1` con sus valores por defecto, y luego elige **Save to flash**.
2. Conecta ahora el servo 2 en su lugar, en el mismo menú. Cambia el
   **Physical ID** a `0D` hex y el **Application ID** a `6801` hex (consulta
   la [tabla de Physical ID](../model-setup/telemetry.md#how-frsky-telemetry-works)
   para ver qué posiciones están libres), ajusta **Channel** a `CH5` y elige
   **Save to flash**.

**Directamente a través del receptor** (por ejemplo, un TD-R18 Tandem, con
ambos servos conectados simultáneamente — consulta el [Paso
4](#4-configure-the-receiver-for-fbus)):

1. Con solo el servo 1 conectado (por ejemplo, al Pin1 del receptor), entra
   en **Device Config → XAct**, **Module** → **Internal module**. Confirma
   los valores por defecto (`0C`/`6800`/`CH1`) y elige **Save to flash**.
2. Con solo el servo 2 conectado (Pin5), en el mismo menú (Device Config se
   comunica con un servo a la vez) — cambia a `0D`/`6801`/`CH5` y elige
   **Save to flash**. Vuelve a seleccionar Device Config después para
   confirmar que el cambio se ha guardado.

## 4. Configurar el receptor para FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [Sistema RF](../model-setup/rf-system.md) → el botón del
receptor → **Options** → ajusta **Telemetry Port** a **FBUS**. Los servos
Xact se conectan entonces en cadena a ese puerto; como cada servo tiene un
único conector, un extensor multicanal F.Port2 (FP2CH4/6/8) lo distribuye a
varios servos.

**TD-R18 Tandem**: Sistema RF → el botón del receptor → **Options** →
ajusta pines individuales (por ejemplo, **Pin1**, **Pin5**) a **FBUS** — se
pueden reasignar de esta forma tantos pines como sean necesarios, evitando
los extensores por completo; cada pin asignado como FBUS transporta la misma
señal FBUS.

## 5. Comprobar el control FBUS de los servos

Conecta el servo 1 al Pin1 y el servo 2 al Pin5 (los canales de alerones del
ejemplo de ala fija), enciende el sistema y comprueba que los canales 1 y 5
mueven los servos correctos.

## 6. Comprobar la telemetría FBUS

Con ambos servos conectados, elimina cualquier sensor `SRV` existente en
[Telemetría](../model-setup/telemetry.md) y vuelve a descubrirlos. Cada
servo informa de 4 sensores: corriente, tensión, temperatura y estado (`OK`
cuando es normal).

## 7. Realizar cambios de configuración más adelante

Una vez que un modelo está completamente cableado, aislar un servo para
reconfigurarlo mediante Device Config no resulta práctico. En su lugar: ve a
Telemetría, busca un sensor perteneciente al servo en cuestión (por ejemplo,
`SRV1 curr`) y elige **Configure** — esto abre directamente la configuración
de ese servo. Elige **Save to flash** después de cualquier cambio.

!!! warning
    No cambies por accidente el Physical ID ni el Application ID desde esta
    pantalla — son los que permiten que cada servo siga siendo direccionable
    en el bus compartido.
