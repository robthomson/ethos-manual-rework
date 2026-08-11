---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Erste Einrichtung des Senders

Die einmalige Einrichtung, die vor der Programmierung eines Modells durchzuführen ist. Die
nachfolgenden [Tutorials](index.md) setzen alle voraus, dass dies zuerst erledigt wurde.

!!! note
    Diese Tutorials sind kein striktes Kochbuch — sie setzen grundlegendes
    RC-Vokabular und einen sicheren Umgang mit den Ethos-Menüs voraus. Falls
    hier etwas unklar ist, lesen Sie zunächst [Benutzeroberfläche &
    Navigation](../getting-started/user-interface-and-navigation.md).

## Schritt 1. Sender- und Flugakkus laden

Laden Sie den Senderakku gemäß den mit dem Sender gelieferten Hinweisen und
die Flugakkus mit einem für ihre Zellchemie geeigneten Ladegerät — bei
Lithium-Akkus ist besondere Sorgfalt geboten.

## Schritt 2. Hardware kalibrieren

Stellen Sie sicher, dass die [Hardware-Kalibrierung](../system-setup/hardware.md#analogs-calibration)
durchgeführt wurde (sie läuft beim ersten Start automatisch), damit der Sender
die genaue Mittelstellung und die Endpunkte jedes Knüppels, jedes Potentiometers
und jedes Schiebereglers kennt. Wiederholen Sie sie unter **System → Hardware**,
sobald ein Knüppel, ein Potentiometer oder ein Schieberegler ausgetauscht wird.

## Schritt 3. System-Setup des Senders vornehmen

Das [System-Setup](../system-setup/index.md) umfasst alles, was für alle
Modelle gleich ist — im Unterschied zu den modellspezifischen Einstellungen
im [Modell-Setup](../model-setup/index.md). Die meisten Standardwerte
sind für den Anfang in Ordnung, prüfen Sie jedoch:

- **[Datum & Uhrzeit](../system-setup/date-and-time.md)** — korrekt einstellen.
- **[Audio → Auswahl an
  Stimmen](../system-setup/general.md#audio-settings)** — Sprachansagen
  einrichten, einschließlich eventueller eigener Audiodateien.
- **[Knüppel Modus (Steuerknüppel)](../system-setup/controls.md)**:
  - **Knüppelmodus** — Mode 1 (Gas/Querruder rechts, Höhenruder/Seitenruder
    links) oder Mode 2 (Gas/Seitenruder links, Querruder/Höhenruder rechts —
    der Standard in Ethos).

    !!! warning
        Ist ein Modell für den einen Knüppelmodus konfiguriert, während
        der Sender auf den anderen eingestellt ist, kann ein Elektromotor in
        dem Moment anlaufen, in dem der Empfänger eingeschaltet wird.

  - **Kanalreihenfolge** — Ethos verwendet standardmäßig **AETR** (Querruder,
    Höhenruder, Gas, Seitenruder); die Spektrum/JR-Konvention lautet **TAER**,
    Futaba/Hitec verwendet **AETR**. Damit wird die Reihenfolge festgelegt, in der
    die Knüppeleingaben beim Anlegen eines neuen Modells zugewiesen werden —
    einzelne Modelle können später weiterhin individuell angepasst werden.

    !!! note "Stabilisierte FrSky-Empfänger"
        Diese erfordern zwingend **AETR**. Bei mehr als einer Ruderfläche pro
        Funktion (z. B. 2 Querruder) fasst der Assistent diese normalerweise
        zusammen (ergibt **AAETR**) — SRx-Empfänger erwarten jedoch stattdessen
        **AETRA**/**AETRAE**. Aktivieren Sie daher unter Knüppel die Option
        **[Erste vier Kanäle
        fest](../system-setup/controls.md#first-four-channels-fixed)**,
        damit die ersten vier Kanäle in jedem Fall in strikter
        AETR-Reihenfolge bleiben.

- **[TX-Akku](../system-setup/battery.md)** — stellen Sie **Hauptspannung**,
  **Niedrige Spannung** und **Anzeigebereich der Spannung** passend zum
  tatsächlich verwendeten Senderakku ein.
- **[Owner Registration ID](../model-setup/rf-system.md#owner-registration-id)**
  — wird von ACCESS-Empfängern verwendet und für Smart Share zwischen Sendern
  geteilt. Sie wird zwar im Modell-Setup eingestellt, wirkt in der
  Praxis aber wie eine systemweite Einstellung, da jedes neue Modell sie
  verwendet (bei Bedarf kann sie während der Registrierung weiterhin pro
  Empfänger geändert werden).

!!! note "Einheiten"
    Ethos besitzt keine globale Umschaltung zwischen metrischen und
    imperialen Einheiten — [die Einheiten der
    Telemetriesensoren](../model-setup/telemetry.md#editing-a-sensor) werden
    einzeln für jeden Sensor festgelegt.
