---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telemetrie

![Erkannte Sensoren](../assets/model-telemetry-discovered-new-sensors.png)

Telemetrie überträgt Informationen vom Modell zurück zum Piloten —
Verbindungsqualität (RSSI, VFR), Spannungen und Ströme sowie alles, was ein
angeschlossener Sensor sonst meldet (GPS-Position, Höhe und so weiter). Pro
Modell werden bis zu 100 Sensoren unterstützt; Erkennung und Konfiguration
erfolgen hier, doch *angezeigt* wird Telemetrie als [Widgets auf
Anzeigebildschirmen](../displays/index.md), die separat unter Bildschirme
konfigurieren eingerichtet werden.

## Funktionsweise der FrSky-Telemetrie {: #how-frsky-telemetry-works }

Die Sensoren von FrSky kommen ohne Hub aus: **Smart Port (S.Port)** ist ein
3-adriger Bus (Gnd, V+, Signal), der in beliebiger Reihenfolge in Reihe an den
S.Port-Anschluss von Empfängern der X-/S-Serie und neuer angeschlossen wird und
im Halbduplex-Betrieb mit 57.600 bps arbeitet (F.Port und FBUS sind schneller).

- **Physical ID** — bis zu 28 Knoten (einschließlich des Empfängers) teilen
  sich den Bus, jeder benötigt eine eindeutige Physical ID (00–1B hex).
  FrSky-Geräte werden mit sinnvollen Standardwerten ausgeliefert (z. B.
  Vario = 00, FLVSS = 01, Current = 02, GPS = 03) — werden zwei gleiche Geräte
  angeschlossen, muss die Physical ID des zweiten über die
  [Gerätekonfiguration](../system-setup/devices.md) geändert werden.
- **Application ID** — unabhängig von der Physical ID: Ein Sensor kann mehrere
  Werte melden, jeder mit eigener Application ID. Ein Vario hat eine Physical
  ID, aber zwei Application IDs (Höhe, Vertikalgeschwindigkeit); ein FLVSS hat
  eine Physical ID und eine Application ID (Spannung). Um zwei 6S-Akkus mit
  zwei FLVSS-Sensoren zu überwachen, müssen beim zweiten **beide** IDs geändert
  werden — die Physical ID für die exklusive Buskommunikation, die Application
  ID, damit der Empfänger Lipo 1 und Lipo 2 unterscheiden kann (z. B. `0300` →
  `0301`). Üblicherweise wird die 4. Hex-Stelle variiert, 0–F.

  !!! note
      Sensoren, die sich eine Application ID teilen, aber unterschiedliche
      Physical IDs haben, sind nur bei deaktivierter
      [Sensorkonflikterkennung](../system-setup/alerts.md) zulässig — eine
      Speziallösung, nicht der Regelfall.

