---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Správce souborů

![Správce souborů – vysílač](../assets/system-filemanager-radio.png)

Správce souborů umožňuje prohlížet úložiště vysílače a nahrávat firmware do
interního RF modulu, zařízení připojených přes S.Port, zařízení OTA
(Over-The-Air) a externích modulů.

## Rozvržení úložiště

Klepnutím na **Flash** (nebo stiskem `PAGE` pro přepnutí disků) zobrazíte
interní virtuální USB flash disk vysítače, který slouží pro systémové bitmapy
a fonty:

![Úložiště Flash](../assets/system-filemanager-flash.png)

- `bitmaps/system` — bitmapy použité pro zobrazení na obrazovkách a ikony
- `fonts/` — fonty pro jednotlivé jazykové volby

Jak bootloader, tak samotný systémový firmware jsou umístěny v této interní
flash paměti, a to u každého vysílače FrSky až po původní X9D.

Řada **X20/X20S/X20HD** používá SD card formátovanou na FAT32 s kapacitou 32 GB
nebo menší (dobrou volbou je karta SanDisk Ultra Micro SDHC Class 10 16GB).
Modely **X18** a **X20 Pro/R/RS** standardně používají interní eMMC (vedle ní
lze přidat i externí SD card) — pro její prohlížení klepněte na **Radio**.
Ethos automaticky vytvoří složky `Logs/`, `models/` a `screenshots/`, pokud
chybí; složka `Firmware/` je ruční konvence pro soubory firmwaru zařízení,
například přijímačů.

## Složky v nejvyšší úrovni {: #top-level-folders }

- **`audio/`** — uživatelské a systémové zvukové soubory, rozdělené podle
  hlasu (`audio/en/gb`, `audio/en/us`, `audio/en/default`). Uživatelské
  soubory přehrává [speciální funkce Play Audio](../model-setup/special-functions.md);
  systémové soubory zahrnují `hello.wav` (uvítání „Welcome to Ethos“ — lze
  přidat i `bye.wav`, ale není součástí dodávky). Formát: 16 kHz nebo 32 kHz
  PCM, lineární 16bitový, nebo A-law (EU)/µ-law (US) 8bitový; názvy souborů
  až 31 znaků plus přípona. Všechny tři složky hlasů udržuje Ethos Suite
  synchronizované bez ohledu na to, která je skutečně zvolena.

  ![Složka audio](../assets/system-filemanager-audio.png)

- **`bitmaps/`** — `bitmaps/models/` obsahuje uživatelské obrázky modelů
  (nastavené v [Model Edit](../model-setup/model-edit.md) nebo v průvodcích
  novým modelem); `bitmaps/user/` obsahuje vše ostatní. Doporučený formát:
  32bitový BMP, 8 bitů na barvu, s alfa kanálem, 300×280 px — tím zůstává
  dekódování ve vysílači nenáročné. Ethos mění velikost souborů BMP za běhu,
  ale ne PNG/JPEG. Názvy souborů mohou obsahovat pouze znaky
  `A-Z a-z 0-9 ()!-_@#;[]+=` a mezery a musí mít 11 znaků nebo méně (plus
  čtyřznakovou příponu), aby se zobrazily ve volbě obrázku modelu — delší
  názvy se ve Správci souborů stále zobrazí, ale nebude je tam možné vybrat.
  Nástroje pro konverzi obrázků v Ethos Suite převod formátu provedou za vás.

  ![Složka bitmaps](../assets/system-filemanager-bitmaps.png)

- **`documents/user/`** — uživatelské textové dokumenty, vyvolávané widgetem
  displeje **Text**.

