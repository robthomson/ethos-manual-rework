---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Kurven

![Kurventypen](../assets/model-curves-type.png)

Wiederverwendbare Übertragungskurven für [Mischer](mixes.md#anatomy-of-a-mix) oder
[Ausgänge](outputs.md#editing-a-channel) — das integrierte Expo steht in beiden
direkt zur Verfügung, alles Weiterführende wird hier definiert (oder über
**Kurve hinzufügen**, das direkt aus beiden Bearbeitungsbildschirmen erreichbar
ist). Bis zu 50 Kurven sind verfügbar; standardmäßig existiert keine davon (Expo
ist unabhängig davon immer integriert). Mit **+** wird eine Kurve hinzugefügt;
durch Antippen einer vorhandenen Kurve erscheinen
**Bearbeiten**/**Verschieben**/**Kopieren-Einfügen**/**Klonen**/**Löschen**.

![Kurve hinzufügen](../assets/model-curves-add.png)

## Kurventypen

- **Expo** — Standardwert 40; positive Werte machen die Reaktion um die
  Mittelstellung weicher, negative Werte machen sie schärfer. Eine weichere
  Reaktion um die Knüppelmitte hilft, Übersteuerung zu vermeiden, insbesondere
  bei weniger erfahrenen Piloten.

  ![Expo](../assets/model-curves-expo.png)

- **Funktion** — ein kleiner Satz fester mathematischer Formen:

  ![Funktionstypen](../assets/model-curves-fn-types.png)

  - **x > 0** — gibt die Quelle im positiven Bereich unverändert weiter; im
    negativen Bereich wird 0 ausgegeben.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — das Spiegelbild: gibt im negativen Bereich weiter, im positiven
    Bereich 0.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — gibt die Quelle als Absolutwert weiter (immer positiv).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — gibt 100 % aus, solange die Quelle positiv ist, und 0, solange
    sie negativ ist (ein harter Umschalter, keine Durchleitung).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — gibt −100 % aus, solange die Quelle negativ ist, und 0, solange
    sie positiv ist.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — gibt −100 % im negativen und +100 % im positiven Bereich aus.

    ![|f|](../assets/model-curves-fn-barf.png)

  Jeder Kurventyp — auch Funktion — besitzt zudem einen **Offset**, der die Kurve
  auf der Y-Achse nach oben oder unten verschiebt (eine Nachkommastelle
  Genauigkeit, wie bei Y-Werten generell):

  ![Funktions-Offset](../assets/model-curves-fn-xgt0-offset.png)

- **Benutzerdefiniert** — eine punktbasierte Kurve, standardmäßig mit 5 Punkten,
  maximal 21.

  ![Benutzerdefinierte Kurve mit 5 Punkten](../assets/model-curves-custom5.png)

  - **Glätten** — legt eine glatte Kurve durch alle Punkte statt gerader
    Teilstrecken zwischen ihnen.

    ![Geglättete Kurve](../assets/model-curves-custom5-2-smooth.png)

  - **Einfacher Modus** — **Ein** beschränkt die Bearbeitung auf gleichmäßig
    verteilte Y-Koordinaten (X ist fest); **Aus** erlaubt die Bearbeitung von X
    und Y je Punkt, ausgenommen die Endpunkte bei −100 %/+100 %, die gesperrt
    sind, da die Kurve stets den gesamten Signalbereich abdecken muss.

    ![Einfacher Modus aus](../assets/model-curves-custom-easy-off.png)

  **Bedienelemente des Editors** (gleiches Schema wie beim [Editor für
  Ausgleichskurven der Ausgänge](outputs.md#balance-channels)):

  - **Quelle** — standardmäßig die eigene(n) Mischerquelle(n) der Kurve, oder
    **Automatischer Analogeingang**, um den zuerst bewegten
    Steuerknüppel/Schieberegler/Potentiometer zu übernehmen.
  - Einrasten auf den nächstgelegenen Punkt beim Drehgeber sowie ein Schalter
    **Sperren**, um die Eingaben einzufrieren, während die resultierende Bewegung
    der Ruderfläche beobachtet wird.
  - Ein Live-Cursor zeigt den aktuellen Eingangswert, der die Kurve ansteuert, um
    ihn vor dem Anpassen mit einem Punkt in Deckung zu bringen.

## Eine Kurve über eine Var ansteuern

Sowohl der **Offset** einer Funktionskurve als auch ein einzelner Punkt einer
**benutzerdefinierten** Kurve können anstelle eines festen Werts von einer
[Var](variables.md) angesteuert werden — und diese Var lässt sich wiederum über
eine umgewidmete Trimmung im Flug verstellen:

![Funktions-Offset über eine Var](../assets/model-curves-fn-offset-var.png)
![Punkt einer benutzerdefinierten Kurve über eine Var](../assets/model-curves-custom-with-var.png)

Siehe [Variablen](variables.md) und [Anleitung: Im Flug verstellbare
Kompensationskurve](../how-to/in-flight-compensation-curve.md) für ein
vollständig durchgearbeitetes Beispiel dieses Musters.
