---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Základní struktura widgetu

Vlastní Lua widget (instalaci popisuje [Vlastní widgety](../displays/custom-widgets.md))
se skládá z malé sady pojmenovaných polí a obslužných funkcí:

- **`key`** *(řetězec)* — jednoznačný identifikátor widgetu.
- **`name`** *(řetězec nebo funkce)* — zobrazovaný název widgetu. Buď
  jednoduchý řetězec, nebo funkce bez argumentů, která název vrací —
  což je užitečné u názvu, který se mění podle jazyka.
- **`create`** *(funkce)* — vyvolána jednou při vytvoření widgetu, bez
  argumentů. Vrací **tabulku widgetu**, která je pak předávána všem
  ostatním níže uvedeným obslužným funkcím — zde inicializujte svůj stav
  a uložte jej do této tabulky.
- **`configure`** *(funkce)* — vyvolána, když uživatel otevře konfigurační
  obrazovku widgetu; jejím jediným argumentem je tabulka widgetu
  z `create()` a nic nevrací. Zde sestavte konfigurační formulář a použijte
  jej k aktualizaci hodnot v tabulce widgetu.
- **`wakeup`** *(funkce)* — vyvolána v každé smyčce (přibližně každých
  50 ms), s tabulkou widgetu jako argumentem, nic nevrací. Zde zkontrolujte,
  zda se něco změnilo; pokud ano, vyvolejte `invalidateWindow()` pro
  spuštění překreslení pomocí `paint()`. Tato obslužná funkce musí být
  rychlá — ideálně by po většinu vyvolání neměla dělat vůbec nic.
- **`event`** *(funkce)* — vyvolána, když widget obdrží událost; Ethos
  prostřednictvím této obslužné funkce směruje do widgetu libovolné události.
- **`paint`** *(funkce)* — vykresluje widget, s tabulkou widgetu jako
  argumentem, nic nevrací. Vyvolána automaticky vždy, když byla spuštěna
  funkce `lcd.invalidate()`. Může být relativně pomalá, ale i tak by měla
  skutečně překreslovat pouze tehdy, když se něco změnilo.
- **`read`** *(funkce, volitelná)* — čte trvale uložená data widgetu.
- **`write`** *(funkce, volitelná)* — zapisuje trvale uložená data widgetu.
- **`init`** *(funkce)* — registruje widget a jeho zpětná volání v systému
  Ethos. Obvykle jde o poslední část skriptu:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

Hodnota `key` musí být jednoznačná mezi všemi nainstalovanými widgety;
ostatní pole se váží k životnímu cyklu widgetu, jak je popsáno výše.

Skripty se nacházejí v adresáři `scripts/` na SD card/eMMC, ideálně
uspořádané do samostatných složek pro jednotlivé widgety (viz [Správce
souborů](../system-setup/file-manager.md#top-level-folders) a [Příklady
umístění skriptů](example-script-locations.md)). Další zpracované příklady
najdete ve vlákně *FrSky ETHOS Lua Script Programming* na rcgroups.
