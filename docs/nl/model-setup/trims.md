---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trims

![Trims](../assets/model-trims.png)

Hier configureer je voor elke stick het trimbereik, de stapgrootte en het
gedrag, plus cross trim en instant trim. De **X20 Pro/R/RS** en de **X18**
hebben twee extra trimschakelaars, **T5**/**T6**, die handig zijn voor
aanpassingen tijdens de vlucht buiten de vier hoofdsticks om:

![T5/T6-trims](../assets/model-trims-pro-t5-t6.png)

Elke stick heeft zijn eigen onafhankelijke set trim-instellingen.

## Trim-instellingen {: #trim-settings }

- **Range** — standaard ±25%, instelbaar tot het volledige bereik van de
  stick van ±100%. Op het hoofddisplay loopt een trim met standaardbereik
  van −100 tot 100; een trim met volledig bereik (100%) loopt van −400 tot
  400 (4× het normale bereik).

  !!! warning
      Een groter bereik betekent dat te lang op een trimschakelaar drukken
      genoeg trim kan toevoegen om het model onvliegbaar te maken.

- **Step** — de fijnheid van de trimschakelaar: **Extra fine**, **Fine**,
  **Medium**, **Coarse**, **Exponential** (fijn rond het midden, grover
  naar de uiteinden) of **Custom** (een specifiek percentage per klik).

  ![Stapopties](../assets/model-trims-step-options.png)

  | Step | µs per klik (bereik 25%) |
  |---|---|
  | Extra fine | 0,5 |
  | Fine | 1 |
  | Medium | 2 |
  | Coarse | 4 |
  | Exponential | 0,3–16 |

  Custom, bij een bereik van 25%: stap van 1% = 1 µs/klik, stap van 100% =
  128 µs/klik. Bij een bereik van 100%: stap van 1% = 5 µs/klik, stap van
  100% = 512 µs/klik.

## Modus

![Trimmodus hoogteroer](../assets/model-trims-mode-elevator.png)

Standaard is een trim altijd actief, maar met **Mode** verander je dat
gedrag. Bij het wijzigen van de modus wordt de trim op 0 gezet.

- **OFF** — schakelt de trim volledig uit.

  ![Modus: off](../assets/model-trims-mode-option-off.png)

  Nuttig bij bijvoorbeeld een elektromodel dat geen gastrim nodig heeft —
  de vrijgekomen trimschakelaar kan dan [worden hergebruikt om een Var aan
  te passen](variables.md).

- **Easy** — één gedeelde trimwaarde voor alle vluchtmodi. De gebruikelijke
  keuze voor rolroer en richtingsroer, omdat die zelden per vluchtmodus
  hoeven te verschillen.

  ![Modus: easy](../assets/model-trims-mode-option-easy.png)

- **Independent per flight mode** — de trim werkt alleen op de actieve
  vluchtmodus. De gebruikelijke keuze voor de hoogteroertrim, omdat die
  vaak per vluchtmodus moet verschillen (bijv. bij wijzigingen van de
  vleugelwelving) — in feite is dit vaak de belangrijkste reden om
  vluchtmodi in te stellen.

  ![Modus: onafhankelijk per vluchtmodus](../assets/model-trims-mode-option-fm.png)

- **Custom** — volledig aangepast gedrag, opgebouwd uit **behaviors** die
  je zelf toevoegt.

### Aangepaste trimgedragingen

![Een gedrag toevoegen](../assets/model-trims-mode-elevator-add-behaviour.png)
![Gedragsopties](../assets/model-trims-mode-elevator-edit-behaviour.png)

Elke gedragsregel heeft een voorwaarde en één van de volgende opties:

- **Unplugged** — schakelt de trim selectief uit onder deze voorwaarde (in
  plaats van hem volledig uit te zetten met Mode = OFF).

  ![Unplugged](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Voorwaarde voor unplugged](../assets/model-trims-mode-unplugged-select.png)

- **Normal** (standaard) — normaal trimgedrag.
- **Equal (to another trim)** — deze trim volgt de trimwaarde van een
  andere voorwaarde exact.

  ![Equal](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Offset + (another trim)** — deze trim wordt bovenop de trimwaarde van
  een andere voorwaarde opgeteld.

  ![Offset](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Uitgewerkt voorbeeld** — een zweefvliegtuig met een basis-hoogteroertrim
in **Cruise** en afhankelijke trims voor **Speed** en **Thermal**:

![FM5 Speed selecteren](../assets/model-trims-mode-elevator-custom-select.png)
![FM4 Thermal selecteren](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Trim voor horizontale vlucht in de standaardmodus (Cruise).
2. Voeg een gedrag toe: **Offset + Default**, voorwaarde `FM5(Speed)`. Elke
   trimaanpassing in de Speed-modus wordt nu opgeslagen als een offset
   bovenop de basiswaarde van Cruise — apart, maar nog steeds daarvan
   afhankelijk.

   ![Offset voor Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Voeg op dezelfde manier een tweede gedrag toe: **Offset + Default**,
   voorwaarde `FM4(Thermal)`. (Zodra het eerste gedrag bestaat, biedt het
   dialoogvenster ook `Equal FM5(Speed)` en `Offset + FM5(Thermal)` aan,
   omdat het nu ook naar dat gedrag kan verwijzen.)

   ![Offset voor Speed en Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Met deze opzet verschuift het later aanpassen van de basis-Cruise-trim
(bijvoorbeeld na een wijziging van het zwaartepunt) de trims van Speed en
Thermal automatisch met hetzelfde bedrag, omdat het offsets daarbovenop
zijn en geen onafhankelijke waarden.

- **Audio** — schakel de standaard trimmelding uit voor een hergebruikte
  trim wanneer het niet langer zinvol is die te horen.

## Extra trims

![Extra trim toevoegen](../assets/model-trims-add-trim-select.png)
![Instellingen extra trim](../assets/model-trims-add-trim-edit.png)

Met **Add an extra trim** maak je een trim buiten de vier standaardsticks
(en T5/T6) om: **Name**, de bronnen **Up**/**Down** die hem aandrijven,
plus dezelfde opties **Range**, **Step**, **Mode** en **Audio** als
hierboven.

