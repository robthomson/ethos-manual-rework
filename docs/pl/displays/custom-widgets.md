---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widgety niestandardowe

Poza [wbudowanymi typami widgetów](index.md) skrypty Lua mogą realizować
całkowicie niestandardowe widgety — zazwyczaj jest to pojedynczy plik `main.lua`
umieszczony w podkatalogu nazwanym zgodnie z jego przeznaczeniem.

## Instalacja

Skopiuj podkatalog widgetu do folderu `scripts/` na karcie SD/eMMC (zobacz
[Menedżer plików](../system-setup/file-manager.md#top-level-folders)). Widget
rejestruje się automatycznie przy następnym uruchomieniu i od tego momentu
pojawia się w selektorze kategorii **Zmień widget** w [Konfiguracji
ekranów](additional-displays.md) obok typów wbudowanych — konfiguruje się go
dokładnie w ten sam sposób.

## Tworzenie własnego widgetu

Strukturę kodu, jaką musi realizować skrypt widgetu, opisano w rozdziale
[Skrypty Lua → Podstawowy układ widgetu](../lua-scripts/basic-widget-layout.md).
