---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Informasjon

![Systeminformasjon](../assets/system-info.png)

Detaljer om systemets firmware, type gimbal, informasjon om intern/ekstern RF-modul,
informasjon om bundet mottaker, senderens driftstid, feillogger og fabrikkgjenoppretting.

## Informasjon om senderen

- **Serienummer** — senderens serienummer.
- **Firmware** — Ethos-versjon og sendertype (f.eks. X20).
- **Firmware-versjon** — byggvariant, f.eks. FCC, LBT eller Flex.
- **Dato** — dato/klokkeslett for firmware-bygget.
- **Tilgjengelig RAM** — ledig system-RAM, nyttig for å oppdage et Lua-skript
  som ikke oppfører seg som det skal; er også tilgjengelig som en System-[kilde](../getting-started/user-interface-and-navigation.md#choosing-a-source)
  slik at den kan vises i en widget.
- **Spaker** — installert versjon av gimbalens Hall-sensorer (eller «ADC» for analoge
  gimbaler).
- **Intern modul** — maskinvare- og firmwareversjoner for den interne
  RF-modulen.
- **Mottaker** — detaljer om mottakeren som er bundet nå, vist etter den
  interne modulen. Hvis en redundant mottaker deler samme plass som
  hovedmottakeren, veksler de to på skjermen (f.eks. en Archer SR10 Pro
  vist sammen med sin redundante R9MM-OTA under «Receiver1»).
- **Ekstern modul** — maskinvare-/firmwaredetaljer for en montert ekstern
  FrSky RF-modul som bruker ACCESS-protokollen. Multi-protocol-moduler
  vises ikke her.

![X20 Pro-informasjon](../assets/system-info-x20pro.png)

## Senderens driftstid

![Senderens driftstid](../assets/system-info-radio-runtime.png)

Holder oversikt over total brukstid for senderen; **Reset** nullstiller den.

## Feil

![Feil](../assets/system-info-errors.png)

En rød trekant i den øverste linjen i hovedvisningen betyr at Ethos har logget en feil,
som vises i detalj her. Mulige årsaker:

- **Feil i Lua-skript** — et problem i et Lua-skript som kjører.
- **RAM-sikkerhetskopifeil** — en modell som er for stor for RAM-området for
  modellsikkerhetskopi. Ethos har utvidet dette fra 4K til 32K, så det er nå lite
  sannsynlig at grensen nås, men hvis den gjør det, er det en betydelig feil:
  modellen lastes saktere fra SD card i stedet for sikkerhetskopi-RAM hvis
  [nødmodus](../getting-started/emergency-mode.md) utløses.
- **Kjøring av et nightly firmware-bygg** — en påminnelse om at nightly-bygg
  ikke er ment for flyging.

**Reset** sletter loggede feil — praktisk midt i en Lua-feilsøkingsøkt.

## Fabrikkgjenoppretting

![Fabrikkgjenoppretting](../assets/system-info-factory-reset.png)

Gjenoppretter senderen til fabrikkinnstillinger helt og holdent på enheten — ingen
PC-tilkobling er nødvendig.

![Bekreftelse av fabrikkgjenoppretting](../assets/system-info-factory-reset-confirm.png)

!!! danger
    Ved bekreftelse slettes **alle** modeller, logger, skjermbilder, dokumenter,
    skript, bitmaps og senderinnstillinger. En fremdriftsindikator viser slettingen,
    og deretter demonteres alle diskene og senderen starter på nytt.

Info-siden på X20 Pro/R/RS viser tilsvarende informasjon for den
senderfamilien.
