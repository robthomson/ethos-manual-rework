---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Disattivato per impostazione predefinita. Imposta la radio come **Master**
(la radio dell'istruttore, che riceve fino a 16 comandi dall'allievo) o
**Slave** (la radio dell'allievo, che invia un numero configurabile di
canali all'istruttore).

## Modalità Master

![Modalità Master](../assets/model-trainer-master.png)
![Opzioni trainer](../assets/model-trainer-options.png)

### Modalità di collegamento

![Opzioni modalità di collegamento](../assets/model-trainer-link-mode-options.png)

- **Cavo trainer** — un cavo audio mono da 3,5 mm tra le due radio.
- **Bluetooth** —

  ![Collegamento Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Modalità** — normale o alta velocità; utilizza l'alta velocità per
    una latenza inferiore, se entrambe le radio la supportano.

    ![Modalità Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Nome locale** — il nome BT mostrato agli altri dispositivi
    (predefinito `FrSkyBT`, modificabile).
  - **Indirizzo locale** — l'indirizzo Bluetooth di questa radio.
  - **Indirizzo remoto** — l'indirizzo della radio accoppiata, una volta
    stabilito il collegamento.
  - **Cerca dispositivi** (solo in modalità Master) — esegue la scansione
    dei dispositivi nelle vicinanze:

    ![Ricerca in corso](../assets/model-trainer-link-mode-bt-search.png)
    ![In attesa](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Selezione dispositivo](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Connesso](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Connetti ultimo dispositivo** / **Reset modulo** — riconnette
    all'accoppiamento precedente, oppure cancella completamente la
    configurazione del modulo Bluetooth.

- **Modulo esterno SBUS** — un ingresso SBUS sul pin PXX-IN del vano del
  modulo esterno, per installare un ricevitore FrSky con uscita SBUS (ad
  es. Archer RS) come estremità ricevente di un collegamento wireless,
  consentendo a **qualsiasi** radio FrSky di fungere da lato allievo
  (buddy box), collegata a tale ricevitore.
- **Modulo esterno CPPM** — stessa idea tramite un ingresso CPPM, per un
  ricevitore datato con uscita CPPM.

### Condizione di attivazione

![Condizione di attivazione](../assets/model-trainer-active-condition.png)

Un interruttore/pulsante, interruttore funzione, interruttore logico,
posizione di trim o fase di volo che, quando attivo, cede il controllo
all'allievo.

### Canali trainer

![Modifica condizione di attivazione](../assets/model-trainer-active-condition-edit.png)

È possibile trasferire fino a 16 canali dall'allievo al master mentre la
condizione di attivazione è vera. Tocca un canale per configurarlo
singolarmente:

- **Condizione di attivazione** — un'esclusione specifica per canale, ad
  esempio per disabilitare solo il comando di profondità dell'allievo
  durante una parte della sessione.
- **Modalità** — **OFF** (disabilitato per l'uso trainer), **Add** (i
  segnali del master e dell'allievo si sommano, così entrambi possono
  agire contemporaneamente sul comando) oppure **Replace** (la modalità
  normale: l'allievo ha il pieno controllo di questo canale mentre è
  attivo).
- **Percentuale** — scala il comando dell'allievo, normalmente 100%.
- **Destinazione** — a quale funzione viene assegnato il canale
  dell'allievo.

Consulta [Guida pratica: ripresa istantanea del
controllo](../how-to/instant-takeback.md) per un esempio pratico in cui
l'istruttore riprende immediatamente il controllo tramite un interruttore,
e [Ignora ingresso
trainer](../getting-started/user-interface-and-navigation.md#choosing-a-source)
per escludere il movimento degli stick dell'allievo da un interruttore
logico che monitora gli stick dell'istruttore.

## Modalità Slave

![Modalità Slave](../assets/model-trainer-slave-mode.png)

- **Modalità di collegamento** — la stessa scelta tra cavo trainer,
  Bluetooth o modulo esterno SBUS/CPPM disponibile in modalità Master
  (con gli stessi campi Bluetooth **Modalità**/**Nome
  locale**/**Indirizzo locale**/**Indirizzo remoto**).

  ![Modalità di collegamento Slave](../assets/model-trainer-slave-link-mode.png)

- **Intervallo canali** — quale intervallo di canali di questa radio viene
  inviato al master.

  ![Canali Slave](../assets/model-trainer-slave-channels.png)
  ![Modifica canale Slave](../assets/model-trainer-slave-channel-edit.png)
