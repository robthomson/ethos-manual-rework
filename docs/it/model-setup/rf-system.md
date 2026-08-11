---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sistema RF

Configura il modulo o i moduli RF interni e/o esterni del modello, l'Owner
Registration ID, l'associazione del ricevitore e le opzioni del ricevitore. È anche
qui che risiede la scelta tra modulo interno ed esterno per il modello — a differenza
di quasi tutto il resto in [Configurazione di sistema](../system-setup/index.md), la selezione
dell'hardware RF è **per modello**, non a livello di radio.

!!! note "Screenshot in attesa"
    Il set di screenshot di questa sezione non è ancora stato acquisito (vedi
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)) — il
    contenuto seguente è accurato ma per ora è solo testuale.

## Owner registration ID {: #owner-registration-id }

Un codice univoco di 8 caratteri (combinazione di lettere maiuscole/minuscole e cifre, senza
caratteri speciali) che diventa il **Registration ID** di un ricevitore quando questo viene
registrato. Impostare lo *stesso* codice su più trasmettitori consente di usare
**Smart Share** tra di essi — farlo prima di creare il modello che si desidera
condividere. Compatibile con EdgeTX; solo parzialmente compatibile con OpenTX.

## Disattivare l'uscita RF

Tenere premuto `PAGE` durante l'accensione per disattivare l'uscita RF interna ed esterna
per quella sessione (un avviso conferma che è disattivata). L'impostazione
**State** del modulo rimane su ON — un normale riavvio ripristina la trasmissione normale.

## Modalità del modulo interno

Il modulo interno di X18/X20/X20S/X20HD (TD-ISRM) funziona in una di tre
modalità — il modulo TD-ISRM Pro delle X20 Pro/R/RS è simile ma aggiunge varianti LoRa e
tandem dual-band. La modalità selezionata **deve corrispondere a ciò che il ricevitore
supporta**, altrimenti l'associazione fallirà; dopo aver cambiato modalità,
verificare attentamente ogni canale e in particolare il comportamento del failsafe.

- **ACCESS** — percorsi a 2.4GHz e 900MHz che lavorano in tandem sotto un unico insieme di
  controlli ACCESS. Fino a tre ricevitori in totale, in qualsiasi combinazione di 2.4GHz
  (24 canali) e 900MHz (16 canali); la telemetria di entrambe le bande è
  attiva simultaneamente, contrassegnata per banda. Una sorgente di telemetria **RX**
  indica quale ricevitore è attualmente la sorgente di telemetria attiva.
- **ACCST D16** — un singolo percorso a 2.4GHz, per i ricevitori della serie "X" legacy.
- **TD mode** — tandem 2.4GHz + 900MHz a bassa latenza e lunga portata per i ricevitori
  Tandem, 24 canali su ciascuna banda.

Le build del **firmware Flex** aggiungono una seconda colonna Type per commutare tra la modulazione
FLEX915M (915MHz in stile FCC) e FLEX868M (868MHz in stile LBT)
sotto una qualsiasi delle tre modalità precedenti — devono essere montate le antenne corrispondenti
a quella selezionata. Gli utenti UE possono usare 200/500mW sugli 868MHz; a 25mW
la telemetria viaggia sugli 868MHz, a 200/500mW passa ai 2.4GHz per
conformità normativa.

Ogni scelta di modalità/intervallo di canali comporta un compromesso sulla frequenza di aggiornamento — ad esempio con
ACCESS, 8 canali si aggiornano ogni 7ms, 16 ogni 14ms, 24 ogni 21ms
(a rotazione in blocchi di 8), ed è disponibile una **Racing mode** a 4ms sui
canali 1-8 con ricevitori compatibili (serie RS, v2.1.7+).

## Registrazione e associazione di un ricevitore (ACCESS) {: #registering-and-binding-a-receiver-access }

L'associazione di un ricevitore ACCESS avviene in due fasi — la **registrazione** deve
avvenire una sola volta per ogni coppia ricevitore/trasmettitore; l'**associazione** può essere ripetuta
successivamente in modalità wireless senza bisogno del pulsante bind.

**Fase 1 — Registrazione**:

1. Toccare **Register** (saltare completamente questo passaggio se il ricevitore è già
   registrato).
