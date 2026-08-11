---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Výstrahy

![Výstrahy](../assets/system-alerts.png)

Čtyři výstrahy platné pro celý vysílač, každou lze samostatně zapnout či vypnout — jsou oddělené od
[speciálních funkcí](../model-setup/special-functions.md)
a [logických přepínačů](../model-setup/logical-switches.md) definovaných pro jednotlivé modely,
které si vytváříte sami.

- **Tichý režim** — hlasová výstraha při startu, pokud je tato kontrola zapnutá a
  [Obecné → Režim zvuku](general.md) je nastaven na Tichý, jako připomenutí, že je
  vysílač ztišený.
- **Hlavní napětí** — „Radio battery is low“, když napětí hlavní baterie vysílače
  klesne pod mez **Nízké napětí** nastavenou v [Baterii](battery.md).
- **Napětí RTC** — „RTC battery is low“, když napětí knoflíkové baterie RTC klesne
  pod 2,5 V (výchozí mez). Záznam dat závisí na hodinách reálného
  času; neplatný čas činí záznamy obtížně čitelnými, zejména při rozlišování
  jednotlivých letových sezení. Tuto výstrahu lze dočasně ztišit, dokud čekáte na
  výměnu baterie, ale neměla by zůstat trvale vypnutá.
- **Varování o konfliktu senzorů** — detekuje kolidující ID telemetrických senzorů.
  Vypnutí má smysl jen tehdy, pokud používáte senzory, které nesplňují specifikaci
  S.Port.
- **Nečinnost** — hlasová výstraha „Prolonged inactivity“ (spolu s vibračním
  upozorněním pro případ, že je hlasitost stažená) poté, co vysílač zůstal
  nepoužívaný delší dobu, než je nastavený čas — ve výchozím nastavení 10 minut.
