---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Script Lua (modello)

![Configurazione Lua](../assets/model-lua-config.png)

Il menu Lua appare solo se è stato installato uno script sorgente o di
attività Lua nella cartella `scripts/` sulla SD card o eMMC (vedi
[Gestione file](../system-setup/file-manager.md#top-level-folders)) —
serve per attivare e configurare selettivamente tali script **per il
modello attivo**, non per installarli. Una volta installati, i sorgenti o
le attività Lua sono disponibili globalmente per ogni modello; questa
pagina è il punto in cui ogni modello li abilita e ne definisce la
propria configurazione. Alcuni esempi di script sorgente e attività Lua
sono pubblicati sulla pagina web Ethos-Feedback-Community
(`/lua/examples/task`, `/lua/examples/source`).

## Compiti Lua

Vengono elencate tutte le attività disponibili, ciascuna con un
interruttore di abilitazione per il modello attivo. Se un'attività è
abilitata, viene mostrato il modulo di configurazione Lua associato (se
previsto) — lo script dell'attività fornisce una funzione di lettura e
una di scrittura per consentire a ogni modello di salvare i propri
parametri di configurazione. Ad esempio, un'attività può esporre un
intervallo numerico configurabile, impostabile in modo indipendente per
ciascun modello.

## Sorgenti Lua

Per le sorgenti vale lo stesso schema: abilitazione per il modello
attivo, quindi configurazione tramite il modulo fornito dallo script
della sorgente. Una sorgente registrata in questo modo diventa
utilizzabile come una comune
[sorgente](../getting-started/user-interface-and-navigation.md#choosing-a-source)
in qualsiasi altra parte di Ethos, esattamente come una sorgente
integrata.

## Per gli autori di script

Le sorgenti e le attività vengono registrate da Lua tramite
`system.registerSource()` e `system.registerTask()` — consulta la Ethos
Lua Reference Guide e la sezione [Script
Lua](../lua-scripts/index.md) di questo manuale per l'ambiente di
scripting generale (i widget sono un meccanismo separato ma correlato —
vedi [Widget personalizzati](../displays/custom-widgets.md)).
