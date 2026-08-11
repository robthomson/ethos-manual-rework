---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Nalezení nejnovějšího bootloaderu nebo jiné komponenty

Vydání firmwaru Ethos obsahují soubor `components.json`, který uvádí
aktuální verzi každé komponenty pro jednotlivé vysílače. To je užitečné
pro potvrzení, zda je daná verze bootloaderu/firmwaru/zvuků/systémových
souborů skutečně aktuální, ještě před jejím nahráním.

!!! note "Snímky obrazovky se připravují"
    Tato stránka zatím neobsahuje snímky obrazovky ze simulátoru — viz [Proces
    tvorby snímků obrazovky](../contributing/screenshot-pipeline.md).

1. Stáhněte soubor `components.json` z nejnovějšího vydání Ethos.
2. Otevřete jej v textovém editoru (VS Code, Poznámkový blok apod.).
3. Najděte sekci pro váš vysílač — např. `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (Jde o ukázkový výpis — skutečná čísla verzí vždy zkontrolujte
   v souboru *aktuálního* vydání.)

4. Odečtěte verzi komponenty, kterou potřebujete — ve výše uvedeném
   příkladu je nejnovější bootloader pro řadu X20 verze `1.4.15`.

Kam umístit stažený soubor s firmwarem, najdete v části [Správce
souborů](../system-setup/file-manager.md#top-level-folders), a postup
pro přepnutí vysílače do režimu bootloaderu za účelem nahrání firmwaru
v části [Režimy připojení
USB](../getting-started/usb-connection-modes.md#bootloader-mode) — nebo
použijte [Ethos Suite](../ethos-suite/index.md), který kontrolu verzí
i nahrávání firmwaru zajistí automaticky.
