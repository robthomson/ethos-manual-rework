---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Informationen

![Systeminformationen](../assets/system-info.png)

Angaben zur System-Firmware, Gimbal-Typ, Informationen zum internen/externen HF-Modul,
Informationen zum gebundenen Empfänger, Betriebszeit des Senders, Fehlerprotokolle und Werksreset.

## Senderinformationen

- **Seriennummer** — die Seriennummer des Senders.
- **Firmware** — Ethos-Version und Sendertyp (z. B. X20).
- **Firmware-Version** — Build-Variante, z. B. FCC, LBT oder Flex.
- **Datum** — Erstellungsdatum/-zeit der Firmware.
- **Verfügbarer RAM** — freier System-RAM, nützlich zum Aufspüren eines fehlerhaften
  Lua-Skripts; auch als System-[Quelle](../getting-started/user-interface-and-navigation.md#choosing-a-source)
  verfügbar, sodass der Wert in einem Widget angezeigt werden kann.
- **Steuerknüppel** — Version der verbauten Gimbal-Hallsensoren (oder „ADC" bei analogen
  Gimbals).
- **Internes Modul** — Hardware- und Firmware-Versionen des internen HF-Moduls.
- **Empfänger** — Details des aktuell gebundenen Empfängers, angezeigt nach dem
  internen Modul. Teilt sich ein redundanter Empfänger denselben Slot mit dem
  Hauptempfänger, wechseln sich beide in der Anzeige ab (z. B. ein Archer SR10 Pro
  zusammen mit dem redundanten R9MM-OTA unter „Receiver1").
- **Externes Modul** — Hardware-/Firmware-Details eines eingesetzten externen
  FrSky-HF-Moduls, das das ACCESS-Protokoll verwendet. Multi-protocol-Module
  werden hier nicht angezeigt.

![X20 Pro Informationen](../assets/system-info-x20pro.png)

## Betriebszeit des Senders

![Betriebszeit des Senders](../assets/system-info-radio-runtime.png)

Erfasst die gesamte Nutzungsdauer des Senders; **Reset** setzt sie auf null zurück.

## Fehler

![Fehler](../assets/system-info-errors.png)

Ein rotes Dreieck in der oberen Leiste der Hauptansicht bedeutet, dass Ethos einen Fehler
protokolliert hat, der hier im Detail angezeigt wird. Mögliche Ursachen:

- **Lua-Skriptfehler** — ein Problem in einem laufenden Lua-Skript.
- **RAM-Backup-Fehler** — ein Modell, das zu groß für den Modell-Backup-RAM ist. Ethos
  hat diesen von 4 K auf 32 K erweitert, sodass der Fall inzwischen unwahrscheinlich ist;
  tritt er dennoch auf, ist es ein bedeutender Fehler: Das Modell wird bei ausgelöstem
  [Notfallmodus](../getting-started/emergency-mode.md) langsamer von der SD card statt aus
  dem Backup-RAM geladen.
- **Verwendung eines Nightly-Firmware-Builds** — ein Hinweis darauf, dass Nightly-Builds
  nicht zum Fliegen vorgesehen sind.

**Reset** löscht die protokollierten Fehler — praktisch während einer Lua-Debugging-Sitzung.

## Werksreset

![Werksreset](../assets/system-info-factory-reset.png)

Setzt den Sender vollständig direkt am Gerät auf die Werkseinstellungen zurück — es ist
keine PC-Verbindung erforderlich.

![Bestätigung des Werksresets](../assets/system-info-factory-reset-confirm.png)

!!! danger
    Beim Bestätigen werden **alle** Modelle, Logs, Screenshots, Dokumente,
    Skripte, Bitmaps und Sendereinstellungen gelöscht. Ein Fortschrittsbalken zeigt
    den Löschvorgang an; danach werden alle Laufwerke ausgehängt und der Sender startet neu.

Die Info-Seite des X20 Pro/R/RS zeigt die entsprechenden Informationen für diese
Senderfamilie an.
