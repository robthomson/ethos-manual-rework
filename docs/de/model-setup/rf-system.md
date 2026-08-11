---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# HF-System

Konfiguriert das interne und/oder externe HF-Modul des Modells, die
Sender-ID, das Binden von Empfängern sowie die Empfängeroptionen. Hier
wird auch festgelegt, ob ein Modell das interne oder das externe Modul
verwendet — anders als bei fast allem anderen in den
[Systemeinstellungen](../system-setup/index.md) erfolgt die Auswahl der
HF-Hardware **pro Modell** und nicht senderweit.

!!! note "Screenshots ausstehend"
    Die Screenshots für diesen Abschnitt wurden noch nicht erstellt (siehe
    [Screenshot-Pipeline](../contributing/screenshot-pipeline.md)) — die
    nachfolgenden Inhalte sind korrekt, liegen aber vorerst nur als Text
    vor.

## Sender-ID des Eigentümers {: #owner-registration-id }

Ein 8-stelliger, eindeutiger Code (Groß- und Kleinbuchstaben sowie
Ziffern, keine Sonderzeichen), der bei der Registrierung zur
**Registrierungs-ID** eines Empfängers wird. Wird auf mehreren Sendern
*derselbe* Code eingetragen, lässt sich **Smart Share** zwischen ihnen
nutzen — richten Sie dies ein, bevor Sie das zu teilende Modell anlegen.
Kompatibel mit EdgeTX; nur teilweise kompatibel mit OpenTX.

## HF-Ausgabe deaktivieren

Halten Sie beim Einschalten `PAGE` gedrückt, um für diese Sitzung sowohl
die interne als auch die externe HF-Ausgabe zu deaktivieren (eine Warnung
bestätigt die Abschaltung). Der **Zustand** des Moduls selbst bleibt auf
EIN — ein normaler Neustart stellt den regulären Sendebetrieb wieder her.

## Betriebsarten des internen Moduls

Das interne HF-Modul von X18/X20/X20S/X20HD (TD-ISRM) arbeitet in einer
von drei Betriebsarten — das TD-ISRM Pro-Modul der X20 Pro/R/RS ist
vergleichbar, bietet zusätzlich jedoch LoRa- und Tandem-Dualband-Varianten.
Der Modus muss mit dem vom Empfänger unterstützten Typ übereinstimmen,
sonst wird das Modell nicht gebunden! Überprüfen Sie nach einem
Moduswechsel sorgfältig den Betrieb aller Kanäle und insbesondere das
Failsafe-Verhalten.

- **ACCESS** — die 2,4G- und 900M-HF-Pfade arbeiten zusammen mit einem
  Satz ACCESS-Steuerungen. Insgesamt können bis zu drei Empfänger
  registriert und gebunden sein, in beliebiger Kombination aus 2,4G
  (24 Kanäle) und 900M (16 Kanäle); die Telemetrie beider Bänder ist
  gleichzeitig aktiv, die Sensoren werden in der Telemetrie als 2.4G oder
  900M identifiziert. Eine Telemetriequelle namens **RX** liefert die
  Empfängernummer des aktiven Empfängers, der Telemetrie sendet.
- **ACCST D16** — ein einziger 2,4G-HF-Pfad, zur Verwendung mit den alten
  Empfängern der „X“-Serie.
- **TD-Modus** — ein Modus mit geringer Latenz und großer Reichweite, der
  die 2,4G- und 900M-HF-Verbindungen im Tandem mit Tandem-Empfängern
  nutzt; Tandem unterstützt 24 Kanäle auf beiden Bändern.

Die **Flex-Firmware** ergänzt eine zweite Spalte unter Typ, mit der sich
in jeder der drei genannten Betriebsarten zwischen FLEX915M (FCC-
Modulation, 915 MHz) und FLEX868M (europäische LBT-Modulation, 868 MHz)
umschalten lässt — die abgestrahlte Leistung und die Antennen müssen an
die gewählte Frequenz angepasst sein. Hinweis für EU-Nutzer: Die
Verwendung von 200 mW und 500 mW ist im 868-MHz-Band erlaubt. Wenn Sie
25 mW wählen, werden die Telemetriedaten über 868 MHz gesendet, während
bei 200 mW oder 500 mW die Telemetriedaten über 2.4G gesendet werden.

