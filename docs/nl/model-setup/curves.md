---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Curves

![Curvetypen](../assets/model-curves-type.png)

Herbruikbare responscurves voor [Mixen](mixes.md#anatomy-of-a-mix) of
[Uitgangen](outputs.md#editing-a-channel) — de ingebouwde Expo is in beide
direct beschikbaar, maar alles wat verder gaat wordt hier gedefinieerd (of via
**Curve toevoegen**, direct bereikbaar vanuit beide bewerkschermen). Er zijn
maximaal 50 curves beschikbaar; standaard bestaat er geen enkele (Expo is
altijd ingebouwd, ongeacht dit). Voeg er een toe met **+**; tik op een
bestaande curve voor **Bewerken**/**Verplaatsen**/**Kopiëren-plakken**/**Klonen**/**Verwijderen**.

![Curve toevoegen](../assets/model-curves-add.png)

## Curvetypen

- **Expo** — standaardwaarde 40; positief maakt de respons rond het midden
  zachter, negatief maakt hem scherper. Een zachtere respons rond het
  middelpunt van de stick helpt overbesturing voorkomen, vooral bij minder
  ervaren piloten.

  ![Expo](../assets/model-curves-expo.png)

- **Function** — een kleine reeks vaste wiskundige vormen:

  ![Functietypen](../assets/model-curves-fn-types.png)

  - **x > 0** — geeft de bron ongewijzigd door zolang deze positief is;
    geeft 0 uit zolang deze negatief is.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — het spiegelbeeld: geeft door zolang negatief, 0 zolang
    positief.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — geeft de bron door als absolute waarde (altijd positief).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — geeft 100% uit zolang de bron positief is, en 0 zolang deze
    negatief is (een harde schakelaar, geen doorgifte).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — geeft −100% uit zolang negatief, 0 zolang positief.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — geeft −100% uit zolang negatief, +100% zolang positief.

    ![|f|](../assets/model-curves-fn-barf.png)

  Elk curvetype — Function inbegrepen — heeft ook een **Offset**, waarmee de
  curve op de Y-as omhoog of omlaag wordt verschoven (met één decimaal
  nauwkeurig, zoals bij Y-waarden in het algemeen):

  ![Function-offset](../assets/model-curves-fn-xgt0-offset.png)

- **Custom** — een curve op basis van punten, standaard 5 punten, maximaal 21.

  ![Custom curve met 5 punten](../assets/model-curves-custom5.png)

  - **Smooth** — laat een vloeiende curve door alle punten lopen in plaats
    van rechte segmenten ertussen.

    ![Vloeiende curve](../assets/model-curves-custom5-2-smooth.png)

  - **Easy mode** — **Aan** beperkt het bewerken tot gelijkmatig verdeelde
    Y-coördinaten (X staat vast); **Uit** maakt het mogelijk om per punt
    zowel X als Y te bewerken, behalve de eindpunten op −100%/+100%, die
    vergrendeld zijn omdat de curve altijd het volledige signaalbereik moet
    bestrijken.

    ![Easy mode uit](../assets/model-curves-custom-easy-off.png)

  **Bedieningselementen van de editor** (zelfde patroon als de [editor voor
  balanscurves bij Uitgangen](outputs.md#balance-channels)):

  - **Source** — standaard de eigen mixbron(nen) van de curve, of **Auto
    analog input** om de eerste bewogen stick/schuifregelaar/potentiometer
    over te nemen.
  - Vastklikken op het dichtstbijzijnde punt met de rotary-encoder, en een
    schakelaar **Lock** om ingangen te bevriezen terwijl u de resulterende
    beweging van het stuurvlak observeert.
  - Een live cursor toont de huidige ingangswaarde die de curve aanstuurt,
    om deze vóór het aanpassen op één lijn met een punt te brengen.

## Een curve aansturen vanuit een Var

Zowel de **Offset** van een Function-curve als een afzonderlijk punt van een
**Custom**-curve kan worden aangestuurd door een [Var](variables.md) in plaats
van door een vaste waarde — en die Var kan op zijn beurt tijdens de vlucht
worden aangepast via een hertoegewezen trim:

![Function-offset vanuit een Var](../assets/model-curves-fn-offset-var.png)
![Custom-curvepunt vanuit een Var](../assets/model-curves-custom-with-var.png)

Zie [Variabelen](variables.md) en [Handleiding: tijdens de vlucht instelbare
compensatiecurve](../how-to/in-flight-compensation-curve.md) voor een volledig
uitgewerkt voorbeeld van dit patroon.
