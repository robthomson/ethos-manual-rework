---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Varování při nízkém napětí baterie

Sledování napětí letové baterie **pod zatížením** a upozornění při poklesu
pod stanovenou hranici je spolehlivější přístup než spoléhání se na pevně
nastavený časovač — senzor jako FrSky FLVSS to výrazně usnadňuje.

## 1. Připojení a nalezení senzoru

![Telemetrický senzor LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Nastavte [Možnosti přijímače → Telemetrický
port](../system-setup/devices.md) na **S.Port**, připojte FLVSS
k přijímači pomocí kabelu S.Port a poté v části
[Telemetrie](../model-setup/telemetry.md) spusťte **Hledat nové senzory** —
senzor LiPo se zobrazí společně s ostatními již nalezenými senzory.

## 2. Přidání logického přepínače

![Logický přepínač pro nízké napětí baterie](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Přidejte nový [logický přepínač](../model-setup/logical-switches.md) se
senzorem LiPo jako zdrojem. Dlouhým stiskem `ENT` na zvýrazněném senzoru
vyberete, kterou z jeho hodnot chcete použít:

![Výběr nejnižšího článku](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Min. napětí baterie / Max. napětí baterie
- **Napětí nejnižšího článku** / Napětí nejvyššího článku
- Počet článků
- Napětí jednotlivých článků (lze vybrat pouze v okamžiku, kdy je senzor
  skutečně připojen ke spárovanému přijímači s připojenou baterií LiPo)

Vyberte **Lowest** (napětí článku) — hodnotu, která je rozhodující pro
ochranu typu LVC.

![Vybráno napětí nejnižšího článku](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Nastavte porovnávanou hodnotu na přibližně **3,4 V** a **Zpoždění před
aktivací** na **4 sekundy** — přepínač se přepne do stavu true, jakmile
napětí nejnižšího článku nepřetržitě po dobu 4 s nebo delší klesne pod
3,4 V na článek. (Napětí 3,4 V *pod zatížením* se po odlehčení obvykle
zotaví na přibližně 3,7 V, takže tento limit odráží skutečný pokles
napětí, nikoli pouze okamžitý šum.)

![Dokončený logický přepínač](../assets/how-to-low-batt-lsw-summary.png)

## 3. Přidání speciální funkce

![Speciální funkce: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Přidejte [speciální funkci Přehrát
zvuk](../model-setup/special-functions.md), jako **Podmínku aktivace**
nastavte logický přepínač `BattLow`, vyberte hlas a v části **Sekvence**
přidejte krok **Přehrát hodnotu** pro celkové napětí LiPo:

![Přehrát hodnotu: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Přehled sekvence](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Při nastavení **Opakování** na 10 sekund bude napětí LiPo hlášeno každých
10 s po celou dobu, kdy napětí nejnižšího článku zůstává pod hranicí
3,4 V / 4 s.
