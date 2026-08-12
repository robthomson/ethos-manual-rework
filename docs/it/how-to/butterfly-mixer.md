---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Mixer Butterfly (Corvo)

La frenata butterfly (detta anche crow) controlla la velocità di
discesa, principalmente sugli alianti: gli alettoni salgono di poco
mentre i flap scendono molto, generando una resistenza notevole — ideale
per controllare l'avvicinamento all'atterraggio. Questo esempio
presuppone un aliante i cui canali Flap esistano già (creati dalla
procedura guidata [Selezione del modello](../model-setup/model-select.md)),
utilizzando lo stick del Gas - Throttle come ingresso del freno: nessun
butterfly con lo stick in alto, progressivamente maggiore man mano che
lo si abbassa, con compensazione dell'elevatore affinché l'aliante non
tenda a cabrare quando si applica il crow.

## 1. Disabilitare il mix Flap predefinito

![Disabilitare il mix flap](../assets/how-to-butterfly-flaps-disable.png)

Imposta l'**Attivazione** del mix Flap creato dalla procedura guidata su
`---`: non verrà utilizzato.

## 2. Creare il mix Butterfly

![Mix butterfly aggiunto](../assets/how-to-butterfly-mix-added.png)

Tocca una linea qualsiasi del mixer, **Aggiungi mix** → **Butterfly**
dalla [libreria dei mix](../model-setup/mixes.md#mix-libraries),
inserendolo dopo il mix Flap (ora disabilitato).

## 3. Configurare l'ingresso

![Ingresso gas](../assets/how-to-butterfly-mix-source-thr.png)

Imposta **Ingressi** su **Gas**. Poiché normalmente il Gas - Throttle
legge il valore massimo con lo stick in alto, mentre il butterfly deve
essere 0 con lo stick in alto, premi a lungo `ENT` su Gas e seleziona
**Inverti**:

![Invertire il gas](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Gas invertito](../assets/how-to-butterfly-mix-source-thr-neg.png)

L'ingresso ora legge 0 con lo stick completamente in alto e il campo
mostra `-Throttle` a conferma dell'inversione. Imposta l'**Attivazione**
su una fase di volo di atterraggio (o su un altro interruttore) se il
butterfly non deve essere sempre disponibile.

## 4. Aggiungere una curva con banda morta

![Selezione curva](../assets/how-to-butterfly-mix-curve-select.png)

Una piccola banda morta all'estremità zero dello stick evita
l'attivazione accidentale dovuta a piccoli disturbi dello stick in
prossimità del fine corsa. Aggiungi una curva personalizzata a 3 punti
(ad esempio denominata "Crowdb") con **Modo Facile** disattivato, in modo
da poter spostare i punti X:

![Curva a 3 punti](../assets/how-to-butterfly-mix-curve-3pt.png)
![Punti della curva](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    L'aggiunta di una curva personalizzata al mix Butterfly ne elimina
    l'offset interno 0–100 (normalmente applicato automaticamente): ora è
    la curva stessa a dover riprodurre tale trasformazione 0–100. In
    questo esempio l'uscita resta a 0% finché lo stick del Gas - Throttle
    non raggiunge −90%, quindi sale linearmente fino al 100%:

    ![Curva aggiunta](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Configurare alettoni e flap

![Uscita alettoni](../assets/how-to-butterfly-mix-ailerons.png)

La suddivisione abituale prevede una salita moderata degli alettoni (ad
esempio 20%) abbinata a una grande deflessione dei flap. I flap
richiedono in genere una corsa verso il basso molto maggiore di quella
verso l'alto: il risultato si ottiene comunemente sfalsando di 20–30°
dalla posizione neutra le squadrette dei servi dei flap nel rinvio
stesso, il che fa sì che i flap risultino circa a metà corsa verso il
basso con il servo al neutro:

![Flap in alto](../assets/how-to-butterfly-mix-flaps-up.png)
![Flap in basso](../assets/how-to-butterfly-mix-flaps-down.png)

Imposta un'escursione elevata per il mix dei flap (ad esempio −180%) per
ottenere la massima corsa; la corsa fisica effettiva è determinata dai
valori Min/Max nella pagina [Uscite](../model-setup/outputs.md).

!!! tip
    Per evitare di forzare i servi, inizia con valori Min/Max delle
    Uscite prudenti (ad esempio ±30%) e allargali con attenzione durante
    la messa a punto finale, verificando che non vi siano impuntamenti.

## 6. Aggiungere un mix di offset "Flap neutri"

![Mix di offset 80%](../assets/how-to-butterfly-offset-mix-80.png)

Poiché lo sfalsamento delle squadrette dei servi lascia i flap deflessi
di circa 20–30% con il servo al neutro, un **Mix di offset** li riporta
alla reale posizione neutra dell'ala per il volo normale. Inizia con un
offset dell'80% (da mettere a punto) e 2 canali di uscita assegnati a
entrambi i canali dei flap:

![Flap in alto con offset](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Flap in basso con offset](../assets/how-to-butterfly-offset-mix-flaps-down.png)

Con lo stick del Gas - Throttle completamente in alto (mix Butterfly
disattivo), verifica che i valori del mixer dei flap si trovino sul
valore di offset (80%); portando lo stick dei flap alla massima
estensione, l'uscita del mixer deve spostarsi dell'intera escursione (ad
esempio dall'80% fino a −100%, cioè 180%). Regola con precisione i limiti
di corsa effettivi nelle Uscite tramite Min/Max o una curva.

## 7. Aggiungere la curva e il mix di compensazione dell'elevatore {: #7-add-the-elevator-compensation-curve-and-mix }

![Curva di compensazione](../assets/how-to-butterfly-comp-curve.png)
![Punti della curva di compensazione](../assets/how-to-butterfly-comp-curve-points.png)

Poiché la compensazione necessaria non è lineare, conviene usare una
curva anziché un'escursione fissa. Definisci una curva personalizzata a 5
punti (ad esempio "EleComp"): in questo esempio si parte con
12%/10%/8%/5%/0% sui vari punti; in assenza di un punto di partenza noto
per il tuo modello, questi valori vanno determinati empiricamente.

Occorre poi convertire tale curva in un valore utilizzabile come
**Escursione** di un mix: aggiungi un [Free
Mix](../model-setup/mixes.md#mix-libraries) ("EleCompx") con Gas come
sorgente e la curva EleComp associata, con uscita su un canale alto non
utilizzato (ad esempio CH20):

![Mix di compensazione su CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

Tornando al mix Butterfly, premi a lungo `ENT` sull'**Escursione**
dell'uscita Elevatore, seleziona **Usa una sorgente**, quindi scegli CH20
(EleCompx) dalla categoria Canali:

![Elevatore con CH20 come sorgente](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Selezione sorgente](../assets/how-to-butterfly-mix-ele-use-source.png)

Il mix Butterfly è ora completamente configurato:

![Compensazione dell'elevatore configurata](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Verificare con la Vista per canale

![Vista per canale](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Passa alla [Vista per canale](../model-setup/mixes.md#per-channel-view)
sull'Elevatore per osservare l'aggiornamento simultaneo di tutti i mix
che vi contribuiscono (ingresso dello stick + compensazione Butterfly)
mentre lo stick del gas/freno si muove: è molto più semplice da
analizzare rispetto alla vista a tabella.

!!! tip
    Prima di mettere a punto i valori iniziali della curva di
    compensazione è utile disporre di dati sulla corsa dell'elevatore
    necessaria in rapporto alla deflessione dei flap (forniti dal
    costruttore del modello o da fonti della community). In mancanza di
    tali dati, parti da pochi millimetri di corsa dell'elevatore per
    l'estensione completa dei flap e affina da lì.
