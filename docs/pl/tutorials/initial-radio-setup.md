---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Wstępna konfiguracja nadajnika

Jednorazowa konfiguracja, którą należy wykonać przed zaprogramowaniem
jakiegokolwiek modelu. Wszystkie [Samouczki](index.md) zamieszczone dalej
zakładają, że została ona przeprowadzona jako pierwsza.

!!! note
    Te samouczki nie są ścisłą instrukcją krok po kroku — zakładają
    znajomość podstawowego słownictwa RC oraz swobodę w poruszaniu się po
    menu Ethos. Jeżeli cokolwiek jest tu niejasne, warto najpierw wrócić do
    rozdziału [Interfejs użytkownika i
    nawigacja](../getting-started/user-interface-and-navigation.md).

## Krok 1. Naładuj akumulator nadajnika i pakiety napędowe

Naładuj akumulator nadajnika zgodnie z wytycznymi dołączonymi do
nadajnika, a pakiety napędowe — ładowarką odpowiednią dla ich chemii;
szczególną ostrożność zachowaj przy pakietach litowych.

## Krok 2. Skalibruj sprzęt

Upewnij się, że [kalibracja
sprzętu](../system-setup/hardware.md#analogs-calibration) została
wykonana (uruchamia się automatycznie przy pierwszym starcie), dzięki
czemu nadajnik zna dokładne położenie środkowe i skrajne każdego gimbala,
potencjometru i suwaka. Powtórz ją w menu **System → Hardware** za każdym
razem, gdy wymieniony zostanie gimbal, potencjometr lub suwak.

## Krok 3. Przeprowadź konfigurację systemową nadajnika

[Ustawienia systemu](../system-setup/index.md) obejmują wszystko, co jest
wspólne dla wszystkich modeli, w odróżnieniu od ustawień indywidualnych
opisanych w [Konfiguracji modelu](../model-setup/index.md). Większość
wartości domyślnych jest na początek odpowiednia, warto jednak przejrzeć:

- **[Data i godzina](../system-setup/date-and-time.md)** — ustaw
  poprawnie.
- **[Audio → Wybór
  głosów](../system-setup/general.md#audio-settings)** — skonfiguruj
  komunikaty głosowe, w tym ewentualne własne pliki dźwiękowe.
- **[Elementy sterujące (drążki)](../system-setup/controls.md)**:
  - **Tryb drążków** — Mode 1 (gaz/lotki po prawej, ster wysokości/ster
    kierunku po lewej) lub Mode 2 (gaz/ster kierunku po lewej, lotki/ster
    wysokości po prawej — ustawienie domyślne w Ethos).

    !!! warning
        Jeżeli model jest skonfigurowany dla jednego trybu drążków,
        podczas gdy nadajnik ustawiony jest na drugi, silnik elektryczny
        może ruszyć w chwili załączenia zasilania odbiornika.

  - **Kolejność kanałów** — Ethos domyślnie stosuje **AETR** (lotki, ster
    wysokości, gaz, ster kierunku); konwencja Spektrum/JR to **TAER**,
    Futaba/Hitec to **AETR**. Ustawienie to określa kolejność
    przypisywania sygnałów z drążków podczas tworzenia nowego modelu —
    poszczególne modele można później skorygować indywidualnie.

    !!! note "Odbiorniki stabilizowane FrSky"
        Wymagają one konkretnie kolejności **AETR**. Przy więcej niż jednej
        powierzchni sterowej na funkcję (np. 2 lotki) kreator zwykle grupuje
        je razem (dając **AAETR**) — jednak odbiorniki SRx oczekują
        **AETRA**/**AETRAE**, dlatego włącz opcję **[Pierwsze cztery kanały
        stałe](../system-setup/controls.md#first-four-channels-fixed)**
        w ustawieniach drążków, aby pierwsze cztery kanały zachowały ścisłą
        kolejność AETR niezależnie od pozostałych ustawień.

- **[Akumulator](../system-setup/battery.md)** — ustaw **Napięcie
  główne**, **Napięcie niskie** oraz **Zakres wyświetlanego napięcia**
  zgodnie z rzeczywistym akumulatorem nadajnika.
- **[Identyfikator rejestracyjny właściciela](../model-setup/rf-system.md#owner-registration-id)**
  — używany przez odbiorniki ACCESS i współdzielony między nadajnikami na
  potrzeby Smart Share. Konfigurowany jest w Konfiguracji modelu, ale
  w praktyce działa jak ustawienie systemowe, ponieważ każdy nowy model
  z niego korzysta (w razie potrzeby można go nadal zmienić dla
  poszczególnych odbiorników podczas rejestracji).

!!! note "Jednostki"
    Ethos nie ma globalnego przełącznika jednostek metryczne/imperialne —
    [jednostki czujników
    telemetrycznych](../model-setup/telemetry.md#editing-a-sensor) ustawia
    się indywidualnie, dla każdego czujnika z osobna.
