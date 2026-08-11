---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Konfiguracja systemu FBUS

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (dawniej
F.Port2) łączy sterowanie i telemetrię w jednej linii, dzięki czemu kilka
urządzeń FBUS może współdzielić jedno połączenie szeregowe (daisy-chain) z
pełną możliwością bezprzewodowej konfiguracji. W tym przewodniku podłączamy
dwa serwa Xact do kanałów lotek (1 i 5) z [Podstawowego przykładu
stałopłata](../tutorials/basic-fixed-wing.md).

!!! note "Zrzuty ekranu w przygotowaniu"
    Ta strona nie zawiera jeszcze zrzutów ekranu z symulatora — zobacz [Proces
    tworzenia zrzutów ekranu](../contributing/screenshot-pipeline.md).

## 1. Pobierz najnowsze oprogramowanie

FBUS wymaga aktualnego oprogramowania zarówno w odbiorniku, jak i w
urządzeniach — np. serwa Xact wymagają wersji v2.0.1 lub nowszej. Odpowiednie
aktualizacje pobierzesz ze [strony pobierania
FrSky](https://www.frsky-rc.com/download/).

## 2. Wgraj oprogramowanie

Skopiuj pliki oprogramowania do katalogu `Firmware/` na karcie SD/eMMC. W
[Menedżerze plików](../system-setup/file-manager.md) podłącz serwo do złącza
S.Port nadajnika (biały/żółty przewód od strony wycięcia), wybierz plik
oprogramowania i użyj opcji **Flashuj urządzenie zewnętrzne**.

## 3 / 5. Konfiguracja Physical ID

Oba serwa mają domyślnie Physical ID `0C` hex / Application ID `6800` hex —
na wspólnej magistrali spowodują konflikt, o ile jedno z nich nie zostanie
zmienione. W zależności od typu odbiornika są dwie drogi:

**Przez złącze S.Port nadajnika** (dowolny odbiornik):

1. Podłącz serwo 1, przejdź do **Konfiguracja urządzenia → XAct** i ustaw
   **Moduł** na **Złącze S.Port**. Pozostaw Physical ID `0C`/Application ID
   `6800` oraz kanał `CH1` z wartościami domyślnymi, a następnie wybierz
   **Zapisz do pamięci flash**.
2. Podłącz zamiast niego serwo 2 i wejdź do tego samego menu. Zmień
   **Physical ID** na `0D` hex, a **Application ID** na `6801` hex (w
   [tabeli Physical
   ID](../model-setup/telemetry.md#how-frsky-telemetry-works) sprawdzisz,
   które pozycje są wolne), ustaw **Kanał** na `CH5` i wybierz **Zapisz do
   pamięci flash**.

**Bezpośrednio przez odbiornik** (np. TD-R18 Tandem, oba serwa podłączone
jednocześnie — zobacz [Krok 4](#4-configure-the-receiver-for-fbus)):

1. Przy podłączonym wyłącznie serwie 1 (np. do Pin1) wejdź w **Konfiguracja
   urządzenia → XAct**, **Moduł** → **Moduł wewnętrzny**. Potwierdź wartości
   domyślne (`0C`/`6800`/`CH1`) i wybierz **Zapisz do pamięci flash**.
2. Przy podłączonym wyłącznie serwie 2 (Pin5) wejdź w to samo menu
   (Konfiguracja urządzenia komunikuje się z jednym serwem naraz) — zmień na
   `0D`/`6801`/`CH5` i wybierz **Zapisz do pamięci flash**. Następnie wejdź
   ponownie w Konfigurację urządzenia, aby potwierdzić, że zmiana została
   zapisana.

## 4. Konfiguracja odbiornika do pracy z FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [System RF](../model-setup/rf-system.md) → przycisk odbiornika
→ **Opcje** → ustaw **Port telemetrii** na **FBUS**. Serwa Xact podłącza się
wtedy szeregowo do tego portu; ponieważ każde serwo ma tylko jedno złącze, do
rozgałęzienia sygnału na kilka urządzeń służy rozdzielacz wielokanałowy
F.Port2 (FP2CH4/6/8).

**TD-R18 Tandem**: System RF → przycisk odbiornika → **Opcje** → ustaw
poszczególne piny (np. **Pin1**, **Pin5**) na **FBUS** — w ten sposób można
przypisać dowolną liczbę pinów, całkowicie eliminując potrzebę stosowania
rozdzielaczy; każdy pin przypisany do FBUS przenosi identyczny sygnał FBUS.

## 5. Sprawdzenie sterowania serwami przez FBUS

Podłącz serwo 1 do Pin1, a serwo 2 do Pin5 (kanały lotek z przykładu
stałopłata), włącz zasilanie i sprawdź, czy kanały 1 i 5 poruszają właściwymi
serwami.

## 6. Sprawdzenie telemetrii FBUS

Przy obu podłączonych serwach usuń istniejące czujniki `SRV` w sekcji
[Telemetria](../model-setup/telemetry.md) i wykonaj ponowne wyszukiwanie.
Każde serwo zgłasza 4 czujniki: prąd, napięcie, temperaturę oraz status
(`OK` w normalnych warunkach).

## 7. Późniejsze zmiany konfiguracji

Gdy model jest już w pełni okablowany, odłączanie pojedynczego serwa w celu
przekonfigurowania go przez Konfigurację urządzenia jest niepraktyczne.
Zamiast tego: przejdź do Telemetrii, znajdź czujnik należący do wybranego
serwa (np. `SRV1 curr`) i wybierz **Konfiguruj** — spowoduje to bezpośrednie
otwarcie konfiguracji tego serwa. Po każdej zmianie wybierz **Zapisz do
pamięci flash**.

!!! warning
    Uważaj, aby przypadkowo nie zmienić na tym ekranie Physical ID ani
    Application ID — to właśnie one zapewniają adresowalność każdego serwa na
    wspólnej magistrali.
