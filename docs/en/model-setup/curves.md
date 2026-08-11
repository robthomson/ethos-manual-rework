# Curves

![Curve types](../assets/model-curves-type.png)

Reusable response curves for [Mixes](mixes.md#anatomy-of-a-mix) or
[Outputs](outputs.md#editing-a-channel) — the built-in Expo is available
directly in both, but anything more elaborate is defined here (or via
**Add curve**, reachable directly from either edit screen). Up to 50
curves are available; none exist by default (Expo is always built in
regardless). Add one with **+**; tap an existing curve for
**Edit**/**Move**/**Copy-paste**/**Clone**/**Delete**.

![Add curve](../assets/model-curves-add.png)

## Curve types

- **Expo** — default value 40; positive softens the response around
  center, negative sharpens it. Softening around mid-stick helps avoid
  over-controlling, especially for less experienced pilots.

  ![Expo](../assets/model-curves-expo.png)

- **Function** — a small set of fixed mathematical shapes:

  ![Function types](../assets/model-curves-fn-types.png)

  - **x > 0** — passes the source through unchanged while positive;
    outputs 0 while negative.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — the mirror: passes through while negative, 0 while
    positive.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — passes the source through as its absolute value (always
    positive).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — outputs 100% while the source is positive, 0 while
    negative (a hard switch, not a pass-through).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — outputs −100% while negative, 0 while positive.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — outputs −100% while negative, +100% while positive.

    ![|f|](../assets/model-curves-fn-barf.png)

  Every curve type — Function included — also has an **Offset**, shifting
  it up or down on the Y axis (one decimal place precision, same as Y
  values generally):

  ![Function offset](../assets/model-curves-fn-xgt0-offset.png)

- **Custom** — a point-based curve, 5 points by default, up to 21.

  ![5-point custom curve](../assets/model-curves-custom5.png)

  - **Smooth** — runs a smooth curve through all points instead of
    straight segments between them.

    ![Smoothed curve](../assets/model-curves-custom5-2-smooth.png)

  - **Easy mode** — **On** restricts editing to evenly-spaced Y
    coordinates only (X is fixed); **Off** allows editing both X and Y
    per point, except the −100%/+100% endpoints, which are locked since
    the curve must always cover the full signal range.

    ![Easy mode off](../assets/model-curves-custom-easy-off.png)

  **Editor controls** (same pattern as the [Outputs balance curve
  editor](outputs.md#balance-channels)):

  - **Source** — the curve's own mix source(s) by default, or **Auto
    analog input** to pick up the first stick/slider/pot moved.
  - Nearest-point snapping to the rotary encoder, and a **Lock** toggle
    to freeze inputs while observing the resulting control surface
    movement.
  - A live cursor shows the current input value driving the curve, to
    help line it up with a point before adjusting.

## Driving a curve from a Var

Both a Function curve's **Offset** and an individual **Custom** curve
point can be driven by a [Var](variables.md) instead of a fixed value —
and that Var can in turn be adjusted in flight via a repurposed trim:

![Function offset from a Var](../assets/model-curves-fn-offset-var.png)
![Custom curve point from a Var](../assets/model-curves-custom-with-var.png)

See [Variables](variables.md) and [How-To: In-Flight Adjustable
Compensation Curve](../how-to/in-flight-compensation-curve.md) for a full
worked example of this pattern.
