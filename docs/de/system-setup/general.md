---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# General

![Allgemeine Einstellungen](../assets/system-general.png)

Umfasst die Attribute der LCD-Anzeige, die Audio-, die Vario- und die Haptik-Einstellungen sowie die obere Symbolleiste.

## Attribute der LCD-Anzeige

- **Sprache** — die Sprache der Anzeigemenüs (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português und weitere).
- **Tastatur** — ermöglicht die Auswahl zwischen den virtuellen Tastaturlayouts
  QWERTY, QWERTZ und AZERTY.
- **Helligkeit** — Schieberegler für die Helligkeit der Hintergrundbeleuchtung;
  durch langes Drücken von `ENT` werden Optionen zur Verwendung einer Quelle
  (z. B. eines Schiebereglers, siehe Beispiel unten) oder zur Einstellung auf
  Minimum bzw. Maximum aufgerufen.

  ![Helligkeitsmenü](../assets/system-general-brightness-menu.png)
  ![Helligkeitsregler](../assets/system-general-brightness-slider.png)

  !!! note
      Wenn **Helligkeit** und **Helligkeit Ruhe-Modus** gleich sind, bleibt der
      Touchscreen auch im „Ruhezustand“ aktiv.

- **Bildschirm einschalten durch** — legt fest, wodurch die
  Hintergrundbeleuchtung aus dem Ruhezustand geweckt wird (es kann mehr als eine
  Option aktiviert sein): **EIN** (bleibt dauerhaft eingeschaltet),
  **Knüppel Modus**, **Schalter**, **Kreisel** (Neigen des Senders). Tasten
  wecken die Hintergrundbeleuchtung unabhängig von diesen Einstellungen immer.
- **Helligkeit reduzieren nach** — die Dauer der Inaktivität, bevor die
  Hintergrundbeleuchtung ausgeschaltet wird (ausgegraut, wenn „Bildschirm
  einschalten durch“ auf EIN steht).
- **Helligkeit Ruhe-Modus** — Helligkeit der Hintergrundbeleuchtung im
  Ruhezustand.
- **Bildschirm-Gestaltung -dunkel-** — wählt zwischen hellem und dunklem Modus
  für das Display.
- **Farbe hervorheben** — ermöglicht die Auswahl der Hervorhebungsfarbe, die in
  der Anzeige verwendet wird. Die Standardeinstellung ist gelb (`#F8B038`).

## Audio-Einstellungen {: #audio-settings }

![Audio-Einstellungen](../assets/system-general-audio.png)

- **Audio-Sprache** — ermöglicht die Auswahl der Sprache für die Sprachansagen.
- **Auswahl an Stimmen** — Ethos unterstützt mehrere gleichzeitig installierte
  Sprachpakete:

  - **Stimme 1 (Hauptstimme)** — wird für alle Systemansagen verwendet, die Teil
    des Ethos-Betriebssystems sind. Für Englisch kann standardmäßig zwischen
    einer amerikanischen (`us`) und einer englischen (`gb`) Stimme gewählt
    werden; die Dateien werden aus `audio/en/us/system` bzw.
    `audio/en/gb/system` gelesen. Benutzer-Sounddateien für die
    [Sonderfunktion „Audio abspielen“](../model-setup/special-functions.md)
    gehören entsprechend nach `audio/en/us/` oder `audio/en/gb/`.
  - **Stimme 2 / Stimme 3** — zusätzliche Sprachpakete, zum Beispiel eine
    benutzerdefinierte TTS-Stimme. Jede benötigt dieselbe Ordnerstruktur wie
    Stimme 1 — eine Stimme namens „Susan“ benötigt also `audio/en/Susan/` für
    die Benutzer-Sounddateien und `audio/en/Susan/system` für ihre
    System-Sounddateien (jede Stimme muss über einen Ordner `/system` verfügen,
    da **Wert abspielen** und die Stoppuhr-Ansagen daraus lesen; eine
    `.csv`-Liste der standardmäßig mitgelieferten System-Sounddateien wird mit
    jeder Audioversion mitgeliefert). Nach der Installation können Sie die
    Stimme auswählen, die für jede Stoppuhr und jede „Audio abspielen“-Funktion
    verwendet werden soll — oder eine Stimme sogar als Stimme 1 zuweisen und
    damit die Systemansagen vollständig ersetzen.
  - **Stimme „default“** — wird automatisch als sichere Rückfallebene
    installiert (und vermeidet Konvertierungsprobleme bei Installationen aus
    1.4.x): Ist Stimme 1 während der Installation bzw. des Upgrades noch nicht
    eingestellt, wird sie auf `default` gesetzt und liest aus
    `audio/en/default/system`. Häufig nachgefragte benutzerdefinierte
    Sounddateien für „Audio abspielen“ liegen in `audio/en/default/`.

- **Hauptlautstärke** — Schieberegler zum Regeln der Gesamtlautstärke (durch
  langes Drücken von `ENT` kann ein Poti verwendet werden); Pieptöne während der
  Einstellung helfen bei der Beurteilung der Lautstärke.
