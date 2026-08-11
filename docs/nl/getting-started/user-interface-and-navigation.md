---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Gebruikersinterface & navigatie

Ethos kan volledig worden bediend met de rechter **rotary encoder** (draaien
om de markering te verplaatsen, indrukken voor `ENT`) en de `RTN`-toets om een
menu te verlaten — het touchscreen, waar aanwezig, is een snelkoppeling voor
dezelfde acties en geen afzonderlijke manier van werken. `MDL`, `DISP` en `SYS`
springen direct naar respectievelijk Modelinstellingen, Schermen configureren
en Systeeminstellingen (dezelfde drie tegels als in de onderste balk); een lange
druk op `RTN` brengt u vanaf elke plek direct terug naar het startscherm.

## Het reset-menu

![Contextmenu](../assets/resetmenu.png)

Een lange druk op `ENT` vanuit het startscherm opent een reset-menu:

- **Reset flight** — reset telemetrie, timers en functieschakelaars, en
  doorloopt opnieuw de [checklist](../model-setup/checklist.md) vóór de vlucht.
- **Reset telemetry** — reset alleen de telemetrie.
- **Reset timers** — reset alleen de timers.
- **Lock touchscreen** — ook bereikbaar door `ENT` + `PAGE` gedurende één
  seconde samen in te drukken vanuit het startscherm, of als trigger van een
  [speciale functie](../model-setup/special-functions.md).

## Bedieningselementen voor bewerken

**Functionele elementen toevoegen** — een timer, logische schakelaar, speciale
functie, curve of variabele wordt aangemaakt door op de **+** naast de
kolomkoppen in het betreffende menu te tikken. Op een zender zonder touchscreen
markeert u een bestaand element, drukt u op `ENT` en kiest u **Add** in het
menu — deze optie is ook beschikbaar op zenders met touchscreen.

### Virtueel toetsenbord

![Teksttoetsenbord](../assets/keyboard-text-azerty.png)

