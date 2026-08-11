---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Menedżer plików

![Menedżer plików — nadajnik](../assets/system-filemanager-radio.png)

Menedżer plików umożliwia przeglądanie pamięci nadajnika oraz wgrywanie
oprogramowania do wewnętrznego modułu RF, urządzeń podłączonych przez S.Port,
urządzeń OTA (Over-The-Air) i modułów zewnętrznych.

## Układ pamięci

Dotknij **Flash** (lub naciśnij `PAGE`, aby przełączyć dyski), aby przeglądać
wewnętrzny wirtualny dysk USB nadajnika, wykorzystywany do systemowych bitmap
i czcionek:

![Pamięć Flash](../assets/system-filemanager-flash.png)

- `bitmaps/system` — bitmapy używane na ekranach i jako ikony
- `fonts/` — czcionki dla poszczególnych wersji językowych

Zarówno bootloader, jak i samo oprogramowanie systemowe znajdują się w tej
wewnętrznej pamięci flash — dotyczy to każdego nadajnika FrSky, aż do
oryginalnego X9D włącznie.

Seria **X20/X20S/X20HD** obsługuje kartę SD sformatowaną w FAT32, o pojemności
32 GB lub mniejszej (dobrym wyborem jest karta SanDisk Ultra Micro SDHC Class 10
16 GB). **X18** oraz **X20 Pro/R/RS** domyślnie korzystają z wewnętrznej pamięci
eMMC (dodatkowo można zamontować zewnętrzną kartę SD) — dotknij **Radio**, aby
ją przeglądać. Ethos automatycznie tworzy katalogi `Logs/`, `models/` oraz
`screenshots/`, jeśli ich brakuje; katalog `Firmware/` jest umowną konwencją dla
plików oprogramowania urządzeń, takich jak odbiorniki.

## Foldery najwyższego poziomu {: #top-level-folders }

- **`audio/`** — użytkownika i systemowe pliki dźwiękowe, podzielone według
  głosu (`audio/en/gb`, `audio/en/us`, `audio/en/default`). Pliki użytkownika są
  odtwarzane przez [funkcję specjalną Play Audio](../model-setup/special-functions.md);
  do plików systemowych należy `hello.wav` (powitanie „Welcome to Ethos” — można
  dodać `bye.wav`, ale nie jest on dostarczany). Format: PCM 16 kHz lub 32 kHz,
  liniowy 16-bitowy, albo 8-bitowy A-law (EU)/µ-law (US); nazwy plików do 31
  znaków plus rozszerzenie. Wszystkie trzy foldery głosowe są synchronizowane
  przez Ethos Suite niezależnie od tego, który jest faktycznie wybrany.

  ![Folder audio](../assets/system-filemanager-audio.png)

- **`bitmaps/`** — `bitmaps/models/` zawiera obrazy modeli użytkownika
  (ustawiane w [Edycji modelu](../model-setup/model-edit.md) lub w kreatorach
  nowego modelu); `bitmaps/user/` zawiera wszystko pozostałe. Zalecany format:
  32-bitowa bitmapa BMP, 8 bitów na kolor, z kanałem alfa, 300×280 px — dzięki
  temu dekodowanie po stronie nadajnika pozostaje niewymagające. Ethos skaluje
  pliki BMP w locie, ale nie robi tego dla PNG/JPEG. Nazwy plików mogą zawierać
  wyłącznie znaki `A-Z a-z 0-9 ()!-_@#;[]+=` oraz spacje i muszą mieć nie więcej
  niż 11 znaków (plus 4-znakowe rozszerzenie), aby pojawiły się w oknie wyboru
  obrazu modelu — dłuższe nazwy nadal będą widoczne w Menedżerze plików, ale nie
  będzie można ich tam wybrać. Narzędzia konwersji obrazów w Ethos Suite
  wykonają konwersję formatu za Ciebie.

  ![Folder bitmaps](../assets/system-filemanager-bitmaps.png)

- **`documents/user/`** — dokumenty tekstowe użytkownika, przywoływane przez
  widget wyświetlający **Text**.

