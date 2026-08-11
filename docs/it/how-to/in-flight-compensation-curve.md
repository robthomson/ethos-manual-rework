---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Curva di compensazione regolabile in volo

## Perché

L'estrazione dei flap modifica la curvatura alare — i modelli ad ala alta
tendono a "cabrare" (ballooning), quelli ad ala bassa tendono ad
affondare — richiedendo una correzione di profondità non lineare rispetto
alla deflessione dei flap, quindi una curva anziché un semplice offset
fisso. Questa guida utilizza le [Var](../model-setup/variables.md) per
rendere regolabili **in volo** i punti di una curva di compensazione,
tramite un trim del gas riassegnato, condizionato dal punto della curva a
cui lo stick dei flap si trova più vicino in quel momento — sviluppando
il passaggio relativo alla compensazione di profondità della [Guida
pratica: Mixer Butterfly](butterfly-mixer.md).

## 1. Scegliere il tipo di curva

Una [curva personalizzata](../model-setup/curves.md) a 5 punti è
sufficiente per una compensazione fluida senza complessità eccessiva. Il
punto 5 (all'estrema destra, stick dei flap tutto in alto / nessun flap)
è sempre fissato a zero — non serve alcuna compensazione senza flap
estratti. Gli altri 4 punti vengono resi regolabili tramite le Var.
Poiché lo stick dei flap si troverà spesso tra due punti definiti,
entrambi i punti ai lati devono poter essere regolati insieme in quella
zona di sovrapposizione.

## 2. Calcolare gli intervalli sovrapposti

Intervalli punto per punto (adattati, con permesso, dal "Crow-aware
adaptive elevator trim" di Mike Shellim per OpenTX su rc-soar.com —
leggermente estesi affinché l'intervallo del Pt2 arrivi fino a +100%, per
la ragione spiegata nel [Passo 6](#6-apply-the-curve)):

| Intervallo stick flap | Punto/i attivo/i |
|---|---|
| Da +100% a +45% | Solo Pt2 |
| Da +45% a +20% | Pt2 e Pt3 |
| Da +20% a −20% | Solo Pt3 |
| Da −20% a −45% | Pt3 e Pt4 |
| Da −45% a −90% | Solo Pt4 |
| Da −90% a −100% | Solo Pt5 |

## 3. Configurare gli interruttori logici

![Interruttori logici dei punti adattivi](../assets/how-in-flight-comp-lsws.png)

Quattro [interruttori logici](../model-setup/logical-switches.md),
ciascuno con funzione **Range** sullo stick dei flap (gas), attivi mentre
lo stick si trova nella zona di quel punto:

- `AdaptivePt2` — intervallo da 20% a 100% (esteso fino a 100%
  appositamente affinché il Pt2 possa essere regolato anche senza flap
  estratti — vedere il Passo 6).

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` — intervallo da −45% a 45%.

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` — intervallo da −90% a −20%.

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` — intervallo da −100% a −90%.

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. Definire le Var di regolazione

![Panoramica delle Var](../assets/how-in-flight-comp-vars.png)

Quattro [Var](../model-setup/variables.md), da `VAdjPt2` a `VAdjPt5`,
ciascuna con intervallo 0–50% (da ampliare se necessario) e un'azione
**trim del gas riassegnato** — passo di 1,0%, condizione di attivazione
data dal corrispondente interruttore logico:

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![Azione VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![Azione VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![Azione VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![Azione VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5-2.png)

Poiché è attivo un solo interruttore logico alla volta (al massimo due,
nelle zone di sovrapposizione), lo stesso trim fisico regola in modo
sicuro Var diverse a seconda della posizione dei flap.

## 5. Definire la curva di compensazione

![Curva di compensazione](../assets/how-in-flight-comp-var-comp-curve.png)
![Punti della curva di compensazione](../assets/how-in-flight-comp-var-comp-curve-pts.png)

Una nuova curva personalizzata a 5 punti (ad esempio "EleComp") con
**Smooth** attivo. Premere a lungo `ENT` sui punti da 1 a 4 e selezionare
**Usa una sorgente** per assegnare rispettivamente da `VAdjPt5` a
`VAdjPt2` (il punto 5 resta fisso a 0, come da Passo 1).

## 6. Applicare la curva {: #6-apply-the-curve }

Utilizzare questa curva esattamente nel punto in cui la [Guida pratica:
Mixer
Butterfly](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix)
associa la propria curva EleComp al mix di compensazione della
profondità.

Ove possibile, partire da dati reali (indicazioni del produttore, post
della community) sulla corsa di profondità necessaria per una data
deflessione dei flap; in alternativa, qualche millimetro di compensazione
a flap tutti estratti è un ragionevole punto di partenza.

!!! tip "Approccio alla messa a punto"
    Iniziare con piccole estrazioni di flap e piccole regolazioni di
    trim. `AdaptivePt2` può essere regolato **senza alcun flap estratto**
    — estrarre un po' di flap, richiuderlo e inserire un po' di
    compensazione alla volta, invece di combattere con un modello che
    cabra o affonda mentre si cerca di trimmare sotto pressione.
    Riapplicare un po' di flap per verificare e regolare nuovamente se
    necessario. Una volta che il Pt2 risulta corretto, passare al punto
    successivo attorno alla metà corsa dello stick — se il Pt2 ha
    richiesto una variazione di trim consistente, conviene atterrare e
    impostare i punti rimanenti ciascuno leggermente più grande del
    precedente, anziché procedere a caso.
