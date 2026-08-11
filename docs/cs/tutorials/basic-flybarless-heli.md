---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Základní příklad nastavení flybarless helikoptéry

Základní nastavení flybarless (FBL) helikoptéry, na příkladu řídicí
jednotky typu Spirit. Na rozdíl od modelu s pevným křídlem je
helikoptéra vnitřně nestabilní — FBL jednotka používá gyroskopy (rychlost
otáčení) a akcelerometry (pohyb/orientaci) k výpočtu korekcí v osách
yaw/pitch/roll pomocí naladěné regulační smyčky PID
(Proporcionální-Integrační-Derivační), která vyvažuje stabilitu,
reakčnost a překmit podle konkrétních fyzikálních a elektrických
vlastností dané helikoptéry.

Tento návod se zabývá pouze **programováním vysílače** — ostatní najdete
v dokumentaci vaší FBL jednotky a předpokládá se, že již máte solidní
obecné znalosti o helikoptérách.

!!! danger
    Z bezpečnostních důvodů před začátkem demontujte rotorové listy.

## Krok 1. Zkontrolujte nastavení systému

Pořadí kanálů **AETR**, **[První čtyři kanály
pevně](../system-setup/controls.md#first-four-channels-fixed)** **OFF**
— FBL jednotky Spirit očekávají kanály SBUS právě v tomto pořadí
(přestože ve své vlastní konfiguraci interně používají TAER).
Zaregistrujte (v případě ACCESS) a spárujte přijímač pomocí [RF
System](../model-setup/rf-system.md).

## Krok 2. Určete potřebná serva/kanály

| Funkce | Kanál |
|---|---|
| Roll (křidélka) | — |
| Pitch (výškovka) | — |
| Plyn | — |
| Yaw (směrovka) | — |
| Zesílení gyra | 5 |
| Kolektiv (Collective Pitch) | 6 |
| Banka nastavení | 7 |
| Rescue | 8 |

## Krok 3. Vytvořte nový model

![Vytvoření modelu helikoptéry](../assets/tut-heli-eg-wiz-create-heli.png)

Ve [Výběru modelu](../model-setup/model-select.md) vytvořte/vyberte
kategorii Heli, spusťte průvodce a zvolte **Flybarless**:

![Volba FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Název modelu](../assets/tut-heli-eg-wiz-name.png)

Pojmenujte model a vyberte obrázek.

## Krok 4. Zkontrolujte a nastavte mixy

![Přehled mixů](../assets/tut-heli-eg-mixes.png)

Průvodce vytvoří Křidélka/Výškovku/Plyn/Směrovku v pořadí AETR, Pitch na
kanálu 6 a FBL Bank na kanálu 7:

![Mix Pitch](../assets/tut-heli-eg-mixes-pitch.png)

Zkontrolujte, že kanál 6 je Collective Pitch. Další dva kanály je nutné
přidat ručně jako [volné mixy](../model-setup/mixes.md#mix-libraries):
**Gyro Gain** (kanál 5) a **Rescue/Stabi** (kanál 8).

**Křidélka/Výškovka/Směrovka** — není co přidávat; rates a Expo jsou
záležitostí FBL jednotky, takže vysílač jen předává čistý lineární
signál.

![Mix křidélek](../assets/tut-heli-eg-mixes-ail.png)

**Collective Pitch** — přímá lineární křivka; jen zkontrolujte výstupní
kanál (obvykle 6). Jak bylo uvedeno výše, rates/Expo řeší FBL jednotka,
nikoli vysílač.

**FBL Bank** — tři banky nastavení jednotky Spirit (různé letové styly,
zesílení senzorů pro různé otáčky nebo Beginner/Acro/3D — případně jen
předvolby ladění) přiřazené třípolohovému přepínači, např. SE:

![Mix banky](../assets/tut-heli-eg-mixes-bank.png)

**Gyro Gain** — přidejte jako volný mix za poslední kanál. Zesílení má
obvykle pevnou hodnotu: nastavte **Zdroj** na Special Value 0, hodnotu
zesílení nastavte pomocí **Offsetu** (doladíte později za letu) a
výstupem bude kanál 5:

![Mix zesílení gyra](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Nastavení letových režimů

![Letové režimy](../assets/tut-heli-eg-flight-modes.png)

Tři [letové režimy](../model-setup/flight-modes.md): výchozí přejmenujte
na **Normal** a přidejte **Idle Up 1**/**Idle Up 2** na přepínači SD.

### Nastavení mixu plynu

Tři křivky plynu, jedna pro každý letový režim, každá jako [vlastní
křivka](../model-setup/curves.md):

- **Normal** — rozběh/vzlet: začíná na −100 % (motor vypnutý) a plynule
  stoupá. Dobře funguje 7bodová křivka se zapnutým **Smooth**; přesné
  hodnoty je nutné doladit za letu.

  ![Křivka Normal](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1** — běžné létání: přímková křivka pro konstantní nastavení
  plynu držící stálé otáčky rotoru, přičemž pohyb zajišťuje Collective
  Pitch, křidélka (roll) a výškovka (pitch). Přechod z režimu Normal
  udržte plynulý — bez velkého skoku. (Většina FBL jednotek nabízí také
  funkci **Governor** pro udržení konstantních otáček rotoru i při
  agresivních manévrech — viz manuál dané FBL jednotky.)

  ![Křivka Idle Up 1](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2** — agresivní létání (akrobacie, 3D); opět se ladí za
  letu.

  ![Křivka Idle Up 2](../assets/tut-heli-eg-curves-iup2.png)

![Křivky plynu v mixech](../assets/tut-heli-eg-mixes-thr-curves.png)

**Vypnutí plynu** — přiřaďte např. přepínač SG-up se zapnutým
**Sticky**: přepnutím SG nahoru se plyn okamžitě vypne a (kvůli funkci
Sticky) jej lze znovu aktivovat pouze tehdy, když je páčka plynu opět
dole/vypnutá.

![Vypnutí plynu](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescue/Stabi** — přiřaďte podobně, např. přepínači SA na kanálu 8.

![Výsledné mixy](../assets/tut-heli-eg-mixes-final.png)

## Krok 5. Nastavení FBL jednotky

1. **Nainstalujte konfigurační nástroj FBL jednotky** — např. Spirit
   Settings, na PC.
2. **Připojte přijímač k FBL jednotce** podle jejího schématu zapojení —
   typicky výstup SBUS Out přijímače do portu RUD FBL jednotky (některé
   modely Spirit vyžadují adaptér SBUS), případně pomocí F.Port1/FBUS.
3. **Připojte FBL jednotku k PC** — kabelem nebo přes Bluetooth, podle
   jejího manuálu.

   !!! danger
       Zatím nepřipojujte žádná serva.

4. **Aktualizujte firmware FBL jednotky**, je-li to potřeba, na kartě
   Update v nástroji.
5. **Obecné nastavení** (karta General v Spirit Settings):
   - Typ přijímače: **Futaba SBUS** nebo **FrSky F.Port** podle potřeby,
     poté restartujte.
   - Mapování kanálů (s pořadím AETR z průvodce):

     | Funkce | Kanál |
     |---|---|
     | Plyn | 1 |
     | Křidélka | 2 |
     | Výškovka | 3 |
     | Směrovka | 4 |
     | Gyro | 5 |
     | Pitch | 6 |
     | Bank | 7 |
     | Rescue/Stabi | 8 |

     (Toto mapování vyplývá ze způsobu, jakým jednotka Spirit
     interpretuje pozice v datovém toku SBUS.)

6. **Limity kanálů** (karta Diagnostic) — FBL jednotka potřebuje
   zkalibrované limity kanálů vysílače a ověřené středy:

   - Nejprve na vysílači vynulujte všechny subtrimy a trimy.
   - Vystřeďte páčku Collective Pitch tak, aby ve
     [Výstupech](../model-setup/outputs.md) ukazovala přesně 1500 µs.
   - Zapněte FBL jednotku a zkontrolujte, že
     křidélka/výškovka/pitch/směrovka ukazují na kartě Diagnostic 0 %
     (FBL jednotka detekuje neutrál automaticky při každé inicializaci).
   - Vychylte každý ovládací prvek do krajních poloh a upravujte
     odpovídající **Min**/**Max** ve Výstupech, dokud karta Diagnostic
     neukazuje přesně +100 %/−100 %; zároveň zkontrolujte, že směr
     ukazatele odpovídá směru výchylky páčky.

   !!! warning
       U těchto kanálů nikdy nepoužívejte subtrim ani trim — FBL
       jednotka Spirit je vyhodnocuje jako vstupní příkazy, nikoli jako
       kalibraci.

7. Upravte **Offset** mixu Gyro Gain tak, abyste dosáhli režimu Heading
   Lock.

Tímto je strana vysílače plně nastavena — pokračujte zbytkem nastavení
podle manuálu vaší FBL jednotky.
