---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Displeje

![Domovská obrazovka displeje](../assets/display-home.png)

Domovská obrazovka se skládá z jedné či více **obrazovek displeje**, z nichž
každá je tvořena **widgety**, které si sami rozmístíte a nakonfigurujete.
Stiskem `DISP` otevřete editor displeje pro aktuální obrazovku.

K dispozici je až **osm** obrazovek, každá vycházející z jednoho ze
**třinácti** rozvržení (s kapacitou až **devíti** buněk pro widgety).
Widgety mohou zobrazovat telemetrii, ale také kteroukoli ze sedmnácti
dalších kategorií informací — stav modelu/vysílače, časovače, kanály a další.
Ke nakonfigurovaným obrazovkám se dostanete přejetím prstem nebo tlačítkem
`PAGE` nahoru/dolů; horní a spodní lišta zůstávají viditelné na každé
obrazovce s výjimkou rozvržení na celou obrazovku.

## Přidání widgetu

![Typy widgetů](../assets/display-widget-types.png)

Každá obrazovka je mřížka; klepnutím na prázdnou buňku otevřete výběr
widgetů. Widgety sahají od jednoduchých textových a číselných údajů až po
ukazatele, grafy a kompletní telemetrické záznamy. Po umístění widgetu
otevřete opětovným klepnutím na něj stejnou nabídku možností, která slouží
ke změně velikosti, přesunutí nebo odebrání:

![Možnosti konfigurace widgetu](../assets/display-widget-config-options.png)

Volbou vlastního nastavení widgetu otevřete konfigurační formulář specifický
pro daný widget. Pole **zdroj** — tedy hodnota, kterou widget zobrazuje —
používá stejný
[výběr zdroje](../getting-started/user-interface-and-navigation.md#choosing-a-source)
jako všude jinde v Ethos:

![Změna zdroje widgetu](../assets/display-change-source.png)

## Typy widgetů {: #widget-types }

**Value** — jediná číselná nebo telemetrická hodnota zobrazená jako text:

![Konfigurace widgetu Value](../assets/display-widget-value-config.png)

Většina zdrojů rovněž podporuje redukci na živé **min** nebo **max** — po
výběru zdroje jej podržte a zvolte Min nebo Max — což je užitečné například
pro nejhorší dosaženou hodnotu RSSI během letu:

![Widget Value s minimem](../assets/display-widget-value-min.png)
![Widget Value s minimem RSSI](../assets/display-widget-value-min-rssi.png)

Po umístění se na obrazovce zobrazuje jako jednoduchý údaj:

![Widget telemetrické hodnoty](../assets/display-widget-value-telemetry.png)

**Bitmap** — zobrazuje statický obrázek (např. fotografii modelu) nebo
sadu obrázků přepínaných podle hodnoty zdroje (např. ikonu baterie, která
se mění podle napětí):

![Konfigurace widgetu Bitmap](../assets/display-widget-bitmap-config.png)
![Typ widgetu Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — účelově navržený ukazatel baterie, který čte údaje ze senzoru
typu FLVSS: celkové napětí sady, počet článků a napětí každého jednotlivého
článku. Při poklesu pod nastavenou mez **Low voltage** se zobrazení zbarví
červeně — v následujícím příkladu se mez 3,3 V uplatní u nejnižšího článku:

![Konfigurace widgetu LiPo](../assets/display-widget-lipo-config.png)
![Widget LiPo](../assets/display-widget-lipo.png)

**Channels** — až 8 výstupních kanálů jako pruhový graf, vodorovně nebo
svisle:

![Konfigurace widgetu Channels](../assets/display-widget-channels-config.png)
![Widget Channels](../assets/display-widget-channels.png)

**Line Chart** — zaznamenává hodnotu zdroje v čase a resetuje se při
funkci Flight Reset:

![Konfigurace widgetu Line Chart](../assets/display-widget-line-chart-config.png)
![Widget Line Chart](../assets/display-widget-line-chart.png)

- **Source** — co se zaznamenává do grafu.
- **Pause condition** — zdroj, který pozastavuje/obnovuje záznam (nebo
  stačí klepnout na běžící widget, pokud pro tento účel není volný žádný
  zdroj).
- **Log period** — interval vzorkování; 500 ms pokryje přibližně 6 minut,
  než se graf začne posouvat, 1 s přibližně 12 minut.
- **Inverted** — převrátí graf svisle.
- **Auto range** — automaticky přizpůsobí svislou osu datům; při vypnutí
  se namísto toho použijí fixní hodnoty **Min**/**Max** (např. stálý rozsah
  −100 %…+100 %).

Klepnutím na běžící graf vyvoláte volby **Pause/resume**, **Reset**
(vymazání a nový start), **Configure widget** nebo přechod na
**Configure screens**:

![Možnosti Line Chart](../assets/display-widget-line-chart-options.png)

**Text** — zobrazuje obsah textového souboru ve formátu Markdown (načítá
se z `documents/user/` — viz [Správce
souborů](../system-setup/file-manager.md#top-level-folders)):

![Konfigurace widgetu Text](../assets/display-widget-text-config.png)
![Widget Text](../assets/display-widget-text.png)

**Timer Log** — posuvný záznam dřívějších hodnot vybraného časovače,
zapisovaný při každém resetu daného časovače (užitečné pro sledování
využití letových sad během sezení); volba **Reverse** umístí nejnovější
záznam nahoru:

![Konfigurace widgetu Timer Log](../assets/display-widget-timer-logs-config.png)
![Widget Timer Log](../assets/display-widget-timer-log.png)

Podržením záznamu (nebo widgetu) vyvoláte **Clear logs**, úpravu/reset
příslušného časovače nebo přechod na konfiguraci widgetu či obrazovky:

![Nabídka záznamu Timer Log](../assets/display-widget-timer-log-menu.png)

**GPS Map** — zobrazuje živou pozici GPS jako trasu, pro modely se
senzorem GPS (podrobnější informace konkrétně o tomto widgetu najdete ve
vlákně *FrSky - ETHOS Lua Script Programming* na rcgroups, příspěvek
č. 8854):

![Konfigurace widgetu GPS Map](../assets/display-widget-gps-map-config.png)

## Možnosti na úrovni obrazovky

Kromě jednotlivých widgetů má každá obrazovka vlastní nastavení — velikost
mřížky rozvržení, pozadí a to, které obrazovky jsou zařazeny do cyklu
`PAGE`:

![Možnosti konfigurace obrazovky](../assets/display-screen-config-options.png)

Plně nakonfigurovaná domovská obrazovka kombinuje několik widgetů do
jednoho přehledného rozvržení:

![Hlavní zobrazení](../assets/display-main-view.png)

Přidávání dalších obrazovek nad rámec výchozí popisuje [Další
displeje](additional-displays.md), widgety vytvořené skripty Lua nad rámec
vestavěné sady pak [Vlastní widgety](custom-widgets.md).
