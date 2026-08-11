---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trims

![Trims](../assets/model-trims.png)

Configura el rango de trim de cada stick, el tamaño de paso y su
comportamiento, además del trim cruzado y el trim instantáneo. Las
**X20 Pro/R/RS** y la **X18** añaden dos interruptores de trim
adicionales, **T5**/**T6**, útiles para ajustes en vuelo más allá de los
cuatro sticks principales:

![Trims T5/T6](../assets/model-trims-pro-t5-t6.png)

Cada stick dispone de su propio conjunto independiente de ajustes de trim.

## Ajustes de trim {: #trim-settings }

- **Range** (rango) — por defecto ±25%, ajustable hasta el ±100% completo
  del stick. En la pantalla principal, un trim con el rango predeterminado
  muestra de −100 a 100; un trim de rango completo (100%) muestra de −400
  a 400 (4× el rango normal).

  !!! warning
      Ampliar el rango implica que mantener pulsado un trim demasiado
      tiempo puede añadir trim suficiente para hacer el modelo
      impilotable.

- **Step** (paso) — granularidad del interruptor de trim: **Extra fine**
  (extra fino), **Fine** (fino), **Medium** (medio), **Coarse** (grueso),
  **Exponential** (exponencial: fino cerca del centro, grueso hacia los
  extremos) o **Custom** (personalizado: un porcentaje concreto por clic).

  ![Opciones de paso](../assets/model-trims-step-options.png)

  | Paso | µs por clic (rango 25%) |
  |---|---|
  | Extra fine | 0,5 |
  | Fine | 1 |
  | Medium | 2 |
  | Coarse | 4 |
  | Exponential | 0,3–16 |

  Personalizado, con un rango del 25%: paso del 1% = 1 µs/clic, paso del
  100% = 128 µs/clic. Con un rango del 100%: paso del 1% = 5 µs/clic, paso
  del 100% = 512 µs/clic.

## Modo

![Modo de trim de profundidad](../assets/model-trims-mode-elevator.png)

Por defecto, un trim está siempre activo, pero **Mode** (modo) cambia ese
comportamiento. Al cambiar de modo, el trim se reinicia a 0.

- **OFF** — desactiva por completo el trim.

  ![Modo: off](../assets/model-trims-mode-option-off.png)

  Útil, por ejemplo, en un modelo eléctrico que no necesita trim de
  acelerador: el control de trim liberado puede
  [reutilizarse para ajustar una Var](variables.md).

- **Easy** — un único valor de trim compartido por todas las fases de
  vuelo. Es la opción habitual para alerones y dirección, ya que rara vez
  necesitan variar según la fase de vuelo.

  ![Modo: easy](../assets/model-trims-mode-option-easy.png)

- **Independiente por fase de vuelo** — el trim solo afecta a la fase de
  vuelo activa. Es la opción habitual para el trim de profundidad, ya que
  suele necesitar valores distintos en cada fase de vuelo (por ejemplo,
  con cambios de curvatura del ala); de hecho, esto es a menudo la razón
  principal para configurar fases de vuelo.

  ![Modo: independiente por fase de vuelo](../assets/model-trims-mode-option-fm.png)

- **Custom** — comportamiento totalmente personalizado, construido a
  partir de **comportamientos** que usted mismo añade.

### Comportamientos de trim personalizados

![Añadir un comportamiento](../assets/model-trims-mode-elevator-add-behaviour.png)
![Opciones de comportamiento](../assets/model-trims-mode-elevator-edit-behaviour.png)

Cada fila de comportamiento tiene una condición y una de estas opciones:

- **Unplugged** (desconectado) — desactiva el trim de forma selectiva bajo
  esa condición (en lugar de anularlo por completo con Mode = OFF).

  ![Unplugged](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Condición de unplugged](../assets/model-trims-mode-unplugged-select.png)

- **Normal** (por defecto) — comportamiento de trim ordinario.
- **Equal (to another trim)** (igual a otro trim) — este trim sigue
  exactamente el valor de trim de otra condición.

  ![Equal](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Offset + (another trim)** (desplazamiento sobre otro trim) — este trim
  se suma al valor de trim de otra condición.

  ![Offset](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Ejemplo práctico** — un velero con un trim de profundidad base en
**Cruise** y trims dependientes para **Speed** y **Thermal**:

![Seleccionar FM5 Speed](../assets/model-trims-mode-elevator-custom-select.png)
![Seleccionar FM4 Thermal](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Trime para vuelo nivelado en el modo predeterminado (Cruise).
2. Añada un comportamiento: **Offset + Default**, condición `FM5(Speed)`.
   Ahora cualquier ajuste de trim realizado en el modo Speed se guarda
   como un desplazamiento sobre el valor base de Cruise: separado, pero
   aún dependiente de él.

   ![Offset para Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Añada un segundo comportamiento: **Offset + Default**, condición
   `FM4(Thermal)`, del mismo modo. (Una vez que existe el primer
   comportamiento, el cuadro de diálogo ofrece también
   `Equal FM5(Speed)` y `Offset + FM5(Thermal)` como opciones, ya que
   ahora puede referenciar también ese comportamiento).

   ![Offset para Speed y Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Con esta configuración, ajustar más adelante el trim base de Cruise (por
ejemplo, tras un cambio del centro de gravedad) desplaza automáticamente
los trims de Speed y Thermal en la misma medida, ya que son
desplazamientos sobre él y no valores independientes.

- **Audio** — desactiva el anuncio de trim estándar en un trim
  reutilizado, cuando ya no tiene sentido escucharlo.

## Trims adicionales

![Añadir trim adicional](../assets/model-trims-add-trim-select.png)
![Ajustes del trim adicional](../assets/model-trims-add-trim-edit.png)

**Add an extra trim** (añadir un trim adicional) crea un trim más allá de
los cuatro sticks estándar (y T5/T6): **Name** (nombre), fuentes
**Up**/**Down** que lo accionan, además de las mismas opciones **Range**,
**Step**, **Mode** y **Audio** descritas arriba.

