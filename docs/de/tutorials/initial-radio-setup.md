---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Erste Einrichtung des Senders

Die einmalige Einrichtung, die vor der Programmierung eines Modells durchzuführen ist. Die
nachfolgenden [Tutorials](index.md) setzen alle voraus, dass dies zuerst erledigt wurde.

!!! note
    Diese Tutorials sind kein striktes Kochbuch — sie setzen grundlegendes
    RC-Vokabular und einen sicheren Umgang mit den Ethos-Menüs voraus. Falls
    hier etwas unklar ist, sehen Sie sich zunächst [Benutzeroberfläche &
    Navigation](../getting-started/user-interface-and-navigation.md)
    an.

## Schritt 1. Sender- und Flugakkus laden

Laden Sie den Senderakku gemäß den mit dem Sender gelieferten Hinweisen und
die Flugakkus mit einem für ihre Zellchemie geeigneten Ladegerät — bei
Lithium-Akkus ist besondere Sorgfalt geboten.

## Schritt 2. Hardware kalibrieren

Stellen Sie sicher, dass die [Hardware-Kalibrierung](../system-setup/hardware.md#analogs-calibration)
durchgeführt wurde (sie läuft beim ersten Start automatisch), damit der Sender
die genaue Mittelstellung und die Endpunkte jedes Gimbals, Potentiometers und
Schiebereglers kennt. Wiederholen Sie sie unter **System → Hardware**, sobald
ein Gimbal, Potentiometer oder Schieberegler ausgetauscht wird.

## Schritt 3. Systemeinstellungen des Senders vornehmen

[Systemeinstellungen](../system-setup/index.md) umfassen alles, was für alle
Modelle gemeinsam gilt — im Unterschied zu den modellspezifischen Einstellungen
der [Modellkonfiguration](../model-setup/index.md). Die meisten Standardwerte
sind für den Anfang in Ordnung, prüfen Sie jedoch:

- **[Datum & Uhrzeit](../system-setup/date-and-time.md)** — korrekt einstellen.
- **[Audio → Auswahl der
  Stimmen](../system-setup/general.md#audio-settings)** — Sprachansagen
  einrichten, einschließlich eventueller eigener Audiodateien.
- **[Bedienelemente (Steuerknüppel)](../system-setup/controls.md)**:
  - **Steuerknüppelmodus** — Mode 1 (Gas/Querruder rechts, Höhenruder/Seitenruder
    links) oder Mode 2 (Gas/Seitenruder links, Querruder/Höhenruder rechts —
    der Standard in Ethos).

    !!! warning
        Ist ein Modell für den einen Steuerknüppelmodus konfiguriert, während
        der Sender auf den anderen eingestellt ist, kann ein Elektromotor in
        dem Moment anlaufen, in dem der Empfänger mit Strom versorgt wird.

  - **Kanalreihenfolge** — Ethos verwendet standardmäßig **AETR** (Querruder,
    Höhenruder, Gas, Seitenruder); die Spektrum/JR-Konvention lautet **TAER**,
    Futaba/Hitec verwendet **AETR**. Dies legt die Reihenfolge fest, in der
    Steuerknüppeleingaben beim Anlegen eines neuen Modells zugewiesen werden —
    Modelle können später weiterhin einzeln angepasst werden.

    !!! note "Stabilisierte FrSky-Empfänger"
        Diese erfordern zwingend **AETR**. Bei mehr als einer Ruderfläche pro
        Funktion (z. B. 2 Querruder) fasst der Assistent diese normalerweise
        zusammen (ergibt **AAETR**) — SRx-Empfänger erwarten jedoch stattdessen
        **AETRA**/**AETRAE**. Aktivieren Sie daher **[Erste vier Kanäle
        fest](../system-setup/controls.md#first-four-channels-fixed)**
        unter Steuerknüppel, damit die ersten vier Kanäle in jedem Fall in
        strikter AETR-Reihenfolge bleiben.

- **[Akku](../system-setup/battery.md)** — stellen Sie **Hauptspannung**,
  **Unterspannung** und **Anzeige-Spannungsbereich** passend zum tatsächlich
  verwendeten Senderakku ein.
- **[Owner Registration ID](../model-setup/rf-system.md#owner-registration-id)**
  — wird von ACCESS-Empfängern verwendet und für Smart Share zwischen Sendern
  geteilt. Sie wird zwar unter Modellkonfiguration eingestellt, wirkt in der
  Praxis aber wie eine systemweite Einstellung, da jedes neue Modell sie
  verwendet (sie kann bei Bedarf während der Registrierung weiterhin pro
  Empfänger geändert werden).

!!! note "Einheiten"
    Ethos besitzt keine globale Umschaltung zwischen metrischen und
    imperialen Einheiten — [die Einheiten von
    Telemetriesensoren](../model-setup/telemetry.md#editing-a-sensor) werden
    einzeln pro Sensor festgelegt.
