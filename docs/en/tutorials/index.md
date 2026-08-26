# Programming Tutorials

This section describes some programming examples for a number of models, preceded by a basic radio setup section covering the basic settings needed for any model.

- Initial radio setup example
- Basic Power Model example
- Simple 4ch Glider example
- Basic Wing example
- Basic Flybarless Helicopter example

Although these examples may appear to be for specific model types, they are merely a vehicle for explaining the Ethos way of programming. It would be useful to actually program these models on the radio, and observe the outputs on the monitor screen as the inputs are manipulated. Once these concepts and the process are understood, you should be able to adapt these examples to your model.

Initial radio setup example

This introductory section describes the initial steps in setting up the radio itself, before programming any specific models. Once completed, any of the programming examples in the following sections can be followed.

Note: These examples are not 'cookbook' in nature. They assume that the user has a basic understanding of the vocabulary of radio control models, and is familiar with navigating the Ethos menu structure. If, at any time, you are confused, please review previous sections of this manual for a refresher. In particular, please refer to the [User Interface and Navigation](../getting-started/user-interface-and-navigation.md) section to familiarize yourself with the radio's user interface, so that you can find the setup page you need easily.

### Step 1. Charge the radio and flight batteries.

Please charge the radio battery using the guidelines received with the radio. Also charge the flight batteries to be used, using a charger suitable for the battery type(s), observing all safety precautions, especially when using Lithium batteries.

### Step 2. Calibrate the hardware.

Ensure that you have performed the hardware calibration during initial startup of the radio, to confirm that the radio knows exactly where the centers and limits of each gimbal, pot, and slider are. It can be re-done by following instructions in the System \\ Hardware \\ [Calibration](../system-setup/hardware.md) section of this manual.

### Step 3. Perform the radio system setup.

The radio system setup is used to configure those parts of the radio system’s hardware that are common to all models. It differs from the '[Model Setup](../model-setup/index.md)' functions which configure the model specific settings for each model.

Please read the system setup section to familiarize yourself with all the settings in this section.

Many settings can (at least initially) be left at their defaults, but the following should be reviewed:

Date & Time

Set the current time and date.

Audio

Set up the voices section for the radio voice announcements including your custom audio files. Refer to the [General / Audio / Choice of Voices](../system-setup/general.md) section.

Sticks

Sticks mode

Select your preferred stick mode. Mode 1 has throttle and aileron on the right stick, and elevator and rudder on the left. Mode 2 has throttle and rudder on the left stick, and aileron and elevator on the right.

Note: Mode 2 is the default.

**C****aution**!  If a model is configured for Mode 2 and the TX for Mode 1, it is possible to have the motor for electric models start when the receiver is turned on.

Channel order

The default channel order for Ethos is AETR (i.e. Aileron, Elevator, Throttle, Rudder). You may prefer to set the default channel order to the order you are accustomed to. TAER is the default for Spektrum/JR, and AETR is the default for Futaba/Hitec. This setting defines the order in which the four stick inputs are inserted when a new model is created. They can of course be changed later.

###### FrSky stabilized receivers

Note that AETR is the required order if you want to use any of the FrSky stabilized receivers. However, for models with more than one surface for ailerons, elevator, rudder, flaps etc the wizard will normally group these surfaces, so for example you would get AAETR if using 2 Aileron channels.

The SRx receivers expect a channel order of AETRA or AETRAE, so the wizard can be told (in System / Sticks) to keep the 'First four channels fixed'.

Battery

Review your radio battery's specification and configure the 'Main voltage', 'Low voltage' and 'Display voltage range' as described in the [System / Battery](../system-setup/battery.md) section of this manual.

Owner registration ID

The ‘Owner registration ID’ is used with ACCESS systems. This ID becomes the ‘Registration ID’ when registering a receiver. Enter the same code in the owner registration ID field of your other transmitters you want to use the SmartShareTM feature with. Refer to the Model Setup / [RF System](../model-setup/rf-system.md) section of this manual (although it is configured in the Model Setup section, the ‘Owner registration ID’ will be used for each new model and can be considered a system setting. Please note also that the owner registration ID can be changed for a particular receiver during the registration process).

Units

Please note that in Ethos telemetry units are configured on a per sensor basis. There is no global metric or imperial setting.
