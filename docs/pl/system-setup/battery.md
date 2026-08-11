---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Akumulator

![Ustawienia akumulatora nadajnika](../assets/system-battery.png)

Kalibruje odczyt wewnętrznego akumulatora nadajnika i ustawia progi
alarmów — niezależnie od ustawień pakietu napędowego modelu (patrz [Poradnik:
Ostrzeżenie o niskim napięciu akumulatora](../how-to/low-battery-warning.md)).

- **Napięcie główne** — pokazuje bieżący odczyt, a jednocześnie służy do
  kalibracji: należy wpisać rzeczywiste napięcie zmierzone
  multimetrem. Wartość domyślna to 8,4 V (w pełni naładowany pakiet 2S Li-ion).
- **Niskie napięcie** — próg alarmu, domyślnie 7,2 V (7,4 V daje dodatkowy
  zapas). Gdy [alert napięcia
  głównego](alerts.md) jest włączony, spadek poniżej tej wartości powoduje wyświetlenie okna ostrzeżenia
  oraz komunikat głosowy „Radio battery is low" powtarzany co minutę, niezależnie od tego, czy okno
  jest otwarte.

  !!! warning
      Wyląduj i naładuj akumulator nadajnika, gdy tylko rozlegnie się ten alert — będzie on
      powtarzany co minutę. Przy 6,0 V nadajnik wyłącza się
      bezwarunkowo, aby chronić ogniwa Li-ion 2×3,0 V.

- **Zakres wyświetlanego napięcia** — wartości min/maks dla graficznego wskaźnika
  akumulatora w prawym górnym rogu: MIN to punkt, w którym gaśnie pierwszy segment
  paska, MAX to punkt, w którym zapala się czwarty. Wartości domyślne to 6,4–8,4 V dla
  wbudowanego pakietu Li-ion; wielu pilotów podnosi dolną granicę, aby wcześniej otrzymać
  ostrzeżenie o niskim napięciu i uniknąć nadmiernego rozładowania. Należy dostosować te wartości do
  faktycznie zamontowanego typu akumulatora.
- **Napięcie RTC** — napięcie ogniwa guzikowego zegara czasu rzeczywistego. 3,0 V dla
  nowego ogniwa; wymień je poniżej 2,7 V, aby zachować dokładność zegara, i licz się z
  [alertem napięcia RTC](alerts.md) poniżej 2,5 V.
