# Curves

![](../assets/model-icon-curves.png)

Curves may be used to modify the control response in the Mixes or Outputs. While the standard Expo curve is available directly in those sections, this section is used to define any custom curves that may be required. The 'Add curve' function may also be reached from the Mixes and Outputs edit screens directly.

There are 50 curves available.

![](../assets/model-curves-add.png)

There are no default curves (except Expo which is built in). Tap on the ‘+’ button to add a new curve.

Once curves have been defined, tapping on one will bring up a popup menu, allowing you to edit, move, copy/paste, clone or delete that curve. You can also add a new curve by selecting ‘Add’, or by tapping on the ‘+’ symbol next to the column headings.

![](../assets/model-curves-edit.png)

The initial screen allows you to name your curve, and to select the curve type.

![](../assets/model-curves-type.png)

The available curve types are:

## Expo

The default exponential curve has value of 40.

![](../assets/model-curves-expo.png)

A positive value will soften the response around 0, while a negative value will sharpen the response around 0. Softening the response around mid stick helps to avoid over controlling the model, especially for beginners.

## Function

![](../assets/model-curves-fn-types.png)

The following mathematical function curves are available:

x > 0

![](../assets/model-curves-fn-xgt0.png)

If the source value is positive, then the curve output follows the source.

If the source value is negative, then the curve output is 0.

Offset

![](../assets/model-curves-fn-xgt0-offset.png)

Note that all curves can have a positive or negative offset which will shift the curve upwards or downwards on the Y axis. Curves offsets and Y value have a one decimal precision.

x < 0

![](../assets/model-curves-fn-xlt0.png)

If the source value is negative, then the curve output follows the source.

If the source value is positive, then the curve output is 0.

|x|

![](../assets/model-curves-fn-barx.png)

The curve output follows the source, but is always positive (also called ‘absolute value’).

f > 0

![](../assets/model-curves-fn-fgt0.png)

If the source value is negative, then the curve output is 0.

If the source value is positive, then the curve output is 100%.

f < 0

![](../assets/model-curves-fn-flt0.png)

If the source value is negative, then the curve output is -100%.

If the source value is positive, then the curve output is 0.

|f|

![](../assets/model-curves-fn-barf.png)

If the source value is negative, then the curve output is -100%.

If the source value is positive, then the curve output is +100%.

## Custom

Points count

![](../assets/model-curves-custom5.png)

The default custom curve has 5 points. You may have up to 21 points on your curve.

##### Menu buttons

![](../assets/Pictures/1000000000000018000000181B9B646A.png) The source(s) configured in the curve’s mixes may be used, or optionally any other convenient analog input. If you select this 'Auto analog input' option, the first stick, slider or pot you move will be used as the source for X.

![](../assets/Pictures/10000000000000280000001EF06CB86B.png)When selected, the nearest curve point on the X axis will be automatically selected for adjustment with the rotary encoder.

The input must be adjusted to align the X value with a curve point before adjustment is made.

![](../assets/Pictures/100000000000001500000019F279C5CD.png) Tapping on this icon, or pressing the ENTER key while in graph edit mode will toggle Lock mode on and off. When enabled, all inputs are locked so that you can release the stick input, allowing you to observe the control surfaces while you adjust your curve.

To assist in setup, the cursor will be active, showing the value of the input that is driving the curve.

![](../assets/model-curves-custom5-2.png)

Curves offsets and Y value have a one decimal precision.

Smooth

![](../assets/model-curves-custom5-2-smooth.png)

If enabled a smooth curve is created through all points.

Easy mode = On

Easy mode has equidistant fixed values on the X axis, and only allows the Y coordinates for the curve to be programmed.

Points

With Easy Mode On, only the Y coordinates may be configured (see examples above).

Easy mode = Off

![](../assets/model-curves-custom-easy-off.png)

Points

With ‘Easy mode’ Off, both the X and Y coordinates may be configured, (see example above).  Note that the -100% and +100% X coordinates for the curve end-points cannot be edited, because the curve must cover the full signal range.

## Function curve ***offset*** change in flight

![](../assets/model-curves-fn-offset-var.png)

The above example shows the Offset parameter of a curve of type “Function" driven by a Var, which could possibly be adjusted in flight by a reassigned Trim.

## Curve point change in flight

![](../assets/model-curves-custom-with-var.png)

In this example above the middle curve point is being driven by a Var, which again could be adjusted in flight by a reassigned Trim. Please refer to the [VARs](variables.md) section for more details.
