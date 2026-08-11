---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Avviso di bassa tensione della batteria

Monitorare la tensione del pacco di volo **sotto carico** e lanciare un allarme quando scende al di sotto di una soglia è un approccio più affidabile rispetto all'uso di un timer fisso — a tal fine è possibile utilizzare un sensore di tensione della batteria come FrSky FLVSS.

## 1. Collegare e rilevare il sensore

![Sensore di telemetria LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Nelle [Opzioni del ricevitore → Porta di telemetria](../system-setup/devices.md) imposta l'opzione **S.Port**, collega l'FLVSS al ricevitore tramite un cavo S.Port e attiva l'opzione **Scopri nuovi sensori** in [Telemetria](../model-setup/telemetry.md) — il sensore LiPo compare insieme agli altri già rilevati.

## 2. Aggiungere un interruttore logico

![Interruttore logico batteria scarica](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Aggiungi un nuovo [interruttore logico](../model-setup/logical-switches.md) e seleziona il sensore Lipo come sorgente. Con il sensore evidenziato, premi a lungo il tasto `ENT` per visualizzare la finestra di dialogo delle opzioni e scegliere quale dei suoi valori utilizzare:

![Selezione della tensione minima delle celle](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Tensione minima del pacco / Tensione massima del pacco
- **Tensione minima delle celle** / Tensione massima delle celle
- Conteggio delle celle
- Tensioni delle singole celle (selezionabili come sorgenti solo quando il sensore è effettivamente collegato a un ricevitore connesso e ha una lipo collegata)

Seleziona **Inferiore** (tensione minima di cella) — il valore che conta per una protezione di tipo LVC.

![Tensione minima delle celle selezionata](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Imposta il valore di confronto a qualcosa come **3,4V** e **Ritardo prima di attivare** a **4 secondi** — l'interruttore logico diventerà vero/attivo quando la tensione più bassa della cella rimarrà al di sotto di 3,4V per cella per almeno 4 secondi. (Una soglia di 3,4V *sotto carico* recupererà circa 3,7V quando non sarà più sotto carico, quindi questa soglia riflette un reale calo di tensione e non un semplice disturbo momentaneo.)

![Interruttore logico completato](../assets/how-to-low-batt-lsw-summary.png)

## 3. Aggiungere una funzione speciale

![Funzione speciale: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Aggiungi una [funzione speciale "Riproduci audio"](../model-setup/special-functions.md), imposta l'**Attivazione** sull'interruttore logico `BattLow`, seleziona la voce che desideri utilizzare e in **Sequenza** aggiungi un comando **Riproduci Valore** per la tensione totale della LiPo:

![Riproduci Valore: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Riepilogo della sequenza](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Con **Ripeti** impostato su 10 secondi, la tensione della Lipo verrà riprodotta ogni 10 secondi finché la cella più bassa rimane al di sotto della soglia di 3,4V per cella per 4 secondi.
