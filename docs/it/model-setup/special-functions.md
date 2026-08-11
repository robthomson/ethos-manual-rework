---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Funzioni speciali

![Menu funzioni speciali](../assets/model-sf-menu.png)

Le funzioni speciali attivano un'azione — riproduzione audio, cattura di
uno screenshot, scrittura dei log, feedback haptic e altro ancora —
quando una condizione diventa vera. Ne sono supportate fino a 100;
nessuna è presente per impostazione predefinita. Aggiungine una con
**+**; tocca una funzione esistente per **Modifica**/**Sposta**/
**Copia-incolla**/**Clona**/**Elimina**.

![Aggiungi funzione speciale](../assets/model-sf-add.png)
![Sposta](../assets/model-sf-move.png)

## Campi comuni a tutte le azioni

- **Stato** — abilita/disabilita la funzione senza eliminarla.
- **Condizione attiva** — **Sempre attiva**, oppure subordinata a
  posizioni di interruttori/interruttori funzione/interruttori
  logici/trim o a fasi di volo. Premi a lungo `ENT` su un interruttore e
  seleziona **Negativo** per invertirlo (ad esempio `SG-up` diventa
  `!SG-up`, attivo ogni volta che SG *non* è in alto).
- **Globale** — aggiunge questa funzione a **tutti** i modelli, esistenti
  e futuri. Se un modello dispone già di una funzione locale configurata
  in modo identico, l'opzione Globale la aggiunge come voce ulteriore;
  disattivando nuovamente Globale la funzione viene rimossa da ogni
  modello tranne quello attualmente selezionato. Le funzioni globali
  risiedono in `radio.bin`, quelle locali nel file del modello.

## Azioni {: #actions }

**Reset** — azzera i **Dati di volo** (telemetria + timer), **Tutti i
timer** o **Tutta la telemetria**.

![Reset](../assets/model-sf-reset.png)

**Screenshot** — salva uno screenshot nella cartella `screenshots/` sulla
SD card/eMMC.

![Screenshot](../assets/model-sf-screenshot.png)

**Imposta failsafe** — registra le posizioni correnti dei canali come
failsafe, tramite il **Modulo** RF interno o esterno.

![Imposta failsafe](../assets/model-sf-set-failsafe.png)

**Riproduci audio** — l'azione più completa, che supporta un'intera
sequenza:

![Riproduci audio](../assets/model-sf-play-audio.png)

