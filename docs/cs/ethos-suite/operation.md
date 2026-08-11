---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Obsluha

## Sekce Welcome

**Update News** — poznámky k vydání a doporučení k zálohování před
aktualizací. Ethos 1.6.0+ vyžaduje, aby interní RF modul a přijímače
TD/TW/AP/AP Plus měly verzi v3.0.1+, aby bylo možné využít jeho vylepšení.
Zapnutí volby **Pre-releases** (se serverem nastaveným na GitHub — viz
[Nastavení Suite](#suite-settings)) zde navíc zobrazí i předběžná vydání
společně s celou historií vydání.

**Ethos web page** — vložené zobrazení stránky ethos.frsky-rc.com: zdroje,
odkazy na šablony modelů a seznam podporovaných vysílačů.

## Sekce Radio

Spravuje připojený vysílač. Zapněte jej do [režimu
bootloaderu](../getting-started/usb-connection-modes.md#bootloader-mode) a
připojte přes USB — Suite po detekci zobrazí typ vysílače (např. „X20“).

### Informace o vysílači

- **Ethos** — nainstalované verze firmwaru/bootloaderu; **Manage Ethos**
  přejde k jejich aktualizaci, pokud jsou zastaralé.
- **RF Module** — nainstalovaný firmware interního RF modulu; **Manage
  internal module** přejde k jeho aktualizaci, pokud je zastaralý.
- **Model manager** / **Lua library** / **Download center** — zkratky
  k těmto nástrojům.

### Aktualizace Ethos {: #updating-ethos }

Karta **Ethos** zobrazuje vedle sebe verze firmwaru, bootloaderu, SD card/eMMC
(zvukové soubory) a flash paměti (systémové bitmapy) — systémové soubory ve
flash paměti se nyní aktualizují společně s firmwarem a nespravují se již
samostatně.

- **Write outdated components** — aktualizuje pouze to, co je zastaralé.
- **Write all components** — aktualizuje vše bez ohledu na verzi.
- Jednotlivé volby **Write firmware**, **Write bootloader**, **Write audio
  files**, každou z nich spustíte kliknutím na tmavě šedé tlačítko vedle
  vybrané volby.
- **Flash from a local file** — obejde stahování a použije soubor firmwaru,
  který již máte na disku.

Výběr vydání znamená nejprve zvolit **branch** (Stable/Testing) a poté verzi.
Aktualizace nejprve vyzve k vytvoření záložní kopie (**Go to backup page**) —
vytvořte ji. Pokud interní RF modul nemá verzi v3.0.1+, Ethos 1.6.0+ vyžaduje
jeho aktualizaci před pokračováním (**Go to Module manager** jej naflashuje
automaticky a poté aktualizace Ethos pokračuje) — u přijímačů TD/TW/AP/AP Plus
je následně nutné smazat telemetrii a znovu ji vyhledat, aby se převzaly
aktualizované názvy senzorů.

Průběh aktualizace se zobrazuje krok za krokem (přepnutí do bootloaderu,
stahování, kopírování, odpojení, zápis, obnovení, „Update successful!“) —
průběh zápisu zrcadlí i obrazovka samotného vysílače.

!!! note "Aktualizace předběžných verzí"
    Soubory předběžného vydání se mohou změnit bez změny čísla verze, což
    Suite nedokáže rozpoznat — předběžnou verzi, kterou již používáte, vždy
    znovu naflashujte, jakmile se z ní stane plné vydání. Pokud si nejste
    jisti, zkontrolujte datum firmwaru v [System →
    Info](../system-setup/information.md).

!!! note "Aktualizace z Ethos 1.2.8 nebo starší"
    Z tak staré verze nemusí být Suite schopen naflashovat
    firmware/bootloader plně automaticky — místo toho se zobrazí dialog
    s pokyny pro ruční flashování. V obou případech před odpojením USB
    ručně odpojte disky.

Soubory systémových bitmap se nyní aktualizují automaticky společně
s firmwarem (není nutná samostatná správa); zvukové soubory se aktualizují
volbou **Write all components** nebo **Write audio files** (stáhne vybraný
jazykový balíček, např. „English audio pack“).

### RF Module Manager

Vyberte verzi (obvykle nejnovější) a volbou **Flash module** přímo
aktualizujte firmware interního RF modulu — po dokončení se potvrdí
„...has been flashed successfully“. Toto se spouští i automaticky v rámci
povinné aktualizace na v3.0.1 popsané výše.

### Režim Ethos

**Switch to Ethos** restartuje vysílač z režimu bootloaderu do běžícího
Ethos (indikováno zelenou ikonou USB na vysílači a zmizením „(Bootloader
Mode)“ z hlavičky Suite). To je nutné, aby **Download center** mohlo
vysílač použít jako prostředníka pro flashování modulů, přijímačů, senzorů
a servopohonů. Tlačítko se poté změní na **Switch to Bootloader** pro
opačný postup. **Eject Drives** korektně odpojí vysílač.

### Model Manager

Zálohuje soubory modelů a nastavení na disk nebo obnoví předchozí zálohu.

!!! warning
    Obnovení **neobnoví** firmware — po obnovení modelů/nastavení
    samostatně naflashujte verzi firmwaru, která dané záloze skutečně
    odpovídá (viz [Aktualizace Ethos](#updating-ethos)), protože soubory
    modelů nejsou zpětně kompatibilní.

- **Backup Location** — vyhledejte složku (pamatuje se pro každý typ
  vysílače); pod ní se zobrazuje datum a čas poslední zálohy.
- **Backup** — uloží soubory modelů a zaznamená k nim aktuální verzi Ethos.
- **Restore** — vyberte, které součásti obnovit: Audio (ve výchozím stavu
  vypnuto), Scripts, Screenshots, System Bitmaps (ve výchozím stavu vypnuto
  — spravuje se nyní s firmwarem), Models (včetně textových souborů
  jakéhokoli [uživatelsky definovaného kontrolního
  seznamu](../how-to/user-defined-checklist.md) uložených společně s nimi),
  Language, User Bitmaps, Logs, System Settings.

### Lua library

Prohlížejte a jedním kliknutím instalujte Lua skripty/nástroje ze vzdálené
knihovny FrSky (nebo instalujte z lokálního zip souboru); nainstalované
skripty se zobrazují společně se vzdáleným katalogem, jakmile nějaké
existují.

## Sekce Tools

- **Download center** — stáhněte jakýkoli firmware ze stránek FrSky a
  (pokud je vysílač v režimu Ethos) použijte jej jako prostředníka pro
  flashování modulu, senzoru, servopohonu nebo přijímače připojeného přes
  upgrade konektor S.Port. Vyberte produkt ze seznamu (např. přijímač
  TW SR8), prohlédněte dostupné **assets**, tlačítkem **Download** uložte
  soubor lokálně nebo tlačítkem **Flash** zapište přímo do připojeného
  zařízení — ukazatel průběhu sleduje flashování a končí hlášením
  „...has been flashed successfully!“

- **Image manager** — převádí obrázky do nativního formátu Ethos (32bitový
  BMP, RGB, alfa kanál se přidává jen v případě potřeby) ve zvolené
  velikosti se zachováním poměru stran. Referenční velikosti: obrázky
  modelů 300×280 (X20) / 180×168 (X18); celoobrazovkové obrázky 800×480
  (X20) / 480×320 (X18) — pravidla pojmenování bitmap viz [Správce
  souborů](../system-setup/file-manager.md#top-level-folders). Umožňuje
  také přímo prohlížet složky `bitmaps/gps`, `bitmaps/models` a
  `bitmaps/user` ve vysílači, včetně nahrávání souborů. Obrázky přidáte do
  seznamu ke konverzi tlačítkem **+** (TIFF není podporován), zvolte
  výstupní cestu (lokální složku; přímo do vysílače pod obrázky
  modelů/uživatele/GPS; nebo aktuálně otevřenou složku vysílače) a
  případně nechte výstupní složku automaticky otevřít nebo vynuťte alfa
  kanál.

- **Audio manager** — převádí zvuk do formátu Ethos (PCM linear, 32 kHz,
  mono, 16bit little-endian). Soubory přidejte tlačítkem **+**, zvolte
  lokální složku nebo je odešlete přímo do složky `audio` ve vysílači
  (poté je přesuňte do správné podsložky hlasu) a případně nechte cílovou
  složku automaticky otevřít.

- **Lua development tools** — **Lua Docs** odkazuje na referenční příručku
  Ethos Lua (viz také vlákno *FrSky - ETHOS Lua Script Programming* na
  rcgroups); **Lua Demo Scripts** odkazuje na ukázkové skripty na GitHubu
  Ethos-Feedback-Community; **Debug** otevírá živé okno protokolu pro
  výpisy Lua `print()` posílané přes USB-Serial, když je vysílač v režimu
  Serial:

  1. Připojte vysílač k Suite běžným způsobem a přepněte do režimu Ethos.
  2. Upravujte Lua skripty přímo na připojeném disku vysílače,
     v libovolném editoru kódu.
  3. Otevřete **Lua Development Tools** → **START DEBUG** — vysílač se
     restartuje do režimu Serial/debug a znovu inicializuje skripty.
  4. Výstup `print()` každého aktivního skriptu se přenáší do terminálu
     Suite.
  5. **STOP DEBUG** přepne zpět do normálního režimu Ethos pro další
     úpravy.

- **DFU Flasher** — flashuje bootloader přes USB (DFU) připojení při
  vypnutém vysílači; funguje i s úplně poškozeným firmwarem, protože
  základní ST bootloader je uložen v ROM. Tlačítkem **Select Bootloader**
  vyberte stažený soubor (Suite oznámí jeho verzi/vhodnost), připojte
  **vypnutý** vysílač a poté stiskněte **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Obvykle chybějící nebo nesprávný DFU ovladač. Většina počítačů
      s Windows 10+ zvládne systémy Tandem s výchozím ovladačem USB DFU,
      ale Windows Update jej někdy nahradí obecným ovladačem, který
      nefunguje — zkontrolujte Správce zařízení a zvažte nástroj jako
      Impulse Driver Fixer. Uživatelé Horus X10 mohou konkrétně
      potřebovat nainstalovat USB ovladač STM32 bootloaderu ručně
      (Impulse Driver Fixer nebo Zadig), protože Windows 10 jej ve
      výchozím stavu neinstaluje.

- **Repair Tool** — pro X18/S, TW Lite, XE a X20 Pro/R/RS: přeformátuje
  interní úložiště, pokud vysílač nemůže čtení NAND nebo ukládání
  nastavení provést.

## Sekce Others

- **Documentation** — odkazy na GitHub Ethos-Feedback-Community, oficiální
  manuály Ethos (ke stažení) a FAQ k Ethos Suite.
- **Ethos Github** — vydání a sledování problémů (před vytvořením nového
  hlášení prohledejte existující).

### Nastavení Suite {: #suite-settings }

- **Language** — čeština, němčina, angličtina, španělština, francouzština,
  hebrejština, italština, nizozemština, norština, portugalština,
  slovinština, čínština.
- **Server location** — **FrSky server** nebo **GitHub** (nutné pro přístup
  k předběžným vydáním výše).
- **Debug options** — přepnutí vyskakovacího okna při fatální chybě;
  zapnutí plného protokolování ladění Suite (nejen pádů); otevření složky
  s protokoly.
- **Version** / **Update Suite** — aktuální verze a ruční kontrola
  aktualizací.
- **About** — poděkování za použité komponenty.

## Ovládání z příkazové řádky

Ethos Suite lze spustit z terminálu:

| Parametr | Funkce |
|---|---|
| `--help` | Zobrazí nápovědu k příkazové řádce. |
| `--version` | Zobrazí nainstalovanou verzi Suite. |
| `--list-radios` | Vypíše všechny podporované vysílače FrSky. |
| `--radio-components --radio {RADIO}` (nebo `--radio auto`) | Vypíše součásti připojeného vysílače a jejich cesty. `auto` provede automatickou detekci; pokud je připojeno více vysílačů, zadejte `{RADIO}`. |
| `--get-path {COMPONENT}` | Získá cestu ke součásti — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` nebo `I18N`. |
| `--serial start` \| `--serial stop` | Zapne/vypne režim sériového ladění. |

!!! note
    Suite se vůbec nespustí, pokud nerozpozná platný příkaz.
