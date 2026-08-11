---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Základní příklad pro model s pevnými křídly

Kompletní postup pro letadlo s motorem, 2 křidélky, 2 klapkami, výškovkou
a směrovkou, s jedním servem na každou plochu, sestavené od začátku do
konce pomocí průvodce. Nejprve dokončete
[Počáteční nastavení vysílače](initial-radio-setup.md).

## Krok 1. Kontrola nastavení systému

Tento příklad používá výchozí pořadí kanálů **AETR**.

## Krok 2. Určení potřebných serv/kanálů

[Mixy](../model-setup/mixes.md) jsou srdcem vysílače — až 100 mixovacích
kanálů, přičemž nejnižší čísla se obvykle přiřazují servům (čísla kanálů
totiž přímo odpovídají kanálům přijímače; interní RF modul X20 podporuje
až 24 výstupních kanálů). Vyšší kanály zůstávají k dispozici pro
virtuální kanály nebo další skutečné kanály přes více RF modulů a SBUS.
Naše konstrukce:

| Funkce | Kanály |
|---|---|
| Motor | 1 |
| Křidélka | 2 |
| Klapky | 2 |
| Výškovka | 1 |
| Směrovka | 1 |

(Zatahovací podvozek doplníme později, v
[kroku 10](#step-10-add-a-mix-for-retracts).)

## Krok 3. Vytvoření nového modelu

![Vytvoření modelu letadla](../assets/tut-fw-eg-wiz-create-airplane.png)

Ve [Výběru modelu](../model-setup/model-select.md) zvolte kategorii,
klepněte na **+** a spusťte průvodce **Letadlo**. Pro tento příklad
vyberte **Nestabilizovaný přijímač**.

![Kanály motoru](../assets/tut-fw-eg-wiz-engine.png)
![Kanály křidélek/klapek](../assets/tut-fw-eg-wiz-ail-flaps.png)

Potvrďte 1 kanál motoru, poté 2 kanály křidélek a zvolte 2 kanály klapek.

![Typ ocasních ploch](../assets/tut-fw-eg-wiz-tail.png)
![Kanály výškovky/směrovky](../assets/tut-fw-eg-wiz-ele-rudd.png)

Potvrďte výchozí **Tradiční ocasní plochy** s 1 kanálem výškovky a
1 kanálem směrovky.

![Název modelu](../assets/tut-fw-eg-wiz-name.png)
![Přijímač](../assets/tut-fw-eg-wiz-rx.png)

Pojmenujte jej (např. „FWexample“ — až 15 znaků), dokončete průvodce a
model se stane aktivním; bude vytvořen v kategorii Airplane.

## Krok 4. Kontrola a konfigurace mixů

![Přehled mixů](../assets/tut-fw-eg-mixes.png)

Průvodce již vytvořil mixy křidélek (kanály 1 a 5), výškovky, plynu,
směrovky a klapek (u klapek je zobrazeno `---` — dosud nemají přiřazený
zdroj).

### Křidélka {: #ailerons }

![Mix křidélek](../assets/tut-fw-eg-mixes-ail-mix.png)
![Úprava mixu křidélek](../assets/tut-fw-eg-mixes-ail-edit.png)

**Váha/Rozsahy** — rozsahy nastavte ještě před prvním letem s novým
modelem: umírněné výchylky (např. 30 %) se hodí pro sportovní létání,
plných 100 % pro 3D. Přidejte rozsah 60 % pro střední polohu přepínače SB
a 30 % pro SB dolů — výchozí hodnota (SB nahoru) zůstane 100 %:

![Rozsahy váhy](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — lineární odezva může působit nervózně okolo neutrálu; přidáním
hodnot Expo (např. 60 %/40 %/20 % pro tytéž polohy SB) se odezva v okolí
neutrálu zploští, aniž by se zmenšila maximální výchylka:

![Rozsahy Expo](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Diferenciál** — stejná výchylka křidélka nahoru i dolů způsobuje větší
odpor na křidélku pohybujícím se dolů než na tom, které jde nahoru, což
model stáčí proti směru zatáčky („nepříznivé stočení“). Kladný
diferenciál (běžně 50 %) zmenšuje výchylku dolů vůči výchylce nahoru a
tento jev potlačuje:

![50% diferenciál](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Chcete-li diferenciál ladit za letu, přidržte `ENT` na hodnotě, zvolte
**Použít zdroj** a vyberte Pot1:

![Použít zdroj](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Vybraný Pot1](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Až budete s hodnotou zjištěnou za letu spokojeni, znovu přidržte tlačítko
a zvolte **Převést na hodnotu**, čímž ji trvale uložíte:

![Převést na hodnotu](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim** — tento mix lze odpojit od přiřazeného trimu, aniž by se trim
sám zakázal, takže jej lze využít k jinému účelu:

![Trim křidélek](../assets/tut-fw-eg-mixes-ail-trim.png)

### Výškovka a směrovka

Stejný postup s trojicí rozsahů a Expo, zde na přepínači SC:

![Rozsahy Expo výškovky](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Plyn

![Mix plynu](../assets/tut-fw-eg-mixes-thr-edit.png)

Jako vstup ponechte páčku plynu — rozsahy ani Expo nejsou potřeba — ale
bezpečnostní přepínač je nezbytný; neočekávaně se rozběhnutý modelářský
motor může způsobit vážné zranění.

**Trim dolní polohy** (spalovací motory) — nastavuje otáčky volnoběhu
nezávisle na plném plynu:

![Trim dolní polohy](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Je-li zapnutý, kanál plynu je s páčkou na volnoběhu na hodnotě −75 %;
páčka trimu plynu pak upravuje volnoběh v rozsahu −100 % až −50 %.

**Vypnutí plynu** — bezpečnostní pojistka. S přepínačem SA dolů jako
aktivní podmínkou (aktivní stav je zobrazen tučně) je výstup plynu držen
na −100 %, jakmile páčka klesne pod −85 %:

![Vypnutí plynu](../assets/tut-fw-eg-mixes-thr-cut.png)

Je-li místo toho zapnuta volba **Sticky**, plyn se vypne **okamžitě** po
přepnutí SA dolů, bez ohledu na polohu páčky:

![Vypnutí plynu se Sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

V obou případech je po zrušení aktivní podmínky nutné vrátit páčku pod
−85 %, než plyn může znovu narůst — tím se zabrání skoku motoru na vysoké
otáčky v okamžiku uvolnění přepínače vypnutí plynu.

**Podržení plynu** — nouzové vypnutí z *jakékoli* polohy páčky, které
sníží výstup přímo na −100 % (nebo na nastavenou hodnotu) v okamžiku
splnění podmínky:

![Podržení plynu](../assets/tut-fw-eg-mixes-thr-hold.png)

### Klapky

![Vstup klapek](../assets/tut-fw-eg-mixes-flaps-input.png)

Přiřaďte klapky k přepínači SE a nastavte váhu obou výstupních kanálů na
100 %:

![Váhy klapek](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Krok 5. Spárování přijímače

Zaregistrujte (v případě ACCESS) a spárujte přijímač v
[RF systému](../model-setup/rf-system.md). Než budete pokračovat
k Výstupům, uvažte odpojení táhel serv nebo dočasné zmenšení jejich
výchylek, abyste při nastavování mezí Min/Max nic mechanicky nepřetížili.

## Krok 6. Konfigurace výstupů

![Výstupy](../assets/tut-fw-eg-outputs.png)

[Výstupy](../model-setup/outputs.md) přizpůsobují logiku mixéru skutečné
mechanice modelu.

**Křidélko 1** — po optimalizaci mechanického táhla vystřeďte servo
pomocí **PWM střed** a poté nastavte **Min**/**Max**. Dočasné přiřazení
potenciometru k hodnotě Min (a stejným způsobem poté k Max, jako
v příkladu s diferenciálem výše) nastavení výrazně zrychlí:

![Úprava výstupu křidélka](../assets/tut-fw-eg-outputs-edit-ail.png)

**Klapky** — klapky obvykle potřebují velkou výchylku dolů pro účinné
brzdění; kvůli tomu se v táhlech obětuje část výchylky nahoru tak, aby
klapka byla při středové poloze serva v polovině výchylky dolů, a pomocí
Min/Max se pak nastaví skutečná zatažená poloha a plná výchylka dolů.
Běžným způsobem, jak vyrovnat výsledný nesouhlas mezi klapkami a
křidélky, je 5bodová křivka. Nastavení dokončete pomocí
**[Vyvážení kanálů](../model-setup/outputs.md#balance-channels)**, čímž
synchronizujete levé a pravé křidélko i klapky.

## Krok 7. Úvod do letových režimů

[Letové režimy](../model-setup/flight-modes.md) umožňují modelu nést
nastavení pro jednotlivé úlohy — obdobně jako řazení převodů. Z 20
dostupných používá tento příklad tři: **Default**, **Flaps Half**
(přepínač SE ve střední poloze) a **Flaps Full** (SE nahoru). Aktivní je
první letový režim, jehož podmínka je splněna; režim **Default** nemá
podmínku vůbec a převezme řízení vždy, když neplatí nic jiného — proto
u něj není volba přepínače. Prolnutí 1 sekundy při zapnutí i vypnutí
vyhladí přechod při vysouvání klapek.

## Krok 8. Konfigurace trimů

Existují dva způsoby, jak řešit trim výškovky měnící se s polohou klapek:

**Nezávislé trimy pro každý letový režim** — nejjednodušší varianta: trim
výškovky se stane plně nezávislým pro každý letový režim a přepíná se
automaticky s pohybem SE. Protože se v každém režimu trimuje od začátku,
pomůže [Okamžitý trim](../model-setup/trims.md#instant-trim) — nejprve
vytrimujte normální let, poté přistaňte a použijte toto nastavení jako
výchozí bod pro režimy s klapkami.

**Základní trim s offsetem** — trimuje se jednou v režimu Default a
kompenzace výškovky pro každý režim klapek se na něj vrství jako offset:

1. Nastavte **Krok** trimu na Medium (pro rychlejší počáteční trimování;
   později jej zmenšete pro doladění), **Režim** na Custom a přidejte
   nové chování.
2. **Aktivní podmínka**: `FM1(Flaps Half)`, režim **Offset + Default** —
   trim režimu Flaps Half je pak základní trim plus offset nastavený
   v době, kdy je tento režim aktivní:

   ![Přidat chování](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Totéž zopakujte pro `FM2(Flaps Full)`:

   ![Výběr letového režimu](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Každý režim klapek lze nyní trimovat nezávisle, ale pozdější úprava
základního trimu v režimu Default (např. kvůli korekci tepelného driftu
serva) automaticky posune trimy oba režimy klapek o stejnou hodnotu.

![Výběr vlastního trimu](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Krok 9. Nastavení časovače letové baterie

V [Časovačích](../model-setup/timers.md) upravte Časovač 1: režim
**Down**, počáteční hodnota 5 minut, běh vždy, když je splněna podmínka
**Plyn aktivní** (a časovač není držen v resetu). Volitelně přiřaďte
proporcionální zdroj časování (např. páčku plynu), aby časovač běžel při
plném plynu reálnou rychlostí a se snižováním plynu se zpomaloval.

## Krok 10. Přidání mixu pro zatahovací podvozek {: #step-10-add-a-mix-for-retracts }

![Zdroj mixu podvozku](../assets/tut-fw-eg-retracts-source.png)

Klepněte na některý mix, zvolte **Přidat mix** → **Volný mix**,
pojmenujte jej „Retracts“, nastavte podmínku Always a jako zdroj přepínač
SF. Výchozí akce s váhou 100 % je v pořádku — tím se podvozku přiřadí
např. kanál 8:

![Výstup podvozku](../assets/tut-fw-eg-retracts-outputs.png)
