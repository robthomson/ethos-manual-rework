---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Modalità di connessione USB

![Menu USB](../assets/usbmenu.png)

Ciò che avviene collegando la radio a un PC tramite USB dipende da come la radio era alimentata al momento del collegamento.

## Modalità a radio spenta

Collegando la radio a un PC tramite USB **mentre è spenta** la si porta in modalità DFU, utilizzata per il flashing del bootloader stesso.

## Modalità bootloader {: #bootloader-mode }

Accendere la radio **tenendo premuto `ENT`** per avviarla in modalità bootloader (lo schermo mostra "Bootloader"). Collegando ora l'USB, lo stato cambia in "USB Plugged" e il PC monta **due** unità: la memoria flash interna della radio e il contenuto della SD card/eMMC. Questa è la modalità per leggere e scrivere file direttamente in entrambe le aree di memoria ed è anche il modo in cui [Ethos Suite](../ethos-suite/index.md) aggiorna il firmware della radio — vedere la sezione Bootloader Mode di Ethos Suite.

## Modalità a radio accesa

Collegando l'USB mentre la radio è **accesa normalmente** compare un selettore di modalità:

- **Joystick** — presenta la radio come joystick USB HID, per pilotare i simulatori di volo su PC.
- **FrSky Suite** — porta la radio in "modalità Ethos" per la comunicazione con [Ethos Suite](../ethos-suite/index.md).
- **Serial** — instrada le tracce di debug Lua su USB-seriale (115200 bps). La scheda Lua Development Tools di Ethos Suite dispone di un terminale integrato per visualizzarle; su Windows può essere necessario il driver Virtual COM Port.
