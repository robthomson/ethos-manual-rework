---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Anzeigen

![Startbildschirm der Anzeige](../assets/display-home.png)

Der Startbildschirm besteht aus einem oder mehreren **Anzeigebildschirmen**, die jeweils aus
**Widgets** aufgebaut sind, die Sie selbst platzieren und konfigurieren. Ein Druck auf `DISP` öffnet den
Anzeigeeditor für den aktuellen Bildschirm.

Es stehen bis zu **acht** Bildschirme zur Verfügung, die jeweils auf einem von
**dreizehn** Layouts basieren (mit bis zu **neun** Widget-Zellen). Widgets können
Telemetriewerte anzeigen, aber auch jede von siebzehn weiteren Informationskategorien —
Modell-/Senderstatus, Timer, Kanäle und mehr. Konfigurierte Bildschirme erreichen Sie
per Touch-Wischgeste oder mit `PAGE` auf/ab; die obere und untere Leiste bleiben
auf jedem Bildschirm sichtbar, außer bei einem Vollbild-Layout.

## Ein Widget hinzufügen

![Widget-Typen](../assets/display-widget-types.png)

Jeder Bildschirm ist ein Raster; das Antippen einer leeren Zelle öffnet die Widget-Auswahl.
Die Widgets reichen von einfachen Text- und Zahlenanzeigen bis hin zu Instrumenten, Diagrammen und
vollständigen Telemetrieprotokollen. Nach dem Platzieren öffnet erneutes Antippen eines Widgets dasselbe
Optionsmenü, mit dem es in der Größe geändert, verschoben oder entfernt wird:

![Widget-Konfigurationsoptionen](../assets/display-widget-config-options.png)

