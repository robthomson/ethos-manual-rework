---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Kontrola hardwaru](../assets/system-hardware-check-x20s.png)

Testování a kalibrace fyzických ovládacích prvků vysílače, definice typů přepínačů a mapování domovských kláves.

## Kontrola hardwaru {: #hardware-check }

Umožňuje vyzkoušet každý fyzický vstup, abyste si ověřili, že se všechny správně registrují.

![Kontrola hardwaru X20 Pro](../assets/system-hardware-check-x20pro.png)
![Kontrola hardwaru X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — kontroluje také dva aretované tlačítkové přepínače **K** a **L** na zadních nárameních a navíc trimy **T5**/**T6**.
- **X18** — kontroluje také přídavné trimy **T5**/**T6**.

## Kalibrace analogových prvků {: #analogs-calibration }

![Kalibrace analogových prvků](../assets/system-hardware-analogs-calibration.png)

Naučí vysílač, kde přesně leží střed a krajní polohy každého gimbalu, potenciometru a posuvníku. Při prvním spuštění se provede automaticky; zopakujte ji po výměně gimbalu, potenciometru nebo posuvníku.

## Kalibrace gyroskopu

![Kalibrace gyroskopu](../assets/system-hardware-gyro-calibration.png)

Kalibruje vestavěný gyroskop, aby vstupy založené na náklonu správně reagovaly na naklánění vysílače — poloha „vodorovně“ odpovídá tomu, jak vysílač běžně držíte. Také se provede automaticky při prvním spuštění.

## Filtr analogových prvků

Zapínatelný/vypínatelný ADC filtr pro páčky, ve výchozím stavu zapnutý — snižuje chvění v okolí středu páčky. Toto je **globální** nastavení; existuje ještě přepis filtru analogových prvků **pro jednotlivé modely** v části [Úprava modelu](../model-setup/model-edit.md).

## Nastavení potenciometrů/posuvníků {: #potssliders-settings }

Umožňuje přejmenovat potenciometry a posuvníky. **X20 Pro/R/RS** navíc podporuje dva přídavné potenciometry, **Ext1**/**Ext2**, obvykle používané pro třísosé gimbaly.

![Hodnoty ADC, potenciometry](../assets/system-hardware-pots-x20s.png)
![Hodnoty ADC, potenciometry (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Nastavení přepínačů {: #switches-settings }

![Přepínače](../assets/system-hardware-switches.png)

- **Prodleva detekce střední polohy přepínače** — zabraňuje tomu, aby rychlé přehození třípolohového přepínače nahoru→dolů (nebo dolů→nahoru) na okamžik zaregistrovalo střední polohu; střední poloha by se měla registrovat pouze tehdy, když se přepínač skutečně zastaví. Výchozí hodnota je 0 ms, zvolená s ohledem na detekci „self-check“ u stabilizovaných přijímačů FrSky na CH12.
- **Typ přepínače** — SA–SJ lze jednotlivě definovat jako **None**, **Momentary**, **2 POS** nebo **3 POS**, což umožňuje zaměnit funkčnost mezi fyzickými přepínači (např. přiřadit tlačítkovému přepínači SH roli, kterou obvykle zastává dvoupolohový SF) — v rámci možností, které skutečně dovoluje zapojení vysílače (třípolohovou roli obecně nelze přiřadit hardwaru, který pro ni není zapojen).

  ![Možnosti přepínačů](../assets/system-hardware-switches-options.png)
  ![Přídavné přepínače](../assets/system-hardware-switches-2.png)

- **Přejmenování** — přepínače lze z označení SA–SJ přejmenovat na vlastní názvy; názvy jsou globální pro všechny modely.
- **X20 Pro** — přidává tlačítkové přepínače **K**/**L** na zadních nárameních a dále polohy **M**/**N**, pokud jsou zapojeny (obvykle pro přepínače na koncích páček).

## Mapování domovských kláves

Umožňuje změnit, kam vedou domovské klávesy `SYS`, `MDL` a `DISP` (`TELE` u starších vysílačů).

- **`DISP`** — krátkému i dlouhému stisku lze přiřadit libovolnou stránku modelu, stránku systému, Konfiguraci obrazovek, Domů nebo Záznam letových dat. Pro konzistenci se sérií X10 se dlouhý stisk `DISP` obvykle nastavuje na Konfiguraci obrazovek.
- **`SYS`/`MDL`** — přiřaditelný je pouze dlouhý stisk (do stejné sady cílů); krátký stisk vždy otevře sekci Nastavení systému, resp. Nastavení modelu.

## Hardwarové možnosti specifické pro vysílač {: #radio-specific-hardware-options }

- **Aktivace haptických gimbalů** (X20 Pro, X20R) — X20 Pro AW a X20RS jsou dodávány s gimbaly MC20R, které obsahují haptické motory pro vibrace páček; pokud byly gimbaly MC20R dodatečně namontovány do X20 Pro nebo X20R, aktivujte je zde (nastavení samotných haptických vzorů viz [Speciální funkce](../model-setup/special-functions.md)).

  ![Haptika (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptika (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Možnosti enkodéru** (X20 Pro AW, X20R/RS) — tyto vysílače mají citlivější rotační enkodér; jeho citlivost lze zmírnit zapnutím **polovičních kroků**.

  ![Možnosti enkodéru (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Prohlížeč hodnot ADC {: #adc-value-inspector }

Zobrazuje surové hodnoty analogově-digitálního převodu, které procesor načítá pro každý analogový vstup:

![Kontrola ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Kontrola ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 levá páčka vodorovně, 2 levá páčka svisle, 3 pravá páčka svisle, 4 pravá páčka vodorovně, 5 Pot 1, 6 Pot 2, 7 prostřední posuvník, 8 levý posuvník, 9 pravý posuvník.

**X20 Pro**: jako výše, ale se dvěma přídavnými kanály externích potenciometrů (7 Ext1, 8 Ext2 — např. potenciometry na páčkách) vloženými před posuvníky, které se posouvají na 9 prostřední posuvník, 10 levý posuvník, 11 pravý posuvník.