Die Wahl von Betriebsart und Kanalbereich wirkt sich auch auf die
übertragenen Aktualisierungsraten aus — unter ACCESS werden z. B.
8 Kanäle alle 7 ms, 16 Kanäle alle 14 ms und 24 Kanäle alle 21 ms
übertragen (im Wechsel in Blöcken zu 8), und mit Empfängern wie dem RS
(HF-Modul und Empfänger ab v2.1.7) steht bei Ch1-8 ein 4-ms-**Racing
Mode** zur Verfügung.

## Empfänger registrieren und binden (ACCESS) {: #registering-and-binding-a-receiver-access }

Das Binden eines ACCESS-Empfängers ist in zwei Phasen unterteilt — die
**Registrierung** muss für jedes Empfänger-Sender-Paar nur einmal
durchgeführt werden; das **Binden** kann danach drahtlos wiederholt
werden, ohne dass die Bindungstaste am Empfänger betätigt werden muss.

**Phase Eins — Registrierung**:

1. Tippen Sie auf **Registrieren** (entfällt vollständig, wenn der
   Empfänger bereits registriert ist).
2. Halten Sie die Bindungstaste des Empfängers gedrückt, schalten Sie den
   Empfänger ein und warten Sie, bis die roten und grünen LEDs aktiv
   werden. Die Meldung „Warten auf Empfänger…“ ändert sich in „Empfänger
   verbunden“, und das Feld Rx Name wird automatisch ausgefüllt.
3. Bestätigen bzw. bearbeiten Sie die **Registrierungs-ID** (voreingestellt
   ist die oben beschriebene Sender-ID des Eigentümers — übereinstimmende
   IDs auf mehreren Sendern sind die Voraussetzung für Smart Share), den
   **RX-Namen** sowie die **UID**. Die UID wird verwendet, um zwischen
   mehreren gleichzeitig in einem Modell verwendeten Empfängern zu
   unterscheiden — bei einem einzelnen Empfänger kann sie auf dem
   Standardwert 0 belassen werden; bei mehreren (z. B. einer je
   8-Kanal-Block) ist 0/1/2 üblich. Bitte beachten Sie, dass diese UID
   nicht vom Empfänger zurück gelesen werden kann, daher ist es ratsam,
   den Empfänger zu kennzeichnen.
4. Drücken Sie zum Abschluss auf **Registrieren**, bestätigen Sie die
   Meldung „Registrierung ok“ und schalten Sie den Empfänger anschließend
   aus — er ist nun registriert, muss aber noch gebunden werden.

**Phase Zwei — Binden**:

!!! warning
    Führen Sie den Bindevorgang nicht durch, wenn ein Elektromotor
    angeschlossen ist oder ein Verbrennungsmotor läuft.

1. Schalten Sie den Empfänger aus; bestätigen Sie, dass die richtige
   Modul-Betriebsart aktiv ist.
2. Tippen Sie auf **EMPF.1** (oder 2/3) → **Binden**. Alle paar Sekunden
   ertönt ein Sprachsignal mit der Ansage „Binden“, um zu bestätigen, dass
   Sie sich im Bindungsmodus befinden.
3. Schalten Sie den Empfänger ein, **ohne** die F/S-Bindungstaste zu
   drücken, und wählen Sie ihn aus der erscheinenden Liste „Empf./Laufw.
   auswählen“ aus.
4. Bestätigen Sie die Meldung, dass die Bindung erfolgreich war. Schalten
   Sie Sender und Empfänger aus und wieder ein — wenn die grüne LED am
   Empfänger leuchtet und die rote LED aus ist, ist der Empfänger mit dem
   Sender verbunden. Die Bindung muss nicht wiederholt werden, es sei
   denn, eines der beiden Module wird ausgetauscht.
5. Wiederholen Sie den Vorgang für Empfänger 2 und 3, falls zutreffend.

## Empfängeroptionen

Tippen Sie bei eingeschaltetem Empfänger auf dessen RX-Schaltfläche, um
folgende Funktionen aufzurufen:

