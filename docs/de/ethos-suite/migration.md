---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migration

Umstieg eines Senders von den älteren, separaten PC-Update-Werkzeugen auf die
Ethos Suite – zum ersten Mal.

1. **Ethos ≥ 1.1.4 sicherstellen** — dies ist die Mindestversion, die den neuen
   Suite-kompatiblen Bootloader (FRSK-Format) direkt aus dem
   [Dateimanager](../system-setup/file-manager.md) flashen kann. Falls nötig,
   zunächst manuell auf 1.1.4 aktualisieren.
2. **SD card/eMMC sichern** — den gesamten Inhalt in einen Ordner auf dem
   PC kopieren.
3. **Den aktuellen Bootloader herunterladen** von den
   [ETHOS-Feedback-Community Releases](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   und entpacken. Zu jedem Release gehört eine Datei `components.json`, in der die
   aktuelle Version jeder Komponente aufgeführt ist — wie diese zu lesen ist, steht
   unter [Anleitung: Den aktuellen Bootloader finden](../how-to/find-latest-bootloader.md).
4. Den Sender unter dem Eintrag `targets` in dieser Datei suchen, um die genau
   zu verwendende Bootloader-Version zu ermitteln, und die passende Datei in den
   Assets dieses Releases heraussuchen.
5. Den Sender in den [Bootloader-Modus](../getting-started/usb-connection-modes.md#bootloader-mode)
   starten (`ENT` gedrückt halten, dann einschalten) und über USB verbinden.
6. Die Bootloader-Datei auf die SD card/eMMC kopieren (normalerweise in den Ordner
   `Firmware/`), anschließend die Laufwerke auswerfen und die Verbindung trennen.
7. Den Sender normal starten, zu **System → Dateimanager** wechseln, die soeben kopierte
   Datei `bootloader.frsk` antippen und **Bootloader flashen** wählen.
8. Die Ethos Suite herunterladen und installieren — [Bedienung](operation.md) beschreibt
   ab hier das Aktualisieren von Firmware und Dateien sowie die übrigen Funktionen der Suite.
9. Wenn die Ethos Suite dies nicht automatisch erledigt, muss der Ordner `bitmaps/user`
   auf der SD card/eMMC gegebenenfalls in `bitmaps/models` umbenannt werden (dort werden
   die Modellbilder des Benutzers abgelegt).
