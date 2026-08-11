---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Timer

![Timer](../assets/model-timers.png)

Otto timer completamente programmabili, ciascuno con conteggio crescente o
decrescente. Puoi aggiungerne uno toccando il simbolo **+** accanto alle
intestazioni delle colonne, oppure selezionando **Aggiungi** più sotto.
Toccando un timer si apre un menu a comparsa che consente di azzerare,
modificare, aggiungere, spostare o copiare/incollare il timer.

![Modifica timer](../assets/model-timer1-edit.png)

## Campi comuni (conteggio decrescente e crescente)

- **Valore** — il valore attuale del timer.
- **Nome** — permette di dare un nome al timer.
- **Modo** — **Up** (crescente) o **Down** (decrescente).
- **Valore iniziale** (solo conteggio decrescente) — il valore da cui parte il
  conteggio alla rovescia.
- **Valore allarme** (solo conteggio crescente) — il valore al quale il timer è
  considerato scaduto; il conteggio prosegue oltre questo valore, ma nei widget
  timer viene visualizzato in rosso.
- **Condizione di avvio** — avvia il timer. Se la **Condizione di arresto** è
  lasciata al valore predefinito, la sola condizione di avvio controlla sia
  l'avvio *sia* l'arresto. In caso contrario, il timer parte la prima volta che
  la condizione di avvio diventa vera e continua a funzionare da quel momento.
- **Condizione di arresto** — se non lasciata al valore predefinito, controlla
  il timer una volta avviato: fermo quando è vera, in funzione quando è falsa.
  Nell'esempio seguente, un timer parte quando `ThrottleActive` diventa vero e
  si ferma quando la telemetria non è più attiva:

  ![Condizione di arresto](../assets/model-timer1-edit-stop.png)

- **Sorgente di temporizzazione proporzionale** — con `---` il conteggio avviene
  in tempo reale. Qualsiasi altra sorgente (ad esempio lo stick del gas o il
  canale del gas) modifica la velocità del timer: a −100% il timer è fermo, a
  +100% procede alla velocità reale e nei valori intermedi varia in modo
  proporzionale.
- **Reset** — un interruttore, un interruttore di funzione, un interruttore
  logico o una posizione di trim che azzera il timer; il timer resta azzerato
  per tutto il tempo in cui la condizione è vera.
- **Persistente** — mantiene il valore del timer allo spegnimento o al cambio di
  modello, ricaricandolo al successivo utilizzo del modello.
- **Voce** — quale [pacchetto vocale](../system-setup/general.md#audio-settings)
  annuncia questo timer.

## Azioni audio

![Aggiungi azione audio](../assets/model-timer1-add-action.png)
![Tipo di azione](../assets/model-timer1-action-type-select.png)
![Azione di conto alla rovescia](../assets/model-timer1-action-countdown.png)

Configurazione degli avvisi completamente flessibile, specifica per ciascun
timer. Ogni azione ha un tipo — **Countdown** (annuncio vocale), **Beep
countdown** (segnali acustici anziché voce), **Play file** (riproduci file) o
**Play value** (riproduci valore) — oltre ai seguenti parametri:

- **Start** — il valore da cui inizia il conto alla rovescia di questa azione.
- **Step** — intervallo tra gli annunci, fino a 10 minuti (600 s).
- **Haptic** — accompagna l'annuncio con una vibrazione.

Una tipica sequenza di tre azioni:

![Riepilogo azioni](../assets/model-timer1-actions-summary.png)
![Azioni del timer 2](../assets/model-timer2-actions-summary.png)

1. Conto alla rovescia vocale a partire da 2:00 rimanenti, ogni 30 s, con
   vibrazione.
2. Conto alla rovescia acustico a partire da 0:10 rimanenti, ogni 1 s, con
   vibrazione.
3. Un file personalizzato (ad esempio `timer-1-elapsed`) riprodotto allo
   scadere, con vibrazione.

Puoi aggiungere altre azioni con **Aggiungi**; l'elenco viene eseguito in ordine
di priorità, con la **priorità più alta per ultima**.

Consulta anche il [widget Timer Log](../displays/index.md#widget-types) per uno
storico delle esecuzioni precedenti del timer.

![Widget timer](../assets/model-timers-widget.png)
