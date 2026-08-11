---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Umístění ukázkových skriptů

Oficiální ukázkové skripty jsou zveřejněny na adrese
[github.com/FrSkyRC/ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/tree/main/lua)
(zejména `/lua/examples/task` a `/lua/examples/source`). Většina ukázek
jsou Lua widgety (konfigurují se v [Konfiguraci
obrazovek](../displays/custom-widgets.md)); ukázka **`servo`**
konkrétně demonstruje **systémový nástroj** — skript, který se objeví za
položkou **Info** v nabídce System, nikoli jako widget na displeji.

## Stažení skriptu

1. Otevřete výše uvedený odkaz na repozitář v prohlížeči a přejděte do
   požadované složky a poté k souboru `main.lua`.
2. Klikněte na soubor, čímž jej zobrazíte, a poté na **Raw**.
3. Klikněte pravým tlačítkem na stránku → **Uložit stránku jako…** a uložte ji jako `main.lua`.
4. Abyste zabránili kolizi se soubory `main.lua` jiných skriptů, přesuňte jej do
   odpovídajícím způsobem pojmenované složky — rozumnou volbou je vlastní
   název zdrojové složky.

U všech dalších souborů, které skript potřebuje (obrázky atd.): klikněte na soubor, klikněte
na **Download**, poté klikněte pravým tlačítkem a zvolte **Uložit obrázek jako…** (nebo
ekvivalent), abyste jej uložili spolu se skriptem.

Skripty se instalují do složky `scripts/` na SD card/eMMC — viz [Správce
souborů](../system-setup/file-manager.md#top-level-folders).

Podívejte se také na vlákno *FrSky ETHOS Lua Script Programming* na rcgroups,
kde najdete komunitní skripty a diskuzi nad rámec oficiálních ukázek.
