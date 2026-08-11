---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# RF systém

Konfiguruje interní a/nebo externí RF modul(y) modelu, registrační ID
vlastníka, párování přijímače a volby přijímače. Zde se také nachází volba
mezi interním a externím modulem pro daný model — na rozdíl od téměř všeho
ostatního v [Nastavení systému](../system-setup/index.md) je volba RF
hardwaru **pro každý model zvlášť**, nikoli pro celý vysílač.

!!! note "Snímky obrazovek budou doplněny"
    Sada snímků obrazovek pro tuto sekci ještě nebyla vytvořena (viz
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)) —
    následující obsah je správný, ale zatím pouze textový.

## Registrační ID vlastníka {: #owner-registration-id }

Osmiznakový jedinečný kód (kombinace velkých/malých písmen a číslic, bez
speciálních znaků), který se při registraci stane **registračním ID**
přijímače. Nastavte *stejný* kód ve více vysílačích, chcete-li mezi nimi
používat funkci **Smart Share** — udělejte to ještě před vytvořením modelu,
který chcete sdílet. Kompatibilní s EdgeTX; jen částečně kompatibilní
s OpenTX.

## Vypnutí RF výstupu

Podržením `PAGE` při zapínání vypnete interní i externí RF výstup pro danou
session (vypnutí potvrdí varování). Samotné nastavení **State** modulu
zůstává ON — běžný restart obnoví normální vysílání.

## Režimy interního modulu

Interní modul X18/X20/X20S/X20HD (TD-ISRM) pracuje v jednom ze tří režimů —
modul TD-ISRM Pro ve X20 Pro/R/RS je obdobný, ale navíc přidává LoRa
a tandemové dvoupásmové varianty. Zvolený režim **musí odpovídat tomu, co
přijímač podporuje**, jinak párování selže; po změně režimu pečlivě
překontrolujte každý kanál a zejména chování failsafe.

- **ACCESS** — pásma 2,4 GHz a 900 MHz pracující v tandemu pod jedinou
  sadou ovládacích prvků ACCESS. Celkem až tři přijímače v jakékoli
  kombinaci 2,4 GHz (24 kanálů) a 900 MHz (16 kanálů); telemetrie z obou
  pásem je aktivní současně a označena podle pásma. Zdroj telemetrie **RX**
  udává, který přijímač je právě aktivním zdrojem telemetrie.
- **ACCST D16** — jediné pásmo 2,4 GHz pro starší přijímače řady „X“.
- **TD mode** — tandemové 2,4 GHz + 900 MHz s nízkou latencí a velkým
  dosahem pro přijímače Tandem, 24 kanálů v každém pásmu.

Verze firmwaru **Flex** přidávají druhý sloupec Type pro přepínání mezi
modulací FLEX915M (915 MHz ve stylu FCC) a FLEX868M (868 MHz ve stylu LBT)
v jakémkoli z výše uvedených tří režimů — pro zvolenou variantu musí být
nasazeny odpovídající antény. Uživatelé v EU mohou na 868 MHz použít
200/500 mW; při 25 mW jde telemetrie po 868 MHz, při 200/500 mW se
z důvodu shody s předpisy přesouvá na 2,4 GHz.

Každá volba režimu/rozsahu kanálů znamená kompromis v obnovovací frekvenci —
např. v režimu ACCESS se 8 kanálů obnovuje každých 7 ms, 16 kanálů každých
14 ms, 24 kanálů každých 21 ms (rotují v blocích po 8) a s kompatibilními
přijímači (řada RS, v2.1.7+) je pro kanály 1–8 dostupný **Racing mode**
se 4 ms.

## Registrace a párování přijímače (ACCESS) {: #registering-and-binding-a-receiver-access }

Párování přijímače ACCESS má dvě fáze — **registrace** musí proběhnout jen
jednou pro každou kombinaci přijímače a vysílače; **párování** lze poté
opakovat bezdrátově bez potřeby tlačítka bind.

**Fáze 1 — registrace**:

1. Klepněte na **Register** (tento krok úplně vynechejte, pokud je přijímač
   již registrován).
2. Při zapínání přijímače držte jeho tlačítko bind; vyčkejte, než se
   rozsvítí obě LED. Dialog se změní z „Waiting for receiver…“ na
   „Receiver connected“ a automaticky vyplní název přijímače.
