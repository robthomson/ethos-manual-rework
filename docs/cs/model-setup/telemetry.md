---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telemetrie

![Nalezené senzory](../assets/model-telemetry-discovered-new-sensors.png)

Telemetrie přenáší informace z modelu zpět k pilotovi — kvalitu spojení
(RSSI, VFR), napětí a proudy a cokoli dalšího, co připojený senzor hlásí
(pozice GPS, výška atd.). Podporováno je až 100 senzorů na model; vyhledání
a konfigurace probíhá zde, ale telemetrie se *zobrazuje* jako [widgety na
obrazovkách displeje](../displays/index.md), které se konfigurují zvlášť
v Konfiguraci obrazovek.

## Jak funguje telemetrie FrSky {: #how-frsky-telemetry-works }

Senzory FrSky nepotřebují hub: **Smart Port (S.Port)** je 3vodičová
sběrnice (Gnd, V+, signál), řetězitelná v libovolném pořadí do konektoru
S.Port na přijímačích řady X/S a novějších, pracující v poloduplexu na
57 600 bps (F.Port a FBUS jsou rychlejší).

- **Physical ID** — sběrnici může využívat až 28 uzlů (včetně přijímače),
  každý potřebuje jedinečné Physical ID (00–1B hex). Zařízení FrSky se
  dodávají s rozumnými výchozími hodnotami (např. Vario = 00, FLVSS = 01,
  proudový senzor = 02, GPS = 03) — pokud připojíte dvě stejná zařízení,
  je nutné u druhého změnit Physical ID přes [Konfiguraci
  zařízení](../system-setup/devices.md).
- **Application ID** — nezávislé na Physical ID: jeden senzor může hlásit
  více hodnot, každá s vlastním Application ID. Vario má jedno Physical ID,
  ale dvě Application ID (výška, vertikální rychlost); FLVSS má jedno
  Physical ID a jedno Application ID (napětí). Sledování dvou 6S sad dvěma
  senzory FLVSS znamená změnit u druhého **obě** ID — Physical ID pro
  výhradní komunikaci na sběrnici a Application ID, aby přijímač rozlišil
  Lipo 1 a Lipo 2 (např. `0300` → `0301`). Běžně se mění 4. hexadecimální
  číslice, 0–F.

  !!! note
      Senzory se stejným Application ID a odlišnými Physical ID jsou
      přípustné pouze s vypnutou [detekcí konfliktu
      senzorů](../system-setup/alerts.md) — jde o zvláštní účelové
      nastavení, nikoli o běžný případ.

