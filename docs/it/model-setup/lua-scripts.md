---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Script Lua (modello)

![Configurazione Lua](../assets/model-lua-config.png)

Questo menu compare solo dopo che uno script Lua di tipo **source** o
**task** è stato installato nella cartella `scripts/` della SD card/eMMC
(vedere [Gestione
file](../system-setup/file-manager.md#top-level-folders)) — serve per
attivare e configurare tali script **per singolo modello**, non per
installarli. Una volta installato, un source o un task è disponibile
globalmente per tutti i modelli; questa pagina è il punto in cui ogni
modello lo abilita e ne definisce la propria configurazione. Esempi di
script source e task sono pubblicati sul sito Ethos-Feedback-Community
(`/lua/examples/task`, `/lua/examples/source`).

## Task Lua

Ogni task installato è elencato con un interruttore di abilitazione per
ciascun modello. Abilitandone uno viene mostrata la relativa maschera di
configurazione (se prevista) — lo script del task fornisce le proprie
funzioni di lettura/scrittura, così ogni modello può salvare le proprie
impostazioni. Ad esempio, un task può esporre un intervallo numerico
configurabile impostabile in modo indipendente per ciascun modello.

## Sorgenti Lua

Lo stesso schema vale per le sorgenti: abilitazione per modello, quindi
configurazione tramite la maschera fornita dallo script della sorgente.
Una sorgente registrata in questo modo diventa utilizzabile come una
comune
[sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source)
in qualsiasi altra parte di Ethos, esattamente come una sorgente
integrata.

## Per gli autori di script

Le sorgenti e i task vengono registrati da Lua tramite
`system.registerSource()` e `system.registerTask()` — consultare la
Ethos Lua Reference Guide e la sezione [Script
Lua](../lua-scripts/index.md) di questo manuale per l'ambiente di
scripting generale (i widget sono un meccanismo separato ma correlato —
vedere [Widget personalizzati](../displays/custom-widgets.md)).
