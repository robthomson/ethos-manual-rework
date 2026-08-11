---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Tryby połączenia USB

![Menu USB](../assets/usbmenu.png)

Działanie połączenia USB z komputerem zależy od tego, w jaki sposób nadajnik
był zasilany w momencie podłączenia kabla.

## Tryb wyłączonego nadajnika

Podłączenie nadajnika do komputera przez USB **przy wyłączonym zasilaniu**
przełącza go w tryb DFU, wykorzystywany do wgrywania samego bootloadera.

## Tryb bootloadera {: #bootloader-mode }

Włącz nadajnik **z wciśniętym przyciskiem `ENT`**, aby uruchomić go w trybie
bootloadera (na ekranie pojawi się napis „Bootloader”). Podłączenie USB w tym
momencie zmienia status na „USB Plugged”, a komputer montuje **dwa** dyski:
wewnętrzną pamięć flash nadajnika oraz zawartość karty SD/eMMC. Jest to tryb
przeznaczony do bezpośredniego odczytu i zapisu plików w obu obszarach pamięci;
w ten sam sposób [Ethos Suite](../ethos-suite/index.md) aktualizuje
oprogramowanie nadajnika — patrz sekcja Bootloader Mode w opisie Ethos Suite.

## Tryb włączonego nadajnika

Podłączenie USB przy **normalnie włączonym nadajniku** wyświetla okno wyboru
trybu:

- **Joystick** — nadajnik przedstawia się jako joystick USB HID, do obsługi
  symulatorów lotu na komputerze.
- **FrSky Suite** — przełącza nadajnik w „tryb Ethos” umożliwiający komunikację
  z [Ethos Suite](../ethos-suite/index.md).
- **Serial** — przesyła komunikaty diagnostyczne Lua przez port szeregowy USB
  (115200 bps). Zakładka Lua Development Tools w Ethos Suite zawiera
  zintegrowany terminal do ich wyświetlania; w systemie Windows może być
  wymagany sterownik wirtualnego portu COM.
