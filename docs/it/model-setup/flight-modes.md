---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Fasi di volo

![Fasi di volo](../assets/model-fm.png)

Le fasi di volo (modalità di volo) permettono a un interruttore di selezionare
comportamenti distinti per lo stesso modello — un aliante potrebbe usare
Lancio/Crociera/Velocità/Termica, un modello a motore Normale/Decollo/
Atterraggio, un elicottero Normale (avviamento rotore, decollo/atterraggio) /
Idle Up 1 (acrobazia) / Idle Up 2 (3D). Sollevano il pilota dalla maggior parte
del lavoro di commutazione manuale e di ri-trimmaggio: una fase di volo può
disporre di trim indipendenti propri e può condizionare sia le
[Variabili](variables.md) sia i [Mix](mixes.md) — insieme, è sufficiente per
gestire una complessità reale. Vedi [Esempio base per ala
fissa](../tutorials/basic-fixed-wing.md) per l'applicazione delle fasi di volo a
un modello reale.

Per impostazione predefinita non è definita alcuna fase di volo. Tocca la fase
di volo predefinita e seleziona **Modifica** per rinominarla, oppure
**Aggiungi** per crearne una nuova — fino a un massimo di 20.

## Nome

Un nome descrittivo — Crociera, Velocità, Termica, Decollo, Atterraggio o
qualsiasi altro sia appropriato.

## Condizione attiva

![Scheda della fase di volo](../assets/model-fm-form.png)

Una nuova fase di volo è inizialmente inattiva (`---`). Una volta impostata, può
essere condizionata scegliendo tra posizioni di interruttori o pulsanti,
interruttori di funzione, interruttori logici, un evento di sistema come il
taglio o il mantenimento del Gas - Throttle, oppure le posizioni dei trim.

La fase di volo **predefinita** non ha alcuna condizione attiva — è quella
attiva ogni volta che nessun'altra condizione di fase di volo risulta vera. È
sempre attiva una sola fase di volo alla volta: la prima (in ordine di priorità)
la cui condizione è vera in quel momento. La fase di volo attiva è indicata in
grassetto.

!!! warning "Aggiungere una fase di volo a un modello esistente"
    Una fase di volo appena aggiunta è, per impostazione predefinita, attiva in
    ogni mix che già dipende dalle fasi di volo — verifica che ciascuno di questi
    mix continui a comportarsi correttamente, in particolare un mix **Blocco**
    che blocca un canale su una specifica fase di volo.

## Dissolvenza in ingresso e in uscita

Tempi di transizione per passare in modo graduale da una fase di volo all'altra
(ad esempio 1 secondo in ciascuna direzione) — hanno effetto solo sui mix che
dipendono a loro volta dalle fasi di volo.

## Gestione delle fasi di volo

![Sposta fase di volo](../assets/model-fm-move.png)
![Selezione per lo spostamento](../assets/model-fm-move-select.png)
![Fasi 0-3](../assets/model-fm-0to3.png)

Tocca una fase di volo per **Modifica**, **Aggiungi**, **Clona** o **Cancella**.
Una fase di volo **clonata** eredita le impostazioni della fase di origine in
ogni mix che utilizza le fasi di volo — stesso comportamento, stesso stato
attivo/inattivo — per questo il clone viene aggiunto, per impostazione
predefinita, come ultima fase di volo, in modo da non interferire con quelle
esistenti. **Muovi** modifica la priorità di una fase di volo: la priorità segue
l'ordine crescente e (come indicato sopra) la prima la cui condizione è vera è
quella attiva.
