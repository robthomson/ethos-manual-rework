---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuración inicial de la emisora

La configuración que solo hay que realizar una vez, antes de programar cualquier modelo. Los
[Tutoriales](index.md) que siguen dan por supuesto que ya se ha hecho.

!!! note
    Estos tutoriales no son un recetario estricto: dan por supuesto un
    vocabulario básico de RC y soltura navegando por los menús de Ethos. Si algo aquí
    no queda claro, repase antes [Interfaz de usuario y
    navegación](../getting-started/user-interface-and-navigation.md).

## Paso 1. Cargue la batería de la emisora y las baterías de vuelo

Cargue la batería de la emisora siguiendo las indicaciones suministradas con la emisora, y
las baterías de vuelo con un cargador adecuado a su química: extreme
las precauciones con los packs de litio.

## Paso 2. Calibre el hardware

Confirme que se ha realizado la [calibración del
hardware](../system-setup/hardware.md#analogs-calibration)
(se ejecuta automáticamente en el primer arranque), de modo que la emisora conozca el
centro exacto y los límites de cada gimbal, potenciómetro y deslizador. Repítala en
**System → Hardware** cada vez que se sustituya un gimbal, un potenciómetro o un deslizador.

## Paso 3. Realice la configuración del sistema de radio

La [Configuración del sistema](../system-setup/index.md) abarca todo lo que es común a
todos los modelos, a diferencia de los ajustes propios de cada modelo de la
[Configuración del modelo](../model-setup/index.md).
La mayoría de los valores por defecto son adecuados para empezar, pero conviene revisar:

- **[Fecha y hora](../system-setup/date-and-time.md)** — ajústelas correctamente.
- **[Audio → Elección de
  voces](../system-setup/general.md#audio-settings)** — configure los anuncios
  de voz, incluidos los archivos de audio personalizados.
- **[Controles (Sticks)](../system-setup/controls.md)**:
  - **Modo de palancas** — Modo 1 (acelerador/alerón a la derecha, profundidad/timón
    a la izquierda) o Modo 2 (acelerador/timón a la izquierda, alerón/profundidad a la
    derecha, el modo por defecto de Ethos).

    !!! warning
        Si un modelo está configurado para un modo de palancas mientras la
        emisora está ajustada al otro, un motor eléctrico puede arrancar
        en el instante en que se alimenta el receptor.

  - **Orden de canales** — Ethos usa por defecto **AETR** (Alerón, Elevador,
    Acelerador, Timón); la convención de Spektrum/JR es **TAER**, y la de Futaba/Hitec
    es **AETR**. Esto establece el orden en que se asignan las entradas de las palancas al
    crear un modelo nuevo; después, cada modelo puede ajustarse individualmente.

    !!! note "Receptores estabilizados FrSky"
        Estos requieren específicamente **AETR**. Con más de una superficie
        por función (p. ej. 2 alerones), el asistente normalmente las agrupa
        (dando **AAETR**), pero los receptores SRx esperan **AETRA**/**AETRAE**
        en su lugar, por lo que debe activar **[Primeros cuatro canales
        fijos](../system-setup/controls.md#first-four-channels-fixed)**
        en Sticks para mantener los cuatro primeros canales en orden AETR estricto
        en cualquier caso.

- **[Batería](../system-setup/battery.md)** — ajuste **Voltaje principal**, **Voltaje
  bajo** y **Rango de voltaje en pantalla** para que coincidan con la batería real de la
  emisora.
- **[ID de registro del propietario](../model-setup/rf-system.md#owner-registration-id)**
  — lo utilizan los receptores ACCESS, y se comparte entre emisoras para Smart
  Share. Se configura en la Configuración del modelo, pero en la práctica funciona como un
  ajuste a nivel de sistema, ya que todo modelo nuevo lo utiliza (aún puede
  cambiarse en cada receptor durante el registro si fuera necesario).

!!! note "Unidades"
    Ethos no tiene un selector global entre sistema métrico e imperial: las [unidades de los
    sensores de telemetría](../model-setup/telemetry.md#editing-a-sensor) se ajustan
    individualmente, sensor por sensor.
