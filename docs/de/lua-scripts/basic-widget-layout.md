# Struktur eines Lua-Widgets

Alle Lua-Skripte – einschließlich der Widgets – verwenden Handler (auch als Code-Module bezeichnet), um spezifische Aufgaben auszuführen, wie etwa die Hintergrunddatenver-arbeitung, die Steuerung bzw. Darstellung der Anzeige, die Konfiguration von Widgets, das Auslesen oder Speichern von Konfigurationen, das Abfangen und Auswerten von Ereignissen und Ähnliches.

## init(function)

Die Init-Handler-Funktion dient dazu, das Widget während des Senderstarts zu registrieren. Sie verwendet die Methode system.registerWidget(), um das Widget zu deklarieren. Zudem legt sie fest, welche weiteren Handler im Skript zum Einsatz kommen.

Ein Beispiel für einen Init-Handler für ein Widget könnte wie folgt aussehen:

local function init()

system.registerWidget({

key = "unique",

name = “Example”,

create = create,

configure = configure,

wakeup = wakeup,

paint = paint,

read = read,

write = write,

})

end

Bitte beachten Sie, dass „key“ ein eindeutiger Bezeichner für Ihr Widget ist. Die verschiedenen aufgeführten Funktionen werden im Lebenszyklus des Widgets verwendet.

## system.registerWidget() method

Die Methode system.registerWidget() kann die folgenden Parameter aufweisen:

## key (string)

Das Widget muss einen eindeutigen Schlüssel haben.

## name (string or function)

Die Funktion name benötigt keine Argumente und gibt den Namen des Widgets als Zeichenkette zurück. Der Name kann einfach eine Zeichenkette oder das Ergebnis einer Funktion sein. Zum Beispiel kann der Name je nach Gebietsschema in einer anderen Sprache sein.

## create (function)

Die Funktion create handler wird bei der Erstellung eines Widgets aufgerufen. Sie benötigt keine Argumente und gibt die Widget-Tabelle zurück, die dann später an alle Funktionen übergeben wird. Initialisieren Sie hier Ihre Variablen und speichern Sie den Status in der zurückgegebenen Widget-Tabelle.

### destroy (function, optional)

Der Destroy-Handler wird bei der Löschung des Widgets aufgerufen.

## configure (function)

Die Configure-Handler-Funktion wird aufgerufen, wenn der Benutzer die Widget-Konfiguration aufruft. Sie akzeptiert die von \`create()\` zurückgegebene Widget-Tabelle als einziges Argument und liefert keinen Rückgabewert. Sie wird immer dann ausgeführt, wenn der Benutzer in die Widget-Konfiguration wechselt. An dieser Stelle können Sie das Konfigurationsformular erstellen und es dazu verwenden, Werte in der Widget-Tabelle zu ändern.

## wakeup (function)

Die Wakeup-Handler-Funktion wird in jeder Schleife aufgerufen, d.h. alle 50ms. Sie nimmt die Widget-Tabelle als einziges Argument und gibt nichts zurück.

Die Funktion wakeup() sollte prüfen, ob sich etwas geändert hat. Wenn ja, ist eine Aktualisierung erforderlich, so dass die Funktion invalidateWindow() aufgerufen werden sollte. Daraufhin wird die Funktion paint() aufgerufen. Sie sollten dafür sorgen, dass diese Funktion sehr schnell ist und idealerweise die meiste Zeit nichts tut.

## event (function)

Die Ereignisbehandlungsfunktion, die aufgerufen wird, wenn ein Ereignis empfangen wird. ETHOS bietet die Möglichkeit, jedes Ereignis in einem Widget durch diese Ereignisfunktion abzufangen.

## paint (function)

Die Funktion paint 'zeichnet' das Widget. Sie nimmt die Widget-Tabelle als einziges Argument und gibt nichts zurück. Sie sollte aufgerufen werden, wenn eine Aktualisierung erforderlich ist, und wird automatisch aufgerufen, wenn lcd.invalidate() aufgerufen wurde. Sie kann langsam sein, daher sollten Sie nur zeichnen, wenn sich etwas geändert hat.

### menu (function, optional)

Der optionale Menü-Handler wird aufgerufen, wenn ein Kontextmenü erstellt wird, um das Hinzufügen weiterer Optionen zum Menü zu ermöglichen. Der Handler sollte eine Tabelle von Paaren der Form { Name, Funktion } zurückgeben.

## read (function)

Optionaler Lese-Handler. In ETHOS ist es möglich, den Speicher nach den Wünschen des Benutzers zu nutzen.

## write (function)

Optionaler Schreibhandler. In ETHOS ist es möglich, den Speicher nach den Wünschen des Benutzers zu nutzen.

### persistent (boolean, optional)

Optionaler Handler für persistente Daten

### title (boolean, optional)

Optionaler Titel-Handler. Der Widget-Titel wird erzwungen ein- oder ausgeschaltet.

LUA-Skripte werden im Ordner scripts/ auf der SD-Karte oder eMMC gespeichert, vorzugsweise in Ordnern organisiert.

Bitte lesen Sie den rcgroups 'FrSky ETHOS Lua Script Programming' Thread für weitere Informationen.
