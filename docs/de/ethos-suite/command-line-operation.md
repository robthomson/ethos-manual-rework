# Befehlszeilenbetrieb

Die FrSky Suite kann über die Befehlszeile eines Terminals ausgeführt werden.

Die folgenden Befehlszeilenoptionen stehen zur Verfügung:

| --help | Hilfetext für das Befehlszeilen-Tool der FrSky Suite. |
| --- | --- |
| --version | Zeigen Sie die Version der installierten FrSky Suite an. |
| --list-radios | Listen Sie alle unterstützten FrSky-Fernsteuerungen auf. |
| --radio-components<br>--radio {RADIO}<br>--radio auto | Listen Sie alle Komponenten und deren Pfade auf. <br>Wenn mehrere Sender an Ihren Computer angeschlossen sind, können Sie mit \[--radio {RADIO}\] eines davon angeben.<br>Andernfalls können Sie \[--radio {RADIO}\] weglassen oder \[--radio auto\] für die automatische Erkennung verwenden. |
| --get-path {COMPONENT} | Den Pfad der angegebenen Komponente abrufen.<br>Derzeit unterstützte Komponenten: BITMAPS, SCRIPTS, SCREENSHOTS, AUDIO, I18N. |
| --serial start\|stop | Den seriellen Debug-Modus aktivieren / deaktivieren. |

Hinweis: Die Suite-App startet erst, wenn sie einen Befehl erfolgreich erkennt.
