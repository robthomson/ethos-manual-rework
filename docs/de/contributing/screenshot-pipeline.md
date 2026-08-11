---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Screenshot-Pipeline

Jeder Screenshot in diesem Handbuch (derzeit etwa 590 Stück, unter
`docs/en/assets/`) wurde durch Skripting des echten Ethos-Simulators erzeugt, nicht
von Hand. Die Umgebung liegt im alten Repository
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), unter
`english/manual/`, und wurde **noch nicht in dieses Repository übernommen** — diese
Seite dokumentiert die Funktionsweise, damit die Portierung erfolgen kann und damit
Screenshots in der Zwischenzeit ohne Neuanfang neu erzeugt oder erweitert werden können.

## Aufbau

Für jedes Menü bzw. jeden Abschnitt des Handbuchs existiert ein Dateipaar:

- `manual/macros/<name>.lua` — ein Skript, das gegen die Lua-API des Simulators
  (siehe unten) geschrieben ist, zu einem bestimmten Bildschirm navigiert und an
  jeder aufnahmewürdigen Stelle `simulator.screenshot(path)` aufruft.
- `manual/<name>.sh` — ein einzeiliger Wrapper, der die Simulator-Binärdatei für
  einen bestimmten Sender startet und auf dieses Makro verweist, z. B.:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` führt alle Makros nacheinander aus, um den gesamten
Satz neu zu erzeugen. Für jeden Abschnitt existieren einzelne `.sh`-Dateien,
sodass die Screenshots einer einzelnen Seite neu erzeugt werden können, ohne
alles erneut durchlaufen zu lassen (jedes Makro benötigt zwischen wenigen
Sekunden und über einer Minute).

Wichtige CLI-Optionen:

- `--read-only` — während des Laufs vorgenommene Änderungen nicht speichern.
- `--no-gui` / `--no-audio` — weitgehend headless; einige Makros benötigen dennoch
  die GUI, da der Simulator ohne sie „überspringt“ (siehe den Kommentar in
  `screenshots.sh`).
- `--radio-settings <file>.bin` — mit welchen gespeicherten Sendereinstellungen
  gebootet wird (dies macht Screenshots sprach- und senderspezifisch — ein
  deutscher Lauf verwendet eine deutsche `.bin`-Datei).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — verweisen den Simulator auf die Modelle/Firmware/Dokumente/Audiodateien,
  die er sehen soll, sodass Screenshots bewusst vorbereitete Inhalte zeigen und nicht
  das, was zufällig auf einer echten SD card liegt.
- `--exec <script>.lua` — das nach dem Booten auszuführende Makro.

Jede Senderfamilie (X20S, X20 PRO, X20 PRO AW, X18S) hat ihre eigene
Simulator-Binärdatei und benötigt pro Sprache eine eigene
`--radio-settings`-Datei (z. B. `x20s-en.bin`, `x20pro-en.bin`), da sich die
Benutzeroberfläche zwischen den Sendern leicht unterscheidet und die
Einstellungsdatei zudem die Sprache enthält.

## Die Makro-API

Makros sind einfaches Lua und steuern ein globales `simulator`-Objekt:

| Aufruf | Zweck |
|---|---|
| `simulator.loadModel("name.bin")` | Vor dem Navigieren eine bestimmte Modelldatei laden — jeder Abschnitt des Handbuchs verwendet ein Modell, das zur Demonstration dieses Abschnitts eingerichtet wurde (siehe die Modellliste unten). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Eine Hardware-Taste drücken — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE` usw. Eine Haltedauer löst einen langen Tastendruck aus (öffnet Kontextmenüs). |
| `simulator.turnRotaryEncoder(n)` | Den Encoder um `n` Rastungen bewegen (negativ = rückwärts) — die primäre Methode, den Cursor zwischen Feldern zu bewegen. |
| `simulator.touch(x, y)` | Eine bestimmte Bildschirmkoordinate antippen — verwendet dort, wo Touch der einzige Weg ist, etwas zu erreichen (z. B. Umschalten des Tastaturlayouts). |
| `simulator.setAnalog(channel, value)` | Direkt eine Position von Steuerknüppel/Potentiometer/Schieberegler setzen (`0`-`3` sind die vier Hauptachsen der Steuerknüppel, `ANALOG_LAST_SLIDER` der letzte Schieberegler), sodass Screenshots einen bewusst gewählten, reproduzierbaren Wert zeigen und nicht den Standardwert des Simulators. |
| `simulator.setSwitch(n, position)` | Die Position eines physischen Schalters setzen. |
| `simulator.setDateTime({...})` | Die Uhr des Simulators festsetzen, damit Zeitstempel in Screenshots (und alles Zeitabhängige) über mehrere Läufe hinweg reproduzierbar sind. |
| `simulator.screenshot(path)` | Den aktuellen Bildschirm als PNG aufnehmen, relativ zum Arbeitsverzeichnis des Makros (daher die `../assets/...`-Pfade in jedem Makro). |
| `simulator.connectUsb()` | Das Anstecken an USB simulieren, um das USB-Menü aufzunehmen. |
| `simulator.sleep(seconds)` | Warten, bis sich eine Animation oder ein Telemetriewert stabilisiert hat, bevor aufgenommen wird. |

`manual/macros/common.lua` wird von den meisten Makros per `dofile` eingebunden und
fixiert lediglich Datum und Uhrzeit, sodass jedes Makro vom selben simulierten
Zeitpunkt aus startet.

## Pro Abschnitt verwendete Modelle

`manual/notes.txt` (informell übernommen, noch nicht in dieses Repository kopiert)
ordnet jedem Makro die `.bin`-Modelldatei zu, von der es abhängt, und begründet dies
— z. B. verwendet `model-mixes.lua` die Datei `rarebear.bin`, `model-fm.lua` verwendet
`zblank.bin` (ein Modell mit absichtlich leerer Flugphasen-Konfiguration),
`model-trims.lua` verwendet `blaster.bin` (mit versetzten Trimmungen eingerichtet, um
den Trimmbereich zu demonstrieren). Die Übernahme der Notizen dieser Datei in eine
richtige Dokumentation hier ist Teil der unten beschriebenen Phase-2-Arbeit.

## Was die Portierung in das neue Repository umfasst (noch nicht erledigt)

- Die Entscheidung, ob Makros direkt aus diesem Repository heraus erneut ausgeführt
  werden (was eine lokale Installation des Ethos-Simulators erfordert, wie im alten
  Repository) oder über CI mit im Workflow gebündeltem bzw. heruntergeladenem Simulator.
- Die Umstrukturierung der flachen `../assets/...`-Ausgabepfade, damit sie dem
  seiten- und sprachspezifischen Asset-Layout dieses Repositorys entsprechen
  (`docs/<locale>/assets/`).
- Eine `--radio-settings ... .bin`-Datei und ein Screenshot-Lauf pro Sprache, sobald
  eine andere Sprache als `en` existiert — Screenshots sind
  UI-sprachspezifisch und können nicht zwischen Sprachen geteilt werden.
- Die Entscheidung, wie viele der rund 40 vorhandenen Makros unverändert übernommen
  und wie viele gegen die aktuelle Navigationsstruktur dieses Repositorys neu
  geschrieben werden (einige Makros erzeugen Screenshots für Abschnitte, die nicht
  mehr 1:1 auf das Seitenlayout dieses Handbuchs abgebildet werden können).
