---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Generale

![Impostazioni generali](../assets/system-general.png)

Riguarda gli attributi del display, l'audio, il vario, il feedback aptico e la barra degli strumenti superiore.

## Attributi del display

- **Lingua** — la lingua dei menu del display (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português e altre).
- **Tastiera** — disposizione della tastiera virtuale QWERTY, QWERTZ o AZERTY.
- **Luminosità** — uno slider per la luminosità della retroilluminazione;
  premere a lungo `ENT` per pilotarla invece da una sorgente (ad esempio uno
  slider, come nell'esempio seguente), oppure forzarla al minimo/massimo.

  ![Menu luminosità](../assets/system-general-brightness-menu.png)
  ![Slider luminosità](../assets/system-general-brightness-slider.png)

  !!! note
      Se **Luminosità** è uguale a **Luminosità in modalità riposo**, il
      touchscreen resta attivo anche durante il "riposo".

- **Risveglio** — quali eventi risvegliano la retroilluminazione dal riposo
  (se ne può abilitare più di uno): **Sempre acceso** (non va mai in riposo),
  **Stick**, **Interruttori**, **Giroscopio** (inclinando la radio). I tasti
  la risvegliano sempre, indipendentemente da queste impostazioni.
- **Riposo** — tempo di inattività prima dello spegnimento della
  retroilluminazione (disattivato se Risveglio è impostato su Sempre acceso).
- **Luminosità in modalità riposo** — luminosità della retroilluminazione
  durante il riposo.
- **Modalità scura** — tema chiaro o scuro del display.
- **Colore di evidenziazione** — il colore d'accento dell'interfaccia
  (predefinito `#F8B038`).

## Impostazioni audio {: #audio-settings }

![Impostazioni audio](../assets/system-general-audio.png)

- **Lingua audio** — lingua degli annunci vocali.
- **Scelta delle voci** — Ethos supporta più pacchetti vocali simultanei:

  - **Voce 1 (principale)** — usata per tutti gli annunci di sistema
    integrati. Per l'inglese, la scelta predefinita è tra i pacchetti
    americano (`us`) e britannico (`gb`), letti da `audio/en/us/system` e
    `audio/en/gb/system`. I file audio utente per la [funzione speciale Play
    Audio](../model-setup/special-functions.md) vanno rispettivamente in
    `audio/en/us/` o `audio/en/gb/`.
  - **Voce 2 / Voce 3** — pacchetti aggiuntivi, ad esempio una voce TTS
    personalizzata. Ognuna richiede la stessa struttura di cartelle della
    Voce 1 — ad esempio una voce chiamata "Susan" richiede `audio/en/Susan/`
    per i suoni utente e `audio/en/Susan/system` per i suoi suoni di sistema
    (ogni voce necessita di una cartella `/system`, poiché è da lì che
    attingono **Play Value** e gli annunci dei timer; a ogni release audio è
    allegato un elenco `.csv` dei file audio di sistema standard). Una volta
    installata, una voce può essere assegnata per singolo timer e per singola
    funzione Play Audio — o addirittura impostata come Voce 1 per sostituire
    completamente gli annunci di sistema.
  - **Voce "default"** — installata automaticamente come ripiego sicuro (e
    usata per evitare problemi di conversione dalle installazioni 1.4.x): se
    la Voce 1 non è già impostata durante un'installazione/aggiornamento,
    viene impostata su `default`, leggendo da `audio/en/default/system`. I
    file audio personalizzati più richiesti per Play Audio si trovano in
    `audio/en/default/`.

- **Volume principale** — uno slider per il volume audio generale (premere a
  lungo `ENT` per pilotarlo da un potenziometro); durante la regolazione
  vengono riprodotti dei bip per valutare il livello a orecchio.
- **Modalità audio**:
  - **Silenzioso** — nessun audio (attiva comunque l'[avviso di modalità
    silenziosa](alerts.md) all'avvio, se abilitato).
  - **Solo allarmi** — sono udibili solo gli allarmi.
  - **Predefinito** — suoni normali.
  - **Frequente** — aggiunge bip di errore quando un valore viene spinto
    oltre il proprio minimo/massimo.
  - **Sempre** — aggiunge bip per la normale navigazione nei menu, oltre a
    quanto previsto da Frequente.
  - **Bluetooth** (solo X20S/HD/Pro/R/RS) — inoltra l'audio a un dispositivo
    Bluetooth accoppiato (auricolare, ecc.). Scegliere **Cerca dispositivi**,
    mettere il dispositivo di destinazione in modalità accoppiamento, quindi
    selezionarlo una volta trovato:

    ![Accoppiamento Bluetooth](../assets/system-general-audio-bluetooth.png)
    ![Ricerca Bluetooth](../assets/system-general-audio-bluetooth-searching.png)
    ![Dispositivo Bluetooth selezionato](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Connessione Bluetooth](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth connesso](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Silenzia altoparlante** controlla quindi l'altoparlante integrato —
    sempre attivo, solo mentre la telemetria è attiva, oppure pilotato da una
    sorgente (ad esempio un interruttore). La radio ricorda il dispositivo
    accoppiato; per un funzionamento normale accendere la radio prima del
    dispositivo Bluetooth e attendere qualche secondo dopo la connessione
    affinché la funzione di silenziamento dell'altoparlante si riattivi.

## Vario

![Audio del vario](../assets/system-general-audio-vario.png)

- **Volume** — volume relativo del tono del vario.
- **Tono a zero** — altezza del tono a velocità di salita nulla.
- **Tono massimo** — altezza del tono alla massima velocità di salita.
- **Ripetizione** — intervallo tra i bip in corrispondenza del tono a zero.

Vedere anche il sensore VSpeed in [Telemetria](../model-setup/telemetry.md) e
la [funzione speciale Play Vario](../model-setup/special-functions.md) per
ulteriori comportamenti del vario.

## Aptico

- **Intensità** — uno slider per l'intensità della vibrazione.
- **Modalità** — le stesse opzioni della Modalità audio descritta sopra.

## Posizione di archiviazione (X18 e X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Queste radio dispongono di una eMMC interna da 8 GB. Per impostazione
predefinita Ethos la utilizza, rendendo la SD card opzionale — ma è possibile
selezionare la eMMC, una SD card o una combinazione di entrambe. Se si
spostano il sistema e i modelli su una SD card, copiare le cartelle/i file
pertinenti (inclusi audio e bitmap) **prima** di cambiare la posizione di
archiviazione.

![Posizione di archiviazione](../assets/system-general-storage.png)

## Barra degli strumenti superiore

![Impostazioni della barra superiore](../assets/system-general-topbar.png)

- **Tensione digitale** — mostra la tensione della batteria della radio come
  valore numerico anziché come barra nella barra degli strumenti superiore.
- **RSSI digitale** — idem, per l'RSSI a 2,4 GHz e 900 MHz.
- **Seleziona modello all'accensione** — mostra la schermata di selezione del
  modello all'avvio, prima che compaiano gli avvisi della checklist del
  modello precedente, così da poter cambiare modello senza doverli prima
  chiudere. L'ultimo modello utilizzato è evidenziato per impostazione
  predefinita.

  ![Seleziona modello all'avvio](../assets/system-general-model-start.png)

## Preselezione modalità USB

![Modalità USB](../assets/system-general-usb.png)

Cosa accade automaticamente quando la radio viene collegata a un PC tramite USB:

- **Non impostato** — richiede una scelta al momento della connessione.
- **Joystick** — entra immediatamente in modalità joystick per un simulatore RC.
- **Ethos Suite** — entra immediatamente in modalità Ethos per [Ethos
  Suite](../ethos-suite/index.md).
- **Seriale** — entra immediatamente in modalità Seriale, instradando le
  tracce di debug Lua su USB-Serial a 115200 bps (potrebbe essere necessario
  un driver per porta COM virtuale su Windows).
