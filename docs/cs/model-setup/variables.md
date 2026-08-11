---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Proměnné

![Proměnné](../assets/model-vars.png)

Proměnné („Vars“) jsou pojmenované kontejnery pro hodnoty vlastních
nastavení modelu, na které se lze odkazovat kdekoli jinde v programování —
včetně [mixů](mixes.md). Jejich umístění do samostatné sekce odděluje
*konfigurační data* modelu od jeho *programové logiky*: místo prohledávání
desítek mixů kvůli nalezení a úpravě jedné hodnoty je vše na jednom místě
pod srozumitelným názvem. K dispozici je 64 proměnných; ve výchozím stavu
žádná neexistuje. Novou přidáte pomocí **+**; klepnutím na existující
proměnnou zobrazíte **Edit**/**Move**/**Copy**/**Clone**/**Delete**.

![Přidání proměnné](../assets/model-vars-add.png)

Proměnná může obsahovat pevnou konstantu, nebo být nastavitelná v rámci
uživatelem definovaných limitů (aby chybné hodnoty nezpůsobily havárii),
a může mít *odlišnou* hodnotu pro každou aktivní podmínku (např. pro každý
letový režim). Hodnoty jsou trvale uchovány mezi jednotlivými zapnutími.
Proměnná zastupuje jakoukoli běžnou číselnou hodnotu všude, kde je
dostupná [funkce
Options](../getting-started/user-interface-and-navigation.md#the-options-feature)
(pole s ikonou hamburgeru).

!!! example
    Kluzák s dělenými křidélky (jejichž vnitřní sekce slouží zároveň jako
    přistávací klapky) potřebuje jediné společné nastavení diferenciálu
    křidélek, používané všude, kde všechny čtyři plochy pracují jako
    křidélka — proměnná obsahující tuto jednu hodnotu, na kterou se
    odkazuje každý příslušný mix, zajišťuje konzistenci a umožňuje ladění
    na jediném místě.

## Přidání proměnné

![Nová proměnná](../assets/model-vars-new_var.png)

- **Value** — aktuální hodnota (pouze pro čtení).
- **Name** — název, lze editovat.
- **Comment** — volný text vysvětlující účel proměnné.
- **Range** — dolní/horní limit (na jedno desetinné místo, v rozsahu
  ±500 %), který hodnota proměnné nikdy nemůže překročit.

### Hodnoty

![Hodnoty proměnné](../assets/model-vars-values.png)

- **Fixed** — jediná konstanta s jedním desetinným místem.
- **Multiple/variable** — volba **Add new value** přiřadí hodnotu ke každé
  aktivní podmínce. Např. `Var12` má hodnotu 9 %, je-li aktivní letový
  režim Thermal (FM4), a −3 %, je-li aktivní režim Speed (FM5), přičemž
  rozsah (Range) je omezen na −10 %…+15 %, takže ani jedna hodnota nemůže
  překročit rozumné limity:

  ![Hodnoty závislé na letovém režimu](../assets/model-vars-fm-dependent.png)
  ![Přidání hodnoty](../assets/model-vars-add-value.png)

### Akce

![Akce proměnné](../assets/model-vars-actions.png)
![Přidání akce](../assets/model-vars-add-action.png)

Akce mění hodnotu proměnné v čase na základě určitého vstupu.

**Přeřazený trim (Repurposed trim)** — předá jeden z fyzických trimů
k nastavování této proměnné namísto jeho běžné funkce, obvykle pouze
v rámci jedné aktivní podmínky:

![Přeřazení trimu](../assets/model-vars-functions-repurpose.png)
![Výběr trimu k přeřazení](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Přeřaďte trim plynu k nastavování proměnné pro kompenzaci prohnutí
    profilu, ale pouze pokud je aktivní letový režim Landing (FM3),
    s rozsahem 0–25 % a krokem 1,0 % na jedno kliknutí. Mimo tuto aktivní
    podmínku se trim automaticky vrátí ke své běžné funkci.

**Aritmetické akce** — řízené jakýmkoli vstupem:

- **Assign** — nastaví proměnnou na konkrétní hodnotu.
- **Add** / **Subtract** / **Multiply** / **Divide** — aritmetická operace
  s aktuální hodnotou.
- **Percentage** — použije procentuální podíl řídicího vstupu.
- **Min** / **Max** — omezí proměnnou vůči řídicímu vstupu.

  ![Akce funkcí](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` přímo přiřadí proměnné 40 %; `FS1(edge)` přidá 2 při
    každém stisku (s omezením na maximum rozsahu); `FS2(edge)` odečte 2
    při každém stisku (s omezením na minimum rozsahu). Volba **Edge**
    (dlouhý stisk funkčního přepínače) je zde podstatná — bez ní by se
    akce opakovaně spouštěla po celou dobu, kdy je přepínač držen, místo
    jednou na stisk.

  ![Řešený příklad](../assets/model-vars-calc-example.png)
