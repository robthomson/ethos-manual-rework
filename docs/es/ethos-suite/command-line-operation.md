# Operación de línea de comandos

FrSky Suite se puede ejecutar desde la línea de comandos del terminal.

Las siguientes opciones de línea de comandos están disponibles:

| --help | texto de ayuda para la herramienta de línea de comandos FrSky Suite. |
| --- | --- |
| --version | muestra la versión del FrSky Suite instalado. |
| --list-radios | lista todas las radios FrSky compatibles. |
| --radio-components<br>--radio {RADIO}<br>--radio auto | lista todos los componentes y sus rutas. <br>Si hay varias radios conectadas a su computador. Puede usar \[--radio {RADIO}\] para especificar una. <br>De lo contrario, puede omitir \[--radio {RADIO}\] o usar \[--radio auto\] para la detección automática. |
| --get-path {COMPONENT} | obtiene la ruta del componente dado.  
  
Componentes actualmente soportados: BITMAPS, SCRIPTS, SCREENSHOTS, AUDIO, I18N. |
| --serial start\|stop | activa / desactiva el modo de depuración serie. |

Aviso: La app de la Suite no se iniciará a menos que reconozca un comando correctamente.
