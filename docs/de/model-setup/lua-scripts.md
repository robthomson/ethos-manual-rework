---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-Skripte (Modell)

![Lua-Konfiguration](../assets/model-lua-config.png)

Dieses Menü erscheint nur, wenn eine Lua-**Quelle** oder ein
**Aufgabenskript** im Ordner `scripts/` auf der SD card/eMMC installiert
ist (siehe [Dateimanager](../system-setup/file-manager.md#top-level-folders))
— es dient dazu, diese Skripte **pro Modell** zu aktivieren und zu
konfigurieren, nicht dazu, sie zu installieren. Einmal installiert, sind
Lua-Quellen oder -Aufgaben global für jedes Modell verfügbar; auf dieser
Seite entscheidet jedes Modell, ob es sie verwendet, und legt seine eigene
Konfiguration fest. Beispiele für Quell- und Aufgabenskripte werden auf der
Ethos-Feedback-Community-Website veröffentlicht (`/lua/examples/task`,
`/lua/examples/source`).

## Lua-Aufgaben

Alle installierten Aufgaben werden aufgelistet und können für das aktive
Modell einzeln aktiviert werden. Wenn eine Aufgabe aktiviert ist, wird das
zugehörige Konfigurationsformular angezeigt (sofern vorhanden) — das
Aufgabenskript verfügt über eine eigene Lese- und Schreibfunktion, damit
jedes Modell seine eigenen Einstellungen speichern kann. Eine Aufgabe kann
beispielsweise einen konfigurierbaren Zahlenbereich haben, der für jedes
Modell unabhängig angepasst werden kann.

## Lua-Quellen

Für Quellen gilt dasselbe Prinzip: pro Modell aktivieren und anschließend
über das Formular konfigurieren, das das Quellenskript bereitstellt. Eine
so registrierte Quelle lässt sich überall sonst in Ethos wie eine
gewöhnliche
[Quelle](../getting-started/user-interface-and-navigation.md#choosing-a-source)
verwenden, genau wie eine integrierte.

## Für Skriptautoren

Quellen und Aufgaben werden aus Lua heraus über `system.registerSource()`
und `system.registerTask()` registriert — weitere Informationen finden Sie
im Ethos LUA Referenzhandbuch sowie unter
[Lua-Skripte](../lua-scripts/index.md) in diesem Handbuch zur allgemeinen
Skriptumgebung (Widgets sind ein separater, verwandter Mechanismus — siehe
[Eigene Widgets](../displays/custom-widgets.md)).
