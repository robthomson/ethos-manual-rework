---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Finn den nyeste bootloaderen eller andre komponenter

Ethos-firmwareutgivelser publiserer en `components.json`-fil som lister opp
gjeldende versjon av hver komponent per sender. Denne er nyttig for å bekrefte
om en gitt versjon av bootloader/firmware/lyd/systemfiler faktisk er
oppdatert før den flashes.

!!! note "Skjermbilder kommer"
    Denne siden har ennå ikke skjermbilder fra simulatoren — se [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

1. Last ned `components.json` fra den nyeste Ethos-utgivelsen.
2. Åpne filen i en tekstredigerer (VS Code, Notepad e.l.).
3. Finn seksjonen for din sender — f.eks. `X20`:

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

   (Et øyeblikksbilde som eksempel — sjekk alltid filen i den *gjeldende*
   utgivelsen for reelle versjonsnumre.)

4. Les av versjonen for den komponenten du trenger — i eksempelet ovenfor er
   den nyeste bootloaderen for X20-familien `1.4.15`.

Se [Filbehandler](../system-setup/file-manager.md#top-level-folders) for
hvor den nedlastede firmwarefilen skal plasseres, og [USB-tilkoblingsmoduser](../getting-started/usb-connection-modes.md#bootloader-mode) for
hvordan du setter senderen i bootloader-modus for å flashe den — eller bruk [Ethos
Suite](../ethos-suite/index.md), som håndterer versjonskontroll og
flashing automatisk.
