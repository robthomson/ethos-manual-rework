---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Podstawowa struktura widgetu

Własny widget Lua (instalacja opisana w [Własne widgety](../displays/custom-widgets.md))
jest zbudowany z niewielkiego zestawu nazwanych pól/procedur obsługi:

- **`key`** *(łańcuch znaków)* — unikatowy identyfikator widgetu.
- **`name`** *(łańcuch znaków lub funkcja)* — wyświetlana nazwa widgetu. Może to
  być zwykły łańcuch znaków albo funkcja bez argumentów zwracająca taki łańcuch —
  przydatne w przypadku nazwy zależnej od języka.
- **`create`** *(funkcja)* — wywoływana jednorazowo przy tworzeniu widgetu,
  bez argumentów. Zwraca **tablicę widgetu**, która jest następnie przekazywana
  do wszystkich pozostałych procedur wymienionych poniżej — tutaj zainicjuj stan
  widgetu i zapisz go w tej tablicy.
- **`configure`** *(funkcja)* — wywoływana, gdy użytkownik otworzy ekran
  konfiguracji widgetu; jako jedyny argument przyjmuje tablicę widgetu zwróconą
  przez `create()` i nic nie zwraca. Zbuduj tutaj formularz konfiguracyjny i
  używaj go do aktualizowania wartości w tablicy widgetu.
- **`wakeup`** *(funkcja)* — wywoływana w każdej pętli (mniej więcej co 50 ms);
  przyjmuje tablicę widgetu i nic nie zwraca. Sprawdź tutaj, czy coś się zmieniło;
  jeśli tak, wywołaj `invalidateWindow()`, aby wymusić ponowne rysowanie poprzez
  `paint()`. Ta procedura powinna działać szybko — najlepiej, aby przez większość
  wywołań nie robiła zupełnie nic.
- **`event`** *(funkcja)* — wywoływana, gdy widget otrzyma zdarzenie; Ethos
  przekazuje dowolne zdarzenia do widgetu za pośrednictwem tej procedury.
- **`paint`** *(funkcja)* — rysuje widget; przyjmuje tablicę widgetu i nic nie
  zwraca. Wywoływana automatycznie zawsze, gdy zostało wywołane
  `lcd.invalidate()`. Może działać stosunkowo wolno, ale mimo to powinna
  faktycznie odrysowywać zawartość tylko wtedy, gdy coś się zmieniło.
- **`read`** *(funkcja, opcjonalna)* — odczytuje zapisane dane widgetu.
- **`write`** *(funkcja, opcjonalna)* — zapisuje dane widgetu.
- **`init`** *(funkcja)* — rejestruje widget i jego funkcje zwrotne w Ethos.
  Zazwyczaj jest to ostatni element skryptu:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` musi być unikatowy wśród wszystkich zainstalowanych widgetów; pozostałe
pola są powiązane z cyklem życia widgetu w sposób opisany powyżej.

Skrypty znajdują się w katalogu `scripts/` na karcie SD/eMMC, najlepiej
zorganizowane w osobne foldery dla każdego widgetu (zobacz [Menedżer
plików](../system-setup/file-manager.md#top-level-folders) oraz [Przykładowe
lokalizacje skryptów](example-script-locations.md)). Dalsze przykłady z
omówieniem znajdziesz w wątku *FrSky ETHOS Lua Script Programming* na rcgroups.
