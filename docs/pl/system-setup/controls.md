---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sterowanie

![Drążki](../assets/system-sticks.png)

W menu pozycja ta nosi nazwę **Drążki** — określa tryb drążków oraz
domyślną kolejność przypisania kanałów.

## Tryb drążków

- **Mode 1** — gaz i lotki na prawym drążku, ster wysokości i ster
  kierunku na lewym.
- **Mode 2** — gaz i ster kierunku na lewym drążku, lotki i ster wysokości
  na prawym.

Drążki są domyślnie nazwane zgodnie ze standardowymi trybami branżowymi
i mogą zostać przemianowane.

## Kolejność kanałów

Określa kolejność przypisywania czterech wejść drążków do kanałów podczas
tworzenia nowego modelu przez kreatory [Wyboru modelu](../model-setup/model-select.md).
Wartością domyślną jest **AETR**. Jeżeli płatowiec ma więcej niż jedną
powierzchnię danego typu, są one grupowane razem, chyba że włączona jest
opcja [Pierwsze cztery kanały stałe](#first-four-channels-fixed) — np. 2 lotki dają
**AAETR**.

![Kolejność kanałów odbiornika](../assets/system-sticks-rx-order.png)

## Pierwsze cztery kanały stałe {: #first-four-channels-fixed }

Gdy opcja jest włączona, pierwsze cztery kanały nigdy nie są grupowane.
Przy kolejności **AETR** i płatowcu z 2 lotkami, 1 sterem wysokości,
1 silnikiem, 1 sterem kierunku i 2 klapami kreator utworzy układ **AETRAFF**
(kanały 1–4 pozostają dokładnie w kolejności A-E-T-R, a druga lotka i obie
klapy zostają dodane na końcu) zamiast **AAETRFF**. To właśnie to ustawienie
sprawia, że kreator tworzy modele odpowiednie dla odbiorników
stabilizowanych SRx, które oczekują takiego stałego układu.

![Stała kolejność 4 kanałów](../assets/system-sticks-4ch-fixed.png)
