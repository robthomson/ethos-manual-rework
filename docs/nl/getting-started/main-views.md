---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Hoofdweergaven

## Startscherm

![Startscherm](../assets/mainview.png)

Het startscherm is wat u ziet wanneer er geen menu geopend is — een stapel van maximaal
**acht** displayschermen die u zelf configureert (zie
[Displays](../displays/index.md)), waartussen u wisselt met de `PAGE`-toets
of met een veegbeweging op het touchscreen. Een nieuw aangemaakt model begint met slechts één scherm
met een modelafbeelding, drie timerwidgets en de trim-/potentiometerindicatoren;
alles daarop is vanaf dat punt door de gebruiker configureerbaar.

Schermen delen normaal gesproken de hieronder beschreven boven- en onderbalk, maar
een scherm kan ook op volledig scherm worden ingesteld, waarbij beide worden verborgen.

## De bovenbalk

De bovenbalk toont links de modelnaam (plus de actieve vluchtmodus,
indien er een geconfigureerd is) en rechts een rij statuspictogrammen:

- Datalogging actief
- Trainerstatus (master of slave, al naargelang)
- RSSI — 2,4GHz-verbinding
- RSSI — 900MHz-verbinding (indien er een dualband-/longrange-module is gemonteerd)
- Luidsprekervolume
- Batterijstatus van de zender

Door het luidspreker- of batterijpictogram aan te raken gaat u direct naar het bijbehorende
instellingenpaneel [Algemeen](../system-setup/general.md) (audio) of
[Batterij](../system-setup/battery.md).

### Foutwaarschuwing

Er verschijnt een rode driehoek in de bovenbalk zodra Ethos een fout detecteert —
een fout in een Lua-script, een RAM-backupfout of het gebruik van een nightly/onstabiele
firmwarebuild zijn de meest voorkomende oorzaken. De details achter de waarschuwing vindt u
altijd in **System → Info**, op dezelfde pagina als de bedrijfstijd van de zender en de
[foutlogboeken](../system-setup/information.md).

## De onderbalk

![Onderbalk](../assets/bottombar.png)

Onderaan bevinden zich vier tabbladen voor de hoofdsecties — **Start**,
**Modelinstellingen**, **Schermen configureren**, **Systeeminstellingen** — met de
systeemklok aan de rechterzijde (raak deze aan om direct naar
[Datum & tijd](../system-setup/date-and-time.md) te gaan).

## Het widgetgebied

Het middengedeelte van elk scherm is gevuld met **widgets**: modelafbeelding, timers,
telemetriewaarden, trim-/potentiometerbalken en meer, allemaal door u geplaatst en
geconfigureerd. Zie [Displays](../displays/index.md) voor het toevoegen, verplaatsen en
configureren van widgets, en [Extra displays](../displays/additional-displays.md)
voor het toevoegen van meer dan het standaard enkele scherm.
