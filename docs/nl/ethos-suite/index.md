---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite is de bijbehorende Windows/Mac-toepassing voor het beheren van een
zender met Ethos, verbonden via USB.

!!! note "Screenshots volgen nog"
    Ethos Suite is een afzonderlijke pc-toepassing en niet de zender zelf, waardoor
    dit hoofdstuk geen gebruikmaakt van de in de simulator vastgelegde screenshots
    die in de rest van de handleiding worden gebruikt — zie [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

Zodra de verbinding tot stand is gebracht, kan Ethos Suite:

1. Het type, de ID en de geïnstalleerde versies van de zender uitlezen — firmware,
   bootloader, interne RF-module, bestanden in het flashgeheugen en bestanden op
   de SD card/eMMC.
2. De zender omschakelen tussen bootloader-modus en het uitvoeren van Ethos, en terug.
3. Geïnstalleerde versies vergelijken met de actuele versies en automatisch bijwerken —
   uitsluitend verouderde onderdelen, alles ongeacht de versie, of onderdelen
   afzonderlijk.
4. Modellen naar schijf back-uppen via **Model Manager**, of een eerdere
   back-up terugzetten (nodig omdat modelbestanden niet achterwaarts compatibel zijn
   tussen firmwareversies).
5. Willekeurige firmware downloaden van de FrSky-downloadsite via het **Download
   center**, en de zender als proxy gebruiken om een module, sensor,
   servo of ontvanger direct te flashen.
6. Afbeeldingen en audiobestanden omzetten naar de eigen formaten van Ethos.
7. **Lua development tools** aanbieden — API-documentatie, demoscripts en een
   debugterminal.
8. De bootloader van de zender flashen in DFU-modus (een verbinding met de zender
   uitgeschakeld), onafhankelijk van de vraag of de eigen firmware van de zender
   nog werkt.
9. De interne opslag van X18/S-, TW Lite-, XE- en X20 Pro/R/RS-zenders repareren
   via de **Repair Tool**, wanneer NAND niet kan worden gelezen of instellingen niet
   worden opgeslagen.
10. De USB-schijven van de zender netjes uitwerpen.
11. Bij het opstarten melden dat er een update voor Suite zelf beschikbaar is
    (die bij het afsluiten wordt geïnstalleerd).

## Verbindingsmodi

Naast de Tools werkt Suite in drie afzonderlijke verbindingstoestanden van de
zender:

- **Zender in bootloader-modus** — het tabblad **Radio** controleert/werkt de
  firmware en de bestanden in flash/op de SD card/eMMC bij; **Model Manager** maakt
  een back-up van de zender of zet deze terug.
- **Zender in Ethos-modus** — Suite gebruikt de zender als proxy (via de tools
  **FRSK Flasher**/Download center) om de interne module, of een aangesloten
  sensor/servo/ontvanger, direct te flashen.
- **Zender in DFU-modus** — verbinding met de zender uitgeschakeld, gebruikt door de
  **DFU Flasher** om de bootloader zelf te flashen, bijvoorbeeld wanneer beschadigde
  firmware verhindert dat de zender normaal opstart.

Zie [Migratie](migration.md) voor het voor de eerste keer overzetten van een
bestaande zender naar Ethos Suite, en [Gebruik](operation.md) voor de
Suite-interface zelf.
