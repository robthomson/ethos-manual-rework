---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Display

![Home dei display](../assets/display-home.png)

La schermata Home è costituita da una o più **schermate di visualizzazione**, ciascuna composta da **widget** che si posizionano e configurano personalmente. Premendo `DISP` si apre l'editor della schermata corrente.

Sono disponibili fino a **otto** schermate, ognuna basata su uno dei **tredici** layout previsti (fino a **nove** celle per widget). I widget possono mostrare la telemetria, ma anche una qualsiasi delle altre diciassette categorie di informazioni — stato del modello/della radio, timer, canali e altro ancora. Le schermate configurate si raggiungono scorrendo con il dito oppure con `PAGE` su/giù; le barre superiore e inferiore restano visibili in tutte le schermate, tranne nel layout a schermo intero.

## Aggiungere un widget

![Tipi di widget](../assets/display-widget-types.png)

Ogni schermata è una griglia; toccando una cella vuota si apre il selettore dei widget. I widget spaziano da semplici indicazioni testuali e numeriche fino a strumenti analogici, grafici e registri di telemetria completi. Una volta posizionato, toccando nuovamente un widget si apre lo stesso menu di opzioni usato per ridimensionarlo, spostarlo o rimuoverlo:

![Opzioni di configurazione del widget](../assets/display-widget-config-options.png)

Selezionando le impostazioni proprie di un widget si apre un modulo di configurazione specifico per quel widget. Il campo **sorgente** — cioè il valore mostrato dal widget — utilizza lo stesso [selettore di sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source) presente ovunque in Ethos:

![Modifica della sorgente del widget](../assets/display-change-source.png)

## Tipi di widget {: #widget-types }

**Value** — una singola lettura numerica o di telemetria, mostrata come testo:

![Configurazione widget Value](../assets/display-widget-value-config.png)

La maggior parte delle sorgenti supporta anche la riduzione al valore **min** o **max** in tempo reale — dopo aver selezionato la sorgente, premere a lungo su di essa e scegliere Min o Max — utile ad esempio per il valore peggiore di RSSI durante un volo:

![Widget Value con min](../assets/display-widget-value-min.png)
![Widget Value con min RSSI](../assets/display-widget-value-min-rssi.png)

Una volta posizionato, viene visualizzato come una semplice indicazione sulla schermata:

![Widget Value con valore di telemetria](../assets/display-widget-value-telemetry.png)

**Bitmap** — visualizza un'immagine statica (ad esempio la foto del modello), oppure un insieme di immagini che si alternano in base al valore di una sorgente (ad esempio un'icona della batteria che cambia con la tensione):

![Configurazione widget Bitmap](../assets/display-widget-bitmap-config.png)
![Tipo di widget Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — un indicatore di batteria dedicato che legge da un sensore come il FLVSS: tensione totale del pacco, numero di celle e tensione di ogni singola cella. Scendendo sotto la soglia di **Low voltage** configurata, la visualizzazione diventa rossa — nell'esempio seguente una soglia di 3,3 V viene attivata dalla cella più bassa:

![Configurazione widget LiPo](../assets/display-widget-lipo-config.png)
![Widget LiPo](../assets/display-widget-lipo.png)

**Channels** — fino a 8 canali di uscita rappresentati come grafico a barre, orizzontale o verticale:

![Configurazione widget Channels](../assets/display-widget-channels-config.png)
![Widget Channels](../assets/display-widget-channels.png)

**Line Chart** — traccia nel tempo il valore di una sorgente, azzerandosi a ogni Flight Reset:

![Configurazione widget Line Chart](../assets/display-widget-line-chart-config.png)
![Widget Line Chart](../assets/display-widget-line-chart.png)

- **Source** — il valore rappresentato nel grafico.
- **Pause condition** — una sorgente che mette in pausa/riprende la registrazione (in alternativa è sufficiente toccare il widget in funzione, se non è disponibile una sorgente libera per questo scopo).
- **Log period** — intervallo di campionamento; 500 ms coprono circa 6 minuti prima dello scorrimento, 1 s circa 12 minuti.
- **Inverted** — capovolge il grafico verticalmente.
- **Auto range** — scala automaticamente l'asse verticale per adattarlo ai dati; se disattivato, utilizza invece valori fissi di **Min**/**Max** (ad esempio un intervallo costante da −100% a +100%).

Toccando un grafico in funzione compaiono le voci **Pause/resume**, **Reset** (cancella e riavvia), **Configure widget**, oppure il collegamento a **Configura schermate**:

![Opzioni del Line Chart](../assets/display-widget-line-chart-options.png)

**Text** — visualizza il contenuto di un file di testo Markdown (letto da `documents/user/` — vedere [File Manager](../system-setup/file-manager.md#top-level-folders)):

![Configurazione widget Text](../assets/display-widget-text-config.png)
![Widget Text](../assets/display-widget-text.png)

**Timer Log** — un registro scorrevole dei valori passati di un timer scelto, scritto ogni volta che quel timer viene azzerato (utile per tenere traccia dell'utilizzo dei pacchi di volo durante una sessione); **Reverse** colloca la voce più recente in cima:

![Configurazione widget Timer Log](../assets/display-widget-timer-logs-config.png)
![Widget Timer Log](../assets/display-widget-timer-log.png)

Premendo a lungo su una voce (o sul widget) si accede a **Clear logs**, alla modifica/azzeramento del timer associato, oppure alla configurazione del widget o della schermata:

![Menu della voce del Timer Log](../assets/display-widget-timer-log-menu.png)

**GPS Map** — traccia in tempo reale la posizione GPS come percorso, per i modelli dotati di sensore GPS (per maggiori dettagli specifici su questo widget si veda il thread *FrSky - ETHOS Lua Script Programming* su rcgroups, post #8854):

![Configurazione widget GPS Map](../assets/display-widget-gps-map-config.png)

## Opzioni a livello di schermata

Oltre ai singoli widget, ogni schermata dispone di impostazioni proprie — dimensione della griglia del layout, sfondo e quali schermate sono incluse nel ciclo di `PAGE`:

![Opzioni di configurazione della schermata](../assets/display-screen-config-options.png)

Una schermata Home completamente configurata combina più widget in un unico layout leggibile a colpo d'occhio:

![Vista principale](../assets/display-main-view.png)

Vedere [Display aggiuntivi](additional-displays.md) per aggiungere altre schermate oltre a quella predefinita, e [Widget personalizzati](custom-widgets.md) per i widget realizzati con script Lua oltre a quelli integrati.
