---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Ein FBUS-System konfigurieren

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (früher
F.Port2) legt Steuerung und Telemetrie auf eine Leitung, sodass sich mehrere
FBUS-Geräte eine einzige, in Reihe geschaltete Verbindung mit vollständiger
drahtloser Konfiguration teilen können. Diese Anleitung verkabelt zwei
Xact-Servos an den Querruderkanälen (1 und 5) des [Basis-Beispiels für
Flächenmodelle](../tutorials/basic-fixed-wing.md).

!!! note "Screenshots ausstehend"
    Für diese Seite gibt es noch keine Simulator-Screenshots — siehe [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## 1. Aktuelle Firmware herunterladen

FBUS benötigt aktuelle Firmware sowohl auf dem Empfänger als auch auf den
Geräten — Xact-Servos etwa benötigen v2.0.1 oder neuer. Die entsprechenden
Updates finden Sie auf der
[FrSky-Downloadseite](https://www.frsky-rc.com/download/).

## 2. Firmware flashen

Kopieren Sie die Firmware-Dateien in den Ordner `Firmware/` auf der SD card/eMMC.
Stecken Sie im [Dateimanager](../system-setup/file-manager.md) das Servo an den
S.Port-Anschluss des Senders (weiße/gelbe Ader zur Kerbe hin), wählen Sie die
Firmware-Datei aus und wählen Sie **Flash External Device**.

## 3 / 5. Physical IDs konfigurieren

Beide Servos verwenden standardmäßig die Physical ID `0C` hex / Application ID
`6800` hex — auf dem gemeinsamen Bus kommt es damit zu einem Konflikt, sofern
nicht eines geändert wird. Je nach Empfängertyp gibt es zwei Wege:

**Über den S.Port-Anschluss des Senders** (beliebiger Empfänger):

1. Servo 1 anstecken, **Device Config → XAct** aufrufen und **Module** auf
   **S.Port connector** setzen. Physical ID `0C`/Application ID `6800` sowie
   Kanal `CH1` auf den Standardwerten belassen, dann **Save to flash**.
2. Stattdessen Servo 2 anstecken, gleiches Menü. **Physical ID** auf `0D` hex
   und **Application ID** auf `6801` hex ändern (welche Plätze frei sind, zeigt
   die [Physical-ID-Tabelle](../model-setup/telemetry.md#how-frsky-telemetry-works)),
   **Channel** auf `CH5` setzen, **Save to flash**.

**Direkt über den Empfänger** (z. B. TD-R18 Tandem, beide Servos gleichzeitig
angeschlossen — siehe [Schritt 4](#4-configure-the-receiver-for-fbus)):

1. Nur mit angeschlossenem Servo 1 (z. B. an Empfänger-Pin1) **Device Config →
   XAct** aufrufen, **Module** → **Internal module**. Standardwerte bestätigen
   (`0C`/`6800`/`CH1`), **Save to flash**.
2. Nur mit angeschlossenem Servo 2 (Pin5) das gleiche Menü aufrufen (Device
   Config kommuniziert immer nur mit einem Servo) — auf `0D`/`6801`/`CH5`
   ändern, **Save to flash**. Anschließend Device Config erneut aufrufen, um
   zu prüfen, ob die Änderung übernommen wurde.

## 4. Den Empfänger für FBUS konfigurieren {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [RF System](../model-setup/rf-system.md) → Schaltfläche des
Empfängers → **Options** → **Telemetry Port** auf **FBUS** setzen. Xact-Servos
werden dann in Reihe an diesem Port angeschlossen; da jedes Servo nur einen
Anschluss besitzt, verteilt ein F.Port2-Mehrkanal-Extender (FP2CH4/6/8) das
Signal auf mehrere Geräte.

**TD-R18 Tandem**: RF System → Schaltfläche des Empfängers → **Options** →
einzelne Pins (z. B. **Pin1**, **Pin5**) auf **FBUS** setzen — auf diese Weise
lassen sich beliebig viele Pins umbelegen, sodass Extender vollständig entfallen;
jeder FBUS-zugewiesene Pin führt dasselbe FBUS-Signal.

## 5. FBUS-Steuerung der Servos prüfen

Servo 1 an Pin1 und Servo 2 an Pin5 anschließen (die Querruderkanäle des
Flächenmodell-Beispiels), einschalten und prüfen, ob die Kanäle 1 und 5 die
jeweils richtigen Servos bewegen.

## 6. FBUS-Telemetrie prüfen

Löschen Sie bei angeschlossenen Servos alle vorhandenen `SRV`-Sensoren unter
[Telemetrie](../model-setup/telemetry.md) und starten Sie die Sensorsuche
erneut. Jedes Servo meldet 4 Sensoren: Strom, Spannung, Temperatur und Status
(`OK` im Normalfall).

## 7. Spätere Konfigurationsänderungen

Ist ein Modell vollständig verkabelt, ist es unpraktisch, ein einzelnes Servo zu
isolieren, um es über Device Config neu zu konfigurieren. Gehen Sie stattdessen
zur Telemetrie, suchen Sie einen Sensor des betreffenden Servos (z. B.
`SRV1 curr`) und wählen Sie **Configure** — damit wird die Konfiguration genau
dieses Servos direkt geöffnet. Nach jeder Änderung **Save to flash** ausführen.

!!! warning
    Ändern Sie in diesem Bildschirm nicht versehentlich die Physical ID oder die
    Application ID — sie sorgen dafür, dass jedes Servo auf dem gemeinsamen Bus
    adressierbar bleibt.
