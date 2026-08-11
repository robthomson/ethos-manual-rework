---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# De nieuwste bootloader of een ander component vinden

Ethos-firmwarereleases publiceren een `components.json`-bestand met de
actuele versie van elk component per zender. Dit is handig om te
controleren of een bepaalde versie van bootloader/firmware/audio/
systeembestanden werkelijk actueel is voordat u deze flasht.

!!! note "Schermafbeeldingen in voorbereiding"
    Voor deze pagina zijn nog geen schermafbeeldingen uit de simulator
    beschikbaar — zie [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

1. Download `components.json` van de nieuwste Ethos-release.
2. Open het bestand in een teksteditor (VS Code, Notepad, enz.).
3. Zoek het gedeelte voor uw zender op — bijvoorbeeld `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (Dit is een momentopname als voorbeeld — controleer voor werkelijke
   versienummers altijd het bestand van de *actuele* release.)

4. Lees de versie af van het component dat u nodig hebt — in het
   bovenstaande voorbeeld is de nieuwste bootloader voor de X20-familie
   `1.4.15`.

Zie [Bestandsbeheer](../system-setup/file-manager.md#top-level-folders) voor
de juiste locatie om het gedownloade firmwarebestand te plaatsen, en [USB-
verbindingsmodi](../getting-started/usb-connection-modes.md#bootloader-mode)
om de zender in bootloader-modus te zetten voor het flashen — of gebruik
[Ethos Suite](../ethos-suite/index.md), dat het controleren van versies en
het flashen automatisch afhandelt.
