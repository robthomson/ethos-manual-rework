---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-skript (modell)

![Lua-konfigurasjon](../assets/model-lua-config.png)

Denne menyen vises bare når et Lua-skript av typen **source** (kilde) eller
**task** (oppgave) er installert under `scripts/` på SD-kortet/eMMC (se
[Filbehandler](../system-setup/file-manager.md#top-level-folders)) — den er
til for å aktivere og konfigurere disse skriptene **per modell**, ikke for å
installere dem. Når et source- eller task-skript er installert, er det
tilgjengelig globalt for alle modeller; på denne siden velger hver modell om
den skal bruke det, og setter sin egen konfigurasjon. Eksempler på source- og
task-skript er publisert på Ethos-Feedback-Community-nettstedet
(`/lua/examples/task`, `/lua/examples/source`).

## Lua-oppgaver

Alle installerte oppgaver listes opp med en aktiveringsbryter per modell. Når
en oppgave aktiveres, vises konfigurasjonsskjemaet dens (hvis den har et) —
oppgaveskriptet leverer sine egne lese-/skrivefunksjoner, slik at hver modell
kan lagre sine egne innstillinger. En oppgave kan for eksempel tilby et
konfigurerbart tallområde som settes uavhengig for hver modell.

## Lua-kilder

Samme mønster gjelder for kilder: aktiver per modell, og konfigurer deretter
via det skjemaet kildeskriptet tilbyr. En kilde som registreres på denne
måten, kan brukes som en vanlig
[kilde](../getting-started/user-interface-and-navigation.md#choosing-a-source)
overalt ellers i Ethos, akkurat som en innebygd kilde.

## For skriptutviklere

Kilder og oppgaver registreres fra Lua med `system.registerSource()` og
`system.registerTask()` — se Ethos Lua Reference Guide, og
[Lua-skript](../lua-scripts/index.md) i denne manualen for det generelle
skriptmiljøet (widgets er en separat, men beslektet mekanisme — se
[Egendefinerte widgets](../displays/custom-widgets.md)).
