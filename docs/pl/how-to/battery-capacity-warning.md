---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ostrzeżenie o pojemności akumulatora

Ostrzeżenie oparte na **zużytej pojemności** (mAh), a nie na napięciu — jest to
bardziej bezpośrednia miara tego, ile pakietu faktycznie zostało wykorzystane.
Istnieją dwa sposoby na osiągnięcie tego celu, zależnie od zamontowanego sprzętu.

## Opcja A: regulator z serii Neuron

Regulatory Neuron firmy FrSky raportują zużycie bezpośrednio — nie jest potrzebny
czujnik obliczany. Ustaw [Opcje odbiornika → Port
telemetrii](../system-setup/devices.md) na S.Port, podłącz przewód telemetrii
regulatora Neuron i [wyszukaj
czujniki](../model-setup/telemetry.md#discovering-sensors) — interesującym nas
czujnikiem jest **ESC Consumption**.

1. Dodaj [przełącznik logiczny](../model-setup/logical-switches.md) na `ESC
   Consumption`, prawdziwy powyżej (przykładowo) 900 mAh — to mniej więcej 60%
   pakietu dobranego tak, by lądować z ok. 30% rezerwy.
2. Dodaj [funkcję specjalną Odtwórz
   dźwięk](../model-setup/special-functions.md), z warunkiem aktywności ustawionym
   na nowy przełącznik i krokiem **Odtwórz wartość** dla `ESC Consumption`.

Jako druga linia obrony: regulatory Neuron raportują również **ESC Voltage** —
skonfiguruj drugi przełącznik logiczny w taki sam sposób, jak w [Ostrzeżeniu o
niskim napięciu akumulatora](low-battery-warning.md) (poniżej 3,4 V na celę —
np. 13,6 V dla pakietu 4S), z własną funkcją Odtwórz dźwięk powtarzaną co 5
sekund.

## Opcja B: czujnik prądu + czujnik obliczany

Jeśli regulator nie raportuje zużycia, to samo zadanie spełni czujnik prądu
(np. FrSky FASxxx) połączony z [czujnikiem obliczanym
**Consumption**](../model-setup/telemetry.md#calculated-sensors).

### 1. Podłączenie i wyszukanie

![Czujnik prądu](../assets/how-to-consumption-telemetry-current-sensor.png)

Podłącz przewód S.Port czujnika prądu i wyszukaj go — pojawi się jako
**Current**. Ustaw jego **Zakres** zgodnie z parametrami czujnika (np. 0–100 A
dla FAS100):

![Edycja czujnika prądu](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Utworzenie czujnika obliczanego Consumption

![Tworzenie czujnika obliczanego](../assets/how-to-consumption-create-calc-select.png)
![Czujnik Consumption](../assets/how-to-consumption-create-calc-sensor.png)

W menu Telemetria wybierz **Utwórz czujnik obliczany** → **Consumption**. Ustaw
jednostki na `mAh`, a **Zakres** na pojemność pakietu (np. 2800 mAh);
**Źródło** ustaw na `Current`.

![Edycja czujnika](../assets/how-to-consumption-sensor-edit.png)
![Edycja czujnika 2](../assets/how-to-consumption-sensor-edit2.png)

Ustaw **Reset** na zdarzenie systemowe `!Telemetry Active` — wybierz **Telemetry
Active**, przytrzymaj `ENT` i wybierz **Invert** — dzięki temu bieżąca suma
zostanie automatycznie wyzerowana, gdy telemetria zaniknie (czyli po wyłączeniu
zasilania modelu).

### 3. Komunikaty progowe

![Przełącznik logiczny Δ 200 mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Dodaj przełącznik logiczny wykorzystujący funkcję **Δ > X** na `Consumption`,
wyzwalany za każdym razem, gdy wartość wzrośnie o ustalony krok — np. co 200 mAh,
co stanowi wygodny ułamek pakietu 2800 mAh.

!!! tip
    Ustaw **Interwał sprawdzania** na `---` (nieskończony), aby wartość
    kumulowała się w nieskończoność do kolejnego progu, zamiast zerować się po
    upływie ustalonego okna. Podczas testowania nadaj **Min. czasowi trwania**
    niewielką wartość różną od zera — przy 0.0 wyzwolenie jest zbyt krótkie, by
    dało się je zauważyć na ekranie.

Dodaj funkcję Odtwórz dźwięk z warunkiem aktywności ustawionym na ten
przełącznik i krokiem Odtwórz wartość dla `Consumption`:

![Odtwarzanie komunikatu przyrostowego](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Odtwórz wartość: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Ostrzeżenie o niskiej pojemności

![Drugi przełącznik logiczny](../assets/how-to-consumption-lsw2-play-battlow.png)

Drugi przełącznik logiczny wyzwala się jednorazowo po przekroczeniu twardego
progu niskiej pojemności — np. 2000 mAh z pakietu 2800 mAh — w połączeniu z
funkcją Odtwórz dźwięk powtarzaną co 10 sekund, aż do zresetowania modelu:

![Odtwórz wartość przy niskim stanie akumulatora](../assets/how-to-consumption-sf2-play-battlow.png)
![Odtwórz wartość: consumption przy niskim stanie akumulatora](../assets/how-to-consumption-sf2-play-value-consumption.png)
