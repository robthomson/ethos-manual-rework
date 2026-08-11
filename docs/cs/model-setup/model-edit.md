---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Úprava modelu

![Úprava modelu](../assets/model-editmodel.png)

Umožňuje upravit parametry na úrovni modelu, které původně nastavil průvodce —
především identitu modelu, ale také několik nastavení platných pro jednotlivý
model a pomocné funkce.

## Název, obrázek

Přejmenování modelu nebo změna jeho obrázku; při procházení obrázků se
zobrazuje náhledová miniatura.

## Typ modelu

![Typ modelu](../assets/model-edit-modeltype.png)

!!! warning
    Změna typu modelu resetuje **všechny** mixy.

## Přiřazení kanálů

Změna typu ocasních ploch nebo (u vrtulníku) typu cykliky rovněž resetuje
všechny mixy. U ostatních kanálů lze změnit počet přiřazených kanálů nebo
je zrušit.

## Filtr analogových prvků

![Filtr analogových prvků](../assets/model-edit-analog-filter.png)

V [Nastavení systému → Hardware](../system-setup/hardware.md) je globální
analogově-digitální filtr, který může snížit rozechvění v okolí středu páčky;
toto nastavení na úrovni modelu jej přepíše pouze pro tento model.

![Možnosti filtru analogových prvků](../assets/model-edit-analog-filter-select.png)

## Funkční přepínače {: #function-switches }

![Funkční přepínače](../assets/model-edit-fn-switches.png)

Šest funkčních přepínačů je k dispozici všude, kde se vyskytuje parametr
**Aktivační podmínka**, ale — na rozdíl od běžných přepínačů — je nelze použít
jako univerzální zdroj. Konfigurují se jedním z těchto způsobů:

- **6-pol. s OFF** — stisknutí funkčního přepínače jej zapne a zaaretuje;
  opětovné stisknutí *téhož* přepínače vypne všech šest.
- **6-POS** — stisknutí funkčního přepínače jej zaaretuje v zapnutém stavu,
  dokud není stisknut *jiný*, který jej převezme.
- **2 × 3-pol.** — rozdělí šest přepínačů do dvou skupin po třech, v každé
  skupině je aktivní jeden přepínač.
- **6 × 2-pol.** — šest nezávislých aretovaných přepínačů zap/vyp.
- **Momentové** — šest nezávislých přepínačů, každý je zapnutý pouze po dobu
  stisknutí.
- **Trvalé** — je-li zapnuto, funkční přepínač si zachová svůj stav i po
  vypnutí vysílače / znovunahrání modelu, místo aby se resetoval.

![Možnosti funkčních přepínačů](../assets/model-edit-fn-switches-select.png)

## Konektor SPort

Pin 5 V na konektoru S.Port vysílače lze přepínat pro každý model zvlášť —
což je užitečné například pro napájení externího přijímače při zapojení
učitel/žák.

## Doba provozu modelu

![Doba provozu modelu](../assets/model-edit-model-runtime.png)

Sleduje celkovou dobu, po kterou byl tento model provozován / létán.

## Resetovat všechny mixy

![Resetovat všechny mixy](../assets/model-edit-model-reset_all_mixes.png)

Resetuje všechny mixy modelu do jejich výchozího stavu.
