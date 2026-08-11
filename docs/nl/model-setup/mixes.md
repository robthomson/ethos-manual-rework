---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mixen

![Pictogram Mixen](../assets/model-icon-mixes.png)

Mixen vormen de kern van het programmeren van modellen in Ethos — hier worden ingangen
(sticks, schakelaars, sensoren, alles wat een [bron](../getting-started/user-interface-and-navigation.md#choosing-a-source)
kan bereiken) doorgestuurd, gevormd en gecombineerd op uitgangskanalen. Er kunnen tot 120
mixen per model worden gedefinieerd.

![Mixentabel](../assets/model-mixes.png)

Als een model is aangemaakt met de **Modelkeuze**-wizard, zijn de basismixen
(rolroer, hoogteroer, gas, richtingsroer en wat het model verder nodig heeft)
hier al ingevuld. Door een mix te selecteren en op `ENT` te drukken opent een
contextmenu waarmee u de mix kunt bewerken, een nieuwe mix kunt toevoegen, kunt overschakelen naar de
[weergave per kanaal](#per-channel-view), de volgorde kunt wijzigen, de mix kunt dupliceren of kunt verwijderen.
Inactieve mixen worden grijs weergegeven en bij het verwijderen wordt altijd eerst om
bevestiging gevraagd.

## Anatomie van een mix {: #anatomy-of-a-mix }

Elke mix heeft dezelfde set velden, ongeacht uit welke categorie de mix
afkomstig is. De mix **rolroer** is een representatief voorbeeld — mixen voor hoogteroer en
richtingsroer zijn identiek opgebouwd.

![Rolroermix](../assets/model-mixes-ail-edit.png)

![Editor voor rolroermix](../assets/model-mixes-ail.png)

**Naam** — standaard het mixtype, aanpasbaar.

**Voorwaarde** — standaard *Altijd*. Kan worden beperkt tot een schakelaarstand,
een functieschakelaar, een logische schakelaar, een vluchtmodus, een
systeemgebeurtenis (gas-afsnijding/gas vasthouden) of een trimstand; in dat geval geldt de mix
alleen zolang de voorwaarde waar is.

**Vluchtmodi** — als er vluchtmodi zijn gedefinieerd, kan de mix bovendien
worden beperkt tot een of meer daarvan.

**Curve** — standaard is een **Expo**-curve beschikbaar (0 = lineair; positief
maakt de reactie rond het midden zachter, negatief maakt deze scherper):

![Expo-curve](../assets/model-mixes-ail-expo.png)

In plaats daarvan kan elke eerder onder [Curves](curves.md) gedefinieerde curve worden
gekozen. Per mix kunnen tot 6 curves worden gestapeld, elk met zijn eigen
voorwaarde — als meer dan één voorwaarde tegelijk waar is, wint de curve die
hoger in de lijst staat. Curves worden **vóór** de rates toegepast.

**Rates** — een of meer gewichtsrijen, elk optioneel geactiveerd door een schakelaar,
functieschakelaar, logische schakelaar, trimstand of vluchtmodus. De eerste
rij is de standaardrij en is actief zolang aan geen enkele andere rijvoorwaarde is voldaan:

![Rolroer-rates](../assets/model-mixes-ail-weight.png)

In plaats van een vast percentage kan een rate worden aangestuurd door een
[bron](../getting-started/user-interface-and-navigation.md#choosing-a-source)
— bijvoorbeeld een potentiometer, om de rate tijdens de vlucht aan te passen:

![Rate aangestuurd door een bron](../assets/model-mixes-ail-diff.png)

**Differentieel** (-100 tot 100, standaard 0) — geeft in de ene richting meer uitslag
dan in de andere. Voor rolroeren is dit de klassieke truc van meer uitslag naar
boven dan naar beneden om negatief giermoment te beperken. Wordt alleen weergegeven zodra de mix
meer dan één uitgangskanaal heeft; differentieel is met name pas zinvol bij een
V-staart- of dubbele-rolroerconfiguratie van de uitgangen.

**Aantal kanalen / uitgangen** — hoeveel uitgangskanalen deze mix aanstuurt
en aan welke fysieke uitgangen deze zijn toegewezen:

![Aantal kanalen](../assets/model-mixes-ail-ch-count.png)

Een lange druk op `ENT` op een uitgangskanaal elders in de interface (bijvoorbeeld in
[Uitgangen](outputs.md)) brengt u direct terug naar deze pagina.

## De gasmix

De gasmix is een mix zoals die voor rolroer/hoogteroer/richtingsroer, plus motorspecifieke
veiligheidsopties.

![Gasmix](../assets/model-mixes-thr.png)

**Ingang** — de gasbron, normaal gesproken de gasstick, maar deze kan worden
vervangen door een potentiometer, schuifregelaar, schakelaar, trim, kanaal, gyro-as, trainerkanaal,
timer of elke andere bron.

**Stationairtrim** — laat bij brandstofmotoren een aparte trim het stationaire toerental
aanpassen zonder de volgasstand te beïnvloeden. Met stationairtrim ingeschakeld staat het
gaskanaal op -75% wanneer de stick op laag stationair staat; de gastrim regelt vervolgens
het stationair tussen -100% en -50%:

![Menu stationairtrim](../assets/model-mixes-thr-trim-menu.png)

![Stationairtrim in lage stand](../assets/model-mixes-thr-trim-low-position.png)

**Gas-afsnijding** — een harde veiligheidsvergrendeling: het kanaal is pas actief nadat
de gasstick door stationair is gegaan, zodat een onbedoelde schakelaarbeweging de motor
niet vanuit een hoge gasstand kan laten aanlopen:

![Gas-afsnijding](../assets/model-mixes-thr-cut.png)

**Gas vasthouden** — houdt het kanaal op een vaste waarde, ongeacht de stickstand,
zonder de veiligheidsvergrendeling die gas-afsnijding biedt:

![Gas vasthouden](../assets/model-mixes-thr-hold.png)

Ook voor gas kan het aantal uitgangskanalen worden ingesteld, net als bij elke andere
mix:

![Aantal gaskanalen](../assets/model-mixes-thr-ch-count.png)

!!! note "Gasvergrendeling"
    Ethos vereist dat de ingang van de gasmix door -100% gaat voordat er wordt
    ontgrendeld, ongeacht de instellingen voor gas-afsnijding/gas vasthouden — bij een model dat met de
    Modelkeuze-wizard is aangemaakt is hier al rekening mee gehouden, maar bij handmatig opgebouwde
    gasmixen moet dat ook gebeuren.

## Mixbibliotheken {: #mix-libraries }

De bibliotheek met vooraf gedefinieerde mixen in de dialoog **Mix toevoegen** is afgestemd op de
modelcategorie die bij het aanmaken van het model is gekozen — vliegtuig, zweefvliegtuig, heli
en multirotor bieden elk een andere set:

![Mixbibliotheek vliegtuig](../assets/model-mixes-library-airplane.png)

![Mixbibliotheek zweefvliegtuig](../assets/model-mixes-library-glider.png)

![Mixbibliotheek heli](../assets/model-mixes-library-heli.png)

![Mixbibliotheek multirotor](../assets/model-mixes-library-multirotor.png)

Elke bibliotheek bevat ook een **Vrije mix** — een mixtype voor algemeen gebruik
zonder vooraf ingestelde in- of uitgang, flexibeler dan de gespecialiseerde items
maar met meer instelwerk om hetzelfde resultaat te bereiken.

## Weergave per kanaal {: #per-channel-view }

Als er veel mixen op dezelfde uitgang zijn gestapeld, kan het moeilijk zijn om hun
gecombineerde effect in de bovenstaande vlakke tabel te zien. Door een mix te selecteren en
**Weergave per kanaal** te kiezen, worden alle mixen die één uitgang beïnvloeden juist samen gegroepeerd:

![Overschakelen naar kanaalweergave](../assets/model-mixes-chview-select.png)

![Ingeklapt kanaal](../assets/model-mixes-chview-collapsed.png)

![Hoogteroerkanaal uitgeklapt](../assets/model-mixes-chview-elevator.png)

Door de samenvattingsrij van een kanaal uit te klappen worden alle mixen weergegeven die eraan bijdragen, elk
met hun actuele numerieke en grafische uitgangswaarde — nuttig om precies vast te stellen
hoeveel een secundaire mix (bijvoorbeeld compensatie van kleppen naar hoogteroer) bovenop de
primaire stickingang optelt:

![Detail kanaalweergave hoogteroer](../assets/model-mixes-chview-elevator-channel.png)

![Hoogteroerkanaal, mix gemarkeerd](../assets/model-mixes-chview-elevator-channel-view.png)

Wanneer u een submix selecteert in plaats van de samenvattingsrij, opent hetzelfde
contextmenu als in de vlakke tabel (bewerken, terug naar tabelweergave, verwijderen):

![Tabelweergave kiezen vanuit kanaalweergave](../assets/model-mixes-chview-table-view-select.png)

![Terug naar tabelweergave](../assets/model-mixes-chview-back-at-mixes-view.png)
