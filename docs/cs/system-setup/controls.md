---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Ovládací prvky

![Páčky](../assets/system-sticks.png)

V menu se nazývá **Páčky** — režim páček a výchozí pořadí přiřazení kanálů.

## Režim páček

- **Mode 1** — plyn a křidélka na pravé páčce, výškovka a směrovka na levé.
- **Mode 2** — plyn a směrovka na levé páčce, křidélka a výškovka na
  pravé.

Páčky jsou standardně pojmenovány podle běžně používaných režimů a lze je
přejmenovat.

## Pořadí kanálů

Určuje pořadí, v jakém jsou čtyři vstupy páček přiřazeny ke kanálům při
vytváření nového modelu pomocí průvodců [Výběr modelu](../model-setup/model-select.md).
Výchozí hodnota je **AETR**. Pokud má konstrukce modelu více než jednu
plochu daného typu, jsou tyto plochy seskupeny za sebou — pokud není
zapnuta volba [Prvních čtyři kanály fixní](#first-four-channels-fixed) —
např. 2 křidélka dají **AAETR**.

![Pořadí kanálů přijímače](../assets/system-sticks-rx-order.png)

## Prvních čtyři kanály fixní {: #first-four-channels-fixed }

Je-li tato volba zapnuta, první čtyři kanály se nikdy neseskupují. Při
pořadí **AETR** a konstrukci se 2 křidélky, 1 výškovkou, 1 motorem, 1
směrovkou a 2 klapkami vytvoří průvodce **AETRAFF** (kanály 1–4 zůstanou
přesně A-E-T-R, druhé křidélko a obě klapky se připojí za ně) namísto
**AAETRFF**. Právě toto nastavení zajistí, že průvodce vytvoří modely
vhodné pro stabilizované přijímače SRx, které tento fixní rozvrh
očekávají.

![Fixní pořadí 4 kanálů](../assets/system-sticks-4ch-fixed.png)
