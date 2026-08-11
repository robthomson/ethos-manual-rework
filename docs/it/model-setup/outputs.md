---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Uscite

![Uscite](../assets/model-outputs.png)

Le Uscite sono il confine tra la pura "logica" dei [Mix](mixes.md) e il
mondo fisico — servi, rinvii, superfici di controllo, attuatori,
trasduttori. È qui che finecorsa, inversione, centraggio e curve di
correzione vengono adattati a ciò di cui il modello ha effettivamente
bisogno dal punto di vista meccanico. Ogni canale di uscita corrisponde a
un'uscita servo del ricevitore (CH1 → connettore servo n. 1, con le
impostazioni di protocollo predefinite).

Ethos lavora in percentuali, ma i servi sono in ultima analisi pilotati
dalla larghezza dell'impulso PWM in microsecondi:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Un canale **privo di mix attivi** emette il valore neutro (0% / 1500µs) —
    ciò include un canale i cui unici mix siano al momento inattivi.
    Assicurarsi che ogni canale effettivamente utilizzato disponga sempre di
    un mix attivo a supportarlo. Su un canale del gas, in particolare, il
    valore neutro corrisponde a **metà gas**.

La schermata Uscite mostra due barre per canale: la barra inferiore
(verde) è il valore del mixer per quel canale, la barra superiore
(arancione) è il valore post-Uscite effettivamente inviato al ricevitore
(sia in % che in µs). I limiti Min/Max compaiono come sezioni in grigio
della barra arancione. I canali non attualmente trasmessi al modulo RF
hanno uno sfondo più scuro. Piccole icone compaiono su un canale quando le
sue impostazioni di Direzione, Curva, Rallentamento o Bilanciamento sono
state modificate rispetto ai valori predefiniti, così da individuare a
colpo d'occhio i canali non predefiniti.

!!! tip
    Una pressione prolungata di `ENT` dalla schermata Mix o Fasi di volo
    porta direttamente qui.

## Modifica di un canale {: #editing-a-channel }

![Modifica uscita profondità](../assets/model-outputs-elevator-edit.png)
![Modifica uscita gas](../assets/model-outputs-throttle-edit.png)

Toccare un canale per aprirlo. Un'anteprima nella parte superiore mostra
il valore del mix (verde) confrontato con il valore di uscita (arancione),
con un piccolo indicatore bianco per i punti Min/Max.

- **Nome** — modificabile.
- **Direzione** — inverte l'uscita del canale, tipicamente per invertire il
  senso di rotazione del servo. Visualizzata come icona a doppia freccia sul
  canale. Questo **non** influisce sui mix che lo alimentano e **non**
  inverte i limiti Min/Max.
