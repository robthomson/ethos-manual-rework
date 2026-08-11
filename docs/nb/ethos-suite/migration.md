---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migrering

Flytte en sender fra de eldre, separate PC-oppdateringsverktøyene til Ethos Suite,
for første gang.

1. **Bekreft Ethos ≥ 1.1.4** — minimumsversjonen som kan flashe den nye
   Suite-kompatible bootloaderen (FRSK-format) direkte fra [File
   Manager](../system-setup/file-manager.md). Oppdater manuelt til 1.1.4
   først om nødvendig.
2. **Ta sikkerhetskopi av SD card/eMMC** — kopier hele innholdet til en mappe på en
   PC.
3. **Last ned den nyeste bootloaderen** fra
   [ETHOS-Feedback-Community releases](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   og pakk den ut. Hver utgivelse publiserer en `components.json` som lister opp
   gjeldende versjon for hver komponent — se [Praktisk guide: Finn den nyeste
   bootloaderen](../how-to/find-latest-bootloader.md) for hvordan den leses.
4. Finn senderen under dens `targets`-oppføring i denne filen for å se hvilken
   bootloader-versjon som skal brukes, og finn den tilsvarende filen blant
   filene i den utgivelsen.
5. Start senderen i [bootloader-modus](../getting-started/usb-connection-modes.md#bootloader-mode)
   (hold `ENT` inne, og slå deretter på) og koble til via USB.
6. Kopier bootloader-filen til SD card/eMMC (normalt til
   `Firmware/`), løs ut deretter diskene og koble fra.
7. Start senderen normalt, gå til **System → File Manager**, trykk på
   `bootloader.frsk`-filen du nettopp kopierte, og velg **Flash bootloader**.
8. Last ned og installer Ethos Suite — [Bruk](operation.md) dekker
   oppdatering av firmware/filer og resten av funksjonene i Suite herfra.
9. Hvis Ethos Suite ikke gjør det automatisk, kan det være nødvendig å gi mappen
   `bitmaps/user` på SD card/eMMC nytt navn til `bitmaps/models` (det er her
   brukerens modellbilder ligger).
