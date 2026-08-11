---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Ogólne

![Ustawienia ogólne](../assets/system-general.png)

Obejmuje atrybuty wyświetlacza, dźwięk, wariometr, wibracje oraz górny pasek narzędzi.

## Atrybuty wyświetlacza

- **Język** — język menu na wyświetlaczu (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português i inne).
- **Klawiatura** — układ klawiatury wirtualnej QWERTY, QWERTZ lub AZERTY.
- **Jasność** — suwak jasności podświetlenia; przytrzymaj `ENT`, aby zamiast
  tego sterować nią ze źródła (np. suwaka, jak w poniższym przykładzie)
  albo wymusić wartość minimalną/maksymalną.

  ![Menu jasności](../assets/system-general-brightness-menu.png)
  ![Suwak jasności](../assets/system-general-brightness-slider.png)

  !!! note
      Jeśli **Jasność** jest równa **Jasności w trybie uśpienia**, ekran
      dotykowy pozostaje aktywny nawet w stanie „uśpienia”.

- **Wybudzanie** — które z tych zdarzeń wybudzają podświetlenie z uśpienia
  (można włączyć więcej niż jedno): **Zawsze włączone** (brak uśpienia),
  **Drążki**, **Przełączniki**, **Żyroskop** (przechylenie nadajnika).
  Przyciski wybudzają zawsze, niezależnie od tych ustawień.
- **Uśpienie** — czas bezczynności, po którym podświetlenie się wyłącza
  (wyszarzone, jeśli Wybudzanie ustawiono na Zawsze włączone).
- **Jasność w trybie uśpienia** — jasność podświetlenia podczas uśpienia.
- **Tryb ciemny** — jasny lub ciemny motyw wyświetlania.
- **Kolor wyróżnienia** — kolor akcentu interfejsu (domyślnie `#F8B038`).

## Ustawienia dźwięku {: #audio-settings }

![Ustawienia dźwięku](../assets/system-general-audio.png)

- **Język komunikatów** — język komunikatów głosowych.
- **Wybór głosów** — Ethos obsługuje wiele jednocześnie zainstalowanych pakietów głosowych:

  - **Głos 1 (główny)** — używany do wszystkich wbudowanych komunikatów
    systemowych. Dla języka angielskiego domyślnie wybiera się między
    pakietem amerykańskim (`us`) a brytyjskim (`gb`), odczytywanym z
    `audio/en/us/system` i `audio/en/gb/system`. Własne pliki dźwiękowe dla
    [funkcji specjalnej Odtwórz dźwięk](../model-setup/special-functions.md)
    umieszcza się odpowiednio w `audio/en/us/` lub `audio/en/gb/`.
  - **Głos 2 / Głos 3** — dodatkowe pakiety, na przykład własny głos TTS.
    Każdy wymaga takiej samej struktury folderów jak Głos 1 — np. głos o
    nazwie „Susan” wymaga folderu `audio/en/Susan/` na dźwięki użytkownika
    oraz `audio/en/Susan/system` na dźwięki systemowe (każdy głos wymaga
    folderu `/system`, ponieważ stamtąd odczytywane są komunikaty **Odtwórz
    wartość** oraz komunikaty timerów; lista `.csv` standardowych plików
    dźwięków systemowych dołączana jest do każdego wydania pakietu audio).
    Po zainstalowaniu głos można przypisać do poszczególnych timerów i
    funkcji Odtwórz dźwięk — a nawet ustawić go jako Głos 1, całkowicie
    zastępując komunikaty systemowe.
  - **Głos „default”** — instalowany automatycznie jako bezpieczne
    rozwiązanie awaryjne (oraz w celu uniknięcia problemów z konwersją
    instalacji 1.4.x): jeśli podczas instalacji/aktualizacji Głos 1 nie jest
    jeszcze ustawiony, przyjmuje wartość `default` i odczytuje dane z
    `audio/en/default/system`. Często pobierane własne pliki dźwiękowe dla
    funkcji Odtwórz dźwięk znajdują się w `audio/en/default/`.

- **Głośność główna** — suwak ogólnej głośności dźwięku (przytrzymaj `ENT`,
  aby sterować nią potencjometrem); podczas regulacji odtwarzane są sygnały
  dźwiękowe, dzięki czemu można ocenić poziom ze słuchu.