- **Min/Max** — limiti rigidi che non vengono mai superati — da impostare
  per evitare forzature meccaniche. Agiscono come impostazioni di
  finecorsa/guadagno: ridurli riduce la corsa anziché causare troncamenti.
  Il valore predefinito è ±100%, regolabile fino a ±150%. Durante la
  regolazione, l'estremo verso cui ci si sta muovendo viene mostrato in
  grassetto (ad esempio, spingendo in avanti lo stick della profondità il
  valore Max diventa grassetto, a conferma che è quello l'estremo che si sta
  impostando).

  ![Avviso ridondanza SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Ridondanza SBUS"
      Una configurazione con ridondanza tramite SBUS non può muovere un servo
      oltre circa ±125%. I campi Min/Max hanno di per sé intervalli
      asimmetrici (−150–0% e 0–150%) — se pilotati da una
      [Variabile](variables.md), assegnare a tale variabile un intervallo
      identico oppure impostare **Ignora intervallo** (vedere [opzioni della
      sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      altrimenti la conversione automatica dell'intervallo produrrà valori
      inattesi. Se l'uscita del ricevitore principale supera il 125% e questo
      entra in failsafe, il ricevitore ridondante che subentra tramite SBUS la
      limita nuovamente al 125%.

- **Centro/Subtrim** — sposta l'uscita, tipicamente per centrare la squadretta
  di un servo; i finecorsa non ne sono influenzati.

  !!! warning
      Non usare il subtrim per spostamenti ampi — introduce un notevole
      differenziale nella risposta del servo. Per qualsiasi cosa oltre il
      centraggio fine, utilizzare invece un **mix di offset**.

- **Centro PWM** — analogo al subtrim, ma sposta *l'intera* banda di corsa del
  servo, inclusi i limiti rigidi, agendo di fatto all'interno del servo stesso
  anziché essere visualizzato nel monitor dei canali. In questo modo il
  centraggio meccanico rimane distinto dalla trimmatura.
- **Curva** — associa una curva Expo o personalizzata (esistente o nuova, con
  una scorciatoia **Modifica** una volta impostata) per correggere la risposta
  reale — ad esempio per mantenere i flap sinistro e destro perfettamente
  allineati. Visualizzata come icona di curva sul canale.
- **Rallentamento su/giù** — rallenta la risposta dell'uscita alle variazioni
  dell'ingresso, espresso in secondi per percorrere 0→100% — ad esempio per
  rallentare un carrello retrattile azionato da un normale servo proporzionale.
  Visualizzato come icona di orologio sul canale. (Un **ritardo**, concetto
  distinto dal rallentamento, è disponibile negli [interruttori
  logici](logical-switches.md).)

## Scambia canali {: #swap-channels }

![Scambia canali](../assets/model-outputs-swap-channels.png)
![Scelta del canale da scambiare](../assets/model-outputs-swap-channels-select.png)

Scambia due canali di uscita. La finestra di dialogo si apre con il canale
corrente già precompilato; selezionare l'altro e confermare — lo scambio è
immediato e ogni mix che fa riferimento a uno dei due canali viene
aggiornato di conseguenza.

## Ripristino impostazioni

![Ripristino canale](../assets/model-outputs-reset-select.png)

Riporta ogni parametro di un canale ai valori predefiniti — utile prima di
riutilizzare un canale per un'altra funzione, con una finestra di conferma
per evitare errori.

## Bilanciamento canali {: #balance-channels }

![Scelta dei canali da bilanciare](../assets/model-outputs-balance-choose_channels.png)
![Scelta di CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Bilancia una coppia (o fino a 4) di canali affinché si muovano all'unisono —
ad esempio, flap che non si muovono in modo solidale possono indurre un
rollio indesiderato; motori sbilanciati su un modello plurimotore possono
indurre un'imbardata indesiderata. Ethos costruisce una curva differenziale
di bilanciamento per ciascun canale selezionato; confrontando le posizioni
fisiche delle superfici in ogni punto della curva è possibile regolarle
affinché coincidano, ottenendo superfici perfettamente allineate.

**Prima di bilanciare**, nell'ordine:

1. Impostare le direzioni dei servi per una corsa corretta.
2. Con i mix in posizione neutra, utilizzare eventualmente il **Centro PWM**
   per allineare le squadrette dei servi.
3. Impostare Min/Max e Subtrim.
4. Configurare eventuali altre curve.
5. Configurare il Rallentamento.
6. *Solo allora* bilanciare ed equalizzare lungo l'intero campo di corsa.

**Utilizzo**: scegliere i canali da bilanciare e l'ordine in cui
visualizzarli —

![CH7/CH6 selezionati](../assets/model-outputs-balance-ch7-and-ch6.png)

— l'uscita del mix sull'asse X, il differenziale di regolazione del
bilanciamento sull'asse Y. Toccare il grafico di un canale (o selezionarlo e
premere `ENT`) per modificarne la curva di bilanciamento; `PAGE` consente di
passare da un canale all'altro durante la modifica:

![Editor della curva di bilanciamento](../assets/model-outputs-balance-curve-edit.png)

Comandi dell'editor:

- **Sorgente** — normalmente la sorgente (o le sorgenti) del mix stesso,
  oppure qualsiasi altro ingresso analogico comodo; **Ingresso analogico
  automatico** acquisisce come X il primo stick/slider/potenziometro che si
  muove, sia nel grafico sia nel modello stesso.
- **Magnete** — aggancia automaticamente la regolazione dell'encoder rotativo
  al punto di curva più vicino sull'asse X:

  ![Magnete disattivato](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Magnete attivato](../assets/model-outputs-balance-ch6-magnet-on.png)

  L'ingresso deve comunque essere mosso per allineare X a un punto della
  curva prima di poterlo regolare.
- **Blocco** — si attiva toccandone l'icona o premendo `ENT` in modalità di
  modifica del grafico; blocca tutti gli ingressi in modo da poter rilasciare
  lo stick e osservare le superfici di controllo mentre si regola la curva.
- **Configurazione** — modifica il numero di punti per canale (tutti o
  singolarmente) e se ciascuna curva debba essere smussata.
- **Guida** (`?`, anche il tasto `MDL`) — apre la guida integrata.

**Multicanale**: è possibile bilanciare insieme fino a 4 canali —

![Bilanciamento a 4 canali](../assets/model-outputs-balance-ch2-9-8-1.png)

Una volta impostata, una curva di bilanciamento può essere rivista,
modificata o cancellata dalla pagina di configurazione del canale stesso —
un'icona di bilanciamento la segnala sul grafico del canale (affiancata
anche da un'icona di Direzione, se anch'essa è diversa dal valore
predefinito).
