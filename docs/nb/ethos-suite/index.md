---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite er det tilhørende Windows-/Mac-programmet for å administrere en sender
som kjører Ethos, tilkoblet via USB.

![Radio-fanen i Ethos Suite](../assets/ethos-suite-radio-tab.png)

Når tilkoblingen er opprettet, kan Ethos Suite:

1. Lese senderens type, ID og installerte versjoner — firmware,
   bootloader, intern RF-modul, filer i flash-minnet og filer på SD-kort/eMMC.
2. Veksle senderen mellom bootloader-modus og kjørende Ethos, og tilbake igjen.
3. Sammenligne installerte versjoner med gjeldende versjoner og oppdatere automatisk —
   bare utdaterte komponenter, alt uansett status, eller komponenter
   enkeltvis.
4. Sikkerhetskopiere modeller til disk via **Model Manager**, eller gjenopprette en tidligere
   sikkerhetskopi (nødvendig fordi modellfiler ikke er bakoverkompatible mellom
   firmwareversjoner).
5. Laste ned firmware fra FrSkys nedlastingsside via **Download
   center**, og bruke senderen som mellomledd for å flashe en modul, sensor,
   servo eller mottaker direkte.
6. Konvertere bilde- og lydfiler til Ethos' egne formater.
7. Tilby **Lua-utviklingsverktøy** — API-dokumentasjon, demoskript og en
   feilsøkingsterminal.
8. Flashe senderens bootloader i DFU-modus (tilkobling med senderen avslått),
   uavhengig av om senderens egen firmware fortsatt fungerer.
9. Reparere internlageret på X18/S, TW Lite, XE og X20 Pro/R/RS-sendere
   via **Repair Tool**, dersom NAND ikke kan leses eller innstillinger ikke lagres.
10. Løse ut senderens USB-disker på en trygg måte.
11. Varsle ved oppstart når en oppdatering av Suite selv er tilgjengelig (installeres
    ved avslutning).

## Tilkoblingsmoduser

I tillegg til verktøyene sine opererer Suite i tre ulike tilstander for
tilkobling til senderen:

- **Sender i bootloader-modus** — fanen **Radio** kontrollerer/oppdaterer
  firmware og filene i flash-minnet/på SD-kortet/eMMC; **Model Manager** sikkerhetskopierer
  eller gjenoppretter senderen.
- **Sender i Ethos-modus** — Suite bruker senderen som mellomledd (via verktøyene
  **FRSK Flasher**/Download center) for å flashe den interne modulen,
  eller en tilkoblet sensor/servo/mottaker, direkte.
- **Sender i DFU-modus** — tilkobling med senderen avslått, brukes av **DFU
  Flasher** for å flashe selve bootloaderen, f.eks. når ødelagt firmware
  hindrer senderen fra å starte opp normalt.

Se [Migrering](migration.md) for å ta i bruk Ethos Suite for første gang
med en eksisterende sender, og [Bruk](operation.md) for selve
Suite-grensesnittet.
