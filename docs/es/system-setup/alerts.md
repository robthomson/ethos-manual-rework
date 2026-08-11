---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Alertas

![Alertas](../assets/system-alerts.png)

Cuatro avisos de ámbito general de la emisora, cada uno activable de forma
independiente — distintos de las [funciones especiales](../model-setup/special-functions.md)
y los [interruptores lógicos](../model-setup/logical-switches.md) por modelo que
usted mismo configura.

- **Modo silencioso** — un aviso hablado al arrancar cuando esta comprobación
  está activada y [General → Modo de audio](general.md) está ajustado a
  Silencioso, como recordatorio de que la emisora está silenciada.
- **Tensión principal** — "Radio battery is low" cuando la batería principal de
  la emisora cae por debajo del umbral de **Tensión baja** ajustado en
  [Batería](battery.md).
- **Tensión RTC** — "RTC battery is low" cuando la pila de botón del RTC cae por
  debajo de 2,5 V (el umbral predeterminado). El registro de datos depende del
  reloj en tiempo real; una hora no válida dificulta la lectura de los registros,
  especialmente al distinguir unas sesiones de vuelo de otras. Este aviso puede
  silenciarse temporalmente mientras se espera para sustituir la pila, pero no
  debería dejarse desactivado indefinidamente.
- **Aviso de conflicto de sensores** — detecta IDs de sensores de telemetría en
  conflicto. Solo conviene desactivarlo si tiene sensores que no cumplen la
  especificación S.Port.
- **Inactividad** — un aviso hablado "Prolonged inactivity" (más una vibración
  háptica, por si el volumen está bajado) después de que la emisora haya
  permanecido sin usarse durante más tiempo del configurado — 10 minutos de
  forma predeterminada.
