---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Uscite

![Uscite](../assets/model-outputs.png)

La sezione Uscite è l'interfaccia tra la pura "logica" dei [Mix](mixes.md) e il
mondo reale — servi, collegamenti, superfici di controllo, attuatori e
trasduttori. È qui che i punti finali, l'inversione, la centratura e le curve
di correzione vengono adattati alle caratteristiche meccaniche del modello.
Ogni canale di uscita corrisponde a un'uscita servo del ricevitore (CH1 →
connettore del servo numero 1, con le impostazioni di protocollo predefinite).

Sebbene Ethos sia configurato utilizzando le percentuali, i servi sono in
definitiva pilotati da un segnale PWM la cui larghezza d'impulso è espressa in
microsecondi:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Un canale **privo di mix attivi** avrà un'uscita in posizione neutra
    (0% / 1500µs) — lo stesso vale quando il mix o i mix di un canale sono
    inattivi. È quindi necessario prestare attenzione affinché i canali
    utilizzati abbiano sempre un mix attivo. Un canale dell'acceleratore in
    posizione neutra sarà a **metà accelerazione**.

La schermata Uscite mostra due grafici a barre per ogni canale: la barra
inferiore (verde) mostra il valore dei mix per il canale, mentre quella
superiore (arancione) mostra il valore effettivo dell'uscita dopo
l'elaborazione delle uscite, ovvero ciò che viene inviato al ricevitore (in
termini sia di % che di µs). Le impostazioni minime e massime del canale sono
indicate dalle sezioni in grigio nella barra superiore (arancione). I canali
che non vengono trasmessi al modulo RF sono indicati con uno sfondo più scuro.
Sul display di un canale appaiono delle piccole icone quando sono state
modificate le impostazioni predefinite per la Direzione, la Curva, il Rallenta
o il Bilanciamento, così da individuare a colpo d'occhio i canali non
predefiniti.

!!! tip
    Una pressione prolungata di `ENT` dalle schermate Mix o Fasi di Volo porta
    direttamente qui.

## Configurazione delle uscite {: #editing-a-channel }

![Modifica uscita elevatore](../assets/model-outputs-elevator-edit.png)
![Modifica uscita gas](../assets/model-outputs-throttle-edit.png)

Tocca il canale di uscita da modificare o rivedere. Nella parte superiore
della schermata viene visualizzata un'anteprima del canale: il valore del mix
è indicato in verde, mentre il valore dell'uscita del canale è indicato in
arancione, con un piccolo indicatore bianco che indica i punti Min/Max.

- **Nome** — può essere modificato.
- **Direzione** — cambia la direzione dell'uscita del canale, in genere per
  invertire la direzione del servo. Quando è abilitata, nella visualizzazione
  del grafico del canale viene visualizzata un'icona a doppia freccia. Tieni
  presente che questo **non** influisce sui mix che pilotano l'uscita e
  **non** cambia i limiti di min/max.
