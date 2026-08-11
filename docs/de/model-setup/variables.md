---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Variablen

![Variablen](../assets/model-vars.png)

Variablen („Vars") sind benannte Container für modelleigene
Einstellungswerte, die an jeder anderen Stelle der Programmierung
referenziert werden können – einschließlich [Mischer](mixes.md). Indem
sie in einem eigenen Bereich abgelegt werden, trennt man die
*Konfigurationsdaten* eines Modells von seiner *Programmierlogik*:
Anstatt Dutzende von Mischern zu durchsuchen, um einen Wert zu finden und
anzupassen, befindet sich alles an einer Stelle mit einem aussagekräftigen
Namen. Es stehen 64 Vars zur Verfügung; standardmäßig existiert keine.
Mit **+** wird eine hinzugefügt; durch Antippen einer vorhandenen Var
erhält man **Bearbeiten**/**Verschieben**/**Kopieren**/**Klonen**/**Löschen**.

![Variable hinzufügen](../assets/model-vars-add.png)

Eine Var kann eine feste Konstante enthalten oder innerhalb
benutzerdefinierter Grenzen verstellbar sein (damit unsinnige Werte keinen
Absturz verursachen) und kann pro aktiver Bedingung (z. B. pro Flugphase)
einen *unterschiedlichen* Wert annehmen. Die Werte bleiben über Sitzungen
hinweg erhalten. Eine Var ersetzt jeden gewöhnlichen numerischen Wert
überall dort, wo die [Options-Funktion](../getting-started/user-interface-and-navigation.md#the-options-feature)
verfügbar ist (die Felder mit dem Hamburger-Symbol).

!!! example
    Ein Segler mit geteilten Querrudern (die inneren Sektionen dienen
    zugleich als Landeklappen) soll überall dort, wo alle vier Ruder als
    Querruder arbeiten, eine einzige gemeinsame Einstellung für das
    Querruder-Differential verwenden – eine Var, die diesen einen Wert
    enthält und aus jedem betroffenen Mischer referenziert wird, hält ihn
    konsistent und muss nur an einer Stelle abgestimmt werden.

## Eine Var hinzufügen

![Neue Variable](../assets/model-vars-new_var.png)

- **Wert** — aktueller Wert (nur Anzeige, nicht editierbar).
- **Name** — editierbar.
- **Kommentar** — Freitext zur Erläuterung des Zwecks.
- **Bereich** — untere/obere Grenzen (eine Nachkommastelle, innerhalb
  ±500 %), die der Wert der Var niemals überschreiten kann.

### Werte

![Variablenwerte](../assets/model-vars-values.png)

- **Fest** — eine einzelne Konstante mit einer Nachkommastelle.
- **Mehrfach/variabel** — **Neuen Wert hinzufügen** hängt pro aktiver
  Bedingung einen Wert an. Beispiel: `Var12` liefert 9 %, solange die
  Flugphase Thermik (FM4) aktiv ist, und −3 %, solange Speed (FM5) aktiv
  ist, wobei der Bereich auf −10 %…+15 % begrenzt ist, sodass keiner der
  Werte sinnvolle Grenzen überschreiten kann:

  ![Flugphasenabhängige Werte](../assets/model-vars-fm-dependent.png)
  ![Einen Wert hinzufügen](../assets/model-vars-add-value.png)

### Aktionen

![Variablenaktionen](../assets/model-vars-actions.png)
![Aktion hinzufügen](../assets/model-vars-add-action.png)

Aktionen verändern den Wert einer Var im Zeitverlauf, gesteuert durch eine
Eingangsgröße.

**Umgewidmete Trimmung** — übergibt eine der physischen Trimmungen der
Verstellung dieser Var anstelle ihrer normalen Funktion, üblicherweise
beschränkt auf eine aktive Bedingung:

![Eine Trimmung umwidmen](../assets/model-vars-functions-repurpose.png)
![Umzuwidmende Trimmung auswählen](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Die Gas-Trimmung wird zur Verstellung einer Var für die
    Wölbklappenkompensation umgewidmet, allerdings nur, solange die
    Flugphase Landung (FM3) aktiv ist, mit dem Bereich 0–25 % und einer
    Schrittweite von 1,0 % pro Klick. Außerhalb dieser aktiven Bedingung
    kehrt die Trimmung automatisch zu ihrer gewöhnlichen Funktion zurück.

**Arithmetische Aktionen** — gesteuert durch eine beliebige Eingangsgröße:

- **Zuweisen** — setzt die Var auf einen bestimmten Wert.
- **Addieren** / **Subtrahieren** / **Multiplizieren** / **Dividieren** —
  Rechenoperationen mit dem aktuellen Wert.
- **Prozent** — wendet einen Prozentsatz der steuernden Eingangsgröße an.
- **Min** / **Max** — begrenzt die Var gegenüber der steuernden
  Eingangsgröße.

  ![Funktionsaktionen](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` weist einer Var direkt 40 % zu; `FS1(edge)` addiert bei
    jedem Druck 2 (begrenzt auf das Maximum des Bereichs); `FS2(edge)`
    subtrahiert bei jedem Druck 2 (begrenzt auf das Minimum des Bereichs).
    Die Option **Edge** (langer Druck auf den Funktionsschalter) ist hier
    entscheidend – ohne sie würde die Aktion kontinuierlich ausgelöst,
    solange der Schalter gehalten wird, statt einmal pro Betätigung.

  ![Durchgerechnetes Beispiel](../assets/model-vars-calc-example.png)
