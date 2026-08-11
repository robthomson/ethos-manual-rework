---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Tryb awaryjny

Tryb awaryjny to reakcja systemu Ethos na nieoczekiwaną awarię niskiego poziomu,
taką jak reset watchdoga. Watchdog to licznik czasu stale restartowany przez
różne części systemu; jeśli coś uniemożliwi jego zrestartowanie, licznik
przekracza limit czasu i wymusza sprzętowy reset. Tryb awaryjny uruchamia
wówczas nadajnik ponownie tak szybko, jak to możliwe, pomijając wszystkie
normalne procedury kontrolne przy starcie, dzięki czemu kontrola nad modelem
zostaje przywrócona z minimalnym opóźnieniem. W tym trybie karta SD/eMMC nie
jest w ogóle używana.

Dostępne są wyłącznie funkcje niezbędne do dalszego sterowania modelem — żadna
z funkcji wyższego poziomu nie działa. Ekran pozostaje pusty, z wyjątkiem
napisu **EMERGENCY MODE**, któremu towarzyszy powtarzający się co 3 sekundy
sygnał dźwiękowy o długości 300 ms; komunikaty głosowe, skrypty Lua,
rejestrowanie danych i telemetria przestają działać. Jeżeli nastąpi to
w powietrzu, należy jak najszybciej wylądować.

Najczęstszą przyczyną jest awaria karty SD.

## Testowanie trybu awaryjnego

Można dodać **narzędzie systemowe**, które celowo wywołuje tryb awaryjny
w celach testowych, aby nie poznawać go po raz pierwszy podczas lotu.
Dotknięcie ikony Emergency Test powoduje wyświetlenie prośby o potwierdzenie,
a następnie przełączenie nadajnika w tryb awaryjny dokładnie tak, jak przy
rzeczywistej awarii.
