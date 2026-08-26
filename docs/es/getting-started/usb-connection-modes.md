# Modos de conexión USB al PC

## Modo con emisora apagada

- Conectando la radio apagada a un PC mediante un cable USB, se entra en el modo DFU que sirve para flashear el bootloader.

## Modo bootloader

- La radio se pone en modo bootloader encendiendo la radio con la tecla Enter pulsada. En la pantalla aparecerá el mensaje de estado 'Bootloader'. 
- A continuación, la radio puede conectarse a un PC mediante un cable de datos USB. El mensaje de estado cambiará a 'USB Plugged', y el PC debería mostrar dos unidades externas conectadas. La primera es para la memoria flash de la radio, y la segunda es el contenido de la tarjeta SD o eMMC.
- Este modo se utiliza para leer y escribir archivos en la tarjeta SD o eMMC y/o en la memoria flash de la radio.
- Este modo también se utiliza para conectar la radio a la Ethos Suite para actualizarla. Encontrará más detalles sobre el [Modo Bootloader](#Bootloader Mode) en la sección de Ethos Suite.

## Modo con emisora encendida

- Si la radio está conectada a un PC mediante un cable de datos USB mientras está encendida normalmente, se muestran las opciones siguientes:

![](../assets/usbmenu.png)

- En modo ‘Joystick’, la radio puede configurarse para controlar simuladores RC.
- En el modo ‘Ethos Suite’, la radio entrará en "Modo Ethos" para la comunicación con Ethos Suite. Consulte el [Modo Ethos](#Ethos Mode) en la sección Ethos Suite.

- En modo ‘Serie’ las trazas de depuración Lua se envían a un puerto USB-Serie si está presente. La pestaña Herramienta de desarrollo Lua de Ethos Suite integra una ventana de terminal que es capaz de visualizar las trazas. La tasa de baudios es 115200bps. Puede encontrar un controlador adecuado para un puerto COM virtual para Windows [aqu](https://www.st.com/en/development-tools/stsw-stm32102.html)í.
