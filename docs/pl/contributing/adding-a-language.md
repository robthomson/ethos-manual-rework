---
translated_from: 23549d0bf136da221c75de9a0c5695864d338cab
---

# Dodawanie nowego języka

Podręcznik krok po kroku, jak uruchomić nową lokalizację od zera do w pełni
przetłumaczonego, w pełni nawigowalnego manuala — napisany z myślą o tym (człowieku
lub agencie), kto zajmie się kolejnym językiem. Każdy z poniższych kroków został
faktycznie wykonany, w tej właśnie kolejności, dla języków `de`, `fr`, `es`, `it`,
`pt-BR` i `zh`; wymienione pułapki to rzeczywiste błędy napotkane w trakcie, a nie
hipotezy.

## Lista kontrolna

Przechodź po kolei; każdy punkt prowadzi do sekcji z konkretnymi poleceniami
i pułapkami napotkanymi w praktyce. Nie przeskakuj od razu do kroku 4 — kroki 1 i 3
są tanie i pozwalają uniknąć późniejszych poprawek.

- [ ] **[1](#1-confirm-the-locale-code-before-touching-anything)** — Potwierdź, że Ethos udostępnia interfejs w tym języku, i wybierz kod lokalizacji, dla którego `mkdocs-material` faktycznie posiada szablon (niekoniecznie kod używany wewnętrznie przez narzędzia FrSky — `pb` kontra `pt-BR` sprawiło nam tu kłopot).
- [ ] **[2](#2-add-the-locale-to-mkdocsyml)** — Dodaj lokalizację do `mkdocs.yml` (jeszcze bez `nav_translations`).
- [ ] **[3](#3-seed-a-glossary-in-scriptstranslatepy)** — Utwórz wstępny słownik ~30 terminów w `GLOSSARIES` w pliku `scripts/translate.py`.
- [ ] **[4](#4-translate)** — Uruchom `scripts/translate.py --only <code>` (najpierw dry-run); potwierdź `0 failed`.
- [ ] **[5](#5-check-for-existing-screenshots-before-considering-the-simulator)** — Sprawdź stare repozytorium `ethos-manual` pod kątem gotowego zestawu zrzutów ekranu, zanim założysz, że potrzebny jest potok symulatora; jeśli zestaw pasuje, skopiuj go hurtowo i sprawdź wizualnie wyrywkowo.
- [ ] **[6](#6-check-and-fix-anchor-links)** — Uruchom `python scripts/check_anchors.py --fix`.
- [ ] **[7](#7-verify-for-real)** — `mkdocs build --strict` i sprawdź, czy `$?` wynosi `0` (a nie tylko czy wyjście wygląda czysto); `check_anchors.py` raportuje 0.
- [ ] **[8](#8-add-nav_translations-once-after-page-coverage-is-complete)** — Gdy pokrycie stron jest kompletne, dodaj `nav_translations` (etykiety liści z nagłówka H1 każdej strony, zakładki sekcji ze słownika).
- [ ] **[9](#9-ship-it)** — Zatwierdź zmiany, wypchnij, obserwuj Action, zweryfikuj na żywo (uwzględnij opóźnienie propagacji CDN dla zupełnie nowych ścieżek).

## 1. Potwierdź kod lokalizacji, zanim cokolwiek ruszysz {: #1-confirm-the-locale-code-before-touching-anything }

Dwie odrębne rzeczy muszą się zgadzać, a pomyłka w którejkolwiek z nich jest
uciążliwa do odkręcenia później (kod na stałe zapisuje się w adresach URL):

- **Czy Ethos rzeczywiście udostępnia interfejs w tym języku?** Manual w języku,
  którego firmware nie obsługuje, wprowadza w błąd zamiast pomagać. Aplikacja
  desktopowa [Ethos Suite](https://www.frsky-rc.com/) firmy FrSky zawiera plik
  `i18n/*.json` dla każdego obsługiwanego języka — po instalacji lokalnej znajduje
  się on w `Program Files/Ethos Suite/i18n/`. Ta lista (`cs`, `de`, `en`, `es`,
  `fr`, `he`, `it`, `nl`, `no`, `pb`, `sk`, `zh-CN` wg ostatniego sprawdzenia) jest
  wiarygodnym wyznacznikiem tego, co obsługuje sam Ethos.
- **Czy `mkdocs-material` udostępnia szablon przełącznika języka dla tego kodu?**
  To *inna* lista i obie nie zawsze się pokrywają — folder Ethos Suite nazywa się
  dosłownie `pb`, ale Material nie ma pliku `partials/languages/pb.html`, tylko
  `pt-BR.html`. Użycie `pb` buduje się poprawnie aż do etapu generowania mapy
  witryny po zakończeniu budowania w `mkdocs build`, gdzie proces kończy się
  awarią `jinja2.exceptions.TemplateNotFound` — **a ten komunikat nie zawiera słowa
  „error” ani „warning”**, więc przeszukiwanie wyjścia budowania pod tym kątem
  (całkowicie rozsądne działanie) zaraportuje czyste budowanie, które w
  rzeczywistości zakończyło się kodem niezerowym. Zawsze sprawdzaj `$?` po
  `mkdocs build --strict`, a nie tylko wypisane komunikaty. Aby zobaczyć dokładne
  kody obsługiwane przez Material:

  ```python
  import material
  from pathlib import Path
  p = Path(material.__file__).parent / "templates" / "partials" / "languages"
  print(sorted(x.stem for x in p.glob("*.html")))
  ```

## 2. Dodaj lokalizację do `mkdocs.yml` {: #2-add-the-locale-to-mkdocsyml }

```yaml
languages:
  - locale: <code>
    name: <native display name>
    build: true
```

Jeszcze bez `nav_translations` — to krok 6, gdy będzie już realna treść, do której
można dopasować etykiety.

## 3. Utwórz wstępny słownik w `scripts/translate.py` {: #3-seed-a-glossary-in-scriptstranslatepy }

Dodaj wpis `GLOSSARIES["<code>"]` (istniejące wpisy `fr`/`de`/`es`/`it` pokazują,
jaki zakres terminów objąć — nazwy powierzchni sterowych, słownictwo dotyczące
miksów/wyjść/timerów/trymów, przełączniki, czujniki itd.). To właśnie utrzymuje
spójność terminologii od pierwszej przetłumaczonej strony, zamiast pozwalać jej
dryfować z strony na stronę. ~30 terminów wystarczy; to punkt wyjścia do
rozbudowy, a nie kompletny słownik.

Jeśli w trakcie działania konsola zgłosi `UnicodeEncodeError` — trafiło się to
konkretnie przy `zh` — to dlatego, że konsola Windows domyślnie używa `cp1252`,
która nie potrafi zakodować pism niełacińskich. Zostało to już naprawione na
początku skryptu (`sys.stdout.reconfigure(encoding="utf-8", ...)`); jeśli problem
powróci, właśnie tam należy szukać.

## 4. Tłumaczenie {: #4-translate }

```bash
python scripts/translate.py --only <code> --dry-run   # confirm scope/cost first
python scripts/translate.py --only <code> --yes
```

Niezależne lokalizacje mogą działać **równolegle** (osobne procesy w tle) —
odczytują wyłącznie współdzielone pliki (`docs/en/`, `mkdocs.yml`), a zapisują do
całkowicie odrębnych drzew `docs/<code>/`, więc nie ma wyścigu. Cztery lokalizacje
tłumaczone jednocześnie zakończyły się mniej więcej w tym samym czasie
rzeczywistym co jedna.

Przed przejściem dalej sprawdź w logu wpis `Done: N translated, 0 failed`.

## 5. Sprawdź istniejące zrzuty ekranu, zanim pomyślisz o symulatorze {: #5-check-for-existing-screenshots-before-considering-the-simulator }

**Nie zakładaj, że nowe zrzuty ekranu wymagają uruchomienia potoku symulatora —
najpierw sprawdź.** Poprzednie repozytorium
([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), zwykle klonowane jako
katalog równoległy) może już zawierać przechwycony, przygotowany przez zespół FrSky
zestaw zrzutów dla danego języka, leżący bezużytecznie. Tak było w przypadku
niemieckiego, francuskiego (folder `french_LT/` — nie mniejszy, niekompletny
`french/`), włoskiego i hiszpańskiego; nie było nic dla portugalskiego ani
chińskiego. Sprawdź pokrycie nazw plików względem tego, do czego odwołuje się
obecnie to repozytorium:

```python
from pathlib import Path
old_repo_lang_assets = Path("../ethos-manual/<language-folder>/assets")  # sibling checkout
current = {p.name for p in Path("docs/en/assets").iterdir() if p.suffix.lower() == ".png"}
old = {p.name for p in old_repo_lang_assets.glob("*.png")}
print(f"{len(old & current)} / {len(current)} would match")
```

Wysoki stopień zgodności (w praktyce ≥90%) oznacza, że wystarczy zwykłe skopiowanie
do `docs/<code>/assets/` — dzięki `fallback_to_default` w `mkdocs.yml` to *wszystko*,
czego potrzeba; żadnych zmian w plikach markdown. **Sprawdź wizualnie co najmniej
jeden skopiowany obraz**, zanim zaufasz dopasowaniu (otwórz go, potwierdź, że to
faktycznie interfejs w docelowym języku, a nie nieaktualne lub niepasujące ujęcie)
— zgodność nazw plików nie gwarantuje ściśle zgodności treści, choć jak dotąd
zawsze tak było.

Jeśli dopasowania nie ma (portugalski, chiński lub dowolny przyszły język, którego
stare repozytorium nigdy nie obejmowało), lokalizacja poprawnie i automatycznie
korzysta z angielskich zrzutów ekranu. To oczekiwany, działający stan; realne
zamknięcie tej luki oznacza przeniesienie/uruchomienie właściwego potoku makr
względem symulatora (patrz [Potok zrzutów ekranu](screenshot-pipeline.md)), co
wykracza poza zakres przebiegu tłumaczenia tekstu i wymaga lokalnej instalacji
symulatora.

## 6. Sprawdź i napraw odnośniki kotwic {: #6-check-and-fix-anchor-links }

Tłumaczenie nagłówka zmienia jego automatycznie generowany slug, co po cichu psuje
każdy odnośnik `#that-heading-slug` z innej strony — i **nie jest to błąd
budowania**: `mkdocs build --strict` na tym nie zawiedzie, więc nic ci o tym nie
powie poza martwym linkiem, w który kliknie czytelnik.

```bash
python scripts/check_anchors.py         # report only
python scripts/check_anchors.py --fix   # pin every finding, in en + every locale that has the page
```

To realna, powracająca klasa błędów, a nie jednorazowe porządki — każda dotychczas
dodana lokalizacja ujawniała kilka nowych przypadków (tych, które akurat zbiegły
się z rozjazdem sluga przetłumaczonego dla danej lokalizacji względem angielskiego,
czego tłumaczenie *innej* lokalizacji nie powodowało). Uruchamiaj skrypt po każdej
partii nowych lub zaktualizowanych tłumaczeń. Domyślnie sam przebudowuje witrynę
(najpierw `mkdocs build --strict`), więc wyniki nigdy nie są nieaktualne.

## 7. Zweryfikuj naprawdę {: #7-verify-for-real }

```bash
mkdocs build --strict; echo "exit code: $?"   # must be 0, not just free of "error"/"warn" text
python scripts/check_anchors.py                # must report 0
```

## 8. Dodaj `nav_translations` — raz, po skompletowaniu pokrycia stron {: #8-add-nav_translations-once-after-page-coverage-is-complete }

Etykiety zakładek i paska bocznego w `nav:` nie pobierają automatycznie
przetłumaczonego tytułu strony danej lokalizacji, chyba że wpis nawigacji w ogóle
nie ma jawnej etykiety. Dodaj `nav_translations` we wpisie lokalizacji w
`mkdocs.yml` dopiero wtedy (a nie wcześniej), gdy lokalizacja ma pełne — lub
niemal pełne — pokrycie stron; tłumaczenie elementów interfejsu przed treścią, do
której prowadzą, wygląda dziwnie. Etykiety liści należy skopiować dosłownie z
nagłówka H1 każdej przetłumaczonej strony (aby tekst w pasku bocznym dokładnie
odpowiadał nagłówkowi strony); etykiety zakładek sekcji (Strona główna, Pierwsze
kroki, ...) powinny być zgodne ze słownikiem z kroku 3. Wyodrębnij każdy H1
programowo, zamiast przepisywać etykiety ręcznie — jest to szybsze i eliminuje
ryzyko pomyłki przy przepisywaniu:

```python
import re
h1 = re.search(r"^#\s+(.+)$", Path(f"docs/{code}/{rel_path}").read_text(encoding="utf-8"), re.MULTILINE).group(1).strip()
```

Pomiń `Translation Status` — to generowana, wyłącznie angielska strona dla
opiekunów, bez przetłumaczonego odpowiednika w żadnej lokalizacji.

## 9. Publikacja {: #9-ship-it }

Zatwierdź zmiany, wypchnij do `main` i obserwuj przebieg Action `Deploy Docs`.
CDN GitHub Pages może zwracać 404 dla zupełnie nowej ścieżki lokalizacji przez
pierwsze 15–30+ sekund po faktycznie udanym wdrożeniu — to opóźnienie propagacji
pamięci podręcznej na brzegu sieci, a nie awaria. Zanim zaczniesz się martwić,
potwierdź przez API GitHuba, że plik istnieje na `gh-pages`:

```bash
gh api "repos/<owner>/<repo>/contents/<version>/<code>/<path>?ref=gh-pages" --jq '.sha, .size'
```

a następnie ponów próbę pobrania adresu na żywo z krótkim odczekaniem.
