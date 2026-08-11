---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Devices

![Devices](../assets/system-devices.png)

In het menu **Device config** genoemd — gereedschappen voor het configureren van randapparatuur die via S.Port/FBUS is aangesloten: sensors, ontvangers, de "gas suite", servo's, VTX en ESC. **DIY sensors** verschijnt automatisch zodra er een DIY-sensor wordt gedetecteerd. Raadpleeg de handleiding van het betreffende apparaat voor alle details; deze pagina behandelt wat ze gemeenschappelijk hebben.

!!! note
    Dit heeft niets te maken met het kiezen van de RF-module (intern of extern) waarmee een *model* zendt — dat is een instelling per model, beschreven in [RF System](../model-setup/rf-system.md).

Device Config is uitbreidbaar: zowel gebruikers als FrSky kunnen hier pagina's toevoegen via Lua.

## Sensor-ID's opnieuw toewijzen

In de Device config-schermen van Ethos kunt u de **Physical ID** en **Application ID** van een apparaat op de S.Port direct wijzigen. Heeft u meerdere apparaten met dezelfde functie, sluit ze dan **één voor één** aan: zoek elk apparaat op via [Telemetry → Discover new sensors](../model-setup/telemetry.md), wijzig hier in Device config de Physical ID en Application ID, ga vervolgens terug en zoek het apparaat opnieuw op onder het nieuwe ID.

## Voorbeeld: ontvangers

![Modulekeuze](../assets/system-devices-module-choice.png)

Gestabiliseerde ontvangers van FrSky kunnen hier worden geconfigureerd zodra het bijbehorende Lua-instelscript is geïnstalleerd (met één klik, vanuit de Lua Library van Ethos Suite). Er zijn twee configuratiepaden, afhankelijk van de generatie van de ontvanger:

- **Stabilizer config** — nieuwere ontvangers met "Advanced stabilization" (gain-regeling op kanaal 13). Er zijn twee onafhankelijke stabilisatiegroepen beschikbaar: groep 1 omvat de kanalen 1–6, groep 2 de kanalen 7–11 — schakel groep 2 uit als u de pinnen 7–11 niet voor stabilisatie gebruikt. Een 6-assige kalibratie is ingebouwd en moet eenmalig worden uitgevoerd op een nieuwe ontvanger, en opnieuw na elke firmware-upgrade naar v3.0.x (volgend op een fabrieksreset). Bij de kalibratie van elke groep is de oude "self-check"-stap vervangen door onafhankelijke kalibratie van de horizontale stand van het model, het kanaalmidden en de kanaaleindpunten, en kan elk kanaal afzonderlijk worden geactiveerd/gedeactiveerd. Configuraties (niet de kalibratiegegevens) kunnen naar een pc worden opgeslagen en daarvan worden teruggezet.
- **SxR** — oudere ontvangers, waaronder legacy-modellen en Archer/Archer Pro, plus ontvangers zoals de SR10 Pro die (ondanks de naam "SRx") Gain op kanaal 9 hebben in plaats van op kanaal 13.

  ![Huidig apparaat](../assets/system-devices-current.png)

!!! warning "Na het updaten naar ontvangerfirmware v3.0.x"
    Voer een fabrieksreset uit (te vinden onder receiver Options in RF setup), bind daarna opnieuw en configureer de ontvanger volledig opnieuw — met name de Stab-functies en de 6-assige kalibratie. Dit is vereist door de nieuwe functie in v3.0.x voor het opslaan van failsafe-gegevens; controleer de failsafe-functie daarna zorgvuldig.

FrSky North America publiceert een uitgebreide handleiding voor het instellen van gestabiliseerde ontvangers, en er is een instructievideo van FrSky Team Pilot Juan Sanchez Garcia die dezelfde stof behandelt.

## Configureren via de S.Port-connector van de zender

S.Port- en FBUS-apparaten kunnen ook direct via de S.Port-connector aan de bovenzijde van de zender worden geconfigureerd, zonder tussenkomst van een gebonden ontvanger.

1. Sluit het apparaat aan op de S.Port-connector van de zender (witte/gele draad naar de zijde met de uitsparing).
2. Ga naar **System → Device config**, scroll naar het apparaat (bijvoorbeeld een FAS40 ADV stroomsensor) en druk op `ENT`.
3. Zet op de configuratiepagina **Module** op **S.Port connector**.
4. Voer uw wijzigingen door — Physical ID en Application ID moeten elk uniek zijn — scroll vervolgens naar beneden en tik op **Save to flash**.

Dit geldt zowel voor FBUS-apparaten (zie ook [How-To: Een FBUS-systeem configureren](../how-to/fbus-setup.md)) als voor gewone S.Port-apparaten zoals een variometer.
