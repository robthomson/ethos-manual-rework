---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Verzování

Ethos dnes vydává firmware pod čísly verzí (1.6.x) a naznačil přechod
k označení podle roku (např. „Ethos26"). Tento manuál musí udržovat
dokumentaci starých verzí dostupnou a správnou, zatímco se aktivně píše
dokumentace nových verzí — a tato stránka popisuje, jak.

## Jak to funguje

Verzování zajišťuje [mike](https://github.com/jimporter/mike), nástroj,
který doporučuje samo Material for MkDocs. `.github/workflows/deploy.yml`
spouští `mike deploy` místo publikování přímo do korene `gh-pages`:
každá verze se sestaví a commitne do vlastního podadresáře (`/1.6/`,
`/26/`, …) a `manual.rt-rc.com/` přesměrovává na tu verzi, která právě
drží alias `latest`. Material automaticky zobrazí rozbalovací nabídku pro
výběr verze, načtenou z `versions.json` (spravovaného nástrojem `mike`)
— to nijak nesouvisí s přepínačem jazyků a čistě se s ním skládá:
verze je vnější segment cesty, jazyk (jakmile bude existovat víc než `en`)
vnitřní, např. `manual.rt-rc.com/26/fr/...`.

Využívá se zde stejný mechanismus „podadresáře na `gh-pages`" jako
u [náhledů PR](index.md#pr-previews) — adresáře verzí nástroje `mike`
a adresář `pr-preview/` koexistují ve stejné branchi bez konfliktů,
protože každý se vždy dotýká jen svých vlastních cest.

## Rozvržení zdrojů: `main` + zmrazené branche

- **`main` vždy odpovídá obsahu aktuální/nejnovější verze firmwaru.**
  Každodenní editace probíhá zde přesně tak jako dnes — na běžném
  workflow pro přispívání se nic nemění.
- Jakmile se manuál nové verze firmwaru začne odchylovat od toho, co je
  v `main`, **nejprve vytvořte branch pojmenovanou podle staré verze**,
  např. `1.6`, a tím ji trvale zmrazte. `main` se pak stává obsahem
  nové verze.
- Zmrazená branch není mrtvá — stále může přijímat opravy prostřednictvím
  vlastních PR. Jen už nesleduje vývoj nové verze.

## Vytvoření nové verze

Když má začít manuál pro další verzi (např. Ethos26):

1. Z `main` vytvořte a odešlete zmrazenou branch pro verzi, kterou
   opouštíte:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   Kopie souboru `.github/workflows/deploy.yml` v branchi `1.6` nyní při
   každém pushi do této branche trvale nasazuje
   `mike deploy --push --update-aliases 1.6 latest` — je to takto správně
   a není nutná žádná úprava, protože branch je úplný snapshot včetně
   vlastní konfigurace CI.

2. V `main` upravte `.github/workflows/deploy.yml`: změňte řetězec verze
   v kroku `Deploy version 1.6 with mike` (a v jeho názvu) z
   `1.6` na označení nové verze (např. `26`). To je **jediná** nutná
   úprava pro zahájení nasazování nové verze — další push do `main`
   ji publikuje do `/26/` a přesune tam alias `latest`,
   zatímco `/1.6/` zůstane přesně tak, jak bylo.

3. Aktualizujte v `main` obsah nové verze podle toho, co se skutečně
   změnilo — nové či přejmenované sekce nabídek, nové snímky obrazovek,
   aktualizovaná terminologie. Sekce `nav` v `mkdocs.yml` se mezi
   branchemi může libovolně lišit; není zde žádná společná konfigurace,
   kterou by bylo nutné udržovat synchronizovanou.

4. Přidejte název nové branche do seznamu spouštěčů `branches:`
   v `.github/workflows/pr-preview.yml`, pokud mají i PR proti ní
   dostávat živé náhledy (zmrazené branche to obvykle nepotřebují,
   protože přijímají jen občasné opravné PR).

## Snímky obrazovek napříč verzemi

Snímky obrazovek se zachycují z konkrétního buildu Ethos (viz
[Pipeline pro snímky obrazovek](screenshot-pipeline.md)) a patří k té
branchi, jejíž uživatelské rozhraní zobrazují — vytvoření nové verze
přirozeně rozdělí i sadu snímků společně se vším ostatním, takže
`1.6/assets/` a (jakmile budou pro nové rozhraní znovu vygenerovány)
`docs/en/assets/` v `main` se po bodu rozdělení vyvíjejí nezávisle.
