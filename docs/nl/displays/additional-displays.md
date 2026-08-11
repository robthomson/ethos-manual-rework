---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Aanvullende displays

![Opties voor schermconfiguratie](../assets/display-screen-config-options.png)

Het standaardmodel heeft één scherm (een modelafbeelding plus drie Timer-widgets),
maar er worden in totaal maximaal **acht** schermen ondersteund. Tik op de **+**
naast "Screen1" om er nog een toe te voegen:

- Kies uit **15** indelingen, waaronder twee speciale indelingen voor het
  startscherm en een volledig-schermoptie, met ruimte voor maximaal 9 widgets —
  precies zo te configureren als het eerste scherm.
- Schermen kunnen via hun eigen bewerkingsvenster opnieuw worden geordend of
  verwijderd (tik op Screen1, Screen2, enz.).

## Uitgewerkt voorbeeld

![Hoofdweergave](../assets/display-main-view.png)

Een typische indeling: links de modelafbeelding (ingesteld bij [Model bewerken →
Afbeelding](../model-setup/model-edit.md)), met rechts de accuspanning van de
ontvanger, RSSI en een "Throttle ACTIVE" Status-widget (een door de community
gemaakte Lua-widget uit de rcgroups-thread *FrSky - ETHOS Lua Script
Programming*) onder elkaar. Door op een widget te tikken opent de configuratie
ervan, of springt u naar de hoofdfunctie Schermen configureren.

## Opties op schermniveau

Naast de afzonderlijke widgets heeft elk scherm zijn eigen instellingen — de
rastergrootte van de indeling, de achtergrond en welke schermen worden
opgenomen in de `PAGE`-cyclus.

Zie [Displays](index.md) voor de widgets zelf, en [Eigen
widgets](custom-widgets.md) voor het toevoegen van Lua-widgets buiten de
ingebouwde set.
