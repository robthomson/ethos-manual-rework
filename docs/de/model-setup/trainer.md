---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Standardmäßig ausgeschaltet. Der Sender kann als **Master** (Lehrer-Sender,
der bis zu 16 Steuersignale vom Schüler empfängt) oder als **Slave**
(Schülersender, der eine konfigurierbare Anzahl von Kanälen an den Lehrer
sendet) konfiguriert werden.

## Master-Modus

![Master-Modus](../assets/model-trainer-master.png)
![Trainer-Optionen](../assets/model-trainer-options.png)

### Verbindungs-Modus

![Optionen für den Verbindungs-Modus](../assets/model-trainer-link-mode-options.png)

- **Trainer-Kabel** — ein 3,5-mm-Mono-Audiokabel zwischen den beiden Sendern.
- **Bluetooth** —

  ![Bluetooth-Verbindung](../assets/model-trainer-link-mode-bt.png)

  - **Mode** — normale oder hohe Geschwindigkeit; für eine geringere
    Latenzzeit sollte die hohe Geschwindigkeit verwendet werden, wenn sie
    beide Sender unterstützen.

    ![Bluetooth-Mode](../assets/model-trainer-link-mode-bt-mode.png)

  - **Lokaler Name** — der lokale BT-Name, der in den angeschlossenen
    Geräten angezeigt wird (Standardname `FrSkyBT`, kann geändert werden).
  - **Lokale Adresse** — die lokale Bluetooth-Adresse dieses Senders.
  - **Externe Adresse** — die Bluetooth-Adresse des entfernten Geräts,
    sobald es verbunden wurde.
  - **Geräte suchen** (nur im Master-Modus) — versetzt den Sender in den
    BT-Suchmodus und sucht nach Geräten in der Umgebung:

    ![Suche läuft](../assets/model-trainer-link-mode-bt-search.png)
    ![Warten](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Gerät auswählen](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Verbunden](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Letztes Gerät anschließen** / **Modul zurücksetzen** — stellt eine
    Verbindung mit dem zuletzt konfigurierten Gerät her bzw. setzt das
    Bluetooth-Modul zurück und löscht dessen Konfigurationseinstellungen.

- **SBUS externes HF-Modul** — bietet einen SBUS-Eingang am PXX IN Pin im
  externen Modulschacht. Dies ermöglicht den Einbau eines FrSky-Empfängers
  mit SBUS-Ausgang (z. B. Archer RS) als Empfänger einer drahtlosen
  Trainerverbindung — so kann **jeder** FrSky-Sender als Schülerseite
  (Buddy-Box) dienen, wenn er an diesen Empfänger gebunden ist.
- **CPPM externes Modul** — in ähnlicher Weise über einen CPPM-Eingang, für
  einen älteren Empfänger mit CPPM-Ausgang.

### Aktive Bedingung

![Aktive Bedingung](../assets/model-trainer-active-condition.png)

Ein Schalter oder Taster, ein Funktionsschalter, ein Logikschalter, eine
Trimmstellung oder ein Flugmodus, der die Steuerung im aktiven Zustand an den
Schüler übergibt.

### Trainer-Kanäle

![Aktive Bedingung bearbeiten](../assets/model-trainer-active-condition-edit.png)

Bis zu 16 Kanäle können vom Schülersender an den Lehrer-Sender übertragen
werden, solange die aktive Bedingung erfüllt ist. Tippen Sie auf jeden Kanal,
um ihn einzeln zu konfigurieren:

- **Aktive Bedingung** — jeder einzelne Schüler-Kanal kann zusätzlich von der
  ausgewählten Quelle gesteuert werden, so kann z. B. der
  Höhenrudereingang des Schülers während eines Teils des Fluges deaktiviert
  werden.
- **Mode** — **AUS** (deaktiviert den Kanal für die Verwendung durch den
  Trainer), **hinzufügen** (additiver Modus, bei dem Lehrer- und
  Schüler-Signale addiert werden, so dass beide gleichzeitig auf die Funktion
  einwirken können) oder **ersetzen** (die normale Betriebsart — der Schüler
  hat die volle Kontrolle über diesen Kanal, während die aktive Bedingung
  erfüllt ist).
- **Prozent** — skaliert den Schüler-Eingang, normalerweise auf 100 %
  eingestellt.
- **Zielort** — ordnet den Kanal des Schülersenders der entsprechenden
  Funktion zu.

Siehe [Anleitung: Sofortige Rückübernahme](../how-to/instant-takeback.md) für
ein ausgearbeitetes Beispiel, wie ein Lehrer die Steuerung per Schalter
sofort zurückholt, sowie [Schülereingaben
ignorieren](../getting-started/user-interface-and-navigation.md#choosing-a-source),
um zu verhindern, dass die Knüppeleingaben des Schülers einen Logikschalter
auslösen, der die eigenen Steuerknüppel des Lehrers überwacht.

## Slave-Modus

![Slave-Modus](../assets/model-trainer-slave-mode.png)

- **Verbindungs-Modus** — dieselbe Auswahl aus Trainerkabel, Bluetooth oder
  externem SBUS-/CPPM-Modul wie beim Master (mit denselben Bluetooth-Feldern
  **Mode**/**Lokaler Name**/**Lokale Adresse**/**Externe Adresse**).

  ![Slave-Verbindungs-Modus](../assets/model-trainer-slave-link-mode.png)

- **Kanalbereich** — legt fest, welcher Kanalbereich dieses Senders an den
  Lehrer-Sender übertragen wird.

  ![Slave-Kanäle](../assets/model-trainer-slave-channels.png)
  ![Slave-Kanal bearbeiten](../assets/model-trainer-slave-channel-edit.png)