Každá přijatá hodnota je vedena jako samostatný senzor: hodnota, Physical/
Application ID, upravitelný název, jednotka, počet desetinných míst,
volitelný příznak zápisu logů na SD card a vlastní průběžné min/max.
Senzory se po nastavení automaticky vyhledávají při každém zapnutí, ale
poprvé je nutné je vyhledat **ručně**. Po nalezení může být senzor hlášen
hlasem, použit jako vstup [vypočítaných senzorů](#calculated-sensors),
použit v [logických přepínačích](logical-switches.md),
[proměnných](variables.md) nebo [mixech](mixes.md), zobrazen na vlastní
telemetrické obrazovce, nebo odečten přímo z této stránky nastavení bez
vytváření jakékoli obrazovky.

**FBUS** (dříve F.Port2) jde ještě dál — sdružuje řízení SBUS a telemetrii
S.Port do jediné linky na 460 800 bps (proti 115 200 u F.Port a 57 600
u S.Port — tyto tři přenosové rychlosti jsou vzájemně nekompatibilní) a
umožňuje jednomu hostu komunikovat po této jediné lince s několika
podřízenými doplňky, vše bezdrátově konfigurovatelné z vysílače.

### Telemetrie s více přijímači (ACCESS Trio)

Pokud jsou v [RF
systému](rf-system.md#registering-and-binding-a-receiver-access)
registrovány až tři přijímače, lze každý spárovaný přijímač konfigurovat
individuálně (piny portů atd.) přes RX1/RX2/RX3. Obvykle existuje jedna
příchozí telemetrická cesta na jedno RF spojení — výjimkou jsou systémy
Tandem/TD, které provozují 2,4 GHz a 900 MHz jako dvě cesty na jednom
modulu. Aktivní zdroj telemetrie se může měnit i za letu podle RF
podmínek; senzor **RX** hlásí v reálném čase, který přijímač právě posílá
telemetrii (a zaznamenává to do logu).

Běžné zapojení: propojit sběrnici senzorů S.Port do řetězu přes všechny tři
přijímače se společným napájením, poté každý přijímač registrovat/spárovat
a vyhledat senzory jako obvykle — zdroj telemetrie se přepíná automaticky
podle změny aktivního RX a data *externích* senzorů S.Port jej transparentně
následují. (Interní senzory přijímače — RSSI, VFR, RxBatt, ADC2 a samotný RX
— se tímto způsobem nepropojují; vždy se hlásí za ten přijímač, který je
právě zdrojem. Současná telemetrie ze všech tří najednou je plánována, ale
zatím není dostupná.)

## Senzory kvality spojení

- **RSSI** (Receiver Signal Strength Indicator) — jak silné je vysílání
  vysílače v místě přijímače. Výchozí alarmy: **ACCESS**/**TD**/
  **TW** 35 (nízká) / 32 (kritická), ztráta kontroly kolem 28; **ACCST**
  45 / 42, ztráta kontroly kolem 38. Hlášení „Telemetry Lost“ se ozve,
  když je spojení úplně přerušeno — v tom okamžiku **už nemohou zaznít
  žádné další alarmy**, protože vysílač nemá žádnou telemetrii
  k vyhodnocení; berte to jako pokyn k okamžitému návratu. (Při vzdálenosti
  pod ~1 m může být přijímač zahlcen a produkovat falešné smyčky alarmů
  Lost/Recovered — nejde o skutečnou závadu.) RSSI dobře přibližuje
  efektivní dosah, ale spolehlivějším ukazatelem kvality spojení je VFR.

  ![Senzor RSSI](../assets/model-telemetry-edit-rssi-sensor.png)

  Přijímače TD hlásí RSSI pro každé pásmo zvlášť (2.4G, 900M); přijímače TW
  rovněž po jednom na pásmo (2.4FSK, 2.4LoRa, 900M) — zapnutím **Individual
  RSSI alert per band** získáte oddělená hlasová hlášení pro každé pásmo
  místo jednoho společného:

  ![Individuální hlášení RSSI](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — počet platných paketů na 100 přijatých; od
  verze ACCESS 2.1 náhrada za dřívější zahrnování podílu ztracených rámců
  do RSSI. Výchozí **Low value warning** je 50 %.

  ![Senzor VFR](../assets/model-telemetry-edit-vfr-sensor.png)

  Přijímače TD/TW hlásí dva proudy VFR (jeden na pásmo); **Rx VFR** (na
  přijímačích TD/TW/AP/AP Plus) naopak počítá všechny dobré rámce bez ohledu
  na to, ve kterém pásmu přišly — sledujte právě tento, pokud chcete
  vyhodnocovat jedinou hodnotu VFR.

- **RxBatt** — napětí baterie přijímače.
- **ADC2** — druhý analogový napěťový vstup, na přijímačích, které jej
  podporují.
- **SWR** — SWR antény, při použití externí antény.
- Senzory polohy/pohybu, kde jsou podporovány: **R.Angle**, **P.Angle**,
  **AccX/Y/Z**.

Ke každému číselnému senzoru navíc automaticky vznikají min/max senzory
`<název>-`/`<název>+`, i když nejsou v hlavním seznamu senzorů zobrazeny.

## Vyhledání senzorů {: #discovering-sensors }

![Vyhledávání nových senzorů: zapnuto](../assets/model-telemetry-discover-new-sensors-on.png)

Se vším spárovaným a zapnutým zapněte **Discover new sensors** — blikající
tečka (nebo červená hodnota, pokud ještě nejsou data) označí každý právě
nalezený senzor a obrazovka se automaticky zaplní. Toto je nutné zopakovat
**pro každý model** a znovu vždy, když je přidán nový senzor.

![Vyhledávání nových senzorů: vypnuto](../assets/model-telemetry-discover-new-sensors-off.png)

- Po dokončení přepněte vyhledávání zpět na **Off**.
- **Delete all** vymaže všechny senzory, abyste mohli začít znovu.

  ![Senzory smazány](../assets/model-telemetry-sensors-deleted.png)

- **Competition mode** zredukuje telemetrii pouze na RSSI a RxBatt — pro
  soutěže, které povolují jen senzory stavu spojení. Po opětovném vypnutí
  je nutné vysílač vypnout a zapnout, než lze senzory znovu vyhledat.

  ![Potvrzení soutěžního režimu](../assets/model-telemetry-comp-only-confirm.png)

- Telemetrický režim **Bluetooth** se spáruje s telefonní aplikací FrSky
  FreeLink, která umí zobrazovat telemetrii živě a také konfigurovat
  zařízení FrSky, například stabilizované přijímače.

  ![Telemetrie přes Bluetooth](../assets/model-telemetry-bt-option.png)

## Úprava senzoru {: #editing-a-sensor }

![Výběr volby úpravy](../assets/model-telemetry-edit-option-select.png)

Klepnutím na senzor vyvoláte **Edit**, **Move**, **Reset** nebo **Delete**.
Společná pole: **Value** (jen ke čtení), **ID** (Physical + Application ID
a vysílající přijímač), **Name**, **Unit**, **Decimals**, **Range** (pevné
limity škálování — relevantní zejména tehdy, když je senzor použit jako
zdroj kanálu), **Write logs**, **Reset** (zdroj, který tento senzor
resetuje) a **Sensor lost warning delay** (úplně vypnout, nebo 1–30 s,
výchozí 10 s, pro odfiltrování krátkých výpadků — mějte na paměti riziko
příliš vysokého nastavení; hlášení „sensor lost“ se přehraje jen jednou,
i když vypadne mnoho senzorů zároveň; u interních senzorů přijímače je
výchozí stav vypnuto, protože ty zmizí jen zřídka).

Některé senzory přidávají vlastní pole:

- **ADC2** — **Ratio** a **Offset** pro korekci škálování.

  ![Úprava senzoru ADC2](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — prahy **Critical value** a **Low value warning**.
- **VFR** — **Low value warning** (výchozí 50 %).
- **VSpeed** (vertikální rychlost varia) — **Range** až ±100 m/s (výchozí
  ±10 m/s). Samotné chování zvuku varia se nyní nastavuje ve [speciální
  funkci Play Vario](special-functions.md), nikoli zde.

  ![Úprava senzoru VSpeed](../assets/model-telemetry-edit-vspeed-sensor.png)

## Vlastní / senzory jiných výrobců

![Vytvoření DIY senzoru](../assets/model-telemetry-diy-sensor-select.png)

**Create DIY Sensor** přidá senzor jiného výrobce než FrSky ručně: **Auto
detect** (pokud je to možné, automaticky vyplní Physical ID, Application ID
a modul), nebo je nastavte ručně, dále **Protocol decimals/unit**
(příchozí přesnost, 0–3 desetinná místa, a nativní jednotka) a **Display
decimals/unit** (nezávislé na těch protokolových) společně se stejnými poli
**Range**/**Ratio**/**Offset**/**Write logs**/**Reset**/**Sensor lost
warning delay** jako u každého jiného senzoru.

![Automatická detekce DIY senzoru](../assets/model-telemetry-diy-sensor-auto-detect.png)

## Vypočítané senzory {: #calculated-sensors }

![Vytvoření vypočítaného senzoru](../assets/model-telemetry-calculated-sensor-select.png)

Odvození nového senzoru z jednoho či více existujících:

- **Consumption** — odebraná energie, integrovaná z proudového senzoru
  (např. série FAS). Jednotka mAh/Ah, rozsah až 1000 Ah.

  ![Senzor odběru](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Distance** — ze zdroje GPS (plus zdroj výšky pro 3D vzdálenost).
  Jednotky cm/m/km/ft, až 20 km.

  ![Senzor vzdálenosti](../assets/model-telemetry-calculated-sensor-distance.png)

- **Trip** — nasčítaná vzdálenost mezi po sobě jdoucími pozicemi GPS. Stejné
  jednotky, až 1000 km.

  ![Senzor trasy](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — kaskádovitě spojí dva nebo více napěťových senzorů Lipo
  pro sledování sad větších než 6S (až 67,2 V/8S). Vyberte jednotlivé
  článkové senzory od nejnižšího k nejvyššímu; u každého dalšího senzoru
  Lipo je nejprve nutné změnit Physical **i** Application ID
  v [Konfiguraci zařízení](../system-setup/devices.md) (pomůže tamní
  nástroj Lipo Voltage), vyhledat je po jednom a přejmenovat, aby byly
  rozlišitelné.

  ![Senzor Multi Lipo](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Percent** — přepočítá senzor na 0–100 %, s volbou **Invert** (např. pro
  zobrazení *zbývajícího* procenta namísto odebraného).

  ![Procentní senzor](../assets/model-telemetry-calculated-sensor-percent.png)

- **Power** — výkon ve wattech z páru zdrojů **Current** a **Voltage**, až
  1 000 000 W.

  ![Senzor výkonu](../assets/model-telemetry-calculated-sensor-power.png)

- **Custom** — libovolný vzorec zřetězený z jednoho či více zdrojů.

Každý vypočítaný senzor má navíc volbu **Persistent** (přežije vypnutí či
změnu modelu, při dalším použití se znovu načte) a tlačítko **Reset** přímo
na obrazovce úprav.

### Vlastní senzory

![Vlastní senzor](../assets/model-telemetry-edit-custom-sensor.png)

Začíná se jedním zdrojem, pak **Add** zřetězí další operace: **Add(+)**,
**Minus(-)**, **Multiply(×)**, **Divide(/)**, **Min**, **Max**, **Sqrt**.
Jednotky lze vybrat z dlouhého seznamu zahrnujícího napětí, proud,
kapacitu, výkon, vzdálenost, rychlost, čas, teplotu, procenta, úhly, tlak a
další; rozsah −1 000 000 až 1 000 000, 0–4 desetinná místa.

![Přidání výpočetního řádku](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "Špičkový výkon"
    Vynásobte napěťový senzor (`VFAS`) proudovým senzorem (`Current`), poté
    přidejte krok **Max** odkazující na aktuální hodnotu samotného senzoru
    (`MaxPower`), abyste sledovali nejvyšší zaznamenanou hodnotu — v tomto
    příkladu 288 W:

    ![Příklad MaxPower](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "Aritmetika s konstantou"
    Zdroj nastaven na `RSSI 2.4G` (hodnota 64 dB), poté akce **Subtract**,
    jejíž vlastní zdroj byl dlouze stisknut a použita volba **Convert to
    value**, což jej změní na upravitelnou konstantu (20) místo živého
    zdroje — výsledkem je stálých 44 dB (64 − 20):

    ![Příklad odečtení](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![Convert to value](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "Interní hodnota zdroje"
    Každý [zdroj](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    má interní celočíselný rozsah ±1024, který odpovídá zobrazovanému
    rozsahu ±100 % — je to přímo viditelné, když vlastní senzor nasměrujete
    například na plyn: plný plyn se interně zobrazí jako **+1024**, plný
    záporný výchyl jako **−1024**.

    ![Interní hodnota na maximu](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![Interní hodnota na minimu](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
