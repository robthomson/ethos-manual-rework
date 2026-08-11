---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ostrzeżenie o niskim napięciu akumulatora

Monitorowanie napięcia pakietu napędowego **pod obciążeniem** i sygnalizowanie
spadku poniżej progu to podejście bardziej niezawodne niż poleganie na stałym
timerze — czujnik taki jak FrSky FLVSS znacznie to ułatwia.

## 1. Podłączenie i wykrycie czujnika

![Czujnik telemetrii LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Ustaw [Opcje odbiornika → Port
telemetrii](../system-setup/devices.md) na **S.Port**, podłącz FLVSS do
odbiornika kablem S.Port, a następnie włącz **Wykryj nowe czujniki** w sekcji
[Telemetria](../model-setup/telemetry.md) — czujnik LiPo pojawi się obok
pozostałych już wykrytych.

## 2. Dodanie przełącznika logicznego

![Przełącznik logiczny niskiego napięcia](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Dodaj nowy [przełącznik logiczny](../model-setup/logical-switches.md) z
czujnikiem LiPo jako źródłem. Przytrzymaj dłużej `ENT` na podświetlonym
czujniku, aby wybrać, której z jego wartości użyć:

![Wybór najniższego ogniwa](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Minimalne napięcie pakietu / Maksymalne napięcie pakietu
- **Najniższe napięcie ogniwa** / Najwyższe napięcie ogniwa
- Liczba ogniw
- Napięcia poszczególnych ogniw (możliwe do wybrania tylko wtedy, gdy czujnik
  jest faktycznie podłączony do zbindowanego odbiornika z dołączonym pakietem
  LiPo)

Wybierz **Najniższe** (napięcie ogniwa) — wartość istotną dla zabezpieczenia
typu LVC.

![Wybrane najniższe ogniwo](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Ustaw wartość porównania na około **3,4 V**, a **Opóźnienie przed aktywacją**
na **4 sekundy** — przełącznik przyjmie stan prawda, gdy napięcie najniższego
ogniwa utrzyma się poniżej 3,4 V przez co najmniej 4 s. (Napięcie 3,4 V *pod
obciążeniem* zwykle wraca do około 3,7 V po zdjęciu obciążenia, więc taki próg
odzwierciedla rzeczywisty spadek, a nie chwilowe zakłócenie.)

![Gotowy przełącznik logiczny](../assets/how-to-low-batt-lsw-summary.png)

## 3. Dodanie funkcji specjalnej

![Funkcja specjalna: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Dodaj [funkcję specjalną Odtwórz dźwięk](../model-setup/special-functions.md),
ustaw **Warunek aktywacji** na przełącznik logiczny `BattLow`, wybierz głos, a
w sekcji **Sekwencja** dodaj krok **Odtwórz wartość** dla całkowitego napięcia
pakietu LiPo:

![Odtwórz wartość: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Podsumowanie sekwencji](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Przy **Powtarzaniu** ustawionym na 10 sekund napięcie pakietu LiPo będzie
wypowiadane co 10 s tak długo, jak długo najniższe ogniwo pozostaje poniżej
progu 3,4 V przez 4 s.
