# Ethos Web Simulator

![](../assets/Pictures/1000000100000ECE0000087EC6EED3C0.png)

The Ethos web simulator is built as a WebAssembly (abbreviated Wasm), which is a portable solution enabling deployment on the web. This means it runs within a browser and does not need installation on a PC. Chrome is the recommended browser.

The Ethos web simulator lets you explore the radio capabilities and test functionality or planned model enhancements without the actual radio. It also lets you very easily explore new releases before upgrading your radio.

The web simulator may be found at [https://ethos-simulator.frsky-rc.com/](https://ethos-simulator.frsky-rc.com/)

The default initial selections are the 26.1.0-RC6 release (at the time of writing), the X20 Pro radio, and the FCC protocol. To start select the display language.

![](../assets/Pictures/1000000100000ECA0000087430BAF911.png)

When it first loads, no valid model data will be found, so it will then start running the new model wizard.

![](../assets/Pictures/1000000100000ECC000008705812BE1A.png)

Complete the wizard to configure a basic test model.

If the default release and radio are not the desired selections, select the desired Ethos release version, the radio type to be simulated, and the RF protocol.

![](../assets/Pictures/100000010000005D000000540670607D.png) Click on the Panels icon in the top menu bar, and select the Console.

![](../assets/Pictures/1000000100000ECE000008704E039C07.png)

The Console will appear next to the Display panel.

![](../assets/Pictures/1000000100000ECC0000087CC2F80823.png)

Click and drag the Console title bar, and drag it downwards. Move the mouse until the Console occupies the bottom left quadrant.

The console is useful for confirming the simulator startup sequence, and for monitoring events and error messages.

![](../assets/Pictures/1000000100000ECA00000870F03E27C8.png)

Click the Panels icon again, and repeat with the Telemetry panel, moving it to the bottom right quadrant.

![](../assets/Pictures/1000000100000ECA00000874CF5DF782.png)

In the Telemetry panel, repeatedly click on ‘Add a new sensor’ and add the sensors you want access to in your simulations.

![](../assets/Pictures/100000010000005400000051110B240F.png) To save your sensors for future sessions click on the icon and select ‘Save telemetry settings’. The telemetry settings will be saved to a file called ‘telemetry.json’ in your downloads path. Move this to a convenient location. In subsequent simulator sessions, click on the ‘Upload’ icon and select ‘Upload a JSON telemetry file’, then browse to your saved ‘telemetry.json’.

You are now ready to start simulating. The browser will remember your panel layout so you don’t need to keep arranging it.

### Recommended setup

It is best to replicate your radio’s setup in the simulator. This will provide the same functionality as you have in your radio, making it easy to test enhancements to your models without affecting your flying or modeling environment until everything works as planned.

The recommended setup steps are:

1. Make a backup of your radio using the Suite [Backup & recovery](operation.md) function.

2. In the Upload menu select ‘Upload a radio backup’ and browse to your saved backup file. (Refer to the menus below.)

![](../assets/Pictures/1000000100000ED400000878558BF0E8.png)

3. It should start with the model that was current on your radio when you made the backup. In this example an Ng2 glider was the current model.

With your familiar radio environment you can now create and test a whole new model, perhaps by basing it on one of your templates, or by making a clone of an existing model and modifying it. These approaches maximize re-use without having to program a model from scratch. Once completed, use the ‘Download a model file’ option to download the .bin model file to your downloads path. Then copy it to your radio.

### Simulator task bar

The simulator task bar has the following controls:

![](../assets/Pictures/10000001000003680000004707491117.png)

![](../assets/Pictures/100000010000003A0000003666C3C7BD.png)	Screenshot (to downloads folder)

![](../assets/Pictures/10000001000000340000003483679B57.png)	Start record (records a macro – beyond the scope of this overview)

![](../assets/Pictures/100000010000003500000034AEFCA677.png)	Panels (lists panels that have not been opened yet)

![](../assets/Pictures/1000000100000032000000354EFA6D7A.png)	Upload… (see menu below)

![](../assets/Pictures/1000000100000033000000366AC34E19.png)	Download... (see menu below)

![](../assets/Pictures/100000010000003600000035C95472AF.png)	Audio On/Off

![](../assets/Pictures/1000000100000032000000365BA45D87.png)	Restart simulator

![](../assets/Pictures/100000010000003600000035FFB1D3C8.png)	Documentation (contains a link to the latest manual)

![](../assets/Pictures/100000010000003200000035D1E633FE.png)	Light/Dark mode

##### Upload menu

![](../assets/Pictures/10000001000000360000002D2C104C73.png)	Upload a model file (.bin)

![](../assets/Pictures/10000001000000390000002C6F32ABA7.png)	Upload a radio backup (.bin)

![](../assets/Pictures/100000010000003300000033269A6153.png)	Upload an audio pack (.zip)

![](../assets/Pictures/100000010000003900000036C03A3D20.png)	Upload a Lua plugin (.zip)

![](../assets/Pictures/10000001000000340000002F288030D0.png)	Upload a CSV translations file (.csv)

![](../assets/Pictures/10000001000000350000002A143579D1.png)	Upload a JSON telemetry file (.json)

![](../assets/Pictures/100000010000002A00000027369727BA.png)	Start a macro (.zip)

##### Download menu

![](../assets/Pictures/10000001000000300000002E352FCCAB.png)	Save the current model file (.bin)

![](../assets/Pictures/100000010000003500000035D957DFFB.png)	Edit the current model

![](../assets/Pictures/100000010000003500000035D957DFFB.png)	Edit the current model file (JSON)

![](../assets/Pictures/1000000100000039000000328FCEB87D.png)	Save all screenshots (browse to target folder, save as .png)

![](../assets/Pictures/10000001000000380000002DE9810693.png)	Save a radio backup (.zip)

![](../assets/Pictures/10000001000000350000002C51A893DF.png)	Save telemetry settings (.json)

##### Controls Panel

![](../assets/Pictures/10000001000007560000040AEB2D971E.png)

The ‘Controls’ panel mimics the hardware controls on the chosen radio.

###### Gimbals

The sticks can be operated by dragging them with a mouse. During debugging it is useful to constrain or restrict the stick movement.

![](../assets/icon-sim-center.png)	Will auto-center the stick in one or both axes.

![](../assets/icon-sim-vertical.png)	Will constrain the stick to vertical movement only.

![](../assets/icon-sim-horizontal.png)	Will constrain the stick to horizontal movement only.

###### Momentary switches and buttons

![](../assets/icon-sim-locked.png)	Will latch momentary switches and buttons so that they can toggle between on and off but will remain in the selected on or off state for debugging.
