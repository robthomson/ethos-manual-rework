---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Logische schakelaars

![Menu logische schakelaars](../assets/model-lsw-menu.png)

Logische schakelaars zijn door de gebruiker geprogrammeerde *virtuele*
schakelaars — geen fysieke bedieningsorganen, maar overal inzetbaar waar
een fysieke schakelaar kan worden gebruikt, als trigger voor een
programma. Elke schakelaar beoordeelt de ingestelde voorwaarde aan de hand
van zijn ingangen (andere schakelaars, telemetriewaarden, mixwaarden,
timerwaarden, gyro-/trainerkanalen en meer) en wordt daarmee waar (True)
of onwaar (False). Er worden maximaal 100 ondersteund; standaard bestaat
er geen enkele. Voeg er een toe met **+**; het menulabel van een
gedefinieerde schakelaar is groen wanneer deze True is en rood wanneer
deze False is. Tik op een bestaande schakelaar voor
**Bewerken**/**Verplaatsen**/**Kopiëren-plakken**/**Klonen**/**Verwijderen**.

![Logische schakelaar toevoegen](../assets/model-lsw-add.png)

## Functie

Elke functie ondersteunt een normale of geïnverteerde uitgang.

- **A ~ X** — waar wanneer bron `A` *ongeveer* gelijk is (binnen circa
  10%) aan een vaste waarde `X`. Over het algemeen te verkiezen boven
  exacte gelijkheid —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — omdat bij `A = X` een telemetriewaarde die bijvoorbeeld schommelt
  tussen 8,5 V en 8,35 V rond een streefwaarde van 8,4 V eenvoudigweg
  nooit precies op 8,4 V uitkomt, waardoor de schakelaar nooit zou
  reageren.
- **A = X** — alleen waar wanneer `A` exact gelijk is aan `X`.
- **A > X** / **A < X** — waar wanneer `A` groter/kleiner is dan `X`.
- **|A| > X** / **|A| < X** — zoals hierboven, maar vergelijkt de
  absolute waarde van `A` (teken wordt genegeerd).
