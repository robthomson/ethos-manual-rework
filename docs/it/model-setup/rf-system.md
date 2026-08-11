---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sistema RF

Configura il modulo o i moduli RF interni e/o esterni del modello, l'ID di
registrazione del proprietario, il binding del ricevitore e le opzioni del
ricevitore. È anche qui che risiede la scelta tra modulo interno ed esterno per il
modello — a differenza di quasi tutto il resto in
[Configurazione di sistema](../system-setup/index.md), la selezione
dell'hardware RF avviene **per modello**, non a livello di radio.

!!! note "Screenshot in attesa"
    Il set di screenshot di questa sezione non è ancora stato acquisito (vedi
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)) — il
    contenuto seguente è accurato ma per ora è solo testuale.

## ID di registrazione del proprietario {: #owner-registration-id }

Un codice univoco di 8 caratteri (combinazione di lettere maiuscole/minuscole e cifre, senza
caratteri speciali) che diventa l'**ID di registrazione** di un ricevitore quando questo viene
registrato. Impostando lo *stesso* codice su più trasmettitori è possibile utilizzare
**Smart Share** tra di essi — farlo prima di creare il modello che si desidera
condividere. Compatibile con EdgeTX; solo parzialmente compatibile con OpenTX.

## Disattivare l'uscita RF

Tieni premuto `PAGE` durante l'accensione per disattivare l'uscita RF interna ed esterna
per quella sessione (un avviso conferma che è disattivata). L'impostazione
**State** del modulo rimane su ON — un normale riavvio ripristina la trasmissione normale.

## Modalità del modulo interno

Il modulo interno di X18/X20/X20S/X20HD (TD-ISRM) funziona in una di tre
modalità — il modulo TD-ISRM Pro delle X20 Pro/R/RS è simile ma aggiunge varianti LoRa e
tandem dual band. La modalità selezionata **deve corrispondere al tipo supportato dal
ricevitore**, altrimenti il modello non si collegherà; dopo il cambio di modalità,
controlla attentamente il funzionamento di tutti i canali del ricevitore e soprattutto il
comportamento del Failsafe.

- **ACCESS** — i percorsi RF 2.4GHz e 900MHz lavorano in tandem con un unico set di
  controlli ACCESS. Fino a tre ricevitori in totale, in qualsiasi combinazione di 2.4GHz
  (24 canali) e 900MHz (16 canali); la telemetria di entrambi i collegamenti è
  attiva contemporaneamente e i sensori sono identificati per banda. Una sorgente di
  telemetria **RX** indica quale ricevitore è attualmente il ricevitore di telemetria attivo.
- **ACCST D16** — un singolo percorso a 2.4GHz, per i ricevitori della serie "X".
- **TD mode** — tandem 2.4GHz + 900MHz a bassa latenza e lunga portata per i ricevitori
  Tandem, 24 canali su entrambe le bande.

Le build del **firmware Flex** aggiungono una seconda colonna Type per commutare tra la modulazione
FLEX915M (915MHz in stile FCC) e FLEX868M (868MHz in stile LBT)
in una qualsiasi delle tre modalità precedenti — è necessario montare le antenne corrispondenti
a quella selezionata. Gli utenti UE possono usare 200/500mW sugli 868MHz; a 25mW
la telemetria viaggia via 868MHz, a 200/500mW passa ai 2.4GHz per
conformità normativa.

Ogni scelta di modalità e di gamma di canali comporta un compromesso sulla frequenza di
aggiornamento — ad esempio con ACCESS 8 canali si aggiornano ogni 7ms, 16 ogni 14ms,
24 ogni 21ms (inviati a rotazione in blocchi di 8), ed è disponibile una **Modalità corsa**
a 4ms con Ch1-8 e ricevitori compatibili (serie RS, v2.1.7 o successiva).

## Registrazione e binding di un ricevitore (ACCESS) {: #registering-and-binding-a-receiver-access }

Il binding di un ricevitore ACCESS si divide in due fasi — la **registrazione** deve
essere eseguita una sola volta per ogni coppia ricevitore/trasmettitore; il **binding** può
essere ripetuto successivamente in modalità wireless, senza utilizzare il pulsante di
collegamento sul ricevitore.

**Fase uno — Registrazione**:

1. Tocca **Register** (salta completamente questo passaggio se il ricevitore è già
   registrato).
2. Tenendo premuto il tasto bind, accendi il ricevitore e attendi che entrambi
   i LED si attivino. Il messaggio "Waiting for receiver…" cambia in
   "Receiver connected" e il campo con il nome del ricevitore viene compilato automaticamente.
