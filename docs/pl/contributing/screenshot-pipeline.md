---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Potok zrzutów ekranu

Każdy zrzut ekranu w tym podręczniku (obecnie około 590 sztuk, w katalogu
`docs/en/assets/`) został wykonany przez skryptowe sterowanie prawdziwym symulatorem Ethos, a nie
ręcznie. Stanowisko znajduje się w starym repozytorium
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), w katalogu
`english/manual/`, i **nie zostało jeszcze przeniesione do tego repozytorium** — niniejsza
strona dokumentuje sposób jego działania, aby można było tego dokonać oraz aby w międzyczasie
móc regenerować lub rozszerzać zrzuty ekranu bez zaczynania od zera.

## Struktura

Dla każdego menu/sekcji podręcznika istnieje para plików:

- `manual/macros/<name>.lua` — skrypt napisany w oparciu o API Lua symulatora
  (opisane poniżej), który przechodzi do określonego ekranu i wywołuje
  `simulator.screenshot(path)` w każdym miejscu wartym uchwycenia.
- `manual/<name>.sh` — jednolinijkowa nakładka uruchamiająca plik binarny symulatora
  dla konkretnego nadajnika, wskazująca na dane makro, np.:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` uruchamia po kolei wszystkie makra, aby zregenerować
cały zestaw. Poszczególne pliki `.sh` istnieją osobno dla każdej sekcji, dzięki czemu zrzuty ekranu
jednej strony można zregenerować bez ponownego uruchamiania wszystkiego (każde makro
zajmuje od kilku sekund do ponad minuty).

Najważniejsze flagi wiersza poleceń:

- `--read-only` — nie zapisuje żadnych zmian wprowadzonych podczas przebiegu.
- `--no-gui` / `--no-audio` — tryb quasi-bezgłowy; niektóre makra nadal wymagają GUI,
  ponieważ bez niego symulator „pomija” operacje (patrz komentarz w `screenshots.sh`).
- `--radio-settings <file>.bin` — z którymi zapisanymi ustawieniami nadajnika ma nastąpić start
  (to właśnie sprawia, że zrzuty ekranu są specyficzne dla języka i nadajnika — przebieg niemiecki
  używa niemieckiego pliku `.bin`).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — wskazują symulatorowi modele/firmware/dokumenty/audio,
  które ma widzieć, tak aby zrzuty ekranu odzwierciedlały celowo przygotowaną zawartość, a nie
  to, co akurat znajduje się na prawdziwej SD card.
- `--exec <script>.lua` — makro uruchamiane po starcie.

Każda rodzina nadajników (X20S, X20 PRO, X20 PRO AW, X18S) ma własny plik binarny
symulatora i wymaga własnego pliku `--radio-settings` dla każdego języka (np.
`x20s-en.bin`, `x20pro-en.bin`), ponieważ interfejs użytkownika nieznacznie różni się między
nadajnikami, a plik ustawień przenosi również język.

## API makr

Makra to zwykły kod Lua, sterujący globalnym obiektem `simulator`:

| Wywołanie | Przeznaczenie |
|---|---|
| `simulator.loadModel("name.bin")` | Ładuje określony plik modelu przed nawigacją — każda sekcja podręcznika używa modelu przygotowanego do zademonstrowania danej sekcji (patrz lista modeli poniżej). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Naciska klawisz sprzętowy — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE` itd. Czas przytrzymania wyzwala długie naciśnięcie (otwiera menu kontekstowe). |
| `simulator.turnRotaryEncoder(n)` | Obraca enkoder o `n` kliknięć (wartość ujemna = w przeciwną stronę) — podstawowy sposób przemieszczania kursora między polami. |
| `simulator.touch(x, y)` | Dotknięcie określonych współrzędnych ekranu — stosowane tam, gdzie dotyk jest jedynym sposobem dotarcia do czegoś (np. przełączenie układu klawiatury). |
| `simulator.setAnalog(channel, value)` | Ustawia bezpośrednio pozycję drążka/potencjometru/suwaka (`0`-`3` to cztery główne drążki, `ANALOG_LAST_SLIDER` to ostatni suwak), dzięki czemu zrzuty ekranu pokazują celową, powtarzalną wartość, a nie wartość domyślną symulatora. |
| `simulator.setSwitch(n, position)` | Ustawia pozycję przełącznika fizycznego. |
| `simulator.setDateTime({...})` | Ustala na stałe zegar symulatora, aby znaczniki czasu na zrzutach ekranu (oraz wszystko zależne od czasu) były powtarzalne między przebiegami. |
| `simulator.screenshot(path)` | Zapisuje bieżący ekran do pliku PNG, względem katalogu roboczego makra (stąd ścieżki `../assets/...` wewnątrz każdego makra). |
| `simulator.connectUsb()` | Symuluje podłączenie USB, na potrzeby uchwycenia menu USB. |
| `simulator.sleep(seconds)` | Czeka na ustabilizowanie animacji/wartości telemetrycznej przed wykonaniem zrzutu. |

Plik `manual/macros/common.lua` jest ładowany przez `dofile` w większości makr i jedynie ustala
datę/godzinę, aby każde makro startowało z tego samego symulowanego momentu.

## Modele używane w poszczególnych sekcjach

Plik `manual/notes.txt` (przeniesiony nieformalnie, jeszcze nieskopiowany do tego repozytorium)
przypisuje każdemu makru plik modelu `.bin`, od którego zależy, wraz z uzasadnieniem — np.
`model-mixes.lua` używa `rarebear.bin`, `model-fm.lua` używa `zblank.bin` (model
z celowo pustą konfiguracją trybów lotu), `model-trims.lua` używa
`blaster.bin` (skonfigurowanego z przesuniętymi trymami, aby zademonstrować zakres trymu).
Przeniesienie treści tego pliku do właściwej dokumentacji jest częścią
prac fazy 2 opisanych poniżej.

## Co obejmuje przeniesienie tego do nowego repozytorium (jeszcze niewykonane)

- Decyzja, czy makra będą uruchamiane bezpośrednio z tego repozytorium (co wymaga
  lokalnej instalacji symulatora Ethos, tak jak w starym repozytorium), czy przez CI z symulatorem
  dołączonym/pobieranym w ramach przepływu pracy.
- Przebudowa płaskich ścieżek wyjściowych `../assets/...` tak, aby odpowiadały układowi zasobów
  tego repozytorium — osobno dla każdej strony i lokalizacji (`docs/<locale>/assets/`).
- Jeden plik `--radio-settings ... .bin` i jeden przebieg generowania zrzutów ekranu na każdą lokalizację,
  gdy tylko pojawi się lokalizacja inna niż `en` — zrzuty ekranu są specyficzne dla języka interfejsu i
  nie mogą być współdzielone między lokalizacjami.
- Decyzja, jaką część z około 40 istniejących makr przenieść bez zmian, a jaką napisać
  od nowa pod kątem obecnej struktury nawigacji w tym repozytorium (niektóre makra
  generują zrzuty ekranu dla sekcji, które nie odpowiadają już jeden do jednego układowi stron
  tego podręcznika).
