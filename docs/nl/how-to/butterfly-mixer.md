---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Butterfly (Crocodile) mixer

Butterfly-remmen (ook bekend als crow) regelen de daalsnelheid, vooral bij
zweefvliegtuigen: de rolroeren gaan een beperkt stuk omhoog terwijl de flaps
ver naar beneden gaan, wat aanzienlijke weerstand oplevert — ideaal om een
landingsnadering te beheersen. Deze uitleg gaat uit van een zweefvliegtuig
waarvan de flapkanalen al bestaan (aangemaakt door de wizard van
[Modelkeuze](../model-setup/model-select.md)), met de gasstick als reminvoer:
geen butterfly met de stick omhoog, steeds meer naarmate hij naar beneden
gaat, met hoogteroercompensatie zodat het zweefvliegtuig niet omhoog schiet
wanneer crow wordt ingezet.

## 1. Schakel de standaard Flaps-mix uit

![Flaps-mix uitschakelen](../assets/how-to-butterfly-flaps-disable.png)

Zet de **Active condition** van de door de wizard aangemaakte Flaps-mix op
`---` — deze wordt niet gebruikt.

## 2. Maak de Butterfly-mix aan

![Butterfly-mix toegevoegd](../assets/how-to-butterfly-mix-added.png)

Tik op een willekeurige mix, **Add Mix** → **Butterfly** uit de
[mixbibliotheek](../model-setup/mixes.md#mix-libraries), geplaatst na de (nu
uitgeschakelde) Flaps-mix.

## 3. Configureer de ingang

![Gas als ingang](../assets/how-to-butterfly-mix-source-thr.png)

Zet **Input** op **Throttle**. Omdat gas met de stick omhoog normaal de
maximumwaarde geeft, terwijl butterfly met de stick omhoog 0 moet zijn: houd
`ENT` lang ingedrukt op Throttle en kies **Invert**:

![Gas inverteren](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Geïnverteerd gas](../assets/how-to-butterfly-mix-source-thr-neg.png)

De ingang geeft nu 0 met de stick volledig omhoog, en het veld toont
`-Throttle` om de inversie te bevestigen. Zet **Active condition** op een
landingsvluchtmodus (of een andere schakelaar) als butterfly niet altijd
beschikbaar moet zijn.

## 4. Voeg een curve met dode zone toe

![Curve selecteren](../assets/how-to-butterfly-mix-curve-select.png)

Een kleine dode zone aan het nulpunt van de stick voorkomt onbedoeld
uitslaan door kleine stickruis nabij de eindaanslag. Voeg een aangepaste
3-puntscurve toe (bijvoorbeeld genaamd "Crowdb") met **Easy mode**
uitgeschakeld, zodat de X-punten verplaatst kunnen worden:

