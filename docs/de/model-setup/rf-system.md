---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# RF-System

Konfiguriert das interne und/oder externe HF-Modul des Modells, die
Owner Registration ID, das Binden von Empfängern sowie die
Empfängeroptionen. Hier wird auch festgelegt, ob ein Modell das interne
oder das externe Modul verwendet — anders als bei fast allem anderen in
den [Systemeinstellungen](../system-setup/index.md) erfolgt die Auswahl
der HF-Hardware **pro Modell** und nicht senderweit.

!!! note "Screenshots ausstehend"
    Die Screenshots für diesen Abschnitt wurden noch nicht erstellt (siehe
    [Screenshot-Pipeline](../contributing/screenshot-pipeline.md)) — die
    nachfolgenden Inhalte sind korrekt, liegen aber vorerst nur als Text
    vor.

## Owner Registration ID {: #owner-registration-id }

Ein 8-stelliger, eindeutiger Code (Groß- und Kleinbuchstaben sowie
Ziffern, keine Sonderzeichen), der bei der Registrierung zur
**Registration ID** eines Empfängers wird. Wird auf mehreren Sendern
*derselbe* Code eingetragen, lässt sich **Smart Share** zwischen ihnen
nutzen — richten Sie dies ein, bevor Sie das zu teilende Modell anlegen.
Kompatibel mit EdgeTX; nur teilweise kompatibel mit OpenTX.

## HF-Ausgabe deaktivieren

Halten Sie beim Einschalten `PAGE` gedrückt, um für diese Sitzung sowohl
die interne als auch die externe HF-Ausgabe zu deaktivieren (eine Warnung
bestätigt die Abschaltung). Die Einstellung **State** des Moduls selbst
bleibt auf ON — ein normaler Neustart stellt den regulären Sendebetrieb
wieder her.

## Betriebsarten des internen Moduls

Das interne Modul von X18/X20/X20S/X20HD (TD-ISRM) arbeitet in einer von
drei Betriebsarten — das TD-ISRM Pro-Modul der X20 Pro/R/RS ist
vergleichbar, bietet zusätzlich jedoch LoRa- und Tandem-Dualband-Varianten.
Die gewählte Betriebsart **muss zum Empfänger passen**, sonst schlägt das
Binden fehl; nach einem Wechsel der Betriebsart sind alle Kanäle und
insbesondere das Failsafe-Verhalten sorgfältig erneut zu prüfen.

- **ACCESS** — 2,4-GHz- und 900-MHz-Pfad arbeiten im Tandem unter einem
  gemeinsamen Satz von ACCESS-Einstellungen. Insgesamt bis zu drei
  Empfänger, in beliebiger Kombination aus 2,4 GHz (24 Kanäle) und
  900 MHz (16 Kanäle); die Telemetrie beider Bänder ist gleichzeitig
  aktiv und nach Band gekennzeichnet. Eine Telemetriequelle **RX** meldet,
  welcher Empfänger aktuell die aktive Telemetriequelle ist.
- **ACCST D16** — ein einzelner 2,4-GHz-Pfad für ältere Empfänger der
  „X“-Serie.
- **TD mode** — latenzarmes Tandem mit großer Reichweite über 2,4 GHz +
  900 MHz für Tandem-Empfänger, 24 Kanäle je Band.

**Flex-Firmware**-Versionen ergänzen eine zweite Spalte „Type“, um in
jeder der drei genannten Betriebsarten zwischen der Modulation FLEX915M
(FCC-Variante, 915 MHz) und FLEX868M (LBT-Variante, 868 MHz) umzuschalten
— es müssen die jeweils passenden Antennen montiert sein. Anwender in der
EU können auf 868 MHz mit 200/500 mW arbeiten; bei 25 mW läuft die
Telemetrie über 868 MHz, bei 200/500 mW wechselt sie aus
Konformitätsgründen auf 2,4 GHz.

Jede Kombination aus Betriebsart und Kanalbereich bedeutet einen
Kompromiss bei der Aktualisierungsrate — unter ACCESS werden z. B.
8 Kanäle alle 7 ms, 16 Kanäle alle 14 ms und 24 Kanäle alle 21 ms
aktualisiert (rotierend in Blöcken zu 8), und mit kompatiblen Empfängern
(RS-Serie, ab v2.1.7) steht für Ch1–8 ein 4-ms-**Racing mode** zur
Verfügung.

## Empfänger registrieren und binden (ACCESS) {: #registering-and-binding-a-receiver-access }

Das Binden eines ACCESS-Empfängers erfolgt in zwei Phasen — die
**Registrierung** muss pro Empfänger/Sender-Paar nur einmal durchgeführt
werden; das **Binden** kann danach beliebig oft drahtlos wiederholt
werden, ohne die Bind-Taste zu benötigen.

**Phase 1 — Registrieren**:

1. Tippen Sie auf **Register** (entfällt vollständig, wenn der Empfänger
   bereits registriert ist).
