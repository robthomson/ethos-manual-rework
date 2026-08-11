---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trim

![Trim](../assets/model-trims.png)

Consente di configurare per ogni stick l'intervallo del trim, l'ampiezza
del passo e il comportamento, oltre al cross trim e al trim istantaneo.
Le radio **X20 Pro/R/RS** e **X18** dispongono di due interruttori di trim
aggiuntivi, **T5**/**T6**, utili per le regolazioni in volo oltre ai quattro
stick principali:

![Trim T5/T6](../assets/model-trims-pro-t5-t6.png)

Ogni stick dispone di un proprio set indipendente di impostazioni di trim.

## Impostazioni dei trim {: #trim-settings }

- **Intervallo** — per impostazione predefinita ±25%, regolabile fino alla
  corsa completa dello stick, ±100%. Nella schermata principale, un trim
  con intervallo predefinito indica valori da −100 a 100; un trim a
  intervallo completo (100%) indica valori da −400 a 400 (4× l'intervallo
  normale).

  !!! warning
      Ampliando l'intervallo, tenere premuta troppo a lungo una levetta di
      trim può aggiungere trim a sufficienza da rendere il modello
      impilotabile.

- **Step** — granularità dell'interruttore di trim: **Extra fine**,
  **Fine**, **Medio**, **Grossolano**, **Esponenziale** (fine in prossimità
  del centro, grossolano allontanandosi) oppure **Personalizzato** (una
  percentuale specifica per ogni clic).

  ![Opzioni di step](../assets/model-trims-step-options.png)

  | Step | µs per clic (intervallo 25%) |
  |---|---|
  | Extra fine | 0.5 |
  | Fine | 1 |
  | Medio | 2 |
  | Grossolano | 4 |
  | Esponenziale | 0.3–16 |

  Personalizzato, con intervallo al 25%: step 1% = 1µs/clic, step 100% =
  128µs/clic. Con intervallo al 100%: step 1% = 5µs/clic, step 100% =
  512µs/clic.

## Modalità

![Modalità del trim dell'elevatore](../assets/model-trims-mode-elevator.png)

Per impostazione predefinita i trim sono sempre attivi, ma la voce **Modo**
ne modifica il comportamento. I trim vengono riportati a 0 quando si cambia
modalità.

- **OFF** — il trim è completamente disabilitato.

  ![Modo: OFF](../assets/model-trims-mode-option-off.png)

  Utile, ad esempio, nei modelli elettrici in cui il trim del gas non è
  necessario: il trim così liberato può quindi essere
  [riutilizzato per regolare una Var](variables.md).

- **Modo Facile** — un solo valore di trim condiviso da tutte le modalità
  di volo. È la scelta abituale per i trim degli alettoni e del timone,
  dato che questi trim non variano tra le varie modalità di volo.

  ![Modo: Facile](../assets/model-trims-mode-option-easy.png)

- **Trim indipendente per modalità di volo** — il trim influisce solo sulla
  modalità di volo attiva. È la scelta abituale per il trim dell'elevatore,
  poiché il trim dell'elevatore richiesto varia in genere per ogni modalità
  di volo (ad esempio a causa delle differenze di curvatura dell'ala): in
  effetti, questo è spesso il motivo principale per cui si implementano le
  modalità di volo.

  ![Modo: indipendente per modalità di volo](../assets/model-trims-mode-option-fm.png)

- **Ad hoc** — comportamento completamente personalizzato, costruito
  tramite i **comportamenti** che si aggiungono manualmente.

### Comportamenti di trim personalizzati

![Aggiungi un comportamento](../assets/model-trims-mode-elevator-add-behaviour.png)
![Opzioni di comportamento](../assets/model-trims-mode-elevator-edit-behaviour.png)

Ogni linea di comportamento presenta una condizione e una delle seguenti
opzioni:

- **Scollegato** — disabilita il trim in modo selettivo in presenza di
  questa condizione (anziché disattivarlo del tutto impostando Modo = OFF).

  ![Scollegato](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Condizione per Scollegato](../assets/model-trims-mode-unplugged-select.png)

- **Normale** (predefinito) — comportamento di trim ordinario.
- **Uguale (a un altro Trim)** — il Trim di questa condizione è configurato
  per essere uguale al Trim di un'altra condizione.

  ![Uguale](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Offset + (un altro Trim)** — il Trim di questa condizione viene sommato
  al Trim di un'altra condizione.

  ![Offset](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Esempio di Trim offset** — un aliante con un trim dell'elevatore di base
per la modalità **Crociera** e trim dipendenti per **Velocità** e
**Termica**:

![Selezione FM5 Speed](../assets/model-trims-mode-elevator-custom-select.png)
![Selezione FM4 Thermal](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Regolare l'elevatore per il volo livellato nella modalità di volo
   predefinita (Cruise).
2. Aggiungere un comportamento: **Offset + Default**, con la condizione
   `FM5(Speed)`. Quando viene selezionata la modalità Speed, qualsiasi
   regolazione del Trim verrà salvata come un offset rispetto al valore del
   Trim di base in Cruise: separato, ma comunque dipendente da esso.

   ![Offset per Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Allo stesso modo, aggiungere un secondo comportamento: **Offset +
   Default**, con la condizione `FM4(Thermal)`. (Una volta configurato il
   primo comportamento, nella finestra di dialogo a discesa compaiono anche
   le opzioni `Equal FM5(Speed)` e `Offset + FM5(Thermal)`, poiché ora è
   possibile fare riferimento anche a quel comportamento.)

   ![Offset per Speed e Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Con questa configurazione, se in seguito il Trim di crociera di base deve
essere modificato (ad esempio perché hai alterato il C di G dell'aliante),
anche i trim di Speed e Thermal saranno modificati automaticamente della
stessa entità, poiché sono offset rispetto ad esso e non valori
indipendenti.

- **Audio** — per ogni Trim l'audio può essere disattivato se gli annunci
  standard non sono desiderati, ad esempio se il Trim è stato riutilizzato
  per altro scopo.

## Trim aggiuntive

![Aggiungi Trim extra](../assets/model-trims-add-trim-select.png)
![Impostazioni del Trim extra](../assets/model-trims-add-trim-edit.png)

Il pulsante **Aggiungi Trim extra** crea un Trim ulteriore rispetto ai
quattro stick standard (e a T5/T6): **Nome**, sorgenti **Su**/**Giù** che lo
comandano, oltre alle stesse opzioni **Intervallo**, **Step**, **Modo** e
**Audio** descritte sopra.

