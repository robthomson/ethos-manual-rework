---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Funcionamiento

## Sección de bienvenida

**Update News** — notas de la versión y recomendaciones de copia de seguridad antes
de actualizar. Ethos 1.6.0+ requiere que el módulo de RF interno y los receptores TD/TW/AP/AP
Plus estén en la v3.0.1+ para aprovechar sus mejoras. Activar
**Pre-releases** (con el servidor configurado en GitHub — consulte [Ajustes de
Suite](#suite-settings)) también muestra aquí las compilaciones previas al lanzamiento, junto con
el historial completo de versiones.

**Ethos web page** — una vista integrada de ethos.frsky-rc.com: recursos,
enlaces a plantillas de modelos y la lista de emisoras compatibles.

## Sección Radio

Gestiona la emisora conectada. Enciéndala en [modo bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) y
conéctela por USB — Suite muestra el tipo de emisora (p. ej. «X20») una vez detectada.

### Información de la emisora

- **Ethos** — versiones instaladas de firmware/bootloader; **Manage Ethos**
  lleva directamente a su actualización si están desfasadas.
- **RF Module** — firmware instalado del módulo de RF interno; **Manage
  internal module** lleva directamente a su actualización si está desfasado.
- **Model manager** / **Lua library** / **Download center** — accesos directos
  a esas herramientas.

### Actualizar Ethos {: #updating-ethos }

La pestaña **Ethos** muestra en paralelo las versiones de Firmware, Bootloader, SD card/eMMC (archivos de audio)
y memoria flash (mapas de bits del sistema) — los archivos de sistema en
la flash se actualizan ahora junto con el firmware y ya no se gestionan
por separado.

- **Write outdated components** — actualiza solo lo que está desfasado.
- **Write all components** — actualiza todo, independientemente de la versión.
- Opciones individuales **Write firmware**, **Write bootloader**, **Write audio
  files**, cada una ejecutada pulsando el botón gris oscuro situado junto a la
  opción elegida.
- **Flash from a local file** — omite la descarga y utiliza un archivo de firmware
  ya presente en el disco.

Seleccionar una versión implica elegir primero una **rama** (Stable/Testing)
y después una versión. La actualización solicita realizar antes una copia de seguridad (**Go to backup
page**) — hágala. Si el módulo de RF interno no está en la v3.0.1+, Ethos
1.6.0+ requiere actualizarlo antes de continuar (**Go to Module
manager** lo flashea automáticamente y, después, la actualización de Ethos se reanuda) — y
en los receptores TD/TW/AP/AP Plus es necesario borrar su telemetría y volver a descubrirla
después para que se adopten los nombres de sensores actualizados.

El progreso de la actualización se muestra paso a paso (cambio a bootloader,
descarga, copia, desmontaje, escritura, actualización, «Update
successful!») — la propia pantalla de la emisora también refleja el progreso de la escritura.

!!! note "Actualizaciones de versiones preliminares"
    Los archivos de una versión preliminar pueden cambiar sin que cambie su número
    de versión, algo que Suite no puede detectar — vuelva a flashear siempre una versión
    preliminar que ya tenga instalada cuando pase a ser una versión completa. Compruebe la
    fecha del firmware en [Sistema → Información](../system-setup/information.md) si
    tiene dudas.

!!! note "Actualización desde Ethos 1.2.8 o anterior"
    Puede que Suite no consiga flashear el firmware/bootloader de forma totalmente
    automática desde una versión tan antigua — en su lugar aparecerá un diálogo guiado
    de flasheo manual. En cualquier caso, expulse las unidades manualmente antes de desconectar el USB.

Los archivos de mapas de bits del sistema se actualizan ahora automáticamente junto con el firmware (no es
necesaria una gestión aparte); los archivos de audio se actualizan mediante **Write all
components** o **Write audio files** (descarga el paquete de idioma seleccionado, p. ej. «English audio pack»).

### RF Module Manager

Seleccione una versión (normalmente la más reciente) y **Flash module** para actualizar
directamente el firmware del módulo de RF interno — al terminar confirma
«...has been flashed successfully». Esto también se activa
automáticamente mediante la ruta de actualización obligatoria a la v3.0.1 descrita arriba.

### Modo Ethos

**Switch to Ethos** reinicia la emisora saliendo del modo bootloader para
ejecutar Ethos (indicado por un icono USB verde en la emisora y por la desaparición de
«(Bootloader Mode)» en el encabezado de Suite). Esto es necesario para que el
**Download center** pueda usar la emisora como intermediaria para flashear módulos,
receptores, sensores y servos. El botón pasa entonces a ser **Switch to
Bootloader** para revertirlo. **Eject Drives** desconecta la emisora
de forma limpia.

### Model Manager

Realiza copias de seguridad de los archivos de modelo y de los ajustes en el disco, o restaura una copia anterior.

!!! warning
    La restauración **no** restaura el firmware — después de restaurar
    modelos/ajustes, vuelva a flashear por separado la versión de firmware que
    corresponda realmente a esa copia de seguridad (consulte [Actualizar
    Ethos](#updating-ethos)), ya que los archivos de modelo no son retrocompatibles.

- **Backup Location** — navegue hasta una carpeta (se recuerda para cada tipo de emisora);
  debajo se muestra la fecha/hora de la última copia de seguridad.
- **Backup** — guarda los archivos de modelo, registrando junto a ellos la versión
  actual de Ethos.
- **Restore** — seleccione qué componentes recuperar: Audio (desactivado por
  defecto), Scripts, Screenshots, System Bitmaps (desactivado por defecto —
  ahora se gestiona con el firmware), Models (incluidos los archivos de texto de cualquier [lista de verificación
  definida por el usuario](../how-to/user-defined-checklist.md) almacenados
  junto a ellos), Language, User Bitmaps, Logs, System Settings.

### Lua library

Explore e instale con un clic scripts/herramientas Lua desde la biblioteca remota de
FrSky (o instale desde un zip local); los scripts instalados se muestran
junto al catálogo remoto en cuanto exista alguno.

## Sección Tools

- **Download center** — descargue cualquier firmware desde el sitio de FrSky y
  (mientras la emisora esté en modo Ethos) úsela como intermediaria para flashear un módulo,
  sensor, servo o receptor conectado mediante una conexión de actualización S.Port.
  Elija el producto de la lista (p. ej. un receptor TW SR8), explore los
  **assets** disponibles, use **Download** para guardarlo localmente o **Flash** para
  escribirlo directamente en el dispositivo conectado — una barra de progreso sigue el
  flasheo y finaliza con «...has been flashed successfully!»

- **Image manager** — convierte imágenes al formato nativo de Ethos (BMP de 32 bits,
  RGB, con canal alfa añadido solo si es necesario) en el tamaño elegido,
  conservando la relación de aspecto. Tamaños de referencia: imágenes de modelo 300×280 (X20) /
  180×168 (X18); imágenes a pantalla completa 800×480 (X20) / 480×320 (X18) — consulte
  [Gestor de archivos](../system-setup/file-manager.md#top-level-folders) para las
  reglas de nomenclatura de los mapas de bits. También permite explorar directamente las carpetas `bitmaps/gps`,
  `bitmaps/models` y `bitmaps/user` de la emisora, con soporte de subida.
  Añada imágenes a la lista de transcodificación con **+** (TIFF no está
  soportado), elija una ruta de salida (una carpeta local; directamente a la emisora
  en imágenes de modelo/usuario/GPS; o la carpeta de la emisora abierta actualmente) y,
  opcionalmente, abra automáticamente la carpeta de salida o fuerce un canal alfa.

- **Audio manager** — convierte audio al formato de Ethos (PCM lineal,
  32 kHz, mono, 16 bits little-endian). Añada archivos con **+**, elija una
  carpeta local o envíelos directamente a la carpeta `audio` de la emisora (moviéndolos
  después a la subcarpeta de voz correcta), con opción de abrir automáticamente el destino.

- **Lua development tools** — **Lua Docs** enlaza con la guía de referencia de Lua para
  Ethos (véase también el hilo de rcgroups *FrSky - ETHOS Lua Script Programming*);
  **Lua Demo Scripts** enlaza con scripts de ejemplo en el GitHub de
  Ethos-Feedback-Community; **Debug** abre una ventana de registro en vivo para
  las trazas `print()` de Lua enviadas por USB-Serial mientras la emisora está en modo
  Serial:

  1. Conecte la emisora a Suite de la forma habitual y cambie al modo Ethos.
  2. Edite los scripts Lua directamente en la unidad montada de la emisora, con cualquier
     editor de código.
  3. Abra **Lua Development Tools** → **START DEBUG** — esto reinicia la
     emisora en modo Serial/depuración y reinicializa los scripts.
  4. La salida `print()` de cada script activo se transmite al terminal de Suite.
  5. **STOP DEBUG** vuelve al modo Ethos normal para seguir editando.

- **DFU Flasher** — flashea el bootloader mediante una conexión USB con la emisora apagada
  (DFU), y funciona incluso con el firmware totalmente corrupto, ya que el
  bootloader ST subyacente reside en la ROM. Use **Select Bootloader** para elegir un
  archivo descargado (Suite informa de su versión/idoneidad), conecte la
  emisora **apagada** y pulse **Flash**.

  !!! note "«Radio connection is not detected!»"
      Normalmente se debe a un controlador DFU ausente o incorrecto. La mayoría de los PC con Windows 10+ gestionan
      los sistemas Tandem con el controlador USB DFU predeterminado, pero Windows Update
      a veces lo sustituye por uno genérico que no funciona — compruebe el
      Administrador de dispositivos y considere una herramienta como Impulse Driver Fixer.
      Los usuarios de Horus X10 en particular pueden necesitar instalar manualmente el controlador USB
      del bootloader STM32 (Impulse Driver Fixer o Zadig),
      ya que Windows 10 no lo instala por defecto.

- **Repair Tool** — para X18/S, TW Lite, XE y X20 Pro/R/RS: reformatea
  el almacenamiento interno cuando la emisora no puede leer la NAND o guardar los ajustes.

## Sección Others

- **Documentation** — enlaces al GitHub de Ethos-Feedback-Community, los
  manuales oficiales de Ethos (descargables) y unas FAQ de Ethos Suite.
- **Ethos Github** — versiones y seguimiento de incidencias (busque incidencias existentes
  antes de crear una nueva).

### Ajustes de Suite {: #suite-settings }

- **Language** — checo, alemán, inglés, español, francés, hebreo,
  italiano, neerlandés, noruego, portugués, esloveno, chino.
- **Server location** — **FrSky server** o **GitHub** (necesario para el
  acceso a versiones preliminares descrito arriba).
- **Debug options** — activar/desactivar la ventana emergente de error fatal; habilitar el registro
  completo de depuración de Suite (no solo de los fallos); abrir la carpeta de registros.
- **Version** / **Update Suite** — versión actual y comprobación manual de
  actualizaciones.
- **About** — reconocimientos de los componentes reutilizados.

## Funcionamiento desde la línea de comandos

Ethos Suite puede ejecutarse desde un terminal:

| Parámetro | Efecto |
|---|---|
| `--help` | Muestra la ayuda de la línea de comandos. |
| `--version` | Muestra la versión de Suite instalada. |
| `--list-radios` | Lista todas las emisoras FrSky compatibles. |
| `--radio-components --radio {RADIO}` (o `--radio auto`) | Lista los componentes de una emisora conectada y sus rutas. `auto` detecta automáticamente; especifique `{RADIO}` si hay más de una conectada. |
| `--get-path {COMPONENT}` | Obtiene la ruta de un componente — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` o `I18N`. |
| `--serial start` \| `--serial stop` | Activa/desactiva el modo de depuración serie. |

!!! note
    Suite no se iniciará en absoluto si no reconoce un comando válido.