- **Min/Max** — sono limiti "rigidi", cioè non potranno mai essere superati:
  devono essere impostati in modo da evitare un vincolo meccanico. Servono
  come impostazioni di guadagno o "punto finale", quindi la riduzione di
  questi limiti ridurrà la corsa piuttosto che indurre il clipping. I limiti
  sono predefiniti a ±100%, ma possono essere aumentati fino a ±150%. Quando
  si regolano i limiti di uscita min/max, l'estremità da regolare è
  evidenziata in grassetto (ad esempio, spostando leggermente in avanti lo
  stick dell'elevatore, il valore massimo viene mostrato in grassetto per
  indicare che è il punto finale da regolare).

  ![Avviso ridondanza SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Ridondanza SBUS"
      Quando si utilizza un sistema di ridondanza con SBUS, non è possibile
      effettuare movimenti del servo superiori a circa ±125%. I parametri
      Min/Max hanno di per sé intervalli asimmetrici (da −150% a 0% e da 0% a
      +150%): se vengono pilotati da una [Var](variables.md), a meno che il
      Var non abbia un intervallo identico, sarà necessario impostare
      l'intervallo del Var come **ignorato** (vedi [opzioni della
      sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      per evitare valori inaspettati dovuti alla conversione dell'intervallo.
      Se si utilizza più del 125% sul ricevitore principale e questo entra in
      failsafe, le posizioni del servo ricevute dal ricevitore ridondante via
      SBUS sono limitate al 125%.

- **Centro/Subtrim** — si usa per introdurre un offset sull'uscita, in genere
  per centrare un braccio di un servo; nota che gli endpoint non vengono
  influenzati.

  !!! warning
      Non essere tentato di usare il Subtrim per aggiungere grandi offset: si
      creerà un grande differenziale nella risposta del servo. Per qualsiasi
      cosa oltre la centratura fine, il modo corretto è aggiungere un **mix di
      offset**.

- **Centro PWM** — si tratta di un'operazione simile al subtrim, con la
  differenza che una regolazione effettuata qui sposterà *l'intera* banda di
  movimento del servo (compresi i limiti rigidi). Questa regolazione non sarà
  visibile sul monitor del canale perché viene effettivamente effettuata nel
  servo. In questo modo si separa la funzione di centratura da quella di
  trimming.
- **Curva** — permette di selezionare una curva Expo o una curva
  personalizzata (esistente o nuova, con il pulsante **Modifica** una volta
  configurata) per condizionare l'uscita e correggere eventuali problemi di
  risposta nel mondo reale, ad esempio per garantire che i flap destro e
  sinistro seguano con precisione. Quando è abilitata, l'icona di una curva
  viene visualizzata nel grafico del canale.
- **Rallenta su/giù** — la risposta dell'uscita può essere rallentata rispetto
  alla variazione dell'ingresso; il valore è il tempo in secondi che l'uscita
  impiega per passare da 0 a +100%. Può essere utilizzato, ad esempio, per
  rallentare i carrelli retrattili azionati da un normale servo proporzionale.
  Quando è configurato, l'icona dell'orologio viene visualizzata nel grafico
  del canale. (La funzione di **ritardo**, concetto distinto dal rallentamento,
  è disponibile tra gli [interruttori logici](logical-switches.md).)

## Scambio di canali {: #swap-channels }

![Scambio canali](../assets/model-outputs-swap-channels.png)
![Scelta del canale da scambiare](../assets/model-outputs-swap-channels-select.png)

Questa funzione permette di scambiare due canali di uscita. La finestra di
dialogo di scambio si apre con il primo canale già compilato: seleziona il
canale da scambiare e conferma — lo scambio avviene immediatamente e tutti i
mix che fanno riferimento a uno dei due canali verranno regolati di
conseguenza.

## Ripristina le impostazioni

![Reset del canale](../assets/model-outputs-reset-select.png)

Il reset delle impostazioni cancella tutti i parametri del canale di uscita
riportandoli ai valori predefiniti — utile prima di riutilizzare un canale per
qualcos'altro. Una finestra di conferma eviterà un reset accidentale.

## Canali di bilanciamento {: #balance-channels }

![Scelta dei canali da bilanciare](../assets/model-outputs-balance-choose_channels.png)
![Scelta di CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Questa funzione ti permette di bilanciare coppie selezionate o un gruppo di
massimo 4 canali per garantire che si muovano all'unisono — ad esempio, uno
sbilanciamento dei flap può causare un rollio indesiderato, mentre uno
sbilanciamento delle manette sui modelli multimotore può causare un'imbardata
indesiderata. Ethos crea automaticamente una curva di bilanciamento
differenziale per ogni canale selezionato; confrontando le posizioni fisiche
delle superfici di controllo in ogni punto delle curve, è possibile regolarle
facilmente in modo che siano uguali. Il risultato finale è un perfetto
tracciamento delle superfici.

**Prima di bilanciare i canali**, nell'ordine:

1. Imposta le direzioni del servo per una corretta corsa delle superfici.
2. Con i mix in posizione neutra, usa facoltativamente il **Centro PWM** per
   impostare le squadrette dei servi ad angolo retto.
3. Configura i limiti Min/Max e il Subtrim.
4. Configura qualsiasi altra curva.
5. Configura il Rallenta.
6. *Solo allora* procedi a bilanciare ed equalizzare le superfici di controllo
   in più punti della corsa.

**Come si usa**: scegli i canali da bilanciare e l'ordine in cui desideri
visualizzarli —

![CH7/CH6 selezionati](../assets/model-outputs-balance-ch7-and-ch6.png)

— le uscite del mix sono visualizzate lungo gli assi X, mentre i valori
differenziali di regolazione del bilanciamento sono visualizzati sugli assi Y.
Tocca il grafico di un canale (o scorrilo e premi `ENT`) per modificare la
curva di bilanciamento; il tasto `PAGE` permette di passare da un canale
all'altro durante la modifica:

![Editor della curva di bilanciamento](../assets/model-outputs-balance-curve-edit.png)

Pulsanti del menu:

- **Sorgente** — possono essere utilizzate le sorgenti configurate nei mix dei
  canali o, opzionalmente, qualsiasi altro ingresso analogico comodo. Se
  selezioni l'opzione **Ingresso analogico automatico**, il primo stick,
  cursore o potenziometro che sposti sarà utilizzato come sorgente per X, non
  solo nel grafico, ma anche nel modello.
- **Magnete** — se abilitato, il punto più vicino alla curva sull'asse X verrà
  selezionato automaticamente per la regolazione con l'encoder rotativo:

  ![Magnete disattivato](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Magnete attivato](../assets/model-outputs-balance-ch6-magnet-on.png)

  L'ingresso deve comunque essere regolato per allineare il valore X con un
  punto della curva prima di effettuare la regolazione.
- **Blocco** — toccando l'icona o premendo il tasto `ENT` mentre sei in
  modalità di modifica del grafico, la modalità di blocco viene attivata o
  disattivata; tutti gli input sono bloccati in modo da poter rilasciare
  l'input dello stick, consentendoti di osservare le superfici di controllo
  mentre regoli la curva.
- **Configurazione** — permette di modificare il numero di punti di tutte le
  curve, o solo di alcune, e di scegliere se smussarle o meno.
- **Aiuto** (`?`, richiamabile anche con il tasto `MDL`) — richiama il file di
  aiuto.

**Opzione multicanale**: è possibile bilanciare fino a 4 canali
contemporaneamente —

![Bilanciamento a 4 canali](../assets/model-outputs-balance-ch2-9-8-1.png)

Una volta che un canale è stato bilanciato, la sua curva di bilanciamento può
essere rivista, modificata o cancellata dalla pagina di configurazione del
canale stesso — sul grafico del canale viene visualizzata un'icona di
bilanciamento (affiancata anche dall'icona della Direzione, se anch'essa è
diversa dal valore predefinito).