2. Halten Sie die Bind-Taste des Empfängers beim Einschalten gedrückt und
   warten Sie, bis beide LEDs leuchten. Der Dialog wechselt von „Waiting
   for receiver…“ zu „Receiver connected“ und trägt den Empfängernamen
   automatisch ein.
3. Bestätigen bzw. bearbeiten Sie die **Registration ID** (Vorgabe ist die
   oben genannte Owner Registration ID — übereinstimmende IDs auf mehreren
   Sendern sind die Voraussetzung für Smart Share), den **Rx name** sowie
   die **UID**. Die UID unterscheidet mehrere gemeinsam in einem Modell
   verwendete Empfänger — bei einem einzelnen Empfänger belassen Sie sie
   auf 0; bei mehreren (z. B. einer je 8-Kanal-Block) ist 0/1/2 üblich.
   Die UID lässt sich später nicht aus dem Empfänger auslesen, beschriften
   Sie ihn daher physisch.
4. Tippen Sie auf **Register**, bestätigen Sie „Registration ok“ und
   schalten Sie den Empfänger anschließend aus — er ist nun registriert,
   aber noch nicht gebunden.

**Phase 2 — Binden**:

!!! warning
    Binden Sie niemals bei angeschlossenem Elektromotor oder laufendem
    Verbrennungsmotor.

1. Empfänger aus; prüfen Sie, dass die richtige Modul-Betriebsart aktiv
   ist.
2. Tippen Sie auf **RX1** (oder 2/3) → **Bind**. Eine sich wiederholende
   Sprachansage „Bind“ bestätigt den Bind-Modus.
3. Schalten Sie den Empfänger ein, **ohne** die Bind-Taste zu betätigen,
   und wählen Sie ihn aus der erscheinenden Liste „Select device“ aus.
4. Bestätigen Sie „Bind successful“. Schalten Sie Sender und Empfänger aus
   und wieder ein — leuchtet die grüne LED des Empfängers und die rote ist
   aus, besteht die Verbindung. Ein erneutes Binden ist nur nötig, wenn
   eine der beiden Seiten ersetzt wird.
5. Wiederholen Sie den Vorgang gegebenenfalls für weitere Empfänger (RX2,
   RX3).

## Empfängeroptionen

Tippen Sie bei eingeschaltetem Empfänger auf dessen RX-Schaltfläche für:

- **Options** — **Telemetry** (ein/aus für diesen Empfänger), **Reduced
  telemetry power 25mW** (statt der üblichen 100 mW — nützlich, wenn nahe
  Servos HF-Störungen aufnehmen), **High PWM Speed** (7 ms
  Servo-Aktualisierung statt 18 ms — stellen Sie sicher, dass Ihre Servos
  das verkraften), **Telemetry port** (S.Port/F.Port/FBUS), **SBUS** (16
  oder 24 Kanäle — vor der Aktivierung muss jedes angeschlossene
  SBUS-Gerät SBUS-24 unterstützen) und **Channel Mapping**, um Kanäle
  bestimmten Empfängeranschlüssen zuzuordnen.
- **Share** — übergibt den Empfänger an einen anderen ACCESS-Sender mit
  *abweichender* Owner Registration ID. Tippen Sie am Quellsender auf
  Share (dessen grüne LED erlischt); am Zielsender binden Sie ganz normal
  — Share erspart die erneute Registrierung, da die ID automatisch
  übertragen wird. Beenden Sie Share am Quellsender, um die Freigabe zu
  beenden; erneutes Binden holt den Empfänger zurück. (Nicht erforderlich,
  wenn alle Sender bereits dieselbe Owner Registration ID verwenden —
  binden Sie dann einfach direkt an dem Sender, der das Modell steuern
  soll.)
- **Reset bind** — räumt nach einem Share auf und stellt die eigene
  Bindung wieder her; schalten Sie den Empfänger anschließend aus und
  wieder ein.
- **Factory reset** — setzt den Empfänger zurück, löscht seine UID und
  hebt die Registrierung vollständig auf.

Bei **ausgeschaltetem** Empfänger bietet dieselbe RX-Schaltfläche
**Options** (wartet auf die Verbindung des Empfängers), **Bind** (z. B. um
einen zuvor anderweitig gebundenen Empfänger neu zu binden) und **Clear**
(entspricht Reset bind).

## Redundante Empfänger {: #redundant-receivers }

Ein zweiter Empfänger kann zur Redundanz an einen freien RX-Slot gebunden
werden — 2,4 G und 900 M können sich jeweils gegenseitig absichern. Die
Redundanz von FrSky arbeitet **frameweise** und nutzt stets den besten
verfügbaren Frame (Active/Active-Failover), sodass die Steuerung bei
Bedarf von Frame zu Frame zwischen den Empfängern wechseln kann.

1. Verbinden Sie SBUS Out des redundanten Empfängers mit SBUS In des
   Hauptempfängers.
