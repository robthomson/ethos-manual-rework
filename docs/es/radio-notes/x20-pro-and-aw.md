---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![Comprobación de hardware del X20 Pro](../assets/system-hardware-check-x20pro.png)

Diferencias respecto al X20S, que es la referencia con la que está escrito este manual;
se aplican al **X20 Pro** y, en su mayoría, se extienden también al **X20 Pro AW**
y a la familia **X20R/RS**.

- **Almacenamiento** — memoria interna eMMC de 8 GB por defecto, SD card opcional — véase
  [General → Ubicación del
  almacenamiento](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **Trims adicionales** — añade los interruptores de trim **T5** y **T6** — véase
  [Trims](../model-setup/trims.md#trim-settings).
- **Interruptores adicionales** — dos pulsadores con enclavamiento, **K** y **L**,
  en los hombros traseros, además de las posiciones de interruptor **M**/**N** si están
  cableadas (habitualmente interruptores en el extremo de los sticks) — véase [Hardware →
  Interruptores](../system-setup/hardware.md#switches-settings).
- **Potenciómetros adicionales** — **Ext1**/**Ext2**, empleados normalmente con gimbals de 3 ejes
  — véase [Hardware → Potenciómetros/Deslizadores](../system-setup/hardware.md#potssliders-settings).
  Esto desplaza el índice del [inspector de valores ADC](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 se sitúan entre Pot2 y los deslizadores.
- **Realimentación háptica** — el **X20 Pro AW** y el **X20RS** se suministran con gimbals MC20R
  que incorporan motores hápticos de vibración en los sticks; un **X20 Pro** o
  un **X20R** pueden obtener lo mismo mediante la actualización retroadaptable a gimbals MC20R,
  que se habilita en [Hardware → Habilitar las mejoras de gimbal
  háptico](../system-setup/hardware.md#radio-specific-hardware-options).
  Una vez habilitada, [Seleccionar motores
  hápticos](../model-setup/special-functions.md#actions) ofrece Por defecto,
  Todos los motores, Stick izquierdo o Stick derecho.
- **Encoder rotativo** — el X20 Pro AW y el X20R/RS emplean un encoder más sensible;
  la opción **medios pasos** en [Hardware → Opción de
  encoder](../system-setup/hardware.md#radio-specific-hardware-options)
  atenúa su respuesta.
- **Módulo de RF interno** — el X20 Pro/R/RS emplean el módulo **TD-ISRM Pro**
  (compatible con LoRa, con modos tándem de doble banda y TD-Pro además
  de ACCESS/ACCST D16), en lugar del módulo TD-ISRM del
  X18/X20/X20S/X20HD — véase [Sistema RF](../model-setup/rf-system.md).
