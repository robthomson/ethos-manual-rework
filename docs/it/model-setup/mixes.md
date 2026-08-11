---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mix

![Icona Mix](../assets/model-icon-mixes.png)

I mix sono il cuore della programmazione dei modelli in Ethos: è qui che gli
ingressi (stick, interruttori, sensori, qualsiasi cosa raggiungibile da una
[sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source))
vengono instradati, modellati e combinati sui canali di uscita. Si possono
definire fino a 120 mix per ogni modello.

![Tabella dei mix](../assets/model-mixes.png)

Se un modello è stato creato con la procedura guidata **Selezione modello**, i
suoi mix di base (alettone, elevatore, Gas - Throttle, timone e tutto ciò che la
cellula richiede) sono già presenti qui. Selezionando un mix e premendo `ENT` si
apre un menu contestuale che consente di modificarlo, aggiungere un nuovo mix,
passare alla [vista per canale](#per-channel-view), riordinarlo, duplicarlo o
cancellarlo. I mix inattivi sono visualizzati in grigio e la cancellazione
richiede sempre una conferma preventiva.

## Anatomia di un mix {: #anatomy-of-a-mix }

Ogni mix condivide lo stesso insieme di campi, indipendentemente dalla libreria
di provenienza. Il mix **alettone** ne è un esempio rappresentativo: i mix di
elevatore e timone hanno una struttura identica.

![Mix alettone](../assets/model-mixes-ail-edit.png)

![Editor del mix alettone](../assets/model-mixes-ail.png)

**Nome** — per impostazione predefinita corrisponde al tipo di mix ed è
modificabile.

**Condizione attiva** — la condizione attiva predefinita è *Sempre acceso*. Può
essere condizionata scegliendo tra posizioni di interruttori o pulsanti,
interruttori di funzione, interruttori logici, fasi di volo, un evento di
sistema come il taglio o il mantenimento del Gas - Throttle oppure le posizioni
dei trim; in tal caso il mix si applica solo finché la condizione è vera.

**Fasi di volo** — se sono state definite delle fasi di volo, il mix può inoltre
essere condizionato a una o più di esse.

**Curva** — l'opzione curva standard è **Expo**, che per impostazione
predefinita ha un valore pari a 0, il che significa che la risposta è lineare
(cioè non c'è curva). Un valore positivo ammorbidisce la risposta intorno allo
0, mentre un valore negativo la rende più netta:

![Curva Expo](../assets/model-mixes-ail-expo.png)

È inoltre possibile selezionare qualsiasi curva definita in precedenza in
[Curve](curves.md). Su un singolo mix si possono specificare fino a 6 curve,
ciascuna con una propria condizione: se più di una condizione è vera, prevale la
curva più in alto nell'elenco. Nota che le curve vengono applicate **prima**
dell'escursione.

**Escursione / Rates** — una o più righe di escursione, ciascuna eventualmente
condizionata da un interruttore, un interruttore di funzione, un interruttore
logico, una posizione di trim o una fase di volo. La prima riga è quella
predefinita, attiva ogni volta che non è soddisfatta la condizione di nessun'altra
riga:

![Escursioni dell'alettone](../assets/model-mixes-ail-weight.png)

Anziché una percentuale fissa, un'escursione può essere pilotata da una
[sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source),
ad esempio un potenziometro, per regolare l'escursione in volo:

![Escursione pilotata da una sorgente](../assets/model-mixes-ail-diff.png)

**Differenziale** (da -100 a +100, predefinito 0) — dà più corsa in una
direzione rispetto all'altra. Per gli alettoni è il classico accorgimento di una
maggiore corsa verso l'alto rispetto a quella verso il basso, per ridurre
l'imbardata inversa. Viene visualizzato solo quando il mix comanda più di un
canale di uscita; nello specifico, il differenziale ha senso solo con una
configurazione di uscita di tipo coda a V o a doppio alettone.

**Numero di canali / uscite** — il conteggio dei canali definisce quanti canali
di uscita comanda questo mix e a quali uscite fisiche sono assegnati:

![Numero di canali](../assets/model-mixes-ail-ch-count.png)

Una pressione prolungata di `ENT` su un canale di uscita in un altro punto
dell'interfaccia (ad esempio in [Uscite](outputs.md)) riporta direttamente a
questa pagina.

## Il mix Gas - Throttle

Il mix Gas - Throttle è un mix analogo a quelli di alettone/elevatore/timone,
con in più le opzioni di sicurezza specifiche per il motore.

![Mix Gas - Throttle](../assets/model-mixes-thr.png)

**Ingresso** — la sorgente del Gas - Throttle, normalmente lo stick del gas, ma
sostituibile con un potenziometro, uno slider, un interruttore, un trim, un
canale, un asse giroscopico, un canale di addestramento, un timer o qualsiasi
altra sorgente.

**Trim del minimo** — per i motori a scoppio, consente a un trim dedicato di
regolare il regime di minimo senza alterare la posizione di massimo. Con il trim
del minimo attivato, il canale del gas si posiziona a -75% con lo stick al
minimo, e il trim del Gas - Throttle regola poi il minimo tra -100% e -50%:

![Menu del trim del minimo](../assets/model-mixes-thr-trim-menu.png)

![Trim del minimo in posizione bassa](../assets/model-mixes-thr-trim-low-position.png)

**Throttle Cut** — un vero e proprio interblocco di sicurezza: il canale diventa
attivo solo dopo che lo stick del Gas - Throttle è passato per il minimo, in
modo che l'azionamento accidentale di un interruttore non possa avviare il
motore da una posizione di gas elevato:

![Throttle Cut](../assets/model-mixes-thr-cut.png)

**Throttle Hold** — mantiene il canale a un valore fisso indipendentemente dalla
posizione dello stick, senza l'interblocco di sicurezza offerto dal Throttle
Cut:

![Throttle Hold](../assets/model-mixes-thr-hold.png)

Anche il mix Gas - Throttle dispone del proprio conteggio dei canali di uscita,
esattamente come qualsiasi altro mix:

![Numero di canali del Gas - Throttle](../assets/model-mixes-thr-ch-count.png)

!!! note "Interblocco del Gas - Throttle"
    Ethos richiede che l'ingresso del mix Gas - Throttle passi per -100% prima
    di consentire l'armamento, indipendentemente dalle impostazioni di Throttle
    Cut e Throttle Hold: un modello creato con la procedura guidata di selezione
    modello ne tiene già conto, ma anche i mix del gas costruiti manualmente
    dovrebbero farlo.

## Librerie di mix {: #mix-libraries }

La libreria dei mixer predefiniti della finestra **Aggiungi mix** è adattata
alla categoria di modello scelta al momento della creazione: aereo, aliante,
elicottero e multirotore presentano ciascuno un insieme diverso:

![Libreria di aerei](../assets/model-mixes-library-airplane.png)

![Libreria di alianti](../assets/model-mixes-library-glider.png)

![Libreria di elicotteri](../assets/model-mixes-library-heli.png)

![Libreria di multirotori](../assets/model-mixes-library-multirotor.png)

Ogni libreria comprende inoltre il **Mix Libero**: un tipo di mix generico senza
ingresso/uscita preimpostati, più flessibile delle voci specializzate ma che
richiede una configurazione più laboriosa per ottenere lo stesso risultato.

## Vista per canale {: #per-channel-view }

Quando sulla stessa uscita si accumulano numerosi mix, può risultare difficile
coglierne l'effetto complessivo dalla tabella riportata sopra. Selezionando un
mix e scegliendo **Visualizza per canale**, tutti i mix che agiscono su una
stessa uscita vengono invece raggruppati insieme:

![Passaggio alla vista per canale](../assets/model-mixes-chview-select.png)

![Canale compresso](../assets/model-mixes-chview-collapsed.png)

![Canale dell'elevatore espanso](../assets/model-mixes-chview-elevator.png)

Espandendo la riga di riepilogo di un canale si visualizzano tutti i mix che vi
contribuiscono, ciascuno con la propria uscita numerica e grafica in tempo
reale: utile per verificare con esattezza quanto un mix secondario (ad esempio
la compensazione Flap a Elevatore) stia aggiungendo all'ingresso primario dello
stick:

![Dettaglio della vista per canale dell'elevatore](../assets/model-mixes-chview-elevator-channel.png)

![Canale dell'elevatore, mix evidenziato](../assets/model-mixes-chview-elevator-channel-view.png)

Selezionando un sotto-mix anziché la riga di riepilogo si apre lo stesso menu
contestuale della vista a tabella (modifica, ritorno alla vista a tabella,
cancellazione):

![Selezione della vista a tabella dalla vista per canale](../assets/model-mixes-chview-table-view-select.png)

![Ritorno alla vista a tabella](../assets/model-mixes-chview-back-at-mixes-view.png)
