---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Basisvoorbeeld vliegende vleugel (elevon)

Een vliegende vleugel met 2 servo's in elevon-configuratie, met de door
Dreamflight aanbevolen rates/Expo/mixverhoudingen van de Weasel als concreet
uitgewerkt voorbeeld. Voltooi eerst de [initiële
zenderinstelling](initial-radio-setup.md).

## Stap 1. Systeeminstellingen controleren {: #step-1-confirm-system-settings }

Standaard **AETR**-volgorde, met **[Eerste vier kanalen
vast](../system-setup/controls.md#first-four-channels-fixed)** **UIT**.
Registreer (bij ACCESS) en bind de ontvanger via
[RF-systeem](../model-setup/rf-system.md) voordat u verdergaat.

## Stap 2. Bepaal de benodigde servo's/kanalen

Bij een elevon-vliegtuig combineren [mixen](../model-setup/mixes.md) de
invoer van rolroer en hoogteroer op beide fysieke roervlakken — in totaal
slechts 2 kanalen, elk een combinatie van beide invoeren.

## Stap 3. Een nieuw model aanmaken

![Vliegtuigmodel aanmaken](../assets/tut-wing-eg-wiz-create-airplane.png)

Start vanuit [Modelkeuze](../model-setup/model-select.md) de wizard
**Airplane** en kies **Non stabilized receiver**.

![Geen motor](../assets/tut-wing-eg-wiz-no-engine.png)

Selecteer **No engine**, accepteer de standaard 2 rolroerkanalen en
selecteer **No flaps**.

![Geen staart](../assets/tut-wing-eg-wiz-no-tail.png)

Selecteer **None** als staarttype — dit is wat Ethos ertoe aanzet de
elevon-mix automatisch op te bouwen (invoer van rolroer + hoogteroer, beide
op dezelfde twee kanalen). Geef het model een naam (bijv. "Weasel"), kies
een bitmap en rond af — het wordt het actieve model in de categorie Airplane.

## Stap 4. De mixen bekijken en configureren

![Overzicht mixen](../assets/tut-wing-eg-mixes.png)

De wizard maakt een mix Ailerons op kanalen 1+2, gevolgd door een mix
Elevators *ook* op kanalen 1+2 — beide invoeren werken op beide
elevon-kanalen, en dat is precies de kern van elevon-mixen.

### Rolroeren

![Rolroermix](../assets/tut-wing-eg-mixes-ail-mix.png)

**Weight/Rates** — volgens de handleiding van de Weasel moet de
rolroeruitslag ongeveer 3× die van het hoogteroer zijn, en samen moeten ze
100% vormen: **75%** rolroer, **25%** hoogteroer. Low rates zijn ongeveer de
helft van high rates: **36%** rolroer low, **12%** hoogteroer low.

![Weight van rolroermix](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — door de Weasel aanbevolen 35% high / 20% low, actief bij
schakelaar SB omlaag, waardoor de reactie rond de middenstand van de stick
vlakker wordt.

**Differentieel** — klein op dit toestel, ongeveer **4%**:

![Rolroerdifferentieel](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Zie [Basisvoorbeeld vliegtuig met vaste
vleugel](basic-fixed-wing.md#ailerons) voor de reden waarom differentieel van
belang is — dezelfde redenering over negatief gierkoppel geldt hier.)

### Hoogteroer

![Hoogteroermix](../assets/tut-wing-eg-mixes-ele-mix.png)

Hetzelfde patroon: **25%**/**12%** high/low rates, dezelfde Expo-waarden als
bij het rolroer.

### Richtingsroer

![Richtingsroermix](../assets/tut-wing-eg-mixes-rud-mix.png)

De Weasel heeft er geen — vliegende vleugels hebben er over het algemeen geen
nodig. Wanneer op een elevon-model *wel* een richtingsroer nodig is, voeg het
dan toe als [vrije mix](../model-setup/mixes.md#mix-libraries) op kanaal 3.

## Stap 5. De ontvanger binden

Zoals in [stap 1](#step-1-confirm-system-settings) — registreer/bind voordat
u verdergaat, en overweeg de servostangen los te koppelen of de uitslag te
beperken totdat de Min/Max-grenzen zijn ingesteld, om te voorkomen dat iets
overbelast wordt.

## Stap 6. De mixen nalopen

Uitgangskanalen 1/2 kunnen worden hernoemd naar **Elevon1**/**Elevon2**. Bij
volledige rolroeruitslag naar rechts geeft kanaal 1 (rechts, omhoog) 75% aan,
terwijl kanaal 2 (links, omlaag) 72% aangeeft — het verschil van 3% *is* het
differentieel in werking. Voeg daar volledig hoogteroer omlaag aan toe en
kanaal 1 wordt 75+25 = 100%, kanaal 2 wordt 72−25 = 47%.

## Stap 7. De maximale servo-uitslagen instellen

![Volledig rolroer](../assets/tut-wing-eg-outputs-full-ail.png)
![Volledig rolroer + volledig hoogteroer](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Centreer eerst elke servo met **PWM center**. De door de Weasel aanbevolen
maximale uitslag is 25 mm rolroer + 10 mm hoogteroer = 35 mm gecombineerd —
geef zowel volledig meewerkende *als* volledig tegenwerkende invoer van
rolroer/hoogteroer en controleer of geen van beide de mechanische of
servogrenzen overschrijdt voordat u de definitieve uitslagen instelt.

- **Min/Max** — harde grenzen die nooit worden overschreven; verlagen ervan
  vermindert de uitslag in plaats van deze af te kappen. Standaard ±100%,
  indien nodig uit te breiden tot ±150%.
- **Curve** — vaak sneller en flexibeler dan direct met Min/Max/Subtrim
  goochelen, met het voordeel van een live grafiek. Een 3-punts curve is
  geschikt voor de meeste uitgangen; een 5-punts curve op de tweede elevon
  maakt het eenvoudig om de uitslag op 5 punten te synchroniseren met de
  eerste. Laat bij gebruik van een curve hiervoor Min/Max/Subtrim op hun
  doorlaatwaarden staan (−100/100/0, of −150/150/0 bij uitgebreide grenzen) en
  laat de curve de vormgeving doen.
