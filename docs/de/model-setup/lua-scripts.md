---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-Skripte (Modell)

![Lua-Konfiguration](../assets/model-lua-config.png)

Dieses Menü erscheint erst, nachdem ein Lua-**Quellen**- oder
**Task**-Skript unter `scripts/` auf der SD card/eMMC installiert wurde
(siehe [Dateimanager](../system-setup/file-manager.md#top-level-folders)) —
es dient dem Aktivieren und Konfigurieren dieser Skripte **pro Modell**,
nicht deren Installation. Nach der Installation steht eine Quelle oder ein
Task global für jedes Modell zur Verfügung; auf dieser Seite entscheidet
jedes Modell, ob es sie verwendet, und legt seine eigene Konfiguration
fest. Beispiele für Quellen- und Task-Skripte werden auf der
Ethos-Feedback-Community-Website veröffentlicht (`/lua/examples/task`,
`/lua/examples/source`).

## Lua-Tasks

Jeder installierte Task wird mit einem Aktivierungsschalter pro Modell
aufgeführt. Beim Aktivieren erscheint dessen Konfigurationsformular (sofern
vorhanden) — das Task-Skript stellt eigene Lese-/Schreibfunktionen bereit,
sodass jedes Modell seine eigenen Einstellungen speichern kann. Ein Task
kann beispielsweise einen konfigurierbaren Zahlenbereich bereitstellen, der
für jedes Modell unabhängig festgelegt wird.

## Lua-Quellen

Für Quellen gilt dasselbe Prinzip: pro Modell aktivieren und anschließend
über das vom Quellen-Skript bereitgestellte Formular konfigurieren. Eine so
registrierte Quelle lässt sich überall sonst in Ethos wie eine gewöhnliche
[Quelle](../getting-started/user-interface-and-navigation.md#choosing-a-source)
verwenden, genau wie eine integrierte.

## Für Skriptautoren

Quellen und Tasks werden aus Lua heraus über `system.registerSource()` und
`system.registerTask()` registriert — siehe den Ethos Lua Reference Guide
sowie [Lua-Skripte](../lua-scripts/index.md) in diesem Handbuch für die
allgemeine Skriptumgebung (Widgets sind ein separater, verwandter
Mechanismus — siehe [Eigene Widgets](../displays/custom-widgets.md)).
