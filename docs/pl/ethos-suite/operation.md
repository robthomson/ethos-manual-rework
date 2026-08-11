---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Obsługa

## Sekcja powitalna

**Update News** — informacje o wydaniu oraz zalecenia dotyczące kopii
zapasowej przed aktualizacją. Ethos 1.6.0+ wymaga, aby wewnętrzny moduł
RF oraz odbiorniki TD/TW/AP/AP Plus miały wersję v3.0.1+, aby móc
korzystać z wprowadzonych usprawnień. Włączenie opcji **Pre-releases**
(z serwerem ustawionym na GitHub — patrz [Ustawienia
Suite](#suite-settings)) powoduje wyświetlanie w tym miejscu również
kompilacji przedpremierowych, obok pełnej historii wydań.

**Strona internetowa Ethos** — wbudowany widok ethos.frsky-rc.com:
materiały, odnośniki do szablonów modeli oraz lista obsługiwanych
nadajników.

## Sekcja Radio

Zarządza podłączonym nadajnikiem. Uruchom go w [trybie
bootloadera](../getting-started/usb-connection-modes.md#bootloader-mode)
i podłącz przez USB — Suite wyświetli typ nadajnika (np. „X20”) po jego
wykryciu.

### Informacje o nadajniku

- **Ethos** — zainstalowane wersje firmware'u/bootloadera; **Manage
  Ethos** przenosi do ich aktualizacji, jeśli są nieaktualne.
- **RF Module** — zainstalowany firmware wewnętrznego modułu RF; **Manage
  internal module** przenosi do jego aktualizacji, jeśli jest
  nieaktualny.
- **Model manager** / **Lua library** / **Download center** — skróty do
  tych narzędzi.

### Aktualizacja Ethos {: #updating-ethos }

Zakładka **Ethos** wyświetla obok siebie wersje firmware'u, bootloadera,
karty SD/eMMC (pliki audio) oraz pamięci flash (bitmapy systemowe) —
pliki systemowe w pamięci flash są teraz aktualizowane wraz z
firmware'em i nie są już zarządzane osobno.

- **Write outdated components** — aktualizuje tylko nieaktualne elementy.
- **Write all components** — aktualizuje wszystko niezależnie od wersji.
- Osobne opcje **Write firmware**, **Write bootloader**, **Write audio
  files**, uruchamiane kliknięciem ciemnoszarego przycisku obok wybranej
  opcji.
- **Flash from a local file** — pomija pobieranie i wykorzystuje plik
  firmware'u już zapisany na dysku.

Wybór wydania oznacza najpierw wskazanie **gałęzi** (Stable/Testing), a
następnie wersji. Przed aktualizacją pojawia się monit o wykonanie kopii
zapasowej (**Go to backup page**) — wykonaj ją. Jeśli wewnętrzny moduł RF
nie ma wersji v3.0.1+, Ethos 1.6.0+ wymaga jego aktualizacji przed
kontynuowaniem (**Go to Module manager** wgrywa firmware automatycznie, a
następnie aktualizacja Ethos jest wznawiana) — natomiast w odbiornikach
TD/TW/AP/AP Plus należy potem usunąć telemetrię i wykryć ją ponownie, aby
pobrać zaktualizowane nazwy czujników.

Postęp aktualizacji jest pokazywany krok po kroku (przełączanie do
bootloadera, pobieranie, kopiowanie, odmontowywanie, zapis, odświeżanie,
„Update successful!”) — postęp zapisu jest również odzwierciedlany na
ekranie samego nadajnika.

!!! note "Aktualizacje przedpremierowe"
    Pliki wersji przedpremierowej mogą się zmieniać bez zmiany numeru
    wersji, czego Suite nie potrafi wykryć — zawsze wgraj ponownie wersję
    przedpremierową, której używasz, gdy stanie się ona pełnym wydaniem.
    W razie wątpliwości sprawdź datę firmware'u w
    [System → Info](../system-setup/information.md).

!!! note "Aktualizacja z Ethos 1.2.8 lub starszego"
    Suite może nie być w stanie w pełni automatycznie wgrać
    firmware'u/bootloadera z tak starej wersji — zamiast tego pojawi się
    okno z instrukcją ręcznego wgrywania. W obu przypadkach przed
    odłączeniem USB należy ręcznie odmontować dyski.

Pliki bitmap systemowych są teraz aktualizowane automatycznie wraz z
firmware'em (bez osobnego zarządzania); pliki audio aktualizuje się przez
**Write all components** lub **Write audio files** (pobiera wybrany pakiet
językowy, np. „English audio pack”).

### Menedżer modułu RF

Wybierz wersję (zwykle najnowszą) i użyj **Flash module**, aby
zaktualizować firmware wewnętrznego modułu RF bezpośrednio — po
zakończeniu wyświetlany jest komunikat „...has been flashed
successfully”. Operacja ta jest również uruchamiana automatycznie w ramach
obowiązkowej ścieżki aktualizacji do v3.0.1 opisanej powyżej.

### Tryb Ethos

**Switch to Ethos** uruchamia ponownie nadajnik, wychodząc z trybu
bootloadera do działającego systemu Ethos (sygnalizuje to zielona ikona
USB na nadajniku oraz zniknięcie „(Bootloader Mode)” z nagłówka Suite).
Jest to wymagane, aby **Download center** mogło wykorzystywać nadajnik
jako pośrednika przy wgrywaniu firmware'u do modułów, odbiorników,
czujników i serw. Przycisk zmienia się wówczas na **Switch to
Bootloader**, umożliwiając powrót. **Eject Drives** bezpiecznie odłącza
nadajnik.

### Menedżer modeli

Tworzy kopię zapasową plików modeli i ustawień na dysku lub przywraca
wcześniejszą kopię.

!!! warning
    Przywracanie **nie** przywraca firmware'u — po przywróceniu
    modeli/ustawień należy osobno wgrać wersję firmware'u odpowiadającą
    tej kopii zapasowej (patrz [Aktualizacja
    Ethos](#updating-ethos)), ponieważ pliki modeli nie są wstecznie
    kompatybilne.

- **Backup Location** — wskaż folder (zapamiętywany osobno dla każdego
  typu nadajnika); poniżej wyświetlana jest data i godzina ostatniej kopii
  zapasowej.
- **Backup** — zapisuje pliki modeli wraz z informacją o bieżącej wersji
  Ethos.
- **Restore** — wybierz, które elementy przywrócić: Audio (domyślnie
  wyłączone), Scripts, Screenshots, System Bitmaps (domyślnie wyłączone —
  zarządzane teraz wraz z firmware'em), Models (w tym pliki tekstowe
  [listy kontrolnej użytkownika](../how-to/user-defined-checklist.md)
  przechowywane razem z nimi), Language, User Bitmaps, Logs, System
  Settings.

### Biblioteka Lua

Przeglądanie i instalacja jednym kliknięciem skryptów/narzędzi Lua ze
zdalnej biblioteki FrSky (lub instalacja z lokalnego archiwum zip);
zainstalowane skrypty są wyświetlane obok zdalnego katalogu, jeśli
jakiekolwiek istnieją.

## Sekcja Tools

- **Download center** — pobieranie dowolnego firmware'u ze strony FrSky
  oraz (gdy nadajnik pracuje w trybie Ethos) wykorzystanie go jako
  pośrednika do wgrania firmware'u do modułu, czujnika, serwa lub
  odbiornika podłączonego przez złącze aktualizacji S.Port. Wybierz produkt
  z listy (np. odbiornik TW SR8), przejrzyj dostępne **assets**, użyj
  **Download**, aby zapisać lokalnie, lub **Flash**, aby wgrać
  bezpośrednio do podłączonego urządzenia — pasek postępu śledzi zapis,
  kończąc się komunikatem „...has been flashed successfully!”

- **Image manager** — konwertuje obrazy do natywnego formatu Ethos
  (32-bitowy BMP, RGB, kanał alfa dodawany tylko w razie potrzeby) o
  wybranym rozmiarze, z zachowaniem proporcji. Rozmiary odniesienia:
  obrazy modeli 300×280 (X20) / 180×168 (X18); obrazy pełnoekranowe
  800×480 (X20) / 480×320 (X18) — zasady nazewnictwa bitmap opisano w
  [Menedżerze plików](../system-setup/file-manager.md#top-level-folders).
  Umożliwia też bezpośrednie przeglądanie folderów `bitmaps/gps`,
  `bitmaps/models` i `bitmaps/user` w nadajniku, z obsługą przesyłania
  plików. Dodaj obrazy do listy konwersji przyciskiem **+** (format TIFF
  nie jest obsługiwany), wybierz ścieżkę wyjściową (folder lokalny;
  bezpośrednio do nadajnika, do obrazów modeli/użytkownika/GPS; albo
  aktualnie otwarty folder nadajnika), a opcjonalnie włącz automatyczne
  otwieranie folderu wynikowego lub wymuszenie kanału alfa.

- **Audio manager** — konwertuje pliki dźwiękowe do formatu Ethos (PCM
  liniowy, 32 kHz, mono, 16-bit little-endian). Dodaj pliki przyciskiem
  **+**, wybierz folder lokalny lub wyślij je bezpośrednio do folderu
  `audio` w nadajniku (przenosząc je następnie do właściwego podfolderu
  głosowego), opcjonalnie z automatycznym otwarciem lokalizacji docelowej.

- **Lua development tools** — **Lua Docs** prowadzi do przewodnika
  referencyjnego Ethos Lua (patrz również wątek *FrSky - ETHOS Lua Script
  Programming* na rcgroups); **Lua Demo Scripts** prowadzi do przykładowych
  skryptów na GitHubie Ethos-Feedback-Community; **Debug** otwiera okno
  dziennika na żywo dla śladów `print()` z Lua przesyłanych przez
  USB-Serial, gdy nadajnik pracuje w trybie Serial:

  1. Podłącz nadajnik do Suite w normalny sposób i przełącz go w tryb
     Ethos.
  2. Edytuj skrypty Lua bezpośrednio na zamontowanym dysku nadajnika, w
     dowolnym edytorze kodu.
  3. Otwórz **Lua Development Tools** → **START DEBUG** — spowoduje to
     ponowne uruchomienie nadajnika w trybie Serial/debug i ponowną
     inicjalizację skryptów.
  4. Wyjście `print()` każdego aktywnego skryptu jest przesyłane do
     terminala Suite.
  5. **STOP DEBUG** przywraca normalny tryb Ethos, umożliwiając dalszą
     edycję.

- **DFU Flasher** — wgrywa bootloader przez połączenie USB przy wyłączonym
  zasilaniu (DFU), działając nawet przy całkowicie uszkodzonym
  firmwarze, ponieważ bazowy bootloader ST znajduje się w pamięci ROM.
  Użyj **Select Bootloader**, aby wybrać pobrany plik (Suite podaje jego
  wersję/przydatność), podłącz **wyłączony** nadajnik, a następnie użyj
  **Flash**.

  !!! note "„Nie wykryto połączenia z nadajnikiem!”"
      Zwykle przyczyną jest brakujący lub nieprawidłowy sterownik DFU.
      Większość komputerów z Windows 10+ obsługuje systemy Tandem za
      pomocą domyślnego sterownika USB DFU, ale Windows Update czasami
      zastępuje go sterownikiem ogólnym, który nie działa — sprawdź
      Menedżera urządzeń i rozważ użycie narzędzia takiego jak Impulse
      Driver Fixer. Użytkownicy Horus X10 mogą w szczególności musieć
      ręcznie zainstalować sterownik USB bootloadera STM32 (Impulse Driver
      Fixer lub Zadig), ponieważ Windows 10 nie instaluje go domyślnie.

- **Repair Tool** — dla X18/S, TW Lite, XE oraz X20 Pro/R/RS: formatuje
  ponownie pamięć wewnętrzną, gdy nadajnik nie może odczytać pamięci NAND
  lub zapisać ustawień.

## Sekcja Others

- **Documentation** — odnośniki do GitHuba Ethos-Feedback-Community,
  oficjalnych podręczników Ethos (do pobrania) oraz FAQ Ethos Suite.
- **Ethos Github** — wydania i system zgłaszania błędów (przed
  utworzeniem nowego zgłoszenia przeszukaj istniejące).

### Ustawienia Suite {: #suite-settings }

- **Language** — czeski, niemiecki, angielski, hiszpański, francuski,
  hebrajski, włoski, niderlandzki, norweski, portugalski, słoweński,
  chiński.
- **Server location** — **FrSky server** lub **GitHub** (wymagany do
  dostępu do wersji przedpremierowych, opisanego powyżej).
- **Debug options** — włączanie/wyłączanie okna błędu krytycznego;
  włączenie pełnego rejestrowania diagnostycznego Suite (nie tylko awarii);
  otwarcie folderu z dziennikami.
- **Version** / **Update Suite** — bieżąca wersja oraz ręczne sprawdzenie
  aktualizacji.
- **About** — podziękowania za wykorzystane komponenty.

## Obsługa z wiersza poleceń

Ethos Suite można uruchomić z terminala:

| Flaga | Działanie |
|---|---|
| `--help` | Wyświetla pomoc wiersza poleceń. |
| `--version` | Wyświetla zainstalowaną wersję Suite. |
| `--list-radios` | Wyświetla listę wszystkich obsługiwanych nadajników FrSky. |
| `--radio-components --radio {RADIO}` (lub `--radio auto`) | Wyświetla listę komponentów podłączonego nadajnika wraz z ich ścieżkami. `auto` wykrywa automatycznie; podaj `{RADIO}`, jeśli podłączony jest więcej niż jeden nadajnik. |
| `--get-path {COMPONENT}` | Zwraca ścieżkę do komponentu — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` lub `I18N`. |
| `--serial start` \| `--serial stop` | Włącza/wyłącza tryb debugowania szeregowego. |

!!! note
    Suite w ogóle się nie uruchomi, jeśli nie rozpozna prawidłowego
    polecenia.
