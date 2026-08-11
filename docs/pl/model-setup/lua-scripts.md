---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Skrypty Lua (Model)

![Konfiguracja Lua](../assets/model-lua-config.png)

To menu pojawia się dopiero wtedy, gdy skrypt **źródła** (source) lub
**zadania** (task) Lua zostanie zainstalowany w katalogu `scripts/` na karcie
SD/eMMC (patrz [Menedżer
plików](../system-setup/file-manager.md#top-level-folders)) — służy ono do
aktywowania i konfigurowania tych skryptów **dla poszczególnych modeli**, a nie
do ich instalowania. Po zainstalowaniu źródło lub zadanie jest dostępne globalnie
dla każdego modelu; na tej stronie każdy model włącza je i ustawia własną
konfigurację. Przykładowe skrypty źródeł i zadań są publikowane na stronie
Ethos-Feedback-Community (`/lua/examples/task`, `/lua/examples/source`).

## Zadania Lua

Każde zainstalowane zadanie jest wyświetlane z przełącznikiem włączenia dla
danego modelu. Włączenie zadania odsłania jego formularz konfiguracyjny (jeśli
taki posiada) — skrypt zadania dostarcza własne funkcje odczytu/zapisu, dzięki
czemu każdy model może zapisać własne ustawienia. Na przykład zadanie może
udostępniać konfigurowalny zakres liczbowy, ustawiany niezależnie dla każdego
modelu.

## Źródła Lua

Ten sam schemat dotyczy źródeł: włącz je dla danego modelu, a następnie
skonfiguruj za pomocą formularza udostępnianego przez skrypt źródła.
Zarejestrowane w ten sposób źródło staje się dostępne jako zwykłe
[źródło](../getting-started/user-interface-and-navigation.md#choosing-a-source)
w każdym innym miejscu Ethos, dokładnie tak samo jak źródło wbudowane.

## Dla autorów skryptów

Źródła i zadania rejestruje się z poziomu Lua za pomocą `system.registerSource()`
oraz `system.registerTask()` — patrz Ethos Lua Reference Guide oraz
[Skrypty Lua](../lua-scripts/index.md) w niniejszej instrukcji, gdzie opisano
ogólne środowisko skryptowe (widgety to osobny, pokrewny mechanizm — patrz
[Widgety niestandardowe](../displays/custom-widgets.md)).
