---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-scripts (model)

![Lua config](../assets/model-lua-config.png)

Dit menu verschijnt alleen zodra een Lua-**source**- of **task**-script is
geïnstalleerd onder `scripts/` op de SD card/eMMC (zie
[Bestandsbeheer](../system-setup/file-manager.md#top-level-folders)) — het dient
voor het activeren en configureren van die scripts **per model**, niet voor het
installeren ervan. Zodra een source of task is geïnstalleerd, is deze globaal
beschikbaar voor elk model; op deze pagina kiest elk model ervoor om deze te
gebruiken en stelt het zijn eigen configuratie in. Voorbeelden van source- en
task-scripts worden gepubliceerd op de site van de Ethos-Feedback-Community
(`/lua/examples/task`, `/lua/examples/source`).

## Lua-tasks

Elke geïnstalleerde task wordt weergegeven met een activeringsschakelaar per
model. Wanneer u er een activeert, verschijnt het bijbehorende
configuratieformulier (indien aanwezig) — het task-script levert zijn eigen
lees-/schrijffuncties, zodat elk model zijn eigen instellingen kan opslaan. Een
task kan bijvoorbeeld een instelbaar numeriek bereik aanbieden dat per model
onafhankelijk wordt ingesteld.

## Lua-sources

Voor sources geldt hetzelfde principe: per model activeren en vervolgens
configureren via het formulier dat het source-script biedt. Een op deze manier
geregistreerde source wordt overal elders in Ethos bruikbaar als een gewone
[bron](../getting-started/user-interface-and-navigation.md#choosing-a-source),
precies zoals een ingebouwde bron.

## Voor scriptauteurs

Sources en tasks worden vanuit Lua geregistreerd met `system.registerSource()`
en `system.registerTask()` — zie de Ethos Lua Reference Guide en
[Lua-scripts](../lua-scripts/index.md) in deze handleiding voor de algemene
scriptomgeving (widgets vormen een afzonderlijk, verwant mechanisme — zie
[Aangepaste widgets](../displays/custom-widgets.md)).
