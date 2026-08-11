---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lokalizacja przykładowych skryptów

Oficjalne przykładowe skrypty są publikowane pod adresem
[github.com/FrSkyRC/ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/tree/main/lua)
(w szczególności katalogi `/lua/examples/task` oraz `/lua/examples/source`). Większość
przykładów to widgety Lua (konfigurowane w [Konfiguracji
ekranów](../displays/custom-widgets.md)); przykład **`servo`**
demonstruje natomiast **narzędzie systemowe** — skrypt, który pojawia się po
pozycji **Info** w menu systemowym, a nie jako widget na wyświetlaczu.

## Pobieranie skryptu

1. Otwórz powyższy odnośnik do repozytorium w przeglądarce i przejdź do
   wybranego katalogu, a następnie do pliku `main.lua`.
2. Kliknij plik, aby go wyświetlić, a następnie wybierz **Raw**.
3. Kliknij stronę prawym przyciskiem myszy → **Zapisz stronę jako…** i zapisz ją pod nazwą `main.lua`.
4. Aby uniknąć konfliktu z plikami `main.lua` innych skryptów, przenieś go do
   odpowiednio nazwanego katalogu — rozsądnym wyborem jest nazwa katalogu
   źródłowego.

W przypadku pozostałych plików wymaganych przez skrypt (obrazów itp.): kliknij plik, kliknij
**Download**, a następnie kliknij prawym przyciskiem myszy i wybierz **Zapisz obraz jako…** (lub odpowiednik), aby
zapisać go obok skryptu.

Skrypty instaluje się w katalogu `scripts/` na karcie SD/pamięci eMMC — zobacz [Menedżer
plików](../system-setup/file-manager.md#top-level-folders).

Zobacz także wątek *FrSky ETHOS Lua Script Programming* na rcgroups, w którym znajdziesz
skrypty społeczności oraz dyskusje wykraczające poza oficjalne przykłady.
