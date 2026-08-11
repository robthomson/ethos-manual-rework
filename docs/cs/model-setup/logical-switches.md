---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Logické přepínače

![Nabídka logických přepínačů](../assets/model-lsw-menu.png)

Logické přepínače jsou uživatelem programované *virtuální* přepínače — nejde
o fyzické ovladače, ale lze je použít jako spouštěč programu všude tam, kde
lze použít fyzický přepínač. Každý z nich vyhodnocuje nastavenou podmínku
vůči svým vstupům (další přepínače, telemetrické hodnoty, hodnoty mixů,
hodnoty časovačů, kanály gyra/trenéra a další) a podle toho nabývá stavu
True nebo False. Podporováno je až 100 přepínačů; ve výchozím stavu není
definován žádný. Nový přidáte pomocí **+**; popisek definovaného přepínače
v nabídce svítí zeleně, je-li True, a červeně, je-li False. Dotykem na
existující přepínač vyvoláte **Edit**/**Move**/**Copy-paste**/**Clone**/**Delete**.

![Přidání logického přepínače](../assets/model-lsw-add.png)

## Funkce

Každá funkce podporuje normální nebo invertovaný výstup.

- **A ~ X** — platí, když je zdroj `A` *přibližně* rovný (s tolerancí
  ~10 %) pevné hodnotě `X`. Obvykle vhodnější než přesná rovnost —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — protože při `A = X` se telemetrická hodnota, která kolísá například
  mezi 8,5 V a 8,35 V okolo cílových 8,4 V, nemusí nikdy přesně na
  8,4 V zastavit, takže by přepínač nikdy nesepnul.
- **A = X** — platí pouze tehdy, když je `A` přesně rovno `X`.
- **A > X** / **A < X** — platí, když je `A` větší/menší než `X`.
- **|A| > X** / **|A| < X** — jako výše, ale porovnává se absolutní
  hodnota `A` (znaménko se ignoruje).
