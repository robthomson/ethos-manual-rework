---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Avviso di capacità della batteria

Avviso basato sulla **capacità consumata** (mAh) anziché sulla tensione — una
misura più diretta di quanta parte del pacco è stata effettivamente utilizzata. Ci sono due
modi per ottenerlo, a seconda dell'hardware installato.

## Opzione A: un ESC della serie Neuron

Gli ESC FrSky della serie Neuron riportano direttamente il consumo — non serve alcun sensore
calcolato. Nelle [Opzioni del ricevitore imposta la Porta di
telemetria](../system-setup/devices.md) sull'opzione S.Port, collega la porta telemetrica del
Neuron e attiva l'opzione [«Scopri nuovi
sensori»](../model-setup/telemetry.md#discovering-sensors) — il sensore di interesse
è **Consumo ESC**.

1. Aggiungi un [interruttore logico](../model-setup/logical-switches.md) su `Consumo
   ESC`, vero quando il consumo supera, ad esempio, i 900 mAh — ovvero circa il 60% di un pacco dimensionato per
   atterrare avendo ancora circa il 30% di riserva.
2. Aggiungi una [funzione speciale «Riproduci
   audio»](../model-setup/special-functions.md), con condizione attiva il nuovo
   interruttore logico e, in «Sequenza», un comando **Riproduci valore** per `Consumo ESC`.

Come ulteriore salvaguardia, gli ESC Neuron riportano anche la **Tensione ESC** —
imposta un secondo interruttore logico nello stesso modo descritto in [Avviso di bassa tensione
della batteria](low-battery-warning.md) (al di sotto di 3,4 V per cella per 4 secondi — ad esempio
13,6 V per una LiPo 4S), con la propria funzione «Riproduci audio» ripetuta ogni 5
secondi.

## Opzione B: un sensore di corrente + sensore calcolato

Se l'ESC non dispone di questa funzionalità, un sensore di corrente (ad esempio della
serie FrSky FASxxx) insieme a un [sensore di **Consumo**
calcolato](../model-setup/telemetry.md#calculated-sensors) svolge lo stesso
compito.

### 1. Collegamento e ricerca

![Sensore di corrente](../assets/how-to-consumption-telemetry-current-sensor.png)

Collega la porta telemetrica del sensore di corrente al ricevitore tramite un cavo S.Port e attiva
l'opzione «Scopri nuovi sensori» — il sensore comparirà come **Corrente**. Imposta il suo
**Intervallo** in base al sensore (ad esempio 0-100A per un FAS100):

![Modifica sensore di corrente](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Creare il sensore calcolato Consumo

![Creazione sensore calcolato](../assets/how-to-consumption-create-calc-select.png)
![Sensore Consumo](../assets/how-to-consumption-create-calc-sensor.png)

In Telemetria clicca su **Crea sensore calcolato** → **Consumo**. Configura l'unità di misura
su `mAh` e l'**Intervallo** in base alla capacità della tua lipo (ad esempio 2800 mAh); la **Sorgente**
su `Corrente`.

![Modifica sensore](../assets/how-to-consumption-sensor-edit.png)
![Modifica sensore 2](../assets/how-to-consumption-sensor-edit2.png)

Imposta il **Reset** sull'evento di sistema `!Telemetria Attiva` — seleziona prima **Telemetria
attiva**, premi a lungo `ENT` e scegli **Inverti** — in modo che il totale progressivo
venga resettato automaticamente quando la telemetria viene persa (ovvero quando il modello viene
spento).

### 3. Annunci a intervalli

![Interruttore logico Delta 200mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Aggiungi un interruttore logico utilizzando la funzione **Δ > X** su `Consumo`,
che diventa vero/attivo ogni volta che il consumo aumenta di un passo fisso — ad esempio ogni 200 mAh, una
frazione conveniente della capacità di un pacco da 2800 mAh.

!!! tip
    Imposta l'**Intervallo di controllo** su `---` (Infinito) in modo che la funzione continui
    a misurare fino al raggiungimento della soglia successiva, anziché azzerarsi dopo una
    finestra fissa. Imposta la **Durata minima** su un valore superiore a 0 durante
    il debug — a 0,0 l'attivazione avviene troppo velocemente per poterla vedere sullo schermo.

Aggiungi una funzione speciale «Riproduci audio», con condizione attiva questo interruttore logico e un
comando «Riproduci valore» per `Consumo`:

![Riproduzione annuncio delta](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Riproduci valore: consumo](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Avviso di capacità bassa

![Secondo interruttore logico](../assets/how-to-consumption-lsw2-play-battlow.png)

Un secondo interruttore logico si attiva una sola volta, al superamento di una soglia critica di capacità —
ad esempio 2000 mAh per una LiPo da 2800 mAh — abbinato a una funzione speciale «Riproduci audio»
che si ripete ogni 10 secondi finché il modello non viene riavviato:

![Riproduci valore con batteria bassa](../assets/how-to-consumption-sf2-play-battlow.png)
![Riproduci valore: consumo con batteria bassa](../assets/how-to-consumption-sf2-play-value-consumption.png)
