---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Notfallmodus

Der Notfallmodus ist die Reaktion von Ethos auf einen unerwarteten Fehler auf unterer Systemebene, beispielsweise einen Watchdog-Reset. Der Watchdog ist ein Timer, der von verschiedenen Teilen des Systems fortlaufend neu gestartet wird; verhindert etwas diesen Neustart, läuft er ab und erzwingt einen Hardware-Reset. Der Notfallmodus startet den Sender daraufhin so schnell wie möglich neu und überspringt sämtliche üblichen Startprüfungen, sodass die Kontrolle über das Modell mit minimaler Verzögerung zurückgegeben wird. Auf die SD card bzw. den eMMC-Speicher wird in diesem Modus überhaupt nicht zugegriffen.

Verfügbar sind ausschließlich die wesentlichen Funktionen, die zur weiteren Steuerung des Modells erforderlich sind — keine der höheren Funktionen. Der Bildschirm bleibt leer bis auf den Schriftzug **EMERGENCY MODE**, begleitet von einem sich alle 3 Sekunden wiederholenden Signalton von 300 ms Dauer; Sprachansagen, Lua-Skripte, Aufzeichnung und Telemetrie werden vollständig eingestellt. Tritt dies im Flug auf, landen Sie so schnell wie möglich.

Die häufigste Ursache ist ein Ausfall der SD card.

## Notfallmodus testen

Es kann ein **Systemtool** hinzugefügt werden, mit dem sich der Notfallmodus zu Testzwecken gezielt auslösen lässt, damit man ihn nicht erst im Flug zum ersten Mal kennenlernt. Ein Tippen auf das Symbol „Emergency Test“ fordert eine Bestätigung an und versetzt den Sender anschließend genau so in den Notfallmodus, wie es bei einem echten Fehler geschehen würde.