3. Potvrďte/upravte **Registration ID** (výchozí je registrační ID
   vlastníka uvedené výše — shodná ID ve více vysílačích jsou to, co
   umožňuje funkci Smart Share), **Rx name** a **UID**. UID rozlišuje více
   přijímačů použitých společně v jednom modelu — u jediného přijímače
   ponechte 0; při použití několika (např. jeden na každý blok 8 kanálů) se
   běžně používá 0/1/2. UID nelze z přijímače později zpětně přečíst, proto
   jej fyzicky označte.
4. Klepněte na **Register**, potvrďte „Registration ok“ a poté přijímač
   vypněte — je registrován, ale ještě nespárován.

**Fáze 2 — párování**:

!!! warning
    Nikdy nepárujte s připojeným elektromotorem nebo běžícím motorem.

1. Přijímač vypnutý; zkontrolujte, že jste ve správném režimu modulu.
2. Klepněte na **RX1** (nebo 2/3) → **Bind**. Opakující se hlasové
   upozornění „Bind“ potvrdí režim párování.
3. Zapněte přijímač **bez** stisknutí jeho tlačítka bind; vyberte jej ze
   zobrazeného seznamu „Select device“.
4. Potvrďte „Bind successful“. Vypněte a znovu zapněte vysílač i přijímač —
   svítící zelená LED přijímače a zhasnutá červená znamenají, že je spojení
   navázáno. Párování není nutné opakovat, dokud se jedna ze stran
   nevymění.
5. Postup zopakujte pro další přijímače (RX2, RX3), pokud je používáte.

## Volby přijímače

Se zapnutým přijímačem klepněte na jeho tlačítko RX pro:

- **Options** — **Telemetry** (zapnuto/vypnuto pro tento přijímač),
  **Reduced telemetry power 25mW** (namísto běžných 100 mW — užitečné,
  pokud blízká serva zachytávají RF rušení), **High PWM Speed** (obnovování
  serv každých 7 ms místo 18 ms — ověřte, že to vaše serva zvládnou),
  **Telemetry port** (S.Port/F.Port/FBUS), **SBUS** (16 nebo 24 kanálů —
  před zapnutím musí každé připojené SBUS zařízení podporovat SBUS-24)
  a **Channel Mapping** pro přemapování kanálů na konkrétní piny přijímače.
- **Share** — předá přijímač jinému vysílači ACCESS s *odlišným*
  registračním ID vlastníka. Na zdrojovém vysílači klepněte na Share (jeho
  zelená LED zhasne); na cílovém vysílači provedete běžný Bind — Share
  přeskočí opakovanou registraci, protože se ID přenese automaticky.
  Sdílení ukončíte opuštěním funkce na zdrojovém vysílači; opětovným
  spárováním se přijímač vrátí zpět. (Není potřeba vůbec, pokud všechny
  vysílače již mají shodné registrační ID vlastníka — pak stačí spárovat
  přímo na tom vysílači, který jej má ovládat.)
- **Reset bind** — uklidí stav po funkci Share a obnoví vaše původní
  párování; poté přijímač vypněte a znovu zapněte.
- **Factory reset** — resetuje přijímač a vymaže jeho UID, čímž jej úplně
  odregistruje.

S **vypnutým** přijímačem totéž tlačítko RX nabízí **Options** (čeká na
připojení přijímače), **Bind** (např. pro opětovné spárování přijímače
dříve spárovaného jinde) a **Clear** (odpovídá Reset bind).

## Redundantní přijímače {: #redundant-receivers }

Druhý přijímač lze pro redundanci spárovat s nevyužitým slotem RX — 2,4G
a 900M se mohou navzájem zálohovat. Redundance FrSky vyhodnocuje situaci
**po jednotlivých rámcích** a vždy použije nejlepší dostupný rámec
(failover typu active/active), takže se řízení může podle potřeby
přepínat mezi přijímači rámec po rámci.

1. Propojte SBUS Out redundantního přijímače s SBUS In hlavního přijímače.
2. Zapněte odpovídající interní RF modul (např. 900M) a nastavte jeho
   antény/výkon.