2. Tenere premuto il pulsante bind del ricevitore mentre lo si alimenta; attendere che entrambi
   i LED si accendano. La finestra di dialogo passa da "Waiting for receiver…" a
   "Receiver connected" e compila automaticamente il nome del ricevitore.
3. Confermare/modificare il **Registration ID** (per impostazione predefinita è l'Owner
   Registration ID indicato sopra — sono gli ID corrispondenti tra i trasmettitori a far
   funzionare Smart Share), il **Rx name** e lo **UID**. Lo UID distingue
   più ricevitori usati insieme in un unico modello — lasciarlo a 0 per un
   singolo ricevitore; con più ricevitori (ad es. uno per ogni blocco di 8 canali), è
   convenzionale usare 0/1/2. Lo UID non può essere riletto dal ricevitore
   in seguito, quindi conviene etichettarlo fisicamente.
4. Toccare **Register**, confermare "Registration ok", quindi spegnere il ricevitore
   — è registrato ma non ancora associato.

**Fase 2 — Associazione**:

!!! warning
    Non eseguire mai l'associazione con un motore elettrico collegato o un motore a scoppio in funzione.

1. Ricevitore spento; verificare di essere nella modalità del modulo corretta.
2. Toccare **RX1** (o 2/3) → **Bind**. Un avviso vocale ripetuto "Bind"
   conferma la modalità di associazione.
3. Alimentare il ricevitore **senza** toccare il suo pulsante bind; selezionarlo
   dall'elenco "Select device" che compare.
4. Confermare "Bind successful". Spegnere e riaccendere sia la radio sia il ricevitore —
   LED verde del ricevitore acceso e rosso spento significa che il collegamento è attivo. Non è necessario ripetere
   l'associazione a meno che uno dei due dispositivi non venga sostituito.
5. Ripetere per eventuali ricevitori aggiuntivi (RX2, RX3).

## Opzioni del ricevitore

Con il ricevitore alimentato, toccare il relativo pulsante RX per accedere a:

- **Options** — **Telemetry** (attiva/disattiva per questo ricevitore), **Reduced
  telemetry power 25mW** (rispetto ai normali 100mW — utile se i servi vicini
  captano interferenze RF), **High PWM Speed** (aggiornamento servi a 7ms invece
  di 18ms — verificare che i servi siano in grado di sostenerlo), **Telemetry port**
  (S.Port/F.Port/FBUS), **SBUS** (16 o 24 canali — ogni dispositivo SBUS collegato
  deve supportare SBUS-24 prima di abilitarlo) e **Channel
  Mapping** per rimappare i canali su specifici pin del ricevitore.
