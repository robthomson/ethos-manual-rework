---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modelkeuze

![Modelwizard - vliegtuig](../assets/model-modelselect-model-wizard-airplane.png)

Hiermee maakt, selecteert, kloont en verwijdert u modellen, en beheert u de
zelfgedefinieerde categoriemappen waarin ze zijn ondergebracht.

## Modelmappen beheren

![Modelmappen](../assets/model-modelselect-folders.png)

Met Ethos kunt u modellen groeperen in eigen mappen — doorgaans zaken als
Airplane, Glider, Heli, Quad, Warbird, Boat, Car, Template of Archive.
Zolang u er geen hebt aangemaakt, staan modellen in een automatische map
**Uncategorized** (aangemaakt bij het upgraden naar Ethos 1.1.0 alpha 17+,
of wanneer een modelbestand van elders naar `\Models` wordt gekopieerd);
Ethos verwijdert deze map weer zodra hij leeg is.

Om een map aan te maken, tikt u op **+** naast "Uncategorized" (of houdt u
`PAGE` omhoog/omlaag lang ingedrukt), geeft u de map een naam (maximaal 15
tekens) en bevestigt u. Mappen worden alfabetisch gesorteerd, waarbij
**Uncategorized** altijd als laatste staat, en komen direct overeen met
submappen onder `\Models` op de SD card/eMMC. Door op een mapnaam te tikken
opent u hernoemen/verwijderen — bij het verwijderen van een map worden de
modellen die erin staan teruggeplaatst naar Uncategorized.

![Map wijzigen](../assets/model-modelselect-folder-change-select.png)

Om een model te verplaatsen, tikt u op het pictogram, kiest u **Change
folder** en tikt u vervolgens op de bestemming:

![Map kiezen](../assets/model-modelselect-folder-airplane-select.png)

## Een nieuw model toevoegen

![Model aanmaken](../assets/model-modelselect-model-create.png)

Selecteer de categorie waarin het model moet worden aangemaakt, tik op **+**
en daarna op **Create model** om de wizard te starten (maak eerst de
categorie aan als die nog niet bestaat). Er zijn wizards beschikbaar voor
**Airplane**, **Glider**, **Helicopter**, **Multirotor** en **Other**; elke
wizard loopt de basisinstellingen voor dat type luchtvaartuig door, inclusief
optionele voorgedefinieerde mixen voor gestabiliseerde FrSky-ontvangers
(gain, stabilisatiemodus). Modelnamen mogen maximaal 15 tekens lang zijn.

### Gestabiliseerde ontvangers en kanaalvolgorde

![Wizard: vliegtuig](../assets/model-modelselect-model-wizard-airplane.png)

Gestabiliseerde FrSky-ontvangers vereisen specifiek kanaalvolgorde **AETR** —
laat [Sticks → Channel order](../system-setup/controls.md) op de AETR-standaard
staan met **First four channels fixed** aan, zodat de uitgangen van de wizard
overeenkomen met wat de ontvanger verwacht.

De wizard wijst kanalen van rechts naar links toe. Voor 2 rolroeren + 1
hoogteroer + 1 richtingsroer + 1 motor is dat:

| Kan. | Functie |
|---|---|
| 1 | Rolroer 1 (rechter rolroer) |
| 2 | Hoogteroer |
| 3 | Gas |
| 4 | Richtingsroer |
| 5 | Rolroer 2 (linker rolroer) |

Met deze toewijzing is het rolroerdifferentieel **positief** voor het normale
geval (meer uitslag naar boven dan naar beneden). De eigen
ontvangerhandleidingen van FrSky documenteren momenteel de *omgekeerde*
conventie (van links naar rechts, dus Kan.1 = linker rolroer, Kan.5 = rechter
rolroer) — in dat geval zou het differentieel **negatief** moeten zijn voor
hetzelfde fysieke effect.

!!! tip
    Het wordt aanbevolen om de Ethos-conventie consequent te gebruiken — alle
    stabilisatiefuncties werken in beide gevallen nog correct, aangezien de
    compensatierichting tijdens de stabilisatie-instelling wordt bepaald. Als
    u toch de conventie uit de ontvangerhandleiding moet volgen, is de
    eenvoudigste weg het model gewoon met de wizard op te bouwen en daarna met
    **Swap channels** in [Uitgangen](outputs.md) de twee rolroerkanalen om te
    wisselen — zo blijft het teken van het differentieel in de rolroermixer
    positief.

