# Displays

![Display home](../assets/display-home.png)

The home screen is one or more **display screens**, each built from
**widgets** you place and configure yourself. Pressing `DISP` opens the
display editor for the current screen.

## Adding a widget

![Widget types](../assets/display-widget-types.png)

Every screen is a grid; tapping an empty cell opens the widget picker.
Widgets range from simple text and numeric readouts to gauges, charts, and
full telemetry logs. Once placed, tapping a widget again opens the same
options menu used to resize, move, or remove it:

![Widget config options](../assets/display-widget-config-options.png)

Selecting a widget's own settings opens a widget-specific configuration
form. The **source** field — what value the widget shows — uses the same
[source picker](../getting-started/user-interface-and-navigation.md#choosing-a-source)
as everywhere else in Ethos:

![Change widget source](../assets/display-change-source.png)

## Widget types

**Value** — a single numeric or telemetry reading, shown as text:

![Value widget config](../assets/display-widget-value-config.png)

Most sources also support reducing to a live **min** or **max**, useful for
things like worst-case RSSI over a flight:

![Value widget min](../assets/display-widget-value-min.png)
![Value widget min RSSI](../assets/display-widget-value-min-rssi.png)

Once placed, it renders as a plain readout on the screen:

![Telemetry value widget](../assets/display-widget-value-telemetry.png)

**Bitmap** — displays a static image (e.g. a model photo), or a set of
images swapped based on a source's value (e.g. a battery icon that changes
with voltage):

![Bitmap widget config](../assets/display-widget-bitmap-config.png)
![Bitmap widget type](../assets/display-widget-bitmap-type.png)

**LiPo** — a purpose-built battery gauge, reading cell count and voltage
directly from a source:

![LiPo widget config](../assets/display-widget-lipo-config.png)
![LiPo widget](../assets/display-widget-lipo.png)

**Channels** — a live bar-graph view of output channel positions:

![Channels widget config](../assets/display-widget-channels-config.png)
![Channels widget](../assets/display-widget-channels.png)

**Line Chart** — plots a source's value over time:

![Line chart widget config](../assets/display-widget-line-chart-config.png)
![Line chart widget](../assets/display-widget-line-chart.png)

Tapping a live line chart opens its own zoom/pan options:

![Line chart options](../assets/display-widget-line-chart-options.png)

**Text** — static or source-driven label text, useful for annotating a
screen layout:

![Text widget config](../assets/display-widget-text-config.png)
![Text widget](../assets/display-widget-text.png)

**Timer Log** — a scrollable log of past timer runs (useful for tracking
flight-pack usage over a session):

![Timer log widget config](../assets/display-widget-timer-logs-config.png)
![Timer log widget](../assets/display-widget-timer-log.png)

Tapping an entry opens per-run detail:

![Timer log entry menu](../assets/display-widget-timer-log-menu.png)

**GPS Map** — plots live GPS position on a track, for models with a GPS
sensor:

![GPS map widget config](../assets/display-widget-gps-map-config.png)

## Screen-level options

Beyond individual widgets, each screen has its own settings — layout grid
size, background, and which screens are included in the `PAGE` cycle:

![Screen config options](../assets/display-screen-config-options.png)

A fully configured home screen combines several widgets into one glanceable
layout:

![Main view](../assets/display-main-view.png)

See [Additional Displays](additional-displays.md) for adding more screens
beyond the default, and [Custom Widgets](custom-widgets.md) for
Lua-scripted widgets beyond the built-in set.
