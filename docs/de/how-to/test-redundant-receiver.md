---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Redundante Empfängerkonfiguration testen

Redundanz ist nur dann sinnvoll, wenn sie vor dem Flug tatsächlich getestet
wird — hier wird vorausgesetzt, dass ein [redundanter
Empfänger](../model-setup/rf-system.md#redundant-receivers) bereits
konfiguriert ist.

!!! note "Screenshots ausstehend"
    Für diese Seite liegen noch keine Simulator-Screenshots vor — siehe
    [Screenshot-Pipeline](../contributing/screenshot-pipeline.md).

## A. Test im realen Einsatz

Wenn der Hauptempfänger auf 2,4 GHz und der redundante Empfänger auf 900 MHz
arbeitet, starten Sie eine
[Reichweitenprüfung](../model-setup/rf-system.md#range-check) und entfernen
Sie sich vom Modell, bis die 2,4-GHz-Verbindung abreißt (über die Warnung
„RSSI Critical" hinaus). Der redundante 900-MHz-Empfänger sollte an diesem
Punkt die Steuerung übernehmen.

## B. Test auf der Werkbank

1. **Normalen Aufbau prüfen** — beide Empfänger gebunden, beide grünen LEDs
   leuchten, Steuerfunktionen reagieren normal.
2. **Hauptempfänger an eine andere Model ID binden** — legen Sie ein
   Wegwerf-Testmodell (z. B. „TestRx") mit einer anderen Model ID an und
   binden Sie den *Haupt*empfänger daran. Wechseln Sie zurück zum zu
   testenden Modell: Die LED des Hauptempfängers sollte nun **rot** leuchten
   (anderweitig gebunden), die LED des redundanten Empfängers bleibt
   **grün** — und die Steuerung sollte weiterhin funktionieren. Damit ist
   nachgewiesen, dass der redundante Empfänger allein das Modell flugfähig
   hält.
3. **Hauptempfänger erneut binden** — wieder an seine normale Model ID.
   Vergewissern Sie sich, dass beide LEDs wieder grün leuchten und die
   Steuerfunktionen arbeiten, bevor Sie den Test als abgeschlossen
   betrachten.