## Trim cruzado

![Trim cruzado](../assets/model-trims-cross.png)
![Edición del trim cruzado](../assets/model-trims-cross-edit.png)

Designa qué interruptor de trim ajusta realmente cada stick, es decir,
permite que el trim de un stick sea accionado por un control físico de
trim distinto del habitual. (T5/T6 solo están disponibles en las X20 Pro
y X18).

## Trim instantáneo {: #instant-trim }

![Trim instantáneo](../assets/model-trims-instant-trim.png)

Mientras está activo, suma las posiciones actuales de los sticks a los
trims predeterminados (y cruzados) correspondientes. Conviene asignarlo a
un interruptor accesible sin soltar los sticks: actívelo mientras vuela
recto y nivelado para fijar los trims al instante, en lugar de pulsar
repetidamente un trim cuando los ajustes están muy desviados. Desactívelo
de nuevo tras el vuelo de trimado para evitar alterar los trims
accidentalmente más adelante.

!!! note
    El trim instantáneo solo está activo mientras se visualiza una de las
    vistas principales.

## Trasladar los trims a los subtrims

![Trasladar los trims a los subtrims](../assets/model-trims-move-trims-to-subtrims.png)

Tras trimar para vuelo nivelado, traslada el valor de trim de un canal
(por ejemplo, profundidad) a su ajuste de [Subtrim](outputs.md) y devuelve
a cero el trim en pantalla: una forma limpia de comprobar que los trims de
vuelo no se han desviado desde entonces.

Cuando intervienen fases de vuelo, un canal puede tener más de un valor de
trim relevante, mientras que el Subtrim en Salidas es un único ajuste
global que se aplica a todas las fases de vuelo. Esta función lo tiene en
cuenta: toma el trim de la fase de vuelo **actualmente seleccionada**, lo
traslada al Subtrim, reinicia ese trim y ajusta el trim de todas las
*demás* fases de vuelo en ese mismo canal para compensar, de modo que la
posición real de la superficie en cada fase de vuelo permanece inalterada
en conjunto.

!!! tip
    Ejecute siempre esta función desde la misma fase de vuelo «base» (por
    ejemplo, Cruise en un velero) para mantener la coherencia: puede
    repetirse con seguridad siempre que lo haga así.

Valores grandes de trim o subtrim generan recorridos muy asimétricos; es
preferible corregir la causa raíz mecánicamente. Procure que los
varillajes queden a 90° con las superficies en neutro (los flaps son la
excepción: se sacrifica algo de recorrido hacia arriba a cambio de más
recorrido hacia abajo) y después utilice **PWM center** (centro PWM) para
afinar hasta exactamente 90° cuando el varillaje ya esté cerca.
