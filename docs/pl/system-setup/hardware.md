---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sprzęt

![Kontrola sprzętu](../assets/system-hardware-check-x20s.png)

Testowanie i kalibracja fizycznych elementów sterujących nadajnika, definicje
typów przełączników oraz mapa klawiszy głównych.

## Kontrola sprzętu {: #hardware-check }

Umożliwia poruszenie każdego fizycznego wejścia, aby potwierdzić, że każde
z nich jest poprawnie rejestrowane.

![Kontrola sprzętu X20 Pro](../assets/system-hardware-check-x20pro.png)
![Kontrola sprzętu X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — sprawdza dodatkowo dwa zatrzaskowe przełączniki przyciskowe **K**
  i **L** na tylnych barkach oraz dodatkowe trymy **T5**/**T6**.
- **X18** — sprawdza dodatkowo trymy **T5**/**T6**.

## Kalibracja analogów {: #analogs-calibration }

![Kalibracja analogów](../assets/system-hardware-analogs-calibration.png)

Uczy nadajnik, gdzie dokładnie znajduje się środek i skrajne położenia każdego
drążka, potencjometru i suwaka. Uruchamia się automatycznie przy pierwszym starcie;
należy ją powtórzyć po wymianie drążka, potencjometru lub suwaka.

## Kalibracja żyroskopu

![Kalibracja żyroskopu](../assets/system-hardware-gyro-calibration.png)

Kalibruje wbudowany żyroskop, tak aby wejścia oparte na przechyle poprawnie
reagowały na przechylanie nadajnika — pozycją „poziomą” staje się sposób, w jaki
zwykle trzymasz nadajnik. Również uruchamia się automatycznie przy pierwszym starcie.

## Filtr analogów

Włączany/wyłączany filtr ADC dla drążków, domyślnie włączony — redukuje drgania
wokół środka drążka. Jest to ustawienie **globalne**; dostępne jest również
nadpisanie filtru analogów **dla pojedynczego modelu** w sekcji
[Edycja modelu](../model-setup/model-edit.md).

## Ustawienia potencjometrów/suwaków {: #potssliders-settings }

Zmiana nazw potencjometrów i suwaków. **X20 Pro/R/RS** obsługuje dodatkowo dwa
dodatkowe potencjometry, **Ext1**/**Ext2**, zwykle wykorzystywane w drążkach
3-osiowych.

![Wartości ADC, potencjometry](../assets/system-hardware-pots-x20s.png)
![Wartości ADC, potencjometry (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Ustawienia przełączników {: #switches-settings }

![Przełączniki](../assets/system-hardware-switches.png)

- **Opóźnienie wykrywania środka przełącznika** — zapobiega temu, aby szybkie
  przełączenie góra→dół (lub dół→góra) przełącznika 3-pozycyjnego chwilowo
  zarejestrowało pozycję środkową; środek powinien być rejestrowany tylko wtedy,
  gdy przełącznik faktycznie się w nim zatrzyma. Wartość domyślna to 0 ms, dobrana
  pod kątem wykrywania „autotestu” na CH12 w odbiornikach stabilizowanych FrSky.
- **Typ przełącznika** — każdy z przełączników SA–SJ może zostać zdefiniowany jako
  **None**, **Momentary**, **2 POS** lub **3 POS**, co pozwala zamieniać funkcjonalność
  między fizycznymi przełącznikami (np. przypisać chwilowemu przełącznikowi SH rolę
  pełnioną zwykle przez 2-pozycyjny SF) — w zakresie, na jaki faktycznie pozwala
  okablowanie nadajnika (roli 3-pozycyjnej zwykle nie da się przypisać sprzętowi,
  które nie jest do tego okablowane).

  ![Opcje przełączników](../assets/system-hardware-switches-options.png)
  ![Dodatkowe przełączniki](../assets/system-hardware-switches-2.png)

- **Zmiana nazw** — przełączniki można przemianować z SA–SJ na własne nazwy;
  nazwy są globalne dla wszystkich modeli.
- **X20 Pro** — dodaje przełączniki przyciskowe **K**/**L** na tylnych barkach
  oraz pozycje **M**/**N**, jeśli są okablowane (zwykle dla przełączników
  na końcach drążków).

## Mapa klawiszy głównych

Zmienia przypisanie tego, dokąd prowadzą klawisze główne `SYS`, `MDL` i `DISP`
(`TELE` w starszych nadajnikach).

- **`DISP`** — zarówno krótkie, jak i długie naciśnięcie można przypisać do dowolnej
  strony Modelu, strony Systemu, Konfiguracji ekranów, Strony głównej lub Rejestru
  danych lotu. Dla spójności z serią X10 długie naciśnięcie `DISP` jest zwyczajowo
  ustawiane na Konfigurację ekranów.
- **`SYS`/`MDL`** — przypisać można wyłącznie długie naciśnięcie (do tego samego
  zestawu miejsc docelowych); krótkie naciśnięcie zawsze otwiera odpowiednio sekcję
  System lub Model.

## Opcje sprzętowe zależne od nadajnika {: #radio-specific-hardware-options }

- **Włączanie ulepszonych drążków z haptyką** (X20 Pro, X20R) — X20 Pro AW i
  X20RS są fabrycznie wyposażone w drążki MC20R z silniczkami wibracyjnymi
  (stick-shaker); jeśli drążki MC20R zostały zamontowane w X20 Pro lub X20R
  w ramach modernizacji, należy włączyć je w tym miejscu (konfigurację samych
  wzorców haptycznych opisano w sekcji
  [Funkcje specjalne](../model-setup/special-functions.md)).

  ![Haptyka (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptyka (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Opcja enkodera** (X20 Pro AW, X20R/RS) — nadajniki te mają bardziej czuły
  enkoder obrotowy; włącz **półkroki**, aby zmniejszyć jego czułość.

  ![Opcja enkodera (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Podgląd wartości ADC {: #adc-value-inspector }

Pokazuje surowe wartości konwersji analogowo-cyfrowej odczytywane przez procesor
dla każdego wejścia analogowego:

![Kontrola ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Kontrola ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 lewy drążek poziomo, 2 lewy drążek pionowo, 3 prawy drążek pionowo,
4 prawy drążek poziomo, 5 Pot 1, 6 Pot 2, 7 środkowy suwak, 8 lewy suwak,
9 prawy suwak.

**X20 Pro**: jak wyżej, ale z dwoma dodatkowymi kanałami zewnętrznych potencjometrów
(7 Ext1, 8 Ext2 — np. potencjometry montowane na drążkach) wstawionymi przed suwakami,
które przesuwają się na 9 środkowy suwak, 10 lewy suwak, 11 prawy suwak.
