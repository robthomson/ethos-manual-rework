# Glasses

![Glasses](../assets/model-glasses.png)

New in Ethos 26.1: connects and configures **ActiveLook** smart glasses,
giving the wearer a heads-up display of real-time flight data, telemetry,
and FPV video overlaid on their view. Two tabs: **Base config** (pairing)
and **Display** (what the HUD actually shows).

## Base config

![Base config](../assets/model-glasses-base-config.png)

- **State** — enables/disables the Glasses function.
- **Local name** / **Local address** — the radio's own Bluetooth name (as
  it appears to the glasses when pairing — defaults to the radio model,
  editable) and address.
- **Device** — tap **Search** to put the radio into Bluetooth search mode:

  ![Search for devices](../assets/model-glasses-base-config-search.png)

  Select the matching address from the found-devices list:

  ![Connected](../assets/model-glasses-base-config-connected.png)
  ![Connected OK](../assets/model-glasses-base-config-connected-ok.png)

  Once linked, the glasses' Bluetooth address shows on the Device line.
  Tap the device to **Disconnect**:

  ![Disconnect](../assets/model-glasses-base-config-disconnect-select.png)

## Display

![Display tab](../assets/model-glasses-display.png)

Tap **Change layout** to pick one of 6 HUD layouts:

![Choose layout](../assets/model-glasses-display-change-layout-select.png)
![Layout options](../assets/model-glasses-display-layouts-select.png)

Each layout exposes a fixed number of widget slots — tap one to configure
it. Only **Value** widgets are available for glasses display:

![Layout selected](../assets/model-glasses-display-layouts-select-5.png)
![Layout ready](../assets/model-glasses-display-layout-5.png)
![Select a widget](../assets/model-glasses-display-widget-1-select.png)
![Value widget options](../assets/model-glasses-display-widget-1-value-select.png)

For example, configuring widget 1 to show Timer 1 and widget 2 to show
minimum VFR:

![Widget 1: Timer 1](../assets/model-glasses-display-widget-1-edit-timer1.png)
![Widget 1 showing Timer 1](../assets/model-glasses-display-widget-1-timer1.png)
![Widget 2: VFR Min](../assets/model-glasses-display-widget-2-vfr.png)
