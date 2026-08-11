---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# SR8/SR10 – Modellkonfiguration und Kanalreihenfolge ändern

Die stabilisierten Empfänger der SRx-Serie von FrSky erwarten eine bestimmte
Kanalreihenfolge. Es gibt zwei Szenarien: ein neues Modell von Grund auf für
einen solchen Empfänger anlegen oder ein bestehendes Modell entsprechend
umstellen.

!!! note "Screenshots folgen"
    Für diese Seite liegen noch keine Simulator-Screenshots vor — siehe [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## Ein neues Modell anlegen

Der Assistent unter [Modellauswahl](../model-setup/model-select.md) fasst
Ruderflächen gleicher Funktion standardmäßig zusammen (z. B. 2 Querruder →
`AAETR`), SRx-Empfänger benötigen jedoch die ersten vier Kanäle fest in der
Reihenfolge **AETRA**.

1. Prüfen Sie unter [Bedienelemente](../system-setup/controls.md), dass die
   **Kanalreihenfolge** auf `AETR` steht.
2. Aktivieren Sie **[Erste vier Kanäle
   fest](../system-setup/controls.md#first-four-channels-fixed)** — dadurch
   fasst der Assistent die ersten vier Kanäle nicht mehr zusammen und behält
   strikt die Reihenfolge `AETRA…` bei, unabhängig davon, wie viele Flächen
   der jeweiligen Funktion die Zelle besitzt.
3. Führen Sie den Assistenten zum Anlegen des Modells wie gewohnt aus — die
   ersten 5 Kanäle ergeben sich als `AETRA`.

!!! note "Selbsttest bei Archer-Empfängern"
    Der Selbsttest für Archer-Empfänger läuft inzwischen über [Gerätekonfiguration →
    SxR](../system-setup/devices.md) (Firmware v2.1.10+) und nicht mehr über eine
    eigene Selbsttest-Prozedur. Der Gaskanal muss auf −100 % stehen, sonst
    startet der Selbsttest nicht.

## Ein bestehendes Modell umsortieren

Die Umstellung eines bestehenden Modells (z. B. aktuell `AAETRFF`) auf die
Reihenfolge für stabilisierte Empfänger (`AETRAE`, anschließend Kanal 9 Gain,
10/11 Flugphasen, 12 Selbsttest bei älteren SxR-Einheiten) erfolgt über eine
Reihe von Kanaltauschen in den [Ausgängen](../model-setup/outputs.md#swap-channels).

Ausgangslage:

| Kanal | Funktion |
|---|---|
| 1 | Querruder1 (rechts) |
| 2 | Querruder2 (links) |
| 3 | Höhenruder |
| 4 | Gas |
| 5 | Seitenruder |
| 6 | Klappe1 (rechts) |
| 7 | Klappe2 (links) |
| 8 | Einziehfahrwerk |

Zielreihenfolge: `AETRAE` — Kanal 1 Querruder1, Kanal 2 Höhenruder, Kanal 3 Gas,
Kanal 4 Seitenruder, Kanal 5 Querruder2, Kanal 6 Höhenruder2/AUX2 (danach
Gain/Flugphasen/Selbsttest auf 9–12).

1. **Zuerst Querruder2 aus dem Weg räumen**: Wählen Sie in den Ausgängen CH2
   (Querruder2), tippen Sie erneut darauf, wählen Sie **Kanäle tauschen** und
   tauschen Sie ihn mit einem freien Kanal (z. B. CH9). Der Tausch wirkt sofort —
   alle Mischer, die einen der beiden Kanäle verwenden, werden automatisch
   aktualisiert.
2. **CH3 (Höhenruder) → CH2 tauschen.**
3. **CH4 (Gas) → CH3 tauschen.**
4. **CH5 (Seitenruder) → CH4 tauschen.**
5. **CH9 (Querruder2, in Schritt 1 zwischengeparkt) → CH5 tauschen.**

Ergebnis:

| Kanal | Funktion |
|---|---|
| 1 | Querruder1 (rechts) |
| 2 | Höhenruder |
| 3 | Gas |
| 4 | Seitenruder |
| 5 | Querruder2 (links) |
| 6 | Klappe1 (rechts) |
| 7 | Klappe2 (links) |
| 8 | Einziehfahrwerk |

— nun in der Reihenfolge, die stabilisierte FrSky-Empfänger erwarten.
