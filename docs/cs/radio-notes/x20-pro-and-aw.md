---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![Kontrola hardwaru X20 Pro](../assets/system-hardware-check-x20pro.png)

Odlišnosti od modelu X20S, který je v této příručce brán jako základ —
platí pro **X20 Pro** a většinou se vztahují také na **X20 Pro AW**
a řadu **X20R/RS**.

- **Úložiště** — ve výchozím stavu interní eMMC 8 GB, SD card volitelně — viz
  [Obecné → Umístění
  úložiště](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **Další trimy** — přidává trimovací přepínače **T5** a **T6** — viz
  [Trimy](../model-setup/trims.md#trim-settings).
- **Další přepínače** — dva tlačítkové přepínače s aretací, **K** a **L**,
  na zadních ramenech, plus pozice přepínačů **M**/**N**, pokud jsou zapojeny
  (typicky přepínače na koncích páček) — viz [Hardware →
  Přepínače](../system-setup/hardware.md#switches-settings).
- **Další potenciometry** — **Ext1**/**Ext2**, typicky používané s tříosými gimbaly
  — viz [Hardware → Potenciometry/Posuvníky](../system-setup/hardware.md#potssliders-settings).
  Tím se posouvají indexy v [prohlížeči hodnot ADC](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 jsou umístěny mezi Pot2 a posuvníky.
- **Haptická odezva** — **X20 Pro AW** a **X20RS** se dodávají s gimbaly MC20R
  s integrovanými vibračními motory v páčkách; **X20 Pro** nebo
  **X20R** může získat totéž dodatečnou výměnou gimbalů za MC20R, což se povoluje
  v [Hardware → Povolení haptických gimbalů](../system-setup/hardware.md#radio-specific-hardware-options).
  Po povolení nabízí [Výběr haptických
  motorů](../model-setup/special-functions.md#actions) možnosti Výchozí,
  Všechny motory, Levá páčka nebo Pravá páčka.
- **Rotační enkodér** — X20 Pro AW a X20R/RS používají citlivější
  enkodér; volba **polovičních kroků** v [Hardware → Volba
  enkodéru](../system-setup/hardware.md#radio-specific-hardware-options)
  jeho citlivost zmírní.
- **Interní RF modul** — X20 Pro/R/RS používají modul **TD-ISRM Pro**
  (s podporou LoRa, s režimy tandem dual-band a TD-Pro navíc
  k ACCESS/ACCST D16) místo modulu TD-ISRM v
  X18/X20/X20S/X20HD — viz [RF systém](../model-setup/rf-system.md).
