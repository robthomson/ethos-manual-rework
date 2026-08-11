---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Informatie

![Systeeminformatie](../assets/system-info.png)

Details over de firmware van het systeem, type gimbal, informatie over de interne/externe RF-module,
gegevens van de gebonden ontvanger, bedrijfstijd van de zender, foutlogboeken en fabrieksreset.

## Zenderinformatie

- **Serienummer** — het serienummer van de zender.
- **Firmware** — Ethos-versie en zendertype (bijv. X20).
- **Firmwareversie** — buildvariant, bijv. FCC, LBT of Flex.
- **Datum** — datum/tijd waarop de firmware is gebouwd.
- **Beschikbaar RAM** — vrij systeem-RAM, nuttig om een zich misdragend
  Lua-script op te sporen; ook beschikbaar als System-[bron](../getting-started/user-interface-and-navigation.md#choosing-a-source)
  zodat het in een widget kan worden weergegeven.
- **Sticks** — versie van de geïnstalleerde Hall-sensoren van de gimbal (of "ADC" bij analoge
  gimbals).
- **Interne module** — hardware- en firmwareversies van de interne RF-module.
- **Ontvanger** — de gegevens van de momenteel gebonden ontvanger, weergegeven na de
  interne module. Als een redundante ontvanger dezelfde slot deelt als de
  hoofdontvanger, wisselen de twee elkaar af op het display (bijv. een Archer SR10 Pro
  die samen met zijn redundante R9MM-OTA onder "Receiver1" wordt weergegeven).
- **Externe module** — hardware-/firmwaregegevens van een geplaatste externe FrSky
  RF-module die het ACCESS-protocol gebruikt. Multi-protocol-modules
  worden hier niet weergegeven.

![X20 Pro-informatie](../assets/system-info-x20pro.png)

## Bedrijfstijd van de zender

![Bedrijfstijd van de zender](../assets/system-info-radio-runtime.png)

Houdt de totale gebruiksduur van de zender bij; **Reset** zet deze op nul.

## Fouten

![Fouten](../assets/system-info-errors.png)

Een rode driehoek in de bovenbalk van de hoofdweergave betekent dat Ethos een fout heeft gelogd,
die hier in detail wordt weergegeven. Mogelijke oorzaken:

- **Lua-scriptfouten** — een probleem in een actief Lua-script.
- **RAM-backupfout** — een model dat te groot is voor het RAM voor modelbackups. Ethos
  heeft dit uitgebreid van 4K naar 32K, dus dit komt nu niet snel meer voor, maar als het
  gebeurt is het een ernstige fout: het model laadt langzamer vanaf de SD card
  in plaats van vanuit het backup-RAM wanneer de [noodmodus](../getting-started/emergency-mode.md)
  wordt geactiveerd.
- **Een nightly firmware-build gebruiken** — een herinnering dat nightly builds
  niet bedoeld zijn om mee te vliegen.

**Reset** wist de gelogde fouten — handig tijdens een Lua-debugsessie.

## Fabrieksreset

![Fabrieksreset](../assets/system-info-factory-reset.png)

Zet de zender volledig op het toestel zelf terug naar de fabrieksinstellingen — er is geen
pc-verbinding nodig.

![Bevestiging fabrieksreset](../assets/system-info-factory-reset-confirm.png)

!!! danger
    Bij bevestiging worden **alle** modellen, logbestanden, schermafbeeldingen, documenten,
    scripts, bitmaps en zenderinstellingen gewist. Een voortgangsbalk toont het wissen,
    waarna alle drives worden ontkoppeld en de zender opnieuw opstart.

De Info-pagina van de X20 Pro/R/RS toont de overeenkomstige informatie voor die
zenderfamilie.
