---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Handbuch

**Ethos** ist das Betriebssystem, das auf den Sendern der Ethos-Familie von FrSky
(X20S, X20 Pro, X20 Pro AW, X18S und weitere) läuft. Dieses Handbuch behandelt die
Einrichtung eines Modells von Grund auf, die Konfiguration der systemweiten
Einstellungen des Senders, die Erstellung eigener Telemetrieanzeigen sowie die
Lua-Skriptumgebung, die auf all dem aufsetzt.

!!! note "In Arbeit"
    Dieses Handbuch wurde von Grund auf neu erstellt, basierend auf dem offiziellen
    Ethos-1.6.3-Handbuch und dem vorhandenen Screenshot-Bestand. Einige wenige Seiten
    (Ethos Suite, RF-System und ein paar Anleitungen) sind vollständig, verfügen aber
    noch nicht über Screenshots — siehe [Screenshot-
    Pipeline](contributing/screenshot-pipeline.md) und
    [Mitwirken](contributing/index.md), falls Sie helfen möchten.

## Wo anfangen

- Neu bei Ethos? Beginnen Sie mit den [Erste Schritte](getting-started/index.md) —
  dem Aufbau des Hauptbildschirms und der Funktionsweise der Navigation, bevor Sie
  Einstellungen ändern.
- Sie richten einen neuen Sender ein? Siehe [Systemeinstellungen](system-setup/index.md)
  für die einmaligen, senderweiten Einstellungen (Hardwarekalibrierung, Warnungen, Akku).
- Sie programmieren ein Modell? [Modellkonfiguration](model-setup/index.md) behandelt
  Mischer, Ausgänge, Flugphasen und alles Weitere, was pro Modell gespeichert wird, und
  die [Tutorials](tutorials/index.md) führen Schritt für Schritt durch die Erstellung von
  Flächenmodellen, Nurflüglern und Hubschraubern.
- Sie erstellen einen Telemetriebildschirm? Siehe [Anzeigen](displays/index.md).
- Sie möchten eine bestimmte Aufgabe schnell lösen? Sehen Sie in den
  [Anleitungen](how-to/index.md) nach.
- Sie schreiben oder installieren Lua-Skripte/Widgets? Siehe [Lua-Skripte](lua-scripts/index.md).

## Behandelte Sender

Dieses Handbuch ist in erster Linie für den **X20S** geschrieben; senderspezifische
Unterschiede (X20 Pro, X20 Pro AW, X18S) werden in den
[Senderhinweisen](radio-notes/index.md) dort aufgeführt, wo die Bedienoberfläche abweicht.
