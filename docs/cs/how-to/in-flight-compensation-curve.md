---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Kompenzační křivka nastavitelná za letu

## Proč

Vysunutí klapek mění prohnutí profilu křídla — hornoplošníky mají tendenci
„vystoupat", dolnoplošníky naopak klesat — což vyžaduje korekci výškovky,
která není lineární vzhledem k výchylce klapek, tedy křivku, ne pevný
posun. Tento postup využívá [Vars](../model-setup/variables.md) k tomu, aby
body kompenzační křivky byly nastavitelné **za letu** pomocí přeřazeného
trimu plynu, přičemž rozhoduje, ke kterému bodu křivky je páčka klapek
právě nejblíže — navazuje na krok kompenzace výškovky z [Praktického
návodu: Butterfly mixer](butterfly-mixer.md).

## 1. Volba typu křivky

Pro plynulou kompenzaci bez zbytečné složitosti postačí 5bodová
[vlastní křivka](../model-setup/curves.md). Bod 5 (nejvíce vpravo, páčka
klapek úplně nahoře / žádné klapky) je vždy pevně na nule — bez vysunutých
klapek není kompenzace potřeba. Ostatní 4 body jsou nastavitelné pomocí
Vars. Protože páčka klapek často stojí mezi dvěma definovanými body, musí
být v této překryvové zóně nastavitelné oba body po obou jejích stranách
současně.

## 2. Výpočet překrývajících se rozsahů

Rozsahy mezi jednotlivými body (převzato se svolením z „Crow-aware adaptive
elevator trim" od Mikea Shellima pro OpenTX na rc-soar.com — mírně
rozšířeno tak, aby rozsah bodu Pt2 dosahoval až k +100 %, z důvodu
vysvětleného v [kroku 6](#6-apply-the-curve)):

| Rozsah páčky klapek | Aktivní bod(y) |
|---|---|
| +100 % až +45 % | pouze Pt2 |
| +45 % až +20 % | Pt2 a Pt3 |
| +20 % až −20 % | pouze Pt3 |
| −20 % až −45 % | Pt3 a Pt4 |
| −45 % až −90 % | pouze Pt4 |
| −90 % až −100 % | pouze Pt5 |

## 3. Konfigurace logických přepínačů

![Logické přepínače adaptivních bodů](../assets/how-in-flight-comp-lsws.png)

Čtyři [logické přepínače](../model-setup/logical-switches.md), každý
využívající funkci **Range** na páčce klapek (plynu), aktivní tehdy, je-li
páčka v zóně příslušného bodu:

- `AdaptivePt2` — rozsah 20 % až 100 % (rozšířeno až na 100 % právě proto,
  aby bylo možné Pt2 nastavovat i bez vysunutých klapek — viz krok 6).

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` — rozsah −45 % až 45 %.

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` — rozsah −90 % až −20 %.

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` — rozsah −100 % až −90 %.

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. Definice Vars pro nastavování

![Přehled Vars](../assets/how-in-flight-comp-vars.png)

Čtyři [Vars](../model-setup/variables.md), `VAdjPt2`–`VAdjPt5`, každá
s rozsahem 0–50 % (v případě potřeby rozšiřte) a s akcí **přeřazeného
trimu plynu** — velikost kroku 1,0 %, podmínka aktivace odpovídající
logický přepínač:

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![Akce VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![Akce VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![Akce VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![Akce VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5-2.png)

Protože je v jednom okamžiku aktivní pouze jeden logický přepínač
(v překryvových zónách nejvýše dva), tentýž fyzický trim bezpečně nastavuje
různé Vars podle polohy klapek.

## 5. Definice kompenzační křivky

![Kompenzační křivka](../assets/how-in-flight-comp-var-comp-curve.png)
![Body kompenzační křivky](../assets/how-in-flight-comp-var-comp-curve-pts.png)

Nová 5bodová vlastní křivka (např. „EleComp") se zapnutou volbou
**Smooth**. Dlouhým stiskem `ENT` na bodech 1–4 a volbou **Use a source**
přiřaďte postupně `VAdjPt5`…`VAdjPt2` (bod 5 zůstává pevně na 0, podle
kroku 1).

## 6. Použití křivky {: #6-apply-the-curve }

Tuto křivku použijte přesně tam, kde [Praktický návod: Butterfly
mixer](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix)
připojuje svoji křivku EleComp k mixu kompenzace výškovky.

Pokud je to možné, vycházejte ze skutečných dat (doporučení výrobce,
příspěvky v komunitě) o tom, jakou výchylku výškovky daná výchylka klapek
vyžaduje; jinak je rozumným výchozím bodem několik milimetrů kompenzace při
plně vysunutých klapkách.

!!! tip "Postup při ladění"
    Začněte s malou výchylkou klapek a malými změnami trimu. `AdaptivePt2`
    lze ladit **úplně bez vysunutých klapek** — klapky krátce vysuňte,
    zase zasuňte a přidávejte kompenzaci vždy po malých krocích, místo
    abyste se pod tlakem snažili trimovat model, který stoupá nebo klesá.
    Znovu krátce vysuňte klapky pro kontrolu a podle potřeby dolaďte. Až
    bude Pt2 v pořádku, přejděte na další bod okolo středu páčky — pokud
    Pt2 vyžadoval velkou změnu trimu, vyplatí se přistát a nastavit
    zbývající body tak, aby každý byl o něco větší než předchozí, místo
    slepého hádání.
