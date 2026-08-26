# Simulador Web de Ethos

![](../assets/Pictures/1000000100000ECE0000087E9D52C826.png)

El simulador web Ethos está construido como WebAssembly (abreviado Wasm), que es una solución portátil que permite su despliegue en la web. Esto significa que se ejecuta dentro de un navegador y no necesita instalación en un PC. Chrome es el navegador recomendado.

El simulador web Ethos le permite explorar las capacidades de la radio y probar la funcionalidad o las mejoras planificadas del modelo sin usar la radio real. También le permite explorar muy fácilmente los nuevos lanzamientos antes de actualizar su radio.

El simulador web se encuentra en [https://ethos-simulator.frsky-rc.com/](https://ethos-simulator.frsky-rc.com/)

La selección inicial predeterminada es la versión 26.1.0-RC6 (al momento de escribir), la radio X20 Pro y el protocolo FCC. Para empezar, seleccione el idioma de la pantalla.

![](../assets/Pictures/1000000100000ECA00000874C3B44D03.png)

Cuando se cargue por primera vez, no se encontrará ningún dato de modelo válido, así que se comenzará a ejecutar automáticamente el asistente de nuevo modelo.

![](../assets/Pictures/1000000100000ECC00000870497896E6.png)

Complete el asistente para configurar un modelo de prueba básico.

Si la versión predeterminada y la radio no son las opciones deseadas, selecciona la versión de lanzamiento de Ethos que quiera, el tipo de radio que se va a simular y el protocolo RF.

![](../assets/Pictures/100000010000005D00000054E66F5895.png) Haga click en este icono en la barra superior del menu Panel, y seleccione la Consola.

![](../assets/Pictures/1000000100000ECE000008706423AC8F.png)

La Consola aparecerá junto al panel de visualización.

![](../assets/Pictures/1000000100000ECC0000087C83E4950C.png)

Haz clic y arrastre la barra de título de la Consola, y arrástrela hacia abajo. Mueva el ratón hasta que la Consola ocupe el cuadrante inferior izquierdo.

La consola es útil para confirmar la secuencia de inicio del simulador y para monitorizar eventos y mensajes de error.

![](../assets/Pictures/1000000100000ECA000008702FCCDE98.png)

Haga clic en el icono de Paneles de nuevo, y repita con el panel de Telemetría, moviéndolo al cuadrante inferior derecho.

![](../assets/Pictures/1000000100000ECA000008747ED7D4D7.png)

En el panel de Telemetría, haga clic repetidamente en ‘Agregar un nuevo sensor’ y añada los sensores a los que quiera acceder en sus simulaciones.

![](../assets/Pictures/100000010000005400000051ACB62F01.png) Haga click en este icono para guardar sus sensores para futuras sesiones, y seleccione ‘Guardar configuración de telemetría’. La configuración de telemetría se guardará en un archivo llamado ‘telemetry.json’ en la carpeta de descargas. Muévelo a un lugar conveniente. En las sesiones posteriores del simulador, haga clic en el ícono de ‘Cargar’ y seleccione ‘Cargar un archivo JSON de telemetría’, luego busque su en el archivo ‘telemetry.json’ guardado.

Ahora está listo para empezar a simular. El navegador recordará la disposición de sus paneles, así que no necesitará seguir corrigiéndola.

### Configuración recomendada

Es mejor replicar la configuración de su radio en el simulador. Esto proporcionará la misma funcionalidad que tiene en su radio, facilitando probar mejoras en sus modelos sin afectar su vuelo o entorno de modelismo hasta que todo funcione como planeado.

Los pasos recomendados para la configuración son:

1. Haga una copia de seguridad de su radio usando la función de [Copia de seguridad y recuperación](operation.md) de la Suite.

2. En el menú de Subir, seleccione 'Subir una copia de seguridad de la radio' y busque el archivo de copia de seguridad que guardó. (Consulte los menús a continuación.)

![](../assets/Pictures/1000000100000ED400000878BB388CA7.png)

3. Debería empezar con el modelo que estaba vigente en su radio cuando hizo la copia de seguridad. En este ejemplo, un planeador Ng2 era el modelo vigente.

Con su entorno de radio acostumbrado, ahora puede crear y probar un modelo completamente nuevo, tal vez basándolo en una de sus plantillas, o haciendo un clon de un modelo existente y modificándolo. Estos enfoques maximizan la reutilización sin tener que programar un modelo desde cero. Una vez completado, utilice la opción 'Descargar un archivo de modelo' para bajar el archivo .bin del modelo a su ruta de descargas. Luego cópielo a su radio.

### Barra de tareas del simulador

The simulator task bar has the following controls:

![](../assets/Pictures/100000010000036800000047E3EA708F.png)

![](../assets/Pictures/100000010000003A00000036AC758BFB.png)	Captura de pantalla (a la carpeta de descargas)

![](../assets/Pictures/100000010000003400000034DE16CBC7.png)	Iniciar grabación (graba una macro – más allá del alcance de este resumen)

![](../assets/Pictures/1000000100000035000000340120C033.png)	Paneles (lista los paneles que aún no se han abierto)

![](../assets/Pictures/100000010000003200000035B08BF6F9.png)	Subir… (ver menú abajo)

![](../assets/Pictures/100000010000003300000036B485D201.png)	Descargar... (ver menú abajo)

![](../assets/Pictures/100000010000003600000035E4DD6074.png)	Audio Activado/Desactivado

![](../assets/Pictures/100000010000003200000036BA846668.png)	Reiniciar simulador

![](../assets/Pictures/1000000100000036000000352D3A7338.png)	Documentación (contiene un enlace al manual más reciente)

![](../assets/Pictures/1000000100000032000000358C5AA574.png)	Modo claro/oscuro

##### Menú de subidas

![](../assets/Pictures/10000001000000360000002DF56DE3FB.png)	Sube un archivo de modelo (.bin)

![](../assets/Pictures/10000001000000390000002C2B0D8C92.png)	Sube una copia de seguridad de la radio (.bin)

![](../assets/Pictures/10000001000000330000003360667B21.png)	Sube un paquete de audio (.zip)

![](../assets/Pictures/1000000100000039000000365A698952.png)	Sube un plugin de Lua (.zip)

![](../assets/Pictures/10000001000000340000002F715D80FB.png)	Sube un archivo de traducciones CSV (.csv)

![](../assets/Pictures/10000001000000350000002A57E2BD00.png)	Sube un archivo de telemetría JSON (.json)

![](../assets/Pictures/100000010000002A00000027C53ED7E7.png)	Inicia una macro (.zip)

##### Menú de descargas

![](../assets/Pictures/10000001000000300000002EDEF4203A.png)	Guarda el archivo del modelo actual (.bin)

![](../assets/Pictures/100000010000003500000035216F2B0D.png)	Edita el modelo actual

![](../assets/Pictures/100000010000003500000035216F2B0D.png)	Edita el archivo del modelo actual (JSON)

![](../assets/Pictures/100000010000003900000032E89F86E0.png)	Guarda todas las capturas de pantalla (navegua a la carpeta de destino, guarda como .png)

![](../assets/Pictures/10000001000000380000002D9C5C49CF.png)	Guardar una copia de respaldo de la radio (.zip)

![](../assets/Pictures/10000001000000350000002C0EC1166A.png)	Guardar la configuración de la telemetría (.json)

##### Panel de Controles

![](../assets/Pictures/10000001000007560000040A4C394584.png)

El panel de 'Controles' imita los controles físicos de la radio elegida.

###### Gimbals

Las palancas se pueden manejar arrastrándolas con el ratón. Durante la depuración es útil limitar o restringir el movimiento de las palancas.

![](../assets/icon-sim-center.png)	Alineará automáticamente la palanca en uno o en ambos ejes.

![](../assets/icon-sim-vertical.png)	Restringirá el movimiento de las palancas al sentido vertical únicamente.

![](../assets/icon-sim-horizontal.png)	Restringirá el movimiento de las palancas al sentido horizontal únicamente.

###### Interruptores y botones momentáneos

![](../assets/icon-sim-locked.png)	Bloqueará los interruptores y los botones momentáneos para que puedan alternar entre encendido y apagado, pero permanecerán en el estado seleccionado de encendido o apagado para depuración.
