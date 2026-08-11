---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# In-flight instelbare compensatiecurve

## Waarom

Het uitslaan van de flaps verandert de welving van de vleugel — hoogdekkers hebben de neiging om "op te ballonneren", laagdekkers om te zakken — waardoor een hoogteroercorrectie nodig is die niet lineair verloopt met de flapuitslag, dus een curve in plaats van een vaste offset. Deze uitleg gebruikt [Vars](../model-setup/variables.md) om de punten van een compensatiecurve **tijdens de vlucht** instelbaar te maken, via een hergebruikte gastrim, afhankelijk van welk curvepunt zich het dichtst bij de huidige stand van de flapstick bevindt — voortbouwend op de stap voor hoogteroercompensatie uit [Handleiding: Butterfly-mixer](butterfly-mixer.md).

## 1. Kies het curvetype

Een [custom curve](../model-setup/curves.md) met 5 punten is voldoende voor een vloeiende compensatie zonder overbodige complexiteit. Punt 5 (uiterst rechts, flapstick volledig omhoog / geen flaps) staat altijd vast op nul — zonder uitgeslagen flaps is geen compensatie nodig. De andere 4 punten worden instelbaar gemaakt via Vars. Omdat de flapstick vaak tussen twee gedefinieerde punten zal staan, moeten in die overlapzone beide punten aan weerszijden gelijktijdig instelbaar zijn.

## 2. Bereken de overlappende bereiken

Bereiken van punt tot punt (met toestemming overgenomen van Mike Shellims "Crow-aware adaptive elevator trim" voor OpenTX op rc-soar.com — licht uitgebreid zodat het bereik van Pt2 helemaal tot +100% reikt, om de reden die in [Stap 6](#6-apply-the-curve) wordt uitgelegd):

| Bereik flapstick | Actief(ve) punt(en) |
|---|---|
| +100% tot +45% | alleen Pt2 |
| +45% tot +20% | Pt2 en Pt3 |
| +20% tot −20% | alleen Pt3 |
| −20% tot −45% | Pt3 en Pt4 |
| −45% tot −90% | alleen Pt4 |
| −90% tot −100% | alleen Pt5 |

## 3. Configureer de logische schakelaars

![Logische schakelaars voor adaptieve punten](../assets/how-in-flight-comp-lsws.png)

Vier [logische schakelaars](../model-setup/logical-switches.md), elk met **Range** op de flapstick (gasstick), actief zolang de stick zich in de zone van dat punt bevindt:

- `AdaptivePt2` — bereik 20% tot 100% (specifiek uitgebreid tot 100% zodat Pt2 ook zonder uitgeslagen flaps kan worden bijgesteld — zie Stap 6).

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` — bereik −45% tot 45%.

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` — bereik −90% tot −20%.

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` — bereik −100% tot −90%.

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. Definieer de Vars voor de bijstelling

![Overzicht van de Vars](../assets/how-in-flight-comp-vars.png)

Vier [Vars](../model-setup/variables.md), `VAdjPt2`–`VAdjPt5`, elk met bereik 0–50% (verruim indien nodig) en een **hergebruikte gastrim** als actie — stapgrootte 1,0%, met de bijbehorende logische schakelaar als actieve voorwaarde:

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![Actie VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![Actie VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![Actie VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![Actie VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5-2.png)

Omdat er telkens slechts één logische schakelaar actief is (maximaal twee, in de overlapzones), stelt dezelfde fysieke trim veilig verschillende Vars bij, afhankelijk van de flapstand.

## 5. Definieer de compensatiecurve

![Compensatiecurve](../assets/how-in-flight-comp-var-comp-curve.png)
![Punten van de compensatiecurve](../assets/how-in-flight-comp-var-comp-curve-pts.png)

Een nieuwe custom curve met 5 punten (bijv. "EleComp") met **Smooth** ingeschakeld. Houd `ENT` lang ingedrukt op de punten 1–4 en kies **Use a source** om respectievelijk `VAdjPt5`…`VAdjPt2` toe te wijzen (punt 5 blijft vast op 0, volgens Stap 1).

## 6. Pas de curve toe {: #6-apply-the-curve }

Gebruik deze curve exact daar waar [Handleiding: Butterfly-mixer](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix) zijn EleComp-curve aan de mix voor hoogteroercompensatie koppelt.

Ga waar mogelijk uit van reële gegevens (aanwijzingen van de fabrikant, berichten uit de community) over hoeveel hoogteroeruitslag een bepaalde flapuitslag vereist; anders is enkele millimeters compensatie bij volledig uitgeslagen flaps een redelijk uitgangspunt.

!!! tip "Aanpak voor het afstemmen"
    Begin met kleine flapuitslagen en kleine trimcorrecties. `AdaptivePt2` kan worden afgestemd **zonder enige uitgeslagen flaps** — zet een beetje flap, haal die weer weg en voeg telkens een klein beetje compensatie toe, in plaats van te vechten tegen een ballonnerend of zakkend model terwijl je onder druk probeert te trimmen. Zet opnieuw een beetje flap om te controleren en stel indien nodig verder bij. Zodra Pt2 goed voelt, ga je naar het volgende punt rond de middenstand van de stick — als Pt2 een grote trimwijziging nodig had, is het de moeite waard om te landen en de resterende punten elk iets groter dan het vorige in te stellen, in plaats van blind te gokken.
