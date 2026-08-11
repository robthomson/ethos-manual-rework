# Emergency Mode

Emergency mode is Ethos's response to an unexpected low-level fault, such
as a watchdog reset. The watchdog is a timer continually restarted by
various parts of the system; if something prevents it from being
restarted, it times out and forces a hardware reset. Emergency mode then
restarts the radio as fast as possible, skipping all of the normal startup
checks so control of the model is handed back with minimal delay. The SD
card/eMMC is not accessed at all in this mode.

Only the essential functions needed to keep controlling the model are
available — none of the higher-level features. The screen goes blank
except for the words **EMERGENCY MODE**, accompanied by a repeating 300ms
beep every 3 seconds; voice alerts, Lua scripts, logging, and telemetry all
stop. If this happens in the air, land as soon as possible.

The most common trigger is SD card failure.

## Testing emergency mode

A **System tool** can be added to deliberately trigger emergency mode for
testing, so it doesn't have to be discovered for the first time in flight.
Tapping the Emergency Test icon prompts for confirmation, then puts the
radio into emergency mode exactly as a real fault would.
