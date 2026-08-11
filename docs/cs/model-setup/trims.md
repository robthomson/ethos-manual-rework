---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trimy

![Trimy](../assets/model-trims.png)

Konfiguruje rozsah trimu, velikost kroku a chování pro každou páčku, dále
křížový trim a okamžitý trim. Vysílače **X20 Pro/R/RS** a **X18** navíc
mají dva doplňkové trimovací přepínače **T5**/**T6**, které se hodí pro
úpravy za letu nad rámec čtyř hlavních páček:

![Trimy T5/T6](../assets/model-trims-pro-t5-t6.png)

Každá páčka má vlastní nezávislou sadu nastavení trimu.

## Nastavení trimu {: #trim-settings }

- **Rozsah** — výchozí ±25 %, nastavitelný až na plných ±100 % rozsahu
  páčky. Na hlavním displeji se trim s výchozím rozsahem zobrazuje jako
  −100 až 100; trim s plným rozsahem (100 %) jako −400 až 400
  (4× normální rozsah).

  !!! warning
      Rozšíření rozsahu znamená, že příliš dlouhé držení trimovací
      páčky může přidat tolik trimu, že se model stane neletuschopným.

- **Krok** — granularita trimovacího přepínače: **Velmi jemný**,
  **Jemný**, **Střední**, **Hrubý**, **Exponenciální** (jemný v okolí
  středu, hrubší dále od něj) nebo **Vlastní** (konkrétní procento na
  jedno kliknutí).

  ![Možnosti kroku](../assets/model-trims-step-options.png)

  | Krok | µs na kliknutí (rozsah 25 %) |
  |---|---|
  | Velmi jemný | 0,5 |
  | Jemný | 1 |
  | Střední | 2 |
  | Hrubý | 4 |
  | Exponenciální | 0,3–16 |

  Vlastní, při rozsahu 25 %: krok 1 % = 1 µs/kliknutí, krok 100 % =
  128 µs/kliknutí. Při rozsahu 100 %: krok 1 % = 5 µs/kliknutí, krok
  100 % = 512 µs/kliknutí.

## Režim

![Režim trimu výškovky](../assets/model-trims-mode-elevator.png)

Ve výchozím stavu je trim vždy aktivní, ale volba **Režim** toto chování
mění. Změna režimu vynuluje trim na 0.

- **OFF** — trim se úplně vypne.

  ![Režim: off](../assets/model-trims-mode-option-off.png)

  Užitečné například u elektromodelu, kde není potřeba trim plynu — takto
  uvolněný trimovací ovladač lze pak [využít k nastavování
  proměnné](variables.md).

- **Easy** — jedna společná hodnota trimu pro všechny letové režimy.
  Obvyklá volba pro křidélka a směrovku, protože ty se podle letového
  režimu jen zřídka mění.

  ![Režim: easy](../assets/model-trims-mode-option-easy.png)

- **Nezávisle pro každý letový režim** — trim ovlivňuje pouze aktivní
  letový režim. Obvyklá volba pro trim výškovky, protože ten se běžně
  musí lišit podle letového režimu (např. při změnách profilu křídla) —
  ve skutečnosti to bývá hlavní důvod, proč letové režimy vůbec nastavovat.

  ![Režim: nezávislý na FM](../assets/model-trims-mode-option-fm.png)

- **Vlastní** — plně vlastní chování, sestavené z **chování**, která si
  přidáte sami.

### Vlastní chování trimu

![Přidání chování](../assets/model-trims-mode-elevator-add-behaviour.png)
![Možnosti chování](../assets/model-trims-mode-elevator-edit-behaviour.png)

Každý řádek chování má podmínku a jednu z těchto možností:

- **Odpojeno** — vypne trim selektivně za dané podmínky (namísto úplného
  vypnutí pomocí Režim = OFF).

  ![Odpojeno](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Podmínka odpojení](../assets/model-trims-mode-unplugged-select.png)

- **Normální** (výchozí) — běžné chování trimu.
- **Rovno (jinému trimu)** — tento trim přesně kopíruje hodnotu trimu
  jiné podmínky.

  ![Rovno](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Offset + (jiný trim)** — tento trim se přičítá k hodnotě trimu jiné
  podmínky.

  ![Offset](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Praktický příklad** — větroň se základním trimem výškovky v režimu
**Cruise** a závislými trimy pro režimy **Speed** a **Thermal**:

![Volba FM5 Speed](../assets/model-trims-mode-elevator-custom-select.png)
![Volba FM4 Thermal](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Vytrimujte model na vodorovný let ve výchozím režimu (Cruise).
2. Přidejte chování: **Offset + Default** s podmínkou `FM5(Speed)`. Nyní
   se každá úprava trimu provedená v režimu Speed uloží jako offset nad
   základní hodnotou režimu Cruise — samostatně, ale stále na ní závisle.

   ![Offset pro Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Stejným způsobem přidejte druhé chování: **Offset + Default** s
   podmínkou `FM4(Thermal)`. (Jakmile existuje první chování, nabídne
   dialog také možnosti `Equal FM5(Speed)` a `Offset + FM5(Thermal)`,
   protože se nyní může odkazovat i na toto chování.)

   ![Offset pro Speed a Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Při tomto nastavení pozdější úprava základního trimu režimu Cruise
(řekněme po změně těžiště) automaticky posune trimy režimů Speed a
Thermal o stejnou hodnotu, protože jsou to offsety nad ním, a nikoli
nezávislé hodnoty.

- **Audio** — vypne standardní hlášení trimu u trimu, který byl použit
  k jinému účelu a jeho hlášení už nemá smysl.

## Doplňkové trimy

![Přidání doplňkového trimu](../assets/model-trims-add-trim-select.png)
![Nastavení doplňkového trimu](../assets/model-trims-add-trim-edit.png)

Volba **Přidat další trim** vytvoří trim nad rámec čtyř standardních
páček (a T5/T6): **Název**, zdroje **Nahoru**/**Dolů** pro jeho ovládání
a dále stejné možnosti **Rozsah**, **Krok**, **Režim** a **Audio** jako
výše.

