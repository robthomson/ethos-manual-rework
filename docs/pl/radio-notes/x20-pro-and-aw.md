---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![Kontrola sprzętu X20 Pro](../assets/system-hardware-check-x20pro.png)

Różnice względem bazowego modelu X20S, dla którego napisano niniejszą
instrukcję — dotyczą one **X20 Pro** i w większości odnoszą się także do
**X20 Pro AW** oraz rodziny **X20R/RS**.

- **Pamięć masowa** — domyślnie wewnętrzna pamięć eMMC 8 GB, SD card
  opcjonalnie — zobacz [Ogólne → Lokalizacja
  pamięci](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **Dodatkowe trymy** — dodaje przełączniki trymu **T5** i **T6** — zobacz
  [Trymy](../model-setup/trims.md#trim-settings).
- **Dodatkowe przełączniki** — dwa zatrzaskowe przyciski, **K** i **L**,
  na tylnych ramionach obudowy, a także pozycje przełączników **M**/**N**,
  jeśli zostały podłączone (zwykle przełączniki w końcówkach drążków) —
  zobacz [Sprzęt →
  Przełączniki](../system-setup/hardware.md#switches-settings).
- **Dodatkowe potencjometry** — **Ext1**/**Ext2**, zwykle używane z
  agregatami 3-osiowymi — zobacz [Sprzęt →
  Potencjometry/Suwaki](../system-setup/hardware.md#potssliders-settings).
  Przesuwa to indeks w [inspektorze wartości ADC](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 znajdują się pomiędzy Pot2 a suwakami.
- **Sprzężenie haptyczne** — **X20 Pro AW** i **X20RS** są dostarczane z
  agregatami MC20R z wbudowanymi silnikami wibracyjnymi drążków; **X20 Pro**
  lub **X20R** może uzyskać tę samą funkcję dzięki modernizacji do agregatów
  MC20R, włączanej w [Sprzęt → Włączanie modernizacji agregatów
  haptycznych](../system-setup/hardware.md#radio-specific-hardware-options).
  Po włączeniu opcja [Wybierz silniki
  haptyczne](../model-setup/special-functions.md#actions) oferuje ustawienia:
  Domyślne, Wszystkie silniki, Lewy drążek lub Prawy drążek.
- **Enkoder obrotowy** — X20 Pro AW oraz X20R/RS wykorzystują bardziej
  czuły enkoder; opcja **połowa kroków** w [Sprzęt → Opcja
  enkodera](../system-setup/hardware.md#radio-specific-hardware-options)
  zmniejsza jego czułość.
- **Wewnętrzny moduł RF** — X20 Pro/R/RS wykorzystują moduł **TD-ISRM Pro**
  (obsługujący LoRa, z trybami tandem dual-band i TD-Pro oprócz
  ACCESS/ACCST D16), a nie moduł TD-ISRM stosowany w
  X18/X20/X20S/X20HD — zobacz [System RF](../model-setup/rf-system.md).
