---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Domyślnie wyłączony. Ustaw nadajnik jako **Master** (nadajnik instruktora,
odbierający do 16 sterowań od ucznia) lub **Slave** (nadajnik ucznia,
wysyłający konfigurowalną liczbę kanałów do instruktora).

## Tryb Master

![Tryb Master](../assets/model-trainer-master.png)
![Opcje trainera](../assets/model-trainer-options.png)

### Tryb połączenia

![Opcje trybu połączenia](../assets/model-trainer-link-mode-options.png)

- **Kabel trainera** — przewód audio mono 3,5 mm pomiędzy dwoma nadajnikami.
- **Bluetooth** —

  ![Połączenie Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Tryb** — normalny lub o wysokiej prędkości; użyj trybu o wysokiej
    prędkości, aby uzyskać mniejsze opóźnienie, jeśli oba nadajniki go
    obsługują.

    ![Tryb Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Nazwa lokalna** — nazwa BT widoczna dla innych urządzeń (domyślnie
    `FrSkyBT`, edytowalna).
  - **Adres lokalny** — adres Bluetooth tego nadajnika.
  - **Adres zdalny** — adres sparowanego nadajnika po nawiązaniu połączenia.
  - **Szukaj urządzeń** (tylko w trybie Master) — skanuje w poszukiwaniu
    pobliskich urządzeń:

    ![Wyszukiwanie](../assets/model-trainer-link-mode-bt-search.png)
    ![Oczekiwanie](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Wybór urządzenia](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Połączono](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Połącz z ostatnim urządzeniem** / **Resetuj moduł** — ponowne
    połączenie z poprzednio sparowanym urządzeniem lub całkowite
    skasowanie konfiguracji modułu Bluetooth.

- **Zewnętrzny moduł SBUS** — wejście SBUS na pinie PXX-IN w kieszeni
  modułu zewnętrznego, przeznaczone do podłączenia odbiornika FrSky z
  wyjściem SBUS (np. Archer RS) jako strony odbiorczej łącza
  bezprzewodowego — dzięki temu **dowolny** nadajnik FrSky może pełnić
  rolę ucznia (buddy box), związany z tym odbiornikiem.
- **Zewnętrzny moduł CPPM** — to samo rozwiązanie z wykorzystaniem
  wejścia CPPM, dla starszych odbiorników z wyjściem CPPM.

### Warunek aktywacji

![Warunek aktywacji](../assets/model-trainer-active-condition.png)

Przełącznik/przycisk, przełącznik funkcyjny, przełącznik logiczny,
pozycja trymu lub tryb lotu, który w stanie aktywnym przekazuje
sterowanie uczniowi.

### Kanały trainera

![Edycja warunku aktywacji](../assets/model-trainer-active-condition-edit.png)

Gdy warunek aktywacji jest spełniony, od ucznia do nadajnika Master może
być przekazywanych do 16 kanałów. Dotknij kanału, aby skonfigurować go
indywidualnie:

- **Warunek aktywacji** — nadpisanie dla pojedynczego kanału, np. aby
  wyłączyć tylko sterowanie sterem wysokości przez ucznia na część sesji.
- **Tryb** — **OFF** (wyłączony dla funkcji trainera), **Add** (sygnały
  nauczyciela i ucznia sumują się, dzięki czemu obaj mogą jednocześnie
  oddziaływać na sterowanie) lub **Replace** (tryb standardowy — uczeń ma
  pełną kontrolę nad tym kanałem, gdy funkcja jest aktywna).
- **Procent** — skaluje sygnał ucznia, standardowo 100%.
- **Przeznaczenie** — funkcja, do której przypisany jest kanał ucznia.

Zobacz [Poradnik: natychmiastowe przejęcie sterowania](../how-to/instant-takeback.md),
gdzie omówiono praktyczny przykład natychmiastowego odzyskania kontroli
przez instruktora za pomocą przełącznika, oraz [Ignorowanie sygnału
trainera](../getting-started/user-interface-and-navigation.md#choosing-a-source),
aby wykluczyć ruchy drążków ucznia z przełącznika logicznego
obserwującego drążki instruktora.

## Tryb Slave

![Tryb Slave](../assets/model-trainer-slave-mode.png)

- **Tryb połączenia** — ten sam wybór: kabel trainera, Bluetooth lub
  zewnętrzny moduł SBUS/CPPM, co w trybie Master (te same pola Bluetooth
  **Tryb**/**Nazwa lokalna**/**Adres lokalny**/**Adres zdalny**).

  ![Tryb połączenia Slave](../assets/model-trainer-slave-link-mode.png)

- **Zakres kanałów** — zakres kanałów tego nadajnika wysyłany do
  nadajnika Master.

  ![Kanały Slave](../assets/model-trainer-slave-channels.png)
  ![Edycja kanału Slave](../assets/model-trainer-slave-channel-edit.png)
