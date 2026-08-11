---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migratie

Een zender voor het eerst overzetten van de oudere, afzonderlijke pc-updatetools
naar Ethos Suite.

1. **Controleer Ethos ≥ 1.1.4** — de minimale versie die de nieuwe
   Suite-compatibele bootloader (FRSK-formaat) rechtstreeks vanuit de
   [File Manager](../system-setup/file-manager.md) kan flashen. Werk indien
   nodig eerst handmatig bij naar 1.1.4.
2. **Maak een back-up van de SD card/eMMC** — kopieer de volledige inhoud naar
   een map op een pc.
3. **Download de nieuwste bootloader** van
   [ETHOS-Feedback-Community releases](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   en pak het bestand uit. Elke release publiceert een `components.json` met de
   huidige versie van elk component — zie [Handleiding: de nieuwste bootloader
   vinden](../how-to/find-latest-bootloader.md) voor het lezen daarvan.
4. Zoek de zender op onder het bijbehorende `targets`-item in dat bestand voor
   de exacte bootloaderversie die gebruikt moet worden, en zoek het
   overeenkomstige bestand op bij de assets van die release.
5. Start de zender op in [bootloader-modus](../getting-started/usb-connection-modes.md#bootloader-mode)
   (houd `ENT` ingedrukt en zet dan de zender aan) en sluit deze via USB aan.
6. Kopieer het bootloaderbestand naar de SD card/eMMC (normaal gesproken naar
   `Firmware/`), werp daarna de schijven uit en koppel de zender los.
7. Start de zender normaal op, ga naar **System → File Manager**, tik op het
   net gekopieerde bestand `bootloader.frsk` en kies **Flash bootloader**.
8. Download en installeer Ethos Suite — [Gebruik](operation.md) behandelt vanaf
   hier het bijwerken van firmware/bestanden en de overige functies van Suite.
9. Als Ethos Suite dit niet automatisch doet, moet de map `bitmaps/user` op de
   SD card/eMMC mogelijk worden hernoemd naar `bitmaps/models` (hier staan de
   modelbitmaps van de gebruiker).
