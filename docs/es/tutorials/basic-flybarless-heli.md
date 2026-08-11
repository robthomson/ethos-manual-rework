---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ejemplo básico de helicóptero flybarless

Una configuración básica de helicóptero flybarless (FBL), tomando como
ejemplo una controladora como la Spirit. A diferencia de un modelo de ala
fija, un helicóptero es intrínsecamente inestable: la unidad FBL
utiliza giróscopos (velocidad de rotación) y acelerómetros
(movimiento/orientación) para calcular las correcciones de
guiñada/cabeceo/alabeo mediante un lazo de control PID
(Proporcional-Integral-Derivativo) ajustado, equilibrando estabilidad,
respuesta y sobreoscilación según las características físicas y eléctricas
del helicóptero concreto.

Este tutorial cubre únicamente la parte de **programación de la emisora**:
consulte la documentación propia de su unidad FBL para el resto, y aborde
este proceso disponiendo ya de buenos conocimientos generales sobre
helicópteros.

!!! danger
    Retire las palas del rotor antes de empezar, por seguridad.

## Paso 1. Comprobar los ajustes del sistema

Orden de canales **AETR**, **[Primeros cuatro canales
fijos](../system-setup/controls.md#first-four-channels-fixed)** en **OFF**:
las unidades FBL Spirit esperan los canales SBUS específicamente en este
orden (aunque internamente utilicen TAER en su propia configuración).
Registre (si es ACCESS) y vincule el receptor mediante [RF
System](../model-setup/rf-system.md).

## Paso 2. Identificar los servos/canales necesarios

| Función | Canal |
|---|---|
| Alabeo (alerón) | — |
| Cabeceo (profundidad) | — |
| Acelerador | — |
| Guiñada (timón) | — |
| Ganancia del giróscopo | 5 |
| Paso colectivo | 6 |
| Banco de ajustes | 7 |
| Rescate | 8 |

## Paso 3. Crear un nuevo modelo

![Crear modelo de helicóptero](../assets/tut-heli-eg-wiz-create-heli.png)

Desde [Selección de modelo](../model-setup/model-select.md), cree/seleccione
una categoría Heli, inicie el asistente y elija **Flybarless**:

![Selección de FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Nombre del modelo](../assets/tut-heli-eg-wiz-name.png)

Asígnele un nombre y elija una imagen.

## Paso 4. Revisar y configurar las mezclas

![Vista general de las mezclas](../assets/tut-heli-eg-mixes.png)

El asistente crea Alerones/Elevador/Acelerador/Timón en orden AETR,
Paso en el canal 6 y Banco FBL en el canal 7:

![Mezcla de paso](../assets/tut-heli-eg-mixes-pitch.png)

Compruebe que el canal 6 es el Paso colectivo. Es necesario añadir
manualmente dos canales más como [mezclas
libres](../model-setup/mixes.md#mix-libraries): **Ganancia del giróscopo**
(canal 5) y **Rescate/Estabi** (canal 8).

**Alerón/Elevador/Timón**: no hay nada que añadir; las tasas y el
Expo son tarea de la unidad FBL, así que la emisora simplemente transmite
una entrada lineal limpia.

![Mezcla de alerones](../assets/tut-heli-eg-mixes-ail.png)

**Paso colectivo**: una curva lineal recta; solo hay que confirmar el canal
de salida (normalmente el 6). Como arriba, las tasas y el Expo los gestiona
la unidad FBL, no la emisora.

**Banco FBL**: la unidad FBL del Spirit dispone de tres bancos de ajustes
(distintos estilos de vuelo, distintas ganancias del sensor para bajas o
altas RPM, o Principiante, Acro o 3D, o simplemente para afinar la
configuración) asignados a un interruptor de 3 posiciones, por ejemplo SE:

![Mezcla de banco](../assets/tut-heli-eg-mixes-bank.png)

**Ganancia del giróscopo**: añádala como mezcla libre después del último
canal. La ganancia suele ser un valor fijo: ajuste la **Fuente** a Valor
especial 0, introduzca la ganancia mediante el **Offset** (afinándola más
tarde en vuelo) y envíe la salida al canal 5:

![Mezcla de ganancia del giróscopo](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Configurar los modos de vuelo

![Modos de vuelo](../assets/tut-heli-eg-flight-modes.png)

Tres [modos de vuelo](../model-setup/flight-modes.md): renombre el Modo de
Vuelo por Defecto a **Normal** y añada **Ralentí 1**/**Ralentí 2** en el
interruptor SD.

### Configurar la mezcla del acelerador

Tres curvas de aceleración, una por modo de vuelo, cada una como [curva
personalizada](../model-setup/curves.md):

- **Normal**: acelerado de la hélice (spool up) y despegue: la curva
  comienza en −100 % (motor apagado) y luego aumenta suavemente. Una curva
  de 7 puntos con **Smooth** activado funciona bien; los valores finales de
  la curva pueden necesitar ser determinados en vuelo.

  ![Curva en modo normal](../assets/tut-heli-eg-curves-normal.png)

- **Ralentí 1**: la mayoría de los vuelos: una curva en línea recta
  significa que tendremos un ajuste constante del acelerador para mantener
  los rotores girando a un ritmo constante, mientras que el movimiento del
  helicóptero será controlado por los mandos de Paso Colectivo, Alerón
  (roll) y Profundidad (pitch). Tenga en cuenta que no debe haber un gran
  salto entre Normal y Ralentí 1, para que la transición se produzca
  suavemente. (La mayoría de las unidades FBL ofrecen además una función de
  **regulación** (Governor) que garantiza que la velocidad del rotor se
  mantenga constante incluso durante maniobras de vuelo agresivas; consulte
  el manual del FBL para obtener más información.)

  ![Curva de ralentí 1](../assets/tut-heli-eg-curves-iup1.png)

- **Ralentí 2**: vuelos más agresivos (acrobacias aéreas y 3D); de nuevo,
  puede ser necesario determinar el valor final del acelerador en vuelo.

  ![Curva de ralentí 2](../assets/tut-heli-eg-curves-iup2.png)

![Curvas del acelerador en las mezclas](../assets/tut-heli-eg-mixes-thr-curves.png)

**Corte de motor (Throttle Cut)**: asigne, por ejemplo, el interruptor
SG-up con **Sticky** en ON: el motor se cortará tan pronto como ponga el
interruptor en la posición 'Arriba' y, debido a la configuración Sticky, el
acelerador sólo puede ser armado con la palanca del acelerador en la
posición baja (off).

![Corte de motor](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescate/Estabi**: asígnelo de forma similar, por ejemplo al conmutador SA
en el canal 8.

![Mezclas finales](../assets/tut-heli-eg-mixes-final.png)

## Paso 5. Configuración del FBL

1. **Instale la herramienta de configuración del FBL**: por ejemplo el
   software Spirit Settings, en su PC.
2. **Conecte el receptor a la unidad FBL** de acuerdo con su sección de
   cableado: normalmente la salida 'SBUS Out' del receptor al puerto 'RUD'
   de la unidad FBL (tenga en cuenta que algunos modelos Spirit requieren
   un adaptador SBUS), o bien mediante F.Port1/FBUS.
3. **Conecte la unidad FBL con su PC**: ya sea mediante cable o a través de
   Bluetooth, según su manual.

   !!! danger
       ¡No conecte ningún servo todavía!

4. **Actualice el firmware del FBL** si es necesario, desde la pestaña
   Update de la herramienta.
5. **Configuración general** (pestaña General del software Spirit
   Settings):
   - Tipo de receptor: **Futaba SBUS** o **FrSky F.Port**, según
     corresponda, y reinicie el sistema.
   - Asignación de canales (con el orden AETR del asistente):

     | Función | Canal |
     |---|---|
     | Acelerador | 1 |
     | Alerón | 2 |
     | Elevador | 3 |
     | Timón | 4 |
     | Giróscopo | 5 |
     | Paso | 6 |
     | Banco | 7 |
     | Rescate/Estabi | 8 |

     (Este orden de los canales se debe a que la unidad Spirit hace
     suposiciones sobre la posición de los canales en el flujo de datos
     SBUS.)

6. **Límites de los canales** (pestaña Diagnóstico): para que la unidad FBL
   funcione correctamente, es necesario calibrar los límites de los canales
   de radio y comprobar los centros:

   - En la radio, asegúrese de que todos los subtrims y trims están a cero.
   - Ajuste su paso colectivo a la posición central de la palanca para dar
     una salida de 1500uS en [Salidas](../model-setup/outputs.md).
   - Encienda la unidad FBL y compruebe que los canales de alerón,
     profundidad, cabeceo y timón están centrados al 0 % en la pestaña
     Diagnóstico (la unidad FBL detecta automáticamente la posición neutral
     durante cada inicialización).
   - Mueva los controles hasta sus límites y ajuste los valores de
     recorridos **Mínimo**/**Máximo** correspondientes en Salidas para
     conseguir una lectura de exactamente +100 %/−100 % en la pestaña
     Diagnóstico, comprobando también que la dirección del movimiento de
     las barras coincide con la de las palancas.

   !!! warning
       No utilice las funciones subtrim o trim de su emisora para estos
       canales, ya que la unidad Spirit FBL las considerará como un comando
       de entrada, no como calibración.

7. Ajuste el valor **Offset** en la mezcla Gyro Gain para asegurar que se
   consigue el Heading Lock.

Después de estos ajustes, todo debería estar configurado con respecto a la
emisora. Ahora puede continuar con el resto de la configuración del FBL
según el manual del Spirit FBL.
