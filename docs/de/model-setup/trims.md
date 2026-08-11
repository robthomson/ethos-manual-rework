---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trimmungen

![Trimmungen](../assets/model-trims.png)

Legt für jeden Steuerknüppel den Trimmbereich, die Schrittweite und das
Verhalten fest, dazu Kreuztrimmung und Sofort-Trimmung. Der **X20 Pro/R/RS**
und der **X18** bieten zwei zusätzliche Trimmschalter, **T5**/**T6**, die
sich für Anpassungen im Flug jenseits der vier Hauptknüppel eignen:

![Trimmungen T5/T6](../assets/model-trims-pro-t5-t6.png)

Jeder Steuerknüppel besitzt einen eigenen, unabhängigen Satz von
Trimmeinstellungen.

## Trimmeinstellungen {: #trim-settings }

- **Bereich** — standardmäßig ±25 %, einstellbar bis zum vollen
  Knüppelweg von ±100 %. In der Hauptansicht zeigt eine Trimmung mit
  Standardbereich Werte von −100 bis 100 an; eine Trimmung mit vollem
  Bereich (100 %) zeigt −400 bis 400 an (das Vierfache des normalen
  Bereichs).

  !!! warning
      Ein größerer Bereich bedeutet, dass zu langes Halten einer
      Trimmtaste so viel Trimmung hinzufügen kann, dass das Modell nicht
      mehr fliegbar ist.

- **Schritt** — Auflösung des Trimmschalters: **Sehr fein**, **Fein**,
  **Mittel**, **Grob**, **Exponentiell** (fein um die Mitte, grob weiter
  außen) oder **Benutzerdefiniert** (ein bestimmter Prozentwert pro
  Klick).

  ![Schrittoptionen](../assets/model-trims-step-options.png)

  | Schritt | µs pro Klick (Bereich 25 %) |
  |---|---|
  | Sehr fein | 0,5 |
  | Fein | 1 |
  | Mittel | 2 |
  | Grob | 4 |
  | Exponentiell | 0,3–16 |

  Benutzerdefiniert bei einem Bereich von 25 %: 1 % Schritt = 1 µs/Klick,
  100 % Schritt = 128 µs/Klick. Bei einem Bereich von 100 %: 1 % Schritt =
  5 µs/Klick, 100 % Schritt = 512 µs/Klick.

## Modus

![Trimmmodus Höhenruder](../assets/model-trims-mode-elevator.png)

Standardmäßig ist eine Trimmung immer aktiv, doch **Modus** ändert dieses
Verhalten. Ein Moduswechsel setzt die Trimmung auf 0 zurück.

- **OFF** — deaktiviert die Trimmung vollständig.

  ![Modus: OFF](../assets/model-trims-mode-option-off.png)

  Nützlich beispielsweise bei einem Elektromodell, das keine Gastrimmung
  benötigt — das freigewordene Trimmelement kann dann
  [zur Verstellung einer Variablen umgewidmet werden](variables.md).

- **Einfach** — ein gemeinsamer Trimmwert für alle Flugphasen. Die übliche
  Wahl für Querruder und Seitenruder, da diese selten je nach Flugphase
  variieren müssen.

  ![Modus: Einfach](../assets/model-trims-mode-option-easy.png)

- **Unabhängig pro Flugphase** — die Trimmung wirkt nur auf die aktive
  Flugphase. Die übliche Wahl für die Höhenrudertrimmung, da diese häufig
  je nach Flugphase unterschiedlich sein muss (z. B. bei Änderung der
  Flügelwölbung) — tatsächlich ist dies oft der Hauptgrund, überhaupt
  Flugphasen einzurichten.

  ![Modus: flugphasenabhängig](../assets/model-trims-mode-option-fm.png)

- **Benutzerdefiniert** — vollständig frei konfigurierbares Verhalten,
  aufgebaut aus **Verhaltensregeln**, die Sie selbst hinzufügen.

### Benutzerdefinierte Trimmverhalten

![Verhalten hinzufügen](../assets/model-trims-mode-elevator-add-behaviour.png)
![Verhaltensoptionen](../assets/model-trims-mode-elevator-edit-behaviour.png)

Jede Verhaltenszeile besitzt eine Bedingung und eine der folgenden
Optionen:

- **Abgekoppelt** — deaktiviert die Trimmung gezielt unter dieser
  Bedingung (anstatt sie mit Modus = OFF vollständig abzuschalten).

  ![Abgekoppelt](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Bedingung für Abgekoppelt](../assets/model-trims-mode-unplugged-select.png)

- **Normal** (Standard) — gewöhnliches Trimmverhalten.
- **Gleich (einer anderen Trimmung)** — diese Trimmung übernimmt exakt den
  Trimmwert einer anderen Bedingung.

  ![Gleich](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Offset + (andere Trimmung)** — diese Trimmung wird zum Trimmwert einer
  anderen Bedingung addiert.

  ![Offset](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Praxisbeispiel** — ein Segler mit einer Basis-Höhenrudertrimmung für
**Cruise** sowie davon abhängigen Trimmungen für **Speed** und
**Thermal**:

![FM5 Speed auswählen](../assets/model-trims-mode-elevator-custom-select.png)
![FM4 Thermal auswählen](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Trimmen Sie das Modell in der Standardflugphase (Cruise) auf
   Horizontalflug.
2. Fügen Sie ein Verhalten hinzu: **Offset + Default** mit der Bedingung
   `FM5(Speed)`. Jede in der Flugphase Speed vorgenommene Trimmänderung
   wird nun als Offset auf den Basiswert von Cruise gespeichert — getrennt,
   aber dennoch von ihm abhängig.

   ![Offset für Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Fügen Sie auf die gleiche Weise ein zweites Verhalten hinzu:
   **Offset + Default** mit der Bedingung `FM4(Thermal)`. (Sobald das erste
   Verhalten existiert, bietet der Dialog zusätzlich `Equal FM5(Speed)` und
   `Offset + FM5(Thermal)` als Optionen an, da nun auch auf dieses
   Verhalten Bezug genommen werden kann.)

   ![Offset für Speed und Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Mit dieser Konfiguration verschiebt eine spätere Änderung der
Basistrimmung von Cruise (etwa nach einer Schwerpunktänderung) die
Trimmungen von Speed und Thermal automatisch um denselben Betrag, da es
sich um Offsets auf diesen Wert und nicht um unabhängige Werte handelt.

- **Audio** — deaktiviert die übliche Trimmansage für eine umgewidmete
  Trimmung, wenn diese nicht mehr sinnvoll ist.

## Zusätzliche Trimmungen

![Zusätzliche Trimmung hinzufügen](../assets/model-trims-add-trim-select.png)
![Einstellungen der zusätzlichen Trimmung](../assets/model-trims-add-trim-edit.png)

**Zusätzliche Trimmung hinzufügen** erzeugt eine Trimmung über die vier
Standardknüppel (und T5/T6) hinaus: **Name**, Quellen für **Auf**/**Ab**
zur Ansteuerung sowie dieselben Optionen für **Bereich**, **Schritt**,
**Modus** und **Audio** wie oben.

