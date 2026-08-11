---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Natychmiastowe przejęcie sterowania w funkcji Trainer

Przydatne rozszerzenie funkcji [Trainer](../model-setup/trainer.md):
zamiast wyłącznie przełącznika, instruktor może natychmiast odzyskać
sterowanie, po prostu poruszając drążkiem lotek lub steru wysokości —
nie trzeba najpierw szukać przełącznika trainer, gdy coś pójdzie nie tak.

Sesję nadal rozpoczyna przełącznik trainer; samą funkcją Trainer steruje
[przełącznik logiczny typu Sticky](../model-setup/logical-switches.md#sticky),
anulowany przez wyłączenie przełącznika **albo** przez wykrycie ruchu
drążka instruktora.

![Trainer aktywny](../assets/trainer-take-back-trainer-active.png)

## 1. Przełącznik logiczny wykrywający lotki

![Wykrywanie sygnału lotek](../assets/trainer-take-back-ailinput.png)

Przełącznik logiczny wykorzystujący warunek **|A| > X** na drążku lotek,
prawdziwy, gdy drążek zostanie wychylony o więcej niż 10% od pozycji
środkowej w dowolnym kierunku. Przytrzymaj dłużej źródło lotek i wybierz
**Ignoruj sygnał trainer**, aby ruch lotkami wykonany przez *ucznia*
(docierający przez łącze trainer) również nie wyzwalał tego warunku:

![Ignoruj sygnał trainer](../assets/trainer-take-back-ailinput-ignore.png)

## 2. Przełącznik logiczny wykrywający ster wysokości

![Wykrywanie sygnału steru wysokości](../assets/trainer-take-back-eleinput.png)

Ten sam schemat, zastosowany do drążka steru wysokości.

## 3. Przełącznik logiczny anulujący

Przełącznik logiczny typu **OR**, prawdziwy, gdy prawdziwy jest
przełącznik wykrywający lotki lub przełącznik wykrywający ster wysokości,
**albo** gdy przełącznik trainer (np. SD) nie jest w dolnym położeniu —
czyli sesję kończy dowolne ze zdarzeń: „instruktor poruszył drążkiem” lub
„przełącznik trainer został wyłączony”.

## 4. Przełącznik logiczny Sticky włączający funkcję Trainer

![Wyłączenie funkcji Trainer](../assets/trainer-take-back-disable-trainer.png)

Przełącznik logiczny typu **Sticky**: **Wyzwalanie ON** to przełącznik
trainer (SD w dół), a **Wyzwalanie OFF** to przełącznik anulujący
z kroku 3. Użyj tego przełącznika Sticky — nazwij go `TrainerActive` —
jako warunku aktywacji funkcji Trainer zamiast samego przełącznika.

## 5. Sygnalizacja dźwiękowa

Dodaj [funkcje specjalne Play Audio](../model-setup/special-functions.md)
ogłaszające moment, w którym `TrainerActive` staje się prawdziwy oraz gdy
zostaje skasowany, dzięki czemu obaj piloci otrzymują wyraźny sygnał
dźwiękowy dokładnie w chwili przekazania sterowania.
