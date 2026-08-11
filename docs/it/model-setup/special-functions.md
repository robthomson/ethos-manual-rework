---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Funzioni speciali

![Menu funzioni speciali](../assets/model-sf-menu.png)

Le funzioni speciali attivano un'azione — riproduzione audio, cattura di
uno screenshot, scrittura dei log, vibrazione aptica e altro ancora —
quando una condizione diventa vera. Ne sono supportate fino a 100;
nessuna è presente per impostazione predefinita. Aggiungine una con
**+**; tocca una funzione esistente per **Modifica**/**Muovi**/
**Copia-incolla**/**Clona**/**Cancella**.

![Aggiungi funzione speciale](../assets/model-sf-add.png)
![Muovi](../assets/model-sf-move.png)

## Campi comuni a tutte le azioni

- **Stato** — abilita o disabilita questa funzione speciale senza
  cancellarla.
- **Condizione attiva** — **Sempre attiva**, oppure attivata da posizioni
  di interruttori, interruttori di funzione, interruttori logici,
  posizioni di trim o modalità di volo. Premi a lungo `ENT` sul nome
  dell'interruttore e seleziona la casella **Negativo** per invertirlo
  (ad esempio `SG-up` diventa `!SG-up`, attivo quando l'interruttore SG
  *non* è in posizione di salita).
- **Globale** — aggiunge questa funzione a **tutti** i modelli, esistenti
  e a qualsiasi nuovo modello creato in futuro. Se un modello esistente ha
  già la funzione, la funzione globale viene aggiunta come nuova funzione;
  disattivando la funzione globale su qualsiasi modello, la funzione viene
  rimossa da tutti i modelli tranne quello correntemente selezionato. Le
  funzioni speciali globali sono memorizzate nel file `radio.bin`, mentre
  quelle locali sono memorizzate nel file del modello.

## Azioni {: #actions }

**Azzeramento** — azzera i **Dati di volo** (telemetria + timer), **Tutti
i timer** oppure **Tutta la telemetria**.

![Azzeramento](../assets/model-sf-reset.png)

**Screenshot** — salva uno screenshot nella cartella `screenshots/` sulla
SD card o sulla eMMC.

![Screenshot](../assets/model-sf-screenshot.png)

**Imposta il failsafe** — registra le posizioni correnti dei canali come
failsafe, tramite il **Modulo** RF interno o esterno.

![Imposta il failsafe](../assets/model-sf-set-failsafe.png)

**Riproduci l'audio** — l'azione più completa, che supporta un'intera
sequenza:

