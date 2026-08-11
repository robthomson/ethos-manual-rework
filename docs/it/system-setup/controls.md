---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Comandi

![Stick](../assets/system-sticks.png)

Nel menu sono indicati come **Stick** — modalità stick e ordine
predefinito di assegnazione dei canali.

## Modalità stick

- **Modalità 1** — throttle e alettone sullo stick destro, elevatore e
  timone su quello sinistro.
- **Modalità 2** — Gas - Throttle e timone sullo stick di sinistra,
  alettone ed elevatore su quello di destra.

Per impostazione predefinita gli stick hanno i nomi delle modalità di stick
standard del settore e possono essere rinominati a piacere.

## Ordine dei canali

L'ordine dei canali definisce l'ordine in cui i quattro ingressi degli stick
vengono assegnati ai canali quando si crea un nuovo modello con le procedure
guidate di [Selezione modello](../model-setup/model-select.md). L'ordine
predefinito è **AETR**. Se ci sono più superfici di ogni tipo, verranno
raggruppate a meno che non sia attiva l'opzione [I primi quattro canali sono
fissi](#first-four-channels-fixed) — ad esempio, per due alettoni l'ordine
dei canali sarà **AAETR**.

![Ordine dei canali del ricevitore](../assets/system-sticks-rx-order.png)

## I primi quattro canali sono fissi {: #first-four-channels-fixed }

Se questa opzione è attivata, il raggruppamento dei canali non avverrà mai
sui primi quattro canali. Con l'ordine **AETR** e un modello con 2 alettoni,
1 elevatore, 1 motore, 1 timone e 2 flap, la procedura guidata crea un
ordine di canali **AETRAFF** (i canali 1–4 restano esattamente A-E-T-R, con
il secondo alettone e i due flap accodati) invece di **AAETRFF**. È questa
l'impostazione che fa creare alla procedura guidata modelli adatti ai
ricevitori stabilizzati SRx, che richiedono tale disposizione fissa.

![Ordine fisso a 4 canali](../assets/system-sticks-4ch-fixed.png)
