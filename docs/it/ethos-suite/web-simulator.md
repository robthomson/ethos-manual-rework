# Simulatore web di Ethos

![](../assets/Pictures/1000000100000ECE0000087E9D52C826.png)

Il simulatore web Ethos è realizzato in WebAssembly (abbreviato Wasm), una soluzione portatile che ne consente la distribuzione sul web. Ciò significa che funziona all'interno di un browser e non richiede l'installazione su un PC. Il browser consigliato è Chrome..

Il simulatore web Ethos consente di esplorare le funzionalità della radio e di testare le funzionalità o i miglioramenti previsti per il modello senza dover ricorrere alla radio vera e propria. Consente inoltre di provare con estrema facilità le nuove versioni prima di aggiornare la radio.

Il simulatore web è disponibile all'indirizzo [https://ethos-simulator.frsky-rc.com/](https://ethos-simulator.frsky-rc.com/)

Le opzioni predefinite sono la versione 26.1.0-RC6 (al momento della stesura di questo documento), la scheda radio X20 Pro e il protocollo FCC. Per iniziare, selezionare la lingua di visualizzazione.

![](../assets/Pictures/1000000100000ECA00000874C3B44D03.png)

Al primo avvio, non verranno rilevati dati di modello validi, pertanto verrà avviata la procedura guidata per la creazione di un nuovo modello.

![](../assets/Pictures/1000000100000ECC00000870497896E6.png)

Completa la procedura guidata per configurare un modello di test di base.

Se la versione e il tipo di radio predefiniti non corrispondono a quelli desiderati, selezionare la versione di Ethos desiderata, il tipo di radio da simulare e il protocollo RF.

Fai clic sull'icona "Pannelli" ![](../assets/Pictures/100000010000005D00000054E66F5895.png) nella barra dei menu in alto, quindi selezionare la Console.

![](../assets/Pictures/1000000100000ECE000008706423AC8F.png)

La console apparirà accanto al pannello di visualizzazione.

![](../assets/Pictures/1000000100000ECC0000087C83E4950C.png)

Fai clic sulla barra del titolo della Console e trascinala verso il basso. Sposta il mouse finché la Console non occupa il quadrante in basso a sinistra.

La console è utile per verificare la sequenza di avvio del simulatore e per monitorare gli eventi e i messaggi di errore.

![](../assets/Pictures/1000000100000ECA000008702FCCDE98.png)

Fai nuovamente clic sull'icona "Pannelli" e ripeti l'operazione con il pannello "Telemetria", spostandolo nel quadrante in basso a destra.

![](../assets/Pictures/1000000100000ECA000008747ED7D4D7.png)

Nel pannello "Telemetria", clicca più volte su "Aggiungi un nuovo sensore" e aggiungi i sensori a cui desideri avere accesso nelle tue simulazioni.

Per salvare i sensori in vista delle sessioni future, clicca sul ![](../assets/Pictures/100000010000005400000051ACB62F01.png) e seleziona “Salva impostazioni di telemetria”. Le impostazioni di telemetria verranno salvate in un file denominato “telemetry.json” nella cartella dei download. Spostalo in una posizione comoda. Nelle successive sessioni del simulatore, clicca sull'icona "Carica" e seleziona "Carica un file di telemetria JSON", quindi individua il file "telemetry.json" che hai salvato.

Ora sei pronto per avviare la simulazione. Il browser memorizzerà la disposizione del pannello, quindi non dovrai continuare a riorganizzarlo.

### Configurazione consigliata

È consigliabile riprodurre la configurazione della propria radio nel simulatore. In questo modo avrai a disposizione le stesse funzionalità della tua radio, il che ti consentirà di testare facilmente i miglioramenti apportati ai tuoi modelli senza influire sul tuo ambiente di volo o di modellismo, finché tutto non funzionerà come previsto.

I passaggi consigliati per la configurazione sono i seguenti:

1. Esegui un backup della tua radio utilizzando la funzione "Backup e ripristino" di Suite.

2. Nel menu "Carica" seleziona "Carica un backup radio" e individua il file di backup salvato. (Fai riferimento ai menu riportati di seguito.)

![](../assets/Pictures/1000000100000ED400000878BB388CA7.png)

