---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# Wkład w rozwój

## Dlaczego ten podręcznik powstał

Poprzedni podręcznik ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
rozpadł się na dwie niepowiązane połowy dla każdego języka. Drzewo angielskie
było wyłącznie **stanowiskiem do generowania zrzutów ekranu** — skrypty
powłoki sterujące prawdziwym symulatorem Ethos poprzez API makr Lua w celu
przechwytywania zrzutów interfejsu — bez żadnego źródła w Markdown (ani w
jakimkolwiek innym formacie tekstowym) dla właściwej treści podręcznika;
tekst angielski istniał jedynie jako stos eksportów PDF/ODT. Drzewo
francuskie było natomiast w pełni napisanym eksportem z GitBooka z realną
treścią, ale budowanym i utrzymywanym niezależnie, z własnym, osobnym
zestawem ręcznie wklejanych zrzutów ekranu. Pozostałe języki nie miały ani
jednego, ani drugiego. Nie istniało pojedyncze źródło prawdy, *z* którego
można by tłumaczyć, ani sposób na stwierdzenie, kiedy przetłumaczona strona
przestała być zgodna z (nieistniejącym) źródłem angielskim.

To repozytorium zaczyna od nowa, z jednym formatem dla każdej strony w
każdym języku: czysty Markdown, budowany za pomocą
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(ten sam zestaw narzędzi, którego używa [wingflight-docs](https://doc.wingflight.org)),
wdrażany na GitHub Pages przy każdym pushu do `main`.

## Sposób pracy

Przed treścią nie ma żadnego CMS-a ani edytora webowego — autorzy i
tłumacze pracują bezpośrednio w git, tak samo jak przy każdej innej zmianie
w tym repozytorium:

1. Utwórz gałąź z `main` (bezpośrednio w tym repozytorium — patrz uwaga o
   forkach poniżej).
2. Zedytuj odpowiedni plik (lub pliki) `.md` w katalogu `docs/en/`.
3. Podejrzyj wynik lokalnie poleceniem `mkdocs serve` (patrz główny
   [README](https://github.com/robthomson/ethos-manual-rework)) albo po
   prostu otwórz pull request i skorzystaj z automatycznego podglądu PR
   opisanego niżej.
4. Otwórz pull request.

Zrzuty ekranu, do których odwołuje się strona, leżą obok niej w
`docs/en/assets/` i są zwykłymi linkami do obrazów w Markdown — bez
specjalnej składni. Sposób ich generowania opisuje
[Potok zrzutów ekranu](screenshot-pipeline.md).

### Podglądy PR {: #pr-previews }

Każdy pull request kierowany do `main` otrzymuje własny działający podgląd,
budowany i wdrażany automatycznie przez `.github/workflows/pr-preview.yml`:
pod adresem `manual.rt-rc.com/pr-preview/<numer PR>/`, podlinkowany w
komentarzu bota w PR i aktualizowany przy każdym pushu. Jest usuwany
automatycznie po zamknięciu PR. Sama główna witryna (`manual.rt-rc.com`)
pozostaje nienaruszona — podglądy żyją obok niej w katalogu `pr-preview/`
na gałęzi `gh-pages`, który przetrwa każde wdrożenie produkcyjne.

Działa to wyłącznie dla gałęzi wypchniętych bezpośrednio do tego
repozytorium, nie dla forków — PR z forka nie otrzyma działającego podglądu
(GitHub celowo odmawia uprawnień zapisu dla `GITHUB_TOKEN` w przepływach
`pull_request` wyzwalanych z forka, tak aby fork nie mógł użyć CI do
wypchnięcia dowolnej treści na `gh-pages`). Osoby pracujące na forkach
nadal mogą korzystać z podglądu lokalnego przez `mkdocs serve`.

## Wersjonowanie

Podręczniki dla wielu wersji firmware'u (np. 1.6 obok przyszłego Ethos26)
znajdują się w tym samym repozytorium jako osobne gałęzie, z których każda
jest wdrażana pod własną ścieżką `manual.rt-rc.com/<wersja>/` z listą wyboru
wersji — pełny schemat oraz sposób utworzenia nowej wersji opisuje
[Wersjonowanie](versioning.md).

## Plan tłumaczeń {: #translation-plan }

Tłumacze (ludzie lub AI) pracują bezpośrednio w git, tak samo jak przy
każdej innej zmianie — bez CMS-a, bez osobnej aplikacji do tłumaczeń.
Pierwszy pilotaż francuski (kilka stron) potwierdził działanie całego
mechanizmu od początku do końca; poniżej opis, jak to faktycznie wygląda.

### Dodawanie/aktualizacja tłumaczenia {: #addingupdating-a-translation }

1. Utwórz gałąź, utwórz/zedytuj `docs/<locale>/<ta sama ścieżka co strona
   angielska>`, tłumacząc tekst. Elementy dosłowne (nazwy klawiszy takie jak
   `ENT`, `RTN`, nazwy elementów interfejsu widoczne na ekranie) pozostaw
   bez zmian.
2. Oznacz stronę informacją o tym, z którego commita angielskiego została
   przetłumaczona:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Ten sha znajdziesz poleceniem `git log -1 --format=%H -- docs/en/<path>`.
3. **Jeżeli strona angielska zawiera nagłówek, do którego inne strony
   odwołują się kotwicą** (sprawdź, wyszukując `#that-heading-slug` w całym
   `docs/en/`), nie dopuść, aby automatycznie generowany slug
   przetłumaczonego nagłówka zmienił cel odnośnika — przypnij jawnie ten sam,
   niezależny od języka identyfikator za pomocą `attr_list` (już włączonego):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Pominięcie tego nie zepsuje budowania, ale po cichu zepsuje przewijanie
   do kotwicy dla każdej innej, wciąż nieprzetłumaczonej strony, która
   odwołuje się do tego nagłówka poprzez mechanizm zastępczy.
4. Otwórz PR — [podejrzyj go](#pr-previews) jak każdą inną zmianę, łącznie z
   przełącznikiem języka.

### Zrzuty ekranu

Nie ma potrzeby niczego z góry duplikować. [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
sięga po plik angielski dla *dowolnego* zasobu, którego dana wersja językowa
nie posiada we własnej kopii — `../assets/foo.png` na przetłumaczonej stronie
po prostu działa, bez żadnych zmian, pokazując angielski zrzut ekranu, do
czasu aż pod tą samą nazwą pliku w `docs/<locale>/assets/` pojawi się
prawdziwy zlokalizowany zrzut, który od tej chwili po cichu przesłania
zasób zastępczy.

**`de` i `fr` mają już prawdziwe zlokalizowane zrzuty ekranu** — nie
przechwycone tutaj, lecz zaimportowane hurtowo ze starego repozytorium
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), które, jak się
okazało, zawierało niemal kompletne zestawy zrzutów dla poszczególnych
języków, przygotowane wcześniej przez sam zespół FrSky (`german/assets/`
oraz, dla francuskiego, `french_LT/assets/` — bardziej kompletny z dwóch
francuskich zestawów zasobów, a nie mniejszy `french/assets/`, który jego
README opisuje jako „w połowie gotowy"). Nazwy plików odpowiadają 1:1 naszym
z `docs/en/assets/`, więc import sprowadzał się do zwykłego kopiowania: 586
z 589 aktualnie używanych zrzutów trafiło za jednym razem do obu języków,
bez udziału symulatora. Nieliczne, które się nie zgadzały (2–3 pliki,
głównie nowsze strony, których makra starego repozytorium nigdy nie
obejmowały), nadal normalnie korzystają z angielskiego zasobu zastępczego.

Dla dowolnej wersji językowej innej niż `de`/`fr`, a także dla domknięcia
tych ostatnich kilku procent, przechwycenie nowych zrzutów oznacza
skorzystanie z [potoku zrzutów ekranu](screenshot-pipeline.md)
— przeniesienia/uruchomienia prawdziwego stanowiska makr na symulatorze —
ponieważ ta praca nie została wcześniej wykonana w źródle.

### Śledzenie nieaktualności

[Status tłumaczeń](translation-status.md) jest generowany automatycznie
przed każdym budowaniem (`hooks/i18n_status.py`, podpięty przez sekcję
`hooks:` w `mkdocs.yml` — działa lokalnie, w podglądach PR i na produkcji
tak samo, zawsze aktualny, nigdy nie commitowany do git) i porównuje
znacznik `translated_from` każdej wersji językowej z faktycznym commitem
ostatniej zmiany każdej strony angielskiej: **aktualna**, **nieaktualna**
(angielska poszła dalej) lub **brakująca**. Ta strona stanowi listę zadań —
bez GitHub Issues, bez grzebania w logach Actions.

### Tłumaczenie automatyczne (opcjonalne)

`scripts/translate.py` to samodzielny skrypt lokalny (niebędący częścią
budowania witryny ani CI), który przepuszcza tę samą listę
brakujących/nieaktualnych stron przez API Claude, tworząc pierwszą wersję
roboczą tłumaczenia każdej strony, automatycznie opatrzoną poprawnym
frontmatterem `translated_from:`:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Domyślnie odczytuje wszystkie wersje językowe z konfiguracji wtyczki `i18n`
w `mkdocs.yml` (`--only` ogranicza do wybranych), pomija wszystko, co jest
już aktualne, chyba że podano `--force`, i nigdy nie commituje ani nie
wypycha zmian — zapisuje jedynie pliki w `docs/<locale>/`, dokładnie tak,
jakby zostały zredagowane ręcznie. Przejrzyj diff, wykonaj sprawdzenie
[przypinania kotwic](#addingupdating-a-translation) dla każdego nowo
przetłumaczonego nagłówka, a następnie otwórz PR jak zwykle.

Prompt systemowy z góry przekazuje Claude'owi dziedzinę podręcznika
(firmware nadajników FrSky Ethos, odbiorcy z kręgu modelarstwa RC) oraz
listę terminów, których nigdy nie wolno tłumaczyć (nazwy fizycznych
klawiszy, nazwy protokołów, nazwy marek) — ta sama technika, którą stosuje
bliźniacze repozytorium
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite)
w swoim `bin/i18n/auto-translate.py`. Każda obsługiwana wersja językowa ma
własny słownik wbudowany w `GLOSSARIES` w skrypcie, co zapewnia spójność
terminologii od pierwszej przetłumaczonej strony.

Uruchomienie zupełnie nowej wersji językowej — od wyboru właściwego kodu
języka, przez tłumaczenie, zrzuty ekranu, poprawki kotwic, po etykiety
nawigacji — jest powtarzalnym procesem od początku do końca: pełny
przewodnik znajdziesz w [Dodawanie nowego
języka](adding-a-language.md).

### Etykiety nawigacji (`nav_translations`)

Etykiety zakładek i paska bocznego w `nav:` (np. „Model Setup") nie
przejmują automatycznie przetłumaczonego tytułu strony w danej wersji
językowej, chyba że wpis nawigacji w ogóle nie ma jawnej etykiety (np.
`- how-to/index.md` — MkDocs użyje wtedy nagłówka H1 samej strony). Wszędzie
tam, gdzie `nav:` podaje jawny ciąg `Etykieta: ścieżka.md` albo nazywa
sekcję (`Model Setup:` jako klucz słownika z elementami podrzędnymi),
etykieta pozostaje po angielsku, dopóki nie obejmie jej mapa
`nav_translations` danej wersji językowej w `mkdocs.yml` — dodawana dla
języka wtedy, gdy pokrycie stron jest już na tyle duże, że przetłumaczenie
elementów interfejsu przed większością treści nie wyglądałoby dziwnie. Mapa
dla `fr` została wypełniona, gdy francuski osiągnął pełne pokrycie stron;
każda etykieta liścia została skopiowana dosłownie z przetłumaczonego
nagłówka H1 danej strony, dzięki czemu tekst w pasku bocznym dokładnie
odpowiada nagłówkowi strony.
