---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Interfaccia utente e navigazione

Ethos può essere utilizzato interamente con l'**encoder rotativo** di destra
(ruotare per spostare la selezione, premere per `ENT`) e con il tasto `RTN`
per uscire da un menu — il touchscreen, dove presente, è una scorciatoia per
le stesse azioni, non una modalità di lavoro separata. `MDL`, `DISP` e `SYS`
portano direttamente a Configurazione del modello, Configura schermate e
Configurazione di sistema rispettivamente (le stesse tre icone della barra
inferiore); una pressione prolungata di `RTN` da qualsiasi punto riporta
immediatamente alla schermata Home.

## Il menu di azzeramento

![Menu contestuale](../assets/resetmenu.png)

Una pressione prolungata di `ENT` dalla schermata Home apre un menu di
azzeramento:

- **Azzera volo** — azzera telemetria, timer e interruttori funzione, e
  riesegue la [checklist](../model-setup/checklist.md) pre-volo.
- **Azzera telemetria** — azzera solo la telemetria.
- **Azzera timer** — azzera solo i timer.
- **Blocca touchscreen** — raggiungibile anche premendo `ENT` + `PAGE`
  insieme per un secondo dalla schermata Home, oppure come trigger di una
  [funzione speciale](../model-setup/special-functions.md).

## Controlli di modifica

**Aggiunta di elementi funzionali** — un timer, un interruttore logico, una
funzione speciale, una curva o una variabile si creano toccando il **+**
accanto alle intestazioni di colonna nel menu corrispondente. Su una radio
senza touchscreen, evidenziare un elemento esistente, premere `ENT` e
scegliere **Aggiungi** dal menu — la stessa opzione è disponibile anche
sulle radio con touchscreen.

### Tastiera virtuale

![Tastiera di testo](../assets/keyboard-text-azerty.png)

