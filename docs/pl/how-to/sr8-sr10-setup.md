---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Konfiguracja modelu dla SR8/SR10 i zmiana kolejności kanałów

Stabilizowane odbiorniki FrSky serii SRx wymagają określonej kolejności kanałów.
Możliwe są dwa scenariusze: utworzenie nowego modelu od podstaw lub
przekonwertowanie istniejącego modelu tak, aby ją spełniał.

!!! note "Zrzuty ekranu w przygotowaniu"
    Ta strona nie ma jeszcze zrzutów ekranu z symulatora — zobacz [Proces
    tworzenia zrzutów ekranu](../contributing/screenshot-pipeline.md).

## Tworzenie nowego modelu

Kreator [Wybór modelu](../model-setup/model-select.md) domyślnie grupuje
powierzchnie sterowe o tej samej funkcji (np. 2 lotki → `AAETR`), natomiast
odbiorniki SRx wymagają, aby pierwsze cztery kanały były ustalone jako **AETRA**.

1. W sekcji [Sterowanie](../system-setup/controls.md) sprawdź, czy **Kolejność
   kanałów** to `AETR`.
2. Włącz opcję **[Pierwsze cztery kanały
   stałe](../system-setup/controls.md#first-four-channels-fixed)** — zapobiega
   ona grupowaniu pierwszych czterech kanałów przez kreatora i utrzymuje je
   ściśle w kolejności `AETRA…`, niezależnie od tego, ile powierzchni każdego
   rodzaju posiada płatowiec.
3. Uruchom kreator tworzenia modelu w normalny sposób — pierwsze 5 kanałów
   zostanie ustawionych jako `AETRA`.

!!! note "Autotest odbiorników Archer"
    Autotest odbiorników Archer jest obecnie uruchamiany poprzez [Konfigurację
    urządzenia → SxR](../system-setup/devices.md) (firmware v2.1.10+), a nie
    dedykowaną procedurą autotestu. Kanał gazu musi znajdować się w położeniu
    −100%, w przeciwnym razie autotest się nie rozpocznie.

## Zmiana kolejności kanałów w istniejącym modelu

Przekonwertowanie istniejącego modelu (np. o kolejności `AAETRFF`) na kolejność
wymaganą przez odbiornik stabilizowany (`AETRAE`, następnie kanał 9 Gain, 10/11
tryby lotu, 12 autotest w starszych jednostkach SxR) sprowadza się do serii
zamian kanałów w sekcji [Wyjścia](../model-setup/outputs.md#swap-channels).

Punkt wyjścia:

| Kan | Funkcja |
|---|---|
| 1 | Lotka1 (prawa) |
| 2 | Lotka2 (lewa) |
| 3 | Ster wysokości |
| 4 | Gaz |
| 5 | Ster kierunku |
| 6 | Klapa1 (prawa) |
| 7 | Klapa2 (lewa) |
| 8 | Podwozie chowane |

Kolejność docelowa: `AETRAE` — Kan1 Lotka1, Kan2 Ster wysokości, Kan3 Gaz,
Kan4 Ster kierunku, Kan5 Lotka2, Kan6 Ster wysokości2/AUX2 (następnie
Gain/tryby lotu/autotest na kanałach 9–12).

1. **Najpierw przenieś Lotkę2 w inne miejsce**: w sekcji Wyjścia wybierz CH2
   (Lotka2), naciśnij ponownie, wybierz **Zamień kanały** i zamień ją z wolnym
   kanałem (np. CH9). Zamiana następuje natychmiast — każdy miks odwołujący się
   do któregokolwiek z tych kanałów zostaje automatycznie zaktualizowany.
2. **Zamień CH3 (Ster wysokości) → CH2.**
3. **Zamień CH4 (Gaz) → CH3.**
4. **Zamień CH5 (Ster kierunku) → CH4.**
5. **Zamień CH9 (Lotka2, odłożona w kroku 1) → CH5.**

Wynik:

| Kan | Funkcja |
|---|---|
| 1 | Lotka1 (prawa) |
| 2 | Ster wysokości |
| 3 | Gaz |
| 4 | Ster kierunku |
| 5 | Lotka2 (lewa) |
| 6 | Klapa1 (prawa) |
| 7 | Klapa2 (lewa) |
| 8 | Podwozie chowane |

— czyli kolejność oczekiwana przez stabilizowane odbiorniki FrSky.
