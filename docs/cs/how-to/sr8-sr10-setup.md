---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Nastavení modelu pro SR8/SR10 a změna pořadí kanálů

Stabilizované přijímače FrSky řady SRx očekávají určité pořadí kanálů. Existují
dva scénáře: vytvoření nového modelu pro takový přijímač od začátku, nebo
úprava existujícího modelu tak, aby tomuto pořadí odpovídal.

!!! note "Snímky obrazovky budou doplněny"
    Tato stránka zatím neobsahuje snímky obrazovek ze simulátoru — viz [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## Vytvoření nového modelu

Průvodce v [Výběru modelu](../model-setup/model-select.md) ve výchozím
nastavení seskupuje plochy se stejnou funkcí (např. 2 křidélka → `AAETR`),
stabilizované přijímače SRx však potřebují první čtyři kanály pevně nastavené
jako **AETRA**.

1. V nabídce [Ovládací prvky](../system-setup/controls.md) zkontrolujte, že
   **Pořadí kanálů** je `AETR`.
2. Zapněte **[První čtyři kanály
   pevně](../system-setup/controls.md#first-four-channels-fixed)** — tím
   zabráníte průvodci ve seskupování prvních čtyř kanálů a ty zůstanou striktně
   v pořadí `AETRA…` bez ohledu na to, kolik jednotlivých ploch daný model má.
3. Spusťte průvodce vytvořením modelu jako obvykle — prvních 5 kanálů vyjde
   v pořadí `AETRA`.

!!! note "Autotest přijímačů Archer"
    Autotest přijímačů Archer se nyní provádí přes [Konfigurace zařízení →
    SxR](../system-setup/devices.md) (firmware v2.1.10 a novější), nikoli
    samostatnou procedurou autotestu. Kanál plynu musí být na −100 %, jinak se
    autotest nespustí.

## Změna pořadí kanálů u existujícího modelu

Převod existujícího modelu (např. se současným pořadím `AAETRFF`) na pořadí pro
stabilizovaný přijímač (`AETRAE`, dále kanál 9 zesílení, 10/11 letové režimy,
12 autotest u starších jednotek SxR) představuje sérii prohození kanálů
v nabídce [Výstupy](../model-setup/outputs.md#swap-channels).

Výchozí stav:

| Kanál | Funkce |
|---|---|
| 1 | Křidélko1 (pravé) |
| 2 | Křidélko2 (levé) |
| 3 | Výškovka |
| 4 | Plyn |
| 5 | Směrovka |
| 6 | Klapka1 (pravá) |
| 7 | Klapka2 (levá) |
| 8 | Zatahovací podvozek |

Cílové pořadí: `AETRAE` — kanál 1 křidélko1, kanál 2 výškovka, kanál 3 plyn,
kanál 4 směrovka, kanál 5 křidélko2, kanál 6 výškovka2/AUX2 (dále zesílení,
letové režimy a autotest na kanálech 9–12).

1. **Nejprve uvolněte místo přesunem křidélka2**: ve Výstupech vyberte CH2
   (křidélko2), znovu na něj klepněte, zvolte **Swap Channels** a prohoďte jej
   s nepoužitým kanálem (např. CH9). Prohození se provede okamžitě — všechny
   mixy odkazující na některý z těchto kanálů se automaticky aktualizují.
2. **Prohoďte CH3 (výškovka) → CH2.**
3. **Prohoďte CH4 (plyn) → CH3.**
4. **Prohoďte CH5 (směrovka) → CH4.**
5. **Prohoďte CH9 (křidélko2 odložené v kroku 1) → CH5.**

Výsledek:

| Kanál | Funkce |
|---|---|
| 1 | Křidélko1 (pravé) |
| 2 | Výškovka |
| 3 | Plyn |
| 4 | Směrovka |
| 5 | Křidélko2 (levé) |
| 6 | Klapka1 (pravá) |
| 7 | Klapka2 (levá) |
| 8 | Zatahovací podvozek |

— tedy pořadí, které stabilizované přijímače FrSky očekávají.
