# Basic Widget Layout

A custom Lua widget (see [Custom Widgets](../displays/custom-widgets.md)
for installing one) is built from a small set of named fields/handlers:

- **`key`** *(string)* — a unique identifier for the widget.
- **`name`** *(string or function)* — the widget's display name. Either a
  plain string, or a function taking no arguments and returning one —
  useful for a name that varies by locale.
- **`create`** *(function)* — called once when the widget is created,
  taking no arguments. Returns a **widget table**, which is then passed
  to every other handler below — initialize your state here and store it
  in that table.
- **`destroy`** *(function, optional)* — called when the widget is
  deleted.
- **`configure`** *(function)* — called when the user opens the widget's
  configuration screen, taking the widget table from `create()` as its
  only argument, returning nothing. Build the configuration form here and
  use it to update values in the widget table.
- **`build`** *(function, optional)* — called on every layout change once
  the widget is placed on a screen, and also right after creation and
  configuration.
- **`wakeup`** *(function)* — called every loop (roughly every 50ms),
  taking the widget table, returning nothing. Check here whether anything
  changed; if so, call `invalidateWindow()` to trigger a repaint via
  `paint()`. Keep this handler fast — ideally doing nothing at all most
  of the time it's called.
- **`event`** *(function)* — called when the widget receives an event;
  Ethos routes arbitrary events to a widget through this handler.
- **`paint`** *(function)* — draws the widget, taking the widget table,
  returning nothing. Called automatically whenever `lcd.invalidate()` has
  fired. Can be comparatively slow, but should still only actually redraw
  when something's changed.
- **`menu`** *(function, optional)* — called when the widget's contextual
  menu is built, to add extra entries beyond the standard ones. Returns a
  table of `{name, function}` pairs.
- **`read`** *(function, optional)* — reads persisted widget storage.
- **`write`** *(function, optional)* — writes persisted widget storage.
- **`persistent`** *(boolean, optional)* — enables persistent data
  storage for the widget.
- **`title`** *(boolean, optional)* — forces the widget's title on or off.
- **`init`** *(function)* — registers the widget and its callbacks with
  Ethos. Typically the last thing in the script:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` must be unique across installed widgets; the other fields tie into
the widget's lifecycle as described above.

Scripts live under `scripts/` on the SD card/eMMC, ideally organized into
per-widget folders (see [File
Manager](../system-setup/file-manager.md#top-level-folders) and [Example
Script Locations](example-script-locations.md)). See the *FrSky ETHOS Lua
Script Programming* thread on rcgroups for further worked examples.
