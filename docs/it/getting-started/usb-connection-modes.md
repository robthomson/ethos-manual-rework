---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Modalità di connessione USB

![Menu USB](../assets/usbmenu.png)

Ciò che avviene collegando la radio a un PC tramite USB dipende da come era alimentata la radio al momento del collegamento.

## Modalità a radio spenta

Collegando la radio a un PC tramite USB **mentre è spenta**, questa entra in modalità DFU, utilizzata per eseguire il flashing del bootloader stesso.

## Modalità bootloader {: #bootloader-mode }

Accendi la radio **tenendo premuto `ENT`** per avviarla in modalità bootloader (lo schermo mostra "Bootloader"). Collegando ora l'USB, lo stato cambia in "USB Plugged" e il PC monta **due** unità: la memoria flash interna della radio e il contenuto della SD card/eMMC. Questa è la modalità che permette di leggere e scrivere i file direttamente in entrambe le aree di memoria ed è anche il modo in cui [Ethos Suite](../ethos-suite/index.md) aggiorna il firmware della radio: consulta la sezione Bootloader Mode di Ethos Suite.

## Modalità a radio accesa

Collegando l'USB mentre la radio è **accesa normalmente** compare un menu di selezione della modalità:

- **Joystick** — la radio viene riconosciuta come joystick USB HID, per utilizzare i simulatori di volo su PC.
- **FrSky Suite** — porta la radio in "modalità Ethos" per la comunicazione con [Ethos Suite](../ethos-suite/index.md).
- **Serial** — invia le tracce di debug Lua tramite USB-seriale (115200 bps). La scheda Lua Development Tools di Ethos Suite dispone di un terminale integrato per visualizzarle; su Windows può essere necessario il driver Virtual COM Port.
