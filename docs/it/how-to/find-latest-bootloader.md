---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trovare il bootloader più recente o altri componenti

Le release del firmware Ethos pubblicano un file `components.json` che elenca
la versione corrente di ogni componente per ciascuna radio, utile per verificare
se una determinata versione di bootloader/firmware/file audio/file di sistema sia
effettivamente aggiornata prima di eseguirne il flash.

!!! note "Screenshot in arrivo"
    Questa pagina non dispone ancora di screenshot del simulatore — vedi [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

1. Scarica il file `components.json` dall'ultima release di Ethos.
2. Aprilo con un editor di testo (VS Code, Blocco note, ecc.).
3. Individua la sezione relativa alla tua radio — ad esempio `X20`:

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

   (Esempio indicativo — controlla sempre il file della release *corrente* per
   i numeri di versione reali.)

4. Leggi la versione del componente che ti interessa — nell'esempio
   precedente, il bootloader più recente per la famiglia X20 è `1.4.15`.

Consulta [Gestione file](../system-setup/file-manager.md#top-level-folders) per
sapere dove collocare il file del firmware scaricato, e [Modalità di connessione
USB](../getting-started/usb-connection-modes.md#bootloader-mode) per
mettere la radio in modalità Bootloader ed eseguirne il flash — oppure usa [Ethos
Suite](../ethos-suite/index.md), che gestisce automaticamente il controllo delle versioni
e il flashing.
