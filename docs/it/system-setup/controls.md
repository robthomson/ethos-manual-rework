---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Comandi

![Stick](../assets/system-sticks.png)

Nel menu sono indicati come **Stick** — modalità degli stick e ordine
predefinito di assegnazione dei canali.

## Modalità stick

- **Mode 1** — gas e alettoni sullo stick destro, profondità e timone
  sul sinistro.
- **Mode 2** — gas e timone sullo stick sinistro, alettoni e profondità
  sul destro.

Per impostazione predefinita gli stick prendono il nome dalle modalità
standard del settore e possono essere rinominati.

## Ordine dei canali

Definisce l'ordine con cui i quattro comandi degli stick vengono assegnati
ai canali quando un nuovo modello viene creato dalle procedure guidate di
[Selezione modello](../model-setup/model-select.md). Il valore predefinito è
**AETR**. Quando una cellula dispone di più superfici dello stesso tipo,
queste vengono raggruppate, a meno che non sia attiva l'opzione [Primi
quattro canali fissi](#first-four-channels-fixed) — ad esempio, con 2
alettoni si ottiene **AAETR**.

![Ordine dei canali del ricevitore](../assets/system-sticks-rx-order.png)

## Primi quattro canali fissi {: #first-four-channels-fixed }

Con questa opzione attiva, i primi quattro canali non vengono mai
raggruppati. Con ordine **AETR** e una cellula dotata di 2 alettoni, 1
profondità, 1 motore, 1 timone e 2 flap, la procedura guidata produce
**AETRAFF** (i canali 1–4 restano esattamente A-E-T-R, con il secondo
alettone e i due flap accodati) invece di **AAETRFF**. È questa
l'impostazione che fa creare alla procedura guidata modelli adatti ai
ricevitori stabilizzati SRx, che richiedono tale disposizione fissa.

![Ordine fisso a 4 canali](../assets/system-sticks-4ch-fixed.png)
