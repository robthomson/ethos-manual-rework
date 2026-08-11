---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Výběr modelu

![Průvodce modelem – letadlo](../assets/model-modelselect-model-wizard-airplane.png)

Vytváří, vybírá, klonuje a maže modely a spravuje uživatelsky definované
kategorie (složky), do nichž jsou modely uspořádány.

## Správa složek modelů

![Složky modelů](../assets/model-modelselect-folders.png)

Ethos umožňuje seskupovat modely do vlastních složek — typicky například
Letadlo, Větroň, Heli, Kvadrokoptéra, Warbird, Loď, Auto, Šablona nebo
Archiv. Dokud žádnou nevytvoříte, nacházejí se modely v automatické složce
**Uncategorized** (vytvoří se při přechodu na Ethos 1.1.0 alpha 17+ nebo
při zkopírování souboru modelu do `\Models` odjinud); jakmile je prázdná,
Ethos ji opět odstraní.

Novou složku vytvoříte klepnutím na **+** vedle „Uncategorized“ (nebo
dlouhým stiskem `PAGE` nahoru/dolů), zadáním názvu (až 15 znaků) a
potvrzením. Složky se řadí abecedně, přičemž **Uncategorized** je vždy
poslední, a odpovídají přímo podsložkám v `\Models` na SD card/eMMC.
Klepnutím na název složky otevřete přejmenování/smazání — smazáním složky
se všechny modely v ní přesunou zpět do Uncategorized.

![Změna složky](../assets/model-modelselect-folder-change-select.png)

Chcete-li model přesunout, klepněte na jeho ikonu, zvolte **Change folder**
a poté klepněte na cílovou složku:

![Volba složky](../assets/model-modelselect-folder-airplane-select.png)

## Přidání nového modelu

![Vytvoření modelu](../assets/model-modelselect-model-create.png)

Vyberte kategorii, v níž má být model vytvořen, klepněte na **+** a poté na
**Create model** pro spuštění průvodce (pokud kategorie ještě neexistuje,
vytvořte ji nejprve). Průvodci jsou k dispozici pro **Airplane**,
**Glider**, **Helicopter**, **Multirotor** a **Other**; každý provede
základním nastavením pro daný typ modelu, včetně volitelných předdefinovaných
mixů pro stabilizované přijímače FrSky (zesílení, režim stabilizace). Názvy
modelů mohou mít až 15 znaků.

### Stabilizované přijímače a pořadí kanálů

![Průvodce: letadlo](../assets/model-modelselect-model-wizard-airplane.png)

Stabilizované přijímače FrSky vyžadují výhradně pořadí kanálů **AETR** —
ponechte [Páčky → Pořadí kanálů](../system-setup/controls.md) na výchozí
hodnotě AETR se zapnutou volbou **První čtyři kanály fixně**, aby výstup
průvodce odpovídal tomu, co přijímač očekává.

Průvodce přiřazuje kanály zprava doleva. Pro 2 křidélka + 1 výškovku +
1 směrovku + 1 motor to je:

| Kan. | Funkce |
|---|---|
| 1 | Křidélko 1 (pravé křidélko) |
| 2 | Výškovka |
| 3 | Plyn |
| 4 | Směrovka |
| 5 | Křidélko 2 (levé křidélko) |

Při tomto přiřazení je diferenciál křidélek pro běžný případ **pozitivní**
(větší výchylka nahoru než dolů). Vlastní manuály přijímačů FrSky aktuálně
uvádějí *opačnou* konvenci (zleva doprava, tedy Kan1 = levé křidélko,
Kan5 = pravé křidélko) — v takovém případě by pro stejný fyzický efekt
musel být diferenciál **negativní**.

!!! tip
    Doporučuje se používat konzistentně konvenci Ethos — všechny
    stabilizační funkce fungují správně v obou případech, protože směr
    kompenzace se nastavuje během konfigurace stabilizace. Pokud přece jen
    potřebujete odpovídat konvenci z manuálu přijímače, nejjednodušší
    cestou je vytvořit model průvodcem běžným způsobem a poté pomocí
    **Swap channels** ve [Výstupech](outputs.md) zaměnit oba kanály
    křidélek — tím zůstane znaménko diferenciálu mixéru křidélek pozitivní.

