---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Počáteční nastavení vysílače

Jednorázové nastavení, které je třeba provést před programováním
jakéhokoli modelu. Všechny následující [Návody](index.md) předpokládají,
že je hotové.

!!! note
    Tyto návody nejsou přísným kuchařkovým postupem — předpokládají
    základní RC slovník a schopnost pohodlně se orientovat v menu Ethos.
    Pokud je zde něco nejasné, projděte si nejprve [Uživatelské rozhraní a
    navigace](../getting-started/user-interface-and-navigation.md).

## Krok 1. Nabijte baterii vysílače a letové baterie

Baterii vysílače nabijte podle pokynů dodaných s vysílačem a letové
baterie nabíječkou vhodnou pro jejich chemii — u lithiových sad
postupujte se zvláštní opatrností.

## Krok 2. Zkalibrujte hardware

Zkontrolujte, že byla provedena [kalibrace
hardwaru](../system-setup/hardware.md#analogs-calibration) (spouští se
automaticky při prvním zapnutí), aby vysílač znal přesný střed a krajní
polohy každého kniplu, potenciometru a posuvníku. Kalibraci zopakujte
v nabídce **System → Hardware** vždy, když je knipl, potenciometr nebo
posuvník vyměněn.

## Krok 3. Proveďte nastavení systému vysílače

[Nastavení systému](../system-setup/index.md) zahrnuje vše, co je společné
všem modelům, na rozdíl od nastavení pro jednotlivé modely v
[Nastavení modelu](../model-setup/index.md). Většina výchozích hodnot je
pro začátek v pořádku, ale zkontrolujte:

- **[Datum a čas](../system-setup/date-and-time.md)** — nastavte správně.
- **[Audio → Volba hlasů](../system-setup/general.md#audio-settings)** —
  nastavte hlasová hlášení, včetně případných vlastních zvukových
  souborů.
- **[Ovládací prvky (páčky)](../system-setup/controls.md)**:
  - **Režim páček** — Mode 1 (plyn/křidélka vpravo, výškovka/směrovka
    vlevo) nebo Mode 2 (plyn/směrovka vlevo, křidélka/výškovka vpravo —
    výchozí nastavení Ethos).

    !!! warning
        Pokud je model nastaven pro jeden režim páček, zatímco vysílač je
        nastaven na druhý, může se elektromotor rozběhnout v okamžiku
        zapnutí přijímače.

  - **Pořadí kanálů** — Ethos používá jako výchozí **AETR** (křidélka,
    výškovka, plyn, směrovka); konvence Spektrum/JR je **TAER**,
    Futaba/Hitec používá **AETR**. Tímto se určuje pořadí, v jakém jsou
    přiřazovány vstupy páček při vytvoření nového modelu — u jednotlivých
    modelů lze později provést úpravy.

    !!! note "Stabilizované přijímače FrSky"
        Tyto přijímače vyžadují konkrétně **AETR**. Pokud je na jednu
        funkci více ploch (např. 2 křidélka), průvodce je normálně
        seskupí (výsledkem je **AAETR**) — přijímače SRx však očekávají
        **AETRA**/**AETRAE**, proto v nastavení páček zapněte **[První
        čtyři kanály
        fixní](../system-setup/controls.md#first-four-channels-fixed)**,
        aby první čtyři kanály zůstaly za všech okolností v přísném
        pořadí AETR.

- **[Baterie](../system-setup/battery.md)** — nastavte **hlavní napětí**,
  **nízké napětí** a **rozsah zobrazovaného napětí** tak, aby odpovídaly
  skutečné baterii vysílače.
- **[Registrační ID vlastníka](../model-setup/rf-system.md#owner-registration-id)**
  — používají jej přijímače ACCESS a je společné pro více vysílačů kvůli
  funkci Smart Share. Konfiguruje se v Nastavení modelu, ale v praxi
  funguje jako systémové nastavení, protože jej používá každý nový model
  (v případě potřeby jej lze při registraci změnit pro jednotlivé
  přijímače).

!!! note "Jednotky"
    Ethos nemá globální přepínač metrických/imperiálních jednotek —
    [jednotky telemetrických
    senzorů](../model-setup/telemetry.md#editing-a-sensor) se nastavují
    individuálně, pro každý senzor zvlášť.
