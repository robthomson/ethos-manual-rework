---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Información

![Información del sistema](../assets/system-info.png)

Detalles del firmware del sistema, tipo de gimbal, información de los módulos de RF interno/externo, información del receptor vinculado, tiempo de uso de la radio, registros de errores y restablecimiento de fábrica.

## Información de la radio

- **Número de serie** — el número de serie de la radio.
- **Firmware** — versión de Ethos y tipo de radio (p. ej. X20).
- **Versión de firmware** — variante de compilación, p. ej. FCC, LBT o Flex.
- **Fecha** — fecha y hora de compilación del firmware.
- **RAM disponible** — memoria RAM libre del sistema, útil para detectar un
  script Lua que no funciona correctamente; también está disponible como [fuente](../getting-started/user-interface-and-navigation.md#choosing-a-source) del sistema,
  de modo que puede mostrarse en un widget.
- **Sticks** — versión de los sensores Hall del gimbal instalado (o «ADC» para gimbals
  analógicos).
- **Módulo interno** — versiones de hardware y firmware del módulo de RF
  interno.
- **Receptor** — datos del receptor vinculado actualmente, que se muestran a continuación del
  módulo interno. Si un receptor redundante comparte la misma ranura que el
  principal, ambos se alternan en la pantalla (p. ej. un Archer SR10 Pro
  mostrado junto a su R9MM-OTA redundante bajo «Receiver1»).
- **Módulo externo** — datos de hardware y firmware de un módulo de RF externo
  FrSky instalado que utilice el protocolo ACCESS. Los módulos Multi-protocol
  no se muestran aquí.

![Información del X20 Pro](../assets/system-info-x20pro.png)

## Tiempo de uso de la radio

![Tiempo de uso de la radio](../assets/system-info-radio-runtime.png)

Registra el tiempo total de uso de la emisora; **Reset** lo pone a cero.

## Errores

![Errores](../assets/system-info-errors.png)

Un triángulo rojo en la barra superior de la vista principal indica que Ethos ha registrado un error,
que aquí se muestra en detalle. Entre las causas se encuentran:

- **Errores de scripts Lua** — un problema en un script Lua en ejecución.
- **Error de copia de seguridad en RAM** — un modelo demasiado grande para la RAM de copia de seguridad de modelos. Ethos
  la amplió de 4K a 32K, por lo que ahora es poco probable que ocurra, pero si sucede,
  se trata de un error importante: el modelo se carga más lentamente desde la tarjeta
  SD en lugar de hacerlo desde la RAM de copia de seguridad si se activa el [Modo de
  emergencia](../getting-started/emergency-mode.md).
- **Uso de una compilación nightly del firmware** — un recordatorio de que las compilaciones nightly
  no están pensadas para volar.

**Reset** borra los errores registrados, algo muy práctico en plena sesión de depuración de Lua.

## Restablecimiento de fábrica

![Restablecimiento de fábrica](../assets/system-info-factory-reset.png)

Devuelve la radio a los ajustes de fábrica íntegramente desde la propia radio, sin necesidad
de conectarla a un PC.

![Confirmación del restablecimiento de fábrica](../assets/system-info-factory-reset-confirm.png)

!!! danger
    Al confirmar se borran **todos** los modelos, registros, capturas de pantalla, documentos,
    scripts, bitmaps y ajustes de la radio. Una barra de progreso muestra el avance del borrado,
    tras el cual se expulsan todas las unidades y la radio se reinicia.

La página de información de la X20 Pro/R/RS muestra la información equivalente para esa
familia de radios.