Toccando un campo di testo qualsiasi (o premendo `ENT` su di esso) si apre
la tastiera a schermo. Il tasto backspace cancella a sinistra del cursore;
`PAGE` cancella a destra e, una volta che il cursore raggiunge la fine del
testo, prosegue cancellando da sinistra. Toccando il campo stesso il cursore
si sposta in quella posizione — oppure si possono usare `SYS`/`DISP` per
spostarlo a sinistra/destra senza touchscreen. Il tasto **?123**/**abc**
attiva il tastierino numerico (che contiene anche i caratteri speciali):

![Tastiera numerica](../assets/keyboard-text-numbers.png)

Su una **radio senza touchscreen**, premendo `ENT` su un campo di testo si
entra direttamente in modalità di modifica: ruotare l'encoder per scorrere
minuscole, maiuscole, cifre e infine caratteri speciali, premendo `ENT` per
inserire ciascuno di essi. `MDL` commuta tra maiuscolo e minuscolo il
carattere immediatamente a destra del cursore (e ogni carattere digitato
successivamente resta in quel formato finché non si commuta di nuovo).
`PAGE` cancella a destra del cursore; `SYS`/`DISP` lo spostano a
sinistra/destra.

## Controlli dei valori numerici

![Inserimento numerico](../assets/keyboard-numbers.png)

Toccando un campo numerico si apre una barra di controllo nella parte
inferiore dello schermo: **`<`**/**`>`** cambiano la dimensione del passo
(scorrendo tra le decadi — ad es. 0.01/0.1/1.0/10.0), **`-`**/**`+`** (o
l'encoder rotativo) regolano il valore di quel passo, e **Altro** apre
ulteriori opzioni:

![Opzioni di inserimento numerico](../assets/keyboard-numbers-options.png)

- Passare al valore predefinito del campo
- Impostare al minimo / impostare al massimo
- Sostituire il selettore a passi con uno **slider**

![Inserimento con slider](../assets/keyboard-numbers-slider.png)

Lo slider (regolabile anch'esso con l'encoder rotativo) è più rapido per le
variazioni grossolane; **Disabilita slider** riporta al selettore a passi.
I valori di intervallo della telemetria si modificano allo stesso modo:

![Slider disabilitato](../assets/keyboard-numbers-options-disable-slider.png)

## La funzione Opzioni {: #the-options-feature }

Quasi ovunque sia previsto un valore o una [sorgente](#choosing-a-source),
una pressione prolungata di `ENT` apre una finestra **Opzioni** — la
presenza della piccola icona di menu ("hamburger") nell'angolo superiore
sinistro di un campo indica che la funzione è disponibile.

### Opzioni dei valori

![Opzioni della sorgente](../assets/source-with-options.png)

La finestra delle opzioni del valore riporta il nome del parametro in corso
di modifica e offre la scelta tra un minimo/massimo fisso oppure il
pilotaggio tramite una **sorgente** (ad es. un potenziometro, per regolare
il valore in volo). Se il campo utilizza già una sorgente, la stessa
pressione prolungata propone invece di convertire il valore corrente di
quella sorgente in un valore fisso:

![Conversione della sorgente in valore](../assets/source-convert-to-value.png)

### Scelta di una sorgente {: #choosing-a-source }

Selezionando **Scegli una sorgente** si apre un selettore a due colonne —
prima una **categoria** (analogici, interruttori, interruttori logici, trim,
canali, un asse del giroscopio, un canale trainer, un timer, un sensore di
telemetria o alcuni valori speciali), quindi il membro specifico:

![Menu delle sorgenti](../assets/source-menu.png)

Una volta impostata la sorgente, la stessa pressione prolungata apre le
opzioni specifiche per il tipo di sorgente:

**Qualsiasi sorgente** —

- **Inverti** — nega la sorgente (ad es. attiva quando un interruttore *non*
  è in alto, invece di quando lo è).
- **Fronte** — interviene una sola volta a ogni transizione (falso→vero o
  vero→falso) invece di restare attiva per tutta la durata dello stato;
  viene indicata con il prefisso `†` sulla sorgente. Disponibile
  genericamente sugli interruttori e, in particolare, sulla condizione di
  attivazione dell'[interruttore logico
  Sticky](../model-setup/logical-switches.md).

**Sorgenti stick** — opzioni di tipo calibrazione/subtrim:

![Opzioni della sorgente stick](../assets/source-stick-options.png)

**Sorgenti interruttore** —

![Opzioni dell'interruttore a 2 posizioni](../assets/source-2pos-options.png)
![Opzioni dell'interruttore](../assets/switch-options.png)

- **Negativo** — inverte l'azione dell'interruttore.
- **Mezza corsa** — per un interruttore a 2 posizioni o un interruttore
  logico, cambia l'intervallo di uscita da ±100% a 0–100%.

**Sorgenti trim** —

![Opzioni della sorgente trim](../assets/source-trim-options.png)

- **Negativo** — inverte l'azione del trim (utile all'interno delle azioni
  di un mix libero).
- **Corsa completa** — i trim hanno per impostazione predefinita un
  intervallo di ±25%; come sorgente può essere ampliato a ±100%.
- **Ignora ingresso trainer** — su un [interruttore
  logico](../model-setup/logical-switches.md), esclude i movimenti
  provenienti dall'ingresso trainer dall'attivazione dell'interruttore. Uso
  tipico: rilevare il movimento degli stick del *master* trainer (ad es. per
  intervenire istantaneamente se l'allievo commette un errore) senza che
  anche i comandi dell'allievo lo attivino.

**Sorgenti variabile** —

![Opzioni della sorgente variabile](../assets/source-var-options.png)

- **Negativo** — nega il valore della variabile per questo utilizzo.
- **Ignora intervallo** — alcuni campi hanno intervalli asimmetrici (ad es.
  Min/Max delle Uscite, che vanno rispettivamente da −150–0% e 0–150%). A
  meno che una [variabile](../model-setup/variables.md) usata come sorgente
  di quel campo non abbia un intervallo identico, attivare questa opzione
  per saltare la conversione automatica dell'intervallo eseguita da Ethos ed
  evitare valori inattesi.

**Sorgenti sensore di telemetria** — riducono la sorgente al suo minimo o
massimo rilevato invece che alla lettura istantanea (alcuni sensori
aggiungono ulteriori opzioni specifiche oltre a queste):

![Opzioni min/max del sensore](../assets/source-sensor-options.png)
![Massimo del sensore selezionato](../assets/source-sensor-maxi.png)