### Stappen van de wizard

![Wizard: staarttype](../assets/model-modelselect-model-wizard-tail.png)
![Wizard: aantal rolroeren/flaps](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Wizard: aantal hoogteroeren/richtingsroeren](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Wizard: motor](../assets/model-modelselect-model-wizard-engine.png)
![Wizard: kanaaltoewijzing wijzigen](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Wizard: naam](../assets/model-modelselect-model-wizard-name.png)
![Wizard: ontvanger](../assets/model-modelselect-model-wizard-rx.png)

Bij een **Airplane** komt na het staarttype en het aantal stuurvlakken het
aantal motorkanalen aan de orde, en daarna het aantal rolroer-/flapkanalen.

Bij de **staartconfiguratie** kiest u tussen een traditionele kruisstaart, een
V-staart of geen staart (delta/vliegende vleugel):

- **Delta/vliegende vleugel** — bij het aanmaken van een Airplane-model met 2
  rolroeren en geen staartvlakken wordt automatisch elevon-mixing opgebouwd,
  met standaardgewichten van 50% zodat volledige gelijktijdige rolroer- +
  hoogteroercommando's samen nog altijd 100% zijn.
- **Delta waarbij een gestabiliseerde ontvanger de mixing doet** — kies dan
  1 rolroer en 1 hoogteroer; de elevon-mixing gebeurt in de ontvanger, volgens
  de bijbehorende handleiding.
- **Delta met afzonderlijke rolroer- en hoogteroervlakken** — laat de wizard
  lopen alsof het model een staart heeft; hij configureert de benodigde
  rolroer- en hoogteroerkanalen (met of zonder richtingsroer), en er wordt geen
  elevon-mixing aangemaakt.

Bij de stap **kanaaltoewijzing wijzigen** kunt u de standaardtoewijzing van de
wizard overschrijven, waarbij u er rekening mee moet houden dat gestabiliseerde
ontvangers hun kanalen in een specifieke volgorde nodig hebben (raadpleeg de
instructies van de ontvanger). In de laatste stap stelt u de modelnaam in en
koppelt u een afbeelding.

Het voltooide model komt terecht in de categoriemap die actief was toen de
wizard werd gestart, alfabetisch gesorteerd binnen die map. Zie [Eenvoudig
voorbeeld met vaste vleugel](../tutorials/basic-fixed-wing.md) voor een
volledig uitgewerkte doorloop.

## Een model van een andere Ethos-zender ontvangen

![Model ontvangen](../assets/model-modelselect-model-receive.png)

Selecteer de doelcategorie, tik op **+** en daarna op **Receive model** — de
zender wacht en toont zijn Bluetooth-adres, zodat de verzender hem kan vinden.
Tik op de verzendende zender op het model en kies **Send model**; de
ontvangende zender vraagt om bevestiging van de inkomende bestandsnaam voordat
deze wordt geaccepteerd.

## Een model selecteren

Tik op **Model select** voor de modellijst.

!!! note "Modelconversie na een Ethos-upgrade"
    Ethos converteert elk model afzonderlijk op het moment dat het na een
    versie-upgrade voor het eerst wordt *geselecteerd*, en niet allemaal
    tegelijk bij de upgrade — er is geen merkbare vertraging en het kan zonder
    problemen op een later moment gebeuren, zelfs onder een nog nieuwere
    Ethos-versie. De datum bij **Last Modification** onderaan het
    selectiescherm wordt bijgewerkt wanneer er een conversie plaatsvindt (of
    wanneer u het model bewerkt — anders blijft deze ongewijzigd).

**Snelle selectie** — een lange aanraking of lang indrukken van `ENT` op een
modelpictogram schakelt direct over naar dat model.

**Menu modelbeheer** — tik op een model om het te markeren, tik nogmaals voor
het menu:

- **Set current model**
- **Clone** — dupliceert het model. Een kloon krijgt automatisch een nieuw
  ontvangernummer; als u in plaats daarvan het ontvangernummer van het
  origineel opnieuw toewijst, werkt het zonder opnieuw te binden.
- **Change folder**
- **Send**/**Receive** — naar of van een andere zender, zoals hierboven.
- **Delete** — alleen beschikbaar voor een model dat niet het huidige model is.
