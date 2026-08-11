---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Verifica hardware](../assets/system-hardware-check-x20s.png)

Test e calibrazione dei comandi fisici della radio, definizione dei tipi di
interruttore e mappatura dei tasti home.

## Verifica hardware {: #hardware-check }

Consente di sollecitare ogni ingresso fisico per verificare che ciascuno
venga rilevato correttamente.

![Verifica hardware X20 Pro](../assets/system-hardware-check-x20pro.png)
![Verifica hardware X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — verifica anche i due pulsanti a ritenuta **K** e **L**
  sulle spalle posteriori, oltre ai trim aggiuntivi **T5**/**T6**.
- **X18** — verifica anche i trim aggiuntivi **T5**/**T6**.

## Calibrazione degli analogici {: #analogs-calibration }

![Calibrazione analogici](../assets/system-hardware-analogs-calibration.png)

Indica alla radio l'esatta posizione del centro e dei fine corsa di ogni
stick, potenziometro e slider. Viene eseguita automaticamente al primo
avvio; ripeterla dopo la sostituzione di uno stick, di un potenziometro o
di uno slider.

## Calibrazione del giroscopio

![Calibrazione giroscopio](../assets/system-hardware-gyro-calibration.png)

Calibra il giroscopio integrato affinché gli ingressi basati
sull'inclinazione rispondano correttamente all'inclinazione della radio: la
posizione "in piano" diventa quella in cui normalmente si tiene la radio.
Anche questa procedura viene eseguita automaticamente al primo avvio.

## Filtro analogici

Un filtro ADC on/off per gli stick, attivo per impostazione predefinita:
riduce le oscillazioni attorno al centro stick. Questa è l'impostazione
**globale**; esiste anche una sovrascrittura del filtro analogici
**per modello** in [Modifica modello](../model-setup/model-edit.md).

## Impostazioni potenziometri/slider {: #potssliders-settings }

Consente di rinominare i potenziometri e gli slider. La **X20 Pro/R/RS**
supporta inoltre due potenziometri aggiuntivi, **Ext1**/**Ext2**,
tipicamente utilizzati per gli stick a 3 assi.

![Valori ADC, potenziometri](../assets/system-hardware-pots-x20s.png)
![Valori ADC, potenziometri (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Impostazioni interruttori {: #switches-settings }

![Interruttori](../assets/system-hardware-switches.png)

- **Ritardo rilevamento posizione centrale** — impedisce che una commutazione
  rapida alto→basso (o basso→alto) di un interruttore a 3 posizioni registri
  momentaneamente la posizione centrale; la posizione centrale dovrebbe
  essere rilevata solo quando l'interruttore vi si ferma effettivamente. Il
  valore predefinito è 0 ms, scelto per adattarsi al rilevamento di
  "auto-verifica" dei ricevitori stabilizzati FrSky sul CH12.
- **Tipo di interruttore** — ciascuno degli interruttori SA–SJ può essere
  definito come **None**, **Momentary**, **2 POS** o **3 POS**, consentendo di
  scambiare le funzionalità tra gli interruttori fisici (ad esempio
  assegnando all'interruttore momentaneo SH il ruolo normalmente svolto dal
  bipolare SF), compatibilmente con quanto il cablaggio della radio supporta
  effettivamente (un ruolo a 3 posizioni generalmente non può essere
  assegnato a un hardware non cablato per tale scopo).

  ![Opzioni interruttore](../assets/system-hardware-switches-options.png)
  ![Interruttori aggiuntivi](../assets/system-hardware-switches-2.png)

- **Rinomina** — gli interruttori possono essere rinominati da SA–SJ a nomi
  personalizzati; i nomi sono globali per tutti i modelli.
- **X20 Pro** — aggiunge i pulsanti **K**/**L** sulle spalle posteriori,
  oltre alle posizioni **M**/**N** se cablate (tipicamente per interruttori
  in testa agli stick).

## Mappatura tasti home

Riassegna la destinazione dei tasti home `SYS`, `MDL` e `DISP` (`TELE` sulle
radio meno recenti).

- **`DISP`** — sia la pressione breve sia quella prolungata possono essere
  riassegnate a qualsiasi pagina Modello, pagina Sistema, Configura
  schermate, Home o al Registro dati di volo. Per coerenza con la serie X10,
  la pressione prolungata di `DISP` è convenzionalmente impostata su
  Configura schermate.
- **`SYS`/`MDL`** — solo la pressione prolungata è riassegnabile (allo stesso
  insieme di destinazioni); una pressione breve apre sempre rispettivamente
  la sezione Sistema o Modello.

## Opzioni hardware specifiche per radio {: #radio-specific-hardware-options }

- **Attivazione degli upgrade haptic degli stick** (X20 Pro, X20R) — le X20
  Pro AW e X20RS sono equipaggiate con stick MC20R dotati di motori haptic
  per la vibrazione degli stick; se gli stick MC20R sono stati installati in
  retrofit su una X20 Pro o X20R, occorre abilitarli qui (vedere
  [Funzioni speciali](../model-setup/special-functions.md) per la
  configurazione dei pattern haptic veri e propri).

  ![Haptic (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptic (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Opzione encoder** (X20 Pro AW, X20R/RS) — queste radio dispongono di un
  encoder rotativo più sensibile; abilitare i **mezzi passi** per attenuarne
  la reattività.

  ![Opzione encoder (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Ispettore dei valori ADC {: #adc-value-inspector }

Mostra i valori grezzi della conversione analogico-digitale letti dalla CPU
per ogni ingresso analogico:

![Verifica ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Verifica ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 stick sinistro orizzontale, 2 stick sinistro verticale, 3 stick
destro verticale, 4 stick destro orizzontale, 5 Pot 1, 6 Pot 2, 7 slider
centrale, 8 slider sinistro, 9 slider destro.

**X20 Pro**: come sopra, ma con due canali aggiuntivi per potenziometri
esterni (7 Ext1, 8 Ext2 — ad esempio potenziometri montati sugli stick)
inseriti prima degli slider, che diventano quindi 9 slider centrale,
10 slider sinistro, 11 slider destro.
