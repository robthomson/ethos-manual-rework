---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Script Lua

Gli script Lua permettono di creare [widget di visualizzazione personalizzati](../displays/custom-widgets.md)
per mostrare informazioni non gestite nativamente da Ethos e, per ciascun modello,
[sorgenti e task](../model-setup/lua-scripts.md) personalizzati — una base
destinata a crescere ulteriormente, verso funzioni personalizzate specializzate e
l'integrazione con le centraline di volo.

Lua è di per sé un linguaggio di scripting generico, leggero e integrabile
(utilizzato ovunque, dai videogiochi alle applicazioni web); Ethos lo integra
proprio per questo tipo di personalizzazione direttamente sulla radio.

!!! warning
    Gli script Lua aumentano il tempo di avvio della radio. Il ritardo introdotto
    da uno script ben scritto dovrebbe essere impercettibile — uno script scritto
    male può invece ritardare l'avvio quasi all'infinito.

- [Interprete Lua](lua-interpreter.md) — quale versione di Lua e quali librerie
  sono integrate in Ethos.
- [Documentazione Ethos Lua](ethos-lua-documentation.md) — dove si trova il
  riferimento completo delle API.
- [Dove trovare script di esempio](example-script-locations.md) — dove reperire e
  scaricare esempi funzionanti.
- [Limiti di configurazione](configuration-limits.md) — budget di memoria per
  bitmap e script.
- [Struttura base di un widget](basic-widget-layout.md) — la struttura di codice
  necessaria a uno script di widget personalizzato.
