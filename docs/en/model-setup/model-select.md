# **Model** **s****elect**

![](../assets/model-icon-modelselect.png)

The model select option is accessed by selecting ‘Model select’ from the Model menu. It is used to select the current model, add a new model, or to clone or delete it.

## Managing model folders

Ethos allows you to create your own model folders to categorize and group your models. Typical model folder names may be Airplane, Glider, Heli, Quad, Warbird, Boat, Car, Template, Archive etc.

![](../assets/model-modelselect-folders.png)

Until you have created and organized your folders, Ethos will automatically create the ‘Uncategorized’ folder. This happens when you upgrade to Ethos version 1.1.0 alpha 17 or later, or when you copy a model from the net or a friend into the \\Models folder on the SD or eMMC card.  Ethos will automatically delete the ‘Uncategorized’ folder when no longer needed.

![](../assets/model-modelselect-model-create.png)

![](../assets/model-modelselect-create-airplane-folder.png)

To create your first folder, tap on the ‘+’ to the right of the ‘Uncategorized’ label, or long press the Page Up/Down key.

Enter the name into the ‘Create folder’ dialog, and tap OK. The folder names can be up to 15 characters. Repeat for your other categories. Note that these folders appear as subfolders beneath the \\Models folder on the SD card or eMMC.

Model category folders are sorted alphabetically, but the ‘Uncategorized’ folder will always appear last in the list.

![](../assets/model-modelselect-folder-options.png)

Tapping on a folder name will bring up a dialog allowing the folder to be renamed or deleted. If there were models in the folder being deleted, Ethos will automatically place them in the ‘Uncategorized’ folder.

Moving models to another folder

![](../assets/model-modelselect-folder-change-select.png)

To move a model to another folder, tap on the model’s icon, then select ‘Change folder’ from the dialog.

![](../assets/model-modelselect-folder-change-glider.png)

Tap on the folder to move it to.

## Adding a new model

![](../assets/model-modelselect-folder-airplane-select.png)

To create a new model, select the model category you wish to create the model under, then tap on the \[+\] icon to create a new model or to receive a model from another Ethos radio via Bluetooth.

![](../assets/model-modelselect-model-create.png)

Tap on ‘Create model’ to start the new model wizard. (You may need to create your model categories first, see above.)

![](../assets/model-modelselect-model-wizard-airplane.png)

Choose the type of model you wish to create, and follow the prompts.

There are wizards for:

- Airplane
- Glider
- Helicopter
- Multirotor
- Other

The wizards assist you with the basic setup for the given type of model. Note that model names can be up to 15 characters.

![](../assets/model-modelselect-model-wizard-rx.png)

The wizards include optionally setting up additional pre-set mixes for FrSky stabilized receivers, such as gain and stabilization mode.

Stabilized receivers

The FrSky stabilized receivers require a specific channel order, namely AETR. Therefore the ‘Channel order’ in the Sticks menu should be left at the default AETR setting and the ‘First four channels fixed’ option should be On, to ensure that the channel order created by the wizard will suit the receiver.

The new model wizards assign channels from right to left, so for a simple model with 2 ailerons, 1 elevator, 1 rudder and 1 motor the channel order will be:

Ch1	Aileron1	(Right Aileron)

Ch2	Elevators

Ch3	Throttle

Ch4	Rudders

Ch5	Aileron2	(Left Aileron)

With the above aileron assignments Aileron Differential will have a positive value for normal differential with more aileron upward movement than downward.

Please note that currently the FrSky receiver manuals use the opposite convention of channel assignment from left to right. This would require

Ch1	Aileron1	(Left Aileron)

Ch5	Aileron2	(Right Aileron)

In this case Aileron Differential will have a negative value for differential.

For consistency it is recommended to use the Ethos convention. All stabilization functions will work correctly because the compensation directions are configured during the stabilization setup.

If you decide to follow the receiver manual convention, the easiest way to achieve this is to use the ‘Swap channels’ feature in the Outputs to swap the aileron channels after creating the model with the wizard. This maintains the positive differential in the aileron mixer.

![](../assets/model-modelselect-model-wizard-engine.png)

For an Airplane type of model, the next page is Engine, which allows selection of the desired number of engine channels (if any).

