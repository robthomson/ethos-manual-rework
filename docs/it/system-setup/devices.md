---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Dispositivi

![Dispositivi](../assets/system-devices.png)

Chiamato **Device config** nel menu — strumenti per la configurazione delle
periferiche collegate tramite S.Port/FBUS: sensori, ricevitori, la "gas
suite", servi, VTX ed ESC. La voce **DIY sensors** compare automaticamente
non appena viene rilevato un sensore DIY. Per i dettagli completi consultare
il manuale specifico di ciascun dispositivo; questa pagina tratta gli aspetti
comuni a tutti.

!!! note
    Questo non ha nulla a che vedere con la scelta del modulo RF (interno o
    esterno) su cui trasmette un *modello* — quella è un'impostazione
    specifica del modello, descritta in
    [Sistema RF](../model-setup/rf-system.md).

Device Config è estensibile: sia gli utenti sia FrSky possono aggiungere
pagine qui tramite Lua.

## Riassegnazione degli ID dei sensori

Le schermate Device config di Ethos consentono di modificare direttamente il
**Physical ID** e l'**Application ID** S.Port di un dispositivo. Se si
possiede più di un dispositivo con la stessa funzione, collegarli **uno alla
volta**: rilevare ciascuno in
[Telemetria → Rileva nuovi sensori](../model-setup/telemetry.md), modificarne
qui in Device config il Physical ID e l'Application ID, quindi tornare
indietro e rilevarlo nuovamente con il nuovo ID.

## Esempio: ricevitori

![Scelta del modulo](../assets/system-devices-module-choice.png)

I ricevitori stabilizzati FrSky possono essere configurati qui una volta
installato il relativo script Lua di configurazione (un clic, dalla Lua
Library di Ethos Suite). Esistono due percorsi di configurazione a seconda
della generazione del ricevitore:

- **Stabilizer config** — ricevitori più recenti dotati di
  "stabilizzazione avanzata" (controllo del guadagno sul canale 13). Vengono
  esposti due gruppi di stabilizzazione indipendenti: il Gruppo 1 riguarda i
  canali 1–6, il Gruppo 2 i canali 7–11 — disattivare il Gruppo 2 se i pin
  7–11 non vengono utilizzati per la stabilizzazione. È integrata una
  calibrazione a 6 assi, che deve essere eseguita una volta su un ricevitore
  nuovo e nuovamente dopo ogni aggiornamento al firmware v3.0.x (a seguito di
  un ripristino delle impostazioni di fabbrica). Nella calibrazione di
  ciascun gruppo, il vecchio passaggio di "self-check" è stato sostituito
  dalla calibrazione indipendente dell'assetto orizzontale del modello, del
  centro canale e dei fine corsa del canale, e ogni canale può essere
  attivato/disattivato singolarmente. Le configurazioni (non i dati di
  calibrazione) possono essere salvate su PC e da lì ripristinate.
- **SxR** — ricevitori più datati, comprese le unità legacy e
  Archer/Archer Pro, oltre a ricevitori come l'SR10 Pro che (nonostante il
  nome "SRx") hanno il Gain sul canale 9 anziché sul 13.

  ![Dispositivo corrente](../assets/system-devices-current.png)

!!! warning "Dopo l'aggiornamento al firmware ricevitore v3.0.x"
    Eseguire un ripristino delle impostazioni di fabbrica (disponibile in
    Options del ricevitore nella configurazione RF), quindi rifare il
    binding e riconfigurare completamente — in particolare le funzioni Stab e
    la calibrazione a 6 assi. Ciò è richiesto dalla nuova funzione di
    salvataggio dei dati di failsafe introdotta con la v3.0.x; verificare
    attentamente il funzionamento del failsafe al termine.

FrSky North America pubblica una guida dettagliata alla configurazione dei
ricevitori stabilizzati, ed è disponibile un video esplicativo del FrSky Team
Pilot Juan Sanchez Garcia che tratta gli stessi argomenti.

## Configurazione tramite il connettore S.Port della trasmittente

I dispositivi S.Port e FBUS possono essere configurati anche direttamente
tramite il connettore S.Port posto sulla parte superiore della trasmittente,
senza passare da un ricevitore associato.

1. Collegare il dispositivo al connettore S.Port della trasmittente (cavo
   bianco/giallo verso il lato con la tacca).
2. Andare in **System → Device config**, scorrere fino al dispositivo (ad
   esempio un sensore di corrente FAS40 ADV) e premere `ENT`.
3. Nella pagina di configurazione, impostare **Module** su **S.Port
   connector**.
4. Apportare le modifiche desiderate — Physical ID e Application ID devono
   essere entrambi univoci — quindi scorrere verso il basso e toccare **Save
   to flash**.

Questo vale sia per i dispositivi FBUS (vedere anche [Guida pratica:
configurare un sistema FBUS](../how-to/fbus-setup.md)) sia per i normali
dispositivi S.Port come un variometro.
