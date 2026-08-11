---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Warnung bei niedriger Akkuspannung

Die Überwachung der Flugakkuspannung **unter Last** mit einer Warnung beim Unterschreiten eines Schwellwerts ist zuverlässiger als das Vertrauen auf einen festen Timer — ein Sensor wie der FrSky FLVSS macht dies unkompliziert.

## 1. Sensor anschließen und erkennen

![LiPo-Telemetriesensor](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Stellen Sie [Empfängeroptionen → Telemetrieport](../system-setup/devices.md) auf **S.Port**, verbinden Sie den FLVSS über ein S.Port-Kabel mit dem Empfänger und aktivieren Sie anschließend **Neue Sensoren suchen** unter [Telemetrie](../model-setup/telemetry.md) — der LiPo-Sensor erscheint zusammen mit den bereits erkannten Sensoren.

## 2. Logischen Schalter hinzufügen

![Logischer Schalter für niedrigen Akkustand](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Fügen Sie einen neuen [logischen Schalter](../model-setup/logical-switches.md) mit dem LiPo-Sensor als Quelle hinzu. Ein langer Druck auf `ENT` beim markierten Sensor öffnet die Auswahl, welcher seiner Werte verwendet werden soll:

![Niedrigste Zelle auswählen](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Minimale Packspannung / Maximale Packspannung
- **Niedrigste Zellenspannung** / Höchste Zellenspannung
- Zellenanzahl
- Einzelne Zellenspannungen (nur auswählbar, solange der Sensor tatsächlich mit einem gebundenen Empfänger verbunden und ein LiPo angeschlossen ist)

Wählen Sie **Lowest** (niedrigste Zellenspannung) — der Wert, auf den es bei einem LVC-artigen Schutz ankommt.

![Niedrigste Zelle ausgewählt](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Setzen Sie den Vergleichswert auf etwa **3,4 V** und **Verzögerung vor Aktivierung** auf **4 Sekunden** — der Schalter wird wahr, sobald die niedrigste Zelle durchgehend 4 s oder länger unter 3,4 V pro Zelle liegt. (3,4 V *unter Last* erholen sich nach dem Wegfall der Last typischerweise auf etwa 3,7 V, dieser Schwellwert spiegelt also einen echten Spannungseinbruch wider und nicht nur kurzzeitige Störungen.)

![Fertiggestellter logischer Schalter](../assets/how-to-low-batt-lsw-summary.png)

## 3. Sonderfunktion hinzufügen

![Sonderfunktion: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Fügen Sie eine [Sonderfunktion „Audio abspielen“](../model-setup/special-functions.md) hinzu, setzen Sie die **Aktivierungsbedingung** auf den logischen Schalter `BattLow`, wählen Sie eine Stimme und fügen Sie unter **Sequenz** einen Schritt **Wert ansagen** für die LiPo-Gesamtspannung hinzu:

![Wert ansagen: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Übersicht der Sequenz](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Mit **Wiederholung** auf 10 Sekunden wird die LiPo-Spannung alle 10 s angesagt, solange die niedrigste Zelle unterhalb des Schwellwerts von 3,4 V/4 s bleibt.
