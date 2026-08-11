---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Pipeline pro snímky obrazovky

Každý snímek obrazovky v této příručce (aktuálně jich je ~590, ve složce
`docs/en/assets/`) byl zachycen skriptováním skutečného simulátoru Ethos, nikoli
ručně. Celá aparatura se nachází ve starém repozitáři
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), ve složce
`english/manual/`, a **dosud nebyla přenesena do tohoto repozitáře** — tato
stránka dokumentuje, jak funguje, aby to bylo možné provést a aby bylo mezitím
možné snímky obrazovky regenerovat nebo rozšiřovat bez nutnosti začínat od nuly.

## Jak je to strukturováno

Pro každou nabídku/sekci příručky existuje dvojice souborů:

- `manual/macros/<name>.lua` — skript napsaný proti Lua API simulátoru (viz
  níže), který přejde na konkrétní obrazovku a v každém bodě, který je vhodné
  zachytit, vyvolá `simulator.screenshot(path)`.
- `manual/<name>.sh` — jednořádkový wrapper, který spustí binárku simulátoru
  pro konkrétní vysílač s odkazem na dané makro, například:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` spustí postupně všechna makra a regeneruje tak celou
sadu. Jednotlivé soubory `.sh` existují pro každou sekci, takže snímky
obrazovky jedné stránky lze regenerovat bez opětovného spuštění všeho (každé
makro trvá od několika sekund po více než minutu).

Klíčové parametry příkazové řádky:

- `--read-only` — neuchovávat žádné změny provedené během běhu.
- `--no-gui` / `--no-audio` — téměř bezhlavý provoz; některá makra přesto
  potřebují GUI, protože simulátor bez něj „přeskakuje“ (viz komentář v
  `screenshots.sh`).
- `--radio-settings <file>.bin` — s uloženým nastavením kterého vysílače se má
  nastartovat (právě tím jsou snímky obrazovky specifické pro jazyk a vysílač —
  německý běh používá německý `.bin`).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — nasměrují simulátor na modely/firmware/dokumenty/zvuky,
  které má vidět, takže snímky obrazovky odrážejí záměrně připravený obsah, a ne
  to, co je náhodou na skutečné SD card.
- `--exec <script>.lua` — makro, které se má spustit po nastartování.

Každá rodina vysílačů (X20S, X20 Pro, X20 Pro AW, X18S) má vlastní binárku
simulátoru a potřebuje vlastní soubor `--radio-settings` pro každý jazyk (např.
`x20s-en.bin`, `x20pro-en.bin`), protože uživatelské rozhraní se mezi vysílači
mírně liší a soubor s nastavením zároveň nese jazyk.

## API pro makra

Makra jsou obyčejný Lua kód řídící globální objekt `simulator`:

| Volání | Účel |
|---|---|
| `simulator.loadModel("name.bin")` | Načte konkrétní soubor modelu před navigací — každá sekce příručky používá model nastavený tak, aby danou sekci demonstroval (viz seznam modelů níže). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Stisk hardwarové klávesy — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE` atd. Doba podržení vyvolá dlouhý stisk (otevře kontextové nabídky). |
| `simulator.turnRotaryEncoder(n)` | Otočí enkodérem o `n` kroků (negativní = opačný směr) — hlavní způsob přesouvání kurzoru mezi položkami. |
| `simulator.touch(x, y)` | Klepnutí na konkrétní souřadnici obrazovky — používá se tam, kde je dotyk jediným způsobem, jak se k něčemu dostat (např. přepnutí rozvržení klávesnice). |
| `simulator.setAnalog(channel, value)` | Nastaví přímo polohu páčky/potenciometru/posuvníku (`0`-`3` jsou čtyři hlavní páčky, `ANALOG_LAST_SLIDER` poslední posuvník), takže snímky obrazovky zobrazují záměrnou, reprodukovatelnou hodnotu, a ne to, co simulátor nastaví výchozím způsobem. |
| `simulator.setSwitch(n, position)` | Nastaví polohu fyzického přepínače. |
| `simulator.setDateTime({...})` | Pevně nastaví hodiny simulátoru, takže časové údaje na snímcích obrazovky (a vše závislé na čase) jsou reprodukovatelné mezi jednotlivými běhy. |
| `simulator.screenshot(path)` | Zachytí aktuální obrazovku do PNG, relativně k pracovnímu adresáři makra (proto ty cesty `../assets/...` uvnitř každého makra). |
| `simulator.connectUsb()` | Simuluje připojení k USB, pro zachycení nabídky USB. |
| `simulator.sleep(seconds)` | Čeká, než se animace/telemetrická hodnota ustálí, teprve pak se zachytí snímek. |

Soubor `manual/macros/common.lua` je pomocí `dofile` vkládán do většiny maker a
pouze pevně nastavuje datum a čas, takže každé makro začíná ve stejném
simulovaném okamžiku.

## Modely použité v jednotlivých sekcích

`manual/notes.txt` (převzato neformálně, dosud nezkopírováno do tohoto
repozitáře) mapuje každé makro na soubor modelu `.bin`, na kterém závisí, a
vysvětluje proč — např. `model-mixes.lua` používá `rarebear.bin`,
`model-fm.lua` používá `zblank.bin` (model se záměrně prázdným nastavením
letových režimů), `model-trims.lua` používá `blaster.bin` (nastavený s
posunutými trimy pro demonstraci rozsahu trimu). Přenos poznámek z tohoto
souboru do řádné dokumentace zde je součástí práce ve fázi 2 níže.

## Co obnáší přenesení do nového repozitáře (dosud neprovedeno)

- Rozhodnout, zda se makra budou spouštět přímo z tohoto repozitáře (což
  vyžaduje lokální instalaci simulátoru Ethos, jako to bylo ve starém
  repozitáři), nebo přes CI se simulátorem přiloženým/stahovaným v rámci
  workflow.
- Restrukturalizovat plochou výstupní cestu `../assets/...` tak, aby odpovídala
  rozvržení assetů tohoto repozitáře podle stránky a jazyka
  (`docs/<locale>/assets/`).
- Jeden soubor `--radio-settings ... .bin` a jeden běh generování snímků
  obrazovky pro každý jazyk, jakmile bude existovat jiný jazyk než `en` —
  snímky obrazovky jsou specifické pro jazyk uživatelského rozhraní a nelze je
  mezi jazyky sdílet.
- Rozhodnout, jakou část z ~40 existujících maker převzít tak, jak jsou, a
  jakou přepsat proti současné struktuře navigace v tomto repozitáři (některá
  makra vytvářejí snímky obrazovky pro sekce, které již neodpovídají 1:1
  rozvržení stránek této příručky).
