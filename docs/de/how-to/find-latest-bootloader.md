---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Aktuellen Bootloader oder andere Komponenten finden

Ethos-Firmware-Releases enthalten eine Datei `components.json`, die die
aktuelle Version jeder Komponente je Sender auflistet. Damit lässt sich
vor dem Flashen prüfen, ob eine bestimmte Bootloader-/Firmware-/Audio-/
System-Dateien-Version tatsächlich aktuell ist.

!!! note "Screenshots ausstehend"
    Für diese Seite liegen noch keine Simulator-Screenshots vor — siehe [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

1. Laden Sie `components.json` aus dem neuesten Ethos-Release herunter.
2. Öffnen Sie die Datei in einem Texteditor (VS Code, Notepad usw.).
3. Suchen Sie den Abschnitt für Ihren Sender — z. B. `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (Nur ein Momentaufnahme-Beispiel — prüfen Sie für die tatsächlichen
   Versionsnummern immer die Datei des *aktuellen* Releases.)

4. Lesen Sie die Version der benötigten Komponente ab — im obigen
   Beispiel ist der neueste Bootloader für die X20-Familie `1.4.15`.

Unter [Dateimanager](../system-setup/file-manager.md#top-level-folders) ist
beschrieben, wo die heruntergeladene Firmware-Datei abgelegt wird, und unter [USB-Verbindungsmodi](../getting-started/usb-connection-modes.md#bootloader-mode),
wie der Sender zum Flashen in den Bootloader-Modus versetzt wird — oder
verwenden Sie [Ethos
Suite](../ethos-suite/index.md), das Versionsprüfung und Flashen
automatisch übernimmt.
