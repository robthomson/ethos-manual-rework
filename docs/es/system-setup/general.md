---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# General

![Ajustes generales](../assets/system-general.png)

Abarca los atributos de pantalla, el audio, el vario, la vibración háptica y la barra de herramientas superior.

## Atributos de pantalla

- **Language** — el idioma de los menús de la pantalla (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português y otros).
- **Keyboard** — disposición del teclado virtual: QWERTY, QWERTZ o AZERTY.
- **Brightness** — control deslizante para el brillo de la retroiluminación; si mantiene pulsado `ENT`
  podrá gobernarlo desde una fuente (por ejemplo un slider, como en el ejemplo siguiente)
  o forzarlo al mínimo/máximo.

  ![Menú de brillo](../assets/system-general-brightness-menu.png)
  ![Deslizador de brillo](../assets/system-general-brightness-slider.png)

  !!! note
      Si **Brightness** tiene el mismo valor que **Sleep mode brightness**, la pantalla táctil
      seguirá activa incluso mientras la emisora esté «dormida».

- **Wake up** — qué elementos sacan del reposo a la retroiluminación (puede
  habilitarse más de uno): **Always on** (nunca se duerme), **Sticks**,
  **Switches**, **Gyro** (al inclinar la emisora). Las teclas siempre la despiertan,
  independientemente de estos ajustes.
- **Sleep** — tiempo de inactividad antes de que se apague la retroiluminación (aparece atenuado
  si Wake up está configurado como Always on).
- **Sleep mode brightness** — brillo de la retroiluminación durante el reposo.
- **Dark mode** — tema de pantalla claro u oscuro.
- **Highlight Color** — color de realce de la interfaz (por defecto `#F8B038`).

## Ajustes de audio {: #audio-settings }

![Ajustes de audio](../assets/system-general-audio.png)

- **Audio language** — idioma de los anuncios de voz.
- **Elección de voces** — Ethos admite varios paquetes de voz simultáneos:

  - **Voice 1 (main)** — se utiliza para todos los anuncios integrados del sistema. Para
    el inglés, la elección predeterminada es entre los paquetes americano (`us`) y británico
    (`gb`), que se leen de `audio/en/us/system` y `audio/en/gb/system`.
    Los archivos de sonido de usuario para la [función especial Play Audio](../model-setup/special-functions.md)
    se colocan en `audio/en/us/` o en `audio/en/gb/`, respectivamente.
  - **Voice 2 / Voice 3** — paquetes adicionales, por ejemplo una voz
    TTS personalizada. Cada uno necesita la misma estructura de carpetas que Voice 1; por ejemplo, una voz
    llamada «Susan» necesita `audio/en/Susan/` para los sonidos de usuario y
    `audio/en/Susan/system` para sus sonidos del sistema (toda voz necesita una
    carpeta `/system`, ya que es de donde leen **Play Value** y los anuncios
    de los cronómetros; con cada versión de audio se distribuye una lista `.csv` de los
    archivos de sonido estándar del sistema). Una vez instalada, una voz puede
    asignarse a cada cronómetro y a cada función Play Audio, o incluso establecerse como Voice
    1 para sustituir por completo los anuncios del sistema.
  - **Voice "default"** — se instala automáticamente como alternativa segura (y
    sirve para evitar problemas de conversión desde instalaciones 1.4.x): si Voice 1 no
    está ya configurada durante una instalación o actualización, se establece en `default`, que lee
    de `audio/en/default/system`. Los archivos de sonido personalizados más solicitados
    para Play Audio se encuentran en `audio/en/default/`.

- **Main volume** — control deslizante para el volumen general del audio (mantenga pulsado `ENT` para
  gobernarlo desde un pot); durante el ajuste suenan pitidos para que pueda valorar el
  nivel de oído.