## Cross trim

![Cross Trim](../assets/model-trims-cross.png)
![Modifica del Cross Trim](../assets/model-trims-cross-edit.png)

Permette di scegliere quale interruttore di trim regola effettivamente
ciascuno stick, ossia consente di comandare il trim di uno stick con un
comando fisico di trim diverso da quello abituale. (I trim T5 e T6 sono
disponibili solo su X20 Pro e X18.)

## Trim istantaneo {: #instant-trim }

![Trim istantaneo](../assets/model-trims-instant-trim.png)

Quando questa funzione è attiva, aggiunge le posizioni correnti degli stick
ai rispettivi valori dei trim di default (anche dei cross trim). È meglio
assegnarla a un interruttore che puoi raggiungere senza lasciare gli stick:
attivandola mentre voli in linea d'aria imposti istantaneamente i trim,
evitando di premere ripetutamente le levette dei trim quando i trim sono
molto lontani dalla regolazione corretta. Va disattivata dopo il volo di
trimmaggio, per evitare di alterare di nuovo i trim per sbaglio.

!!! note
    Il trim istantaneo è attivo solo quando si è in una delle viste
    principali della radio.

## Sposta i trim ai SubTrim

![Muove i trim ai subtrim](../assets/model-trims-move-trims-to-subtrims.png)

Dopo aver regolato il modello per il volo livellato, questa funzione sposta
il valore di trim di un canale (ad esempio dell'elevatore) nella relativa
impostazione [Subtrim](outputs.md) e riporta a zero il trim nella schermata
principale: in questo modo è facile verificare che i trim di volo non si
siano spostati.

Quando si utilizzano le modalità di volo, un canale può avere più di un
valore di trim rilevante, mentre il parametro Subtrim in Outputs è
un'impostazione globale che si applica a tutte le modalità di volo. La
funzione ne tiene conto: prende il trim della modalità di volo
**attualmente selezionata**, ne trasferisce il contenuto al Subtrim,
resetta quel trim e regola tutti gli *altri* trim interessati delle
modalità di volo sullo stesso canale, in modo che le posizioni delle
superfici di controllo in ogni modalità di volo rimangano complessivamente
invariate.

!!! tip
    Esegui sempre questa operazione dalla stessa modalità di volo "base"
    (ad esempio Cruise su un aliante) per essere coerente: rispettando
    questa regola può essere ripetuta senza problemi.

Valori di trim o subtrim elevati generano corse molto asimmetriche: sarebbe
più saggio correggere il problema meccanicamente. Occorre fare ogni sforzo
per avere 90 gradi ai leveraggi quando le superfici sono in posizione
neutra (fanno eccezione i flap, dove si sacrifica la corsa verso l'alto per
massimizzare quella verso il basso); dopo aver avvicinato il più possibile i
collegamenti a 90 gradi, si dovrebbe usare il **PWM Center** per portarli
esattamente a 90 gradi.
