---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite è l'applicazione companion per Windows/Mac dedicata alla gestione di una radio
che esegue Ethos, collegata tramite USB.

!!! note "Screenshot in attesa"
    Ethos Suite è un'applicazione separata per PC, non la radio stessa, quindi
    questa sezione non utilizza gli screenshot acquisiti dal simulatore come il resto
    del manuale — vedi [Pipeline degli
    screenshot](../contributing/screenshot-pipeline.md).

Una volta connessa, Ethos Suite può:

1. Leggere il tipo di radio, l'ID e le versioni installate — firmware,
   bootloader, modulo RF interno, file della memoria flash e file della
   SD card/eMMC.
2. Passare la radio dalla modalità bootloader all'esecuzione di Ethos, e viceversa.
3. Confrontare le versioni installate con quelle correnti e aggiornarle automaticamente —
   solo i componenti obsoleti, tutti i componenti indipendentemente dallo stato, oppure i
   singoli componenti.
4. Eseguire il backup dei modelli su disco tramite il **Model Manager**, oppure ripristinare un
   backup precedente (necessario poiché i file dei modelli non sono retrocompatibili tra le
   versioni del firmware).
5. Scaricare qualsiasi firmware dal sito di download di FrSky tramite la scheda **Download
   center**, e utilizzare la radio come proxy per eseguire il flash direttamente di un modulo,
   un sensore, un servo o un ricevitore.
6. Convertire immagini e file audio nei formati nativi di Ethos.
7. Fornire gli **strumenti di sviluppo Lua** — documentazione API, script dimostrativi e un
   terminale di debug.
8. Eseguire il flash del bootloader della radio in modalità DFU (una connessione a radio spenta),
   indipendentemente dal fatto che il firmware della radio sia ancora funzionante.
9. Riparare la memoria interna delle radio X18/S, TW Lite, XE e X20 Pro/R/RS
   tramite il **Repair Tool**, se la NAND non può essere letta o le impostazioni non vengono salvate.
10. Espellere in modo corretto le unità USB della radio.
11. Segnalare all'avvio la disponibilità di un aggiornamento della Suite stessa (che viene
    installato all'uscita).

## Modalità di connessione

Oltre ai suoi strumenti, Suite opera in tre distinti stati di connessione della
radio:

- **Radio in modalità Bootloader** — la scheda **Radio** verifica/aggiorna il
  firmware e i file della memoria flash/scheda SD/eMMC; il **Model Manager** esegue il backup
  o il ripristino della radio.
- **Radio in modalità Ethos** — Suite utilizza la radio come proxy (tramite gli
  strumenti **FRSK Flasher**/Download center) per eseguire direttamente il flash del modulo interno,
  o di qualsiasi sensore/servo/ricevitore collegato.
- **Radio in modalità DFU** — connessione a radio spenta, utilizzata dal **DFU
  Flasher** per eseguire il flash del bootloader stesso, ad esempio quando una corruzione del firmware
  impedisce alla radio di accendersi normalmente.

Consulta [Migrazione](migration.md) per trasferire per la prima volta una radio esistente a Ethos
Suite, e [Funzionamento](operation.md) per l'interfaccia della Suite
vera e propria.
