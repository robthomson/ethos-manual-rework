---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Cómo probar un sistema de receptores redundantes

La redundancia solo sirve de algo si se comprueba de verdad antes de volar —
para esta prueba se asume que ya ha configurado un [receptor redundante](../model-setup/rf-system.md#redundant-receivers).

!!! note "Capturas de pantalla pendientes"
    Esta página aún no tiene capturas de pantalla del simulador — consulte [Flujo
    de capturas de pantalla](../contributing/screenshot-pipeline.md).

## A. Prueba real

Asumiendo que el receptor principal es 2.4G y el redundante 900M, active la
[prueba de alcance](../model-setup/rf-system.md#range-check) y simplemente
aléjese caminando del modelo hasta que el receptor de 2.4G deje de funcionar
(por ejemplo, después de obtener la alerta crítica de RSSI). En ese momento, el
receptor redundante de 900M debería haber tomado el control del modelo.

## B. Prueba en banco

1. **Confirme el funcionamiento normal de la configuración** — ambos receptores
   vinculados, ambos con los LED verdes encendidos y los controles respondiendo
   con normalidad.
2. **Vincule el receptor principal a otra ID de modelo** — cree un modelo
   sencillo de pruebas (por ejemplo, «TestRx») con una ID de modelo distinta y
   vincule a él el receptor *principal*. Cambie de nuevo al modelo que se quiere
   probar: el LED del receptor principal debería estar ahora en **rojo** (por
   estar vinculado con otro modelo), mientras que el LED del receptor redundante
   debería seguir en **verde** — y los controles deberían funcionar
   perfectamente, probando que el receptor redundante por sí solo mantiene el
   modelo en condiciones de vuelo.
3. **Vuelva a vincular el receptor principal** a la ID normal del modelo.
   Confirme que las luces LED de ambos receptores están de nuevo en verde y que
   los controles funcionan normalmente antes de dar la prueba por finalizada.
