---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Další displeje

![Možnosti konfigurace obrazovky](../assets/display-screen-config-options.png)

Výchozí model obsahuje jednu obrazovku (obrázek modelu a tři widgety časovačů), podporováno je však celkem až **osm** obrazovek. Klepnutím na **+** vedle „Screen1“ přidáte další:

- Vyberte z **15** rozvržení, včetně dvou rozvržení určených pro domovskou obrazovku a možnosti celé obrazovky, které pojme až 9 widgetů — konfigurace je zcela stejná jako u první obrazovky.
- Obrazovky lze přeřadit nebo odstranit v jejich vlastním dialogu úprav (klepněte na Screen1, Screen2 atd.).

## Praktický příklad

![Hlavní zobrazení](../assets/display-main-view.png)

Typické rozvržení: vlevo obrázek modelu (nastavený v [Editace modelu → Obrázek](../model-setup/model-edit.md)), vpravo pod sebou napětí baterie přijímače, RSSI a widget stavu „Throttle ACTIVE“ (Lua widget vytvořený komunitou, z vlákna *FrSky - ETHOS Lua Script Programming* na rcgroups). Klepnutím na kterýkoli widget otevřete jeho konfiguraci, případně přejdete přímo do hlavní funkce Konfigurace obrazovek.

## Možnosti na úrovni obrazovky

Kromě jednotlivých widgetů má každá obrazovka vlastní nastavení — velikost mřížky rozvržení, pozadí a to, které obrazovky jsou zařazeny do cyklu tlačítka `PAGE`.

Samotným widgetům se věnuje kapitola [Displeje](index.md), přidávání widgetů se skripty Lua nad rámec vestavěné sady popisuje kapitola [Vlastní widgety](custom-widgets.md).
