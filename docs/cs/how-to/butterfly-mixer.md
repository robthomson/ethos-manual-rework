---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Mix Butterfly (vrána)

Brzdění butterfly (též crow) řídí rychlost klesání, především u větroňů:
křidélka se mírně zvednou, zatímco klapky se vychýlí hodně dolů, čímž
vzniká značný odpor — ideální pro řízení přiblížení na přistání. Tento
postup předpokládá větroň, který již má kanály klapek (vytvořené
průvodcem [Výběr modelu](../model-setup/model-select.md)), přičemž jako
vstup brzdy slouží páčka plynu: s páčkou nahoře žádné butterfly, s
pohybem dolů postupně více, s kompenzací výškovky, aby větroň při
nasazení crow nevystoupal vzhůru.

## 1. Vypnutí výchozího mixu Flaps

![Vypnutí mixu klapek](../assets/how-to-butterfly-flaps-disable.png)

U mixu Flaps vytvořeného průvodcem nastavte **Aktivní podmínku** na `---`
— nebude se používat.

## 2. Vytvoření mixu Butterfly

![Přidaný mix Butterfly](../assets/how-to-butterfly-mix-added.png)

Klepněte na kterýkoli mix, **Přidat mix** → **Butterfly** z [knihovny
mixů](../model-setup/mixes.md#mix-libraries), umístěný za (nyní vypnutý)
mix Flaps.

## 3. Nastavení vstupu

![Vstup plynu](../assets/how-to-butterfly-mix-source-thr.png)

Nastavte **Vstup** na **Plyn**. Protože plyn s páčkou nahoře běžně
udává maximum, zatímco butterfly musí být s páčkou nahoře 0, dlouze
stiskněte `ENT` na položce Plyn a vyberte **Invertovat**:

![Invertování plynu](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Invertovaný plyn](../assets/how-to-butterfly-mix-source-thr-neg.png)

Vstup nyní s páčkou plně nahoře udává 0 a pole zobrazuje `-Throttle`
jako potvrzení inverze. Pokud nemá být butterfly dostupné trvale,
nastavte **Aktivní podmínku** na přistávací letový režim (nebo jiný
přepínač).

## 4. Přidání křivky s mrtvým pásmem

![Výběr křivky](../assets/how-to-butterfly-mix-curve-select.png)

Malé mrtvé pásmo na nulovém konci páčky zabrání nechtěnému nasazení
brzdy vlivem drobného šumu páčky poblíž koncové zarážky. Přidejte vlastní
3bodovou křivku (např. s názvem „Crowdb") s vypnutým **Snadným režimem**,
aby bylo možné posouvat body X:

![3bodová křivka](../assets/how-to-butterfly-mix-curve-3pt.png)
![Body křivky](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    Přidání vlastní křivky do mixu Butterfly odstraní jeho interní offset
    0–100 (normálně aplikovaný automaticky) — tuto transformaci 0–100
    nyní musí zajistit sama křivka. V tomto příkladu zůstává výstup 0 %,
    dokud páčka plynu nedosáhne −90 %, poté lineárně stoupá na 100 %:

    ![Přidaná křivka](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Nastavení křidélek a klapek

![Výstup křidélek](../assets/how-to-butterfly-mix-ailerons.png)

Obvyklým rozdělením je mírné zvednutí křidélek (např. 20 %) v kombinaci s
velkou výchylkou klapek. Klapky obvykle potřebují mnohem větší zdvih dolů
než nahoru — toho se běžně dosahuje pootočením páek serv klapek o 20–30°
od neutrálu přímo v mechanice, takže klapky jsou při neutrální poloze
serva přibližně napůl vychýlené dolů:

![Klapky nahoře](../assets/how-to-butterfly-mix-flaps-up.png)
![Klapky dole](../assets/how-to-butterfly-mix-flaps-down.png)

Nastavte váhu mixu klapek vysoko (např. −180 %) pro maximální zdvih;
skutečný fyzický zdvih je dán hodnotami Min/Max ve
[Výstupech](../model-setup/outputs.md).

!!! tip
    Abyste serva nepřetěžovali, začněte s hodnotami Min/Max ve Výstupech
    konzervativně (např. ±30 %) a při finálním nastavení je opatrně
    rozšiřujte s ohledem na zadrhávání mechaniky.

## 6. Přidání offsetového mixu „Flaps Neutral"

![Offsetový mix 80 %](../assets/how-to-butterfly-offset-mix-80.png)

Protože pootočení páek serv nechává klapky při neutrálu serva vychýlené o
~20–30 %, vrátí je **Offset Mix** pro normální let do skutečné neutrální
polohy vůči křídlu. Začněte s offsetem 80 % (bude se dolaďovat) a se
2 výstupními kanály přiřazenými k oběma kanálům klapek:

![Klapky nahoře s offsetem](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Klapky dole s offsetem](../assets/how-to-butterfly-offset-mix-flaps-down.png)

S páčkou plynu plně nahoře (mix Butterfly vypnutý) zkontrolujte, že
hodnoty mixeru klapek odpovídají offsetu (80 %); přesun páčky klapek do
plného vysunutí by měl posunout výstup mixeru o celou váhu (např. z 80 %
na −100 %, tedy rozsah 180 %). Skutečné limity zdvihu dolaďte ve
Výstupech pomocí Min/Max nebo křivky.

## 7. Přidání kompenzační křivky a mixu výškovky {: #7-add-the-elevator-compensation-curve-and-mix }

![Kompenzační křivka](../assets/how-to-butterfly-comp-curve.png)
![Body kompenzační křivky](../assets/how-to-butterfly-comp-curve-points.png)

Protože potřebná kompenzace není lineární, použijte místo fixní váhy
křivku. Definujte vlastní 5bodovou křivku (např. „EleComp") — v tomto
příkladu začíná na hodnotách 12 %/10 %/8 %/5 %/0 % v jednotlivých bodech;
bez známého výchozího bodu pro váš model je nutné je najít empiricky.

Dále tuto křivku převeďte na hodnotu použitelnou jako **Váha** mixu:
přidejte [Volný mix](../model-setup/mixes.md#mix-libraries) („EleCompx")
se zdrojem Plyn a připojenou křivkou EleComp, s výstupem na vysoký
nevyužitý kanál (např. CH20):

![Kompenzační mix na CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

Zpět v mixu Butterfly dlouze stiskněte `ENT` na položce **Váha** výstupu
výškovky, zvolte **Použít zdroj** a poté vyberte CH20 (EleCompx) z
kategorie Kanály:

![Výškovka používající CH20 jako zdroj](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Výběr zdroje](../assets/how-to-butterfly-mix-ele-use-source.png)

Mix Butterfly je nyní plně nastavený:

![Nastavená kompenzace výškovky](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Kontrola pomocí zobrazení po kanálech

![Zobrazení po kanálech](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Přepněte na výškovce na [Zobrazení po
kanálech](../model-setup/mixes.md#per-channel-view) a sledujte, jak se
při pohybu páčky plynu/brzdy současně aktualizují všechny přispívající
mixy (vstup páčky + kompenzace Butterfly) — je to výrazně snazší pro
ladění než plochý tabulkový přehled.

!!! tip
    Před nastavováním výchozích hodnot kompenzační křivky se vyplatí mít
    údaje o potřebném zdvihu výškovky v závislosti na výchylce klapek (od
    výrobce modelu nebo z komunitních zdrojů). Pokud takové údaje nemáte,
    začněte s několika milimetry zdvihu výškovky na plné vysunutí klapek
    a postupně dolaďujte.
