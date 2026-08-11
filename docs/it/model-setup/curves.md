---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Curve

![Tipi di curva](../assets/model-curves-type.png)

Curve di risposta riutilizzabili per i [Mix](mixes.md#anatomy-of-a-mix) o le
[Uscite](outputs.md#editing-a-channel) — l'Expo integrato è disponibile
direttamente in entrambi, ma tutto ciò che è più elaborato si definisce qui
(oppure tramite **Aggiungi curva**, raggiungibile direttamente da entrambe le
schermate di modifica). Sono disponibili fino a 50 curve; per impostazione
predefinita non ne esiste nessuna (l'Expo resta comunque sempre integrato).
Aggiungine una con **+**; tocca una curva esistente per
**Modifica**/**Muovi**/**Copia-incolla**/**Clona**/**Cancella**.

![Aggiungi curva](../assets/model-curves-add.png)

## Tipi di curva

- **Expo** — valore predefinito 40; un valore positivo ammorbidisce la risposta
  intorno al centro, mentre un valore negativo la rende più netta. Ammorbidire
  la risposta a metà corsa dello stick aiuta a evitare comandi eccessivi,
  soprattutto per i piloti meno esperti.

  ![Expo](../assets/model-curves-expo.png)

- **Funzione** — un piccolo insieme di forme matematiche predefinite:

  ![Tipi di funzione](../assets/model-curves-fn-types.png)

  - **x > 0** — lascia passare la sorgente invariata quando è positiva;
    restituisce 0 quando è negativa.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — l'opposto speculare: lascia passare quando è negativa, 0 quando
    è positiva.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — lascia passare la sorgente come valore assoluto (sempre
    positivo).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — restituisce 100% quando la sorgente è positiva, 0 quando è
    negativa (una commutazione netta, non un passaggio diretto).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — restituisce −100% quando è negativa, 0 quando è positiva.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — restituisce −100% quando è negativa, +100% quando è positiva.

    ![|f|](../assets/model-curves-fn-barf.png)

  Ogni tipo di curva — Funzione inclusa — dispone anche di un **Offset**, che la
  sposta verso l'alto o verso il basso sull'asse Y (precisione di un decimale,
  come per i valori Y in generale):

  ![Offset della funzione](../assets/model-curves-fn-xgt0-offset.png)

- **Personalizzata** — una curva definita per punti, 5 punti per impostazione
  predefinita, fino a un massimo di 21.

  ![Curva personalizzata a 5 punti](../assets/model-curves-custom5.png)

  - **Smooth** — traccia una curva morbida attraverso tutti i punti anziché
    segmenti rettilinei tra un punto e l'altro.

    ![Curva smussata](../assets/model-curves-custom5-2-smooth.png)

  - **Modalità semplice** — **On** limita la modifica alle sole coordinate Y
    equidistanti (la X è fissa); **Off** consente di modificare sia X sia Y per
    ogni punto, tranne gli estremi −100%/+100%, che restano bloccati poiché la
    curva deve sempre coprire l'intera escursione del segnale.

    ![Modalità semplice disattivata](../assets/model-curves-custom-easy-off.png)

  **Comandi dell'editor** (stesso schema dell'[editor della curva di
  bilanciamento delle Uscite](outputs.md#balance-channels)):

  - **Sorgente** — per impostazione predefinita la sorgente (o le sorgenti) di
    mix della curva stessa, oppure **Ingresso analogico automatico** per
    rilevare il primo stick/slider/potenziometro mosso.
  - Aggancio al punto più vicino con l'encoder rotativo e un comando **Blocco**
    per congelare gli ingressi mentre si osserva il movimento risultante della
    superficie di comando.
  - Un cursore in tempo reale mostra il valore d'ingresso corrente che pilota la
    curva, per aiutare ad allinearlo a un punto prima della regolazione.

## Pilotare una curva da una Var

Sia l'**Offset** di una curva Funzione sia un singolo punto di una curva
**Personalizzata** possono essere pilotati da una [Var](variables.md) anziché da
un valore fisso — e quella Var può a sua volta essere regolata in volo tramite un
trim riutilizzato allo scopo:

![Offset della funzione da una Var](../assets/model-curves-fn-offset-var.png)
![Punto di curva personalizzata da una Var](../assets/model-curves-custom-with-var.png)

Vedi [Variabili](variables.md) e [Guida pratica: curva di compensazione
regolabile in volo](../how-to/in-flight-compensation-curve.md) per un esempio
completo e dettagliato di questo schema.