- **Optionen** — **Telemetrie** (kann für diesen Empfänger deaktiviert
  werden), **Reduzierte Telemetrieleistung 25mW** (statt der
  normalerweise 100 mW — möglicherweise erforderlich, wenn z. B. Servos
  durch HF-Störungen in ihrer Nähe gestört werden), **HS-PWM Rate** (7 ms
  Servo-Aktualisierungsrate statt 18 ms — stellen Sie sicher, dass Ihre
  Servos diese Aktualisierungsrate verarbeiten können), **Telem. Port**
  (S.Port/F.Port/FBUS), **SBUS** (16- oder 24-Kanal-Modus — alle
  angeschlossenen SBUS-Geräte müssen den SBUS-24-Modus unterstützen,
  bevor Sie ihn aktivieren) und **Kanal-Mapping**, um Kanäle den
  Empfängerpins neu zuzuordnen.
- **teilen** — überträgt den Empfänger auf einen anderen ACCESS-Sender
  mit einer *anderen* Sender-ID. Tippen Sie am Quellsender auf „teilen“
  (die grüne LED des Empfängers schaltet sich aus); am Zielsender wählen
  Sie ganz normal BIND — der „teilen“-Prozess überspringt den
  Registrierungsschritt, da die Sender-ID automatisch übertragen wird.
  Drücken Sie am Quellsender die Taste EXIT, um den „teilen“-Prozess zu
  beenden; erneutes Binden holt den Empfänger zurück. (Nicht erforderlich,
  wenn alle Ihre Sender dieselbe Sender-ID verwenden — binden Sie dann
  einfach direkt an dem Sender, der den Empfänger steuern soll.)
- **Bindung löschen** — räumt nach einem „teilen“ auf und stellt Ihre
  eigene Bindung wieder her; schalten Sie den Empfänger anschließend ein,
  und er wird an Ihren Sender gebunden.
- **Werkseinstellungen** — setzt den Empfänger auf die Werkseinstellungen
  zurück und löscht die UID. Der Empfänger ist nicht mehr im Sender
  registriert.

Tippen Sie bei **ausgeschaltetem** Empfänger auf dieselbe RX-Schaltfläche,
so stehen **Optionen** (der Sender versucht, eine Verbindung herzustellen,
und wartet auf den Empfänger), **BIND** (z. B. um ein Modell, das an einen
anderen Sender gebunden war, neu zu binden) und **Name löschen**
(entspricht „Bindung löschen“) zur Verfügung.

## Redundante Empfänger {: #redundant-receivers }

Ein zweiter Empfänger kann an einen unbenutzten Steckplatz gebunden
werden, um bei Empfangsproblemen Redundanz zu gewährleisten — ein 2.4G-
oder ein 900M-Empfänger kann jeweils als Backup dienen. Die
FrSky-Redundanz für die Steuerung wird immer **pro Frame** ausgewertet,
wobei der beste Frame gewählt wird (aktive/aktive Ausfallsicherung),
sodass die Steuerung nach Bedarf bei jedem Frame umschalten kann.

1. Verbinden Sie den SBUS-Out-Anschluss des redundanten Empfängers mit
   dem SBUS IN-Anschluss des Hauptempfängers.
2. Aktivieren Sie das entsprechende interne HF-Modul (z. B. 900M) und
   konfigurieren Sie die Antennen- und HF-Leistungsoptionen.
3. Registrieren Sie den neuen Empfänger (falls noch nicht geschehen) und
   binden Sie ihn wie oben beschrieben an den freien Steckplatz.
4. Stellen Sie sicher, dass die grüne LED am redundanten Empfänger
   leuchtet — er wird nun als redundanter Empfänger aufgelistet.

## Failsafe {: #failsafe }

Die Failsafe-Daten werden etwa alle 10 Sekunden vom Sender gesendet; bei
TD-, TW-, AP- und AP Plus-Empfängern werden die Failsafe-Daten zusätzlich
im Empfänger gespeichert, was bedeutet, dass die Failsafe-Einstellungen
sofort verfügbar sind, wenn der Empfänger aus irgendeinem Grund neu
gestartet wird. Beachten Sie, dass die Failsafe-Funktion nach einem
Upgrade von Empfängern mit dieser Funktion zurückgesetzt und überprüft
werden muss.

- **Position halten** — die zuletzt empfangenen Positionen werden
  beibehalten.
- **Benutzer** — für jeden Kanal separat: **nicht eingestellt**,
  **Position halten**, **Benutzer** (ein fester Wert — tippen Sie auf das
  Symbol mit dem Pfeil, um den aktuellen Wert des Kanals zu übernehmen,
  oder geben Sie ihn direkt ein) oder **kein Impuls**.
