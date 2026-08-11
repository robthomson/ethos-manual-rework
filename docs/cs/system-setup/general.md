---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Obecné

![Obecná nastavení](../assets/system-general.png)

Zahrnuje vlastnosti displeje, zvuk, vario, haptiku a horní lištu.

## Vlastnosti displeje

- **Jazyk** — jazyk menu na displeji (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português a další).
- **Klávesnice** — rozložení virtuální klávesnice QWERTY, QWERTZ nebo AZERTY.
- **Jas** — posuvník jasu podsvícení; dlouhým stiskem `ENT` jej lze místo
  toho řídit ze zdroje (např. posuvníkem, jak ukazuje níže uvedený příklad)
  nebo jej nastavit natrvalo na minimum/maximum.

  ![Menu jasu](../assets/system-general-brightness-menu.png)
  ![Posuvník jasu](../assets/system-general-brightness-slider.png)

  !!! note
      Pokud se **Jas** rovná hodnotě **Jas v režimu spánku**, zůstává
      dotyková obrazovka aktivní i ve „spánku“.

- **Probuzení** — které z těchto podnětů probudí podsvícení ze spánku (lze
  povolit více než jeden): **Vždy zapnuto** (nikdy neusíná), **Páčky**,
  **Přepínače**, **Gyro** (naklonění vysílače). Klávesy jej probudí vždy,
  bez ohledu na tato nastavení.
- **Spánek** — doba nečinnosti, po níž se podsvícení vypne (zašedlé, pokud
  je Probuzení nastaveno na Vždy zapnuto).
- **Jas v režimu spánku** — jas podsvícení během spánku.
- **Tmavý režim** — světlé nebo tmavé téma displeje.
- **Barva zvýraznění** — akcentová barva uživatelského rozhraní (výchozí
  `#F8B038`).

## Nastavení zvuku {: #audio-settings }

![Nastavení zvuku](../assets/system-general-audio.png)

- **Jazyk zvuku** — jazyk hlasových hlášení.
- **Volba hlasů** — Ethos podporuje více současně používaných hlasových sad:

  - **Hlas 1 (hlavní)** — používá se pro všechna vestavěná systémová
    hlášení. Pro angličtinu je výchozí volba mezi americkou (`us`)
    a britskou (`gb`) sadou, které se načítají z `audio/en/us/system`
    a `audio/en/gb/system`. Uživatelské zvukové soubory pro [speciální
    funkci Play Audio](../model-setup/special-functions.md) patří do
    `audio/en/us/`, resp. `audio/en/gb/`.
  - **Hlas 2 / Hlas 3** — doplňkové sady, například vlastní TTS hlas. Každá
    potřebuje stejnou strukturu složek jako Hlas 1 — např. hlas nazvaný
    „Susan“ potřebuje `audio/en/Susan/` pro uživatelské zvuky
    a `audio/en/Susan/system` pro své systémové zvuky (každý hlas potřebuje
    složku `/system`, protože právě z ní se načítají hlášení **Play Value**
    a hlášení časovačů; seznam standardních systémových zvukových souborů ve
    formátu `.csv` je součástí každého vydání zvukových sad). Po instalaci
    lze hlas přiřadit jednotlivým časovačům i jednotlivým funkcím Play Audio
    — nebo jej dokonce nastavit jako Hlas 1 a zcela tak nahradit systémová
    hlášení.
  - **Hlas „default“** — instaluje se automaticky jako bezpečná záloha
    (a používá se k zabránění problémům s konverzí z instalací verze 1.4.x):
    pokud není Hlas 1 během instalace/aktualizace již nastaven, nastaví se
    na `default` a načítá se z `audio/en/default/system`. Často požadované
    vlastní zvukové soubory pro Play Audio se nacházejí v
    `audio/en/default/`.

- **Hlavní hlasitost** — posuvník celkové hlasitosti zvuku (dlouhým stiskem
  `ENT` ji lze řídit z potenciometru); během nastavování se přehrávají
  pípnutí, takže lze úroveň posoudit sluchem.
