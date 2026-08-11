---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Křivky

![Typy křivek](../assets/model-curves-type.png)

Opakovaně použitelné křivky odezvy pro [Mixy](mixes.md#anatomy-of-a-mix) nebo
[Výstupy](outputs.md#editing-a-channel) — vestavěné Expo je dostupné
přímo v obou, ale cokoli složitějšího se definuje zde (nebo pomocí
**Add curve**, dostupného přímo z obou editačních obrazovek). K dispozici
je až 50 křivek; ve výchozím stavu žádná neexistuje (Expo je vždy
vestavěné bez ohledu na to). Novou přidáte pomocí **+**; klepnutím na
existující křivku získáte volby
**Edit**/**Move**/**Copy-paste**/**Clone**/**Delete**.

![Přidání křivky](../assets/model-curves-add.png)

## Typy křivek

- **Expo** — výchozí hodnota 40; kladná hodnota zjemňuje odezvu okolo
  středu, záporná ji zostřuje. Zjemnění okolo středu páčky pomáhá
  předcházet přeřízení modelu, zvláště u méně zkušených pilotů.

  ![Expo](../assets/model-curves-expo.png)

- **Function** — malá sada pevných matematických tvarů:

  ![Typy funkcí](../assets/model-curves-fn-types.png)

  - **x > 0** — propouští zdroj nezměněný, dokud je kladný; při
    záporných hodnotách vydává 0.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — zrcadlová varianta: propouští při záporných hodnotách,
    0 při kladných.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — propouští zdroj jako jeho absolutní hodnotu (vždy
    kladnou).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — vydává 100 %, pokud je zdroj kladný, a 0, pokud je
    záporný (tvrdý přepínač, nikoli propouštění).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — vydává −100 % při záporných hodnotách a 0 při kladných.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — vydává −100 % při záporných hodnotách a +100 % při
    kladných.

    ![|f|](../assets/model-curves-fn-barf.png)

  Každý typ křivky — včetně Function — má také **Offset**, který ji
  posouvá nahoru nebo dolů po ose Y (s přesností na jedno desetinné
  místo, stejně jako obecně u hodnot Y):

  ![Offset funkce](../assets/model-curves-fn-xgt0-offset.png)

- **Custom** — křivka založená na bodech, ve výchozím stavu 5 bodů, až 21.

  ![Vlastní pětibodová křivka](../assets/model-curves-custom5.png)

  - **Smooth** — vede skrz všechny body plynulou křivku místo přímých
    úseků mezi nimi.

    ![Vyhlazená křivka](../assets/model-curves-custom5-2-smooth.png)

  - **Easy mode** — **On** omezuje editaci pouze na rovnoměrně rozložené
    souřadnice Y (X je pevné); **Off** umožňuje u každého bodu editovat
    X i Y, s výjimkou krajních bodů −100 %/+100 %, které jsou uzamčené,
    protože křivka musí vždy pokrývat celý rozsah signálu.

    ![Easy mode vypnutý](../assets/model-curves-custom-easy-off.png)

  **Ovládací prvky editoru** (stejný princip jako [editor vyvažovací
  křivky ve Výstupech](outputs.md#balance-channels)):

  - **Source** — ve výchozím stavu vlastní zdroj(e) mixu dané křivky,
    nebo **Auto analog input** pro zachycení první pohnuté
    páčky/posuvníku/potenciometru.
  - Přichytávání k nejbližšímu bodu pomocí otočného enkodéru a přepínač
    **Lock** pro zmrazení vstupů při sledování výsledného pohybu kormidla.
  - Živý kurzor zobrazuje aktuální vstupní hodnotu, která křivku řídí,
    aby bylo možné ji před úpravou zarovnat s bodem.

## Řízení křivky z Var

Jak **Offset** křivky typu Function, tak jednotlivý bod křivky **Custom**
mohou být místo pevné hodnoty řízeny pomocí [Var](variables.md) — a tuto
Var lze následně upravovat za letu prostřednictvím přeřazeného trimu:

![Offset funkce z Var](../assets/model-curves-fn-offset-var.png)
![Bod vlastní křivky z Var](../assets/model-curves-custom-with-var.png)

Kompletní propracovaný příklad tohoto postupu najdete v kapitolách
[Proměnné](variables.md) a [Praktický návod: Kompenzační křivka
nastavitelná za letu](../how-to/in-flight-compensation-curve.md).
