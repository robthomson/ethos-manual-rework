---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Batteria

![Impostazioni della batteria della radio](../assets/system-battery.png)

Calibra la lettura della batteria interna della radio e imposta le soglie
di allarme — funzione distinta dalle impostazioni del pacco batteria del
modello (vedere [Guida pratica: avviso di tensione batteria bassa](../how-to/low-battery-warning.md)).

- **Tensione principale** — mostra la lettura corrente e funge anche da
  regolazione di calibrazione: inserire la tensione effettiva misurata con
  un multimetro. Il valore predefinito è 8.4V (un pacco Li-ion 2S
  completamente carico).
- **Tensione bassa** — la soglia di allarme, predefinita 7.2V (7.4V offre
  un margine maggiore). Quando l'[avviso di tensione principale](alerts.md)
  è attivo, scendere sotto questo valore genera una finestra di avviso e un
  messaggio vocale "Batteria della radio scarica" ogni minuto, che la
  finestra sia aperta o meno.

  !!! warning
      Atterrare e ricaricare la batteria della radio non appena questo
      avviso viene emesso — si ripete ogni minuto in ogni caso. A 6.0V la
      radio si spegne incondizionatamente per proteggere le celle Li-ion
      2×3.0V.

- **Intervallo di tensione visualizzato** — i valori min/max per
  l'indicatore grafico della batteria nell'angolo in alto a destra: MIN è
  il punto in cui il primo segmento si spegne, MAX quello in cui si
  accende il quarto. I valori predefiniti sono 6.4–8.4V per il pacco
  Li-ion integrato; molti piloti alzano il limite inferiore per ottenere
  un avviso di bassa tensione anticipato ed evitare la scarica eccessiva.
  Impostare questi valori in base al tipo di batteria effettivamente
  installata.
- **Tensione RTC** — la tensione della batteria a bottone dell'orologio in
  tempo reale. 3.0V quando è nuova; sostituirla al di sotto di 2.7V per
  mantenere l'orologio preciso, e aspettarsi l'[avviso di tensione RTC](alerts.md)
  al di sotto di 2.5V.
