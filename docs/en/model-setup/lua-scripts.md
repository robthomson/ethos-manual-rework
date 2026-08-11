# Lua Scripts (Model)

![Lua config](../assets/model-lua-config.png)

This menu only appears once a Lua **source** or **task** script has been
installed under `scripts/` on the SD card/eMMC (see [File
Manager](../system-setup/file-manager.md#top-level-folders)) — it's for
activating and configuring those scripts **per model**, not for installing
them. Once installed, a source or task is available globally to every
model; this page is where each model opts in and sets its own
configuration. Example source and task scripts are published on the
Ethos-Feedback-Community site (`/lua/examples/task`,
`/lua/examples/source`).

## Lua tasks

Every installed task is listed with an enable toggle per model. Enabling
one reveals its configuration form (if it has one) — the task script
supplies its own read/write functions so each model can save its own
settings. For example, a task might expose a configurable numeric range
that's set independently per model.

## Lua sources

The same pattern for sources: enable per model, then configure via
whatever form the source script provides. A source registered this way
becomes usable as an ordinary
[source](../getting-started/user-interface-and-navigation.md#choosing-a-source)
anywhere else in Ethos, exactly like a built-in one.

## For script authors

Sources and tasks are registered from Lua via `system.registerSource()`
and `system.registerTask()` — see the Ethos Lua Reference Guide, and
[Lua Scripts](../lua-scripts/index.md) in this manual for the general
scripting environment (widgets are a separate, related mechanism — see
[Custom Widgets](../displays/custom-widgets.md)).
