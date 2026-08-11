---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Controles

![Sticks](../assets/system-sticks.png)

Llamado **Sticks** en el menú: el modo de sticks y el orden predeterminado
de asignación de canales.

## Modo de sticks

- **Modo 1**: acelerador y alerones en el stick derecho, profundidad y
  dirección en el izquierdo.
- **Modo 2**: acelerador y dirección en el stick izquierdo, alerones y
  profundidad en el derecho.

Los sticks se nombran según los modos estándar del sector de forma
predeterminada, y pueden renombrarse.

## Orden de canales

Define el orden en que las cuatro entradas de los sticks se asignan a los
canales cuando se crea un nuevo modelo mediante los asistentes de
[Selección de modelo](../model-setup/model-select.md). El valor
predeterminado es **AETR**. Cuando un fuselaje tiene más de una superficie
del mismo tipo, estas se agrupan entre sí, salvo que [Primeros cuatro
canales fijos](#first-four-channels-fixed) esté activado; por ejemplo, 2
alerones se convierte en **AAETR**.

![Orden de canales del receptor](../assets/system-sticks-rx-order.png)

## Primeros cuatro canales fijos {: #first-four-channels-fixed }

Con esta opción activada, los primeros cuatro canales nunca se agrupan. Con
el orden **AETR** y un fuselaje con 2 alerones, 1 profundidad, 1 motor, 1
dirección y 2 flaps, el asistente genera **AETRAFF** (los canales 1–4
permanecen exactamente como A-E-T-R, y el segundo alerón y ambos flaps se
añaden a continuación) en lugar de **AAETRFF**. Este es el ajuste que hace
que el asistente cree modelos adecuados para los receptores estabilizados
SRx, que esperan esa disposición fija.

![Orden fijo de 4 canales](../assets/system-sticks-4ch-fixed.png)
