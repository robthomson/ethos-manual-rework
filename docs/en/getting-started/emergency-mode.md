# Emergency Mode

Emergency mode is the radio’s response to an unexpected event like a watchdog reset. The watchdog is a timer that is continually restarted by different parts of Ethos. If a failure of any kind prevents the watchdog timer from being restarted, it will time out and cause a hardware reset of the radio. In this emergency mode the radio restarts extremely quickly, without any of the normal startup checks so that you get back control of your model as quickly as possible. The SD card or eMMC is not accessed in emergency mode.

Emergency mode provides only the essential functions for controlling your model but none of the high level functions. The screen will go blank and display the words ‘EMERGENCY MODE’, accompanied by a 300ms beep repeating continually every 3 seconds. Voice alerts, running of scripts, logging etc. will cease operating. If emergency mode occurs, you should obviously land as quickly as possible.

The most common cause of emergency mode is SD card failure.

## Emergency mode test

In some cases, it can be helpful for users to be able to test the emergency mode.

![](../assets/Pictures/1000000000000320000001E0CAE58A4D.png)

A System tool can be added to test the emergency mode. Tap on the Emergency Test icon to initiate the test.

![](../assets/Pictures/1000000000000320000001E07840F732.png)

A dialog will ask for confirmation to proceed.

![](../assets/Pictures/1000000000000320000001E0FC0300AF.png)

The radio will enter Emergency Mode.
