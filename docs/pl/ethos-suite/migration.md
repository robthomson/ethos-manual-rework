---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migracja

Przenoszenie nadajnika ze starszych, oddzielnych narzędzi aktualizacyjnych dla PC do Ethos Suite, po raz pierwszy.

1. **Upewnij się, że masz Ethos ≥ 1.1.4** — to minimalna wersja, która potrafi wgrać nowy bootloader zgodny z Suite (format FRSK) bezpośrednio z poziomu [Menedżera plików](../system-setup/file-manager.md). W razie potrzeby najpierw zaktualizuj ręcznie do wersji 1.1.4.
2. **Wykonaj kopię zapasową karty SD/eMMC** — skopiuj całą zawartość do folderu na komputerze.
3. **Pobierz najnowszy bootloader** ze [strony wydań ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases) i rozpakuj archiwum. Każde wydanie zawiera plik `components.json` z listą aktualnych wersji wszystkich komponentów — sposób jego odczytania opisano w [Poradniku: Jak znaleźć najnowszy bootloader](../how-to/find-latest-bootloader.md).
4. Odszukaj swój nadajnik we wpisie `targets` w tym pliku, aby ustalić dokładną wersję bootloadera do użycia, a następnie znajdź odpowiadający jej plik wśród zasobów danego wydania.
5. Uruchom nadajnik w [trybie bootloadera](../getting-started/usb-connection-modes.md#bootloader-mode) (przytrzymaj `ENT`, następnie włącz zasilanie) i podłącz go przez USB.
6. Skopiuj plik bootloadera na kartę SD/eMMC (zwykle do katalogu `Firmware/`), następnie odłącz (wysuń) dyski i rozłącz połączenie.
7. Uruchom nadajnik normalnie, przejdź do **System → Menedżer plików**, dotknij właśnie skopiowanego pliku `bootloader.frsk` i wybierz **Flash bootloader**.
8. Pobierz i zainstaluj Ethos Suite — rozdział [Obsługa](operation.md) opisuje aktualizację firmware'u i plików oraz pozostałe funkcje Suite.
9. Jeżeli Ethos Suite nie zrobi tego automatycznie, może być konieczna zmiana nazwy folderu `bitmaps/user` na karcie SD/eMMC na `bitmaps/models` (to tam przechowywane są bitmapy modeli użytkownika).
