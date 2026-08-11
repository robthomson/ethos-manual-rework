---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Bedieningsorganen

![Sticks](../assets/system-sticks.png)

In het menu **Sticks** genoemd — stickmodus en de standaard volgorde van de
kanaaltoewijzing.

## Stickmodus

- **Mode 1** — gas en rolroer op de rechterstick, hoogteroer en
  richtingsroer op de linker.
- **Mode 2** — gas en richtingsroer op de linkerstick, rolroer en hoogteroer
  op de rechter.

De sticks zijn standaard benoemd volgens de in de industrie gangbare modi en
kunnen worden hernoemd.

## Kanaalvolgorde

Bepaalt in welke volgorde de vier stickingangen aan kanalen worden toegewezen
wanneer een nieuw model wordt opgebouwd met de wizards van
[Modelkeuze](../model-setup/model-select.md). Standaard is **AETR**. Wanneer een
vliegtuigconfiguratie meer dan één van een bepaald stuurvlak heeft, worden deze
gegroepeerd, tenzij [Eerste vier kanalen
vast](#first-four-channels-fixed) is ingeschakeld — bijvoorbeeld 2 rolroeren
wordt **AAETR**.

![Kanaalvolgorde ontvanger](../assets/system-sticks-rx-order.png)

## Eerste vier kanalen vast {: #first-four-channels-fixed }

Als dit is ingeschakeld, worden de eerste vier kanalen nooit gegroepeerd. Met de
volgorde **AETR** en een vliegtuigconfiguratie met 2 rolroeren, 1 hoogteroer,
1 motor, 1 richtingsroer en 2 flaps produceert de wizard **AETRAFF** (kanalen
1–4 blijven exact A-E-T-R, waarbij het tweede rolroer en beide flaps erachter
worden toegevoegd) in plaats van **AAETRFF**. Dit is de instelling waarmee de
wizard modellen opbouwt die geschikt zijn voor SRx-gestabiliseerde ontvangers,
die deze vaste indeling verwachten.

![Vaste volgorde 4 kanalen](../assets/system-sticks-4ch-fixed.png)
