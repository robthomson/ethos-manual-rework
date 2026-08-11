---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Baterie

![Nastavení baterie vysílače](../assets/system-battery.png)

Kalibruje měření interní baterie vysílače a nastavuje mezní hodnoty alarmů — nezávisle na nastavení letové baterie modelu (viz [Praktický návod: Varování při nízkém napětí baterie](../how-to/low-battery-warning.md)).

- **Hlavní napětí** — zobrazuje aktuální hodnotu a zároveň slouží ke kalibraci: zadejte skutečné napětí změřené multimetrem. Výchozí hodnota je 8,4 V (plně nabitý 2S Li-ion pack).
- **Nízké napětí** — mezní hodnota alarmu, výchozí 7,2 V (7,4 V poskytuje větší rezervu). Je-li zapnuté [Upozornění na hlavní napětí](alerts.md), pokles pod tuto hodnotu vyvolá výstražný dialog a každou minutu hlasové upozornění „Radio battery is low“, ať už je dialog otevřený, nebo ne.

  !!! warning
      Jakmile se toto upozornění ozve, přistávejte a nabijte baterii vysílače — opakuje se každou minutu bez ohledu na cokoli. Při 6,0 V se vysílač bezpodmínečně vypne, aby ochránil články 2×3,0 V Li-ion.

- **Rozsah zobrazovaného napětí** — minimum/maximum pro grafický indikátor baterie v pravém horním rohu: MIN je hodnota, při níž zhasne první segment, MAX je hodnota, při níž se rozsvítí čtvrtý. Výchozí hodnoty jsou 6,4–8,4 V pro vestavěný Li-ion pack; mnoho pilotů zvyšuje dolní hranici, aby dostali varování o nízkém napětí dříve a předešli přílišnému vybití. Nastavte tyto hodnoty podle skutečně použitého typu baterie.
- **Napětí RTC** — napětí knoflíkové baterie hodin reálného času. U nové je 3,0 V; pod 2,7 V ji vyměňte, aby hodiny šly přesně, a pod 2,5 V očekávejte [upozornění na napětí RTC](alerts.md).
