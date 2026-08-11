---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migrazione

Passaggio di una radio dai vecchi strumenti di aggiornamento per PC separati a Ethos Suite, per la prima volta.

1. **Verificare che Ethos sia ≥ 1.1.4** — la versione minima in grado di eseguire il flash del nuovo bootloader compatibile con Suite (formato FRSK) direttamente dal [File Manager](../system-setup/file-manager.md). Se necessario, aggiorna prima manualmente alla 1.1.4.
2. **Eseguire il backup della SD card/eMMC** — copiarne l'intero contenuto in una cartella sul PC.
3. **Scaricare l'ultimo bootloader** dalle [release di ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases) e decomprimerlo. Ogni release pubblica un file `components.json` che elenca la versione corrente di ogni componente — vedi [Guida pratica: trovare l'ultimo bootloader](../how-to/find-latest-bootloader.md) per sapere come leggerlo.
4. Individua la radio nella voce `targets` di quel file per conoscere l'esatta versione del bootloader da utilizzare e cerca il file corrispondente tra gli asset di quella release.
5. Avvia la radio in [modalità bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) (tieni premuto `ENT`, quindi accendi) e collegala via USB.
6. Copia il file del bootloader sulla SD card/eMMC (normalmente nella cartella `Firmware/`), quindi espelli le unità e scollega il cavo.
7. Avvia normalmente la radio, vai in **System → File Manager**, tocca il file `bootloader.frsk` appena copiato e seleziona **Flash bootloader**.
8. Scarica e installa Ethos Suite — [Funzionamento](operation.md) illustra da qui in avanti l'aggiornamento di firmware e file e le restanti funzionalità di Suite.
9. Se Ethos Suite non lo fa automaticamente, potrebbe essere necessario rinominare la cartella `bitmaps/user` presente sulla SD card/eMMC in `bitmaps/models` (è qui che risiedono le bitmap utente dei modelli).
