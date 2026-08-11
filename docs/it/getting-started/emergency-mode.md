---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modalità di emergenza

La modalità di emergenza è la risposta di Ethos a un guasto imprevisto di basso livello, come un reset del watchdog. Il watchdog è un timer che viene continuamente riavviato da varie parti del sistema; se qualcosa ne impedisce il riavvio, il timer scade e forza un reset hardware. La modalità di emergenza riavvia quindi la radio il più rapidamente possibile, saltando tutti i normali controlli di avvio, in modo che il controllo del modello venga restituito con il minimo ritardo. In questa modalità la SD card/eMMC non viene utilizzata in alcun modo.

Sono disponibili solo le funzioni essenziali necessarie a mantenere il controllo del modello, nessuna delle funzioni di livello superiore. Lo schermo rimane vuoto, ad eccezione della scritta **EMERGENCY MODE**, accompagnata da un segnale acustico di 300 ms ripetuto ogni 3 secondi; gli avvisi vocali, gli script Lua, la registrazione dei dati e la telemetria si interrompono. Se ciò accade in volo, atterra il prima possibile.

La causa più frequente è un guasto della SD card.

## Verifica della modalità di emergenza

È possibile aggiungere uno **strumento di sistema** per attivare deliberatamente la modalità di emergenza a scopo di prova, in modo da non doverla scoprire per la prima volta in volo. Toccando l'icona Emergency Test viene richiesta una conferma, dopodiché la radio entra in modalità di emergenza esattamente come in caso di guasto reale.