### Kroky průvodce

![Průvodce: typ ocasních ploch](../assets/model-modelselect-model-wizard-tail.png)
![Průvodce: počet křidélek/klapek](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Průvodce: počet výškovek/směrovek](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Průvodce: motor](../assets/model-modelselect-model-wizard-engine.png)
![Průvodce: přeřazení kanálů](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Průvodce: název](../assets/model-modelselect-model-wizard-name.png)
![Průvodce: přijímač](../assets/model-modelselect-model-wizard-rx.png)

U typu **Airplane** průvodce po volbě typu ocasních ploch a počtu
kormidelních ploch pokračuje počtem kanálů motoru a poté počtem kanálů
křidélek/klapek.

**Konfigurace ocasních ploch** představuje volbu mezi tradičním křížovým
ocasem, V-ocasem, nebo bez ocasu (delta/samokřídlo):

- **Delta/samokřídlo** — vytvořením modelu Airplane se 2 křidélky a bez
  ocasních ploch se automaticky vytvoří mixování elevonů s výchozími
  váhami 50 %, takže plné současné výchylky křidélek + výškovky stále dávají
  dohromady 100 %.
- **Delta se stabilizovaným přijímačem, který provádí mixování** — zvolte
  místo toho 1 křidélko a 1 výškovku; mixování elevonů provádí přijímač
  podle vlastního manuálu.
- **Delta se samostatnými plochami křidélek a výškovky** — nechte průvodce
  proběhnout, jako by model měl ocasní plochy; nakonfiguruje potřebné kanály
  křidélek a výškovky (se směrovkou nebo bez ní) a žádné mixování elevonů
  se nevytvoří.

Krok **přeřazení kanálů** umožňuje přepsat výchozí mapování průvodce, přičemž
je třeba mít na paměti, že stabilizované přijímače potřebují své kanály v
konkrétním pořadí (viz pokyny daného přijímače). Poslední krok nastaví název
modelu a připojí obrázek.

Hotový model se uloží do té kategorie (složky), která byla aktivní při
spuštění průvodce, a v ní se zařadí abecedně. Kompletní podrobný postup
najdete v [Základním příkladu pro model s pevným
křídlem](../tutorials/basic-fixed-wing.md).

## Příjem modelu z jiného vysílače Ethos

![Příjem modelu](../assets/model-modelselect-model-receive.png)

Vyberte cílovou kategorii, klepněte na **+** a poté na **Receive model** —
vysílač bude čekat a zobrazí svou Bluetooth adresu, aby jej odesílatel mohl
najít. Na odesílajícím vysílači klepněte na model a zvolte **Send model**;
přijímající vysílač před přijetím potvrdí příchozí název souboru.

## Výběr modelu

Klepnutím na **Model select** zobrazíte seznam modelů.

!!! note "Konverze modelu po aktualizaci Ethos"
    Ethos konvertuje každý model jednotlivě při jeho prvním *vybrání* po
    aktualizaci verze, ne všechny naráz při aktualizaci — nedochází k žádné
    patrné prodlevě a je bezpečné to provést kdykoli později, i pod ještě
    novější verzí Ethos. Datum **Last Modification** ve spodní části
    obrazovky výběru se při konverzi aktualizuje (stejně jako při editaci
    modelu — jinak zůstává nezměněno).

**Rychlý výběr** — dlouhý dotyk nebo dlouhý stisk `ENT` na ikoně modelu na
něj okamžitě přepne.

**Nabídka správy modelu** — klepnutím na model jej označíte, dalším
klepnutím otevřete nabídku:

- **Set current model**
- **Clone** — duplikuje model. Klon automaticky získá nové číslo přijímače;
  pokud místo toho přeřadíte číslo přijímače původního modelu, funguje bez
  potřeby opětovného párování.
- **Change folder**
- **Send**/**Receive** — do jiného vysílače nebo z něj, jak je popsáno výše.
- **Delete** — nabízí se pouze u modelu, který není aktuálně vybraný.