- **Audio mode**:
  - **Silent** — sin audio (aun así activa la [alerta de modo silencioso](alerts.md)
    al arrancar, si está habilitada).
  - **Alarms only** — solo se oyen las alarmas.
  - **Default** — sonidos normales.
  - **Often** — añade pitidos de error cuando un valor se lleva más allá de su
    mínimo o máximo.
  - **Always** — añade, además de lo anterior (Often), pitidos para la navegación normal por los menús.
  - **Bluetooth** (solo X20S/HD/Pro/R/RS) — envía el audio a un dispositivo
    Bluetooth emparejado (auriculares, etc.). Elija **Search Devices**, ponga el
    dispositivo de destino en modo de emparejamiento y selecciónelo cuando aparezca:

    ![Emparejamiento Bluetooth](../assets/system-general-audio-bluetooth.png)
    ![Búsqueda Bluetooth](../assets/system-general-audio-bluetooth-searching.png)
    ![Dispositivo Bluetooth seleccionado](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Conectando por Bluetooth](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth conectado](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Speaker mute** controla entonces el altavoz interno: siempre activo,
    solo mientras la telemetría esté activa, o gobernado por una fuente (por ejemplo un
    interruptor). La emisora recuerda el dispositivo emparejado; para un funcionamiento normal,
    encienda la emisora antes que el dispositivo Bluetooth y espere unos
    segundos tras la conexión para que el silenciado del altavoz vuelva a activarse.

## Vario {: #vario }

![Audio del vario](../assets/system-general-audio-vario.png)

- **Volume** — volumen relativo del tono del vario.
- **Pitch zero** — frecuencia del tono con velocidad de ascenso cero.
- **Pitch max** — frecuencia del tono con la velocidad de ascenso máxima.
- **Repeat** — retardo entre pitidos con el tono a cero.

Consulte también el sensor VSpeed en [Telemetría](../model-setup/telemetry.md)
y la [función especial Play Vario](../model-setup/special-functions.md)
para conocer más detalles del comportamiento del vario.

## Vibración

- **Strength** — control deslizante para la intensidad de la vibración háptica.
- **Mode** — el mismo conjunto de opciones que Audio mode, más arriba.

## Ubicación de almacenamiento (X18 y X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Estas emisoras disponen de una eMMC interna de 8 GB. Por defecto, Ethos la utiliza, con lo que
la SD card es opcional, pero puede seleccionar la eMMC, una SD card o una
combinación de ambas. Si traslada el sistema y los modelos a una SD card, copie
las carpetas y archivos correspondientes (incluidos audio y bitmaps) **antes**
de cambiar la ubicación de almacenamiento.

![Ubicación de almacenamiento](../assets/system-general-storage.png)

## Barra de herramientas superior

![Ajustes de la barra superior](../assets/system-general-topbar.png)

- **Digital voltage** — muestra el voltaje de la batería de la emisora como un número en lugar de
  como una barra en la barra de herramientas superior.
- **Digital RSSI** — lo mismo, para el RSSI de 2,4 GHz y de 900 MHz.
- **Select model at power on** — muestra la pantalla de selección de modelo al
  arrancar, antes de que aparezcan las alertas de la lista de comprobación del modelo anterior, de modo que pueda
  cambiar de modelo sin tener que descartarlas primero. El último modelo utilizado
  aparece resaltado por defecto.

  ![Selección de modelo al arrancar](../assets/system-general-model-start.png)

## Preselección del modo USB

![Modo USB](../assets/system-general-usb.png)

Lo que ocurre automáticamente cuando la emisora se conecta a un PC por USB:

- **Not set** — pregunta qué opción usar en el momento de la conexión.
- **Joystick** — entra inmediatamente en modo joystick para un simulador de RC.
- **Ethos Suite** — entra inmediatamente en modo Ethos para [Ethos
  Suite](../ethos-suite/index.md).
- **Serial** — entra inmediatamente en modo Serial, enviando las trazas de depuración de Lua
  por USB-Serial a 115200 bps (puede ser necesario un controlador de puerto COM virtual
  para Windows).
