---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modo de emergencia

El modo de emergencia es la respuesta de Ethos ante un fallo inesperado de bajo nivel, como un reinicio por watchdog. El watchdog es un temporizador que diversas partes del sistema reinician continuamente; si algo impide que se reinicie, se agota su tiempo y fuerza un reinicio del hardware. El modo de emergencia reinicia entonces la emisora lo más rápido posible, omitiendo todas las comprobaciones normales de arranque, de modo que el control del modelo se devuelve con el mínimo retardo. En este modo no se accede en absoluto a la SD card/eMMC.

Solo están disponibles las funciones esenciales necesarias para seguir controlando el modelo — ninguna de las funciones de nivel superior. La pantalla queda en blanco salvo por las palabras **EMERGENCY MODE**, acompañadas de un pitido repetido de 300 ms cada 3 segundos; las alertas de voz, los scripts Lua, el registro de datos y la telemetría se detienen. Si esto ocurre en vuelo, aterrice lo antes posible.

La causa más habitual es un fallo de la SD card.

## Prueba del modo de emergencia

Se puede añadir una **herramienta del sistema** para activar deliberadamente el modo de emergencia con fines de prueba, de modo que no haya que descubrirlo por primera vez en vuelo. Al pulsar el icono Emergency Test se solicita confirmación y, a continuación, la emisora entra en modo de emergencia exactamente igual que si se tratara de un fallo real.