3. Zaregistrujte nový přijímač (pokud ještě není) a poté jej spárujte
   s volným slotem RX podle výše uvedeného postupu.
4. Zkontrolujte, že svítí jeho zelená LED — nyní je uveden jako redundantní
   přijímač.

## Failsafe {: #failsafe }

Data failsafe se z vysílače odesílají znovu přibližně každých 10 sekund;
u přijímačů TD/TW/AP/AP Plus se navíc ukládají i v přijímači, takže přežijí
jeho restart. Po každé aktualizaci firmwaru přijímače, která toto chování
přidává, pečlivě znovu zkontrolujte failsafe.

- **Hold** — podrží poslední přijaté polohy kanálů.
- **Custom** — pro každý kanál zvlášť: **Not Set**, **Hold**, **Custom**
  (pevná hodnota — klepnutím na ikonu šipky zachytíte aktuální hodnotu,
  nebo ji zadejte přímo) nebo **No Pulses**.
- **No Pulses** — zcela zastaví impulzy, což je vhodné pro letové
  kontroléry s vlastním chováním return-to-home při ztrátě signálu.
- **Receiver** — (přijímače řady X a novější) nastaví failsafe místo toho
  v samotném přijímači.

!!! warning
    Než se na zvolené nastavení failsafe začnete spoléhat, pečlivě jej
    otestujte.

## Kontrola dosahu {: #range-check }

Provádějte ji na letišti před každým letovým dnem s novou nebo změněnou
konfigurací. Volba **Range Check** záměrně snižuje vysílací výkon (režim
potvrzuje opakované hlasové upozornění) a zobrazuje živé hodnoty VFR%/RSSI
pro vyhodnocení kvality spojení. Výkon FrSky při kontrole dosahu je
přibližně −10 dB vůči běžné provozní úrovni +20 dB; při výšce 1 m
u vysílače i přijímače lze očekávat kritický alarm okolo 30 m — kratší
vzdálenost za normálních podmínek může signalizovat problém.

Při více spárovaných přijímačích se data kontroly dosahu zobrazují vždy pro
jeden aktivní přijímač v každém pásmu — vypnutím právě aktivního přijímače
umožníte převzetí dalšímu (v prioritě 0/1/2, zobrazené senzorem **RX**),
takže lze postupně zkontrolovat každý z nich.

## Externí a RF moduly třetích stran

Externí moduly FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro) se
řídí stejným postupem Register/Bind jako interní modul, s počty kanálů,
úrovněmi výkonu a požadavky na antény podle konkrétního protokolu — přesné
údaje najdete v manuálu daného modulu.

**ELRS** (ExpressLRS) je podporován jak prostřednictvím režimu ELRS modulu
TWIN Lite Pro, tak prostřednictvím originálních modulů ELRS (které
vyžadují instalaci Lua skriptu ELRS do `scripts/elrs`, aby se objevily jako
volba modulu). Dvanáct kanálů; klíčová nastavení jsou **Packet Rate**
(kompromis mezi latencí a dosahem), **Telemetry Ratio** (jak často se
telemetrie odesílá, 1:1 až 1:128), **Switch Mode** (**Hybrid** — většina
pomocných kanálů omezena na 2–3 polohy pro nižší latenci — nebo **Wide** —
plné rozlišení 64–128 kroků), **Model Match** a **Tx Power**
(10 mW–1000 mW, volitelně **Dynamic Power** pro automatické přizpůsobení
podle kvality spojení — vyžaduje zapnutou telemetrii).

**Moduly třetích stran** (v současnosti Ghost, Multi-protocol, Crossfire,
kromě ELRS) vyžadují každý svůj vlastní, uživatelem nainstalovaný Lua
skript — viz poznámky ke `scripts/` v [Screenshot Pipeline](../contributing/screenshot-pipeline.md)
a vlákno *Third-Party External Modules* na rcgroups. Položka modulu se na
obrazovce RF objeví teprve po instalaci jeho skriptu. Modul Multi-protocol
(IRX4 Lite) lze navíc flashovat firmwarem přímo ze
[Správce souborů](../system-setup/file-manager.md): zkopírujte soubor
s firmwarem do `Firmware/` a poté zvolte **Flash external multimodule**.
