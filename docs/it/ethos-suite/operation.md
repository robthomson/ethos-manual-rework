---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Utilizzo

## Sezione Welcome

**Update News** — note di rilascio e raccomandazioni sui backup prima
dell'aggiornamento. Ethos 1.6.0+ richiede che il modulo RF interno e i
ricevitori TD/TW/AP/AP Plus siano alla versione v3.0.1+ per poterne
sfruttare i miglioramenti. Attivando le **Pre-releases** (con il server
impostato su GitHub — vedi [Impostazioni della
Suite](#suite-settings)) vengono elencate qui anche le build di
pre-rilascio, insieme allo storico completo delle versioni.

**Ethos web page** — una vista integrata di ethos.frsky-rc.com: risorse,
collegamenti ai template dei modelli ed elenco delle radio supportate.

## Sezione Radio

Gestisce la radio collegata. Accendila in [modalità
bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) e
collegala via USB — la Suite mostra il tipo di radio (ad es. "X20") una
volta rilevata.

### Informazioni sulla radio

- **Ethos** — versioni installate di firmware/bootloader; **Manage Ethos**
  porta direttamente al loro aggiornamento se non sono aggiornate.
- **RF Module** — firmware installato del modulo RF interno; **Manage
  internal module** porta direttamente al suo aggiornamento se non è
  aggiornato.
- **Model manager** / **Lua library** / **Download center** — scorciatoie
  verso questi strumenti.

### Aggiornamento di Ethos {: #updating-ethos }

La scheda **Ethos** mostra affiancate le versioni di Firmware,
Bootloader, SD card/eMMC (file audio) e memoria flash (bitmap di
sistema) — i file di sistema in flash vengono ora aggiornati insieme al
firmware e non sono più gestiti separatamente.

- **Write outdated components** — aggiorna solo ciò che non è aggiornato.
- **Write all components** — aggiorna tutto, indipendentemente dalla
  versione.
- Opzioni individuali **Write firmware**, **Write bootloader**, **Write
  audio files**, ciascuna avviata premendo il pulsante grigio scuro
  accanto all'opzione scelta.
- **Flash from a local file** — salta il download e utilizza un file
  firmware già presente sul disco.

Selezionare una release significa scegliere prima un **branch**
(Stable/Testing) e poi una versione. L'aggiornamento richiede
innanzitutto un backup (**Go to backup page**) — eseguilo. Se il modulo
RF interno non è alla versione v3.0.1+, Ethos 1.6.0+ ne richiede
l'aggiornamento prima di proseguire (**Go to Module manager** lo
aggiorna automaticamente, quindi l'aggiornamento di Ethos riprende) — e
per i ricevitori TD/TW/AP/AP Plus è necessario, successivamente,
eliminare e riscoprire la telemetria per acquisire i nomi aggiornati dei
sensori.

L'avanzamento dell'aggiornamento viene mostrato passo dopo passo
(passaggio al bootloader, download, copia, smontaggio, scrittura,
aggiornamento, "Update successful!") — anche lo schermo della radio
riflette l'avanzamento della scrittura.

!!! note "Aggiornamenti di pre-rilascio"
    I file di una pre-release possono cambiare senza che ne cambi il
    numero di versione, cosa che la Suite non è in grado di rilevare —
    riprogramma sempre una versione di pre-rilascio già installata non
    appena diventa una release completa. In caso di dubbio, verifica la
    data del firmware in [Sistema →
    Info](../system-setup/information.md).

!!! note "Aggiornamento da Ethos 1.2.8 o versioni precedenti"
    La Suite potrebbe non essere in grado di programmare
    firmware/bootloader in modo completamente automatico da una versione
    così datata — in tal caso compare una finestra guidata per la
    programmazione manuale. In entrambi i casi, espelli manualmente le
    unità prima di scollegare l'USB.

I file bitmap di sistema vengono ora aggiornati automaticamente insieme
al firmware (non è necessaria alcuna gestione separata); i file audio si
aggiornano tramite **Write all components** o **Write audio files**
(viene scaricato il pacchetto della lingua selezionata, ad es. "English
audio pack").

### RF Module Manager

Seleziona una versione (normalmente la più recente) e premi **Flash
module** per aggiornare direttamente il firmware del modulo RF interno —
al termine viene confermato "...has been flashed successfully". Questa
operazione viene attivata automaticamente anche dalla procedura di
aggiornamento obbligatorio a v3.0.1 descritta sopra.

### Ethos Mode

**Switch to Ethos** riavvia la radio uscendo dalla modalità bootloader ed
eseguendo Ethos (indicato da un'icona USB verde sulla radio e dalla
scomparsa di "(Bootloader Mode)" nell'intestazione della Suite). Questo è
necessario affinché il **Download center** possa usare la radio come
proxy per programmare moduli, ricevitori, sensori e servi. Il pulsante
diventa quindi **Switch to Bootloader** per invertire l'operazione.
**Eject Drives** scollega la radio in modo sicuro.

### Model Manager

Esegue il backup su disco dei file dei modelli e delle impostazioni,
oppure ripristina un backup precedente.

!!! warning
    Il ripristino **non** ripristina il firmware — dopo aver ripristinato
    modelli/impostazioni, riprogramma separatamente la versione di
    firmware effettivamente corrispondente a quel backup (vedi
    [Aggiornamento di Ethos](#updating-ethos)), poiché i file dei modelli
    non sono retrocompatibili.

- **Backup Location** — seleziona una cartella (memorizzata per ciascun
  tipo di radio); sotto di essa viene mostrata la data/ora dell'ultimo
  backup.
- **Backup** — salva i file dei modelli, registrando insieme ad essi la
  versione di Ethos corrente.
- **Restore** — seleziona quali componenti ripristinare: Audio
  (disattivato per impostazione predefinita), Scripts, Screenshots,
  System Bitmaps (disattivato per impostazione predefinita — ora gestiti
  con il firmware), Models (inclusi eventuali file di testo di
  [checklist definite dall'utente](../how-to/user-defined-checklist.md)
  memorizzati insieme ad essi), Language, User Bitmaps, Logs, System
  Settings.

### Lua library

Consente di sfogliare e installare con un clic script/strumenti Lua dalla
libreria remota di FrSky (oppure di installarli da un file zip locale);
gli script installati vengono mostrati accanto al catalogo remoto una
volta che ne esiste almeno uno.

## Sezione Tools

- **Download center** — scarica qualsiasi firmware dal sito FrSky e
  (mentre la radio è in modalità Ethos) la utilizza come proxy per
  programmare un modulo, un sensore, un servo o un ricevitore collegato
  tramite una connessione di aggiornamento S.Port. Scegli il prodotto
  dall'elenco (ad es. un ricevitore TW SR8), sfoglia gli **assets**
  disponibili, premi **Download** per salvarlo localmente oppure **Flash**
  per scriverlo direttamente sul dispositivo collegato — una barra di
  avanzamento segue la programmazione, che termina con "...has been
  flashed successfully!"

- **Image manager** — converte le immagini nel formato nativo di Ethos
  (BMP a 32 bit, RGB, canale alfa aggiunto solo se necessario) nella
  dimensione scelta, preservando le proporzioni. Dimensioni di
  riferimento: immagini dei modelli 300×280 (X20) / 180×168 (X18);
  immagini a schermo intero 800×480 (X20) / 480×320 (X18) — vedi [File
  Manager](../system-setup/file-manager.md#top-level-folders) per le
  regole di denominazione dei bitmap. Permette inoltre di sfogliare
  direttamente le cartelle `bitmaps/gps`, `bitmaps/models` e
  `bitmaps/user` della radio, con supporto al caricamento. Aggiungi le
  immagini all'elenco di conversione con **+** (il formato TIFF non è
  supportato), scegli un percorso di destinazione (una cartella locale;
  direttamente sulla radio nelle immagini modello/utente/GPS; oppure la
  cartella della radio attualmente aperta) e, facoltativamente, apri
  automaticamente la cartella di destinazione o forza un canale alfa.

- **Audio manager** — converte l'audio nel formato di Ethos (PCM lineare,
  32 kHz, mono, 16 bit little-endian). Aggiungi i file con **+**, scegli
  una cartella locale o inviali direttamente alla cartella `audio` della
  radio (spostandoli poi nella sottocartella della voce corretta), con
  possibilità di aprire automaticamente la destinazione.

- **Lua development tools** — **Lua Docs** rimanda alla guida di
  riferimento Lua di Ethos (vedi anche il thread rcgroups *FrSky - ETHOS
  Lua Script Programming*); **Lua Demo Scripts** rimanda agli script di
  esempio sul GitHub Ethos-Feedback-Community; **Debug** apre una
  finestra di log in tempo reale per le tracce `print()` di Lua inviate
  tramite USB-Serial mentre la radio è in modalità Serial:

  1. Collega la radio alla Suite normalmente e passa alla modalità Ethos.
  2. Modifica gli script Lua direttamente sull'unità montata della radio,
     con un qualsiasi editor di codice.
  3. Apri **Lua Development Tools** → **START DEBUG** — la radio si
     riavvia in modalità Serial/debug e reinizializza gli script.
  4. L'output `print()` di ogni script attivo viene trasmesso al
     terminale della Suite.
  5. **STOP DEBUG** riporta alla modalità Ethos normale per proseguire
     con le modifiche.

- **DFU Flasher** — programma il bootloader tramite una connessione USB a
  radio spenta (DFU), funzionando anche con firmware completamente
  corrotto, poiché il bootloader ST sottostante risiede in ROM. Premi
  **Select Bootloader** per scegliere un file scaricato (la Suite ne
  riporta versione/idoneità), collega la radio **spenta**, quindi premi
  **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Di norma si tratta di un driver DFU mancante o errato. La maggior
      parte dei PC con Windows 10+ gestisce i sistemi Tandem con il
      driver USB DFU predefinito, ma Windows Update a volte lo sostituisce
      con uno generico che non funziona — controlla Gestione dispositivi
      e valuta uno strumento come Impulse Driver Fixer. In particolare
      gli utenti Horus X10 potrebbero dover installare manualmente il
      driver USB del bootloader STM32 (Impulse Driver Fixer o Zadig),
      poiché Windows 10 non lo installa per impostazione predefinita.

- **Repair Tool** — per X18/S, TW Lite, XE e X20 Pro/R/RS: riformatta la
  memoria interna quando la radio non riesce a leggere la NAND o a
  salvare le impostazioni.

## Sezione Others

- **Documentation** — collegamenti al GitHub Ethos-Feedback-Community, ai
  manuali ufficiali di Ethos (scaricabili) e a una FAQ su Ethos Suite.
- **Ethos Github** — release e issue tracker (cerca tra le segnalazioni
  esistenti prima di aprirne una nuova).

### Impostazioni della Suite {: #suite-settings }

- **Language** — ceco, tedesco, inglese, spagnolo, francese, ebraico,
  italiano, olandese, norvegese, portoghese, sloveno, cinese.
- **Server location** — **FrSky server** oppure **GitHub** (necessario
  per l'accesso alle pre-release descritto sopra).
- **Debug options** — attiva/disattiva il popup di errore fatale; abilita
  la registrazione completa dei log di debug della Suite (non solo dei
  crash); apre la cartella dei log.
- **Version** / **Update Suite** — versione corrente e controllo manuale
  degli aggiornamenti.
- **About** — riconoscimenti per i componenti riutilizzati.

## Utilizzo da riga di comando

Ethos Suite può essere eseguita da un terminale:

| Flag | Effetto |
|---|---|
| `--help` | Mostra la guida della riga di comando. |
| `--version` | Mostra la versione della Suite installata. |
| `--list-radios` | Elenca tutte le radio FrSky supportate. |
| `--radio-components --radio {RADIO}` (o `--radio auto`) | Elenca i componenti di una radio collegata e i relativi percorsi. `auto` esegue il rilevamento automatico; specifica `{RADIO}` se è collegata più di una radio. |
| `--get-path {COMPONENT}` | Ottiene il percorso di un componente — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` o `I18N`. |
| `--serial start` \| `--serial stop` | Abilita/disabilita la modalità di debug seriale. |

!!! note
    La Suite non si avvia affatto se non riconosce un comando valido.
