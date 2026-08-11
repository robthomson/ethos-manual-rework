---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Esempio base per aeromodello ad ala fissa

Una guida completa per un aeromodello con motore + 2 alettoni + 2 flap +
profondità + timone, un servo per ogni superficie, realizzato dall'inizio
alla fine con la procedura guidata. Completare prima la
[Configurazione iniziale della radio](initial-radio-setup.md).

## Passo 1. Verificare le impostazioni di sistema

Questo esempio utilizza l'ordine dei canali predefinito **AETR**.

## Passo 2. Individuare i servi/canali necessari

[Mix](../model-setup/mixes.md) è il cuore della radio — fino a 100 canali
di mix, normalmente con i numeri più bassi assegnati ai servi (poiché i
numeri dei canali corrispondono direttamente ai canali del ricevitore; il
modulo RF interno dell'X20 supporta fino a 24 canali di uscita). I canali
più alti sono liberi per canali virtuali o canali reali aggiuntivi tramite
più moduli RF e SBUS. La nostra cellula:

| Funzione | Canali |
|---|---|
| Motore | 1 |
| Alettoni | 2 |
| Flap | 2 |
| Profondità | 1 |
| Timone | 1 |

(I carrelli retrattili vengono aggiunti più avanti, al
[Passo 10](#step-10-add-a-mix-for-retracts).)

## Passo 3. Creare un nuovo modello

![Creazione modello aeroplano](../assets/tut-fw-eg-wiz-create-airplane.png)

Da [Selezione modello](../model-setup/model-select.md), scegliere una
categoria, toccare **+** e avviare la procedura guidata **Airplane**.
Per questo esempio scegliere **Non stabilized receiver**.

![Canali motore](../assets/tut-fw-eg-wiz-engine.png)
![Canali alettoni/flap](../assets/tut-fw-eg-wiz-ail-flaps.png)

Accettare 1 canale motore, quindi 2 canali alettoni e selezionare 2 canali
flap.

![Tipo di coda](../assets/tut-fw-eg-wiz-tail.png)
![Canali profondità/timone](../assets/tut-fw-eg-wiz-ele-rudd.png)

Accettare la **Traditional Tail** predefinita, con 1 canale profondità e 1
canale timone.

![Nome del modello](../assets/tut-fw-eg-wiz-name.png)
![Ricevitore](../assets/tut-fw-eg-wiz-rx.png)

Assegnare un nome (ad es. "FWexample" — fino a 15 caratteri), completare la
procedura guidata: il modello diventa quello attivo, creato nella categoria
Airplane.

## Passo 4. Rivedere e configurare i mix

![Panoramica dei mix](../assets/tut-fw-eg-mixes.png)

La procedura guidata ha già creato i mix di alettoni (canali 1 e 5),
profondità, gas, timone e flap (i flap mostrano `---` — nessuna sorgente
ancora assegnata).

### Alettoni {: #ailerons }

![Mix alettoni](../assets/tut-fw-eg-mixes-ail-mix.png)
![Modifica mix alettoni](../assets/tut-fw-eg-mixes-ail-edit.png)

**Peso/Rate** — impostare i rate prima di far volare qualcosa di nuovo: una
corsa moderata (ad es. 30%) è adatta al volo sportivo, il 100% pieno al 3D.
Aggiungere un rate del 60% per l'interruttore SB in posizione centrale e un
rate del 30% per SB in basso — il valore predefinito (SB in alto) resta al
100%:

![Rate di peso](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — una risposta lineare può risultare nervosa attorno al centro;
aggiungere rate di Expo (ad es. 60%/40%/20% sulle stesse posizioni di SB)
per addolcire la risposta vicino al centro senza ridurre l'escursione
massima:

![Rate di Expo](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Differenziale** — un'escursione uguale verso l'alto e verso il basso degli
alettoni genera più resistenza sull'alettone che si abbassa rispetto a
quello che si alza, facendo imbardare il modello verso l'esterno della
virata ("imbardata inversa"). Un differenziale positivo (il 50% è un valore
comune) riduce l'escursione verso il basso rispetto a quella verso l'alto
per compensare questo effetto:

![Differenziale al 50%](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Per regolare il differenziale in volo, premere a lungo `ENT` sul valore,
scegliere **Use a source** e selezionare Pot1:

![Usa una sorgente](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Pot1 selezionato](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Una volta soddisfatti del valore trovato in volo, premere di nuovo a lungo e
scegliere **Convert to value** per fissarlo definitivamente:

![Converti in valore](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim** — è possibile scollegare questo mix dal trim associato senza
disattivare il trim stesso, rendendolo così disponibile per un altro scopo:

![Trim alettoni](../assets/tut-fw-eg-mixes-ail-trim.png)

### Profondità e timone

Lo stesso schema con tripli rate + Expo, qui sull'interruttore SC:

![Rate di Expo profondità](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Gas

![Mix gas](../assets/tut-fw-eg-mixes-thr-edit.png)

Lasciare l'ingresso sullo stick del gas — non servono rate né Expo — ma un
interruttore di sicurezza è indispensabile; l'avviamento imprevisto di un
motore a scoppio o elettrico può causare lesioni gravi.

**Trim di posizione bassa** (motori glow/a benzina) — regola il regime di
minimo indipendentemente dal gas massimo:

![Trim di posizione bassa](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Con questa opzione attiva, il canale del gas si trova a −75% con lo stick al
minimo; la leva del trim del gas regola quindi il minimo tra −100% e −50%.

**Taglio gas** — un blocco di sicurezza. Con l'interruttore SA in basso come
condizione attiva (mostrata in grassetto quando è attiva), l'uscita del gas
si mantiene a −100% non appena lo stick scende sotto −85%:

![Taglio gas](../assets/tut-fw-eg-mixes-thr-cut.png)

Con **Sticky** attivato, invece, il gas viene tagliato **nell'istante** in
cui SA va in basso, indipendentemente dalla posizione dello stick:

![Taglio gas sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

In entrambi i casi, una volta che la condizione attiva cessa, lo stick deve
essere riportato sotto −85% prima che il gas possa aumentare di nuovo —
evitando che il motore salti a un'elevata apertura del gas nel momento in
cui l'interruttore di taglio viene rilasciato.

**Blocco gas** — un taglio di emergenza da *qualsiasi* posizione dello
stick, che porta l'uscita direttamente a −100% (o a un valore configurato)
nell'istante in cui la condizione è soddisfatta:

![Blocco gas](../assets/tut-fw-eg-mixes-thr-hold.png)

### Flap

![Ingresso flap](../assets/tut-fw-eg-mixes-flaps-input.png)

Assegnare i flap all'interruttore SE e impostare al 100% il peso di entrambi
i canali di uscita:

![Pesi flap](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Passo 5. Effettuare il bind del ricevitore

Registrare (se ACCESS) ed eseguire il bind tramite
[RF System](../model-setup/rf-system.md). Prima di passare alle Uscite,
valutare di scollegare i rinvii dei servi o di ridurre temporaneamente la
corsa dei servi, per evitare forzature durante l'impostazione dei limiti
Min/Max.

## Passo 6. Configurare le uscite

![Uscite](../assets/tut-fw-eg-outputs.png)

[Uscite](../model-setup/outputs.md) adatta la logica del mixer alla
meccanica reale del modello.

**Aileron 1** — centrare il servo con **PWM center** dopo aver ottimizzato
il rinvio meccanico, quindi impostare **Min**/**Max**. Assegnare
temporaneamente un potenziometro a Min (e poi a Max, allo stesso modo
dell'esempio del differenziale visto sopra) rende la regolazione più rapida:

![Modifica uscita alettoni](../assets/tut-fw-eg-outputs-edit-ail.png)

**Flap** — i flap richiedono di solito un'ampia deflessione verso il basso
per una frenata efficace; conviene sacrificare parte della corsa verso
l'alto nel rinvio per ottenerla, in modo che il flap risulti a metà corsa
verso il basso con il servo al centro, e usare quindi Min/Max per definire
le posizioni effettive di flap retratti e completamente estesi. Una curva a
5 punti è un metodo comune per correggere eventuali disallineamenti
risultanti tra flap e alettoni. Concludere con **[Bilanciamento
canali](../model-setup/outputs.md#balance-channels)** per sincronizzare
alettoni e flap destro/sinistro.

## Passo 7. Introduzione alle fasi di volo

Le [Fasi di volo](../model-setup/flight-modes.md) consentono a un modello di
avere impostazioni specifiche per ogni compito — come cambiare marcia. Delle
20 disponibili, questo esempio ne usa tre: **Default**, **Flaps Half**
(interruttore SE in centro) e **Flaps Full** (SE in alto). È attiva la prima
fase di volo la cui condizione è vera; la fase **Default** non ha alcuna
condizione e subentra ogni volta che nessun'altra è applicabile — per questo
non prevede l'opzione di selezione di un interruttore. Una dissolvenza di
1 secondo in entrata/uscita rende più graduale la transizione durante
l'estensione dei flap.

## Passo 8. Configurare i trim

Due modi per gestire la variazione del trim di profondità in funzione della
posizione dei flap:

**Trim indipendenti per fase di volo** — l'opzione più semplice: il trim di
profondità diventa completamente indipendente per ciascuna fase di volo,
commutando automaticamente al variare di SE. Poiché ogni fase viene trimmata
da zero, l'[Instant
trim](../model-setup/trims.md#instant-trim) è di aiuto — trimmare prima per
il volo normale, quindi atterrare e usare quel valore come punto di partenza
per le fasi con i flap.

**Trim di base con offset** — si trimma una sola volta in Default, con la
compensazione di profondità di ciascuna fase flap sovrapposta come offset:

1. Impostare lo **Step** del trim su Medium (per una trimmatura iniziale più
   rapida; ridurlo in seguito per la regolazione fine), la **Mode** su
   Custom e aggiungere un nuovo comportamento.
2. **Condizione attiva**: `FM1(Flaps Half)`, modalità **Offset + Default** —
   il trim in Flaps Half diventa il trim di base più l'offset impostato
   mentre quella fase è attiva:

   ![Aggiungi comportamento](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Ripetere per `FM2(Flaps Full)`:

   ![Selezione fase di volo](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Ogni fase con i flap può ora essere trimmata in modo indipendente, ma una
successiva regolazione del trim di base Default (ad es. per correggere la
deriva termica dei servi) sposta automaticamente entrambi i trim delle fasi
flap della stessa quantità.

![Selezione trim personalizzato](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Passo 9. Impostare un timer per la batteria di volo

In [Timer](../model-setup/timers.md), modificare il Timer 1: modalità
**Down**, valore iniziale di 5 minuti, in funzione ogni volta che
**Throttle active** è vero (e non mantenuto in reset). Facoltativamente,
assegnare una sorgente di conteggio proporzionale (ad es. lo stick del gas)
in modo che il timer scorra a velocità reale a gas pieno e rallenti al
ridursi del gas.

## Passo 10. Aggiungere un mix per i carrelli retrattili {: #step-10-add-a-mix-for-retracts }

![Sorgente mix carrelli retrattili](../assets/tut-fw-eg-retracts-source.png)

Toccare un mix, **Add Mix** → **Free Mix**, denominarlo "Retracts",
impostare la condizione su Always e la sorgente sull'interruttore SF.
L'azione predefinita con Weight = 100% va bene — questo assegna, ad esempio,
il canale 8 ai carrelli retrattili:

![Uscita carrelli retrattili](../assets/tut-fw-eg-retracts-outputs.png)