3. Dovrebbe partire dal modello che era selezionato sulla tua radio al momento della creazione del backup. In questo esempio, il modello selezionato era un aliante Ng2.

Grazie all'ambiente radio a te familiare, ora puoi creare e testare un modello completamente nuovo, magari basandoti su uno dei tuoi modelli predefiniti oppure creando un clone di un modello esistente e modificandolo. Questi approcci consentono di massimizzare il riutilizzo senza dover programmare un modello da zero. Una volta completata l'operazione, utilizza l'opzione "Scarica un file di modello" per scaricare il file di modello .bin nella cartella dei download. Quindi copialo sulla tua radio.

### Barra delle attività del simulatore

La barra delle attività del simulatore presenta i seguenti comandi:

![](../assets/Pictures/100000010000036800000047E3EA708F.png)

![](../assets/Pictures/100000010000003A00000036AC758BFB.png)	Screenshot (nella cartella "Download")

![](../assets/Pictures/100000010000003400000034DE16CBC7.png)	Avvia registrazione (registra una macro – argomento che esula dall'ambito di questa panoramica)

![](../assets/Pictures/1000000100000035000000340120C033.png)	Pannelli (elenca i pannelli che non sono stati ancora aperti)

![](../assets/Pictures/100000010000003200000035B08BF6F9.png)	Carica… (vedi il menu qui sotto)

![](../assets/Pictures/100000010000003300000036B485D201.png)	Scarica... (vedi il menu qui sotto)

![](../assets/Pictures/100000010000003600000035E4DD6074.png)	Audio On/Off

![](../assets/Pictures/100000010000003200000036BA846668.png)	Riavvia il simulatore

![](../assets/Pictures/1000000100000036000000352D3A7338.png)	Documentazione (contiene un link al manuale più recente)

![](../assets/Pictures/1000000100000032000000358C5AA574.png)	Modalità chiara/scura

Upload menu

![](../assets/Pictures/10000001000000360000002DF56DE3FB.png)	Carica un file di modello (.bin)

![](../assets/Pictures/10000001000000390000002C2B0D8C92.png)	Carica un backup radio (.bin)

![](../assets/Pictures/10000001000000330000003360667B21.png)	Carica un pacchetto audio (.zip)

![](../assets/Pictures/1000000100000039000000365A698952.png)	Carica un plugin Lua (.zip)

![](../assets/Pictures/10000001000000340000002F715D80FB.png)	Carica un file CSV contenente le traduzioni (.csv)

![](../assets/Pictures/10000001000000350000002A57E2BD00.png)	Carica un file di telemetria JSON (.json)

![](../assets/Pictures/100000010000002A00000027C53ED7E7.png)	Avvia una macro (.zip)

Download menu

![](../assets/Pictures/10000001000000300000002EDEF4203A.png)	Salva il file del modello corrente (.bin)

![](../assets/Pictures/100000010000003500000035216F2B0D.png)	Modifica il modello corrente

![](../assets/Pictures/100000010000003500000035216F2B0D.png)	Modifica il file del modello corrente (JSON)

![](../assets/Pictures/100000010000003900000032E89F86E0.png)	Salva tutti gli screenshot (seleziona la cartella di destinazione, salva come .png)

![](../assets/Pictures/10000001000000380000002D9C5C49CF.png)	Salva un backup della Radio (.zip)

![](../assets/Pictures/10000001000000350000002C0EC1166A.png)	Salva le impostazioni di telemetria (.json)

Pannello di controllo

![](../assets/Pictures/10000001000007560000040A4C394584.png)

Il pannello “Controlli” riproduce i comandi hardware della radio selezionata.

Gimbals

Gli stick possono essere azionati trascinandoli con il mouse. Durante il debug è utile limitare o restringere il movimento degli stick.

	Centra automaticamente lo stick su uno o entrambi gli assi.

	Limiterà il movimento dello stick esclusivamente in senso verticale.

	Limiterà il movimento dello stick esclusivamente in orizzontale.

Interruttori e pulsanti momentanei

	Blocca gli interruttori e i pulsanti momentanei in modo che rimangano nello stato selezionato (acceso o spento) durante il debug.