![3-puntscurve](../assets/how-to-butterfly-mix-curve-3pt.png)
![Curvepunten](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    Het toevoegen van een aangepaste curve aan de Butterfly-mix verwijdert
    de interne 0–100-offset (die normaal automatisch wordt toegepast) — de
    curve zelf moet die 0–100-transformatie nu reproduceren. In dit
    voorbeeld blijft de uitgang 0% tot de gasstick −90% bereikt en stijgt
    daarna lineair naar 100%:

    ![Curve toegevoegd](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Configureer rolroeren en flaps

![Rolroeruitgang](../assets/how-to-butterfly-mix-ailerons.png)

Een beperkte rolroeruitslag naar boven (bijvoorbeeld 20%) gecombineerd met
een grote flapuitslag is de gebruikelijke verdeling. Flaps hebben doorgaans
veel meer uitslag naar beneden dan naar boven nodig — dat wordt vaak bereikt
door de servoarmen van de flaps 20–30° uit het neutraal te plaatsen in de
aansturing zelf, waardoor de flaps bij servo-neutraal ongeveer halverwege
naar beneden staan:

![Flaps omhoog](../assets/how-to-butterfly-mix-flaps-up.png)
![Flaps omlaag](../assets/how-to-butterfly-mix-flaps-down.png)

Stel het gewicht van de flapmix hoog in (bijvoorbeeld −180%) voor maximale
uitslag; de werkelijke fysieke uitslag wordt bepaald door Min/Max in
[Uitgangen](../model-setup/outputs.md).

!!! tip
    Om overbelasting van de servo's te voorkomen, begin met conservatieve
    Min/Max-waarden bij Uitgangen (bijvoorbeeld ±30%) en verruim deze
    voorzichtig tijdens de definitieve instelling, terwijl u let op
    klemmen.

## 6. Voeg een "Flaps Neutral" offsetmix toe

![Offsetmix van 80%](../assets/how-to-butterfly-offset-mix-80.png)

Omdat de verplaatste servoarmen ervoor zorgen dat de flaps bij servo-neutraal
~20–30% uitgeslagen staan, brengt een **Offset Mix** ze terug naar de
werkelijke neutraalstand van de vleugel voor normale vlucht. Begin met een
offset van 80% (nog af te stemmen), met 2 uitgangskanalen toegewezen aan
beide flapkanalen:

![Flaps omhoog met offset](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Flaps omlaag met offset](../assets/how-to-butterfly-offset-mix-flaps-down.png)

Controleer met de gasstick volledig omhoog (Butterfly-mix uit) dat de
mixerwaarden van de flaps op de offset (80%) staan; wanneer u de flapstick
naar volledig uitgeslagen beweegt, moet de mixeruitgang over het volledige
gewicht bewegen (bijvoorbeeld van 80% naar −100%, een verloop van 180%). Stem
de werkelijke uitslagbegrenzing fijn af bij Uitgangen via Min/Max of een
curve.

## 7. Voeg de hoogteroercompensatiecurve en -mix toe {: #7-add-the-elevator-compensation-curve-and-mix }

![Compensatiecurve](../assets/how-to-butterfly-comp-curve.png)
![Punten van de compensatiecurve](../assets/how-to-butterfly-comp-curve-points.png)

Omdat de benodigde compensatie niet lineair is, gebruikt u een curve in plaats
van een vast gewicht. Definieer een aangepaste 5-puntscurve (bijvoorbeeld
"EleComp") — in dit voorbeeld begint deze met 12%/10%/8%/5%/0% over de punten;
zonder een bekend startpunt voor uw model moeten deze waarden empirisch worden
bepaald.

Zet die curve vervolgens om in een waarde die als **Weight** van een mix
gebruikt kan worden: voeg een
[Vrije mix](../model-setup/mixes.md#mix-libraries) ("EleCompx") toe met
Throttle als bron en de EleComp-curve eraan gekoppeld, met uitvoer naar een
hoog, ongebruikt kanaal (bijvoorbeeld CH20):

![Compensatiemix op CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

Houd terug in de Butterfly-mix `ENT` lang ingedrukt op **Weight** van de
hoogteroeruitgang, kies **Use a source** en selecteer vervolgens CH20
(EleCompx) uit de categorie Channels:

![Hoogteroer met CH20 als bron](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Bron selecteren](../assets/how-to-butterfly-mix-ele-use-source.png)

De Butterfly-mix is nu volledig geconfigureerd:

![Hoogteroercompensatie geconfigureerd](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Controleren met View by Channel

![Weergave per kanaal](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Schakel over naar [Weergave per kanaal](../model-setup/mixes.md#per-channel-view)
op het hoogteroer om alle bijdragende mixen (stickinvoer +
butterflycompensatie) samen te zien meebewegen terwijl de gas-/remstick
beweegt — veel eenvoudiger om te debuggen dan de platte tabelweergave.

!!! tip
    Gegevens over de benodigde hoogteroeruitslag ten opzichte van de
    flapuitslag (van de fabrikant van het model of uit communitybronnen)
    zijn waardevol voordat u de startwaarden van de compensatiecurve
    instelt. Bij gebrek daaraan begint u met enkele millimeters
    hoogteroeruitslag per volledige flapuitslag en verfijnt u van daaruit.