## Křížový trim

![Křížový trim](../assets/model-trims-cross.png)
![Úprava křížového trimu](../assets/model-trims-cross-edit.png)

Určuje, který trimovací přepínač skutečně nastavuje danou páčku — tedy
umožňuje, aby byl trim páčky ovládán jiným fyzickým trimovacím ovladačem
než obvykle. (T5/T6 jsou dostupné pouze u X20 Pro a X18.)

## Okamžitý trim {: #instant-trim }

![Okamžitý trim](../assets/model-trims-instant-trim.png)

Dokud je aktivní, přičítá aktuální polohy páček do odpovídajících
výchozích (a křížových) trimů. Nejlépe jej přiřaďte přepínači, na který
dosáhnete bez pouštění páček — spusťte jej během přímého vodorovného
letu a trimy se nastaví okamžitě, místo opakovaného klikání trimovací
páčkou, když jsou trimy značně mimo. Po trimovacím letu jej opět
vypněte, aby nedošlo k nechtěnému rozhození trimů.

!!! note
    Okamžitý trim je aktivní pouze při zobrazení jednoho z hlavních
    zobrazení.

## Přesun trimů do subtrimů

![Přesun trimů do subtrimů](../assets/model-trims-move-trims-to-subtrims.png)

Po vytrimování na vodorovný let přesune hodnotu trimu kanálu (např.
výškovky) do jeho nastavení [Subtrim](outputs.md) a trim na obrazovce
vynuluje — čistý způsob, jak později ověřit, že se letové trimy
neposunuly.

Pokud jsou ve hře letové režimy, může mít kanál více relevantních hodnot
trimu, zatímco Subtrim ve Výstupech je jediné globální nastavení platné
pro všechny letové režimy. Tato funkce s tím počítá: vezme trim
**právě zvoleného** letového režimu, přesune jej do Subtrimu, tento trim
vynuluje a trimy *všech ostatních* letových režimů na stejném kanálu
odpovídajícím způsobem upraví — takže skutečná poloha plochy zůstane
v každém letovém režimu celkově nezměněna.

!!! tip
    Pro konzistenci tuto funkci vždy spouštějte ze stejného „základního“
    letového režimu (např. Cruise u větroně) — pak ji lze bezpečně
    opakovat.

Velké hodnoty trimu nebo subtrimu vytvářejí velmi asymetrické výchylky —
lepší je odstranit příčinu mechanicky. Snažte se, aby byly tahové páky
v 90° při neutrální poloze ploch (výjimkou jsou klapky, kde vyměníte část
výchylky nahoru za větší výchylku dolů), a jakmile je mechanika blízko,
dolaďte pomocí **PWM center** přesně na 90°.
