# Basic layout of a Lua widget

A custom Lua widget has the following basic structure:

## key (string)

The widget must have a unique key.

## name (string or function)

The name function takes no arguments and returns the widget name as a string. The name can simply be a string, or the result of a function. For example, the name can be in a different language depending on locale.

## create (function)

The create handler function is called on widget creation. It takes no arguments and will return the widget table which is then later passed to all functions. Initialize your variables here and store the state in the returned widget table.

## configure (function)

The configure handler function is called when the user enters widget configuration. It takes the widget table returned by create() as its only argument and returns nothing. It is called when the user enters the widget configuration. Here you can create the configuration form and use it to change values in the widget table.

## wakeup (function)

The wakeup handler function is called during each loop, i.e. every 50ms. It takes the widget table as its only argument and returns nothing.

The wakeup() should check if anything has changed. If yes, a refresh is needed so the invalidateWindow() function should be called. This will cause the paint() function to be called. You should make sure this function is very fast, ideally doing nothing most of the time.

## event (function)

The event handler function called when an event is received. ETHOS provides the ability to catch any event in a widget, through this event function.

## paint (function)

The paint function ‘draws’ the widget. It takes the widget table as its only argument and returns nothing. It should be called when a refresh is needed, and is automatically called whenever lcd.invalidate() has been called. It can be slow, so only paint if something has changed.

## read (function)

Optional read handler. In ETHOS it is possible to use the storage as the user wishes.

## write (function)

Optional write handler. In ETHOS it is possible to use the storage as the user wishes.

## init(function)

The init function is used to register the widget and various callbacks. You might have something like this at the bottom of your script:

Code:

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

Note that 'key' is a unique identifier for your widget. The various functions listed are used in the widget lifecycle.

Lua scripts are stored in the scripts/ folder on the SD card or eMMC, preferably organized in folders.

Please refer to the rcgroups ‘FrSky ETHOS Lua Script Programming’ thread for more information.
