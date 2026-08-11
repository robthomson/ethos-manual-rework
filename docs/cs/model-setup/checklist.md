---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Kontrolní seznam

![Kontrolní seznam](../assets/model-checklist.png)

Sada předletových bezpečnostních kontrol, které se provedou při zapnutí
vysílače a/nebo při načtení modelu. Vestavěné kontroly zahrnují tichý
režim, nenastavený failsafe, polohy přepínačů/potenciometrů, baterii
vysílače a baterii RTC — kontrola přepínačů zobrazuje, kterým směrem je
třeba každý přepínač přesunout, což je na varovné obrazovce vyznačeno
červenými body:

![Kontrolní seznam při startu](../assets/model-checklist-at_start.png)

!!! note
    Stiskem `OK` nebo `RTN` se předletové kontroly zcela přeskočí, bez
    ohledu na to, co varování na obrazovce naznačuje.

## Kontrola plynu

![Funkce kontroly](../assets/model-checklist-check_function.png)

Zapněte kontrolu a zvolte operátor — `<` (menší než), `~` (přibližně
rovno) nebo `>` (větší než) — vůči zadané hodnotě; varování se zobrazí,
pokud je páčka plynu mimo rozsah, který dané porovnání povoluje.

## Kontrola failsafe

Varuje, pokud pro aktuální model nebyl nastaven
[failsafe](rf-system.md#failsafe).

!!! tip
    Důrazně doporučujeme ponechat tuto kontrolu zapnutou.

## Kontrola přepínačů

![Přepínače](../assets/model-checklist-switches.png)
![Možnosti kontroly přepínačů](../assets/model-checklist-switches-options.png)

Pro každý přepínač lze vyžadovat konkrétní polohu při startu (přepínače
s vlastními názvy z [Nastavení systému →
Hardware](../system-setup/hardware.md#switches-settings) se zobrazují pod
těmito názvy). Volba **Načíst všechny polohy přepínačů** zaznamená
*aktuální* fyzické polohy jako požadované pro všechny přepínače, které
nejsou označeny jako **Bez kontroly**.

## Kontrola funkčních přepínačů

![Funkční přepínače](../assets/model-checklist-function-switches.png)
![Možnosti kontroly funkčních přepínačů](../assets/model-checklist-function-switches-options.png)

Stejný princip, ale pro šest [funkčních
přepínačů](model-edit.md#function-switches). Volba **Načíst všechny
polohy funkčních přepínačů** funguje stejně jako výše.

## Kontrola potenciometrů / posuvníků

![Potenciometry](../assets/model-checklist-pots.png)
![Možnosti kontroly potenciometrů](../assets/model-checklist-pots-options.png)

Vyžaduje při startu konkrétní polohy potenciometrů/posuvníků, a to
jednotlivě pro každý ovladač (`~`/`<`/`>`, stejně jako u kontroly plynu).
Volba **Načíst všechny polohy potenciometrů** zaznamená aktuální polohy
automaticky — poté si pečlivě zkontrolujte automaticky vybrané operátory,
protože `~` versus `<`/`>` nemusí odpovídat vašemu skutečnému záměru.

## Uživatelsky definovaný text

![Uživatelský text kontrolního seznamu](../assets/model-checklist-user-checklist.png)

Zobrazí soubor s prostým nebo formátovaným textem jako součást startovního
kontrolního seznamu, jakmile je pro daný model nainstalován. Kompletní
postup nastavení najdete v části [Praktický návod: Uživatelsky definovaný
textový kontrolní seznam](../how-to/user-defined-checklist.md).
