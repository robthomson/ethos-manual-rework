---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Utilizzo

## Sezione Welcome

**Update News** — note di rilascio e raccomandazioni sui backup prima
dell'aggiornamento. Ethos 1.6.0+ richiede che il modulo RF interno e i
ricevitori TD/TW/AP/AP Plus siano alla versione 3.0.1 o successiva per
poterne sfruttare i miglioramenti. Attivando le **Pre-releases** (con
l'impostazione del server su GitHub — vedi [Impostazioni della
Suite](#suite-settings)) vengono elencate qui anche le build di
pre-rilascio, insieme allo storico completo delle versioni.

**Ethos web page** — una vista integrata di ethos.frsky-rc.com: risorse,
collegamenti ai template dei modelli ed elenco delle radio supportate.

## Sezione Radio

Gestisce la radio collegata. Accendila in [modalità
Bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) e
collegala via USB — la Suite mostra il tipo di radio (ad es. "X20") una
volta rilevata.

### Informazioni sulla radio

- **Ethos** — versioni installate di firmware e bootloader; **Manage
  Ethos** porta direttamente al loro aggiornamento se non sono
  aggiornate.
- **RF Module** — firmware installato del modulo RF interno; **Manage
  internal module** porta direttamente al suo aggiornamento se non è
  aggiornato.
- **Model manager** / **Lua library** / **Download center** — scorciatoie
  verso questi strumenti.

### Aggiornamento di Ethos {: #updating-ethos }

La scheda **Ethos** mostra affiancate le versioni del firmware, del
bootloader, dei file audio della scheda SD o eMMC e delle bitmap di
sistema della memoria flash — i file di sistema nella memoria flash
vengono ora aggiornati insieme al firmware, quindi non devono più essere
gestiti separatamente.

- **Write outdated components** — aggiorna solo i componenti obsoleti.
- **Write all components** — aggiorna tutto, indipendentemente dalla
  versione.
- Opzioni individuali **Write firmware**, **Write bootloader**, **Write
  audio files**, ciascuna avviata cliccando sul pulsante grigio scuro di
  aggiornamento accanto all'opzione selezionata.
- **Flash from a local file** — salta il download ed esegue il flash
  della radio da un file firmware già presente sul disco.

Selezionare una release significa scegliere prima il ramo desiderato
(Stabile/Versione di prova) e poi la versione. Prima di continuare ti
verrà richiesto di eseguire un backup della radio (**Go to backup
page**) — eseguilo. Se il modulo RF interno non è alla versione 3.0.1 o
successiva, Ethos 1.6.0 o superiore ne richiede l'aggiornamento prima di
poter proseguire (**Go to Module manager** ne esegue il flash
automaticamente, dopodiché l'aggiornamento di Ethos continua) — inoltre
sui ricevitori TD/TW/AP/AP Plus occorre poi cancellare la telemetria e
riscoprire i sensori per ottenere i nomi aggiornati della telemetria.

L'avanzamento dell'aggiornamento viene mostrato passo dopo passo
(passaggio al bootloader, download del firmware, copia del firmware,
smontaggio delle unità, scrittura del firmware, aggiornamento delle
informazioni radio, "Aggiornamento riuscito!") — a questo punto anche il
display della radio mostra l'avanzamento della scrittura.

!!! note "Aggiornamenti pre-release"
    Con gli aggiornamenti pre-release i file possono cambiare senza che
    il numero di versione venga modificato, una situazione che Ethos
    Suite non rileva — devi quindi eseguire sempre un nuovo flash della
    versione pre-release già installata quando diventa una release
    completa. Nel caso del firmware della radio, in caso di dubbio la
    data può essere controllata nella pagina [Sistema →
    Info](../system-setup/information.md).

!!! note "Aggiornamento da Ethos 1.2.8 o versioni precedenti"
    Da una versione così datata Ethos Suite potrebbe non essere in grado
    di eseguire il flash del firmware o del bootloader in modo
    automatico — in questo caso viene visualizzata una finestra di
    dialogo che fornisce una guida al completamento del flash manuale.
    In entrambi i casi, sarebbe prudente espellere manualmente le unità
    prima di scollegare il cavo USB.

Ethos Suite scarica ora automaticamente sulla radio i file bitmap di
sistema corrispondenti al firmware (non è più necessario gestirli
separatamente); i file audio si aggiornano tramite **Write all
components** o **Write audio files** (viene scaricato il pacchetto audio
della lingua selezionata, ad es. "English audio pack").

### RF Module Manager

Seleziona la versione desiderata (di solito la più recente) e clicca su
**Flash module** per scrivere il firmware nel modulo RF interno — al
termine viene visualizzata la finestra di dialogo "...è stato flashato
con successo". Questa operazione viene avviata automaticamente anche
dalla procedura di aggiornamento obbligatorio alla versione 3.0.1
descritta sopra.

### Ethos Mode

**Switch to Ethos** fa uscire la radio dalla modalità bootloader
riavviandola in Ethos (indicato da un'icona USB verde sulla radio e dalla
scomparsa di "(Bootloader Mode)" nell'intestazione della Suite). La
modalità Ethos è necessaria affinché il **Download center** possa usare
la radio come proxy per eseguire il flash di moduli, ricevitori, sensori
e servi. Il pulsante diventa quindi **Switch to Bootloader**, che
permette di tornare in modalità bootloader. **Eject Drives** scollega la
radio in modo sicuro.

### Model Manager

Permette di salvare su disco un backup dei file dei modelli e delle
impostazioni, oppure di ripristinare un backup precedente.

!!! warning
    Il ripristino **non** ripristina il firmware — dopo aver ripristinato
    modelli e impostazioni, devi ancora riscrivere separatamente la
    versione di firmware corrispondente al tuo backup (vedi
    [Aggiornamento di Ethos](#updating-ethos)), poiché i file dei modelli
    non sono retrocompatibili.

- **Backup Location** — clicca sull'icona della cartella per navigare e
  selezionare il percorso di backup desiderato (viene salvato per ogni
  tipo di radio); sotto la posizione vengono visualizzate la data e l'ora
  dell'ultimo backup.
- **Backup** — salva i file dei modelli, registrando insieme ad essi la
  versione corrente di Ethos.
- **Restore** — seleziona i componenti da ripristinare: Audio (non
  selezionato per impostazione predefinita), Script, Screenshot, Bitmap
  di sistema (non selezionate per impostazione predefinita — ora gestite
  insieme al firmware), Modelli (inclusi i file di testo della
  [checklist definita dall'utente](../how-to/user-defined-checklist.md)
  memorizzati insieme ad essi), Lingua, Bitmap utente, Registri,
  Impostazioni di sistema.

### Lua library

Consente di sfogliare e installare con un clic script e strumenti Lua
dalla libreria remota di FrSky (oppure di installarli da un file zip
locale); gli script installati vengono mostrati accanto al catalogo
remoto non appena ne esiste almeno uno.

## Sezione Tools

- **Download center** — permette di scaricare qualsiasi firmware dal sito
  di download di FrSky e, mentre la radio è in modalità Ethos, di
  utilizzarla come proxy per eseguire il flash di un modulo, un sensore,
  un servo o un ricevitore collegato tramite una connessione di
  aggiornamento S.Port. Scegli il prodotto dall'elenco (ad es. un
  ricevitore TW SR8), sfoglia gli **assets** disponibili, clicca su
  **Download** per salvarlo localmente oppure su **Flash** per scriverlo
  direttamente sul dispositivo collegato — una barra di avanzamento segue
  il flash, che termina con "...è stato flashato con successo!"

- **Image manager** — converte le immagini nel formato nativo di Ethos
  (BMP a 32 bit, RGB, canale alfa aggiunto solo se necessario) nella
  dimensione scelta, preservando le proporzioni. Dimensioni di
  riferimento: immagini dei modelli 300×280 (X20) / 180×168 (X18);
  immagini a schermo intero 800×480 (X20) / 480×320 (X18) — vedi [File
  Manager](../system-setup/file-manager.md#top-level-folders) per le
  regole di denominazione delle bitmap. Permette inoltre di sfogliare
  direttamente le cartelle `bitmaps/gps`, `bitmaps/models` e
  `bitmaps/user` della radio, con supporto al caricamento. Aggiungi le
  immagini all'elenco di conversione con **+** (il formato TIFF non è
  supportato), scegli un percorso di destinazione (una cartella locale;
  direttamente sulla radio nelle immagini modello/utente/GPS; oppure la
  cartella della radio attualmente aperta) e, facoltativamente, apri
  automaticamente la cartella di destinazione o forza il canale alfa.

- **Audio manager** — converte l'audio nel formato di Ethos (PCM lineare,
  32 kHz, mono, 16 bit little-endian). Aggiungi i file con **+**, scegli
  una cartella locale oppure inviali direttamente alla cartella `audio`
  della radio (spostandoli poi nella sottocartella della voce corretta),
  con la possibilità di aprire automaticamente la destinazione.

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

- **DFU Flasher** — esegue il flash del bootloader tramite una
  connessione USB a radio spenta (DFU), funzionando anche con firmware
  completamente corrotto, poiché il bootloader ST sottostante risiede in
  ROM. Clicca su **Select Bootloader** per scegliere un file scaricato
  (la Suite ne riporta versione e idoneità), collega la radio **spenta**,
  quindi clicca su **Flash**.

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