Jeder empfangene Wert wird als eigener Sensor geführt: Wert, Physical/
Application ID, ein editierbarer Name, Einheit, Nachkommastellen, ein
optionales Kennzeichen zur Protokollierung auf der SD card sowie eigene
laufende Min-/Max-Werte. Nach der Einrichtung werden Sensoren bei jedem
Einschalten automatisch erkannt, beim ersten Mal muss die Erkennung jedoch
**manuell** erfolgen. Ein einmal erkannter Sensor kann per Sprachausgabe
angesagt, in [berechnete Sensoren](#calculated-sensors) eingespeist, in
[logischen Schaltern](logical-switches.md), [Vars](variables.md) oder
[Mischern](mixes.md) verwendet, auf einem eigenen Telemetriebildschirm
angezeigt oder direkt auf dieser Konfigurationsseite abgelesen werden, ganz
ohne einen Bildschirm anzulegen.

**FBUS** (früher F.Port2) geht noch einen Schritt weiter und legt die
SBUS-Steuerung und die S.Port-Telemetrie mit 460.800 bps auf eine einzige
Leitung (gegenüber 115.200 bei F.Port und 57.600 bei S.Port — die drei
Bitraten sind untereinander inkompatibel); zudem kann ein Host auf dieser
einen Leitung mit mehreren Slave-Zubehörgeräten kommunizieren, die sich alle
drahtlos vom Sender aus konfigurieren lassen.

### Telemetrie mit mehreren Empfängern (ACCESS Trio)

Mit bis zu drei unter [RF
System](rf-system.md#registering-and-binding-a-receiver-access) registrierten
Empfängern kann jeder gebundene Empfänger über RX1/RX2/RX3 einzeln
konfiguriert werden (Port-Pins usw.). Normalerweise gibt es einen eingehenden
Telemetriepfad pro RF-Verbindung — die Tandem-/TD-Systeme bilden die Ausnahme
und betreiben 2,4 GHz und 900 MHz als zwei Pfade auf einem Modul. Die aktive
Telemetriequelle kann sich je nach RF-Bedingungen während des Fluges ändern;
der Sensor **RX** meldet in Echtzeit, welcher Empfänger gerade Telemetrie
sendet (und protokolliert dies).

Der übliche Aufbau: Den S.Port-Sensorbus über alle drei Empfänger
durchschleifen, mit gemeinsamer Stromversorgung, dann jeden Empfänger
registrieren/binden und die Sensoren wie gewohnt erkennen lassen — die
Telemetriequelle wechselt automatisch mit dem aktiven RX, und die Daten
*externer* S.Port-Sensoren folgen transparent mit. (Empfängerinterne Sensoren
— RSSI, VFR, RxBatt, ADC2 und RX selbst — werden auf diese Weise nicht
verknüpft; sie werden stets für den Empfänger gemeldet, der aktuell die Quelle
ist. Gleichzeitige Telemetrie von allen dreien ist geplant, aber noch nicht
verfügbar.)

## Sensoren zur Verbindungsqualität

- **RSSI** (Receiver Signal Strength Indicator) — wie stark die Übertragung des
  Senders am Empfänger ankommt. Standardalarme: **ACCESS**/**TD**/
  **TW** 35 (niedrig) / 32 (kritisch), Kontrollverlust bei etwa 28; **ACCST**
  45 / 42, Kontrollverlust bei etwa 38. „Telemetrie verloren" wird ausgelöst,
  wenn die Verbindung vollständig abgerissen ist — ab diesem Punkt **können
  keine weiteren Alarme mehr ertönen**, da dem Sender keine Telemetrie zur
  Auswertung mehr zur Verfügung steht; werten Sie dies als Aufforderung, sofort
  umzukehren. (Bei weniger als ca. 1 m Abstand kann der Empfänger übersteuert
  werden und Alarmschleifen aus Verlust/Wiederherstellung erzeugen — kein
  echter Fehler.) RSSI bildet die effektive Reichweite gut ab, VFR ist jedoch
  der zuverlässigere Indikator für die Verbindungsqualität.

  ![RSSI-Sensor](../assets/model-telemetry-edit-rssi-sensor.png)

  TD-Empfänger melden ein RSSI pro Band (2.4G, 900M); TW-Empfänger ebenfalls
  eines pro Band (2.4FSK, 2.4LoRa, 900M) — aktivieren Sie **Individual RSSI
  alert per band**, um für jedes Band eine eigene Sprachwarnung statt einer
  kombinierten Warnung zu erhalten:

  ![Individuelle RSSI-Warnung](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — gültige Pakete pro 100 empfangene; ab ACCESS 2.1
  der Ersatz dafür, die Verlustrate in den RSSI-Wert einzurechnen. Die
  Standard-**Low value warning** liegt bei 50 %.

  ![VFR-Sensor](../assets/model-telemetry-edit-vfr-sensor.png)

  TD-/TW-Empfänger melden zwei VFR-Ströme (einen pro Band); **Rx VFR** (bei
  TD-/TW-/AP-/AP-Plus-Empfängern) zählt stattdessen jeden gültigen Frame
  unabhängig davon, über welches Band er eintraf — der Wert, den man im Auge
  behalten sollte, wenn nur ein einziger VFR-Wert verfolgt wird.

- **RxBatt** — Empfängerakkuspannung.
- **ADC2** — ein zweiter analoger Spannungseingang, bei Empfängern, die ihn
  unterstützen.
- **SWR** — Antennen-SWR bei Verwendung einer externen Antenne.
- Lage-/Bewegungssensoren, sofern unterstützt: **R.Angle**, **P.Angle**,
  **AccX/Y/Z**.

Zu jedem numerischen Sensor werden zudem automatisch Min-/Max-Sensoren
`<name>-`/`<name>+` angelegt, auch wenn sie in der Hauptsensorliste nicht
aufgeführt werden.

## Sensoren erkennen {: #discovering-sensors }

![Neue Sensoren erkennen: ein](../assets/model-telemetry-discover-new-sensors-on.png)

Wenn alles gebunden und eingeschaltet ist, aktivieren Sie **Discover new
sensors** — ein blinkender Punkt (oder ein roter Wert, falls noch keine Daten
vorliegen) markiert jeden Sensor, sobald er gefunden wird, und der Bildschirm
füllt sich automatisch. Dies muss **pro Modell** wiederholt werden und
außerdem jedes Mal, wenn ein neuer Sensor hinzukommt.

![Neue Sensoren erkennen: aus](../assets/model-telemetry-discover-new-sensors-off.png)

- Schalten Sie die Erkennung anschließend wieder **Aus**.
- **Delete all** löscht alle Sensoren, um neu zu beginnen.

  ![Sensoren gelöscht](../assets/model-telemetry-sensors-deleted.png)

- **Competition mode** reduziert die Telemetrie auf RSSI und RxBatt — für
  Wettbewerbe, die nur Sensoren zum Verbindungsstatus zulassen. Nach dem
  Deaktivieren ist ein Neustart erforderlich, bevor Sensoren erneut erkannt
  werden können.

  ![Bestätigung Wettbewerbsmodus](../assets/model-telemetry-comp-only-confirm.png)

- Der Telemetriemodus **Bluetooth** koppelt mit der FrSky-Handy-App FreeLink,
  die Telemetrie live anzeigen und außerdem FrSky-Geräte wie stabilisierte
  Empfänger konfigurieren kann.

  ![Bluetooth-Telemetrie](../assets/model-telemetry-bt-option.png)

## Sensor bearbeiten {: #editing-a-sensor }

![Auswahl der Bearbeitungsoptionen](../assets/model-telemetry-edit-option-select.png)

Tippen Sie auf einen Sensor für **Edit**, **Move**, **Reset** oder **Delete**.
Übliche Felder: **Value** (schreibgeschützt), **ID** (Physical + Application ID
sowie sendender Empfänger), **Name**, **Unit**, **Decimals**, **Range** (feste
Skalierungsgrenzen — vor allem relevant, wenn der Sensor als Kanalquelle
verwendet wird), **Write logs**, **Reset** (eine Quelle, die diesen Sensor
zurücksetzt) und **Sensor lost warning delay** (ganz deaktivierbar oder 1–30 s,
Standard 10 s, um kurze Aussetzer herauszufiltern — bedenken Sie das Risiko
eines zu hohen Werts; die Meldung „Sensor verloren" wird nur einmal
ausgegeben, selbst wenn viele Sensoren gleichzeitig ausfallen; für
empfängerinterne Sensoren standardmäßig deaktiviert, da diese selten
ausfallen).

Manche Sensoren haben zusätzliche eigene Felder:

- **ADC2** — **Ratio** und **Offset** zur Korrektur der Skalierung.

  ![ADC2-Sensor bearbeiten](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — Schwellenwerte **Critical value** und **Low value warning**.
- **VFR** — **Low value warning** (Standard 50 %).
- **VSpeed** (Vertikalgeschwindigkeit des Varios) — **Range** bis ±100 m/s
  (Standard ±10 m/s). Das Audioverhalten des Varios selbst befindet sich jetzt
  unter der [Sonderfunktion Play Vario](special-functions.md), nicht mehr hier.

  ![VSpeed-Sensor bearbeiten](../assets/model-telemetry-edit-vspeed-sensor.png)

## DIY-/Fremdsensoren

![DIY-Sensor anlegen](../assets/model-telemetry-diy-sensor-select.png)

**Create DIY Sensor** fügt einen Nicht-FrSky-Sensor manuell hinzu: **Auto
detect** (füllt Physical ID, Application ID und Modul nach Möglichkeit
automatisch aus) oder manuelle Eingabe, dazu **Protocol decimals/unit**
(eingehende Genauigkeit, 0–3 Nachkommastellen, und die native Einheit) und
**Display decimals/unit** (unabhängig von denen des Protokolls) neben denselben
Feldern **Range**/**Ratio**/**Offset**/**Write logs**/**Reset**/**Sensor lost
warning delay** wie bei jedem anderen Sensor.

![DIY-Sensor automatisch erkennen](../assets/model-telemetry-diy-sensor-auto-detect.png)

## Berechnete Sensoren {: #calculated-sensors }

![Berechneten Sensor anlegen](../assets/model-telemetry-calculated-sensor-select.png)

Leiten Sie einen neuen Sensor aus einem oder mehreren vorhandenen ab:

- **Consumption** — verbrauchte Energie, integriert aus einem Stromsensor
  (z. B. der FAS-Serie). Einheit mAh/Ah, Bereich bis 1000 Ah.

  ![Verbrauchssensor](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Distance** — aus einer GPS-Quelle (plus einer Höhenquelle für die
  3D-Entfernung). Einheiten cm/m/km/ft, bis 20 km.

  ![Entfernungssensor](../assets/model-telemetry-calculated-sensor-distance.png)

- **Trip** — aufsummierte Entfernung zwischen aufeinanderfolgenden GPS-Fixes.
  Gleiche Einheiten, bis 1000 km.

  ![Trip-Sensor](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — kaskadiert zwei oder mehr Lipo-Spannungssensoren, um Akkus
  größer als 6S zu überwachen (bis 67,2 V/8S). Wählen Sie jeden Zellensensor
  von niedrig nach hoch; bei jedem zusätzlichen Lipo-Sensor müssen zuvor
  **sowohl** Physical als auch Application ID in der
  [Gerätekonfiguration](../system-setup/devices.md) geändert werden (das dortige
  Werkzeug zur Lipo-Spannungseinrichtung hilft dabei), die Sensoren einzeln
  nacheinander erkannt und so umbenannt werden, dass sie unterscheidbar sind.

  ![Multi-Lipo-Sensor](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Percent** — skaliert einen Sensor auf 0–100 % um, mit einer Option
  **Invert** (z. B. um die *verbleibende* statt der verbrauchten Menge in
  Prozent anzuzeigen).

  ![Prozentsensor](../assets/model-telemetry-calculated-sensor-percent.png)

- **Power** — Leistung aus einem Paar aus **Current**- und **Voltage**-Quelle,
  bis 1.000.000 W.

  ![Leistungssensor](../assets/model-telemetry-calculated-sensor-power.png)

- **Custom** — eine beliebige Formel, verkettet aus einer oder mehreren Quellen.

Jeder berechnete Sensor besitzt außerdem die Option **Persistent** (übersteht
Ausschalten/Modellwechsel und wird bei der nächsten Verwendung wieder geladen)
sowie eine Schaltfläche **Reset** direkt im Bearbeitungsbildschirm.

### Benutzerdefinierte Sensoren

![Benutzerdefinierter Sensor](../assets/model-telemetry-edit-custom-sensor.png)

Ausgehend von einer Quelle verkettet **Add** weitere Rechenoperationen:
**Add(+)**, **Minus(-)**, **Multiply(×)**, **Divide(/)**, **Min**,
**Max**, **Sqrt**. Die Einheiten sind aus einer langen Liste wählbar, die
Spannung, Strom, Kapazität, Leistung, Entfernung, Geschwindigkeit, Zeit,
Temperatur, Prozent, Winkel, Druck und mehr umfasst; Bereich −1.000.000 bis
1.000.000, 0–4 Nachkommastellen.

![Rechenzeile hinzufügen](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "Spitzenleistung"
    Multiplizieren Sie einen Spannungssensor (`VFAS`) mit einem Stromsensor
    (`Current`) und fügen Sie dann einen **Max**-Schritt hinzu, der den
    aktuellen Wert des Sensors selbst (`MaxPower`) referenziert, um den
    höchsten aufgetretenen Messwert festzuhalten — 288 W in diesem
    Beispieldurchlauf:

    ![MaxPower-Beispiel](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "Rechnen mit einer Konstante"
    Als Quelle ist `RSSI 2.4G` eingestellt (Anzeige 64 dB), gefolgt von einer
    **Subtract**-Aktion, deren eigene Quelle per langem Druck ausgewählt und
    mit **Convert to value** in eine editierbare Konstante (20) statt einer
    Live-Quelle umgewandelt wurde — das Ergebnis ist konstant 44 dB (64 − 20):

    ![Subtraktionsbeispiel](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![In Wert umwandeln](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "Der interne Wert einer Quelle"
    Jede [Quelle](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    besitzt einen internen Ganzzahlbereich von ±1024, der ihrem angezeigten
    Bereich von ±100 % entspricht — direkt sichtbar, wenn man einen
    benutzerdefinierten Sensor beispielsweise auf Gas richtet: Vollgas ergibt
    intern **+1024**, Vollausschlag in die Gegenrichtung **−1024**.

    ![Interner Wert bei Maximum](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![Interner Wert bei Minimum](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
