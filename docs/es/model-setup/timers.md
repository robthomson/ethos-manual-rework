---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Temporizadores

![Temporizadores](../assets/model-timers.png)

Ocho temporizadores totalmente programables, cada uno con cuenta ascendente o
descendente. Añada uno con el **+** situado junto a los encabezados de columna,
o mediante **Añadir** más abajo. Al tocar un temporizador se abren las opciones
de reinicio/edición/añadir/mover/copiar-pegar.

![Edición de temporizador](../assets/model-timer1-edit.png)

## Campos comunes (cuenta descendente y ascendente)

- **Valor** — la lectura actual del temporizador.
- **Nombre** — editable.
- **Modo** — **Up** (ascendente) o **Down** (descendente).
- **Valor inicial** (solo cuenta descendente) — el valor desde el que se
  descuenta.
- **Valor de alarma** (solo cuenta ascendente) — el valor a partir del cual se
  considera que el temporizador ha transcurrido; sigue contando más allá de este
  valor, pero se muestra en rojo en los widgets de temporizador.
- **Condición de inicio** — pone en marcha el temporizador. Si la **condición de
  parada** se deja en su valor predeterminado, la condición de inicio controla
  por sí sola el arranque *y* la parada. En caso contrario, el temporizador se
  inicia la primera vez que la condición de inicio se cumple y continúa
  funcionando a partir de ese momento.
- **Condición de parada** — si no se deja en su valor predeterminado, controla el
  temporizador una vez en marcha: detenido mientras sea verdadera, en marcha
  mientras sea falsa. En el ejemplo siguiente, un temporizador se inicia cuando
  `ThrottleActive` pasa a ser verdadero y se detiene cuando la telemetría deja de
  estar activa:

  ![Condición de parada](../assets/model-timer1-edit-stop.png)

- **Fuente de temporización proporcional** — `---` cuenta en tiempo real.
  Cualquier otra fuente (por ejemplo, el stick de acelerador o el canal de
  acelerador) escala la velocidad del temporizador: a −100 % el temporizador
  está detenido, a +100 % funciona a velocidad de tiempo real, y escala
  proporcionalmente entre ambos extremos.
- **Reinicio** — un interruptor, interruptor de función, interruptor lógico o
  posición de trim que reinicia el temporizador; se mantiene reiniciado mientras
  la condición sea verdadera.
- **Persistente** — conserva el valor del temporizador tras apagar la emisora o
  cambiar de modelo, recuperándolo la próxima vez que se use el modelo.
- **Voz** — qué [paquete de voz](../system-setup/general.md#audio-settings)
  anuncia este temporizador.

## Acciones de audio

![Añadir acción de audio](../assets/model-timer1-add-action.png)
![Tipo de acción](../assets/model-timer1-action-type-select.png)
![Acción de cuenta atrás](../assets/model-timer1-action-countdown.png)

Configuración de avisos totalmente flexible para cada temporizador. Cada acción
tiene un tipo — **Countdown** (cuenta atrás hablada), **Beep countdown** (pitidos
en lugar de voz), **Play file** (reproducir archivo) o **Play value**
(reproducir valor) — además de:

- **Start** — el valor desde el que comienza la cuenta atrás de esta acción.
- **Step** — intervalo de anuncio, hasta 10 minutos (600 s).
- **Haptic** — acompañar el anuncio con vibración.

Un conjunto típico de tres acciones:

![Resumen de acciones](../assets/model-timer1-actions-summary.png)
![Acciones del temporizador 2](../assets/model-timer2-actions-summary.png)

1. Cuenta atrás hablada a partir de 2:00 restantes, cada 30 s, con vibración.
2. Cuenta atrás con pitidos a partir de 0:10 restantes, cada 1 s, con vibración.
3. Un archivo personalizado (por ejemplo, `timer-1-elapsed`) reproducido al
   transcurrir el tiempo, con vibración.

Añada más acciones con **Añadir**; la lista se ejecuta por orden de prioridad,
con la **prioridad más alta al final**.

Consulte también el [widget de pantalla Timer Log](../displays/index.md#widget-types)
para obtener un registro continuo de las ejecuciones anteriores del temporizador.

![Widget de temporizador](../assets/model-timers-widget.png)
