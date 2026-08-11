---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Znajdowanie najnowszej wersji bootloadera lub innego komponentu

Wydania firmware'u Ethos zawierają plik `components.json` zawierający listę
aktualnych wersji wszystkich komponentów dla każdego nadajnika. Jest on przydatny
do sprawdzenia, czy dana wersja bootloadera/firmware'u/plików audio/plików
systemowych jest rzeczywiście aktualna, zanim zostanie wgrana.

!!! note "Zrzuty ekranu w przygotowaniu"
    Ta strona nie zawiera jeszcze zrzutów ekranu z symulatora — zobacz [Proces
    tworzenia zrzutów ekranu](../contributing/screenshot-pipeline.md).

1. Pobierz plik `components.json` z najnowszego wydania Ethos.
2. Otwórz go w edytorze tekstu (VS Code, Notatnik itp.).
3. Odszukaj sekcję dotyczącą Twojego nadajnika — np. `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (Przykładowa migawka — rzeczywiste numery wersji zawsze sprawdzaj w pliku
   z *aktualnego* wydania).

4. Odczytaj wersję interesującego Cię komponentu — w powyższym przykładzie
   najnowszy bootloader dla rodziny X20 ma numer `1.4.15`.

Informacje o tym, gdzie umieścić pobrany plik firmware'u, znajdziesz w rozdziale
[Menedżer plików](../system-setup/file-manager.md#top-level-folders), a opis
przełączania nadajnika w tryb bootloadera w celu wgrania firmware'u — w rozdziale
[Tryby połączenia USB](../getting-started/usb-connection-modes.md#bootloader-mode).
Możesz też skorzystać z [Ethos Suite](../ethos-suite/index.md), które
automatycznie sprawdza wersje i wgrywa oprogramowanie.
