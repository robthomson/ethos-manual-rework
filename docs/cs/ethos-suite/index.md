---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite je doprovodná aplikace pro Windows/Mac určená ke správě vysílače
s firmwarem Ethos, připojeného přes USB.

!!! note "Snímky obrazovek budou doplněny"
    Ethos Suite je samostatná PC aplikace, nikoli vysílač samotný, a proto
    tato část nepoužívá snímky obrazovek zachycené v simulátoru, jako je to
    ve zbytku příručky — viz [Postup tvorby snímků
    obrazovek](../contributing/screenshot-pipeline.md).

Po připojení umožňuje Ethos Suite:

1. Zjistit typ vysílače, jeho ID a nainstalované verze — firmware,
   bootloader, interní RF modul, soubory ve flash paměti a soubory na
   SD card/eMMC.
2. Přepínat vysílač mezi režimem bootloaderu a běžícím systémem Ethos a zpět.
3. Porovnat nainstalované verze s aktuálními a automaticky je aktualizovat —
   pouze zastaralé komponenty, vše bez ohledu na verzi, nebo jednotlivé
   komponenty samostatně.
4. Zálohovat modely na disk pomocí **Model Manager**, nebo obnovit
   předchozí zálohu (což je nutné, protože soubory modelů nejsou zpětně
   kompatibilní mezi verzemi firmwaru).
5. Stáhnout jakýkoli firmware ze stránek FrSky prostřednictvím **Download
   center** a použít vysílač jako prostředníka k přímému nahrání firmwaru
   do modulu, senzoru, serva nebo přijímače.
6. Konvertovat obrázky a zvukové soubory do nativních formátů systému Ethos.
7. Poskytnout **Lua development tools** — dokumentaci API, ukázkové skripty
   a ladicí terminál.
8. Nahrát bootloader vysílače v režimu DFU (připojení s vypnutým napájením),
   nezávisle na tom, zda vlastní firmware vysílače stále funguje.
9. Opravit interní úložiště u vysílačů X18/S, TW Lite, XE a X20 Pro/R/RS
   pomocí **Repair Tool**, pokud nelze načíst NAND nebo se neukládají
   nastavení.
10. Bezpečně odpojit USB disky vysílače.
11. Upozornit při spuštění na dostupnou aktualizaci samotné aplikace Suite
    (nainstaluje se při ukončení).

## Režimy připojení

Kromě svých nástrojů pracuje Suite ve třech odlišných stavech připojení
vysílače:

- **Vysílač v režimu bootloaderu** — karta **Radio** kontroluje/aktualizuje
  firmware a soubory ve flash paměti / na SD card / eMMC; **Model Manager**
  zálohuje nebo obnovuje vysílač.
- **Vysílač v režimu Ethos** — Suite používá vysílač jako prostředníka
  (pomocí nástrojů **FRSK Flasher**/Download center) k přímému nahrání
  firmwaru do interního modulu nebo do jakéhokoli připojeného
  senzoru/serva/přijímače.
- **Vysílač v režimu DFU** — připojení s vypnutým napájením, které používá
  **DFU Flasher** k nahrání samotného bootloaderu, například když poškozený
  firmware brání normálnímu zapnutí vysílače.

Postup prvního přechodu existujícího vysílače na Ethos Suite najdete
v části [Migrace](migration.md), samotné rozhraní Suite popisuje část
[Obsluha](operation.md).
