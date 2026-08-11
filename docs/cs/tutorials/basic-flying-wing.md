---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Základní příklad samokřídla (elevony)

Samokřídlo s elevony ovládanými 2 servy, na němž jsou jako konkrétní
propočtený příklad použity doporučené hodnoty rates/Expo/mixovacích
poměrů z modelu Dreamflight Weasel. Nejprve dokončete [Prvotní nastavení
vysílače](initial-radio-setup.md).

## Krok 1. Zkontrolujte nastavení systému {: #step-1-confirm-system-settings }

Výchozí pořadí **AETR**, s volbou **[Prvních čtyři kanály
pevně](../system-setup/controls.md#first-four-channels-fixed)** nastavenou
na **OFF**. Před pokračováním přijímač zaregistrujte (pokud jde o ACCESS)
a spárujte pomocí [RF systému](../model-setup/rf-system.md).

## Krok 2. Určete potřebná serva/kanály

U konstrukce s elevony [mixy](../model-setup/mixes.md) kombinují vstup
křidélek a výškovky na obě fyzické plochy — celkem tedy jen 2 kanály, z
nichž každý je směsí obou vstupů.

## Krok 3. Vytvořte nový model

![Vytvoření modelu letadla](../assets/tut-wing-eg-wiz-create-airplane.png)

Ve [Výběru modelu](../model-setup/model-select.md) spusťte průvodce
**Airplane** a zvolte **Non stabilized receiver**.

![Bez motoru](../assets/tut-wing-eg-wiz-no-engine.png)

Vyberte **No engine**, ponechte výchozí 2 kanály křidélek a zvolte **No
flaps**.

![Bez ocasních ploch](../assets/tut-wing-eg-wiz-no-tail.png)

Jako typ ocasních ploch zvolte **None** — právě to způsobí, že Ethos
automaticky vytvoří mix pro elevony (vstupy křidélek + výškovky, oba na
tytéž dva kanály). Pojmenujte model (např. „Weasel“), vyberte obrázek a
dokončete průvodce — model se stane aktivním v kategorii Airplane.

## Krok 4. Zkontrolujte a nastavte mixy

![Přehled mixů](../assets/tut-wing-eg-mixes.png)

Průvodce vytvoří mix Křidélka na kanálech 1+2 a za ním mix Výškovka
*rovněž* na kanálech 1+2 — oba vstupy působí na oba kanály elevonů, což
je celý princip mixování elevonů.

### Křidélka

![Mix křidélek](../assets/tut-wing-eg-mixes-ail-mix.png)

**Weight/Rates** — podle manuálu modelu Weasel by výchylka křidélek měla
být přibližně 3× větší než výchylka výškovky a součet obou by měl být
100 %: **75 %** křidélka, **25 %** výškovka. Nízké rates jsou asi
poloviční proti vysokým: **36 %** křidélka nízké, **12 %** výškovka
nízká.

![Weight mixu křidélek](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — pro Weasel doporučeno 35 % vysoké / 20 % nízké, aktivní při
přepínači SB dole, což zplošťuje odezvu v okolí středu páčky.

**Diferenciál** — u této konstrukce malý, přibližně **4 %**:

![Diferenciál křidélek](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Vysvětlení, proč je diferenciál důležitý, najdete v [Základním příkladu
modelu s pevným křídlem](basic-fixed-wing.md#ailerons) — uplatňuje se
zde stejná úvaha o negativním vybočení.)

### Výškovka

![Mix výškovky](../assets/tut-wing-eg-mixes-ele-mix.png)

Stejný postup: **25 %**/**12 %** vysoké/nízké rates, stejné hodnoty Expo
jako u křidélek.

### Směrovka

![Mix směrovky](../assets/tut-wing-eg-mixes-rud-mix.png)

Weasel žádnou nemá — samokřídla ji obvykle nepotřebují. Pokud je na
modelu s elevony směrovka *přece jen* potřeba, přidejte ji jako [Volný
mix](../model-setup/mixes.md#mix-libraries) na kanálu 3.

## Krok 5. Spárujte přijímač

Stejně jako v [Kroku 1](#step-1-confirm-system-settings) — před dalším
postupem přijímač zaregistrujte/spárujte a zvažte odpojení servopák nebo
omezení dráhy, dokud nejsou nastaveny limity Min/Max, abyste nic
nepřetěžovali.

## Krok 6. Zkontrolujte mixy

Výstupní kanály 1/2 lze přejmenovat na **Elevon1**/**Elevon2**. Při plné
výchylce křidélek vpravo kanál 1 (pravý, jdoucí nahoru) ukazuje 75 %,
zatímco kanál 2 (levý, jdoucí dolů) ukazuje 72 % — tento 3% rozdíl *je*
projev diferenciálu. Přidejte k tomu plnou výchylku výškovky dolů a kanál
1 se stane 75+25 = 100 %, kanál 2 pak 72−25 = 47 %.

## Krok 7. Nastavte maximální výchylky serv

![Plná výchylka křidélek](../assets/tut-wing-eg-outputs-full-ail.png)
![Plná výchylka křidélek + plná výchylka výškovky](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Nejprve každé servo vystřeďte pomocí **PWM center**. Doporučená maximální
výchylka modelu Weasel je 25 mm křidélka + 10 mm výškovka = 35 mm
souhrnně — zadejte plné souhlasné *i* plné protichůdné vstupy křidélek a
výškovky a před nastavením konečných výchylek se ujistěte, že žádná z
nich nepřekračuje mechanické limity ani limity serv.

- **Min/Max** — pevné limity, které nelze nikdy překročit; jejich
  zmenšení zmenší výchylku, místo aby signál omezovalo. Výchozí ±100 %,
  v případě potřeby rozšiřitelné na ±150 %.
- **Curve** — často rychlejší a pružnější než přímé žonglování s
  Min/Max/Subtrim, navíc s výhodou živého grafu. Většině výstupů
  postačuje 3bodová křivka; 5bodová křivka na druhém elevonu umožňuje
  snadno sladit dráhu v 5 bodech s prvním elevonem. Pokud k tomu použijete
  křivku, ponechte Min/Max/Subtrim na hodnotách bez vlivu (−100/100/0
  nebo −150/150/0 při rozšířených limitech) a tvarování přenechte křivce.
