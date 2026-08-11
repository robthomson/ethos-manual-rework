---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Visualizzazioni principali

## Schermata Home

![Schermata Home](../assets/mainview.png)

La schermata Home è ciò che viene visualizzato quando nessun menu è aperto: una
serie di massimo **otto** viste principali che l'utente configura a proprio
piacimento (consulta [Configurare le schermate](../displays/index.md)), tra le
quali ci si sposta con il tasto `PAGE` o con un gesto di sfioramento. Un modello
appena creato parte con una sola schermata, che mostra un'immagine del modello,
tre widget per i timer e gli indicatori dei trim e dei potenziometri; da lì tutti
gli elementi sono configurabili dall'utente.

Le viste principali condividono normalmente le barre superiore e inferiore
descritte di seguito, ma una vista può anche essere impostata a schermo intero,
nascondendo entrambe.

## La barra superiore

La barra superiore mostra il nome del modello sulla sinistra (e la modalità di
volo attiva, se configurata) e, a destra, una serie di icone di stato:

- Se la registrazione dei dati è attiva
- Icona del Trainer per il master o lo slave, a seconda dei casi
- RSSI — collegamento 2.4G
- RSSI — collegamento 900M (se è installato un modulo dual-band/long-range)
- Volume dell'altoparlante
- Stato della batteria della radio

Toccando le icone dell'altoparlante o della batteria si aprono direttamente i
relativi pannelli di controllo [Generale](../system-setup/general.md) (audio) e
[Batteria](../system-setup/battery.md).

### Avviso di errore

Quando Ethos rileva un errore, nella barra superiore viene visualizzata un'icona
di avvertimento con un triangolo rosso: le cause più comuni sono gli errori dello
script Lua, un errore di backup della RAM oppure l'esecuzione di una build
notturna (instabile) del firmware. Il dettaglio relativo all'avviso viene sempre
visualizzato nella pagina **Sistema → Info**, la stessa in cui si trovano il tempo
di funzionamento della radio e i [log degli errori](../system-setup/information.md).

## La barra inferiore

![Barra inferiore](../assets/bottombar.png)

La barra inferiore presenta quattro schede per accedere alle funzioni di livello
superiore — **Home**, **Configurazione del modello**, **Configurazione delle
schermate**, **Configurazione del sistema** — con l'ora del sistema sulla destra
(toccando l'ora si accede direttamente a
[Data e ora](../system-setup/date-and-time.md)).

## L'area dei widget

L'area centrale di ogni vista è costituita da **widget**: immagine del modello,
timer, dati di telemetria, barre dei trim e dei potenziometri e altro ancora,
tutti posizionati e configurati dall'utente. Consulta
[Configurare le schermate](../displays/index.md) per sapere come aggiungere,
spostare e configurare i widget, e
[Schermate aggiuntive](../displays/additional-displays.md) per aggiungere altre
schermate oltre a quella singola predefinita.
