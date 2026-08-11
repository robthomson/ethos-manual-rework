---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Disattivata per impostazione predefinita. Imposta la radio come **Master**
(la radio dell'istruttore, che riceve fino a 16 comandi dalla radio
studente) o **Slave** (la radio dell'allievo, che trasferisce al master un
numero configurabile di canali).

## Modalità Master

![Modalità Master](../assets/model-trainer-master.png)
![Opzioni Trainer](../assets/model-trainer-options.png)

### Modalità di collegamento

![Opzioni modalità di collegamento](../assets/model-trainer-link-mode-options.png)

- **Cavo Trainer** — un cavo audio mono da 3,5 mm tra le due radio.
- **Bluetooth** —

  ![Collegamento Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Modalità** — velocità normale o alta velocità; per ottenere una
    latenza inferiore è consigliabile l'alta velocità, se entrambe le
    radio la supportano.

    ![Modalità Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Nome locale** — il nome del BT locale che verrà visualizzato negli
    altri dispositivi (predefinito `FrSkyBT`, modificabile).
  - **Indirizzo locale** — l'indirizzo Bluetooth locale della radio.
  - **Indirizzo distante** — l'indirizzo del dispositivo remoto, una volta
    stabilito il collegamento.
  - **Cerca dispositivi** (disponibile solo se la modalità Trainer è
    Master) — mette la radio in modalità di ricerca BT:

    ![Ricerca in corso](../assets/model-trainer-link-mode-bt-search.png)
    ![In attesa](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Selezione dispositivo](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Connesso](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Connetti ultimo dispositivo** / **Reset modulo** — si collega
    all'ultimo dispositivo configurato, oppure resetta il modulo e
    cancella completamente le impostazioni di configurazione.

- **SBUS modulo esterno** — fornisce un ingresso SBUS sul pin PXX IN
  dell'alloggiamento del modulo esterno, per installare un ricevitore
  FrSky con uscita SBUS (ad es. Archer RS) come estremità ricevente di un
  collegamento trainer wireless, consentendo a **qualsiasi** radio FrSky
  di fungere da lato allievo (buddy box), collegata a tale ricevitore.
- **CPPM modulo esterno** — allo stesso modo, tramite un ingresso CPPM,
  da utilizzare con un ricevitore legacy dotato di uscita CPPM.

### Condizione attiva

![Condizione attiva](../assets/model-trainer-active-condition.png)

Un interruttore o un pulsante, un interruttore di funzione, un
interruttore logico, la posizione del trim o la modalità di volo che,
quando è attivo, trasferisce il controllo del modello alla radio dello
studente.

### Canali del trainer

![Modifica condizione attiva](../assets/model-trainer-active-condition-edit.png)

È possibile trasferire fino a 16 canali dalla radio studente alla radio
master quando la condizione attiva è vera. Tocca ogni canale per
configurarlo singolarmente:

- **Condizione attiva** — ogni singolo canale slave può anche essere
  controllato dalla sorgente selezionata, ad esempio per disattivare
  l'ingresso dell'elevatore dello studente durante una parte della
  sessione.
- **Modalità** — **OFF** (disattiva il canale per l'uso del trainer),
  **Aggiungi** (modalità additiva, in cui i segnali master e slave
  vengono sommati, in modo che sia l'insegnante che lo studente possano
  agire sulla funzione) oppure **Sostituisci** (la modalità di utilizzo
  normale: l'allievo ha il pieno controllo di questo canale quando è
  attiva).
- **Percentuale** — scala l'ingresso Slave, normalmente impostata al 100%.
- **Destinazione** — mappa il canale della radio slave alla funzione
  corrispondente.

Consulta [Guida pratica: ripresa istantanea del
controllo](../how-to/instant-takeback.md) per un esempio pratico in cui
l'istruttore riprende immediatamente il controllo tramite un interruttore,
e [Ignora ingresso
trainer](../getting-started/user-interface-and-navigation.md#choosing-a-source)
per escludere il movimento degli stick dello studente da un interruttore
logico che rileva gli stick dell'istruttore.

## Modalità Slave

![Modalità Slave](../assets/model-trainer-slave-mode.png)

- **Modalità di collegamento** — la stessa scelta tra cavo trainer,
  Bluetooth o modulo esterno SBUS/CPPM della modalità Master (con gli
  stessi campi Bluetooth **Modalità**/**Nome locale**/**Indirizzo
  locale**/**Indirizzo distante**).

  ![Modalità di collegamento Slave](../assets/model-trainer-slave-link-mode.png)

- **Intervallo canali** — seleziona quale gamma di canali di questa radio
  viene trasferita alla radio master.

  ![Canali Slave](../assets/model-trainer-slave-channels.png)
  ![Modifica canale Slave](../assets/model-trainer-slave-channel-edit.png)
