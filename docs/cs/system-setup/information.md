---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Informace

![Systémové informace](../assets/system-info.png)

Podrobnosti o firmwaru systému, typ gimbalů, informace o interním/externím RF modulu,
informace o spárovaném přijímači, doba provozu vysílače, protokoly chyb a obnovení výrobních nastavení.

## Informace o vysílači

- **Serial number** — sériové číslo vysílače.
- **Firmware** — verze Ethos a typ vysílače (např. X20).
- **Firmware Version** — varianta buildu, např. FCC, LBT nebo Flex.
- **Date** — datum a čas vytvoření firmwaru.
- **RAM available** — volná systémová RAM, užitečná pro odhalení chybně
  se chovajícího Lua skriptu; je dostupná také jako systémový [zdroj](../getting-started/user-interface-and-navigation.md#choosing-a-source),
  takže ji lze zobrazit ve widgetu.
- **Sticks** — verze instalovaných Hallových senzorů gimbalů (nebo „ADC“ pro analogové
  gimbaly).
- **Internal Module** — verze hardwaru a firmwaru interního RF
  modulu.
- **Receiver** — údaje o aktuálně spárovaném přijímači, zobrazené za
  interním modulem. Pokud redundantní přijímač využívá stejný slot jako
  hlavní přijímač, oba se na displeji střídají (např. Archer SR10 Pro
  zobrazený spolu se svým redundantním R9MM-OTA pod položkou „Receiver1“).
- **External Module** — údaje o hardwaru a firmwaru připojeného externího
  RF modulu FrSky používajícího protokol ACCESS. Multi-protocol moduly
  se zde nezobrazují.

![Informace X20 Pro](../assets/system-info-x20pro.png)

## Doba provozu vysílače

![Doba provozu vysílače](../assets/system-info-radio-runtime.png)

Sleduje celkovou dobu používání vysílače; volba **Reset** ji vynuluje.

## Chyby

![Chyby](../assets/system-info-errors.png)

Červený trojúhelník v horní liště hlavního zobrazení znamená, že Ethos zaznamenal chybu,
jejíž podrobnosti se zobrazují zde. Příčiny mohou být:

- **Chyby Lua skriptů** — problém ve spuštěném Lua skriptu.
- **Chyba záložní RAM** — model je příliš velký pro RAM určenou pro záložní kopii modelu. Ethos
  tuto oblast rozšířil ze 4 kB na 32 kB, takže je nyní málo pravděpodobné, že k tomu dojde, ale pokud
  ano, jde o významnou chybu: při aktivaci [Emergency
  Mode](../getting-started/emergency-mode.md) se model načítá pomaleji z SD card
  namísto ze záložní RAM.
- **Používání nightly buildu firmwaru** — upozornění, že nightly buildy
  nejsou určeny k létání.

Volba **Reset** vymaže zaznamenané chyby — což je praktické během ladění Lua skriptů.

## Obnovení výrobních nastavení

![Obnovení výrobních nastavení](../assets/system-info-factory-reset.png)

Obnoví vysílač do výrobního nastavení výhradně v samotném zařízení — bez potřeby
připojení k PC.

![Potvrzení obnovení výrobních nastavení](../assets/system-info-factory-reset-confirm.png)

!!! danger
    Potvrzením se vymažou **všechny** modely, protokoly, snímky obrazovky, dokumenty,
    skripty, bitmapy a nastavení vysílače. Průběh mazání sleduje ukazatel průběhu,
    po jehož dokončení se odpojí všechny disky a vysílač se restartuje.

Stránka Info na X20 Pro/R/RS zobrazuje odpovídající informace pro tuto
řadu vysílačů.