- **Tryb dźwięku**:
  - **Cichy** — brak dźwięku (nadal wyzwala [alert trybu
    cichego](alerts.md) przy uruchomieniu, jeśli jest włączony).
  - **Tylko alarmy** — słyszalne są wyłącznie alarmy.
  - **Domyślny** — normalne dźwięki.
  - **Częsty** — dodaje sygnały błędu, gdy wartość zostanie przekroczona
    poza minimum/maksimum.
  - **Zawsze** — oprócz trybu Częsty dodaje sygnały przy zwykłej nawigacji
    po menu.
  - **Bluetooth** (tylko X20S/HD/Pro/R/RS) — przekazuje dźwięk do sparowanego
    urządzenia Bluetooth (zestawu słuchawkowego itp.). Wybierz **Szukaj
    urządzeń**, przełącz urządzenie docelowe w tryb parowania, a następnie
    wybierz je po znalezieniu:

    ![Parowanie Bluetooth](../assets/system-general-audio-bluetooth.png)
    ![Wyszukiwanie Bluetooth](../assets/system-general-audio-bluetooth-searching.png)
    ![Wybrane urządzenie Bluetooth](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Łączenie Bluetooth](../assets/system-general-audio-bluetooth-connecting.png)
    ![Połączono przez Bluetooth](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Wyciszenie głośnika** steruje wówczas wbudowanym głośnikiem — zawsze
    włączone, tylko gdy aktywna jest telemetria, albo sterowane ze źródła
    (np. przełącznika). Nadajnik zapamiętuje sparowane urządzenie; dla
    prawidłowego działania włącz nadajnik przed urządzeniem Bluetooth i
    odczekaj kilka sekund po nawiązaniu połączenia, aż wyciszenie głośnika
    ponownie zadziała.

## Wariometr {: #vario }

![Dźwięk wariometru](../assets/system-general-audio-vario.png)

- **Głośność** — względna głośność tonu wariometru.
- **Wysokość tonu zero** — wysokość tonu przy zerowej prędkości wznoszenia.
- **Wysokość tonu maks.** — wysokość tonu przy maksymalnej prędkości wznoszenia.
- **Powtarzanie** — odstęp między sygnałami przy zerowej prędkości wznoszenia.

Zobacz także czujnik VSpeed w sekcji [Telemetria](../model-setup/telemetry.md)
oraz [funkcję specjalną Odtwórz wariometr](../model-setup/special-functions.md),
aby poznać dalsze zachowania wariometru.

## Wibracje

- **Siła** — suwak intensywności wibracji.
- **Tryb** — ten sam zestaw opcji co w trybie dźwięku powyżej.

## Lokalizacja pamięci (X18 i X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Te nadajniki mają wbudowaną pamięć eMMC 8 GB. Domyślnie Ethos z niej
korzysta, dzięki czemu karta SD card jest opcjonalna — można jednak wybrać
pamięć eMMC, kartę SD card lub kombinację obu. Przenosząc system i modele na
kartę SD card, skopiuj odpowiednie foldery/pliki (w tym audio i bitmapy)
**przed** zmianą lokalizacji pamięci.

![Lokalizacja pamięci](../assets/system-general-storage.png)

## Górny pasek narzędzi

![Ustawienia górnego paska](../assets/system-general-topbar.png)

- **Napięcie cyfrowe** — pokazuje napięcie akumulatora nadajnika w górnym
  pasku narzędzi jako liczbę zamiast paska.
- **Cyfrowe RSSI** — to samo dla RSSI 2,4 GHz i 900 MHz.
- **Wybór modelu przy włączeniu** — wyświetla ekran wyboru modelu przy
  starcie, przed pojawieniem się alertów listy kontrolnej poprzedniego
  modelu, dzięki czemu można zmienić model bez wcześniejszego ich
  odrzucania. Ostatnio używany model jest domyślnie podświetlony.

  ![Wybór modelu przy starcie](../assets/system-general-model-start.png)

## Wstępny wybór trybu USB

![Tryb USB](../assets/system-general-usb.png)

Co dzieje się automatycznie po podłączeniu nadajnika do komputera przez USB:

- **Nie ustawiono** — pyta o wybór w chwili podłączenia.
- **Joystick** — natychmiast przechodzi w tryb joysticka dla symulatora RC.
- **Ethos Suite** — natychmiast przechodzi w tryb Ethos dla [Ethos
  Suite](../ethos-suite/index.md).
- **Serial** — natychmiast przechodzi w tryb Serial, przekazując komunikaty
  debugowania Lua przez USB-Serial z prędkością 115200 bps (może być
  wymagany sterownik wirtualnego portu COM dla systemu Windows).
