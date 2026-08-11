---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Variabelen

![Variabelen](../assets/model-vars.png)

Variabelen ("Vars") zijn benoemde containers voor de eigen
instellingswaarden van een model, die overal elders in de programmering
kunnen worden aangeroepen — inclusief [mixen](mixes.md). Door ze in een
eigen sectie te bewaren, wordt de *configuratiedata* van een model
gescheiden van de *programmeerlogica*: in plaats van tientallen mixen door
te zoeken om een waarde te vinden en aan te passen, staat alles op één
plek onder een betekenisvolle naam. Er zijn 64 Vars beschikbaar; standaard
bestaat er geen enkele. Voeg er een toe met **+**; tik op een bestaande
Var voor **Bewerken**/**Verplaatsen**/**Kopiëren**/**Klonen**/
**Verwijderen**.

![Variabele toevoegen](../assets/model-vars-add.png)

Een Var kan een vaste constante bevatten, of instelbaar zijn binnen
door de gebruiker gedefinieerde grenzen (om te voorkomen dat verkeerde
waarden een crash veroorzaken), en kan per actieve conditie (bijv. per
vluchtmodus) een *andere* waarde bevatten. Waarden blijven bewaard tussen
sessies. Een Var kan elke gewone numerieke waarde vervangen op elke plek
waar de [Options-functie](../getting-started/user-interface-and-navigation.md#the-options-feature)
beschikbaar is (de velden met het hamburgerpictogram).

!!! example
    Een zwever met gedeelde rolroeren (waarvan de binnenste secties
    tevens als landingskleppen dienen) heeft één gedeelde instelling voor
    rolroerdifferentieel nodig die overal wordt gebruikt waar alle vier
    de roervlakken als rolroer werken — een Var met die ene waarde,
    aangeroepen vanuit elke betreffende mix, houdt het consistent en
    betekent dat de waarde maar op één plek afgestemd hoeft te worden.

## Een Var toevoegen

![Nieuwe variabele](../assets/model-vars-new_var.png)

- **Value** — huidige waarde (alleen-lezen weergave).
- **Name** — aanpasbaar.
- **Comment** — vrije tekst die het doel toelicht.
- **Range** — onder-/bovengrens (één decimaal, binnen ±500%) die de waarde
  van de Var nooit kan overschrijden.

### Waarden

![Waarden van variabele](../assets/model-vars-values.png)

- **Fixed** — één enkele constante, met één decimaal.
- **Multiple/variable** — **Add new value** koppelt een waarde per actieve
  conditie. Zo geeft `Var12` 9% zolang vluchtmodus Thermal (FM4) actief
  is, en −3% zolang Speed (FM5) actief is, met een Range beperkt tot
  −10%…+15% zodat geen van beide zinvolle grenzen kan overschrijden:

  ![Vluchtmodusafhankelijke waarden](../assets/model-vars-fm-dependent.png)
  ![Een waarde toevoegen](../assets/model-vars-add-value.png)

### Acties

![Acties van variabele](../assets/model-vars-actions.png)
![Actie toevoegen](../assets/model-vars-add-action.png)

Acties wijzigen de waarde van een Var in de loop van de tijd, aangedreven
door een ingang.

**Hergebruikte trim** — draagt een van de fysieke trims over aan het
instellen van deze Var in plaats van de normale functie, doorgaans beperkt
tot één actieve conditie:

![Een trim hergebruiken](../assets/model-vars-functions-repurpose.png)
![Te hergebruiken trim selecteren](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Gebruik de gastrim om een Var voor camber-compensatie in te stellen,
    maar alleen zolang vluchtmodus Landing (FM3) actief is, met Range
    0–25% en een stap van 1,0% per klik. Buiten die actieve conditie
    valt de trim automatisch terug op zijn gewone functie.

**Rekenkundige acties** — aangedreven door elke willekeurige ingang:

- **Assign** — zet de Var op een specifieke waarde.
- **Add** / **Subtract** / **Multiply** / **Divide** — rekenkundige
  bewerking op de huidige waarde.
- **Percentage** — past een percentage van de aandrijvende ingang toe.
- **Min** / **Max** — begrenst de Var ten opzichte van de aandrijvende
  ingang.

  ![Functieacties](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` kent direct 40% toe aan een Var; `FS1(edge)` telt er bij
    elke druk 2 bij op (begrensd op het maximum van de Range);
    `FS2(edge)` trekt er bij elke druk 2 van af (begrensd op het minimum
    van de Range). De optie **Edge** (lang indrukken van de
    functieschakelaar) is hier van belang — zonder deze optie zou de
    actie continu opnieuw worden uitgevoerd zolang de schakelaar
    ingedrukt blijft, in plaats van eenmaal per druk.

  ![Uitgewerkt voorbeeld](../assets/model-vars-calc-example.png)
