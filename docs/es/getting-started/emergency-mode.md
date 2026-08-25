# Modo de emergencia

El modo de emergencia es la respuesta de la radio a un evento inesperado como un reinicio del “watchdog”. El “watchdog” es un temporizador que se reinicia continuamente por diferentes partes de Ethos. Si un fallo de cualquier tipo impide que el temporizador “watchdog” se reinicie, se agotará el tiempo y provocará un reinicio hardware de la radio. En este Modo de Emergencia la radio se reinicia extremadamente rápido, sin ninguna de las comprobaciones normales de arranque para que usted recupere el control de su modelo lo más rápido posible. En el Modo de Emergencia no se puede acceder a la Tarjeta SD o eMMC.

El Modo Emergencia sólo proporciona las funciones esenciales para controlar su modelo, pero ninguna de las funciones de alto nivel. La pantalla se quedará en blanco y mostrará las palabras “Modo Emergencia”, acompañadas de un pitido de 300 ms que se repetirá continuamente cada 3 segundos. Las alertas de voz, la ejecución de scripts, el registro, etc. dejarán de funcionar. Si se produce el modo de Emergencia, obviamente deberá aterrizar lo antes posible.

La causa más común del Modo de Emergencia es el fallo de la tarjeta SD o eMMC.

## Prueba del modo de emergencia

En determinados casos puede ser útil para el usuario poder probar el modo de emergencia.

![](../assets/Pictures/1000000000000320000001E0CAE58A4D.png)

Se puede añadir una herramienta de Sistema para probar el modo de emergencia. Seleccione el icono Emergency Test para iniciar la prueba.

![](../assets/Pictures/1000000000000320000001E07840F732.png)

Un cuadro de diálogo le pedirá confirmación para proceder.

![](../assets/Pictures/1000000000000320000001E0FC0300AF.png)

La radio entrará en el modo de emergencia.
