---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Geräte

![Geräte](../assets/system-devices.png)

Im Menü heißt dieser Bereich **Geräte Konfig.** — Werkzeuge zur
Konfiguration von Peripheriegeräten, die über S.Port/FBUS angeschlossen
sind: Sensoren, Empfänger, die „Gas Suite", Servos, VTX und ESC.
**DIY-Sensoren** erscheint automatisch, sobald ein DIY-Sensor erkannt wird.
Ausführliche Angaben entnehmen Sie bitte dem Handbuch des jeweiligen
Geräts; diese Seite behandelt das, was allen gemeinsam ist.

!!! note
    Dies hat nichts mit der Auswahl zu tun, über welches HF-Modul (intern
    oder extern) ein *Modell* sendet — das ist eine modellspezifische
    Einstellung und wird unter
    [HF-System](../model-setup/rf-system.md) behandelt.

Die Geräte Konfig. ist erweiterbar: Sowohl Anwender als auch FrSky können
hier über Lua weitere Seiten hinzufügen.

## Sensor-IDs neu zuweisen

Auf den Seiten der Geräte Konfig. können Sie die **physikalische ID** und
die **Anwendungs-ID** eines S.Port-Geräts direkt ändern. Wenn Sie mehrere
Geräte mit derselben Funktion besitzen, schließen Sie diese **einzeln
nacheinander** an: Suchen Sie jedes Gerät über
[Telemetrie → Neue Sensoren suchen](../model-setup/telemetry.md), ändern Sie
hier in der Geräte Konfig. dessen physikalische ID und Anwendungs-ID, und
führen Sie anschließend die Sensorsuche unter der neuen ID erneut durch.

## Beispiel Empfänger

![Modulauswahl](../assets/system-devices-module-choice.png)

Stabilisierte FrSky-Empfänger können hier konfiguriert werden, sobald das
zugehörige Lua-Einrichtungsskript installiert ist (ein Klick in der
Lua-Bibliothek von Ethos Suite). Je nach Empfängergeneration gibt es zwei
Konfigurationswege:

- **Stabilizer config** — neuere Empfänger mit „Advanced stabilization"
  (Verstärkungsregelung auf Kanal 13). Es stehen zwei unabhängige
  Stabilisierungsgruppen zur Verfügung: Gruppe 1 umfasst die Kanäle 1–6,
  Gruppe 2 die Kanäle 7–11 — schalten Sie Gruppe 2 ab, wenn Sie die Pins
  7–11 nicht zur Stabilisierung verwenden. Eine 6-Achsen-Kalibrierung ist
  integriert und muss bei einem neuen Empfänger einmalig durchgeführt
  werden, ebenso nach jedem Firmware-Update auf v3.0.x (im Anschluss an
  einen Werksreset). Unter der Kalibrierung jeder Gruppe wurde der frühere
  Schritt „Selbsttest" durch die unabhängige Kalibrierung von Fluglage,
  Kanalmitte und Kanalendpunkten ersetzt; jeder Kanal kann einzeln
  aktiviert bzw. deaktiviert werden. Konfigurationen (nicht die
  Kalibrierdaten) können auf einem PC gespeichert und von dort
  wiederhergestellt werden.
- **SxR** — ältere Empfänger, einschließlich Altgeräten sowie Archer und
  Archer Pro, außerdem Empfänger wie der SR10 Pro, die (trotz der
  Bezeichnung „SRx") die Verstärkung auf Kanal 9 statt auf Kanal 13 haben.

  ![Aktuelles Gerät](../assets/system-devices-current.png)

!!! warning "Nach dem Update auf die Empfänger-Firmware v3.0.x"
    Führen Sie ein Zurücksetzen auf Werkseinstellungen durch (zu finden
    unter den Empfänger-Optionen im HF-System), binden Sie anschließend neu
    und konfigurieren Sie den Empfänger vollständig neu — insbesondere die
    Stab-Funktionen und die 6-Achsen-Kalibrierung. Dies ist wegen der neuen
    Funktion zur Speicherung der Failsafe-Daten in v3.0.x erforderlich;
    prüfen Sie die Failsafe-Funktion danach sorgfältig.

FrSky North America veröffentlicht eine ausführliche Anleitung zur
Einrichtung stabilisierter Empfänger; außerdem gibt es ein Video von FrSky
Team Pilot Juan Sanchez Garcia, das dieselben Inhalte Schritt für Schritt
behandelt.

## Konfiguration über den S.Port-Anschluss des Senders

S.Port- und FBUS-Geräte lassen sich auch direkt über den S.Port-Anschluss
an der Oberseite des Senders konfigurieren, ohne den Umweg über einen
gebundenen Empfänger.

1. Stecken Sie das Gerät in den S.Port-Anschluss an der Oberseite des
   Senders. Das weiße oder gelbe Kabel wird an der Seite mit der
   Einkerbung angeschlossen.
2. Gehen Sie zu **System / Geräte Konfig.**, blättern Sie zu Ihrem Gerät
   (zum Beispiel einem Stromsensor FAS40 ADV) und drücken Sie `ENT`.
3. Sobald sich die Konfigurationsseite öffnet, klicken Sie auf **Modul**
   und wählen Sie **S.Port Anschluss**.
4. Nehmen Sie Ihre Konfigurationsänderungen vor und denken Sie daran, dass
   sowohl die physikalische ID als auch die Anwendungs-ID eindeutig sein
   müssen. Scrollen Sie dann weiter nach unten und tippen Sie auf die
   Schaltfläche **Speichern int. Speicher**.

Das gilt sowohl für FBUS-Geräte (siehe auch [Wie konfiguriere ich ein
FBUS-System](../how-to/fbus-setup.md)) als auch für einfache S.Port-Geräte
wie ein Variometer.
