---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![X20 Pro Hardware-Prüfung](../assets/system-hardware-check-x20pro.png)

Unterschiede gegenüber dem X20S, auf den sich dieses Handbuch bezieht —
sie gelten für den **X20 Pro** und weitgehend auch für den **X20 Pro AW**
sowie die **X20R/RS**-Familie.

- **Speicher** — standardmäßig interner 8-GB-eMMC-Speicher, SD card optional — siehe
  [Allgemein → Speicherort](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **Zusätzliche Trimmungen** — zusätzliche Trimmschalter **T5** und **T6** — siehe
  [Trimmungen](../model-setup/trims.md#trim-settings).
- **Zusätzliche Schalter** — zwei rastende Drucktaster **K** und **L**
  an den hinteren Schultern sowie die Schalterpositionen **M**/**N**, sofern
  verdrahtet (üblicherweise Schalter am Knüppelende) — siehe [Hardware →
  Schalter](../system-setup/hardware.md#switches-settings).
- **Zusätzliche Potentiometer** — **Ext1**/**Ext2**, üblicherweise in Verbindung mit
  3-Achs-Gimbals genutzt — siehe [Hardware → Potis/Schieberegler](../system-setup/hardware.md#potssliders-settings).
  Dadurch verschiebt sich die Reihenfolge im [ADC-Wert-Inspektor](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 liegen zwischen Pot2 und den Schiebereglern.
- **Haptische Rückmeldung** — der **X20 Pro AW** und der **X20RS** werden mit MC20R-Gimbals
  mit eingebauten haptischen Stick-Shaker-Motoren ausgeliefert; ein **X20 Pro** oder
  **X20R** lässt sich mit MC20R-Gimbals nachrüsten und erhält damit dieselbe Funktion.
  Freigeschaltet wird sie unter [Hardware → Haptische Gimbal-Upgrades aktivieren](../system-setup/hardware.md#radio-specific-hardware-options).
  Nach der Aktivierung bietet [Haptische Motoren auswählen](../model-setup/special-functions.md#actions)
  die Optionen Standard, Alle Motoren, Linker Knüppel oder Rechter Knüppel.
- **Drehgeber** — der X20 Pro AW und die X20R/RS verwenden einen empfindlicheren
  Drehgeber; die Option **Halbe Schritte** unter [Hardware → Encoder-Option](../system-setup/hardware.md#radio-specific-hardware-options)
  verringert diese Empfindlichkeit.
- **Internes HF-Modul** — der X20 Pro/R/RS verwenden das Modul **TD-ISRM Pro**
  (LoRa-fähig, mit Tandem-Dualband- und TD-Pro-Modi zusätzlich zu ACCESS/ACCST D16)
  anstelle des TD-ISRM-Moduls in X18/X20/X20S/X20HD — siehe [HF-System](../model-setup/rf-system.md).