- **Δ > X** — waar wanneer de verandering van `A` (delta) binnen het
  **controle-interval** ten minste `X` bedraagt. Een interval van `---`
  betekent een oneindig venster.

  ![Delta groter dan X](../assets/model-lsw-delta-gtX.png)
  ![Absolute delta groter dan X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — zoals hierboven, met de absolute waarde van de
  verandering.
- **Bereik** — waar wanneer `A` binnen een opgegeven bereik valt.

  ![Bereik](../assets/model-lsw-range.png)

- **AND** — alleen waar als elke vermelde bron (Waarde 1…N) waar is.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — waar als ten minste één vermelde bron waar is.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (exclusieve OR) — waar als *precies één* vermelde bron waar is.

  ![XOR](../assets/model-lsw-XOR.png)

- **Timergenerator** — schakelt continu vrij aan/uit: aan gedurende
  **Duur actief**, uit gedurende **Duur inactief**.

  ![Timergenerator](../assets/model-lsw-timer-generator.png)

- **Sticky** — een vergrendeling (SR-flipflop); zie [hieronder](#sticky).
- **Edge** — een kortstondige impuls; zie [hieronder](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Vergrendelt op **True** zodra aan de voorwaarde **Trigger ON** is voldaan
en blijft True totdat aan **Trigger OFF** is voldaan — optioneel begrensd
door **Actieve voorwaarde** (zolang die False is, wordt de uitgang
ongeacht alles op False gehouden; de interne vergrendeling van Sticky
blijft op de achtergrond werken en wordt weer naar de uitgang
doorgeschakeld zodra de actieve voorwaarde weer True wordt, met
inachtneming van eventuele vertragingen).

Sinds Ethos 1.6.2 accepteren beide triggers een **Edge**-modifier (lang
indrukken van `ENT` op de triggervoorwaarde, dan Edge selecteren —
weergegeven met een voorvoegsel `†`) voor veel fijnere sturing:

![Sticky met edge](../assets/model-lsw-sticky-with-edge.png)
![Edge-optie selecteren](../assets/model-lsw-sticky-edge-select.png)

- **Trigger ON `SA` (geen vertraging)** — vergrendelt op True op het
  moment dat SA hoog wordt.
- **Trigger ON `SA` (vertraging = 1 s)** — vergrendelt op True 1 s nadat
  SA hoog is geworden, *mits* SA aan het einde van die seconde nog steeds
  hoog is.
- **Trigger ON `†SA` (vertraging = 1 s)** — vergrendelt van True→False
  1 s nadat SA hoog is geworden, **ongeacht** of SA op dat moment nog
  hoog is (de flank heeft al plaatsgevonden; de vertraging bepaalt enkel
  het tijdstip van het resultaat).

Trigger OFF werkt op dezelfde manier, maar omgekeerd. Vertragingen worden
**na** de actieve voorwaarde toegepast — een wijziging van de actieve
voorwaarde start de vertragingstiming dus opnieuw voordat de vergrendelde
waarde weer op de uitgang komt. Wanneer beide triggers gelijktijdig van
False→True gaan, wordt de uitgang van Sticky eenmaal **omgeschakeld**. Zie
ook [Gemeenschappelijke parameters](#shared-parameters) hieronder.

### Edge

![Edge](../assets/model-lsw-edge.png)

Een kortstondige impuls: True gedurende **Duur**, zodra aan de
triggervoorwaarde is voldaan. **Tijdens** is een paar `[t1:t2]` dat
precies bepaalt wanneer:

- **Opgaande flank, Tijdens = 0,0 s** — reageert op het moment dat
  Trigger ON van False→True gaat.

  ![Opgaande flank](../assets/model-lsw-edge-rising-edge.png)
  ![Tijdens = 0](../assets/model-lsw-edge-during-eq0.png)

- **Opgaande flank, Tijdens ≥ 0,0 s (bijv. 5,0 s)** — reageert 5 s nadat
  Trigger ON True is geworden, waarbij kortere "pieken" binnen dat venster
  van 5 s worden genegeerd.

  ![Tijdens > 0, opgaande flank](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![Tijdens > 0](../assets/model-lsw-edge-during-gt0.png)

- **Neergaande flank, Tijdens = 0,0 s** — reageert op het moment dat
  Trigger ON van True→False gaat.
- **Neergaande flank, Tijdens ≥ 0,0 s (bijv. 3,0 s)** — reageert bij de
  overgang True→False, maar alleen als de toestand eerst ten minste 3 s
  True was.
- **Impuls (zowel t1 als t2 ingesteld)** — reageert alleen als Trigger ON
  binnen dat venster van False→True→False gaat (bijv. tussen 2 s en 5 s
  later).

## Gemeenschappelijke parameters {: #shared-parameters }

![Gemeenschappelijke parameters](../assets/model-lsw-common-parameters.png)

- **Actieve voorwaarde** — begrenst de uitgang van de schakelaar op
  dezelfde manier als bij Sticky hierboven. Opties: Altijd aan,
  standen van schakelaar/functieschakelaar/logische schakelaar/trim,
  Telemetrie, Vluchtmodi of een systeemgebeurtenis (Gas vasthouden,
  Gas-afsnijding, Gas actief, Telemetrie actief, RSSI laag, Trainer
  actief, Vlucht-reset).
- **Vertraging voor actief** / **Vertraging voor inactief** — hoelang de
  voorwaarde True (of False) moet blijven voordat de uitgang volgt, tot
  60 s. Niet van toepassing op Timergenerator of Edge. (Zie
  [Handleiding: Waarschuwing accucapaciteit](../how-to/battery-capacity-warning.md)
  voor een vertraging die wordt gebruikt om een spanningsdip te
  ontdenderen.)
- **Bevestiging voor actief** / **inactief** — vraagt de gebruiker om
  bevestiging voordat de toestand daadwerkelijk verandert (met een optie
  Annuleren, voor gevallen waarin de schakelaar te vaak reageert om
  bruikbaar te zijn) — handig om iets risicovols te begrenzen, bijv. een
  bevestiging voordat een grondvoertuig op afstand wordt uitgeschakeld.

  ![True bevestigen](../assets/model-lsw-confirm-lsw-true.png)
  ![False bevestigen](../assets/model-lsw-confirm-lsw-false.png)

- **Min. duur** — zodra True, blijft de schakelaar ten minste zo lang
  True. Als deze op `---` blijft staan, kan de uitgang slechts één
  mixercyclus True zijn — te kort om de regel in de gebruikersinterface
  zelfs maar vet te zien worden.
- **Max. duur** — zodra True, gaat de schakelaar na deze tijd automatisch
  terug naar False, indien nog steeds ingesteld. Beide duren gaan tot
  60 s.
- **Opmerking** — vrije tekst, weergegeven overal waar deze schakelaar aan
  een waardewidget wordt toegevoegd, om het doel te documenteren.

## Gebruik met telemetrie

Een systeemgebeurtenis **Telemetrie actief** (of een schakelaar waarvan de
bron een telemetriesensor is, die alleen actief is zolang die sensor
gegevens rapporteert) dekt voorwaarden van het type "wordt er momenteel
telemetrie ontvangen".

!!! warning
    Een [mix](mixes.md) die door een op telemetrie gebaseerde logische
    schakelaar wordt begrensd, heeft een **tweede** mixactie nodig met
    dezelfde schakelaar **geïnverteerd**, zodat de mix nog een geldige
    waarde heeft zodra de telemetrie wegvalt — bedenk dat een inactieve
    mix neutraal uitvoert (0% / 1500 µs, of **halfgas** op een gaskanaal).
    Gebruik als alternatief een **Offset**-actie, die al ingebouwde
    afzonderlijke waarden voor actief/inactief heeft — bijv. bron **0**
    (de speciale waarde) met de offset zo ingesteld dat de mix +100%
    aangeeft zolang `LS3` actief is en −100% zolang deze inactief is,
    waarmee beide gevallen in één actie worden gedekt.

## Vergelijking van bronnen

Een bron wordt normaal gesproken vergeleken met een vaste waarde, maar in
plaats daarvan kunnen ook twee bronnen van *hetzelfde* type direct met
elkaar worden vergeleken — bijv. twee timers, twee spanningen of twee
RPM-sensoren.

## Trainer-ingang van slave negeren

![Trainer-ingang negeren](../assets/model-lsw-ignore-trainer-input.png)

De [opties](../getting-started/user-interface-and-navigation.md#choosing-a-source)
van een bron kunnen de trainer-ingang van een aangesloten leerling-zender
(slave) uitsluiten — dit wordt doorgaans gebruikt bij een logische
schakelaar die de stickbeweging van de **master** zelf bewaakt (bijv. om
onmiddellijk in te grijpen als er iets misgaat), zonder dat de ingangen
van de leerling deze eveneens activeren. Vaak gecombineerd met een
trainerschakelaar die de actieve voorwaarde van de master zelf begrenst.