![](../assets/model-modelselect-model-wizard-ail-and-flaps.png)

For an Airplane type of model, the number of aileron and flap channels are selected next.

![](../assets/model-modelselect-model-wizard-tail.png)

For an Airplane type of model, the tail configuration is chosen between Traditional cross tail, V-tail or no tail (e.g. on a delta or flying wing).

Delta wings

An Elevon setup can be achieved by creating a new Airplane model with 2 Ailerons and No Tail surfaces, which will result in Elevon mixing being automatically built. The default mix weights are 50% to give a total 100% if both aileron and elevator are applied simultaneously.

Alternatively, when using a stabilized receiver, the delta mixing can be performed by the receiver. In the wizard, for this situation you should select 1 aileron and 1 elevator, because the elevon mixing will be done in the receiver. Please refer to the stabilized receiver manual for details.

For a delta wing model having both aileron and elevator surfaces, allow the wizard to complete as though the model has a tail. It will configure the needed aileron and elevator channels, with or without a rudder as required.

![](../assets/model-modelselect-model-wizard-ele-and-rudder.png)

For an Airplane type of model, having chosen for example a traditional cross tail, the number of elevator and rudder channels may be configured.

![](../assets/model-modelselect-model-wizard-ch-reassignment.png)

After setting up the channel options, the step shown above allows you to reassign the model functions to different channels. The wizard obeys the ‘Channel order’ configured in Sticks, but this screen allows you to reassign the channels, bearing in mind that FrSky stabilized receivers require the stabilized channels to be in a specific order. Please refer to the receiver’s instructions for details.

![](../assets/model-modelselect-model-wizard-name.png)

In the last step the model name can be defined, and a model image linked.

![](../assets/model-modelselect-model-wizard-ultimate.png)

The new model has been created.

![](../assets/model-modelselect-model-airplane-category.png)

The created model will be appear in the user-defined model category folder that was active when the wizard was started, and will be sorted alphabetically within each group.

Please also refer to the [Basic Fixed Wing Airplane example](../tutorials/basic-fixed-wing.md) in the Programming Tutorials section for a worked example.

## Receiving a model from another Ethos radio

![](../assets/model-modelselect-folder-airplane-select.png)

To receive a model, select the model category you wish to create the model under, then tap on the \[+\] icon.

![](../assets/model-modelselect-model-receive.png)

Tap on ‘Receive model’ to initiate the process to receive a model from another Ethos radio via Bluetooth.

![](../assets/Pictures/1000000000000320000001E0A34D638D.png)

Your radio will go into waiting mode, and also display its local Bluetooth address to enable identification of the correct address on the sending radio.

![](../assets/Pictures/1000000000000320000001E0D6F5A932.png)

On the sending radio, tap on the model icon and select ‘Send model’ to initiate the transfer.

![](../assets/Pictures/1000000000000320000001E0964706D2.png)

The receiving radio will announce the model file about to be received for confirmation. Tap on Yes to receive the model.

## Selecting a model

![](../assets/model-icon-modelselect.png)

Tap on ‘Model select’ to bring up a list of your models.

![](../assets/model-modelselect-folders.png)

Please note that after an Ethos version upgrade, ETHOS converts the models individually when they are selected with the model selection screen. There is no need to select each model after an update because the conversion can take place at a later date when they are selected, even with a later release of Ethos. There is no noticeable delay in the conversion process when a model is selected. When the conversion takes place, the Last Modification date at the bottom of the model selection screen will change to the current date. If no conversion is needed the date only changes if you make an edit to the model.

Quick select

Touch\_long or Enter\_long on a model icon will switch to that model immediately.

Model management menu

Tap on a model to highlight it, then tap on it again to bring up the model management menu.

![](../assets/model-modelselect-folder-change-select.png)

Options in the model management menu:

- Tap on ‘Set current model’ to make the highlighted model the current model.
- You can Clone the model, which will duplicate the model. Please note that when you clone a model Ethos gives the clone a new receiver number. If you give it the old receiver number it will work, no need to rebind.
- You change the model’s folder.
- You can send or receive the model to or from another radio.
- Alternatively, you can Delete the model. Note that the Delete option only appears if the selected model is not the current model.
