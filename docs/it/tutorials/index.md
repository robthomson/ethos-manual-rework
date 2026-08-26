# Tutorial di programmazione

Questa sezione descrive alcuni esempi di programmazione per diversi modelli, preceduti da una sezione di configurazione di base della radio che copre le impostazioni di base necessarie per qualsiasi modello.

- Esempio di configurazione iniziale della radio
- Esempio di modello di potenza di base
- Esempio di semplice aliante 4ch
- Esempio di ala di base
- Esempio di elicottero Flybarless di base

Sebbene questi esempi possano sembrare relativi a tipi di modelli specifici, sono solo un veicolo per spiegare il metodo di programmazione Ethos. Sarebbe utile programmare effettivamente questi modelli sulla radio e osservare le uscite sullo schermo del monitor mentre vengono manipolati gli ingressi. Una volta compresi questi concetti e il processo, dovresti essere in grado di adattare questi esempi al tuo modello.

Esempio di configurazione iniziale della radio

Questa sezione introduttiva descrive i passi iniziali per configurare la radio stessa, prima di programmare qualsiasi modello specifico. Una volta completata, è possibile seguire tutti gli esempi di programmazione riportati nelle sezioni successive.

Nota: questi esempi non sono di tipo "ricettario". Partono dal presupposto che l'utente abbia una conoscenza di base del vocabolario dei modelli di radiocomando e che abbia familiarità con la navigazione nella struttura dei menu di Ethos. Se in qualsiasi momento dovessi essere confuso, ti invitiamo a rivedere le sezioni precedenti di questo manuale per un ripasso. In particolare, consulta la sezione [Interfaccia utente e navigazione ](../getting-started/user-interface-and-navigation.md)per familiarizzare con l'interfaccia utente della radio, in modo da trovare facilmente la pagina di configurazione di cui hai bisogno.

### Passo 1. Carica le batterie della radio e del volo.

Carica la batteria della radio seguendo le istruzioni ricevute con la radio. Carica anche le batterie di volo da utilizzare, utilizzando un caricabatterie adatto al tipo di batteria, osservando tutte le precauzioni di sicurezza, soprattutto quando si utilizzano batterie al litio.

### Passo 2. Calibra l'hardware.

Assicurati di aver eseguito la calibrazione hardware durante l'avvio iniziale della radio, per confermare che la radio conosce esattamente i centri e i limiti di ogni cardano, potenziometro e cursore. È possibile rifarla seguendo le istruzioni riportate nella sezione [Calibrazione ](../system-setup/hardware.md)del sistema e dell'hardware di questo manuale.

### Passo 3. Esegui la configurazione del sistema radio.

La configurazione del sistema radio serve a configurare le parti dell'hardware del sistema radio comuni a tutti i modelli. Si differenzia dalle funzioni di "Impostazione del modello" che configurano le impostazioni specifiche per ogni modello.

Leggi la sezione dedicata alla configurazione del sistema per familiarizzare con tutte le impostazioni di questa sezione.

Molte impostazioni possono essere lasciate (almeno inizialmente) ai valori predefiniti, ma è opportuno rivedere le seguenti:

Data e ora

Imposta l'ora e la data corrente.

Audio

Imposta la sezione Voci per gli annunci vocali via radio includendo i tuoi file audio personalizzati. Consulta la sezione [Generale / Audio / Scelta delle voci](../system-setup/general.md).

Stick

Modalità Stick

Seleziona la modalità stick che preferisci. La modalità 1 prevede il throttle e l'alettone sullo stick destro e l'elevatore e il timone su quello sinistro. La modalità 2 prevede Gas - Throttle e timone sullo stick di sinistra e alettone ed elevatore su quello di destra.

Nota: la modalità 2 è quella predefinita.

**Attenzione**!  Se un modello è configurato per la modalità 2 e il TX per la modalità 1, è possibile che il motore dei modelli elettrici si avvii all'accensione del ricevitore.

ordine dei canali

L'ordine dei canali predefinito di Ethos è AETR (cioè Aileron, Elevator, Throttle, Rudder). Potresti preferire impostare l'ordine dei canali predefinito in base all'ordine a cui sei abituato. TAER è l'ordine predefinito per Spektrum/JR, mentre AETR è l'ordine predefinito per Futaba/Hitec. Questa impostazione definisce l'ordine in cui vengono inseriti i quattro ingressi degli stick quando viene creato un nuovo modello. Naturalmente può essere modificato in seguito.

- Ricevitori stabilizzati FrSky

Nota che AETR è l'ordine richiesto se vuoi utilizzare uno dei ricevitori stabilizzati FrSky. Tuttavia, per i modelli con più di una superficie per gli alettoni, l'elevatore, il timone, i flap e così via, la procedura guidata normalmente raggruppa queste superfici, quindi ad esempio si ottiene AAETR se si utilizzano 2 canali per gli alettoni.

I ricevitori SRx si aspettano un ordine dei canali di AETRA o AETRAE, quindi si può dire alla procedura guidata (in Sistema / Stick) di mantenere i "primi quattro canali fissi".

Batteria

Controlla le specifiche della batteria della radio e configura la "Tensione principale", la "Bassa tensione" e la "Gamma di tensione del display" come descritto nella sezione [Sistema / Batteria ](../system-setup/battery.md)di questo manuale.

ID di registrazione del proprietario

L'"ID di registrazione del proprietario" viene utilizzato con i sistemi ACCESS. Questo ID diventa l'"ID di registrazione" quando si registra un ricevitore. Inserisci lo stesso codice nel campo dell'ID di registrazione del proprietario degli altri trasmettitori con cui vuoi utilizzare la funzione SmartShareTM. Consulta la sezione Impostazione del modello / [Sistema RF di ](../model-setup/rf-system.md)questo manuale (sebbene sia configurato nella sezione Impostazione del modello, l'"ID di registrazione del proprietario" sarà utilizzato per ogni nuovo modello e può essere considerato un'impostazione del sistema. Si noti inoltre che l'ID di registrazione del proprietario può essere cambiato per un particolare ricevitore durante il processo di registrazione).

Unità

Tieni presente che in Ethos le unità di telemetria sono configurate per ogni sensore. Non esiste un'impostazione metrica o imperiale globale.
