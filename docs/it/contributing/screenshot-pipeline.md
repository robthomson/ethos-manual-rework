---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Pipeline degli screenshot

Ogni screenshot di questo manuale (attualmente circa 590, sotto
`docs/en/assets/`) è stato catturato scriptando il simulatore reale di Ethos, non
manualmente. L'infrastruttura si trova nel vecchio repository
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), sotto
`english/manual/`, e **non è ancora stata portata in questo repository** — questa
pagina documenta il suo funzionamento affinché ciò sia possibile e affinché, nel
frattempo, gli screenshot possano essere rigenerati o estesi senza ripartire da zero.

## Come è strutturata

Per ogni menu/sezione del manuale esiste una coppia di file:

- `manual/macros/<name>.lua` — uno script scritto per l'API Lua del simulatore
  (descritta più sotto) che naviga fino a una schermata specifica e richiama
  `simulator.screenshot(path)` in ogni punto degno di essere catturato.
- `manual/<name>.sh` — un wrapper di una sola riga che avvia il binario del
  simulatore per una radio specifica, puntandolo a quella macro, ad esempio:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` esegue in sequenza tutte le macro per rigenerare
l'intero set. Esistono singoli file `.sh` per ogni sezione, in modo che gli
screenshot di una singola pagina possano essere rigenerati senza rieseguire
tutto (ogni macro impiega da pochi secondi a più di un minuto).

Flag CLI principali:

- `--read-only` — non rende persistente alcuna modifica effettuata durante l'esecuzione.
- `--no-gui` / `--no-audio` — quasi headless; alcune macro necessitano comunque
  della GUI perché senza di essa il simulatore "salta" dei passaggi (vedere il
  commento in `screenshots.sh`).
- `--radio-settings <file>.bin` — con quali impostazioni salvate della radio
  avviarsi (è questo che rende gli screenshot specifici per lingua e per radio —
  un'esecuzione in tedesco usa un `.bin` tedesco).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — indicano al simulatore i modelli/firmware/documenti/audio
  che deve vedere, in modo che gli screenshot riflettano contenuti predisposti
  deliberatamente anziché qualsiasi cosa si trovi su una SD card reale.
- `--exec <script>.lua` — la macro da eseguire dopo l'avvio.

Ogni famiglia di radio (X20S, X20 PRO, X20 PRO AW, X18S) dispone di un proprio
binario del simulatore e necessita di un proprio file `--radio-settings` per ogni
lingua (ad esempio `x20s-en.bin`, `x20pro-en.bin`), poiché l'interfaccia varia
leggermente tra le radio e il file delle impostazioni contiene anche la lingua.

## L'API delle macro

Le macro sono semplice codice Lua che pilota una variabile globale `simulator`:

| Chiamata | Scopo |
|---|---|
| `simulator.loadModel("name.bin")` | Carica un file di modello specifico prima della navigazione — ogni sezione del manuale utilizza un modello configurato per illustrare quella sezione (vedere l'elenco dei modelli più sotto). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Preme un tasto fisico — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE`, ecc. Una durata di pressione prolungata attiva una pressione lunga (apre i menu contestuali). |
| `simulator.turnRotaryEncoder(n)` | Sposta l'encoder di `n` scatti (valore negativo = senso inverso) — il modo principale per spostare il cursore tra i campi. |
| `simulator.touch(x, y)` | Tocca una coordinata specifica dello schermo — utilizzato dove il touch è l'unico modo per raggiungere qualcosa (ad esempio per cambiare il layout della tastiera). |
| `simulator.setAnalog(channel, value)` | Imposta direttamente la posizione di uno stick/potenziometro/slider (`0`-`3` sono i quattro stick principali, `ANALOG_LAST_SLIDER` l'ultimo slider), così che gli screenshot mostrino un valore deliberato e riproducibile anziché quello predefinito del simulatore. |
| `simulator.setSwitch(n, position)` | Imposta la posizione di un interruttore fisico. |
| `simulator.setDateTime({...})` | Fissa l'orologio del simulatore, in modo che le marche temporali negli screenshot (e tutto ciò che dipende dal tempo) siano riproducibili tra le varie esecuzioni. |
| `simulator.screenshot(path)` | Cattura la schermata corrente in un file PNG, con percorso relativo alla directory di lavoro della macro (da cui i percorsi `../assets/...` all'interno di ogni macro). |
| `simulator.connectUsb()` | Simula il collegamento USB, per catturare il menu USB. |
| `simulator.sleep(seconds)` | Attende che un'animazione o un valore di telemetria si stabilizzi prima della cattura. |

`manual/macros/common.lua` viene incluso con `dofile` dalla maggior parte delle
macro e si limita a fissare data e ora, in modo che ogni macro parta dallo stesso
istante simulato.

## Modelli utilizzati per ciascuna sezione

`manual/notes.txt` (riportato in modo informale, non ancora copiato in questo
repository) associa ogni macro al file di modello `.bin` da cui dipende e spiega
il motivo — ad esempio `model-mixes.lua` usa `rarebear.bin`, `model-fm.lua` usa
`zblank.bin` (un modello con una configurazione delle fasi di volo
deliberatamente vuota), `model-trims.lua` usa `blaster.bin` (configurato con trim
offset per illustrare l'escursione dei trim). Il riporto delle note di questo file
in una documentazione vera e propria fa parte del lavoro di fase 2 descritto sotto.

## Cosa comporta il porting nel nuovo repository (non ancora fatto)

- Decidere se le macro debbano essere rieseguite direttamente da questo
  repository (richiedendo un'installazione locale del simulatore Ethos, come
  faceva il vecchio repository) oppure tramite CI, con il simulatore incluso o
  scaricato nel workflow.
- Ristrutturare i percorsi di output piatti `../assets/...` per adattarli al
  layout degli asset di questo repository, organizzato per pagina e per locale
  (`docs/<locale>/assets/`).
- Un file `--radio-settings ... .bin` e un'esecuzione degli screenshot per ogni
  locale, non appena esisterà un locale diverso da `en` — gli screenshot sono
  specifici della lingua dell'interfaccia e non possono essere condivisi tra
  locali diversi.
- Decidere quante delle circa 40 macro esistenti riportare così come sono e
  quante invece riscrivere in base all'attuale struttura di navigazione di questo
  repository (alcune macro producono screenshot per sezioni che non
  corrispondono più 1:1 all'impaginazione di questo manuale).