- **Share** — cede il ricevitore a un'altra radio ACCESS con un Owner Registration ID
  *diverso*. Sulla radio sorgente, toccare Share (il suo
  LED verde si spegne); sulla radio di destinazione, eseguire Bind normalmente — Share
  salta la nuova registrazione poiché l'ID viene trasferito automaticamente. Uscire sulla
  radio sorgente per terminare la condivisione; una nuova associazione lo riporta indietro. (Non è affatto necessario
  se tutte le radio condividono già lo stesso Owner Registration ID — basta eseguire
  l'associazione direttamente sulla radio che deve controllarlo.)
- **Reset bind** — ripulisce dopo uno Share e ripristina la propria associazione;
  spegnere e riaccendere il ricevitore in seguito.
- **Factory reset** — resetta il ricevitore e ne cancella lo UID,
  annullandone completamente la registrazione.

Con il ricevitore **spento**, lo stesso pulsante RX offre **Options** (attende
che il ricevitore si connetta), **Bind** (ad es. per riassociare un ricevitore
precedentemente associato altrove) e **Clear** (equivalente a Reset bind).

## Ricevitori ridondanti {: #redundant-receivers }

Un secondo ricevitore può essere associato a uno slot RX libero per ridondanza — 2.4G
e 900M possono fare da backup l'uno all'altro. La ridondanza FrSky valuta
**frame per frame**, utilizzando sempre il miglior frame disponibile (failover attivo/attivo),
quindi il controllo può passare da un ricevitore all'altro frame dopo frame secondo necessità.

1. Collegare l'uscita SBUS Out del ricevitore ridondante all'ingresso SBUS In del ricevitore principale.
2. Abilitare il corrispondente modulo RF interno (ad es. 900M) e impostarne
   antenna/potenza.
3. Registrare il nuovo ricevitore (se non già fatto), quindi associarlo allo slot
   RX libero come descritto sopra.
4. Verificare che il suo LED verde sia acceso — ora è elencato come ricevitore
   ridondante.

## Failsafe {: #failsafe }

I dati di failsafe vengono ritrasmessi dal trasmettitore circa ogni 10 secondi; sui
ricevitori TD/TW/AP/AP Plus vengono inoltre salvati lato ricevitore, così da sopravvivere
a un riavvio del ricevitore. Ricontrollare attentamente il failsafe dopo qualsiasi
aggiornamento del firmware del ricevitore che introduca questo comportamento.

- **Hold** — mantiene le ultime posizioni dei canali ricevute.
- **Custom** — per canale: **Not Set**, **Hold**, **Custom** (un valore
  fisso — toccare l'icona a freccia per catturare il valore corrente, oppure inserirne uno
  direttamente) o **No Pulses**.
- **No Pulses** — interrompe del tutto gli impulsi, per flight controller dotati di
  un proprio comportamento di return-to-home in caso di perdita di segnale.
- **Receiver** — (ricevitori serie X o successivi) imposta invece il failsafe sul
  ricevitore stesso.

!!! warning
    Testare accuratamente l'impostazione di failsafe scelta prima di farvi
    affidamento.

## Prova di portata {: #range-check }

Eseguirla sul campo prima di ogni sessione di volo con una configurazione nuova o modificata.
Selezionando **Range Check** si riduce deliberatamente la potenza di trasmissione (un
avviso vocale ripetuto conferma la modalità) e vengono mostrati VFR%/RSSI in tempo reale per
valutare la qualità del collegamento. Il livello di potenza in prova di portata di FrSky è di circa
−10dB rispetto al normale livello operativo di +20dB; a 1m di altezza sia per
la radio sia per il ricevitore, ci si aspetta un allarme critico intorno ai 30m — una distanza
inferiore in condizioni normali può indicare un problema.

Con più ricevitori associati, i dati della prova di portata sono mostrati per un ricevitore attivo
alla volta per banda — spegnendo quello attualmente attivo si consente al successivo
(nell'ordine di priorità 0/1/2, indicato tramite il sensore **RX**) di subentrare, così da
poter controllare ciascuno a turno.

## Moduli RF esterni e di terze parti

I moduli esterni FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
seguono lo stesso schema Register/Bind del modulo interno, con
numero di canali, livelli di potenza e requisiti di antenna specifici per protocollo
— consultare il manuale del modulo specifico per i valori esatti.

**ELRS** (ExpressLRS) è supportato sia tramite la modalità ELRS del modulo TWIN Lite Pro
sia tramite moduli ELRS originali (che richiedono l'installazione dello script Lua ELRS
in `scripts/elrs` prima di comparire come opzione di modulo). Dodici
canali; le impostazioni principali sono **Packet Rate** (compromesso tra latenza e portata),
**Telemetry Ratio** (frequenza di invio della telemetria, da 1:1 a 1:128),
**Switch Mode** (**Hybrid** — la maggior parte dei canali ausiliari ridotta a 2–3 posizioni
per una latenza inferiore — oppure **Wide** — risoluzione completa a 64–128 passi),
**Model Match** e **Tx Power** (10mW–1000mW, con **Dynamic Power** opzionale per
scalare automaticamente in base alla qualità del collegamento — richiede la telemetria abilitata).

I **moduli di terze parti** (attualmente Ghost, Multi-protocol, Crossfire, oltre
a ELRS) richiedono ciascuno il proprio script Lua installato dall'utente — vedere
le note su `scripts/` in [Screenshot Pipeline](../contributing/screenshot-pipeline.md)
e il thread *Third-Party External Modules* su rcgroups. La voce di un
modulo compare nella schermata RF solo dopo che il relativo script è stato
installato. Il modulo Multi-protocol (IRX4 Lite) può inoltre essere
aggiornato via firmware direttamente da [File Manager](../system-setup/file-manager.md):
copiare il file del firmware in `Firmware/`, quindi selezionare **Flash external
multimodule**.
