# Ethos Web Simulator

![](../assets/Pictures/1000000100000ECE0000087EC6EED3C0.png)

Der Ethos-Websimulator basiert auf WebAssembly (kurz Wasm) – einer portablen Lösung, die den Einsatz im Web ermöglicht. Das bedeutet, dass er direkt im Browser läuft und keine Installation auf dem PC erfordert. Als Browser wird Chrome empfohlen.

Mit dem Ethos-Web-Simulator können Sie die Funktionen des Senders erkunden sowie Funktionalitäten oder geplante Modellerweiterungen testen, ohne den eigentlichen Sender zur Hand zu haben. Zudem können Sie ganz einfach neue Versionen ausprobieren, bevor Sie Ihren Sender aktualisieren.

Der Websimulator ist unter folgender Adresse zu finden: [https://ethos-simulator.frsky-rc.com/](https://ethos-simulator.frsky-rc.com/)

Die standardmäßigen Voreinstellungen sind das Release 26.1.0-RC6 (zum Zeitpunkt der Erstellung dieses Textes), der Sender X20 Pro und das FCC-Protokoll. Wählen Sie zunächst die Anzeigesprache aus.

![](../assets/Pictures/10000001000003E8000001E763388F1A.png)

Beim ersten Laden werden keine gültigen Modelldaten gefunden; daher wird der Wizard für neue Modelle gestartet.

![](../assets/Pictures/10000001000003E7000001E41CF0251F.png)

Schließen Sie den Wizard ab, um ein grundlegendes Testmodell zu konfigurieren.

Wenn die Standard-Release-Version und der Sender nicht den gewünschten Einstellungen entsprechen, wählen Sie die gewünschte Ethos-Release-Version, den zu simulierenden Sendertyp sowie das HF-Protokoll aus.

![](../assets/Pictures/100000010000005D000000540670607D.png)Klicken Sie auf das Panels-Symbol in der oberen Menüleiste und wählen Sie die Konsole aus.

![](../assets/Pictures/10000001000003ED000001E2E24C04FD.png)

Die Konsole erscheint neben dem Anzeigebereich.

![](../assets/Pictures/10000001000007760000039E77FB9A75.png)

Klicken Sie auf die Titelleiste der Konsole und ziehen Sie sie nach unten. Bewegen Sie die Maus, bis die Konsole den unteren linken Quadranten einnimmt.

Die Konsole ist nützlich, um die Startsequenz des Simulators zu bestätigen sowie Ereignisse und Fehlermeldungen zu überwachen.

![](../assets/Pictures/10000001000003E7000001E3DD3D257B.png)

Klicken Sie erneut auf das Symbol „Bereiche“ und wiederholen Sie den Vorgang für den Bereich „Telemetrie“, indem Sie ihn in den unteren rechten Quadranten verschieben.

![](../assets/Pictures/10000001000003E8000001E44C095D79.png)

Klicken Sie im Telemetrie-Bereich wiederholt auf „Neuen Sensor hinzufügen“ und fügen Sie die Sensoren hinzu, auf die Sie in Ihren Simulationen zugreifen möchten.

Um Ihre Sensoren für zukünftige Sitzungen zu speichern, klicken Sie auf das Symbol ![](../assets/Pictures/100000010000005400000051110B240F.png) und wählen Sie „Telemetrieeinstellungen speichern“. Die Telemetrieeinstellungen werden in einer Datei namens „telemetry.json“ in Ihrem Download-Ordner gespeichert. Verschieben Sie diese Datei an einen geeigneten Speicherort. Klicken Sie in nachfolgenden Simulatorsitzungen auf das Symbol „Hochladen“ und wählen Sie „JSON-Telemetriedatei hochladen“. Navigieren Sie anschließend zu Ihrer gespeicherten Datei „telemetry.json“.

Sie können nun mit der Simulation beginnen. Der Browser merkt sich Ihre Panel-Anordnung, sodass Sie diese nicht immer wieder neu einrichten müssen.

### Empfohlene Konfiguration

Am besten ist es, die Konfiguration Ihres Senders im Simulator nachzubilden. Dadurch stehen Ihnen dieselben Funktionen wie am Sender zur Verfügung, sodass Sie Verbesserungen an Ihren Modellen einfach testen können, ohne Ihre Flug- oder Modellbauumgebung zu beeinträchtigen, bis alles wie geplant funktioniert.

Die empfohlenen Einrichtungsschritte sind:

1. Erstellen Sie ein Backup Ihres Radios mithilfe der [Sicherungs- und Wiederherstellungsfunktion](operation.md) der Suite.

2. Wählen Sie im Menü „Upload“ die Option „Upload a radio backup“ aus und navigieren Sie zu Ihrer gespeicherten Backup-Datei. (Siehe die untenstehenden Menüs.)

![](../assets/Pictures/10000001000003E6000001E3073FE756.png)

3. Es sollte mit dem Modell beginnen, das auf Ihrem Sender aktiv war, als Sie das Backup erstellt haben. In diesem Beispiel war ein Thermy XT 3.3-Segelflugzeug das aktive Modell.

In Ihrer gewohnten Senderumgebung können Sie nun ein völlig neues Modell erstellen und testen – etwa indem Sie auf einer Ihrer Vorlagen aufbauen oder ein bestehendes Modell klonen und anpassen. Diese Vorgehensweisen maximieren die Wiederverwendbarkeit, ohne dass Sie ein Modell von Grund auf neu programmieren müssen. Sobald das Modell fertiggestellt ist, nutzen Sie die Option „Modelldatei herunterladen“, um die .bin-Datei in Ihren Download-Ordner zu speichern. Kopieren Sie diese anschließend auf Ihren Sender.

### Simulator-Taskleiste

Die Taskleiste des Simulators verfügt über die folgenden Bedienelemente:

![](../assets/Pictures/10000001000003680000004707491117.png)

![](../assets/Pictures/100000010000003A0000003666C3C7BD.png)	Screenshot (werden im Ordner Download gespeichert)

![](../assets/Pictures/10000001000000340000003483679B57.png)	Aufnahme starten (zeichnet ein Makro auf)

![](../assets/Pictures/100000010000003500000034AEFCA677.png)	Bereiche (listet Bereiche auf, die noch nicht geöffnet wurden)

![](../assets/Pictures/1000000100000032000000354EFA6D7A.png)	Hochladen… (siehe Menü unten)

![](../assets/Pictures/1000000100000033000000366AC34E19.png)	Download ... (siehe Menü unten)

![](../assets/Pictures/100000010000003600000035C95472AF.png)	Audio ein/aus

![](../assets/Pictures/1000000100000032000000365BA45D87.png)	Simulator neu starten

![](../assets/Pictures/100000010000003600000035FFB1D3C8.png)	Dokumentation (enthält einen Link zum aktuellen Handbuch)

![](../assets/Pictures/100000010000003200000035D1E633FE.png)	Hintergrundmodus hell/dunkel

##### Upload-Menü

![](../assets/Pictures/10000001000000360000002D2C104C73.png)	Laden Sie eine Modelldatei (.bin) in den Simulator.

![](../assets/Pictures/10000001000000390000002C6F32ABA7.png)	Laden Sie ein Sender-Backup (.bin) in den Simulator

![](../assets/Pictures/100000010000003300000033269A6153.png)	Laden Sie ein Audiopaket (.zip) in den Simulator.

![](../assets/Pictures/100000010000003900000036C03A3D20.png)	Laden Sie ein Lua-Plugin (.zip) in den Simulator.

![](../assets/Pictures/10000001000000340000002F288030D0.png)	Laden Sie eine CSV-Übersetzungsdatei (.csv) in den Simulator.

![](../assets/Pictures/10000001000000350000002A143579D1.png)	Laden Sie eine JSON-Telemetriedatei (.json) in den Simulator.

![](../assets/Pictures/100000010000002A00000027369727BA.png)	Makro starten (.zip)

##### Download-Menü

![](../assets/Pictures/10000001000000300000002E352FCCAB.png)	Speichern Sie die aktuelle Modelldatei (.bin).

![](../assets/Pictures/100000010000003500000035D957DFFB.png)	Aktuelles Modell bearbeiten

![](../assets/Pictures/100000010000003500000035D957DFFB.png)	Bearbeiten Sie die aktuelle Modelldatei (JSON)

![](../assets/Pictures/1000000100000039000000328FCEB87D.png)	Screenshot speichern (Zielordner auswählen, als .png speichern)

![](../assets/Pictures/10000001000000380000002DE9810693.png)	Sender-Backup speichern (.zip)

![](../assets/Pictures/10000001000000350000002C51A893DF.png)	Telemetrieeinstellungen speichern (.json)

##### Bedienelementefeld

![](../assets/Pictures/10000001000003BC000001B2AF3D4DEC.png)

Das Bedienelementefeld „Bedienelemente“ bildet die Bedienelemente des gewählten Senders nach.

###### Steuerknüppel

Die Steuerknüppel lassen sich durch Ziehen mit der Maus bedienen. Beim Bedienen ist es hilfreich, die Bewegung der Knüppel einzuschränken oder zu begrenzen.

![](../assets/icon-sim-center.png)	Zentriert den Steuerknüppel automatisch auf einer oder beiden Achsen.

![](../assets/icon-sim-vertical.png)	Beschränkt den Steuerknüppel auf eine rein vertikale Bewegung.

![](../assets/icon-sim-horizontal.png)	Beschränkt den Steuerknüppel auf eine rein horizontale Bewegung.

###### Tastschalter und Taster

![](../assets/icon-sim-locked.png)	Durch das Anklicken dieses Symbols wird es markiert und der Taster wird in einen Taster mit Rastfunktion umgewandelt. Diese Funktion kann bei der Fehlersuche sehr hilfreich sein. Durch erneutes Anklicken dieses Symbols wird die Umwandlung rückgängig gemacht.

**Beachte:** auch nach einen Neustart bleibt die Umwandlung in einen Taster mit Rastfunktion erhalten.
