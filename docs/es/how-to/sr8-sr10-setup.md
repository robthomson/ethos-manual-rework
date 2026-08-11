---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuración de modelo y reordenación de canales para SR8/SR10

Los receptores estabilizados SRx de FrSky esperan un orden de canales
específico. Se dan dos escenarios: crear un modelo nuevo desde cero para uno de
ellos, o convertir un modelo existente para que coincida.

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas de pantalla del simulador — consulte
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md).

## Creación de un modelo nuevo

El asistente de [Selección de modelo](../model-setup/model-select.md) agrupa por
defecto las superficies con la misma función (p. ej. 2 alerones → `AAETR`), pero
los receptores SRx necesitan que los cuatro primeros canales queden fijados como
**AETRA**.

1. En [Controls](../system-setup/controls.md), confirme que el **orden de
   canales** es `AETR`.
2. Active **[Primeros cuatro canales
   fijos](../system-setup/controls.md#first-four-channels-fixed)** — esto impide
   que el asistente agrupe los cuatro primeros canales, manteniéndolos
   estrictamente en el orden `AETRA…` independientemente de cuántas superficies
   de cada tipo tenga la célula.
3. Ejecute el asistente de creación de modelo con normalidad — los 5 primeros
   canales resultan en `AETRA`.

!!! note "Autocomprobación de receptores Archer"
    La autocomprobación de los receptores Archer se realiza ahora a través de
    [Device Config → SxR](../system-setup/devices.md) (firmware v2.1.10+) en
    lugar de un procedimiento de autocomprobación dedicado. El canal del
    acelerador debe estar al −100% o la autocomprobación no se iniciará.

## Reordenación de un modelo existente

Convertir un modelo existente (p. ej. actualmente `AAETRFF`) al orden del
receptor estabilizado (`AETRAE`, y después el canal 9 para Gain, 10/11 para
fases de vuelo y 12 para la autocomprobación en las unidades SxR más antiguas)
consiste en una secuencia de intercambios de canales en
[Salidas](../model-setup/outputs.md#swap-channels).

Punto de partida:

| Can | Función |
|---|---|
| 1 | Alerón1 (derecho) |
| 2 | Alerón2 (izquierdo) |
| 3 | Profundidad |
| 4 | Acelerador |
| 5 | Dirección |
| 6 | Flap1 (derecho) |
| 7 | Flap2 (izquierdo) |
| 8 | Tren retráctil |

Orden objetivo: `AETRAE` — CH1 Alerón1, CH2 Profundidad, CH3 Acelerador,
CH4 Dirección, CH5 Alerón2, CH6 Profundidad2/AUX2 (y después Gain/fases de
vuelo/autocomprobación en 9–12).

1. **Aparte primero el Alerón2**: en Salidas, seleccione CH2 (Alerón2), pulse de
   nuevo, **Intercambiar canales**, e intercámbielo con un canal sin usar
   (p. ej. CH9). El intercambio es inmediato — todas las mezclas que hagan
   referencia a cualquiera de los dos canales se actualizan automáticamente.
2. **Intercambie CH3 (Profundidad) → CH2.**
3. **Intercambie CH4 (Acelerador) → CH3.**
4. **Intercambie CH5 (Dirección) → CH4.**
5. **Intercambie CH9 (Alerón2, aparcado en el paso 1) → CH5.**

Resultado:

| Can | Función |
|---|---|
| 1 | Alerón1 (derecho) |
| 2 | Profundidad |
| 3 | Acelerador |
| 4 | Dirección |
| 5 | Alerón2 (izquierdo) |
| 6 | Flap1 (derecho) |
| 7 | Flap2 (izquierdo) |
| 8 | Tren retráctil |

— ahora en el orden que esperan los receptores estabilizados de FrSky.
