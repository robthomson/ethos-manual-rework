---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Een FBUS-systeem configureren

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (voorheen
F.Port2) brengt besturing en telemetrie op één lijn samen, waardoor meerdere
FBUS-apparaten één in serie doorgekoppelde verbinding kunnen delen met volledige
draadloze configuratie. In deze uitleg worden twee Xact-servo's aangesloten op de
rolroerkanalen (1 en 5) van het [eenvoudige
vliegtuigvoorbeeld](../tutorials/basic-fixed-wing.md).

!!! note "Schermafbeeldingen volgen nog"
    Deze pagina heeft nog geen schermafbeeldingen uit de simulator — zie
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md).

## 1. Download de nieuwste firmware

FBUS vereist actuele firmware op zowel de ontvanger als de apparaten — Xact-servo's
hebben bijvoorbeeld v2.0.1 of nieuwer nodig. Haal de betreffende updates op via de
[downloadpagina van FrSky](https://www.frsky-rc.com/download/).

## 2. Flash de firmware

Kopieer de firmwarebestanden naar `Firmware/` op de SD card/eMMC. Ga in
[Bestandsbeheer](../system-setup/file-manager.md), sluit de servo aan op de
S.Port-connector van de zender (witte/gele draad naar de uitsparing toe),
selecteer het firmwarebestand en kies **Flash External Device**.

## 3 / 5. Physical ID's configureren

Beide servo's hebben standaard Physical ID `0C` hex / Application ID `6800` hex —
ze zullen met elkaar in conflict komen op de gedeelde bus tenzij er één wordt
gewijzigd. Er zijn twee manieren, afhankelijk van het type ontvanger:

**Via de S.Port-connector van de zender** (elke ontvanger):

1. Sluit servo 1 aan, ga naar **Device Config → XAct** en stel **Module** in op
   **S.Port connector**. Laat Physical ID `0C`/Application ID `6800` en kanaal
   `CH1` op de standaardwaarden staan en kies daarna **Save to flash**.
2. Sluit vervolgens servo 2 aan, in hetzelfde menu. Wijzig **Physical ID** naar
   `0D` hex en **Application ID** naar `6801` hex (zie de [tabel met Physical
   ID's](../model-setup/telemetry.md#how-frsky-telemetry-works) voor de vrije
   posities), stel **Channel** in op `CH5` en kies **Save to flash**.

**Direct via de ontvanger** (bijv. TD-R18 Tandem, waarbij beide servo's
gelijktijdig zijn aangesloten — zie [stap 4](#4-configure-the-receiver-for-fbus)):

1. Met alleen servo 1 aangesloten (bijv. op Pin1 van de ontvanger): **Device
   Config → XAct**, **Module** → **Internal module**. Bevestig de
   standaardwaarden (`0C`/`6800`/`CH1`) en kies **Save to flash**.
2. Met alleen servo 2 aangesloten (Pin5), in hetzelfde menu (Device Config
   communiceert met één servo tegelijk) — wijzig naar `0D`/`6801`/`CH5` en kies
   **Save to flash**. Selecteer daarna Device Config opnieuw om te controleren of
   de wijziging is doorgevoerd.

## 4. De ontvanger configureren voor FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [RF System](../model-setup/rf-system.md) → de knop van de ontvanger
→ **Options** → stel **Telemetry Port** in op **FBUS**. Xact-servo's worden
vervolgens in serie op die poort doorgekoppeld; omdat elke servo maar één
connector heeft, splitst een F.Port2-multikanaalverdeler (FP2CH4/6/8) de
verbinding naar meerdere servo's.

**TD-R18 Tandem**: RF System → de knop van de ontvanger → **Options** → stel
afzonderlijke pinnen (bijv. **Pin1**, **Pin5**) in op **FBUS** — op deze manier
kunnen zoveel pinnen als nodig worden toegewezen, waardoor verdelers volledig
overbodig worden; elke aan FBUS toegewezen pin voert hetzelfde FBUS-signaal.

## 5. Controleer de FBUS-besturing van de servo's

Sluit servo 1 aan op Pin1 en servo 2 op Pin5 (de rolroerkanalen van het
vliegtuigvoorbeeld), schakel de voeding in en controleer of kanalen 1 en 5 de
juiste servo's bewegen.

## 6. Controleer de FBUS-telemetrie

Verwijder met beide servo's aangesloten alle bestaande `SRV`-sensoren onder
[Telemetrie](../model-setup/telemetry.md) en zoek ze opnieuw op. Elke servo meldt
4 sensoren: stroom, spanning, temperatuur en status (`OK` bij normale werking).

## 7. Later configuratiewijzigingen doorvoeren

Zodra een model volledig is ingebouwd, is het niet praktisch om één servo te
isoleren om die via Device Config opnieuw te configureren. Doe in plaats daarvan
het volgende: ga naar Telemetrie, zoek een sensor die bij de betreffende servo
hoort (bijv. `SRV1 curr`) en kies **Configure** — hiermee opent u direct de
configuratie van die servo. Kies na elke wijziging **Save to flash**.

!!! warning
    Wijzig de Physical ID of Application ID niet per ongeluk vanuit dit scherm —
    die zorgen ervoor dat elke servo op de gedeelde bus adresseerbaar blijft.
