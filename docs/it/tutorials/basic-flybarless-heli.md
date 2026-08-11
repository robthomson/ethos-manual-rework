---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Esempio di elicottero flybarless di base

Configurazione di un elicottero flybarless (FBL) di base, prendendo come
esempio un controller quale lo Spirit. A differenza di un modello ad ala
fissa, un elicottero è intrinsecamente instabile: il controller FBL
utilizza giroscopi (che misurano il tasso di rotazione attorno a un asse)
e accelerometri (che rilevano movimento e orientamento) per calcolare le
correzioni di imbardata, beccheggio e rollio tramite un anello di
controllo PID (Proportional Integral Derivative) opportunamente regolato,
bilanciando stabilità, reattività e overshoot in funzione delle
caratteristiche fisiche ed elettriche del singolo elicottero.

Questo tutorial si occupa solo della **programmazione radio**: per il
resto della configurazione fare riferimento alla documentazione della
propria unità FBL, presupponendo già una buona conoscenza del
funzionamento degli elicotteri.

!!! danger
    Prima di iniziare, per evitare lesioni, rimuovere le pale del rotore.

## Passo 1. Conferma le impostazioni del sistema

Ordine dei canali **AETR** e **[Primi quattro canali
fissi](../system-setup/controls.md#first-four-channels-fixed)** su
**OFF**: le unità Spirit FBL si aspettano i canali SBUS esattamente in
questo ordine (nonostante l'unità utilizzi il TAER nella propria
configurazione). Registrare (se il ricevitore è ACCESS) e collegare il
ricevitore tramite [RF System](../model-setup/rf-system.md).

## Passo 2. Identificare i servi/canali necessari

| Funzione | Canale |
|---|---|
| Rollio (alettone) | — |
| Passo (elevatore) | — |
| Gas | — |
| Imbardata (timone) | — |
| Guadagno del giroscopio | 5 |
| Passo collettivo | 6 |
| Banco di impostazioni | 7 |
| Rescue | 8 |

## Passo 3. Crea un nuovo modello

![Creazione guidata del modello elicottero](../assets/tut-heli-eg-wiz-create-heli.png)

Da [Selezione del modello](../model-setup/model-select.md),
creare/selezionare una categoria Heli, avviare la procedura guidata e
scegliere **Flybarless**:

![Selezione FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Nome del modello](../assets/tut-heli-eg-wiz-name.png)

Definire un nome e un'immagine per il modello.

## Passo 4. Rivedere e configurare i mix

![Panoramica dei mix](../assets/tut-heli-eg-mixes.png)

La procedura guidata crea Alettoni, Elevatori, Motore e Timone nella
sequenza AETR, il Pitch sul canale 6 e il Bank FBL sul canale 7:

![Mix del pitch](../assets/tut-heli-eg-mixes-pitch.png)

Verificare che il canale 6 sia il Pitch collettivo. Occorre aggiungere
manualmente altri due canali utilizzando i [Free
Mix](../model-setup/mixes.md#mix-libraries): **Guadagno del giroscopio**
(canale 5) e **Rescue/Stabi** (canale 8).

**Alettone/Elevatore/Timone**: non è necessario aggiungere nulla; i rates
e l'expo sono gestiti dall'unità FBL, quindi la radio passa semplicemente
gli ingressi di controllo lineare all'unità FBL.

![Mix degli alettoni](../assets/tut-heli-eg-mixes-ail.png)

**Pitch collettivo**: è solo una curva lineare, quindi è sufficiente
confermare il canale di uscita (normalmente il canale 6). Come sopra, i
rates e l'expo sono gestiti dall'unità FBL e non qui.

**Bank FBL**: i tre banchi di impostazioni dello Spirit (per passare da
uno stile di volo all'altro, per ottenere un diverso guadagno del sensore
a bassi o alti regimi, oppure per principianti, acro o 3D — o
semplicemente per mettere a punto le impostazioni) assegnati a un
interruttore a 3 posizioni, ad esempio SE:

![Mix del banco](../assets/tut-heli-eg-mixes-bank.png)

**Guadagno del giroscopio**: aggiungerlo come Free Mix dopo l'ultimo
canale. Il guadagno è in genere un valore fisso: impostare la
**sorgente** su Valore speciale 0, comporre il valore di guadagno
richiesto utilizzando l'**offset** (il valore finale può essere
determinato in volo) e assegnare il canale di uscita 5:

![Mix del guadagno del giroscopio](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Configurare le fasi di volo

![Fasi di volo](../assets/tut-heli-eg-flight-modes.png)

Tre [fasi di volo](../model-setup/flight-modes.md): rinominare quella
predefinita in **Normal** e aggiungere **Idle Up 1**/**Idle Up 2**
sull'interruttore SD.

### Configurare il mix del gas

Tre curve del gas, una per ciascuna fase di volo, ognuna una [curva
personalizzata](../model-setup/curves.md):

- **Normal**: viene utilizzata per lo spool up e il decollo, quindi la
  curva inizia a −100% (motore spento) e poi aumenta dolcemente. Una
  curva a 7 punti con **Smooth** attivo dà un buon risultato; i valori
  finali possono essere determinati in volo.

  ![Curva Normal](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1**: viene utilizzata per la maggior parte dei voli; la curva
  rettilinea significa un'impostazione costante del gas per far girare i
  rotori a una velocità costante, mentre il movimento dell'elicottero è
  controllato dal Pitch collettivo, dagli alettoni (rollio) e
  dall'elevatore (beccheggio). Non ci deve essere un grande salto tra
  Normal e Idle Up 1, in modo che la transizione avvenga senza problemi.
  (La maggior parte delle unità FBL offre anche una funzione **Governor**,
  che assicura che la velocità del rotore sia mantenuta costante anche
  durante le manovre di volo aggressive: consultare il manuale dell'unità
  FBL.)

  ![Curva Idle Up 1](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2**: utilizzata per voli più aggressivi (acrobatici e 3D);
  anche in questo caso il valore finale può essere determinato in volo.

  ![Curva Idle Up 2](../assets/tut-heli-eg-curves-iup2.png)

![Curve del gas nei mix](../assets/tut-heli-eg-mixes-thr-curves.png)

**Taglio gas**: assegnare ad esempio l'interruttore SG-up con **Sticky**
attivo: il gas verrà tagliato non appena si porta l'interruttore in
posizione 'Up' e, a causa dell'impostazione Sticky, può essere riarmato
solo con lo stick del gas in posizione bassa (off).

![Taglio gas](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescue/Stabi**: in modo analogo, può essere assegnato ad esempio
all'interruttore SA sul canale 8.

![Mix finali](../assets/tut-heli-eg-mixes-final.png)

## Passo 5. Impostazione FBL

1. **Installare lo strumento di configurazione FBL**, ad esempio il
   software Spirit Settings, sul PC.
2. **Collegare il ricevitore all'unità FBL** seguendo la sezione
   Cablaggio del relativo manuale: tipicamente l'uscita SBUS del
   ricevitore va collegata alla porta RUD dell'unità FBL (alcuni modelli
   Spirit richiedono un adattatore SBUS), oppure si può utilizzare la
   porta F.Port1/FBUS.
3. **Collegare l'unità FBL al PC**, utilizzando il cavo in dotazione o
   via Bluetooth, come indicato nel relativo manuale.

   !!! danger
       Non collegare ancora nessun servo!

4. **Aggiornare il firmware dell'FBL** alla versione più recente, se
   necessario, dalla scheda Update dello strumento.
5. **Configurazione generale** (scheda Generale di Spirit Settings):
   - Tipo di ricevitore: **Futaba SBUS** oppure **FrSky F.Port** a
     seconda dei casi, quindi riavviare il sistema.
   - Mappatura dei canali (con l'ordine AETR della procedura guidata):

     | Funzione | Canale |
     |---|---|
     | Gas | 1 |
     | Alettone | 2 |
     | Elevatore | 3 |
     | Timone | 4 |
     | Gyro | 5 |
     | Pitch | 6 |
     | Bank | 7 |
     | Rescue/Stabi | 8 |

     (Questo ordine dei canali è dovuto al fatto che l'unità Spirit fa
     delle ipotesi sulla posizione dei canali nel flusso di dati SBUS.)

6. **Limiti del canale** (scheda Diagnostica): per un corretto
   funzionamento dell'unità FBL è necessario calibrare i limiti dei
   canali della radio e controllare i centri.

   - Azzerare innanzitutto tutti i subtrim e i trim sulla radio.
   - Portare lo stick del Pitch collettivo in posizione centrale per
     ottenere un'uscita di esattamente 1500µs nella pagina
     [Uscite](../model-setup/outputs.md).
   - Accendere l'unità FBL e controllare che i canali di alettoni,
     elevatore, passo e timone siano centrati allo 0% nella scheda
     Diagnostica (l'unità FBL rileva automaticamente la posizione neutra
     durante ogni inizializzazione).
   - Spostare ciascun comando fino ai suoi limiti e regolare le
     corrispondenti impostazioni **Min**/**Max** nella pagina Uscite
     finché la scheda Diagnostica non indica esattamente +100%/−100%,
     verificando anche che la direzione del movimento delle barre
     corrisponda a quella degli stick.

   !!! warning
       Non utilizzare mai le funzioni di subtrim o trim su questi canali:
       l'unità Spirit FBL le considera come un comando di ingresso e non
       come una calibrazione.

7. Regolare il valore dell'**offset** nel mix del Guadagno del giroscopio
   per garantire il blocco della direzione (Heading Lock).

Dopo queste regolazioni, tutto è configurato per quanto riguarda il
trasmettitore: si può continuare con il resto della configurazione
dell'FBL come indicato nel manuale dell'unità FBL.
