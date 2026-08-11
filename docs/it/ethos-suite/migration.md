---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migrazione

Passaggio di una radio dai vecchi strumenti di aggiornamento per PC separati a Ethos Suite, per la prima volta.

1. **Verificare Ethos ≥ 1.1.4** — la versione minima in grado di flashare direttamente il nuovo bootloader compatibile con Suite (formato FRSK) dal [File Manager](../system-setup/file-manager.md). Se necessario, aggiornare prima manualmente alla 1.1.4.
2. **Eseguire il backup della SD card/eMMC** — copiarne l'intero contenuto in una cartella su un PC.
3. **Scaricare il bootloader più recente** dalle [release di ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases) e decomprimerlo. Ogni release pubblica un file `components.json` che elenca la versione corrente di ogni componente — vedere [Guida pratica: trovare il bootloader più recente](../how-to/find-latest-bootloader.md) per la sua lettura.
4. Individuare la radio nella voce `targets` di quel file per conoscere l'esatta versione del bootloader da utilizzare, quindi cercare il file corrispondente tra gli asset di quella release.
5. Avviare la radio in [modalità bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) (tenere premuto `ENT`, poi accendere) e collegarla via USB.
6. Copiare il file del bootloader sulla SD card/eMMC (normalmente nella cartella `Firmware/`), quindi espellere le unità e scollegare il cavo.
7. Avviare normalmente la radio, andare in **System → File Manager**, toccare il file `bootloader.frsk` appena copiato e selezionare **Flash bootloader**.
8. Scaricare e installare Ethos Suite — [Funzionamento](operation.md) illustra da qui in avanti l'aggiornamento di firmware/file e le restanti funzionalità di Suite.
9. Se Ethos Suite non lo fa automaticamente, potrebbe essere necessario rinominare la cartella `bitmaps/user` presente sulla SD card/eMMC in `bitmaps/models` (è qui che risiedono le bitmap dei modelli dell'utente).
