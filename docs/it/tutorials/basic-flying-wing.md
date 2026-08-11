---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Esempio base di ala volante (elevoni)

Un'ala volante a 2 servi con elevoni, che utilizza come esempio pratico concreto
i rate/Expo/rapporti di mix consigliati per la Dreamflight Weasel. Completare
prima la [Configurazione iniziale della radio](initial-radio-setup.md).

## Passo 1. Verificare le impostazioni di sistema {: #step-1-confirm-system-settings }

Ordine predefinito **AETR**, con **[Primi quattro canali
fissi](../system-setup/controls.md#first-four-channels-fixed)** su **OFF**.
Registrare (se ACCESS) e connettere il ricevitore tramite
[Sistema RF](../model-setup/rf-system.md) prima di proseguire.

## Passo 2. Individuare i servi/canali necessari

Su una cellula con elevoni, i [mix](../model-setup/mixes.md) combinano il comando
di alettone e quello di profondità su entrambe le superfici fisiche — in totale
solo 2 canali, ciascuno una combinazione di entrambi i comandi.

## Passo 3. Creare un nuovo modello

![Creazione di un modello aereo](../assets/tut-wing-eg-wiz-create-airplane.png)

Da [Selezione modello](../model-setup/model-select.md), avviare la procedura
guidata **Airplane**, scegliendo **Non stabilized receiver**.

![Nessun motore](../assets/tut-wing-eg-wiz-no-engine.png)

Selezionare **No engine**, accettare i 2 canali alettone predefiniti e
selezionare **No flaps**.

![Nessuna coda](../assets/tut-wing-eg-wiz-no-tail.png)

Selezionare **None** come tipo di coda — è questo che induce Ethos a costruire
automaticamente il mix per elevoni (comandi di alettone + profondità, entrambi
sugli stessi due canali). Assegnare un nome al modello (ad es. "Weasel",
scegliere un'immagine e terminare — diventerà il modello attivo nella categoria
Airplane.

## Passo 4. Esaminare e configurare i mix

![Panoramica dei mix](../assets/tut-wing-eg-mixes.png)

La procedura guidata crea un mix Alettoni sui canali 1+2, seguito da un mix
Profondità *anch'esso* sui canali 1+2 — entrambi i comandi agiscono su entrambi
i canali degli elevoni, ed è proprio in questo che consiste il mixaggio a
elevoni.

### Alettoni

![Mix alettoni](../assets/tut-wing-eg-mixes-ail-mix.png)

**Peso/Rate** — secondo il manuale della Weasel, la deflessione degli alettoni
dovrebbe essere circa 3 volte quella della profondità, e le due devono sommarsi
a 100%: **75%** alettoni, **25%** profondità. I rate bassi valgono circa la metà
di quelli alti: **36%** alettoni bassi, **12%** profondità bassa.

![Peso del mix alettoni](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — valori consigliati per la Weasel: 35% alto / 20% basso, attivi con
l'interruttore SB in basso, per appiattire la risposta attorno al centro dello
stick.

**Differenziale** — ridotto su questa cellula, circa **4%**:

![Differenziale alettoni](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Vedere l'[Esempio base di ala
fissa](basic-fixed-wing.md#ailerons) per capire perché il differenziale è
importante — qui vale lo stesso ragionamento sull'imbardata inversa.)

### Profondità

![Mix profondità](../assets/tut-wing-eg-mixes-ele-mix.png)

Stesso schema: rate **25%**/**12%** alto/basso, gli stessi valori di Expo degli
alettoni.

### Timone

![Mix timone](../assets/tut-wing-eg-mixes-rud-mix.png)

La Weasel non ne ha uno — in genere le ali volanti non ne hanno bisogno. Nei casi
in cui *serva* un timone su un modello a elevoni, aggiungerlo come [Mix
libero](../model-setup/mixes.md#mix-libraries) sul canale 3.

## Passo 5. Connettere il ricevitore

Come al [Passo 1](#step-1-confirm-system-settings) — registrare/connettere prima
di proseguire, e valutare di scollegare i rinvii dei servi o di ridurre le corse
finché non sono impostati i limiti Min/Max, per evitare di forzare qualcosa.

## Passo 6. Esaminare i mix

I canali di uscita 1/2 possono essere rinominati **Elevon1**/**Elevon2**. Con
alettone tutto a destra, il canale 1 (destro, in salita) indica 75%, mentre il
canale 2 (sinistro, in discesa) indica 72% — la differenza del 3% *è* il
differenziale in azione. Aggiungendo anche profondità tutta a picchiare, il
canale 1 diventa 75+25 = 100% e il canale 2 diventa 72−25 = 47%.

## Passo 7. Configurare le corse massime dei servi

![Alettone completo](../assets/tut-wing-eg-outputs-full-ail.png)
![Alettone completo + profondità completa](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Centrare prima ciascun servo con **PWM center**. La corsa massima consigliata per
la Weasel è 25 mm di alettone + 10 mm di profondità = 35 mm combinati — applicare
comandi di alettone/profondità sia concordi *sia* opposti al massimo e verificare
che nessuno superi i limiti meccanici o del servo prima di impostare le
deflessioni definitive.

- **Min/Max** — limiti rigidi, mai superati; ridurli riduce la corsa anziché
  troncarla. Valore predefinito ±100%, estendibile a ±150% se necessario.
- **Curva** — spesso più rapida e flessibile rispetto a gestire direttamente
  Min/Max/Subtrim, con il vantaggio di un grafico in tempo reale. Una curva a 3
  punti è adatta alla maggior parte delle uscite; una curva a 5 punti sul secondo
  elevone facilita la sincronizzazione della corsa in 5 punti rispetto al primo.
  Quando si usa una curva a questo scopo, lasciare Min/Max/Subtrim ai loro valori
  neutri (−100/100/0, oppure −150/150/0 con limiti estesi) e lasciare che sia la
  curva a modellare la risposta.
