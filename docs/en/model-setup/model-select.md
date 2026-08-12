# Model Select

![Model wizard - airplane](../assets/model-modelselect-model-wizard-airplane.png)

Creates, selects, clones, and deletes models, and manages the user-defined
category folders they're organized into.

## Managing model folders

![Model folders](../assets/model-modelselect-folders.png)

Ethos lets you group models into your own folders — typically things like
Airplane, Glider, Heli, Quad, Warbird, Boat, Car, Template, or Archive.
Until you create any, models live in an automatic **Uncategorized**
folder (created on upgrading to Ethos 1.1.0 alpha 17+, or when a model
file is copied into `\Models` from elsewhere); Ethos deletes it again once
it's empty.

To create a folder, tap **+** next to "Uncategorized" (or long-press
`PAGE` up/down), name it (up to 15 characters), and confirm. Folders sort
alphabetically, with **Uncategorized** always last, and correspond
directly to subfolders under `\Models` on the SD card/eMMC. Tapping a
folder name opens rename/delete — deleting a folder moves any models in it
back to Uncategorized.

![Change folder](../assets/model-modelselect-folder-change-select.png)

To move a model, tap its icon, choose **Change folder**, then tap the
destination:

![Choose folder](../assets/model-modelselect-folder-airplane-select.png)

## Adding a new model

![Create model](../assets/model-modelselect-model-create.png)

Select the category to create the model in, tap **+**, then **Create
model** to launch the wizard (create the category first if it doesn't
exist yet). Wizards are available for **Airplane**, **Glider**,
**Helicopter**, **Multirotor**, and **Other**; each walks through the
basic setup for that airframe type, including optional pre-set mixes for
FrSky stabilized receivers (gain, stabilization mode). Model names can be
up to 15 characters.

### Stabilized receivers and channel order

![Wizard: airplane](../assets/model-modelselect-model-wizard-airplane.png)

FrSky stabilized receivers require channel order **AETR** specifically —
leave [Sticks → Channel order](../system-setup/controls.md) at its AETR
default with **First four channels fixed** on, so the wizard's output
matches what the receiver expects.

As of Ethos 26.1, the wizard assigns channels starting from the left and
alternating from the outside in — matching FrSky's own stabilized-receiver
documentation (earlier versions assigned right-to-left instead, which
needed a manual channel swap to line up; that workaround is no longer
necessary). For 2 ailerons + 1 elevator + 1 rudder + 1 motor, that's:

| Ch | Function |
|---|---|
| 1 | Aileron 1 (left aileron) |
| 2 | Elevator |
| 3 | Throttle |
| 4 | Rudder |
| 5 | Aileron 2 (right aileron) |

!!! note "Upgrading a model built on Ethos 1.6.x"
    Existing models keep working after the upgrade — Ethos never changes
    [Channels](outputs.md) output assignments, so no rewiring is needed.
    What it *may* do, the first time an affected model is selected, is
    reorder aileron-related mixes (the aileron mix itself, Ail→Flaps,
    Ail→Rud, V-tail Rudders) so aileron differential keeps working
    correctly under the new left-to-right convention, appending "Left"/
    "Right" to the affected channel names. See [Converting 1.6.x Models to
    26.1](../how-to/converting-1.6-models.md) for the three specific
    scenarios (default channel usage, swapped channels, inverted-mix
    channels) and what, if anything, needs manual attention in each.

### Wizard steps

![Wizard: tail type](../assets/model-modelselect-model-wizard-tail.png)
![Wizard: aileron/flap count](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Wizard: elevator/rudder count](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Wizard: engine](../assets/model-modelselect-model-wizard-engine.png)
![Wizard: channel reassignment](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Wizard: name](../assets/model-modelselect-model-wizard-name.png)
![Wizard: receiver](../assets/model-modelselect-model-wizard-rx.png)

For an **Airplane**, after tail type/surface counts the wizard covers
engine channel count, then aileron/flap channel count.

**Tail configuration** is a choice of traditional cross tail, V-tail, or
no tail (delta/flying wing):

- **Delta/flying wing** — creating an Airplane model with 2 ailerons and
  no tail surfaces automatically builds elevon mixing, with default 50%
  weights so full simultaneous aileron + elevator commands still total
  100%.
- **Delta with a stabilized receiver doing the mixing** — instead select
  1 aileron and 1 elevator; elevon mixing happens in the receiver, per its
  own manual.
- **Delta with dedicated aileron and elevator surfaces** — let the wizard
  run as if the model has a tail; it configures the needed aileron and
  elevator channels (with or without a rudder), and no elevon mixing is
  created.

The **channel reassignment** step lets you override the wizard's default
mapping, bearing in mind that stabilized receivers need their channels in
a specific order (check the receiver's own instructions). The final step
sets the model name and links a picture.

The finished model lands in whichever category folder was active when the
wizard started, sorted alphabetically within it. See [Basic Fixed-Wing
Example](../tutorials/basic-fixed-wing.md) for a full worked walkthrough.

## Receiving a model from another Ethos radio

![Receive model](../assets/model-modelselect-model-receive.png)

Select the destination category, tap **+**, then **Receive model** — the
radio waits and shows its Bluetooth address so the sender can find it. On
the sending radio, tap the model and choose **Send model**; the receiving
radio confirms the incoming filename before accepting.

## Selecting a model

Tap **Model select** for the model list.

!!! note "Model conversion after an Ethos upgrade"
    Ethos converts each model individually the first time it's *selected*
    after a version upgrade, not all at once on upgrade — there's no
    noticeable delay, and it's safe to do at any later point, even under a
    still-newer Ethos release. The **Last Modification** date at the
    bottom of the selection screen updates when a conversion happens (or
    when you edit the model — otherwise it's unchanged).

**Quick select** — a long touch or long `ENT` on a model icon switches to
it immediately.

**Model management menu** — tap a model to highlight it, tap again for the
menu:

- **Set current model**
- **Clone** — duplicates the model. A clone gets a new receiver number
  automatically; if you reassign the original's receiver number instead,
  it works with no rebinding needed.
- **Change folder**
- **Send**/**Receive** — to or from another radio, as above.
- **Delete** — only offered for a model that isn't the current one.
