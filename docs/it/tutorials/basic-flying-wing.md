---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Esempio di aereo ad ala volante di base (Elevon)

Un'ala volante con 2 servi per gli elevoni, che utilizza come esempio pratico
concreto i rates, gli expo e i rapporti di mix raccomandati da Dreamflight
Weasel. Completa prima la [Configurazione iniziale della
radio](initial-radio-setup.md).

## Passo 1. Conferma le impostazioni del sistema {: #step-1-confirm-system-settings }

Ordine dei canali **AETR** predefinito, con **[Primi quattro canali
fissi](../system-setup/controls.md#first-four-channels-fixed)** su **OFF**.
Registra (se il tuo ricevitore è ACCESS) e collega il ricevitore tramite
[RF System](../model-setup/rf-system.md) prima di proseguire.

## Passo 2. Identificare i servi/canali necessari

Per un modello di elevone, i [mix](../model-setup/mixes.md) combinano i comandi
dell'alettone e dell'elevatore in modo che agiscano entrambi sulle superfici
fisiche — in totale solo 2 canali, ciascuno una combinazione di entrambi gli
ingressi.

## Passo 3. Crea un nuovo modello

![Creazione del modello aereo](../assets/tut-wing-eg-wiz-create-airplane.png)

Da [Selezione del modello](../model-setup/model-select.md), avvia la procedura
guidata **Aereo**, scegliendo l'opzione **Ricevitore non stabilizzato**.

![Nessun motore](../assets/tut-wing-eg-wiz-no-engine.png)

Seleziona **Nessun motore**, accetta i 2 canali predefiniti per gli alettoni e
seleziona **Nessun flap**.

![Nessuna coda](../assets/tut-wing-eg-wiz-no-tail.png)

Seleziona **Nessuno** come tipo di coda — è questo che porta Ethos a creare
automaticamente il mix di elevoni (ingressi degli alettoni + dell'elevatore,
entrambi sugli stessi due canali). Dai un nome al modello (ad esempio "Weasel"),
seleziona un'immagine bitmap e segui la procedura guidata fino alla fine —
diventerà il modello attivo nel gruppo Airplane.

## Passo 4. Rivedere e configurare i mix

![Panoramica dei mix](../assets/tut-wing-eg-mixes.png)

La procedura guidata ha creato un mix di Alettoni sui canali 1 e 2, seguito da un
mix di Elevatori *anch'esso* sui canali 1 e 2 — entrambi i controlli di ingresso
agiscono sui due canali degli elevoni, ed è proprio in questo che consiste il
mixaggio degli elevoni.

### Alettoni

![Mix alettoni](../assets/tut-wing-eg-mixes-ail-mix.png)

**Escursione / Rates** — facendo riferimento al manuale Weasel, la deflessione
degli alettoni dovrebbe essere circa 3 volte superiore a quella dell'elevatore, e
le due devono sommarsi al 100%: **75%** alettoni e **25%** elevatore. Le velocità
basse dovrebbero essere circa il 50% di quelle alte: **36%** per gli alettoni e
**12%** per l'elevatore.

![Escursione del mix alettoni](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — i valori raccomandati da Weasel sono il 35% per gli alti e il 20% per
i bassi, attivi nella posizione di abbassamento dell'interruttore SB, così da
appiattire la risposta al centro dello stick.

**Differenziale** — piuttosto piccolo su questa cellula, circa il **4%**:

![Differenziale alettoni](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Consulta l'[Esempio base ad ala
fissa](basic-fixed-wing.md#ailerons) per capire perché il differenziale è
importante — qui vale lo stesso ragionamento sull'imbardata avversa.)

### Elevatore

![Mix elevatore](../assets/tut-wing-eg-mixes-ele-mix.png)

In modo simile agli alettoni: rates del **25%** e del **12%** per alti e bassi, e
gli stessi valori di Expo degli alettoni.

### Timone

![Mix timone](../assets/tut-wing-eg-mixes-rud-mix.png)

Il Weasel non ha un timone — in genere le ali volanti non ne hanno bisogno. Se su
un modello con elevoni il timone *serve*, aggiungilo con un [Mix
libero](../model-setup/mixes.md#mix-libraries) sul canale 3.

## Passo 5. Bind /collegamento il ricevitore

Come al [Passo 1](#step-1-confirm-system-settings) — registra/collega il
ricevitore prima di procedere e, per evitare danni dovuti al sovraccarico dei
servi, valuta di scollegare i leveraggi dei servi o di ridurne la corsa fino a
quando non saranno impostati i limiti min/max.

## Passo 6. Esamina i mix

I canali di uscita 1 e 2 possono essere rinominati **Elevon1** ed **Elevon2**.
Applicando tutto l'alettone destro, il canale 1 (destro, in salita) è al 75%,
mentre il canale 2 (sinistro, in discesa) è al 72% — la differenza del 3% *è* il
differenziale in azione. Aggiungendo anche tutto l'elevatore in discesa, il canale
1 diventa 75+25 = 100% e il canale 2 diventa 72−25 = 47%.

## Passo 7. Configura l'escursione massima del servo

![Alettone completo](../assets/tut-wing-eg-outputs-full-ail.png)
![Alettone completo + elevatore completo](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Inizia centrando ogni servo con la regolazione **PWM center**. L'escursione
massima consigliata da Weasel è 25 mm (alettoni) + 10 mm (elevatore) = 35 mm
combinati — applica gli aiuti completi *e* gli input opposti di alettoni ed
elevatore e verifica che non vengano superati i limiti meccanici o del servo
prima di impostare le deflessioni definitive.

- **Min/Max** — limiti "rigidi", che non potranno mai essere superati; ridurli
  riduce la corsa piuttosto che indurre il clipping (ritaglio). Predefiniti a
  +/- 100,0%, ma aumentabili fino a +/- 150,0% se necessario.
- **Curva** — spesso più veloce e flessibile rispetto a gestire direttamente
  Min/Max/Subtrim, oltre ad avere un bel grafico. Una curva a 3 punti è adatta
  alla maggior parte delle uscite; una curva a 5 punti sul secondo elevone
  facilita la sincronizzazione della corsa su 5 punti rispetto al primo. Quando
  si utilizza una curva a questo scopo, è buona norma lasciare Min, Max e Subtrim
  ai valori "passanti" (−100/100/0, oppure −150/150/0 se si utilizzano limiti
  estesi) e lasciare che sia la curva a modellare la risposta.