## Kreuztrimmung

![Kreuztrimmung](../assets/model-trims-cross.png)
![Kreuztrimmung bearbeiten](../assets/model-trims-cross-edit.png)

Legt fest, welcher Trimmschalter tatsächlich welchen Steuerknüppel trimmt
— erlaubt also, die Trimmung eines Knüppels über ein anderes physisches
Trimmelement als üblich anzusteuern. (T5/T6 stehen nur beim X20 Pro und
X18 zur Verfügung.)

## Sofort-Trimmung {: #instant-trim }

![Sofort-Trimmung](../assets/model-trims-instant-trim.png)

Solange aktiv, werden die aktuellen Knüppelpositionen in die entsprechenden
Standardtrimmungen (und Kreuztrimmungen) übernommen. Am besten auf einen
Schalter legen, der erreichbar ist, ohne die Knüppel loszulassen — im
geraden Horizontalflug auslösen, um die Trimmungen sofort zu setzen,
anstatt bei stark verstellten Trimmungen wiederholt eine Trimmtaste zu
betätigen. Nach dem Trimmflug wieder deaktivieren, um die Trimmungen
später nicht versehentlich zu verstellen.

!!! note
    Die Sofort-Trimmung ist nur aktiv, solange eine der Hauptansichten
    angezeigt wird.

## Trimmungen in Subtrims übernehmen

![Trimmungen in Subtrims übernehmen](../assets/model-trims-move-trims-to-subtrims.png)

Nach dem Austrimmen auf Horizontalflug wird der Trimmwert eines Kanals
(z. B. Höhenruder) in dessen [Subtrim](outputs.md)-Einstellung übernommen
und die angezeigte Trimmung auf null zurückgesetzt — eine saubere
Möglichkeit, später zu prüfen, ob sich die Flugtrimmung verändert hat.

Bei Verwendung von Flugphasen kann ein Kanal mehrere relevante Trimmwerte
besitzen, während das Subtrim in den Ausgängen eine einzige globale
Einstellung für alle Flugphasen ist. Diese Funktion berücksichtigt das:
Sie übernimmt die Trimmung der **aktuell ausgewählten** Flugphase in das
Subtrim, setzt diese Trimmung zurück und passt die Trimmungen *aller
anderen* Flugphasen desselben Kanals kompensierend an — sodass die
tatsächliche Ruderstellung in jeder Flugphase insgesamt unverändert
bleibt.

!!! tip
    Führen Sie dies aus Konsistenzgründen immer aus derselben
    „Basis“-Flugphase heraus aus (z. B. Cruise bei einem Segler) — solange
    Sie das tun, kann der Vorgang gefahrlos wiederholt werden.

Große Trimm- oder Subtrimwerte führen zu sehr asymmetrischen Ausschlägen —
besser, die Ursache mechanisch zu beheben. Ziel sind Anlenkungen im
90°-Winkel bei neutralen Rudern (Ausnahme sind Wölbklappen, bei denen man
etwas Ausschlag nach oben gegen mehr Ausschlag nach unten eintauscht);
anschließend lässt sich mit **PWM center** exakt auf 90° feinjustieren,
sobald die Anlenkung nahe dran ist.