Door een tekstveld aan te raken (of erop `ENT` te drukken) opent het
schermtoetsenbord. De backspace-toets wist links van de cursor; `PAGE` wist
naar rechts, en zodra de cursor het einde van de tekst bereikt, gaat het wissen
verder vanaf links. Door het veld zelf aan te raken plaatst u de cursor op die
positie — of gebruik `SYS`/`DISP` om deze zonder touchscreen naar links/rechts
te verplaatsen. De toets **?123**/**abc** schakelt naar het numerieke
toetsenblok (dat ook speciale tekens bevat):

![Numeriek toetsenbord](../assets/keyboard-text-numbers.png)

Op een **zender zonder touchscreen** komt u door op een tekstveld op `ENT` te
drukken direct in de bewerkingsmodus: draai de encoder om door kleine letters,
hoofdletters, cijfers en vervolgens speciale tekens te scrollen, en druk op
`ENT` om elk teken in te voegen. `MDL` wisselt tussen hoofd- en kleine letter
van het teken direct rechts van de cursor (en elk daarna getypt teken blijft in
die schrijfwijze tot er opnieuw wordt gewisseld). `PAGE` wist rechts van de
cursor; `SYS`/`DISP` verplaatsen deze naar links/rechts.

## Bedieningselementen voor numerieke waarden

![Numerieke invoer](../assets/keyboard-numbers.png)

Door een numeriek veld aan te raken opent een bedieningsbalk onderaan het
scherm: **`<`**/**`>`** wijzigen de stapgrootte (in decaden — bijvoorbeeld
0,01/0,1/1,0/10,0), **`-`**/**`+`** (of de rotary encoder) passen de waarde met
die stap aan, en **More** opent verdere opties:

![Opties voor numerieke invoer](../assets/keyboard-numbers-options.png)

- Naar de standaardwaarde van het veld springen
- Op minimum / op maximum instellen
- De stapregelaar vervangen door een **schuifregelaar**

![Invoer met schuifregelaar](../assets/keyboard-numbers-slider.png)

De schuifregelaar (ook met de rotary encoder verstelbaar) is sneller voor grove
wijzigingen; **Disable slider** keert terug naar de stapregelaar. Telemetrische
bereikwaarden worden op dezelfde manier bewerkt:

![Schuifregelaar uitgeschakeld](../assets/keyboard-numbers-options-disable-slider.png)

## De Options-functie {: #the-options-feature }

Vrijwel overal waar een waarde of [bron](#choosing-a-source) wordt verwacht,
opent een lange druk op `ENT` een **Options**-dialoog — het kleine menu-icoon
("hamburger") in de linkerbovenhoek van een veld geeft aan dat dit beschikbaar
is.

### Waarde-opties

![Bronopties](../assets/source-with-options.png)

De dialoog met waarde-opties noemt de parameter die wordt bewerkt en biedt de
keuze tussen een vast minimum/maximum of het aansturen ervan door een **bron**
(bijvoorbeeld een potentiometer, om de waarde tijdens de vlucht aan te passen).
Als het veld al een bron gebruikt, biedt dezelfde lange druk in plaats daarvan
aan om de huidige waarde van die bron om te zetten in een vaste waarde:

![Bron omzetten naar waarde](../assets/source-convert-to-value.png)

### Een bron kiezen {: #choosing-a-source }

Met **Choose a source** opent een keuzelijst met twee kolommen — eerst een
**categorie** (analoge ingangen, schakelaars, logische schakelaars, trims,
kanalen, een gyro-as, een trainerkanaal, een timer, een telemetriesensor of een
aantal speciale waarden), daarna het specifieke element daaruit:

![Bronmenu](../assets/source-menu.png)

Zodra een bron is ingesteld, opent dezelfde lange druk opties die specifiek zijn
voor het soort bron:

**Elke bron** —

- **Invert** — inverteert de bron (bijvoorbeeld actief wanneer een schakelaar
  *niet* omhoog staat, in plaats van wanneer dat wel zo is).
- **Edge** — schakelt eenmalig bij een overgang (false→true of true→false) in
  plaats van actief te blijven gedurende de hele toestand; wordt met een
  `†`-voorvoegsel bij de bron weergegeven. Beschikbaar bij schakelaars in het
  algemeen, en specifiek bij de triggervoorwaarde van de
  [Sticky logische schakelaar](../model-setup/logical-switches.md).

**Stick-bronnen** — opties in de stijl van kalibratie/subtrim:

![Opties voor stick-bron](../assets/source-stick-options.png)

**Schakelaarbronnen** —

![Opties voor 2-standenschakelaar](../assets/source-2pos-options.png)
![Schakelaaropties](../assets/switch-options.png)

- **Negative** — inverteert de schakelaarwerking.
- **HalfRange** — wijzigt bij een 2-standenschakelaar of logische schakelaar het
  uitgangsbereik van ±100% naar 0–100%.

**Trim-bronnen** —

![Opties voor trim-bron](../assets/source-trim-options.png)

- **Negative** — inverteert de trimwerking (nuttig binnen de Actions van een
  vrije mix).
- **Full range** — trims hebben standaard ±25%; als bron kan dit worden
  uitgebreid tot ±100%.
- **Ignore trainer input** — sluit bij een [logische
  schakelaar](../model-setup/logical-switches.md) beweging van de trainer-ingang
  uit van het activeren van de schakelaar. Typisch gebruik: het detecteren van
  de stickbeweging van de *master*-trainer zelf (bijvoorbeeld om onmiddellijk in
  te grijpen als de leerling iets verkeerd doet) zonder dat de stickbewegingen
  van de leerling deze ook activeren.

**Variabelebronnen** —

![Opties voor variabelebron](../assets/source-var-options.png)

- **Negative** — negeert de waarde van de variabele voor dit gebruik.
- **Ignore range** — sommige velden hebben asymmetrische bereiken (bijvoorbeeld
  Min/Max bij Uitgangen, die respectievelijk van −150–0% en 0–150% lopen).
  Tenzij een [variabele](../model-setup/variables.md) die als bron voor dat veld
  wordt gebruikt exact hetzelfde bereik heeft, schakelt u dit in om de
  automatische bereikomzetting van Ethos over te slaan en onverwachte waarden te
  voorkomen.

**Telemetriesensorbronnen** — beperk de bron tot het actuele minimum of maximum
in plaats van de momentane meetwaarde (sommige sensoren bieden hierbovenop nog
sensorspecifieke opties):

![Opties voor sensor min/max](../assets/source-sensor-options.png)
![Sensormaximum geselecteerd](../assets/source-sensor-maxi.png)
