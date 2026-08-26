# Configurazione della **schermata** principale

![](../assets/display-home.png)

Il contorno verde indica che ci si trova in modalità di configurazione. È possibile configurare un widget toccandolo

## Configura l’immagine modello



Seleziona il widget immagine modello per modificare.

![](../assets/display-widget-bitmap-config.png)

Per impostazione predefinita, il widget bitmap nella schermata principale presenta il “Tipo di bitmap” impostato su “Bitmap modello”. La bitmap non può essere selezionata qui, ma va configurata in “Modello / Modifica modello” o nelle procedure guidate per la creazione di nuovi modelli. La bitmap del modello deve trovarsi nella cartella /bitmaps/model.  
  
Per impostazione predefinita, i tre widget sulla destra visualizzano i tre timer.

![](../assets/display-widget-types.png)

È possibile riconfigurarli per visualizzare altri parametri selezionando ciascun widget e modificandone il tipo una volta aperta la finestra di dialogo. Per ulteriori dettagli, vedere di seguito.  
  
Nell'elenco compariranno anche i widget Lua personalizzati.

## Esempio di widget della schermata principale

![](../assets/mainview.png)

Nell'esempio qui sopra, a sinistra il widget Model Bitmap visualizza l'immagine del modello configurata in Model / Edit model / Picture. Il widget in alto a destra mostra la tensione della batteria del ricevitore, quello al centro l'RSSI e quello in basso "Throttle ACTIVE". Questo è il widget di stato disponibile nella discussione FrSky - ETHOS Lua Script Programming su rcgroups.

![](../assets/display-widget-config-options.png)

Tocca un qualsiasi widget dalle viste principali per visualizzare una finestra di dialogo per configurare il widget o per accedere alla funzione principale [Configura schermate](index.md).

Widget nella parte superiore dello schermo (solo serie XE)



Nelle radio della serie XE, il widget predefinito nella schermata principale è di tipo “Bitmap”, impostato su “Bitmap modello”. La bitmap non può essere selezionata da qui, ma va configurata in “Modello / Modifica modello” o nelle procedure guidate per la creazione di nuovi modelli. L'immagine bitmap del modello deve trovarsi nella cartella /bitmaps/model.

Per modificare il widget, tocca l'immagine bitmap del modello per accedere alla modalità di modifica. Consulta i widget standard riportati di seguito per selezionare un widget diverso da visualizzare nella schermata superiore.



Nell'esempio sopra riportato è stato selezionato il widget "Canali".

## 		Widget standard

Bitmap

Serve a visualizzare una bitmap selezionata.

![](../assets/display-widget-bitmap-config.png)

Nell'esempio precedente, il widget visualizzerà la bitmap del modello, che deve trovarsi in /bitmaps/model.

![](../assets/display-widget-bitmap-type.png)

Il widget può anche visualizzare una bitmap utente, che deve trovarsi in /bitmaps/user.

Valore

![](../assets/display-widget-value-config.png)

Il widget Valore visualizza semplicemente il valore della sorgente selezionata.

Valore minimo/massimo

![](../assets/display-widget-value-min.png)

Quando si visualizzano i valori della telemetria, una pressione prolungata sul sensore dopo la selezione permette di visualizzare il valore minimo o massimo.

![](../assets/display-widget-value-min-rssi.png)

In questo esempio, il valore minimo di RSSI sarà visualizzato nel widget Valore.

![](../assets/display-widget-value-telemetry.png)

Esempi di widget Valore tra cui RSSI Min.

Registri del timer

![](../assets/display-widget-timer-logs-config.png)

È possibile selezionare il timer da registrare. L'inversione metterà la voce più recente in cima al registro.

![](../assets/display-widget-timer-log.png)

I registri dei timer forniscono un registro dei valori dei timer. I valori del timer vengono scritti quando il timer viene resettato.

![](../assets/display-widget-timer-log-menu.png)

Premi a lungo sul widget per "cancellare i registri", modificare il Timer(n), resettare il Timer(n) o configurare il widget o le schermate.

Mappa GPS

![](../assets/display-widget-gps-map-config.png)

Questo widget supporta la visualizzazione di una mappa GPS. Per maggiori dettagli, consulta la discussione sull'X20 Ethos su rcgroups, in particolare il post [#8854](https://www.rcgroups.com/forums/showpost.php?p=47392275&postcount=8854).

LiPo

![](../assets/display-widget-lipo-config.png)

Il widget Lipo visualizzerà le informazioni sulla tensione delle Lipo provenienti da sensori come FLVSS.

![](../assets/display-widget-lipo.png)

Il widget Lipo mostra la tensione totale del pacco e il numero di celle, oltre alle tensioni delle singole celle.

Se la tensione più bassa della cella è inferiore alla soglia di "Bassa tensione", le tensioni vengono visualizzate in rosso. Nel secondo widget Lipo qui sopra, la soglia di bassa tensione è stata impostata a 3,3v e il valore è stato visualizzato in rosso.

Canali

![](../assets/display-widget-channels-config.png)

Il widget Canali permette di visualizzare fino a 8 canali in formato grafico a barre, con barre orizzontali o verticali.

![](../assets/display-widget-channels.png)

L'esempio precedente mostra due widget Canali: quello di sinistra mostra 4 canali in verticale, mentre quello di destra mostra 8 canali in orizzontale.

Grafico a linee

Configurazione

![](../assets/display-widget-line-chart-config.png)

Il widget del grafico a linee permette di tracciare il grafico della sorgente selezionata.

Nota che il widget ripristina i suoi dati in caso di "Flight Reset".

- Fonte

Seleziona la sorgente da analizzare.

- Condizione di pausa

Seleziona la sorgente da utilizzare come controllo di pausa. Se non disponi di un ricambio, puoi anche mettere in pausa e riprendere il grafico a linee toccando il widget mentre è in esecuzione.

- Periodo di log

È possibile impostare il periodo di registrazione. Utilizzando un periodo di 500ms, il grafico coprirà circa 6 minuti prima di iniziare a scorrere fuori dalla pagina, mentre 1s coprirà circa 12 minuti.

- Invertito

Il grafico di log può essere invertito.

- Gamma **automatica**

Se l'intervallo automatico è attivato, l'asse verticale verrà scalato in base all'ingresso. Se l'intervallo automatico è disattivato, l'asse verticale verrà scalato in base alle impostazioni Min e Max. Nell'esempio precedente, il widget superiore è stato impostato per l'intervallo automatico e il grafico mostra un'oscillazione della sorgente da +26% a -22%.

- Min/Max

Nell'esempio precedente, il widget in basso ha l'intervallo automatico disattivato e viene utilizzato un intervallo fisso da -100% a +100%.

![](../assets/display-widget-line-chart.png)

Opzioni di esecuzione

![](../assets/display-widget-line-chart-options.png)

Toccando il grafico a linee mentre è in esecuzione si apre una finestra di dialogo che ti permette di:

- Metti in pausa o riprendi la registrazione
- Azzera il grafico e ricomincia
- Configura le impostazioni del widget
- Vai al menu "Configura schermate

Testo

![](../assets/display-widget-text-config.png)

Il widget Testo visualizza il contenuto di un file di testo. È supportato il formato markdown.

Il file di testo deve essere collocato in una cartella denominata documenti/utente.

![](../assets/display-widget-text.png)

Il contenuto del file verrà visualizzato nel widget Testo.
