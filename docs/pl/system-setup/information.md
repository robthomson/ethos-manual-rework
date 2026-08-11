---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Informacje

![Informacje o systemie](../assets/system-info.png)

Szczegóły oprogramowania systemowego, typ gimbali, informacje o wewnętrznym/zewnętrznym
module RF, dane powiązanego odbiornika, czas pracy nadajnika, dzienniki błędów oraz reset fabryczny.

## Informacje o nadajniku

- **Numer seryjny** — numer seryjny nadajnika.
- **Firmware** — wersja Ethos oraz typ nadajnika (np. X20).
- **Wersja firmware** — wariant kompilacji, np. FCC, LBT lub Flex.
- **Data** — data/godzina kompilacji oprogramowania.
- **Dostępna pamięć RAM** — wolna pamięć RAM systemu, przydatna do wykrycia
  nieprawidłowo działającego skryptu Lua; udostępniona również jako systemowe
  [źródło](../getting-started/user-interface-and-navigation.md#choosing-a-source),
  dzięki czemu może być wyświetlana w widgecie.
- **Drążki** — wersja zainstalowanych czujników Halla w gimbalach (lub „ADC”
  dla gimbali analogowych).
- **Moduł wewnętrzny** — wersje sprzętowa i programowa wewnętrznego modułu RF.
- **Odbiornik** — dane aktualnie powiązanego odbiornika, wyświetlane po informacjach
  o module wewnętrznym. Jeśli odbiornik redundantny współdzieli ten sam slot co
  odbiornik główny, oba są wyświetlane naprzemiennie (np. Archer SR10 Pro
  pokazywany na przemian z redundantnym R9MM-OTA w pozycji „Receiver1”).
- **Moduł zewnętrzny** — dane sprzętowe/programowe zamontowanego zewnętrznego
  modułu RF FrSky korzystającego z protokołu ACCESS. Moduły Multi-protocol nie
  są tutaj wyświetlane.

![Informacje X20 Pro](../assets/system-info-x20pro.png)

## Czas pracy nadajnika

![Czas pracy nadajnika](../assets/system-info-radio-runtime.png)

Śledzi łączny czas użytkowania nadajnika; **Reset** zeruje licznik.

## Błędy

![Błędy](../assets/system-info-errors.png)

Czerwony trójkąt na górnym pasku widoku głównego oznacza, że Ethos zarejestrował
błąd, którego szczegóły widoczne są w tym miejscu. Możliwe przyczyny:

- **Błędy skryptów Lua** — problem w działającym skrypcie Lua.
- **Błąd kopii zapasowej RAM** — model zbyt duży dla pamięci RAM przeznaczonej na
  kopię zapasową modelu. Ethos zwiększył ją z 4K do 32K, więc obecnie wystąpienie
  tego błędu jest mało prawdopodobne, ale jeśli się pojawi, jest to błąd istotny:
  po uruchomieniu [trybu awaryjnego](../getting-started/emergency-mode.md) model
  ładuje się wolniej z karty SD zamiast z pamięci kopii zapasowej.
- **Uruchomienie nocnej kompilacji firmware** — przypomnienie, że kompilacje
  nocne nie są przeznaczone do latania.

**Reset** czyści zarejestrowane błędy — przydatne w trakcie sesji debugowania Lua.

## Reset fabryczny

![Reset fabryczny](../assets/system-info-factory-reset.png)

Przywraca nadajnik do ustawień fabrycznych w całości na samym urządzeniu — bez
potrzeby podłączania do komputera.

![Potwierdzenie resetu fabrycznego](../assets/system-info-factory-reset-confirm.png)

!!! danger
    Potwierdzenie kasuje **wszystkie** modele, dzienniki, zrzuty ekranu, dokumenty,
    skrypty, bitmapy oraz ustawienia nadajnika. Postęp kasowania pokazuje pasek
    postępu, po czym wszystkie dyski są odmontowywane, a nadajnik uruchamia się
    ponownie.

Strona informacyjna X20 Pro/R/RS wyświetla odpowiadające informacje dla tej
rodziny nadajników.
