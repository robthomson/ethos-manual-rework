---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Layout base di un widget

Un widget Lua personalizzato (vedi [Widget personalizzati](../displays/custom-widgets.md)
per l'installazione) è costituito da un piccolo insieme di campi/handler
denominati:

- **`key`** *(stringa)* — un identificatore univoco del widget.
- **`name`** *(stringa o funzione)* — il nome visualizzato del widget. Può
  essere una semplice stringa oppure una funzione senza argomenti che ne
  restituisce una — utile per un nome che varia in base alla lingua.
- **`create`** *(funzione)* — chiamata una sola volta alla creazione del
  widget, senza argomenti. Restituisce una **tabella del widget**, che viene
  poi passata a tutti gli altri handler elencati di seguito: inizializza qui
  lo stato e memorizzalo in quella tabella.
- **`configure`** *(funzione)* — chiamata quando l'utente apre la schermata
  di configurazione del widget; riceve come unico argomento la tabella del
  widget restituita da `create()` e non restituisce nulla. Costruisci qui il
  modulo di configurazione e utilizzalo per aggiornare i valori nella
  tabella del widget.
- **`wakeup`** *(funzione)* — chiamata a ogni ciclo (all'incirca ogni 50 ms);
  riceve la tabella del widget e non restituisce nulla. Verifica qui se
  qualcosa è cambiato; in tal caso, chiama `invalidateWindow()` per
  attivare un ridisegno tramite `paint()`. Mantieni questo handler veloce —
  idealmente non deve fare assolutamente nulla nella maggior parte delle
  chiamate.
- **`event`** *(funzione)* — chiamata quando il widget riceve un evento;
  Ethos indirizza al widget eventi arbitrari attraverso questo handler.
- **`paint`** *(funzione)* — disegna il widget; riceve la tabella del widget
  e non restituisce nulla. Viene chiamata automaticamente ogni volta che è
  stato invocato `lcd.invalidate()`. Può essere relativamente lenta, ma
  dovrebbe comunque ridisegnare effettivamente solo quando qualcosa è
  cambiato.
- **`read`** *(funzione, opzionale)* — legge i dati persistenti del widget.
- **`write`** *(funzione, opzionale)* — scrive i dati persistenti del widget.
- **`init`** *(funzione)* — registra il widget e le sue callback in Ethos.
  Tipicamente è l'ultimo elemento dello script:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` deve essere univoco fra tutti i widget installati; gli altri campi si
integrano nel ciclo di vita del widget come descritto sopra.

Gli script risiedono nella cartella `scripts/` sulla SD card/eMMC,
preferibilmente organizzati in cartelle separate per ciascun widget (vedi
[Gestione file](../system-setup/file-manager.md#top-level-folders) e
[Esempi di posizione degli script](example-script-locations.md)). Per
ulteriori esempi pratici, consulta il thread *FrSky ETHOS Lua Script
Programming* su rcgroups.
