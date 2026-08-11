---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mixy

![Ikona Mixy](../assets/model-icon-mixes.png)

Mixy jsou jádrem programování modelu v Ethos — zde se vstupy (páčky,
přepínače, senzory, cokoli, na co lze dosáhnout jako na
[zdroj](../getting-started/user-interface-and-navigation.md#choosing-a-source))
směrují, tvarují a kombinují do výstupních kanálů. Pro každý model lze
definovat až 120 mixů.

![Tabulka mixů](../assets/model-mixes.png)

Pokud byl model vytvořen průvodcem **Výběr modelu**, jsou zde již základní
mixy (křidélka, výškovka, plyn, směrovka a cokoli dalšího, co daná
konstrukce vyžaduje) předvyplněny. Vybráním mixu a stiskem `ENT` se otevře
kontextová nabídka, ve které jej lze upravit, přidat nový mix, přepnout na
[zobrazení po kanálech](#per-channel-view), změnit jeho pořadí, duplikovat
jej nebo smazat. Neaktivní mixy jsou zobrazeny šedě a smazání vždy nejprve
vyžaduje potvrzení.

## Struktura mixu {: #anatomy-of-a-mix }

Každý mix má stejnou sadu polí, bez ohledu na to, z jaké kategorie pochází.
Mix **křidélek** je reprezentativním příkladem — mixy výškovky a směrovky
mají zcela shodné rozvržení.

![Mix křidélek](../assets/model-mixes-ail-edit.png)

![Editor mixu křidélek](../assets/model-mixes-ail.png)

**Název** — ve výchozím stavu odpovídá typu mixu, lze jej upravit.

**Podmínka** — výchozí hodnotou je *Always*. Lze ji omezit na polohu
přepínače, funkční přepínač, logický přepínač, letový režim, systémovou
událost (vypnutí/podržení plynu) nebo polohu trimu; v takovém případě se mix
uplatní pouze tehdy, je-li podmínka splněna.

**Letové režimy** — jsou-li definovány letové režimy, lze mix navíc omezit
na jeden nebo více z nich.

**Křivka** — ve výchozím stavu je k dispozici křivka **Expo** (0 = lineární;
kladná hodnota zjemňuje odezvu okolo středu, záporná ji zostřuje):

![Křivka Expo](../assets/model-mixes-ail-expo.png)

Namísto ní lze vybrat kteroukoli křivku dříve definovanou v sekci
[Křivky](curves.md). Na jeden mix lze naskládat až 6 křivek, každou s vlastní
podmínkou — je-li současně splněno více podmínek, uplatní se křivka umístěná
v seznamu výše. Křivky se aplikují **před** hodnotami rates.

**Rates** — jeden nebo více řádků s váhou, každý volitelně podmíněný
přepínačem, funkčním přepínačem, logickým přepínačem, polohou trimu nebo
letovým režimem. První řádek je výchozí a je aktivní vždy, když není splněna
podmínka žádného jiného řádku:

![Rates křidélek](../assets/model-mixes-ail-weight.png)

Místo pevného procentuálního údaje lze hodnotu rate řídit ze
[zdroje](../getting-started/user-interface-and-navigation.md#choosing-a-source)
— například z potenciometru, aby bylo možné ji upravovat za letu:

![Rate řízený ze zdroje](../assets/model-mixes-ail-diff.png)

**Diferenciál** (-100 až 100, výchozí 0) — poskytuje větší výchylku v jednom
směru než ve druhém. U křidélek jde o klasický postup s větší výchylkou
nahoru než dolů pro potlačení nežádoucího zatáčení. Zobrazuje se pouze
tehdy, má-li mix více než jeden výstupní kanál; diferenciál konkrétně
vyžaduje konfiguraci výstupů typu V-tail nebo dvou samostatných křidélek,
aby měl smysl.

**Počet kanálů / výstupů** — kolik výstupních kanálů tento mix řídí a na
které fyzické výstupy jsou mapovány:

![Počet kanálů](../assets/model-mixes-ail-ch-count.png)

Dlouhý stisk `ENT` na výstupním kanálu jinde v uživatelském rozhraní
(např. v sekci [Výstupy](outputs.md)) přejde přímo zpět na tuto stránku.

## Mix plynu

Mix plynu je mix typu křidélka/výškovka/směrovka doplněný o bezpečnostní
volby specifické pro motor.

![Mix plynu](../assets/model-mixes-thr.png)

**Vstup** — zdroj plynu, obvykle páčka plynu, kterou však lze zaměnit za
potenciometr, posuvník, přepínač, trim, kanál, osu gyra, kanál učitele,
časovač nebo jakýkoli jiný zdroj.

**Trim volnoběhu** — u spalovacích motorů umožňuje samostatnému trimu
nastavovat otáčky volnoběhu bez ovlivnění polohy plného plynu. Je-li trim
volnoběhu zapnutý, je kanál plynu při páčce na nízkém volnoběhu na -75 % a
trim plynu pak nastavuje volnoběh v rozsahu -100 % až -50 %:

![Nabídka trimu volnoběhu](../assets/model-mixes-thr-trim-menu.png)

![Trim volnoběhu v dolní poloze](../assets/model-mixes-thr-trim-low-position.png)

**Vypnutí plynu** — striktní bezpečnostní blokování: kanál je aktivní teprve
poté, co páčka plynu projde volnoběhem, takže nechtěné přehození přepínače
nemůže rozběhnout motor z polohy vysokého plynu:

![Vypnutí plynu](../assets/model-mixes-thr-cut.png)

**Podržení plynu** — drží kanál na pevné hodnotě bez ohledu na polohu páčky,
bez bezpečnostního blokování, které poskytuje vypnutí plynu:

![Podržení plynu](../assets/model-mixes-thr-hold.png)

Plyn rovněž nabízí vlastní nastavení počtu výstupních kanálů, stejně jako
kterýkoli jiný mix:

![Počet kanálů plynu](../assets/model-mixes-thr-ch-count.png)

!!! note "Blokování plynu"
    Ethos vyžaduje, aby vstup mixu plynu prošel hodnotou -100 %, než dojde
    k aktivaci, a to bez ohledu na nastavení vypnutí/podržení plynu — model
    vytvořený průvodcem výběru modelu s tím již počítá, ale ručně vytvořené
    mixy plynu by na to měly být připraveny také.

## Knihovny mixů {: #mix-libraries }

Knihovna předdefinovaných mixů v dialogu **Přidat mix** je přizpůsobena
kategorii modelu zvolené při jeho vytvoření — letadlo, větroň, helikoptéra a
multirotor nabízejí každý jinou sadu:

![Knihovna mixů pro letadlo](../assets/model-mixes-library-airplane.png)

![Knihovna mixů pro větroň](../assets/model-mixes-library-glider.png)

![Knihovna mixů pro helikoptéru](../assets/model-mixes-library-heli.png)

![Knihovna mixů pro multirotor](../assets/model-mixes-library-multirotor.png)

Každá knihovna obsahuje také **Volný mix** — univerzální typ mixu bez
předvoleného vstupu/výstupu, který je flexibilnější než specializované
položky, ale pro dosažení stejného výsledku vyžaduje více nastavování.

## Zobrazení po kanálech {: #per-channel-view }

Pokud je na jednom výstupu naskládáno více mixů, může být obtížné rozpoznat
jejich souhrnný efekt z výše uvedené plošné tabulky. Vybráním mixu a volbou
**View by channel** se místo toho seskupí všechny mixy ovlivňující jeden
výstup:

![Přepnutí na zobrazení po kanálech](../assets/model-mixes-chview-select.png)

![Sbalený kanál](../assets/model-mixes-chview-collapsed.png)

![Rozbalený kanál výškovky](../assets/model-mixes-chview-elevator.png)

Rozbalením souhrnného řádku kanálu se zobrazí všechny mixy, které do něj
přispívají, každý se svým aktuálním číselným i grafickým výstupem — to je
užitečné pro ověření, kolik přesně přidává druhotný mix (např. kompenzace
klapek do výškovky) k primárnímu vstupu z páčky:

![Detail zobrazení kanálu výškovky](../assets/model-mixes-chview-elevator-channel.png)

![Kanál výškovky se zvýrazněným mixem](../assets/model-mixes-chview-elevator-channel-view.png)

Vybráním podřízeného mixu místo souhrnného řádku se otevře stejná kontextová
nabídka jako v plošné tabulce (úprava, přepnutí zpět na tabulkové zobrazení,
smazání):

![Volba tabulkového zobrazení ze zobrazení po kanálech](../assets/model-mixes-chview-table-view-select.png)

![Zpět v tabulkovém zobrazení](../assets/model-mixes-chview-back-at-mixes-view.png)
