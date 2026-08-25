# Emergency Mode

Emergency mode is the radio’s response to an unexpected event like a watchdog reset. The watchdog is a timer that is continually restarted by different parts of Ethos. If a failure of any kind prevents the watchdog timer from being restarted, it will time out and cause a hardware reset of the radio. In this emergency mode the radio restarts extremely quickly, without any of the normal startup checks so that you get back control of your model as quickly as possible. The SD card or eMMC is not accessed in emergency mode.

Emergency mode provides only the essential functions for controlling your model but none of the high level functions. The screen will go blank and display the words ‘EMERGENCY MODE’, accompanied by a 300ms beep repeating continually every 3 seconds. Voice alerts, running of scripts, logging etc. will cease operating. If emergency mode occurs, you should obviously land as quickly as possible.

The most common cause of emergency mode is SD card failure.
