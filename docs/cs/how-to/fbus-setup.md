---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Konfigurace systému FBUS

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (dříve
F.Port2) sdružuje řízení a telemetrii na jedné lince, takže několik
zařízení FBUS může sdílet jediné sériově zapojené (daisy-chain) spojení
s plnou bezdrátovou konfigurací. Tento postup zapojí dvě serva Xact na
kanály křidélek (1 a 5) v [základním příkladu pro motorové
letadlo](../tutorials/basic-fixed-wing.md).

!!! note "Snímky obrazovky budou doplněny"
    Tato stránka zatím neobsahuje snímky obrazovky ze simulátoru — viz [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## 1. Stáhněte nejnovější firmware

FBUS vyžaduje aktuální firmware v přijímači i v zařízeních — např. servа
Xact potřebují verzi v2.0.1 nebo novější. Příslušné aktualizace najdete na
[stránce ke stažení FrSky](https://www.frsky-rc.com/download/).

## 2. Nahrajte firmware

Zkopírujte soubory firmwaru do adresáře `Firmware/` na SD card/eMMC.
V [Souborovém manažeru](../system-setup/file-manager.md) připojte servo
ke konektoru S.Port vysílače (bílý/žlutý vodič směrem k zářezu), vyberte
soubor firmwaru a zvolte **Flash External Device**.

## 3 / 5. Nastavení Physical ID

Obě serva mají ve výchozím stavu Physical ID `0C` hex / Application ID
`6800` hex — na sdílené sběrnici by si vzájemně kolidovala, dokud jedno
z nich nezměníte. Podle typu přijímače existují dvě možnosti:

**Přes konektor S.Port vysílače** (jakýkoli přijímač):

1. Připojte servo 1, přejděte do **Device Config → XAct** a nastavte
   **Module** na **S.Port connector**. Physical ID `0C`/Application ID
   `6800` a kanál `CH1` ponechte ve výchozím nastavení, poté zvolte
   **Save to flash**.
2. Připojte místo něj servo 2 a otevřete stejnou nabídku. Změňte
   **Physical ID** na `0D` hex a **Application ID** na `6801` hex
   (v [tabulce Physical ID](../model-setup/telemetry.md#how-frsky-telemetry-works)
   zjistíte, které pozice jsou volné), nastavte **Channel** na `CH5` a
   zvolte **Save to flash**.

**Přímo přes přijímač** (např. TD-R18 Tandem, kde jsou obě serva zapojena
současně — viz [krok 4](#4-configure-the-receiver-for-fbus)):

1. Připojte pouze servo 1 (např. na Pin1 přijímače), přejděte do
   **Device Config → XAct** a nastavte **Module** → **Internal module**.
   Potvrďte výchozí hodnoty (`0C`/`6800`/`CH1`) a zvolte
   **Save to flash**.
2. Připojte pouze servo 2 (Pin5) a otevřete stejnou nabídku (Device
   Config komunikuje vždy jen s jedním servem) — změňte hodnoty na
   `0D`/`6801`/`CH5` a zvolte **Save to flash**. Poté znovu otevřete
   Device Config a ověřte, že se změna uložila.

## 4. Nastavení přijímače pro FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [RF systém](../model-setup/rf-system.md) → tlačítko
přijímače → **Options** → nastavte **Telemetry Port** na **FBUS**. Serva
Xact se pak na tento port zapojují sériově; protože každé servo má jen
jeden konektor, rozvětvení k několika servům zajistí vícekanálový
rozbočovač F.Port2 (FP2CH4/6/8).

**TD-R18 Tandem**: RF systém → tlačítko přijímače → **Options** →
nastavte jednotlivé piny (např. **Pin1**, **Pin5**) na **FBUS** — tímto
způsobem lze přiřadit libovolný počet pinů a rozbočovače tak nejsou
vůbec potřeba; každý pin přiřazený k FBUS vede identický signál FBUS.

## 5. Kontrola řízení serv přes FBUS

Připojte servo 1 na Pin1 a servo 2 na Pin5 (kanály křidélek z příkladu
motorového letadla), zapněte napájení a ověřte, že kanály 1 a 5 pohybují
správnými servy.

## 6. Kontrola telemetrie FBUS

S oběma připojenými servy odstraňte veškeré existující senzory `SRV`
v [Telemetrii](../model-setup/telemetry.md) a spusťte nové vyhledání.
Každé servo hlásí 4 senzory: proud, napětí, teplotu a stav (`OK` při
běžném provozu).

## 7. Pozdější změny konfigurace

Jakmile je model kompletně zapojen, není praktické izolovat jedno servo
kvůli přenastavení přes Device Config. Postupujte místo toho takto:
přejděte do Telemetrie, najděte senzor patřící danému servu (např.
`SRV1 curr`) a zvolte **Configure** — otevře se přímo konfigurace tohoto
serva. Po každé změně zvolte **Save to flash**.

!!! warning
    Na této obrazovce nezměňte omylem Physical ID nebo Application ID —
    právě tyto hodnoty umožňují adresovat jednotlivá serva na sdílené
    sběrnici.