## Kruistrim

![Cross trim](../assets/model-trims-cross.png)
![Cross trim bewerken](../assets/model-trims-cross-edit.png)

Hier bepaal je welke trimschakelaar elke stick daadwerkelijk bijstelt —
oftewel: je laat de trim van een stick aansturen door een andere fysieke
trimschakelaar dan gebruikelijk. (T5/T6 zijn alleen beschikbaar op de
X20 Pro en de X18.)

## Instant trim {: #instant-trim }

![Instant trim](../assets/model-trims-instant-trim.png)

Zolang deze functie actief is, worden de huidige stickposities opgeteld bij
de bijbehorende standaardtrims (en kruistrims). Wijs hem het beste toe aan
een schakelaar die je kunt bereiken zonder de sticks los te laten — activeer
hem tijdens rechte, horizontale vlucht om de trims direct in te stellen, in
plaats van herhaaldelijk op een trimschakelaar te drukken wanneer de trims
er ver naast zitten. Schakel de functie na de trimvlucht weer uit om te
voorkomen dat je de trims later per ongeluk verstoort.

!!! note
    Instant trim is alleen actief zolang je een van de hoofdweergaven
    bekijkt.

## Trims naar subtrims verplaatsen

![Trims naar subtrims verplaatsen](../assets/model-trims-move-trims-to-subtrims.png)

Nadat je hebt uitgetrimd voor horizontale vlucht, verplaatst deze functie de
trimwaarde van een kanaal (bijv. hoogteroer) naar de bijbehorende
[Subtrim](outputs.md)-instelling en zet de trim op het scherm terug op nul —
een nette manier om te controleren of de vliegtrims sindsdien niet zijn
verlopen.

Bij gebruik van vluchtmodi kan een kanaal meer dan één relevante trimwaarde
hebben, terwijl Subtrim in Outputs één globale instelling is die voor alle
vluchtmodi geldt. Deze functie houdt daar rekening mee: de trim van de
**momenteel geselecteerde** vluchtmodus wordt naar Subtrim verplaatst, die
trim wordt gereset en de trim van elke *andere* vluchtmodus op hetzelfde
kanaal wordt ter compensatie aangepast — zodat de werkelijke roerstand in
elke vluchtmodus per saldo ongewijzigd blijft.

!!! tip
    Voer dit voor de consistentie altijd uit vanuit dezelfde
    "basis"-vluchtmodus (bijv. Cruise bij een zweefvliegtuig) — zolang je dat
    doet, kun je het veilig herhalen.

Grote trim- of subtrimwaarden leiden tot zeer asymmetrische roeruitslagen —
het is beter om de oorzaak mechanisch op te lossen. Streef naar
stangenstelsels onder 90° wanneer de roeren neutraal staan (met uitzondering
van flaps, waarbij je wat opwaartse slag inruilt voor meer neerwaartse slag)
en gebruik daarna **PWM center** om exact op 90° af te stemmen zodra het
stangenstelsel er dicht bij zit.