Die Auswahl der eigenen Einstellungen eines Widgets öffnet ein widgetspezifisches Konfigurationsformular.
Das Feld **Quelle** — also der vom Widget angezeigte Wert — verwendet dieselbe
[Quellenauswahl](../getting-started/user-interface-and-navigation.md#choosing-a-source)
wie überall sonst in Ethos:

![Widget-Quelle ändern](../assets/display-change-source.png)

## Widget-Typen {: #widget-types }

**Value** — ein einzelner Zahlen- oder Telemetriewert, als Text dargestellt:

![Konfiguration des Value-Widgets](../assets/display-widget-value-config.png)

Die meisten Quellen unterstützen zudem eine Reduktion auf einen laufenden **Min**- oder **Max**-Wert — nach
Auswahl der Quelle diese lange drücken und Min oder Max wählen — nützlich zum Beispiel
für den schlechtesten RSSI-Wert während eines Fluges:

![Value-Widget Min](../assets/display-widget-value-min.png)
![Value-Widget Min RSSI](../assets/display-widget-value-min-rssi.png)

Nach dem Platzieren wird es als einfache Anzeige auf dem Bildschirm dargestellt:

![Telemetrie-Value-Widget](../assets/display-widget-value-telemetry.png)

**Bitmap** — zeigt ein statisches Bild (z. B. ein Modellfoto) oder einen Satz von
Bildern, die abhängig vom Wert einer Quelle gewechselt werden (z. B. ein Akkusymbol, das sich
mit der Spannung ändert):

![Konfiguration des Bitmap-Widgets](../assets/display-widget-bitmap-config.png)
![Bitmap-Widget-Typ](../assets/display-widget-bitmap-type.png)

**LiPo** — eine speziell entwickelte Akkuanzeige, die von einem Sensor wie
FLVSS liest: Gesamtspannung des Akkupacks, Zellenzahl und jede einzelne Zellenspannung.
Ein Unterschreiten der konfigurierten Schwelle **Low voltage** färbt die Anzeige
rot — im folgenden Beispiel löst eine Schwelle von 3,3 V bei der niedrigsten Zelle aus:

![Konfiguration des LiPo-Widgets](../assets/display-widget-lipo-config.png)
![LiPo-Widget](../assets/display-widget-lipo.png)

**Channels** — bis zu 8 Ausgangskanäle als Balkendiagramm, horizontal oder
vertikal:

![Konfiguration des Channels-Widgets](../assets/display-widget-channels-config.png)
![Channels-Widget](../assets/display-widget-channels.png)

**Line Chart** — stellt den Wert einer Quelle über die Zeit dar und wird bei einem Flight
Reset zurückgesetzt:

![Konfiguration des Liniendiagramm-Widgets](../assets/display-widget-line-chart-config.png)
![Liniendiagramm-Widget](../assets/display-widget-line-chart.png)

- **Source** — was aufgezeichnet wird.
- **Pause condition** — eine Quelle, die die Aufzeichnung anhält/fortsetzt (oder tippen Sie einfach
  das laufende Widget an, falls dafür keine Quelle frei ist).
- **Log period** — Abtastintervall; 500 ms decken etwa 6 Minuten ab,
  bevor gescrollt wird, 1 s etwa 12 Minuten.
- **Inverted** — spiegelt das Diagramm vertikal.
- **Auto range** — skaliert die vertikale Achse automatisch passend zu den Daten;
  abgeschaltet werden stattdessen feste **Min**-/**Max**-Werte verwendet (z. B. ein konstanter
  Bereich von −100 %…+100 %).

Das Antippen eines laufenden Diagramms öffnet **Pause/resume**, **Reset** (Löschen und
Neustart), **Configure widget** oder den Sprung zu **Bildschirme konfigurieren**:

![Optionen des Liniendiagramms](../assets/display-widget-line-chart-options.png)

**Text** — stellt den Inhalt einer Markdown-Textdatei dar (gelesen aus
`documents/user/` — siehe [Datei-Manager](../system-setup/file-manager.md#top-level-folders)):

![Konfiguration des Text-Widgets](../assets/display-widget-text-config.png)
![Text-Widget](../assets/display-widget-text.png)

**Timer Log** — ein scrollbares Protokoll der vergangenen Werte eines ausgewählten Timers, das
bei jedem Zurücksetzen dieses Timers geschrieben wird (nützlich zum Nachverfolgen des Flugakku-Verbrauchs
über eine Session hinweg); **Reverse** setzt den neuesten Eintrag nach oben:

![Konfiguration des Timer-Log-Widgets](../assets/display-widget-timer-logs-config.png)
![Timer-Log-Widget](../assets/display-widget-timer-log.png)

Ein langer Druck auf einen Eintrag (oder auf das Widget) bietet **Clear logs**, das Bearbeiten/Zurücksetzen des
zugrunde liegenden Timers oder den Sprung zur Widget-/Bildschirmkonfiguration:

![Menü eines Timer-Log-Eintrags](../assets/display-widget-timer-log-menu.png)

**GPS Map** — stellt die aktuelle GPS-Position als Spur dar, für Modelle mit einem GPS-Sensor
(weitere Details speziell zu diesem Widget finden Sie im Thread *FrSky - ETHOS Lua Script Programming*
auf rcgroups, Beitrag #8854):

![Konfiguration des GPS-Map-Widgets](../assets/display-widget-gps-map-config.png)

## Optionen auf Bildschirmebene

Über die einzelnen Widgets hinaus verfügt jeder Bildschirm über eigene Einstellungen — Rastergröße des Layouts,
Hintergrund und welche Bildschirme im `PAGE`-Durchlauf enthalten sind:

![Bildschirm-Konfigurationsoptionen](../assets/display-screen-config-options.png)

Ein vollständig konfigurierter Startbildschirm kombiniert mehrere Widgets zu einem auf einen Blick
erfassbaren Layout:

![Hauptansicht](../assets/display-main-view.png)

Siehe [Weitere Anzeigen](additional-displays.md) zum Hinzufügen weiterer Bildschirme
über den Standard hinaus und [Benutzerdefinierte Widgets](custom-widgets.md) für
Lua-skriptbasierte Widgets jenseits der integrierten Auswahl.
