---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Checklist

![Checklist](../assets/model-checklist.png)

Een reeks veiligheidscontroles vóór de vlucht die worden uitgevoerd wanneer de
zender wordt opgestart en/of een model wordt geladen. De ingebouwde controles
omvatten stille modus, failsafe niet ingesteld, schakelaar-/potentiometerposities,
zender- en RTC-batterij — de schakelaarcontrole laat zien in welke richting elke
schakelaar moet worden bewogen, aangegeven met rode stippen op het
waarschuwingsscherm:

![Checklist bij opstarten](../assets/model-checklist-at_start.png)

!!! note
    Zowel `OK` als `RTN` slaat de controles vóór de vlucht volledig over,
    ongeacht wat de waarschuwing op het scherm suggereert.

## Gascontrole

![Controlefunctie](../assets/model-checklist-check_function.png)

Schakel de controle in en kies een operator — `<` (kleiner dan), `~` (ongeveer
gelijk) of `>` (groter dan) — ten opzichte van een waarde; er wordt gewaarschuwd
als de gasstick buiten het bereik van die vergelijking valt.

## Failsafe-controle

Waarschuwt als [failsafe](rf-system.md#failsafe) niet is ingesteld voor het
huidige model.

!!! tip
    Het wordt sterk aanbevolen om dit ingeschakeld te laten.

## Schakelaarcontrole

![Schakelaars](../assets/model-checklist-switches.png)
![Opties schakelaarcontrole](../assets/model-checklist-switches-options.png)

Vraag per schakelaar een specifieke positie bij het opstarten (schakelaars met
eigen namen uit [Systeeminstellingen →
Hardware](../system-setup/hardware.md#switches-settings) worden met die namen
weergegeven). **Alle schakelaarposities laden** neemt de *huidige* fysieke
posities over als de gewenste posities voor elke schakelaar die niet is gemarkeerd
als **Geen controle**.

## Controle van functieschakelaars

![Functieschakelaars](../assets/model-checklist-function-switches.png)
![Opties controle functieschakelaars](../assets/model-checklist-function-switches-options.png)

Hetzelfde principe, voor de zes
[functieschakelaars](model-edit.md#function-switches). **Alle posities van
functieschakelaars laden** werkt op dezelfde manier als hierboven.

## Controle potentiometers / schuifregelaars

![Potentiometers](../assets/model-checklist-pots.png)
![Opties controle potentiometers](../assets/model-checklist-pots-options.png)

Vraagt bij het opstarten om specifieke posities van potentiometers/schuifregelaars,
afzonderlijk per bedieningselement (`~`/`<`/`>`, net als bij de gascontrole).
**Alle potentiometerposities laden** neemt de huidige posities automatisch over —
controleer daarna zorgvuldig de automatisch gekozen operatoren, want `~` versus
`<`/`>` komt mogelijk niet overeen met wat u werkelijk bedoelde.

## Door gebruiker gedefinieerde tekst

![Eigen checklisttekst](../assets/model-checklist-user-checklist.png)

Geeft een bestand met platte of opgemaakte tekst weer als onderdeel van de
opstartchecklist, zodra dit voor het model is geïnstalleerd. Zie [Handleiding:
checklist met eigen tekst](../how-to/user-defined-checklist.md) voor de volledige
configuratie.
