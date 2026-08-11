---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Wersjonowanie

Ethos dostarcza obecnie oprogramowanie sprzętowe oznaczone numerami wersji (1.6.x), a producent zapowiedział przejście na oznaczenia oparte na roku (np. „Ethos26”). Ten podręcznik musi utrzymywać dokumentację starszych wersji dostępną i poprawną, podczas gdy nowe wersje są aktywnie opracowywane — na tej stronie opisano, jak to działa.

## Jak to działa

Wersjonowanie obsługuje [mike](https://github.com/jimporter/mike), narzędzie rekomendowane przez samo Material for MkDocs. `.github/workflows/deploy.yml` uruchamia `mike deploy` zamiast publikować bezpośrednio do katalogu głównego `gh-pages`: każda wersja jest budowana i zatwierdzana we własnym podkatalogu (`/1.6/`, `/26/`, …), a `manual.rt-rc.com/` przekierowuje do tej wersji, która aktualnie ma alias `latest`. Material automatycznie wyświetla listę rozwijaną wyboru wersji, odczytując `versions.json` (utrzymywany przez `mike`) — jest to niezależne od przełącznika języka i dobrze się z nim komponuje: wersja stanowi zewnętrzny segment ścieżki, a język (gdy pojawi się więcej niż `en`) wewnętrzny, np. `manual.rt-rc.com/26/fr/...`.

Wykorzystywany jest tu ten sam mechanizm „podkatalogu na `gh-pages`”, co w przypadku [podglądów PR](index.md#pr-previews) — katalogi wersji tworzone przez `mike` oraz katalog `pr-preview/` współistnieją na tej samej gałęzi bez konfliktów, ponieważ każdy z nich modyfikuje wyłącznie własne ścieżki.

## Układ źródeł: `main` + zamrożone gałęzie

- **`main` zawsze odpowiada treści bieżącej/najnowszej wersji oprogramowania sprzętowego.** Bieżąca edycja odbywa się właśnie tutaj, dokładnie tak jak obecnie — normalny proces współtworzenia nie ulega zmianie.
- Gdy podręcznik nowej wersji oprogramowania sprzętowego musi zacząć się różnić od treści na `main`, **najpierw utwórz gałąź nazwaną od starej wersji**, np. `1.6`, aby trwale ją zamrozić. `main` staje się wtedy treścią nowej wersji.
- Zamrożona gałąź nie jest martwa — nadal może otrzymywać poprawki poprzez własne PR-y. Przestaje jedynie śledzić rozwój nowej wersji.

## Tworzenie nowej wersji

Gdy trzeba rozpocząć podręcznik kolejnej wersji (np. Ethos26):

1. Z gałęzi `main` utwórz i wypchnij zamrożoną gałąź dla pozostawianej wersji:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   Kopia pliku `.github/workflows/deploy.yml` w gałęzi `1.6` będzie odtąd trwale wykonywać `mike deploy --push --update-aliases 1.6 latest` przy każdym pushu do tej gałęzi — jest to poprawne w niezmienionej postaci i nie wymaga edycji, ponieważ gałąź stanowi pełną migawkę wraz z własną konfiguracją CI.

2. W gałęzi `main` zmodyfikuj `.github/workflows/deploy.yml`: zmień oznaczenie wersji w kroku `Deploy version 1.6 with mike` (oraz jego nazwę) z `1.6` na etykietę nowej wersji (np. `26`). To **jedyna** wymagana zmiana, aby rozpocząć publikowanie nowej wersji — kolejny push do `main` opublikuje ją w `/26/` i przeniesie tam alias `latest`, podczas gdy `/1.6/` pozostanie dokładnie w niezmienionym stanie.

3. Zaktualizuj treść nowej wersji na `main` odpowiednio do faktycznych zmian — nowe lub zmienione nazwy sekcji menu, nowe zrzuty ekranu, zaktualizowana terminologia. Sekcja `nav` w `mkdocs.yml` może się dowolnie różnić między gałęziami; nie ma współdzielonej konfiguracji, którą trzeba by synchronizować.

4. Dodaj nazwę nowej gałęzi do listy wyzwalaczy `branches:` w `.github/workflows/pr-preview.yml`, jeśli PR-y kierowane do niej również mają otrzymywać podglądy na żywo (zamrożone gałęzie zwykle tego nie potrzebują, ponieważ przyjmują jedynie sporadyczne PR-y z poprawkami).

## Zrzuty ekranu w różnych wersjach

Zrzuty ekranu są wykonywane z określonej kompilacji Ethos (zobacz [Proces tworzenia zrzutów ekranu](screenshot-pipeline.md)) i należą do tej gałęzi, której interfejs przedstawiają — utworzenie nowej wersji w naturalny sposób rozgałęzia również zestaw zrzutów ekranu wraz z całą resztą, więc `1.6/assets/` oraz (po ponownym wygenerowaniu dla nowego interfejsu) `docs/en/assets/` w gałęzi `main` rozchodzą się niezależnie od punktu rozgałęzienia.
