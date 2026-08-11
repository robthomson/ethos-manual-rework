---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Noodmodus

De noodmodus is de reactie van Ethos op een onverwachte storing op laag niveau, zoals een watchdog-reset. De watchdog is een timer die continu opnieuw wordt gestart door verschillende delen van het systeem; als iets verhindert dat hij opnieuw wordt gestart, verloopt hij en forceert hij een hardwarereset. De noodmodus start de zender daarna zo snel mogelijk opnieuw op, waarbij alle normale opstartcontroles worden overgeslagen zodat de besturing van het model met minimale vertraging wordt teruggegeven. De SD card/eMMC wordt in deze modus helemaal niet benaderd.

Alleen de essentiële functies die nodig zijn om het model te blijven besturen zijn beschikbaar — geen enkele van de functies op hoger niveau. Het scherm blijft leeg, op de woorden **EMERGENCY MODE** na, begeleid door een terugkerende pieptoon van 300 ms elke 3 seconden; spraakmeldingen, Lua-scripts, logging en telemetrie stoppen allemaal. Als dit in de lucht gebeurt, land dan zo snel mogelijk.

De meest voorkomende oorzaak is een defect van de SD card.

## Noodmodus testen

Er kan een **System tool** worden toegevoegd om de noodmodus opzettelijk te activeren voor testdoeleinden, zodat u deze niet voor het eerst tijdens de vlucht hoeft te ontdekken. Wanneer u op het pictogram Emergency Test tikt, wordt om bevestiging gevraagd, waarna de zender in de noodmodus wordt gezet, precies zoals bij een echte storing.
