---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Controles

![Palancas](../assets/system-sticks.png)

En el menú aparece como **Sticks**: define el modo de palancas y el orden
predeterminado de asignación de canales.

## Modo de palancas

- **Modo 1**: motor y alerones en la palanca derecha, profundidad y
  dirección en la izquierda.
- **Modo 2**: motor y dirección en la palanca izquierda, alerones y
  profundidad en la derecha.

Por defecto, las palancas se nombran según los modos estándar del sector,
aunque se pueden renombrar.

## Orden de canales

Define el orden en que las cuatro entradas de las palancas se asignan a los
canales cuando se crea un modelo nuevo con los asistentes de [Selección de
modelo](../model-setup/model-select.md). El valor predeterminado es
**AETR**. Cuando una aeronave tiene más de una superficie del mismo tipo,
estas se agrupan entre sí, salvo que [Primeros cuatro canales
fijos](#first-four-channels-fixed) esté activado; por ejemplo, con 2
alerones queda **AAETR**.

![Orden de canales del receptor](../assets/system-sticks-rx-order.png)

## Primeros cuatro canales fijos {: #first-four-channels-fixed }

Con esta opción activada, los cuatro primeros canales nunca se agrupan. Con
el orden **AETR** y una aeronave con 2 alerones, 1 profundidad, 1 motor, 1
dirección y 2 flaps, el asistente genera **AETRAFF** (los canales 1–4 se
mantienen exactamente como A-E-T-R, y el segundo alerón y los dos flaps se
añaden a continuación) en lugar de **AAETRFF**. Este es el ajuste que hace
que el asistente cree modelos adecuados para los receptores estabilizados
SRx, que requieren esa disposición fija.

![Orden fijo de 4 canales](../assets/system-sticks-4ch-fixed.png)