- **`Firmware/`** — pliki oprogramowania dla wewnętrznego modułu RF, modułów
  zewnętrznych oraz innych urządzeń (odbiorników itp.), wgrywane stąd przez
  S.Port lub OTA. Skopiuj tutaj nowe oprogramowanie, gdy nadajnik jest w
  [trybie bootloadera](../getting-started/usb-connection-modes.md) i podłączony
  przez USB; dotknięcie pliku oprogramowania i wybranie **Flash** rozpoczyna
  aktualizację:

  ![Wgrywanie oprogramowania wewnętrznego modułu RF](../assets/system-filemanager-flash.png)
  ![Wgrywanie oprogramowania odbiornika S8R przez S.Port](../assets/system-filemanager-flash-S8R.png)
  ![Wgrywanie oprogramowania odbiornika TD-R18 przez OTA](../assets/system-filemanager-flash-TD-ISRM.png)
  ![Wgrywanie bootloadera](../assets/system-filemanager-flash-bootloader.png)

- **`I18n/`** — pliki tłumaczeń językowych.

- **`Logs/`** — logi danych.

- **`models/`** — same pliki modeli. Nie można ich tutaj bezpośrednio edytować —
  jedynie tworzyć kopie zapasowe lub udostępniać. Od wersji Ethos v1.2.11 model
  jest nazywany zgodnie z nazwą modelu, a nie kolejno `model01.bin` (np. model o
  nazwie „Extra” otrzyma plik `Extra.bin`; drugi model „Extra” — `Extra01.bin`).
  Zmiana nazwy modelu w [Edycji modelu](../model-setup/model-edit.md) powoduje
  również zmianę nazwy pliku — zawsze małymi literami (nazwa wyświetlana z
  wielkimi i małymi literami jest przechowywana wewnątrz pliku) — przy czym nie
  każdy znak nazwy modelu trafia do nazwy pliku. Od wersji v1.1.0 Alpha 17 każda
  utworzona przez użytkownika kategoria modeli otrzymuje własny podfolder.

- **`screenshots/`** — pliki wyjściowe [funkcji specjalnej
  Screenshot](../model-setup/special-functions.md).

- **`scripts/`** — skrypty Lua, opcjonalnie uporządkowane we własnych
  podfolderach wraz z plikami pomocniczymi. Typy skryptów to **widgety** (patrz
  [Wyświetlacze](../displays/index.md)), **zadania i źródła** (własne czujniki
  lub czynności po locie — po zainstalowaniu tutaj pojawiają się w menu
  [Lua](../model-setup/lua-scripts.md) modelu) oraz **narzędzia** (np. narzędzia
  konfiguracji odbiorników stabilizowanych w menu systemowym). Zewnętrzne moduły
  innych producentów mają własne skrypty i foldery, np. `scripts/multi`,
  `scripts/elrs`, `scripts/ghost`, `scripts/crossfire`.

  !!! warning
      Skrypty Lua wydłużają czas uruchamiania nadajnika. Opóźnienie
      spowodowane dobrze napisanym skryptem jest niezauważalne — źle
      napisany skrypt może opóźnić uruchomienie niemal w nieskończoność.

- **`radio.bin`** (folder główny) — plik ustawień systemowych, zapisywany przez
  sam nadajnik podczas inicjalizacji. Wykonaj jego kopię zapasową razem z
  katalogiem `models/` przed aktualizacją oprogramowania, aby w razie potrzeby
  móc wrócić do wcześniejszej wersji.

- **`firmware.bin`** (folder główny) — umieść tutaj nowy plik oprogramowania
  nadajnika, aby został automatycznie wgrany przy następnym odłączeniu
  nadajnika od komputera. Zawartość karty SD/eMMC oraz wewnętrznego dysku flash
  może wymagać aktualizacji w tym samym przebiegu.

- **`sdcard.version`** (folder główny) — wersja zawartości karty SD,
  utrzymywana przez Ethos Suite.

## Udostępnianie plików przez Bluetooth

Ethos umożliwia przesyłanie plików między nadajnikami przez Bluetooth. Na
nadajniku **odbierającym** przejdź w Menedżerze plików do folderu docelowego,
przytrzymaj `ENT` i wybierz **Receive file here**:

![Odbieranie przez Bluetooth](../assets/system-filemanager-bluetooth-receive.png)

Na nadajniku **wysyłającym** dotknij pliku, wybierz **Send file** i postępuj
zgodnie z komunikatami na obu nadajnikach:

![Wysyłanie przez Bluetooth](../assets/system-filemanager-bluetooth-send.png)

Jeśli któryś z nadajników ma już aktywne połączenie Bluetooth (telemetria, łącze
trenerskie lub — w X20S/Pro — audio), pojawi się pytanie, czy najpierw odłączyć
to urządzenie.