- **kein Impuls** — schaltet die Impulse aus (zur Verwendung mit
  Flugcontrollern, die bei Signalverlust zum Heimat-GPS-Ort zurückkehren).
- **Empfänger** — bei Empfängern der Serie X oder höher können Sie damit
  die Failsafe-Funktion im Empfänger einstellen.

!!! warning
    Testen Sie die gewählten Failsafe-Einstellungen unbedingt sorgfältig,
    bevor Sie sich darauf verlassen.

## Reichweitentest {: #range-check }

Eine Reichweitenkontrolle sollte auf dem Flugplatz durchgeführt werden,
wenn das Modell flugbereit ist — vor jeder Flugsession mit einem neuen
oder geänderten Setup. Wenn die Reichweitenprüfung durch Auswahl von
**Reichweitentest** aktiviert wird, wird die Sendeleistung reduziert (alle
paar Sekunden ertönt die Sprachansage „Reichweitentest“, um zu bestätigen,
dass Sie sich in diesem Modus befinden); ein Popup-Fenster zeigt die VFR%-
und RSSI-Werte an, um das Verhalten der Empfangsqualität zu bewerten. Der
FrSky-Reichweitentest-Pegel liegt rund −10 dB gegenüber dem Normalpegel
von +20 dB. Unter idealen Bedingungen, bei denen sich sowohl der Sender
als auch der Empfänger 1 m über dem Boden befinden, sollten Sie frühestens
in einem Abstand von etwa 30 m einen kritischen Alarm erhalten — eine
geringere Distanz kann unter normalen Bedingungen auf ein Problem
hindeuten.

Bei mehreren gebundenen Empfängern werden im Reichweitentestmodus
Reichweitendaten für jeweils einen aktiven Empfänger pro Band geliefert —
wenn Sie diesen Empfänger ausschalten, wird der nächste Empfänger zum
aktiven Telemetrieempfänger (in der Priorität 0, 1 und dann 2, angezeigt
vom **RX**-Sensor), sodass jeder der Empfänger der Reihe nach auf seine
Reichweite überprüft werden kann.

## Externe HF-Module und Module von Drittanbietern

Externe FrSky-Module (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
folgen demselben Ablauf aus Registrierung und Binden wie das interne
Modul, mit protokollspezifischen Kanalzahlen, HF-Leistungen und
Antennenanforderungen — genaue Werte entnehmen Sie bitte den
entsprechenden Modulhandbüchern.

**ELRS** (ExpressLRS) wird sowohl über den ELRS-Modus des TWIN Lite
Pro-Moduls als auch über echte ELRS-Module unterstützt (bei diesen müssen
Sie das ELRS-Lua-Skript in `scripts/elrs` installieren, bevor Sie ELRS als
Moduloption erhalten). Zwölf Kanäle werden unterstützt; die wichtigsten
Einstellungen sind **Packet Rate** (Kompromiss zwischen Reichweite und
Latenzzeit), **Telemetrie-Verhältnis** (bestimmt, wie oft Telemetriedaten
gesendet werden, 1:1 bis 1:128), **Switch Mode** (**Hybrid** — die meisten
Kanäle haben nur 2 oder 3 Positionen, um die Latenz zu verringern — oder
**Wide** — volle Auflösung mit 64 bis 128 Stufen), **Modell Match** und
**TX-Leistung** (10 mW bis 1000 mW, optional **Dynamische Leistung**, um
die Ausgangsleistung automatisch in Abhängigkeit von der
Verbindungsqualität anzupassen — dazu muss die Telemetrie aktiviert sein).

**Module von Drittanbietern** (derzeit Ghost, Multi-protocol und
Crossfire, zusätzlich zu ELRS) benötigen jeweils ein eigenes, vom Benutzer
installiertes Lua-Skript — siehe die Hinweise zu `scripts/` in der
[Screenshot-Pipeline](../contributing/screenshot-pipeline.md) sowie den
Thread *Third-Party External Modules* auf rcgroups. Die Auswahl für ein
Modul erscheint erst dann auf dem HF-Bildschirm, nachdem das Lua-Skript
installiert wurde. Das Multi-protocol-Modul (IRX4 Lite) lässt sich
zusätzlich direkt aus dem
[Dateimanager](../system-setup/file-manager.md) heraus flashen: Kopieren
Sie die Firmware-Datei in den Ordner `Firmware/` und wählen Sie dann
**Flash externes Multimodul**.