- **Audio Modus**:
  - **lautlos** — kein Ton (beim Start ertönt dennoch der [Alarm „Stummer
    Modus“](alerts.md), sofern aktiviert).
  - **nur Alarm** — nur Alarme werden per Audio ausgegeben.
  - **Standard** — Töne sind aktiviert.
  - **öfter** — zusätzlich werden Fehlertöne ausgegeben, wenn versucht wird, den
    Maximal- oder Minimalwert eines Wertes zu überschreiten.
  - **immer** — zusätzlich zu den Tönen unter „öfter“ ertönen auch Pieptöne,
    wenn im Menü navigiert wird.
  - **Bluetooth** (nur X20S/HD/Pro/R/RS) — leitet den Ton an ein gekoppeltes
    Bluetooth-Gerät wie z. B. ein Headset weiter. Tippen Sie auf **suche
    Laufwerke**, versetzen Sie das gewünschte Gerät in den Kopplungsmodus und
    wählen Sie es aus, sobald es gefunden wurde:

    ![Bluetooth-Kopplung](../assets/system-general-audio-bluetooth.png)
    ![Bluetooth-Suche](../assets/system-general-audio-bluetooth-searching.png)
    ![Bluetooth-Gerät ausgewählt](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Bluetooth-Verbindungsaufbau](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth verbunden](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Lautsprecher AUS** steuert dann den eingebauten Lautsprecher — wählen Sie
    zwischen „immer ein“, „nur ein, wenn die Telemetrie aktiv ist“ oder
    „gesteuert durch eine Quelle wie einen Schalter“. Das System merkt sich das
    Bluetooth-Gerät; schalten Sie für den normalen Betrieb zunächst den Sender
    und dann das Bluetooth-Gerät ein. Nach dem Verbindungsaufbau dauert es
    einige Sekunden, bis die Stummschaltung des Lautsprechers wieder aktiviert
    wird.

## Vario {: #vario }

![Vario-Audio](../assets/system-general-audio-vario.png)

- **Lautstärke** — die relative Lautstärke des Variotons.
- **Tonfrequenz Sinken** — die Tonhöhe bei Steigrate null.
- **Tonfrequenz Steigen** — die Tonhöhe bei maximaler Steigrate.
- **Wiederholrate** — der Zeitabstand zwischen den Tönen bei Steigrate null.

Weitere Vario-Parameter entnehmen Sie bitte dem VSpeed-Sensor unter
[Telemetrie](../model-setup/telemetry.md) und der [Sonderfunktion Vario
abspielen](../model-setup/special-functions.md).

## Haptik

- **Stärke** — Schieberegler zum Einstellen der Stärke der haptischen Vibration.
- **Mode** — dieselben Optionen wie im Audio-Modus oben.

## Speicherort (X18 und X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Diese Sender verfügen über einen internen 8-GB-eMMC-Speicher. Ethos verwendet
ihn standardmäßig, wodurch eine SD card optional wird — Sie können jedoch den
eMMC, eine SD card oder eine Kombination aus beiden auswählen. Wenn Sie System
und Modelle auf eine SD card verschieben, kopieren Sie die betreffenden
Ordner und Dateien (einschließlich Audio und Bitmaps) **vor** dem Umschalten des
Speicherorts.

![Speicherort](../assets/system-general-storage.png)

## Obere Symbolleiste

![Einstellungen der oberen Symbolleiste](../assets/system-general-topbar.png)

- **Spannung Senderakku digital** — zeigt die Akkuspannung des Senders in der
  oberen Symbolleiste als Zahl statt als Balken an.
- **RSSI digital** — dasselbe für den RSSI von 2,4 GHz und 900 MHz.
- **Modell beim Einschalten wählen** — zeigt beim Start den
  Modellauswahlbildschirm an, bevor die Checklisten-Hinweise des zuvor
  verwendeten Modells erscheinen, sodass Sie das Modell wechseln können, ohne
  diese zuvor bestätigen zu müssen. Das zuletzt verwendete Modell ist
  standardmäßig hervorgehoben.

  ![Modellauswahl beim Start](../assets/system-general-model-start.png)

## USB-Modus-Vorauswahl

![USB-Modus](../assets/system-general-usb.png)

Legt fest, was automatisch geschieht, wenn der Sender per USB mit einem PC
verbunden wird:

- **Nicht gesetzt** — beim Verbinden wird nach einer Auswahl gefragt.
- **Joystick** — wechselt sofort in den Joystick-Modus für einen RC-Simulator.
- **Ethos Suite** — wechselt sofort in den Ethos-Modus für [Ethos
  Suite](../ethos-suite/index.md).
- **Seriell** — wechselt sofort in den seriellen Modus und leitet
  Lua-Debug-Ausgaben mit 115200 bps über USB-Seriell weiter (unter Windows kann
  ein Treiber für den virtuellen COM-Port erforderlich sein).
