---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![X20 Pro Hardware-Prüfung](../assets/system-hardware-check-x20pro.png)

Unterschiede gegenüber der X20S-Basis, auf die sich dieses Handbuch bezieht —
diese gelten für die **X20 Pro** und weitgehend auch für die **X20 Pro AW**
sowie die **X20R/RS**-Familie.

- **Speicher** — standardmäßig interner 8-GB-eMMC-Speicher, SD card optional — siehe
  [Allgemein → Speicherort](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **Zusätzliche Trimmungen** — ergänzt die Trimmschalter **T5** und **T6** — siehe
  [Trimmung](../model-setup/trims.md#trim-settings).
- **Zusätzliche Schalter** — zwei rastende Drucktaster, **K** und **L**,
  an den hinteren Schultern, zusätzlich die Schalterpositionen **M**/**N**, sofern
  verdrahtet (typischerweise Schalter am Knüppelende) — siehe [Hardware →
  Schalter](../system-setup/hardware.md#switches-settings).
- **Zusätzliche Potentiometer** — **Ext1**/**Ext2**, typischerweise mit 3-Achs-Gimbals
  verwendet — siehe [Hardware → Potentiometer/Schieberegler](../system-setup/hardware.md#potssliders-settings).
  Dadurch verschiebt sich der Index im [ADC-Wertinspektor](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 liegen zwischen Pot2 und den Schiebereglern.
- **Haptisches Feedback** — die **X20 Pro AW** und die **X20RS** werden mit MC20R-Gimbals
  mit integrierten haptischen Stick-Shaker-Motoren ausgeliefert; eine **X20 Pro** oder
  **X20R** kann dies durch eine Nachrüstung mit MC20R-Gimbals erhalten, freigeschaltet
  unter [Hardware → Haptische Gimbal-Upgrades aktivieren](../system-setup/hardware.md#radio-specific-hardware-options).
  Nach der Aktivierung bietet [Haptische Motoren auswählen](../model-setup/special-functions.md#actions)
  die Optionen Standard, Alle Motoren, Linker Steuerknüppel oder Rechter Steuerknüppel.
- **Drehgeber** — die X20 Pro AW und die X20R/RS verwenden einen empfindlicheren
  Drehgeber; eine Option **Halbe Schritte** unter [Hardware → Encoder-Option](../system-setup/hardware.md#radio-specific-hardware-options)
  dämpft dies ab.
- **Internes HF-Modul** — die X20 Pro/R/RS verwenden das Modul **TD-ISRM Pro**
  (LoRa-fähig, mit Tandem-Dualband- und TD-Pro-Modi zusätzlich zu ACCESS/ACCST D16)
  statt des TD-ISRM-Moduls in X18/X20/X20S/X20HD — siehe [RF System](../model-setup/rf-system.md).