- **`Firmware/`** — soubory firmwaru pro interní RF modul, externí moduly a
  další zařízení (přijímače atd.), které se odtud nahrávají přes S.Port nebo
  OTA. Nový firmware sem zkopírujte, když je vysílač v [režimu
  bootloaderu](../getting-started/usb-connection-modes.md) a připojen přes
  USB; klepnutím na soubor firmwaru a volbou **Flash** se aktualizace spustí:

  ![Nahrání firmwaru do interního RF modulu](../assets/system-filemanager-flash.png)
  ![Nahrání firmwaru přijímače S8R přes S.Port](../assets/system-filemanager-flash-S8R.png)
  ![Nahrání firmwaru přijímače TD-R18 přes OTA](../assets/system-filemanager-flash-TD-ISRM.png)
  ![Nahrání bootloaderu](../assets/system-filemanager-flash-bootloader.png)

- **`I18n/`** — soubory jazykových překladů.

- **`Logs/`** — datové logy.

- **`models/`** — samotné soubory modelů. Zde je nelze přímo editovat, pouze
  zálohovat nebo sdílet. Od verze Ethos v1.2.11 je model pojmenován podle
  názvu modelu namísto `model01.bin` a dále (např. model nazvaný „Extra“ se
  stane `Extra.bin`; druhý „Extra“ pak `Extra01.bin`). Přejmenování modelu
  v [Model Edit](../model-setup/model-edit.md) přejmenuje i jeho soubor —
  vždy malými písmeny (zobrazovaný název s velkými i malými písmeny je uložen
  uvnitř souboru) a ne každý znak z názvu modelu se do názvu souboru přenese.
  Od verze v1.1.0 Alpha 17 má každá uživatelem vytvořená kategorie modelů
  vlastní podsložku.

- **`screenshots/`** — výstup [speciální funkce
  Screenshot](../model-setup/special-functions.md).

- **`scripts/`** — Lua skripty, volitelně uspořádané do vlastních podsložek
  s podpůrnými soubory. Typy skriptů jsou **widgets** (viz
  [Displeje](../displays/index.md)), **tasks a sources** (vlastní senzory
  nebo akce po letu — po instalaci sem se objeví v nabídce
  [Lua](../model-setup/lua-scripts.md) daného modelu) a **tools** (např.
  konfigurační nástroje pro stabilizované přijímače v nabídkách System).
  Externí moduly třetích stran mají každý vlastní skript a složku, např.
  `scripts/multi`, `scripts/elrs`, `scripts/ghost`, `scripts/crossfire`.

  !!! warning
      Lua skripty prodlužují dobu startu vysílače. U dobře napsaného skriptu
      je zdržení nepostřehnutelné — špatně napsaný skript může start
      zdržet téměř neomezeně.

- **`radio.bin`** (korenová složka) — soubor systémového nastavení, který
  vysílač zapisuje sám při inicializaci. Před aktualizací firmwaru jej
  zálohujte společně se složkou `models/`, abyste se v případě potřeby mohli
  vrátit na starší verzi.

- **`firmware.bin`** (korenová složka) — vložením nového souboru firmwaru
  vysílače sem zajistíte jeho automatické nahrání při nejbližším odpojení
  vysílače od PC. Ve stejném průchodu může být nutné aktualizovat i obsah
  SD card/eMMC a interního flash disku.

- **`sdcard.version`** (korenová složka) — verze obsahu SD card, kterou
  spravuje Ethos Suite.

## Sdílení souborů přes Bluetooth

Ethos umí přenášet soubory mezi vysílači přes Bluetooth. Na **přijímajícím**
vysílači přejděte ve Správci souborů do cílové složky, dlouze stiskněte `ENT`
a zvolte **Receive file here**:

![Příjem přes Bluetooth](../assets/system-filemanager-bluetooth-receive.png)

Na **odesílajícím** vysílači klepněte na soubor, zvolte **Send file** a
postupujte podle pokynů na obou vysílačích:

![Odeslání přes Bluetooth](../assets/system-filemanager-bluetooth-send.png)

Pokud některý z vysílačů již má aktivní připojení Bluetooth (telemetrie,
propojení učitel–žák nebo — u X20S/Pro — audio), zobrazí se dotaz, zda má být
toto zařízení nejprve odpojeno.
