---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Letové režimy

![Letové režimy](../assets/model-fm.png)

Letové režimy (letové fáze) umožňují přepínačem volit mezi odlišnými
způsoby chování téhož modelu — u větroňů to může být Start/Cestovní/
Rychlost/Termika, u motorových modelů Normální/Vzlet/Přistání, u vrtulníků
Normální (rozběh, vzlet/přistání) / Idle Up 1 (akrobacie) / Idle Up 2 (3D).
Zbavují pilota většiny nutnosti ručně přepínat a dotrimovávat: letový režim
může mít vlastní nezávislé trimy a může podmiňovat jak
[Proměnné](variables.md), tak [Mixy](mixes.md) — to dohromady stačí i na
skutečně složitá nastavení. Letové režimy použité na reálném modelu najdete
v [Základním příkladu pro model s pevným
křídlem](../tutorials/basic-fixed-wing.md).

Ve výchozím stavu nejsou definovány žádné letové režimy. Klepněte na
výchozí letový režim a zvolte **Edit** pro jeho přejmenování, nebo **Add**
pro vytvoření nového — celkem až 20.

## Název

Popisný název — Cestovní, Rychlost, Termika, Vzlet, Přistání, cokoli, co se
hodí.

## Podmínka aktivace

![Formulář letového režimu](../assets/model-fm-form.png)

Nový letový režim je zpočátku neaktivní (`---`). Po nastavení může být
ovládán polohou přepínače nebo tlačítka, funkčním přepínačem, logickým
přepínačem, systémovou událostí (vypnutí/podržení plynu) nebo polohou trimu.

**Výchozí** letový režim nemá podmínku aktivace vůbec — je aktivní vždy,
když neplatí podmínka žádného jiného letového režimu. Vždy je aktivní pouze
jeden letový režim: první (v pořadí priority), jehož podmínka je právě
splněna. Aktivní režim je zobrazen tučně.

!!! warning "Přidání letového režimu k existujícímu modelu"
    Nově přidaný letový režim je ve výchozím stavu aktivní v každém mixu,
    který již na letových režimech závisí — u každého takového mixu
    zkontrolujte, že se stále chová správně, zejména u mixu typu **Lock**,
    který uzamyká kanál na konkrétní letový režim.

## Náběh, doběh

Časy přechodu pro plynulé prolínání mezi letovými režimy (např. 1 sekunda
v každém směru) — má to vliv pouze na mixy, které samy závisejí na letových
režimech.

## Správa letových režimů

![Přesun letového režimu](../assets/model-fm-move.png)
![Výběr pro přesun](../assets/model-fm-move-select.png)
![Režimy 0–3](../assets/model-fm-0to3.png)

Klepnutím na letový režim vyvoláte **Edit**, **Add**, **Clone** nebo
**Delete**. **Klonovaný** letový režim přebírá nastavení svého předlohového
režimu v každém mixu, který používá letové režimy — stejné chování, stejný
aktivní/neaktivní stav — proto se klon ve výchozím stavu přidává jako
poslední letový režim, aby nezasahoval do existujících. **Move** mění
prioritu letového režimu: priorita je ve vzestupném pořadí a (jak je uvedeno
výše) aktivní je první režim se splněnou podmínkou.
