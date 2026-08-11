---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Bedienelemente

![Steuerknüppel](../assets/system-sticks.png)

Im Menü als **Sticks** bezeichnet — Knüppelmodus und die standardmäßige
Reihenfolge der Kanalzuordnung.

## Knüppelmodus

- **Mode 1** — Gas und Querruder auf dem rechten Steuerknüppel, Höhenruder
  und Seitenruder auf dem linken.
- **Mode 2** — Gas und Seitenruder auf dem linken Steuerknüppel, Querruder
  und Höhenruder auf dem rechten.

Die Steuerknüppel sind standardmäßig nach den branchenüblichen Modes
benannt und können umbenannt werden.

## Kanalreihenfolge

Legt fest, in welcher Reihenfolge die vier Knüppeleingaben den Kanälen
zugewiesen werden, wenn ein neues Modell über die Assistenten der
[Modellauswahl](../model-setup/model-select.md) erstellt wird. Standard ist
**AETR**. Verfügt eine Zelle über mehrere Ruder derselben Art, werden diese
gruppiert, sofern nicht [Erste vier Kanäle
festgelegt](#first-four-channels-fixed) aktiviert ist — z. B. werden aus
2 Querrudern **AAETR**.

![Kanalreihenfolge des Empfängers](../assets/system-sticks-rx-order.png)

## Erste vier Kanäle festgelegt {: #first-four-channels-fixed }

Ist diese Option aktiviert, werden die ersten vier Kanäle niemals gruppiert.
Bei der Reihenfolge **AETR** und einer Zelle mit 2 Querrudern, 1 Höhenruder,
1 Motor, 1 Seitenruder und 2 Klappen erzeugt der Assistent **AETRAFF**
(die Kanäle 1–4 bleiben exakt A-E-T-R, das zweite Querruder und beide
Klappen werden dahinter angehängt) statt **AAETRFF**. Mit dieser Einstellung
erstellt der Assistent Modelle, die für stabilisierte SRx-Empfänger geeignet
sind, welche genau dieses feste Layout erwarten.

![Feste Reihenfolge der ersten 4 Kanäle](../assets/system-sticks-4ch-fixed.png)
