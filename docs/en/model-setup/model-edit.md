# Edit model

![](../assets/model-icon-editmodel.png)

The ‘Edit model’ option is used to edit the basic parameters for the model as set up by the wizard.

![](../assets/model-editmodel.png)

## Name, Picture

The model can be renamed, or the picture assigned or changed. When browsing for a picture a preview thumbnail is shown to facilitate locating the correct image.

## Model type

![](../assets/model-edit-modeltype.png)

Changing the model type will cause all mixes to be reset.

## Channel assignments

Changing the tail type, or heli swash plate will cause all mixes to be reset. On the other channels the number of assigned channels can be changed or unassigned.

## Analogs filter

![](../assets/model-edit-analog-filter.png)

![](../assets/model-edit-analog-filter-select.png)

There is a global analog to digital converter filter setting on the Hardware page under [Analogs Filter](../system-setup/hardware.md), which may improve jitter around stick centre. This model specific setting can be used to override the global setting.

## Function switches

![](../assets/model-edit-fn-switches.png)

The six function switches are available wherever 'Active condition' parameters are found. Please note that they cannot be used as a source like normal switches can.

![](../assets/model-edit-fn-switches-select.png)

Configuration

They may be configured as follows:

6-Pos with OFF

Pressing any function switch will latch that switch ON. However, pressing a switch that is already ON a second time will turn it off, leaving all six function switches OFF.

6-POS

Pressing any function switch will latch that switch ON until a different function switch is pressed to latch the newly pressed switch ON.

2 x 3-Pos

Breaks the 6 function switches into two groups of 3. Each group can have one switch ON.

6 x 2-Pos

Breaks the 6 function switches into 6 latching switches. Each switch can be ON or OFF.

Momentary

Breaks the 6 function switches into 6 momentary switches. Each switch is ON while depressed.

Persistent

If enabled, this will cause the function switch to be in the same state when the radio is turned on or the model is reloaded.

## SPort connector

![](../assets/model-edit-sport.png)

The 5V pin on the SPort connector may be controlled on a model by model basis, to power for example an external receiver in a trainer application.

## Model runtime

The model runtime timer keeps track of the total time that the model has run.

## Reset all mixes

![](../assets/model-edit-model-reset_all_mixes.png)

Executing 'Reset all mixes' will reset all the mixes.
