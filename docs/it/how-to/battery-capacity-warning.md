---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Avviso di capacità della batteria

Avviso basato sulla **capacità consumata** (mAh) anziché sulla tensione — una
misura più diretta di quanta parte del pacco è stata effettivamente utilizzata. Ci sono due
modi per ottenerlo, a seconda dell'hardware installato.

## Opzione A: un ESC della serie Neuron

Gli ESC Neuron di FrSky riportano il consumo direttamente — non serve alcun sensore
calcolato. Imposta [Opzioni ricevitore → Porta
telemetria](../system-setup/devices.md) su S.Port, collega il cavo di telemetria del
Neuron ed esegui la [ricerca dei
sensori](../model-setup/telemetry.md#discovering-sensors) — il sensore che
interessa è **ESC Consumption**.

1. Aggiungi un [interruttore logico](../model-setup/logical-switches.md) su `ESC
   Consumption`, vero al di sopra di (ad esempio) 900mAh — all'incirca il 60% di un pacco dimensionato per
   atterrare con ancora ~30% di riserva.
2. Aggiungi una [funzione speciale Riproduci
   audio](../model-setup/special-functions.md), con condizione attiva il nuovo
   interruttore e uno step **Riproduci valore** per `ESC Consumption`.

Come seconda linea di difesa, gli ESC Neuron riportano anche **ESC Voltage** —
imposta un secondo interruttore logico allo stesso modo di [Avviso di tensione
batteria bassa](low-battery-warning.md) (sotto 3,4V/cella per 4s — ad esempio
13,6V per un pacco 4S), con la propria funzione Riproduci audio ripetuta ogni 5
secondi.

## Opzione B: un sensore di corrente + sensore calcolato

Se l'ESC non riporta il consumo, un sensore di corrente (ad esempio FrSky
FASxxx) combinato con un [sensore **Consumption**
calcolato](../model-setup/telemetry.md#calculated-sensors) svolge lo stesso
compito.

### 1. Collegamento e ricerca

![Sensore di corrente](../assets/how-to-consumption-telemetry-current-sensor.png)

Collega il cavo S.Port del sensore di corrente ed esegui la ricerca — comparirà come
**Current**. Imposta il suo **Range** in modo che corrisponda al sensore (ad esempio 0–100A per un
FAS100):

![Modifica sensore di corrente](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Creare il sensore calcolato Consumption

![Creazione sensore calcolato](../assets/how-to-consumption-create-calc-select.png)
![Sensore Consumption](../assets/how-to-consumption-create-calc-sensor.png)

In Telemetria, **Crea sensore calcolato** → **Consumption**. Imposta l'unità
su `mAh` e il **Range** sulla capacità del pacco (ad esempio 2800mAh); la **Sorgente**
su `Current`.

![Modifica sensore](../assets/how-to-consumption-sensor-edit.png)
![Modifica sensore 2](../assets/how-to-consumption-sensor-edit2.png)

Imposta **Reset** sull'evento di sistema `!Telemetry Active` — seleziona **Telemetry
Active**, premi a lungo `ENT` e scegli **Inverti** — in modo che il totale progressivo
si azzeri automaticamente non appena la telemetria viene persa (ovvero quando il modello viene
spento).

### 3. Annunci a intervalli

![Interruttore logico Delta 200mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Aggiungi un interruttore logico che usa la funzione **Δ > X** su `Consumption`,
attivandosi ogni volta che il valore aumenta di un passo fisso — ad esempio ogni 200mAh, una
frazione comoda di un pacco da 2800mAh.

!!! tip
    Imposta l'**Intervallo di controllo** su `---` (infinito) affinché continui ad accumulare
    verso la soglia successiva indefinitamente, anziché azzerarsi dopo una
    finestra fissa. Assegna alla **Durata minima** un piccolo valore diverso da zero durante
    il debug — a 0.0 l'attivazione è troppo breve per essere visibile sullo schermo.

Aggiungi una funzione Riproduci audio, con condizione attiva questo interruttore e uno step Riproduci
valore per `Consumption`:

![Riproduzione annuncio delta](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Riproduci valore: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Avviso di capacità bassa

![Secondo interruttore logico](../assets/how-to-consumption-lsw2-play-battlow.png)

Un secondo interruttore logico si attiva una sola volta, superata una soglia critica di capacità bassa —
ad esempio 2000mAh su un pacco da 2800mAh — abbinato a una funzione Riproduci audio
ripetuta ogni 10 secondi finché il modello non viene riavviato:

![Riproduci valore con batteria bassa](../assets/how-to-consumption-sf2-play-battlow.png)
![Riproduci valore: consumption con batteria bassa](../assets/how-to-consumption-sf2-play-value-consumption.png)
