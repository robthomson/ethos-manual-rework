---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Eerste instelling van de zender

De eenmalige instelling die u doorloopt voordat u een model programmeert. De
[Tutorials](index.md) die hierna volgen, gaan er allemaal van uit dat dit eerst
is gedaan.

!!! note
    Deze tutorials zijn geen strikt kookboek — ze veronderstellen basiskennis
    van RC-terminologie en enige ervaring met het navigeren door de
    Ethos-menu's. Als iets hier onduidelijk is, lees dan eerst
    [Gebruikersinterface en
    navigatie](../getting-started/user-interface-and-navigation.md).

## Stap 1. Laad de zender- en vluchtaccu's op

Laad de zenderaccu op volgens de richtlijnen die bij de zender zijn geleverd, en
de vluchtaccu's met een lader die geschikt is voor het betreffende accutype —
wees bijzonder voorzichtig met lithiumpakketten.

## Stap 2. Kalibreer de hardware

Controleer of de [hardwarekalibratie](../system-setup/hardware.md#analogs-calibration)
is uitgevoerd (deze start automatisch bij de eerste keer opstarten), zodat de
zender het exacte middelpunt en de eindposities van elke gimbal, potentiometer
en schuifregelaar kent. Voer de kalibratie opnieuw uit via **Systeem → Hardware**
telkens wanneer een gimbal, potentiometer of schuifregelaar wordt vervangen.

## Stap 3. Voer de systeeminstellingen van de zender uit

[Systeeminstellingen](../system-setup/index.md) omvat alles wat voor elk model
gelijk is, in tegenstelling tot de per model geldende instellingen van
[Modelinstellingen](../model-setup/index.md). De meeste standaardwaarden zijn om
te beginnen prima, maar controleer:

- **[Datum en tijd](../system-setup/date-and-time.md)** — correct instellen.
- **[Audio → Keuze van
  stemmen](../system-setup/general.md#audio-settings)** — stel de spraakmeldingen
  in, inclusief eventuele eigen audiobestanden.
- **[Besturing (Sticks)](../system-setup/controls.md)**:
  - **Stickmodus** — Mode 1 (gas/rolroeren rechts, hoogteroer/richtingsroer
    links) of Mode 2 (gas/richtingsroer links, rolroeren/hoogteroer rechts — de
    standaard in Ethos).

    !!! warning
        Als een model voor de ene stickmodus is geconfigureerd terwijl de zender
        op de andere staat ingesteld, kan een elektromotor op het moment dat de
        ontvanger wordt ingeschakeld direct gaan draaien.

  - **Kanaalvolgorde** — Ethos gebruikt standaard **AETR** (Aileron, Elevator,
    Throttle, Rudder); de Spektrum/JR-conventie is **TAER**, Futaba/Hitec
    gebruikt **AETR**. Hiermee wordt bepaald in welke volgorde de stickingangen
    worden toegewezen wanneer een nieuw model wordt aangemaakt — modellen kunnen
    later nog individueel worden aangepast.

    !!! note "FrSky-gestabiliseerde ontvangers"
        Deze vereisen specifiek **AETR**. Met meer dan één stuurvlak per functie
        (bijv. 2 rolroeren) groepeert de wizard deze normaal gesproken (wat
        **AAETR** oplevert) — maar SRx-ontvangers verwachten in plaats daarvan
        **AETRA**/**AETRAE**, dus schakel **[Eerste vier kanalen
        vast](../system-setup/controls.md#first-four-channels-fixed)** in onder
        Sticks om de eerste vier kanalen ongeacht de rest in strikte
        AETR-volgorde te houden.

- **[Accu](../system-setup/battery.md)** — stel **Hoofdspanning**, **Lage
  spanning** en **Weergegeven spanningsbereik** in overeenkomstig de
  daadwerkelijke accu van de zender.
- **[Eigenaars-registratie-ID](../model-setup/rf-system.md#owner-registration-id)**
  — wordt gebruikt door ACCESS-ontvangers en wordt tussen zenders gedeeld voor
  Smart Share. Dit wordt geconfigureerd onder Modelinstellingen, maar functioneert
  in de praktijk als een systeembrede instelling, omdat elk nieuw model deze
  gebruikt (indien nodig kan het per ontvanger tijdens de registratie nog worden
  gewijzigd).

!!! note "Eenheden"
    Ethos heeft geen globale omschakeling tussen metrisch en imperiaal — de
    [eenheden van telemetriesensoren](../model-setup/telemetry.md#editing-a-sensor)
    worden afzonderlijk per sensor ingesteld.
