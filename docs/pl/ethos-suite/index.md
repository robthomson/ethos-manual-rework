---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite to towarzysząca aplikacja dla systemów Windows/Mac, służąca do zarządzania nadajnikiem z systemem Ethos, podłączonym przez USB.

![Karta Radio w Ethos Suite](../assets/ethos-suite-radio-tab.png)

Po nawiązaniu połączenia Ethos Suite umożliwia:

1. Odczyt typu nadajnika, jego identyfikatora oraz zainstalowanych wersji —
   oprogramowania układowego, bootloadera, wewnętrznego modułu RF, plików
   pamięci flash oraz plików na SD card/eMMC.
2. Przełączanie nadajnika pomiędzy trybem bootloadera a uruchomionym systemem
   Ethos i z powrotem.
3. Porównanie zainstalowanych wersji z aktualnymi oraz automatyczną
   aktualizację — wyłącznie nieaktualnych komponentów, wszystkich niezależnie
   od stanu, lub poszczególnych komponentów pojedynczo.
4. Tworzenie kopii zapasowych modeli na dysku za pomocą **Model Manager** oraz
   przywracanie wcześniejszej kopii (niezbędne, ponieważ pliki modeli nie są
   wstecznie zgodne pomiędzy wersjami oprogramowania układowego).
5. Pobranie dowolnego oprogramowania układowego ze strony pobierania FrSky za
   pośrednictwem **Download center** oraz wykorzystanie nadajnika jako pośrednika
   do bezpośredniego wgrania oprogramowania do modułu, czujnika, serwa lub
   odbiornika.
6. Konwersję plików graficznych i dźwiękowych do natywnych formatów Ethos.
7. Udostępnienie **narzędzi programistycznych Lua** — dokumentacji API, skryptów
   demonstracyjnych oraz terminala debugowania.
8. Wgranie bootloadera nadajnika w trybie DFU (połączenie przy wyłączonym
   zasilaniu), niezależnie od tego, czy własne oprogramowanie układowe nadajnika
   nadal działa.
9. Naprawę pamięci wewnętrznej w nadajnikach X18/S, TW Lite, XE oraz
   X20 Pro/R/RS za pomocą **Repair Tool**, jeśli nie można odczytać pamięci NAND
   lub ustawienia nie są zapisywane.
10. Bezpieczne odłączanie dysków USB nadajnika.
11. Powiadamianie przy uruchomieniu o dostępnej aktualizacji samej aplikacji
    Suite (instalowanej przy zamknięciu programu).

## Tryby połączenia

Poza swoimi narzędziami, Suite działa w trzech odrębnych stanach połączenia
z nadajnikiem:

- **Nadajnik w trybie bootloadera** — zakładka **Radio** sprawdza/aktualizuje
  oprogramowanie układowe oraz pliki pamięci flash/SD card/eMMC;
  **Model Manager** tworzy kopię zapasową nadajnika lub ją przywraca.
- **Nadajnik w trybie Ethos** — Suite wykorzystuje nadajnik jako pośrednika
  (poprzez narzędzia **FRSK Flasher**/Download center) do bezpośredniego
  wgrania oprogramowania do modułu wewnętrznego lub dowolnego podłączonego
  czujnika/serwa/odbiornika.
- **Nadajnik w trybie DFU** — połączenie przy wyłączonym zasilaniu, używane
  przez **DFU Flasher** do wgrania samego bootloadera, np. gdy uszkodzenie
  oprogramowania układowego uniemożliwia normalne uruchomienie nadajnika.

Zobacz [Migracja](migration.md), aby przenieść istniejący nadajnik do Ethos
Suite po raz pierwszy, oraz [Obsługa](operation.md), aby poznać sam interfejs
Suite.