3. Conferma o modifica l'**ID di registrazione** (per impostazione predefinita è l'ID di
   registrazione del proprietario indicato sopra — sono gli ID identici tra i trasmettitori a far
   funzionare Smart Share), il **Nome RX** e l'**UID**. L'UID viene utilizzato per
   distinguere tra più ricevitori utilizzati contemporaneamente in un unico modello — può
   essere lasciato a 0 per un singolo ricevitore; con più ricevitori (ad es. uno per ogni
   blocco di 8 canali) di solito si usano 0/1/2. Tieni presente che questo UID non può essere
   letto dal ricevitore, quindi è bene etichettare il ricevitore.
4. Premi **Register** per completare l'operazione, conferma "Registration ok", quindi spegni
   il ricevitore — a questo punto è registrato, ma deve ancora essere collegato.

**Fase due — Binding**:

!!! warning
    Non eseguire mai l'operazione di binding con un motore elettrico collegato o un motore a combustione interna acceso.

1. Ricevitore spento; conferma di essere nella modalità di modulo corretta.
2. Tocca **RX1** (o 2/3) → **Bind**. Un avviso vocale annuncerà "Bind" ogni pochi secondi
   per confermare che sei in modalità bind.
3. Accendi il ricevitore **senza** toccare il pulsante di collegamento F/S; selezionalo
   dall'elenco "Select device" che compare.
4. Conferma "Bind OK". Spegni e riaccendi sia la radio sia il ricevitore —
   se il LED verde del ricevitore è acceso e il LED rosso è spento, il ricevitore è collegato
   al trasmettitore. Il collegamento non dovrà essere ripetuto, a meno che uno dei due non
   venga sostituito.
5. Ripeti l'operazione per i ricevitori aggiuntivi (RX2, RX3), se applicabile.

## Opzioni del ricevitore

Con il ricevitore acceso, tocca il relativo pulsante RX per accedere a:

- **Options** — **Telemetria** (può essere disabilitata per questo ricevitore), **Potenza
  telemetria ridotta 25mW** (invece dei normali 100mW — utile se, ad esempio, i servi
  subiscono interferenze a causa delle radiofrequenze inviate vicino a loro), **Alta
  velocità PWM** (velocità di aggiornamento PWM di 7 ms invece dei 18 ms standard —
  assicurati che i tuoi servi siano in grado di gestire questa velocità), **Porta di
  telemetria** (S.Port/F.Port/FBUS), **SBUS** (modalità a 16 o 24 canali — tutti i
  dispositivi SBUS collegati devono supportare la modalità SBUS-24 per poter attivare il
  nuovo protocollo) e **Mappatura dei canali**, per riattribuire i canali ai pin del
  ricevitore.
- **Share** — permette di spostare il ricevitore su un'altra radio ACCESS con un
  *diverso* ID di registrazione del proprietario. Sulla radio sorgente tocca Condividi (il
  LED verde del ricevitore si spegne); sulla radio di destinazione esegui il Bind
  normalmente — il processo di condivisione salta la fase di registrazione, perché l'ID di
  registrazione del proprietario viene trasferito automaticamente. Premi EXIT sulla radio
  sorgente per interrompere il processo di condivisione; un nuovo collegamento riporta il
  ricevitore alla radio di partenza. (Non è necessario utilizzare questa funzione se tutte
  le radio utilizzano lo stesso ID di registrazione del proprietario — basta eseguire il
  binding direttamente sulla radio che deve controllare il ricevitore.)
- **Reset bind** — ripulisce e ripristina il binding dopo una condivisione; spegni poi il
  ricevitore e sarà collegato al tuo trasmettitore.
- **Factory reset** — ripristina le impostazioni di fabbrica del ricevitore e ne cancella
  l'UID, annullandone completamente la registrazione.

Con il ricevitore **spento**, lo stesso pulsante RX offre **Options** (la radio tenterà di
connettersi e attenderà il ricevitore), **Bind** (ad es. per ricollegare un ricevitore
precedentemente legato a un altro trasmettitore) e **Clear** (equivalente a un Reset bind).

## Aggiunta di un ricevitore ridondante {: #redundant-receivers }

Un secondo ricevitore può essere collegato a uno slot RX non utilizzato per garantire la
ridondanza — un ricevitore 2.4G o 900M può essere il backup dell'altro. La ridondanza FrSky
per il controllo viene sempre valutata **per ogni frame**, scegliendo il frame migliore
disponibile (failover attivo/attivo), quindi il controllo può passare da un ricevitore
all'altro a seconda delle necessità su ogni frame.