2. Aktivieren Sie das entsprechende interne HF-Modul (z. B. 900M) und
   stellen Sie Antenne/Sendeleistung ein.
3. Registrieren Sie den neuen Empfänger (falls noch nicht geschehen) und
   binden Sie ihn wie oben beschrieben an den freien RX-Slot.
4. Prüfen Sie, ob dessen grüne LED leuchtet — er wird nun als redundanter
   Empfänger geführt.

## Failsafe {: #failsafe }

Die Failsafe-Daten werden vom Sender etwa alle 10 Sekunden erneut
übertragen; bei TD-/TW-/AP-/AP-Plus-Empfängern werden sie zusätzlich im
Empfänger gespeichert und überstehen so einen Neustart des Empfängers.
Prüfen Sie das Failsafe nach jedem Firmware-Update eines Empfängers, das
dieses Verhalten hinzufügt, sorgfältig erneut.

- **Hold** — hält die zuletzt empfangenen Kanalpositionen.
- **Custom** — kanalweise: **Not Set**, **Hold**, **Custom** (ein fester
  Wert — tippen Sie auf das Pfeilsymbol, um den aktuellen Wert zu
  übernehmen, oder geben Sie ihn direkt ein) oder **No Pulses**.
- **No Pulses** — stellt die Impulsausgabe vollständig ein, für
  Flugcontroller mit eigener Return-to-Home-Funktion bei Signalverlust.
- **Receiver** — (Empfänger der X-Serie oder neuer) legt das Failsafe
  stattdessen im Empfänger selbst fest.

!!! warning
    Testen Sie die gewählte Failsafe-Einstellung sorgfältig, bevor Sie
    sich darauf verlassen.

## Reichweitentest {: #range-check }

Führen Sie diesen Test am Flugplatz vor jeder Flugsession mit einem neuen
oder geänderten Setup durch. Die Auswahl von **Range Check** reduziert die
Sendeleistung bewusst (eine sich wiederholende Sprachansage bestätigt den
Modus) und zeigt VFR%/RSSI in Echtzeit zur Beurteilung der Verbindungs­qualität
an. Die Sendeleistung im Reichweitentest liegt bei FrSky rund −10 dB
gegenüber dem normalen Betriebspegel von +20 dB; bei 1 m Höhe von Sender
und Empfänger ist mit einem kritischen Alarm bei etwa 30 m zu rechnen —
eine geringere Distanz unter normalen Bedingungen kann auf ein Problem
hindeuten.

Bei mehreren gebundenen Empfängern werden die Daten des Reichweitentests
pro Band jeweils nur für einen aktiven Empfänger angezeigt — schaltet man
den derzeit aktiven aus, übernimmt der nächste (in der Priorität 0/1/2,
angezeigt über den Sensor **RX**), sodass jeder der Reihe nach geprüft
werden kann.

## Externe und Fremd-HF-Module

Externe FrSky-Module (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
folgen demselben Register-/Bind-Ablauf wie das interne Modul, mit
protokollspezifischen Kanalzahlen, Sendeleistungen und
Antennenanforderungen — genaue Werte entnehmen Sie der Anleitung des
jeweiligen Moduls.

**ELRS** (ExpressLRS) wird sowohl über den ELRS-Modus des Moduls TWIN Lite
Pro als auch über echte ELRS-Module unterstützt (diese benötigen das unter
`scripts/elrs` installierte ELRS-Lua-Skript, bevor sie als Moduloption
erscheinen). Zwölf Kanäle; die wichtigsten Einstellungen sind **Packet
Rate** (Kompromiss zwischen Latenz und Reichweite), **Telemetry Ratio**
(wie oft Telemetrie gesendet wird, 1:1 bis 1:128), **Switch Mode**
(**Hybrid** — die meisten Aux-Kanäle auf 2–3 Positionen reduziert für
geringere Latenz — oder **Wide** — volle Auflösung mit 64–128 Stufen),
**Model Match** und **Tx Power** (10 mW–1000 mW, optional **Dynamic
Power**, um automatisch mit der Verbindungsqualität zu skalieren — setzt
aktivierte Telemetrie voraus).

**Fremdmodule** (derzeit Ghost, Multi-protocol, Crossfire, zusätzlich zu
ELRS) benötigen jeweils ein eigenes, vom Anwender installiertes Lua-Skript
— siehe die Hinweise zu `scripts/` in der
[Screenshot-Pipeline](../contributing/screenshot-pipeline.md) sowie den
Thread *Third-Party External Modules* auf rcgroups. Der Eintrag eines
Moduls erscheint erst dann im RF-Bildschirm, wenn dessen Skript installiert
ist. Das Multi-protocol-Modul (IRX4 Lite) lässt sich zusätzlich direkt aus
dem [Dateimanager](../system-setup/file-manager.md) heraus mit Firmware
flashen: Kopieren Sie die Firmware-Datei nach `Firmware/` und wählen Sie
dann **Flash external multimodule**.
