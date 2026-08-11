---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Selezione modello

![Procedura guidata modello - aeroplano](../assets/model-modelselect-model-wizard-airplane.png)

Consente di creare, selezionare, clonare ed eliminare i modelli, e di gestire
le cartelle di categoria definite dall'utente in cui sono organizzati.

## Gestione delle cartelle dei modelli

![Cartelle dei modelli](../assets/model-modelselect-folders.png)

Ethos consente di raggruppare i modelli in cartelle personalizzate — tipicamente
voci come Aeroplano, Aliante, Elicottero, Quad, Warbird, Barca, Auto, Template
o Archivio. Finché non ne viene creata alcuna, i modelli risiedono in una
cartella automatica **Uncategorized** (creata all'aggiornamento a Ethos 1.1.0
alpha 17+, oppure quando un file di modello viene copiato in `\Models` da
un'altra posizione); Ethos la elimina nuovamente quando è vuota.

Per creare una cartella, toccare **+** accanto a "Uncategorized" (oppure
premere a lungo `PAGE` su/giù), assegnarle un nome (fino a 15 caratteri) e
confermare. Le cartelle sono ordinate alfabeticamente, con **Uncategorized**
sempre in ultima posizione, e corrispondono direttamente alle sottocartelle di
`\Models` sulla SD card/eMMC. Toccando il nome di una cartella si apre la
funzione di rinomina/eliminazione — eliminando una cartella, gli eventuali
modelli contenuti vengono riportati in Uncategorized.

![Cambia cartella](../assets/model-modelselect-folder-change-select.png)

Per spostare un modello, toccarne l'icona, scegliere **Change folder**, quindi
toccare la destinazione:

![Scelta della cartella](../assets/model-modelselect-folder-airplane-select.png)

## Aggiunta di un nuovo modello

![Crea modello](../assets/model-modelselect-model-create.png)

Selezionare la categoria in cui creare il modello, toccare **+**, quindi
**Create model** per avviare la procedura guidata (se la categoria non esiste
ancora, crearla prima). Sono disponibili procedure guidate per **Airplane**,
**Glider**, **Helicopter**, **Multirotor** e **Other**; ciascuna guida attraverso
la configurazione di base per quel tipo di cellula, inclusi mix preimpostati
opzionali per i ricevitori stabilizzati FrSky (guadagno, modalità di
stabilizzazione). I nomi dei modelli possono avere fino a 15 caratteri.

### Ricevitori stabilizzati e ordine dei canali

![Procedura guidata: aeroplano](../assets/model-modelselect-model-wizard-airplane.png)

I ricevitori stabilizzati FrSky richiedono specificamente l'ordine dei canali
**AETR** — lasciare [Stick → Ordine canali](../system-setup/controls.md) sul
valore predefinito AETR con **First four channels fixed** attivo, in modo che
l'uscita della procedura guidata corrisponda a quanto il ricevitore si aspetta.

La procedura guidata assegna i canali da destra a sinistra. Per 2 alettoni +
1 profondità + 1 timone + 1 motore, si ottiene:

| Can. | Funzione |
|---|---|
| 1 | Alettone 1 (alettone destro) |
| 2 | Profondità |
| 3 | Gas |
| 4 | Timone |
| 5 | Alettone 2 (alettone sinistro) |

Con questa assegnazione, il differenziale degli alettoni è **positivo** per il
caso normale (escursione verso l'alto maggiore di quella verso il basso). I
manuali dei ricevitori FrSky documentano attualmente la convenzione *opposta*
(da sinistra a destra, quindi Can.1 = alettone sinistro, Can.5 = alettone
destro) — nel qual caso il differenziale dovrebbe essere **negativo** per
ottenere lo stesso effetto fisico.

!!! tip
    Si raccomanda di utilizzare in modo coerente la convenzione Ethos — in
    entrambi i casi tutte le funzioni di stabilizzazione continuano a
    funzionare correttamente, poiché la direzione di compensazione viene
    impostata durante la configurazione della stabilizzazione. Se è
    necessario adeguarsi alla convenzione del manuale del ricevitore, la via
    più semplice consiste nel costruire il modello normalmente con la
    procedura guidata e utilizzare poi **Swap channels** in
    [Uscite](outputs.md) per scambiare i due canali degli alettoni — in
    questo modo il segno del differenziale nel mixer degli alettoni rimane
    positivo.

### Passaggi della procedura guidata

![Procedura guidata: tipo di coda](../assets/model-modelselect-model-wizard-tail.png)
![Procedura guidata: numero di alettoni/flap](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Procedura guidata: numero di profondità/timone](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Procedura guidata: motore](../assets/model-modelselect-model-wizard-engine.png)
![Procedura guidata: riassegnazione dei canali](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Procedura guidata: nome](../assets/model-modelselect-model-wizard-name.png)
![Procedura guidata: ricevitore](../assets/model-modelselect-model-wizard-rx.png)

Per un **Airplane**, dopo il tipo di coda e il numero di superfici, la procedura
guidata richiede il numero di canali per il motore, quindi il numero di canali
per alettoni/flap.

La **configurazione della coda** offre la scelta fra coda tradizionale a croce,
coda a V oppure nessuna coda (delta/tuttala):

- **Delta/tuttala** — creando un modello Airplane con 2 alettoni e nessuna
  superficie di coda si genera automaticamente il mixaggio elevoni, con pesi
  predefiniti del 50% affinché i comandi simultanei a fondo corsa di alettoni +
  profondità raggiungano comunque un totale del 100%.
- **Delta con mixaggio eseguito da un ricevitore stabilizzato** — selezionare
  invece 1 alettone e 1 profondità; il mixaggio elevoni avviene nel ricevitore,
  secondo il relativo manuale.
- **Delta con superfici dedicate di alettoni e profondità** — lasciare che la
  procedura guidata proceda come se il modello avesse una coda; verranno
  configurati i canali necessari per alettoni e profondità (con o senza timone),
  senza creare alcun mixaggio elevoni.

Il passaggio di **riassegnazione dei canali** consente di sovrascrivere la
mappatura predefinita della procedura guidata, tenendo presente che i ricevitori
stabilizzati richiedono i canali in un ordine specifico (consultare le istruzioni
del ricevitore). L'ultimo passaggio imposta il nome del modello e associa
un'immagine.

Il modello completato viene collocato nella cartella di categoria attiva al
momento dell'avvio della procedura guidata, ordinato alfabeticamente al suo
interno. Vedere [Esempio base per ala fissa](../tutorials/basic-fixed-wing.md)
per una procedura completa passo-passo.

## Ricezione di un modello da un'altra radio Ethos

![Ricevi modello](../assets/model-modelselect-model-receive.png)

Selezionare la categoria di destinazione, toccare **+**, quindi **Receive
model** — la radio si mette in attesa e mostra il proprio indirizzo Bluetooth
affinché il mittente possa individuarla. Sulla radio trasmittente, toccare il
modello e scegliere **Send model**; la radio ricevente chiede conferma del nome
del file in arrivo prima di accettarlo.

## Selezione di un modello

Toccare **Model select** per visualizzare l'elenco dei modelli.

!!! note "Conversione dei modelli dopo un aggiornamento di Ethos"
    Ethos converte ciascun modello individualmente la prima volta che viene
    *selezionato* dopo un aggiornamento di versione, e non tutti insieme al
    momento dell'aggiornamento — non si nota alcun ritardo ed è sicuro farlo
    in qualsiasi momento successivo, anche con una release di Ethos ancora
    più recente. La data di **Last Modification** in fondo alla schermata di
    selezione viene aggiornata quando avviene una conversione (o quando si
    modifica il modello — altrimenti rimane invariata).

**Selezione rapida** — un tocco prolungato o una pressione lunga di `ENT`
sull'icona di un modello vi commuta immediatamente.

**Menu di gestione del modello** — toccare un modello per evidenziarlo,
toccarlo nuovamente per aprire il menu:

- **Set current model**
- **Clone** — duplica il modello. Un clone riceve automaticamente un nuovo
  numero di ricevitore; se invece si riassegna il numero di ricevitore
  dell'originale, funziona senza necessità di rieseguire il binding.
- **Change folder**
- **Send**/**Receive** — verso o da un'altra radio, come sopra.
- **Delete** — disponibile solo per un modello che non sia quello corrente.