- **Δ > X** — platí, když změna `A` (delta) během intervalu **Check
  interval** dosáhne alespoň `X`. Interval `---` znamená nekonečné okno.

  ![Delta větší než X](../assets/model-lsw-delta-gtX.png)
  ![Absolutní delta větší než X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — jako výše, ale s absolutní hodnotou změny.
- **Range** — platí, když `A` leží v zadaném rozsahu.

  ![Range](../assets/model-lsw-range.png)

- **AND** — platí pouze tehdy, když je pravdivý každý uvedený zdroj
  (Value 1…N).

  ![AND](../assets/model-lsw-AND.png)

- **OR** — platí, když je pravdivý alespoň jeden uvedený zdroj.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (exkluzivní OR) — platí, když je pravdivý *právě jeden* uvedený
  zdroj.

  ![XOR](../assets/model-lsw-XOR.png)

- **Timer generator** — trvale se sám přepíná zap/vyp: zapnuto po dobu
  **Duration active**, vypnuto po dobu **Duration inactive**.

  ![Timer generator](../assets/model-lsw-timer-generator.png)

- **Sticky** — záchyt (klopný obvod SR); viz [níže](#sticky).
- **Edge** — krátkodobý impuls; viz [níže](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Zachytí stav **True** ve chvíli, kdy je splněna podmínka **Trigger ON**,
a zůstane True, dokud není splněna podmínka **Trigger OFF** — volitelně
s hlídáním podmínkou **Active condition** (dokud je tato podmínka False,
je výstup držen na False bez ohledu na ostatní; vnitřní záchyt funkce
Sticky se přitom dále vyhodnocuje na pozadí a jeho stav se na výstup opět
propustí, jakmile se Active condition vrátí do True, s ohledem na
nastavená zpoždění).

Od verze Ethos 1.6.2 přijímají oba spouštěče modifikátor **Edge** (dlouhý
stisk `ENT` na podmínce spouštěče, volba Edge — zobrazuje se s předponou
`†`), který umožňuje výrazně jemnější řízení:

![Sticky s edge](../assets/model-lsw-sticky-with-edge.png)
![Výběr volby Edge](../assets/model-lsw-sticky-edge-select.png)

- **Trigger ON `SA` (bez zpoždění)** — zachytí True v okamžiku, kdy SA
  přejde do vysoké úrovně.
- **Trigger ON `SA` (delay = 1s)** — zachytí True 1 s po přechodu SA do
  vysoké úrovně, *pokud* je SA na konci této sekundy stále ve vysoké
  úrovni.
- **Trigger ON `†SA` (delay = 1s)** — zachytí True→False 1 s po přechodu
  SA do vysoké úrovně, **bez ohledu** na to, zda je SA v té době stále
  vysoko (hrana už proběhla; zpoždění pouze určuje časování výsledku).

Trigger OFF se chová stejně, jen obráceně. Zpoždění se uplatňují **až za**
podmínkou Active condition — změna Active condition tedy časování zpoždění
znovu spustí, než se zachycená hodnota opět dostane na výstup. Současné
překlopení obou spouštěčů z False→True **přepne** výstup funkce Sticky
jednou do opačného stavu. Viz také [Společné parametry](#shared-parameters)
níže.

### Edge

![Edge](../assets/model-lsw-edge.png)

Krátkodobý impuls: True po dobu **Duration**, jakmile je splněna podmínka
spouštěče. **During** je dvojice `[t1:t2]`, která přesně určuje, kdy:

- **Náběžná hrana, During = 0.0s** — sepne v okamžiku, kdy Trigger ON
  přejde z False→True.

  ![Náběžná hrana](../assets/model-lsw-edge-rising-edge.png)
  ![During = 0](../assets/model-lsw-edge-during-eq0.png)

- **Náběžná hrana, During ≥ 0.0s (např. 5.0s)** — sepne 5 s po přechodu
  Trigger ON do True a ignoruje jakékoli kratší „špičky“ v průběhu tohoto
  5sekundového okna.

  ![During > 0, náběžná hrana](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![During > 0](../assets/model-lsw-edge-during-gt0.png)

- **Sestupná hrana, During = 0.0s** — sepne v okamžiku, kdy Trigger ON
  přejde z True→False.
- **Sestupná hrana, During ≥ 0.0s (např. 3.0s)** — sepne při přechodu
  True→False, ale pouze pokud předtím byl stav True alespoň 3 s.
- **Impuls (nastaveno t1 i t2)** — sepne pouze tehdy, když Trigger ON
  projde sekvencí False→True→False v daném okně (např. mezi 2 s a 5 s).

## Společné parametry {: #shared-parameters }

![Společné parametry](../assets/model-lsw-common-parameters.png)

- **Active condition** — hlídá výstup přepínače stejným způsobem jako
  u funkce Sticky výše. Možnosti: Always on, pozice přepínače/funkčního
  přepínače/logického přepínače/trimu, Telemetry, Flight modes nebo
  systémová událost (Throttle hold, Throttle cut, Throttle active,
  Telemetry active, RSSI low, Trainer active, Flight reset).
- **Delay before active** / **Delay before inactive** — jak dlouho musí
  podmínka platit (nebo neplatit), než ji výstup převezme; až 60 s. Netýká
  se funkcí Timer generator ani Edge. (Příklad zpoždění použitého k
  potlačení zákmitů při krátkém poklesu napětí najdete v [Praktickém
  návodu: Varování o kapacitě baterie](../how-to/battery-capacity-warning.md).)
- **Confirmation before active** / **inactive** — před skutečnou změnou
  stavu vyžádá potvrzení od uživatele (s možností Cancel, pro případy, kdy
  se stav mění příliš často, než aby to bylo užitečné) — vhodné pro
  zajištění něčeho rizikového, například pro potvrzení před vzdáleným
  vypnutím pozemního modelu.

  ![Potvrzení true](../assets/model-lsw-confirm-lsw-true.png)
  ![Potvrzení false](../assets/model-lsw-confirm-lsw-false.png)

- **Min Duration** — jakmile je stav True, zůstane True alespoň po tuto
  dobu. Při ponechání na `---` může být výstup True pouze po jediný cyklus
  mixéru — příliš krátce, než aby bylo v uživatelském rozhraní vidět
  ztluštění řádku.
- **Max Duration** — jakmile je stav True, po uplynutí této doby se
  automaticky vrátí na False, pokud je stále nastaven. Obě doby lze
  nastavit až na 60 s.
- **Comment** — volný text zobrazovaný všude, kde je tento přepínač přidán
  do hodnotového widgetu; slouží k dokumentaci jeho účelu.

## Použití s telemetrií

Systémová událost **Telemetry active** (nebo přepínač, jehož zdrojem je
telemetrický senzor a který je aktivní pouze tehdy, když tento senzor
posílá data) pokrývá podmínky typu „je právě přijímána telemetrie“.

!!! warning
    [Mix](mixes.md) řízený logickým přepínačem založeným na telemetrii
    potřebuje **druhou** akci mixu se stejným přepínačem **invertovaným**,
    aby mix měl platnou hodnotu i po ztrátě telemetrie — nezapomeňte, že
    neaktivní mix dává na výstup neutrál (0 % / 1500 µs, případně
    **poloviční plyn** na kanálu plynu). Alternativně použijte akci
    **Offset**, která má samostatné hodnoty pro aktivní a neaktivní stav
    již zabudované — např. zdroj **0** (speciální hodnota) s offsetem
    nastaveným tak, aby mix dával +100 %, když je `LS3` aktivní, a −100 %,
    když je neaktivní, pokryje oba případy v jediné akci.

## Porovnání zdrojů

Zdroj se běžně porovnává s pevnou hodnotou, ale místo toho lze přímo
porovnat dva zdroje *stejného* typu — např. dva časovače, dvě napětí nebo
dva senzory otáček.

## Ignorování vstupu trenéra od žáka

![Ignorování vstupu trenéra](../assets/model-lsw-ignore-trainer-input.png)

[Volby](../getting-started/user-interface-and-navigation.md#choosing-a-source)
zdroje umožňují vyloučit vstup trenéra z připojeného vysílače žáka —
typicky se to používá u logického přepínače, který hlídá pohyb páčky
samotného **učitele** (např. aby bylo možné okamžitě zasáhnout, když se
něco pokazí), aniž by jej spouštěly i vstupy žáka. Obvykle se kombinuje
s přepínačem trenéra, který řídí Active condition na straně učitele.
