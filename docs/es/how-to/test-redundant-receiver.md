---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Probar una configuración de receptor redundante

La redundancia solo vale la pena si realmente se prueba antes de volar —
esto supone que ya hay un [receptor redundante](../model-setup/rf-system.md#redundant-receivers)
configurado.

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas de pantalla del simulador — consulte [Flujo
    de capturas de pantalla](../contributing/screenshot-pipeline.md).

## A. Prueba en condiciones reales

Con el receptor principal en 2,4 GHz y el redundante en 900 MHz, inicie una
[Prueba de alcance](../model-setup/rf-system.md#range-check) y aléjese del
modelo hasta que la señal de 2,4 GHz se pierda (más allá de la alerta de RSSI
crítico). En ese momento, el receptor redundante de 900 MHz debería asumir el
control.

## B. Prueba de banco

1. **Confirme la configuración normal** — ambos receptores vinculados, ambos
   LED verdes encendidos, los controles respondiendo con normalidad.
2. **Vincule el receptor principal a otro Model ID** — cree un modelo de prueba
   desechable (por ejemplo, «TestRx») con un Model ID diferente y vincule a él
   el receptor *principal*. Vuelva al modelo que está probando: el LED del
   receptor principal debería estar ahora **rojo** (vinculado en otro lugar),
   mientras que el LED del receptor redundante permanece **verde** — y los
   controles deberían seguir funcionando, lo que demuestra que el receptor
   redundante por sí solo mantiene el modelo en condiciones de vuelo.
3. **Vuelva a vincular el receptor principal** a su Model ID habitual. Confirme
   que ambos LED vuelven a estar verdes y que los controles funcionan antes de
   dar la prueba por finalizada.
