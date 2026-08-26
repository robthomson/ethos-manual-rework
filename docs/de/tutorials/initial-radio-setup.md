# Beispiel für die Ersteinrichtung eines Senders

In diesem einführenden Abschnitt werden die ersten Schritte zur Einrichtung des Senders selbst beschrieben, bevor spezifische Modelle programmiert werden. Danach können die Programmierbeispiele in den folgenden Abschnitten befolgt werden.

Hinweis: Diese Beispiele sind nicht als „Kochbuch“ zu verstehen. Sie setzen voraus, dass der Benutzer ein grundlegendes Verständnis des Vokabulars der Fernsteuerungsmodelle hat und mit der Navigation in der Ethos-Menüstruktur vertraut ist. Sollten Sie zu irgendeinem Zeitpunkt verwirrt sein, lesen Sie bitte zur Auffrischung frühere Abschnitte dieses Handbuchs. Lesen Sie insbesondere den [Abschnitt Benutzeroberfläche und Navigation](../getting-started/user-interface-and-navigation.md), um sich mit der Benutzeroberfläche des Senders vertraut zu machen, damit Sie die gewünschte Einrichtungsseite leicht finden können.

## Schritt 1. Laden Sie den Sender- und die Flugakkus auf.

Bitte laden Sie den Akku des Senders anhand der mit dem Sender gelieferten Anleitung. Laden Sie auch die zu verwendenden Flugakkus mit einem für den Akkutyp/die Akkus geeigneten Ladegerät und beachten Sie dabei alle Sicherheitsvorkehrungen, insbesondere bei der Verwendung von Lithium-Akkus.

## Schritt 2. Kalibrieren Sie die Hardware.

Vergewissern Sie sich, dass Sie die Hardware-Kalibrierung bei der ersten Inbetriebnahme des Senders durchgeführt haben, um zu bestätigen, dass der Sender genau weiß, wo sich die Mittelpunkte und Grenzwerte jedes Steuerknüppels, Potis und Schiebers befinden. Sie können die Kalibrierung erneut durchführen, indem Sie die Anweisungen im Abschnitt System \\ Hardware \\ [Kalibrierung](../system-setup/hardware.md) dieses Handbuchs befolgen.

## Schritt 3. Führen Sie die Einrichtung des Sender-Systems durch.

Mit dem Sender-System-Setup werden die Teile der Hardware des Senders konfiguriert, die für alle Modelle gleich sind. Es unterscheidet sich von den „Modell-Setup“-Funktionen, die die modellspezifischen Einstellungen für jedes Modell konfigurieren.

Bitte lesen Sie den Abschnitt System-Setup, um sich mit allen Einstellungen in diesem Abschnitt vertraut zu machen.

Viele Einstellungen können (zumindest anfangs) auf den Standardwerten belassen werden, aber die folgenden sollten überprüft werden:

### Datum und Uhrzeit

Stellen Sie die aktuelle Uhrzeit und das Datum ein.

### Audio

Richten Sie den Bereich Stimmen für die Radio-Sprachansagen ein, einschließlich Ihrer eigenen Audiodateien. Siehe den Abschnitt [General / Audio / Auswahl](../system-setup/general.md) der Stimmen.

### Steuerknüppel

#### Knüppel Mode

Wählen Sie Ihren bevorzugten Steuerknüppelmodus. In Modus 1 befinden sich Gas und Querruder auf dem rechten Steuerknüppel und Höhen- und Seitenruder auf dem linken. Im Modus 2 befinden sich Gas und Seitenruder auf dem linken Steuerknüppel und Quer- und Höhenruder auf dem rechten.

Hinweis: Modus 2 ist die Standardeinstellung.

**Achtung!**  Wenn ein Modell für Modus 2 und der Sender für Modus 1 konfiguriert ist, ist es möglich, dass der Motor bei Elektromodellen startet, wenn der Empfänger eingeschaltet wird.

#### Reihenfolge der Kanäle

Die Standard-Kanalreihenfolge für Ethos ist AETR (d.h. Querruder, Höhenruder, Gas, Seitenruder). Sie können es vorziehen, die Standard-Kanalreihenfolge so einzustellen, wie Sie es gewohnt sind. TAER ist die Standardeinstellung für Spektrum/JR, und AETR ist die Standardeinstellung für Futaba/Hitec. Diese Einstellung legt die Reihenfolge fest, in der die vier Knüppeleingänge beim Erstellen eines neuen Modells eingefügt werden. Sie können natürlich später geändert werden.

##### Stabilisierte FrSky-Empfänger

Beachten Sie, dass AETR die erforderliche Reihenfolge ist, wenn Sie einen der stabilisierten FrSky-Empfänger verwenden möchten. Bei Modellen mit mehr als einer Fläche für Querruder, Höhenruder, Seitenruder, Wölbklappen usw. fasst der Modell-Wizard diese Flächen normalerweise zusammen, so dass Sie z. B. AAETR erhalten, wenn Sie 2 Querruderkanäle verwenden.

Die SRx-Empfänger erwarten eine Kanalreihenfolge von AETRA oder AETRAE, so dass der Wizard (in System /Knüppel-Mode angewiesen werden kann, die 'ersten vier Kanäle fest' zu behalten.

### TX-Akku&Sp.Bat.

Überprüfen Sie die technischen Daten Ihrer Senderbatterie und konfigurieren Sie 'Akkuspannung', Warnschwelle 'Akkuspannung' und 'Anzeigespannungsbereich' wie im Abschnitt [System / Batterie ](../system-setup/battery.md)in diesem Handbuch beschrieben.

### Sender-ID des Eigentümers

Die 'Eigentümer-Registrierungs-ID' wird bei ACCESS-Systemen verwendet. Diese ID wird bei der Registrierung eines Empfängers zur „Registrierungs-ID“. Geben Sie denselben Code in das Feld für die Sender-ID Ihrer anderen Sender ein, mit denen Sie die SmartShareTM -Funktion nutzen möchten. Beachten Sie den Abschnitt [Modell-Setup / HF-System](../model-setup/rf-system.md) in diesem Handbuch (obwohl sie im Abschnitt Modell-Setup konfiguriert wird, wird die „Sender-ID“ für jedes neue Modell verwendet und kann als Systemeinstellung betrachtet werden. Bitte beachten Sie auch, dass die Sender-ID für einen bestimmten Empfänger während des Registrierungsprozesses geändert werden kann).

### Einheiten

Bitte beachten Sie, dass in Ethos die Telemetrieeinheiten für jeden Sensor einzeln konfiguriert werden. Es gibt keine globale metrische oder imperiale Einstellung.