- **Režim zvuku**:
  - **Tichý** — bez zvuku (při startu se přesto spustí [výstraha tichého
    režimu](alerts.md), je-li povolena).
  - **Pouze alarmy** — slyšitelné jsou pouze alarmy.
  - **Výchozí** — normální zvuky.
  - **Často** — přidává chybová pípnutí při pokusu překročit minimum/maximum
    hodnoty.
  - **Vždy** — nad rámec režimu Často přidává pípnutí při běžné navigaci
    v menu.
  - **Bluetooth** (pouze X20S/HD/Pro/R/RS) — přenáší zvuk do spárovaného
    Bluetooth zařízení (headsetu apod.). Zvolte **Hledat zařízení**,
    přepněte cílové zařízení do párovacího režimu a po nalezení jej vyberte:

    ![Párování Bluetooth](../assets/system-general-audio-bluetooth.png)
    ![Vyhledávání Bluetooth](../assets/system-general-audio-bluetooth-searching.png)
    ![Vybrané zařízení Bluetooth](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Připojování Bluetooth](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth připojeno](../assets/system-general-audio-bluetooth-connected-ok.png)

    Volba **Ztlumení reproduktoru** poté řídí vestavěný reproduktor — vždy
    zapnuto, pouze při aktivní telemetrii, nebo řízeně ze zdroje (např.
    přepínačem). Vysílač si spárované zařízení pamatuje; pro normální provoz
    zapněte vysílač dříve než Bluetooth zařízení a po jeho připojení počítejte
    s několika sekundami, než se ztlumení reproduktoru znovu aktivuje.

## Vario {: #vario }

![Zvuk varia](../assets/system-general-audio-vario.png)

- **Hlasitost** — relativní hlasitost tónu varia.
- **Nulová výška tónu** — výška tónu při nulové rychlosti stoupání.
- **Maximální výška tónu** — výška tónu při maximální rychlosti stoupání.
- **Opakování** — prodleva mezi pípnutími při nulové výšce tónu.

Další informace o chování varia najdete u senzoru VSpeed v části
[Telemetrie](../model-setup/telemetry.md) a u [speciální funkce Play
Vario](../model-setup/special-functions.md).

## Haptika

- **Intenzita** — posuvník intenzity vibrací.
- **Režim** — stejná sada možností jako u Režimu zvuku výše.

## Umístění úložiště (X18 a X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Tyto vysílače mají interní 8GB eMMC. Ethos jej používá jako výchozí, takže
SD card je volitelná — můžete však vybrat eMMC, SD card nebo kombinaci obou.
Přesouváte-li systém a modely na SD card, zkopírujte příslušné složky
a soubory (včetně zvuků a bitmap) **před** přepnutím umístění úložiště.

![Umístění úložiště](../assets/system-general-storage.png)

## Horní lišta

![Nastavení horní lišty](../assets/system-general-topbar.png)

- **Digitální napětí** — zobrazuje napětí baterie vysílače v horní liště
  jako číslo místo ukazatele.
- **Digitální RSSI** — totéž pro RSSI v pásmu 2,4 GHz a 900 MHz.
- **Vybrat model při zapnutí** — zobrazí při startu obrazovku výběru modelu,
  ještě před výstrahami kontrolního seznamu předchozího modelu, takže lze
  model přepnout bez jejich předchozího potvrzení. Naposledy použitý model
  je ve výchozím stavu zvýrazněn.

  ![Výběr modelu při startu](../assets/system-general-model-start.png)

## Předvolba režimu USB

![Režim USB](../assets/system-general-usb.png)

Co se stane automaticky, když se vysílač připojí k PC přes USB:

- **Nenastaveno** — při připojení se zobrazí dotaz na volbu.
- **Joystick** — okamžitě přejde do režimu joysticku pro RC simulátor.
- **Ethos Suite** — okamžitě přejde do režimu Ethos pro [Ethos
  Suite](../ethos-suite/index.md).
- **Sériový** — okamžitě přejde do sériového režimu a přenáší ladicí výpisy
  Lua přes USB-Serial rychlostí 115200 bps (může být nutný ovladač
  virtuálního COM portu pro Windows).