1. Collega la porta SBUS Out del ricevitore ridondante alla porta SBUS IN del ricevitore principale.
2. Abilita il corrispondente modulo RF interno (ad es. 900M) e configura l'antenna e le
   opzioni di potenza RF.
3. Registra il nuovo ricevitore (se non è ancora stato registrato), quindi eseguine il
   binding sullo slot RX libero come descritto sopra.
4. Assicurati che il LED verde sia acceso — il ricevitore ridondante sarà ora elencato.

## Failsafe {: #failsafe }

I dati di failsafe vengono inviati dal trasmettitore ogni 10 secondi circa; sui
ricevitori TD, TW, AP e AP Plus sono ora salvati anche sul ricevitore, il che significa che
le impostazioni sono immediatamente disponibili se il ricevitore si riavvia per qualsiasi
motivo. La funzione Failsafe deve essere reimpostata e controllata attentamente dopo aver
aggiornato i ricevitori con questa funzione.

- **Hold** — mantiene le ultime posizioni ricevute.
- **Custom** — per ogni canale: **Not Set**, **Hold**, **Custom** (un valore
  fisso — tocca l'icona con la freccia per utilizzare il valore corrente del canale, oppure
  inseriscine uno direttamente) o **No Pulses**.
- **No Pulses** — disattiva gli impulsi, da utilizzare con i controllori di volo dotati di
  ritorno a casa via GPS in caso di perdita del segnale.
- **Receiver** — (ricevitori della serie X o successivi) permette di impostare il failsafe
  nel ricevitore stesso.

!!! warning
    Assicurati di testare attentamente le impostazioni di Failsafe scelte prima di
    farvi affidamento.

## Controllo portata {: #range-check }

Un Controllo portata deve essere effettuato sul campo prima di ogni sessione di volo con una
configurazione nuova o modificata. Selezionando **Range Check** si riduce deliberatamente la
potenza del trasmettitore (un avviso vocale ripetuto conferma la modalità) e vengono
visualizzati i valori VFR% e RSSI in tempo reale per valutare la qualità della ricezione. Il
livello di controllo della portata FrSky è di circa −10 dB rispetto al normale livello
operativo di +20 dB; in condizioni ideali, con la radio e il ricevitore a 1 metro dal suolo,
dovresti ricevere un allarme critico solo a circa 30 metri di distanza — una distanza
inferiore in condizioni normali può indicare un problema.

Con più ricevitori collegati, i dati di Controllo portata vengono forniti per un ricevitore
alla volta su ciascun link — spegnendo il ricevitore attualmente attivo, il successivo
(con priorità 0, 1 e poi 2, indicato dal sensore **RX**) diventerà il ricevitore di
telemetria attivo, così da poter controllare ciascuno a turno.

## Moduli RF esterni e di terze parti

I moduli esterni FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
seguono lo stesso schema Register/Bind del modulo interno, con
numero di canali, livelli di potenza e requisiti di antenna specifici per protocollo
— per i dettagli sulla configurazione, consulta il manuale del modulo in questione.

**ELRS** (ExpressLRS) è supportato sia tramite la modalità ELRS del modulo TWIN Lite Pro
sia tramite moduli ELRS veri e propri (che richiedono l'installazione dello script ELRS Lua
in `scripts/elrs` prima di ottenere l'opzione ELRS come modulo). Sono supportati dodici
canali; le impostazioni principali sono **Packet Rate** (compromesso tra portata e latenza),
**Telemetry Ratio** (frequenza di invio dei dati di telemetria, da 1:1 a 1:128),
**Switch Mode** (**Hybrid** — la maggior parte dei canali ausiliari a 2 o 3 posizioni
per ridurre la latenza — oppure **Wide** — risoluzione completa a 64–128 passi),
**Model Match** e **Tx Power** (da 10mW a 1000mW, con **Dynamic Power** opzionale per
regolare automaticamente la potenza in base alla qualità del collegamento — richiede la
telemetria abilitata).

I **moduli di terze parti** (attualmente Ghost, Multi-protocol e Crossfire, oltre
a ELRS) richiedono ciascuno il proprio script Lua installato dall'utente — vedi
le note su `scripts/` in [Screenshot Pipeline](../contributing/screenshot-pipeline.md)
e il thread *Third-Party External Modules* su rcgroups. La selezione di un
modulo appare nella schermata RF solo dopo l'installazione del relativo script.
Il modulo Multi-protocol (IRX4 Lite) può inoltre essere
aggiornato via firmware direttamente da [File Manager](../system-setup/file-manager.md):
copia il file del firmware nella cartella `Firmware/`, poi seleziona **Flash external
multimodule**.
