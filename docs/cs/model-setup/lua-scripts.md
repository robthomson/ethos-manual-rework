---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua skripty (model)

![Konfigurace Lua](../assets/model-lua-config.png)

Tato nabídka se zobrazí až poté, co je do složky `scripts/` na SD kartě/eMMC
nainstalován Lua skript typu **source** (zdroj) nebo **task** (úloha) — viz
[Správce souborů](../system-setup/file-manager.md#top-level-folders). Slouží
k aktivaci a konfiguraci těchto skriptů **pro jednotlivé modely**, nikoli
k jejich instalaci. Po instalaci je zdroj nebo úloha globálně dostupná pro
každý model; na této stránce se každý model přihlásí k jejich používání
a nastaví si vlastní konfiguraci. Ukázkové skripty typu source a task jsou
zveřejněny na stránkách Ethos-Feedback-Community (`/lua/examples/task`,
`/lua/examples/source`).

## Lua úlohy (tasks)

Každá nainstalovaná úloha je uvedena v seznamu s přepínačem pro povolení
u daného modelu. Po povolení se zobrazí její konfigurační formulář (pokud
jej má) — skript úlohy poskytuje vlastní funkce pro čtení a zápis, takže
každý model si může uložit své vlastní nastavení. Úloha může například
nabízet konfigurovatelný číselný rozsah, který se nastavuje nezávisle pro
každý model.

## Lua zdroje (sources)

U zdrojů platí stejný postup: povolení pro daný model a následná konfigurace
prostřednictvím formuláře, který skript zdroje poskytuje. Takto
zaregistrovaný zdroj lze používat jako běžný
[zdroj](../getting-started/user-interface-and-navigation.md#choosing-a-source)
kdekoli jinde v Ethos, stejně jako vestavěný zdroj.

## Pro autory skriptů

Zdroje a úlohy se z Lua registrují pomocí funkcí `system.registerSource()`
a `system.registerTask()` — viz Ethos Lua Reference Guide a část
[Lua skripty](../lua-scripts/index.md) v této příručce, která popisuje
obecné skriptovací prostředí (widgety jsou samostatný, ale příbuzný
mechanismus — viz [Vlastní widgety](../displays/custom-widgets.md)).