![Riproduci l'audio](../assets/model-sf-play-audio.png)

- **Voce** — quale delle massimo 3 voci configurate utilizzare (consulta
  [Generale](../system-setup/general.md#audio-settings)).
- **Ripeti** — l'audio può essere riprodotto una sola volta oppure
  ripetuto alla frequenza inserita qui (fino a 10 minuti).
- **Salta all'avvio** — se abilitato, questa funzione non verrà riprodotta
  all'avvio.
- **Sequenza** — fino a 100 comandi, ciascuno dei quali può essere:

  - **Riproduci file** — riproduce il file audio selezionato.

    ![Riproduci file](../assets/model-sf-play-audio-add-play-file.png)

  - **Riproduci valore** — riproduce il valore della sorgente
    selezionata: analogici, interruttori, interruttori logici, trim,
    canali, gyro, orologio di sistema, trainer, timer o telemetria.

    ![Riproduci valore](../assets/model-sf-play-audio-add-play-value.png)

  - **Durata dell'attesa** — inserisce un ritardo fisso, fino a 10 minuti.
  - **Condizione di attesa** — mette in pausa la sequenza finché la
    condizione non è soddisfatta.

  ![Aggiungi una nuova linea in sequenza](../assets/model-sf-play-audio-add-line.png)
  ![Tipo di linea della sequenza](../assets/model-sf-play-audio-add-line-type.png)

  Ad esempio: riprodurre `vfrlow.wav` quando l'interruttore logico
  `VFRlow` diventa attivo, seguito dal valore minimo di VFR registrato —

  ![Riproduci valore dopo il file](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — oppure mettere in pausa una sequenza fino a quando l'interruttore SH
  non viene spostato in posizione di riposo:

  ![Sequenza con condizione di attesa](../assets/model-sf-play-audio-add-sequence.png)

  Toccando una riga della sequenza è possibile modificarla, aggiungerne
  una nuova, spostarla o cancellarla:

  ![Gestione delle sequenze](../assets/model-sf-play-audio-add-sequence-management.png)

**Aptico** — vibrazione di feedback:

![Aptico](../assets/model-sf-haptic.png)

- **Pattern** — imposta il modello dell'aptico: singola, doppia, tripla,
  quintupla o molto breve.

  ![Pattern aptico](../assets/model-sf-haptic-pattern.png)

- **Intensità** — la forza della vibrazione aptica, tra 1 e 10
  (predefinita 5).
- **Ripeti** — una sola volta oppure ripetuto con la frequenza inserita
  qui.
- **Seleziona i motori aptici** — sulle radio dotate di motori con
  feedback aptico nei joystick (X20 Pro AW, X20RS, oppure una X20 Pro/X20R
  aggiornata montando i joystick aptici MC20R — consulta
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Predefinito** (aptico interno), **Tutti i motori**, **Stick sinistro**
  o **Stick destro**.

  ![Aptico su X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Scrivi i log** — i file di log vengono memorizzati in formato `.csv`
nella cartella `Logs/` della SD card o della eMMC; l'ora e la data
dell'RTC vengono registrate insieme ai dati (fondamentali per distinguere
poi le singole sessioni di volo):

![Scrivi i log](../assets/model-sf-write-logs.png)

- **Intervallo di scrittura** — regolabile tra 100 e 500 ms.
- **Stick/Potenziometro/slider**, **Interruttori**, **Interruttori
  logici**, **Canali** — categorie di registrazione attivabili in modo
  indipendente.

  **Visualizzatore di log**: apri un file di log dalla cartella `/Logs`
  con il File Manager. Seleziona i canali da visualizzare (l'RSSI è
  selezionato per impostazione predefinita); la visualizzazione può essere
  spostata con l'encoder rotativo o passando il dito a sinistra o a
  destra, e può essere ingrandita o ridotta ruotando l'encoder mentre si
  tiene premuto `PAGE`. Il pulsante `DISP` sposta il focus sul primo
  pulsante della colonna di destra.

**Riproduci testo** (solo X20 Pro) — sintesi vocale generata dalla radio
anziché la riproduzione di un file preparato in precedenza:

![Riproduci testo](../assets/model-sf-x20pro-play-text.png)

- **Testo** — la stringa di testo da convertire in voce e riprodurre.
  Usando le lettere MAIUSCOLE la parola verrà riprodotta facendo lo
  “spelling” (ad esempio "OFF" verrà riprodotto come "O-F-F"); usando il
  minuscolo viene riprodotta la parola intera ("off").
- **Ripeti**, **Salta all'avvio** — come sopra.

**Vai alla schermata** — fa passare il display alla schermata
selezionata, ad esempio alla registrazione dei dati di volo di un
ricevitore quando viene premuto un pulsante:

![Vai alla schermata](../assets/model-sf-go-to-screen.png)
![Opzioni schermo](../assets/model-sf-go-to-screen-options.png)

**Blocca il touchscreen** — blocca il touchscreen per evitare che venga
utilizzato inavvertitamente (la funzione è disponibile anche premendo
contemporaneamente `ENT` e `PAGE` per 1 secondo dalla schermata
principale):

![Blocca il touchscreen](../assets/model-sf-lock-touchscreen.png)

**Carica il modello** — carica il **Modello** specificato quando la
condizione attiva è soddisfatta, con un'eventuale richiesta di
**Conferma** prima del passaggio effettivo:

![Carica il modello](../assets/model-sf-load-model.png)

**Esegui vario** — genera l'audio del vario a partire da una sorgente
scelta (di solito il sensore VSpeed dei vario FrSky, ma è possibile
utilizzare qualsiasi sensore con unità di misura m/s):

![Esegui vario](../assets/model-sf-play-vario.png)
![Sorgente vario: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Intervallo** — il tasso di salita o discesa associato al tono, per
  impostazione predefinita ±10 m/s (fino a ±100 m/s). Quando la velocità
  di salita è superiore al valore di **Centro**, il tono aumenta in modo
  lineare fino a raggiungere il valore massimo dell'Intervallo (il tono
  alla massima velocità di salita può essere configurato in [Generale →
  Vario](../system-setup/general.md#vario)); in discesa il tono è continuo
  e diminuisce linearmente fino al valore minimo dell'Intervallo.
- **Centro** — la banda che definisce un tasso di salita pari a zero, per
  impostazione predefinita ±0,3 m/s (fino a ±2 m/s); al suo interno il
  tono è costante (anche il tono a velocità di salita zero si configura in
  Generale → Vario). Passando da **Beep** a **Silenzioso** i segnali
  acustici vengono tacitati.

  ![Opzioni intervallo/centro del vario](../assets/model-sf-play-vario-options.png)
