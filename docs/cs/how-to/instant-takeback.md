---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Okamžité převzetí řízení pro funkci Trainer

Užitečné rozšíření funkce [Trainer](../model-setup/trainer.md): místo pouhého přepínače může instruktor převzít řízení okamžitě jen pohybem páčky křidélek nebo výškovky — pokud se něco pokazí, není nutné nejprve hledat přepínač trainer.

Přepínač trainer stále zahajuje výcvikovou relaci; samotnou funkci trainer řídí [Sticky logický přepínač](../model-setup/logical-switches.md#sticky), který se ruší buď vypnutím přepínače, **nebo** detekcí pohybu páčky instruktora.

![Trainer aktivní](../assets/trainer-take-back-trainer-active.png)

## 1. Logický přepínač pro detekci křidélek

![Detekce vstupu křidélek](../assets/trainer-take-back-ailinput.png)

Logický přepínač využívající **|A| > X** na páčce křidélek, pravdivý, když se páčka vychýlí o více než 10 % ze středu v kterémkoli směru. Dlouze stiskněte zdroj křidélek a zvolte **Ignore trainer input**, aby jej nespouštěl také pohyb křidélek *studenta* (přicházející přes spojení trainer):

![Ignorovat vstup trainer](../assets/trainer-take-back-ailinput-ignore.png)

## 2. Logický přepínač pro detekci výškovky

![Detekce vstupu výškovky](../assets/trainer-take-back-eleinput.png)

Stejný postup, ale na páčce výškovky.

## 3. Logický přepínač pro zrušení

Logický přepínač **OR**, pravdivý tehdy, když je pravdivý přepínač detekce křidélek nebo detekce výškovky, **nebo** když přepínač trainer (např. SD) není dole — tedy relaci ukončí kterákoli z podmínek „instruktor pohnul páčkou“ nebo „přepínač trainer byl vypnut“.

## 4. Sticky logický přepínač pro povolení funkce trainer

![Vypnutí funkce trainer](../assets/trainer-take-back-disable-trainer.png)

Logický přepínač typu **Sticky**: **Trigger ON** je přepínač trainer (SD dole), **Trigger OFF** je přepínač pro zrušení z kroku 3. Tento Sticky přepínač — pojmenujte jej `TrainerActive` — použijte jako podmínku aktivace funkce Trainer namísto samotného přepínače.

## 5. Zvuková signalizace

Přidejte [speciální funkce Play Audio](../model-setup/special-functions.md), které ohlásí, kdy se `TrainerActive` stane pravdivým a kdy se zruší, aby oba piloti dostali jasný zvukový signál o tom, kdy přesně dochází k předání řízení.