- **Voce** — quale delle massimo 3 voci configurate utilizzare (vedi
  [Generale](../system-setup/general.md#audio-settings)).
- **Ripetizione** — riproduzione singola oppure ripetuta a un intervallo
  configurabile (fino a 10 minuti).
- **Ignora all'avvio** — impedisce l'attivazione di questa funzione
  durante l'avvio.
- **Sequenza** — fino a 100 passi, ciascuno dei quali può essere:

  - **Riproduci file** — riproduce un file audio selezionato.

    ![Riproduci file](../assets/model-sf-play-audio-add-play-file.png)

  - **Riproduci valore** — pronuncia il valore di una sorgente: analogici,
    interruttori, interruttori logici, trim, canali, giroscopio, orologio
    di sistema, trainer, timer o telemetria.

    ![Riproduci valore](../assets/model-sf-play-audio-add-play-value.png)

  - **Attendi durata** — una pausa fissa, fino a 10 minuti.
  - **Attendi condizione** — sospende la sequenza fino al verificarsi di
    una condizione.

  ![Aggiungi riga alla sequenza](../assets/model-sf-play-audio-add-line.png)
  ![Tipo di riga della sequenza](../assets/model-sf-play-audio-add-line-type.png)

  Ad esempio: riprodurre `vfrlow.wav` quando l'interruttore logico
  `VFRlow` diventa attivo, quindi pronunciare il valore minimo VFR
  registrato —

  ![Riproduci valore dopo il file](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — oppure sospendere una sequenza finché l'interruttore SH non viene
  portato in basso, prima di proseguire:

  ![Sequenza con condizione di attesa](../assets/model-sf-play-audio-add-sequence.png)

  Tocca una qualsiasi riga della sequenza per modificarla, aggiungerne
  una, riordinarla o eliminarla:

  ![Gestione della sequenza](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptic** — feedback vibrazionale:

![Haptic](../assets/model-sf-haptic.png)

- **Schema** — singola, doppia, tripla, quintupla o molto breve.

  ![Schema haptic](../assets/model-sf-haptic-pattern.png)

- **Intensità** — 1–10 (predefinita 5).
- **Ripetizione** — una sola volta oppure a un intervallo prestabilito.
- **Seleziona motori haptic** — sulle radio dotate di motori haptic negli
  stick (X20 Pro AW, X20RS, oppure una X20 Pro/X20R aggiornata con gimbal
  MC20R — vedi
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Predefinito** (haptic interno), **Tutti i motori**, **Stick sinistro**
  o **Stick destro**.

  ![Haptic su X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Scrivi log** — scrive log in formato `.csv` nella cartella `Logs/` sulla
SD card/eMMC, con marcatura temporale dall'RTC (essenziale per
distinguere successivamente le diverse sessioni di volo):

![Scrivi log](../assets/model-sf-write-logs.png)

- **Intervallo di scrittura** — 100–500 ms.
- **Stick/Potenziometri/Slider**, **Interruttori**, **Interruttori
  logici**, **Canali** — categorie di registrazione attivabili in modo
  indipendente.

  **Visualizzazione dei log**: apri un file di log da `/Logs` nel Gestore
  file. Scegli quali canali tracciare (RSSI è selezionato per
  impostazione predefinita); sposta la visualizzazione con l'encoder
  rotativo o con uno swipe e ingrandisci ruotando l'encoder mentre tieni
  premuto `PAGE`. `DISP` sposta il focus sul primo pulsante della colonna
  di destra.

**Riproduci testo** (solo X20 Pro) — sintesi vocale direttamente sulla
radio anziché un file pre-registrato:

![Riproduci testo](../assets/model-sf-x20pro-play-text.png)

- **Testo** — la stringa da pronunciare. Il testo TUTTO MAIUSCOLO viene
  compitato lettera per lettera (ad esempio "OFF" → "O-F-F"); in
  minuscolo viene pronunciato come parola ("off").
- **Ripetizione**, **Ignora all'avvio** — come sopra.

**Vai alla schermata** — commuta il display su una schermata scelta, ad
esempio passando al registro dei dati di volo di un ricevitore alla
pressione di un pulsante:

![Vai alla schermata](../assets/model-sf-go-to-screen.png)
![Opzioni schermata](../assets/model-sf-go-to-screen-options.png)

**Blocca touchscreen** — blocca il touchscreen contro comandi involontari
(raggiungibile anche direttamente tenendo premuti insieme `ENT` + `PAGE`
per 1 s dalla schermata home):

![Blocca touchscreen](../assets/model-sf-lock-touchscreen.png)

**Carica modello** — carica un **Modello** specificato quando viene
attivata, con un'eventuale richiesta di **Conferma** prima del passaggio
effettivo:

![Carica modello](../assets/model-sf-load-model.png)

**Riproduci vario** — genera l'audio del vario a partire da una sorgente
scelta (normalmente il sensore VSpeed di un vario FrSky, ma è utilizzabile
qualsiasi sensore con unità m/s):

![Riproduci vario](../assets/model-sf-play-vario.png)
![Sorgente vario: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Intervallo** — velocità di salita/discesa associata al tono, valore
  predefinito ±10 m/s (fino a ±100 m/s). Al di sopra del **Centro**, il
  tono sale linearmente con la velocità di salita fino al valore massimo
  dell'Intervallo (il tono alla velocità massima si imposta in [Generale →
  Vario](../system-setup/general.md#vario)); in discesa viene emesso un
  tono continuo che scende di frequenza verso il valore minimo
  dell'Intervallo.
- **Centro** — la banda di "salita zero", predefinita ±0,3 m/s (fino a
  ±2 m/s); al suo interno il tono resta costante (anche il tono a velocità
  zero si imposta in Generale → Vario). Imposta **Beep**→**Silenzioso**
  per disattivare completamente il tono.

  ![Opzioni intervallo/centro del vario](../assets/model-sf-play-vario-options.png)
