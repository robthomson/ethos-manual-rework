---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Checkliste

![Checkliste](../assets/model-checklist.png)

Eine Reihe von Sicherheitsprüfungen vor dem Flug, die beim Einschalten des
Senders und/oder beim Laden eines Modells ausgeführt werden. Zu den
integrierten Prüfungen gehören Stummschaltung, nicht gesetztes Failsafe,
Schalter- und Geberstellungen sowie Sender- und RTC-Batterie — die
Schalterprüfung zeigt an, in welche Richtung jeder Schalter bewegt werden
muss, gekennzeichnet durch rote Punkte auf dem Warnbildschirm:

![Checkliste beim Start](../assets/model-checklist-at_start.png)

!!! note
    Sowohl `OK` als auch `RTN` überspringen die Vorflugprüfungen
    vollständig, unabhängig davon, was die Warnung auf dem Bildschirm
    nahelegt.

## Gasprüfung

![Prüffunktion](../assets/model-checklist-check_function.png)

Aktivieren Sie die Prüfung und wählen Sie einen Operator — `<` (kleiner
als), `~` (ungefähr gleich) oder `>` (größer als) — im Vergleich zu einem
Wert; es wird gewarnt, wenn sich der Gasknüppel außerhalb des von diesem
Vergleich zugelassenen Bereichs befindet.

## Failsafe-Prüfung

Warnt, wenn für das aktuelle Modell kein [Failsafe](rf-system.md#failsafe)
gesetzt wurde.

!!! tip
    Es wird dringend empfohlen, diese Prüfung aktiviert zu lassen.

## Schalterprüfung

![Schalter](../assets/model-checklist-switches.png)
![Optionen der Schalterprüfung](../assets/model-checklist-switches-options.png)

Für jeden Schalter kann eine bestimmte Stellung beim Start verlangt werden
(Schalter mit eigenen Namen aus [Systemeinstellungen →
Hardware](../system-setup/hardware.md#switches-settings) werden mit diesen
Namen angezeigt). **Alle Schalterstellungen laden** übernimmt die
*aktuellen* physischen Stellungen als Sollstellungen für jeden Schalter,
der nicht mit **Keine Prüfung** gekennzeichnet ist.

## Prüfung der Funktionsschalter

![Funktionsschalter](../assets/model-checklist-function-switches.png)
![Optionen der Funktionsschalterprüfung](../assets/model-checklist-function-switches-options.png)

Dasselbe Prinzip gilt für die sechs
[Funktionsschalter](model-edit.md#function-switches). **Alle
Funktionsschalterstellungen laden** funktioniert genauso wie oben
beschrieben.

## Prüfung der Potis / Schieberegler

![Potis](../assets/model-checklist-pots.png)
![Optionen der Potiprüfung](../assets/model-checklist-pots-options.png)

Verlangt beim Start bestimmte Stellungen der Potis bzw. Schieberegler,
und zwar einzeln für jedes Bedienelement (`~`/`<`/`>`, wie bei der
Gasprüfung). **Alle Potistellungen laden** übernimmt die aktuellen
Stellungen automatisch — prüfen Sie anschließend die automatisch
gewählten Operatoren sorgfältig, da `~` gegenüber `<`/`>` möglicherweise
nicht dem entspricht, was Sie tatsächlich beabsichtigt haben.

## Benutzerdefinierter Text

![Benutzerdefinierter Checklistentext](../assets/model-checklist-user-checklist.png)

Zeigt eine Datei mit einfachem oder erweitertem Text als Teil der
Startcheckliste an, sobald sie für das Modell eingerichtet ist. Die
vollständige Einrichtung finden Sie unter [Anleitung: Benutzerdefinierte
Text-Checkliste](../how-to/user-defined-checklist.md).
