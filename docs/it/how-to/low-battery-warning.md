---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Avviso di tensione batteria bassa

Monitorare la tensione del pacco di volo **sotto carico** e segnalare il superamento di una soglia è un approccio più affidabile rispetto all'uso di un timer fisso — un sensore come il FrSky FLVSS rende tutto ciò molto semplice.

## 1. Collegare e rilevare il sensore

![Sensore telemetrico LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Impostare [Opzioni ricevitore → Porta telemetria](../system-setup/devices.md) su **S.Port**, collegare il FLVSS al ricevitore tramite un cavo S.Port, quindi attivare **Rileva nuovi sensori** in [Telemetria](../model-setup/telemetry.md) — il sensore LiPo compare insieme agli altri già rilevati.

## 2. Aggiungere un interruttore logico

![Interruttore logico batteria bassa](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Aggiungere un nuovo [interruttore logico](../model-setup/logical-switches.md) con il sensore Lipo come sorgente. Premere a lungo `ENT` sul sensore evidenziato per scegliere quale dei suoi valori utilizzare:

![Selezione della cella più bassa](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Tensione minima del pacco / Tensione massima del pacco
- **Tensione della cella più bassa** / Tensione della cella più alta
- Numero di celle
- Tensioni delle singole celle (selezionabili solo quando il sensore è effettivamente collegato a un ricevitore associato con una LiPo connessa)

Selezionare **Lowest** (tensione di cella) — il valore che conta per una protezione di tipo LVC.

![Cella più bassa selezionata](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Impostare il valore di confronto a circa **3,4V** e **Ritardo prima dell'attivazione** a **4 secondi** — l'interruttore diventa vero quando la cella più bassa rimane sotto i 3,4V per cella in modo continuativo per 4s o più. (3,4V *sotto carico* risalgono tipicamente a circa 3,7V una volta rimosso il carico, quindi questa soglia riflette un reale calo di tensione e non un semplice disturbo momentaneo.)

![Interruttore logico completato](../assets/how-to-low-batt-lsw-summary.png)

## 3. Aggiungere una funzione speciale

![Funzione speciale: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Aggiungere una [funzione speciale Riproduci audio](../model-setup/special-functions.md), con **Condizione di attivazione** impostata sull'interruttore logico `BattLow`, scegliere una voce e, in **Sequenza**, aggiungere un passo **Riproduci valore** per la tensione totale della LiPo:

![Riproduci valore: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Riepilogo della sequenza](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Con **Ripetizione** impostata su 10 secondi, la tensione della LiPo viene annunciata ogni 10s per tutto il tempo in cui la cella più bassa rimane al di sotto della soglia di 3,4V/4s.
