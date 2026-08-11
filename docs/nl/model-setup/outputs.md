---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Uitgangen

![Uitgangen](../assets/model-outputs.png)

Uitgangen vormen de grens tussen de zuivere "logica" van [Mixen](mixes.md) en de
fysieke wereld — servo's, stangenstelsels, roervlakken, actuatoren,
omvormers. Hier worden eindpunten, omkering, centrering en
correctiecurves aangepast aan wat het model mechanisch daadwerkelijk nodig
heeft. Elk uitgangskanaal correspondeert met een servo-uitgang van de ontvanger
(CH1 → servoaansluiting #1, bij de standaard protocolinstellingen).

Ethos werkt met percentages, maar servo's worden uiteindelijk aangestuurd met een
PWM-pulsbreedte in microseconden:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Een kanaal **zonder actieve mix** geeft neutraal uit (0% / 1500µs) — dit
    geldt ook voor een kanaal waarvan de enige mix(en) momenteel inactief zijn.
    Zorg ervoor dat elk kanaal dat je daadwerkelijk gebruikt altijd door een
    actieve mix wordt ondersteund. Op een gaskanaal betekent neutraal specifiek
    **half gas**.

Het scherm Uitgangen toont twee balken per kanaal: de onderste (groene) balk is
de waarde van de mixer voor dat kanaal, de bovenste (oranje) balk is de
waarde na de uitgangsverwerking die daadwerkelijk naar de ontvanger wordt
gestuurd (zowel in % als in µs). Min/Max-limieten worden weergegeven als grijze
delen van de oranje balk. Kanalen die momenteel niet naar de RF-module worden
verzonden, hebben een donkerdere achtergrond. Kleine pictogrammen verschijnen bij
een kanaal wanneer de instellingen Richting, Curve, Vertraging of Balans zijn
gewijzigd ten opzichte van de standaardwaarde, zodat je niet-standaard kanalen in
één oogopslag kunt herkennen.

!!! tip
    Een lange druk op `ENT` vanuit het scherm Mixen of Vluchtmodi springt
    direct hierheen.

## Een kanaal bewerken {: #editing-a-channel }

![Hoogteroeruitgang bewerken](../assets/model-outputs-elevator-edit.png)
![Gasuitgang bewerken](../assets/model-outputs-throttle-edit.png)

Tik op een kanaal om het te openen. Een voorbeeldweergave bovenaan toont de
mixwaarde (groen) tegenover de uitgangswaarde (oranje), met een kleine witte
markering voor de Min/Max-punten.

- **Naam** — bewerkbaar.
- **Richting** — keert de uitgang van het kanaal om, doorgaans om de
  draairichting van de servo om te keren. Wordt weergegeven als een
  dubbelepijl-pictogram bij het kanaal. Dit heeft **geen** invloed op de mixen die
  het kanaal voeden en verwisselt de Min/Max-limieten **niet**.
- **Min/Max** — harde limieten die nooit worden overschreven — stel ze in om
  mechanisch klemmen te voorkomen. Ze werken als eindpunt-/versterkingsinstelling:
  ze verkleinen de uitslag in plaats van afkapping te veroorzaken. De standaard is
  ±100%, instelbaar tot ±150%. Tijdens het instellen wordt het uiteinde waarnaar
  op dat moment wordt bewogen vet weergegeven (beweeg bijvoorbeeld de
  hoogteroerstick naar voren en de Max-waarde wordt vet, ter bevestiging dat je
  dat uiteinde instelt).

  ![Waarschuwing SBUS-redundantie](../assets/model-outputs-sbus-warning.png)

  !!! warning "SBUS-redundantie"
      Een redundantie-opstelling via SBUS kan een servo niet verder dan ongeveer
      ±125% bewegen. De Min/Max-velden zelf hebben asymmetrische bereiken (−150–0%
      en 0–150%) — als je ze aanstuurt vanuit een [Var](variables.md), geef die
      Var dan een identiek bereik of stel **Bereik negeren** in (zie
      [bronopties](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      anders levert de automatische bereikconversie onverwachte waarden op. Als de
      uitgang van de hoofdontvanger 125% overschrijdt en deze in failsafe gaat,
      begrenst de redundante ontvanger die via SBUS overneemt de waarde terug tot
      125%.

- **Center/Subtrim** — verschuift de uitgang, doorgaans om een servoarm te
  centreren; de eindpunten blijven ongewijzigd.

  !!! warning
      Gebruik subtrim niet voor grote verschuivingen — dit brengt aanzienlijk
      differentieel in de respons van de servo. Gebruik in plaats daarvan een
      **offset-mix** voor alles wat verder gaat dan fijne centrering.

- **PWM center** — vergelijkbaar met subtrim, maar verschuift de *volledige*
  servoslagband inclusief de harde limieten, en gebeurt in feite binnen de servo
  zelf in plaats van dat het op de kanaalmonitor wordt weergegeven. Zo blijft
  mechanische centrering gescheiden van trimmen.
- **Curve** — koppelt een Expo- of aangepaste curve (bestaand of nieuw, met een
  snelkoppeling **Bewerken** zodra deze is ingesteld) om de respons in de praktijk
  te corrigeren — bijvoorbeeld om de linker- en rechterflaps nauwkeurig gelijk te
  laten lopen. Wordt weergegeven als een curvepictogram bij het kanaal.
- **Slow up/down** — vertraagt de respons van de uitgang op ingangswijzigingen, in
  seconden voor een slag van 0→100% — bijvoorbeeld om intrekbaar landingsgestel
  dat door een gewone proportionele servo wordt aangedreven te vertragen. Wordt
  weergegeven als een klokpictogram bij het kanaal. (Een **vertraging**, in
  tegenstelling tot slow, is beschikbaar bij [logische
  schakelaars](logical-switches.md).)

## Kanalen verwisselen {: #swap-channels }

![Kanalen verwisselen](../assets/model-outputs-swap-channels.png)
![Kanaal kiezen om te verwisselen](../assets/model-outputs-swap-channels-select.png)

Verwisselt twee uitgangskanalen. Het dialoogvenster opent met het huidige kanaal
al ingevuld; kies het andere en bevestig — de verwisseling is direct, en elke mix
die naar een van beide kanalen verwijst, wordt dienovereenkomstig bijgewerkt.

## Instellingen wissen

![Kanaal wissen](../assets/model-outputs-reset-select.png)

Zet elke parameter van een kanaal terug naar de standaardwaarde — handig voordat
je een kanaal voor iets anders gaat gebruiken, met een bevestigingsvenster om
ongelukken te voorkomen.

## Kanalen balanceren {: #balance-channels }

![Kanalen kiezen om te balanceren](../assets/model-outputs-balance-choose_channels.png)
![CH7/CH6 kiezen](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Balanceert een paar (of tot 4) kanalen zodat ze synchroon bewegen — flaps die
niet gelijk bewegen kunnen bijvoorbeeld ongewenste rolbeweging veroorzaken; niet
gebalanceerde gaskanalen op een meermotorig model kunnen ongewenste giering
veroorzaken. Ethos maakt per geselecteerd kanaal een differentiële balanscurve;
door de fysieke standen van de roervlakken op elk curvepunt te vergelijken kun je
ze op elkaar afstemmen, wat leidt tot perfect gelijklopende roervlakken.

**Vóór het balanceren**, in deze volgorde:

1. Stel de servorichtingen in voor de juiste slag.
2. Gebruik met de mixen op neutraal eventueel **PWM center** om de servoarmen
   recht te zetten.
3. Stel Min/Max en Subtrim in.
4. Configureer eventuele andere curves.
5. Configureer Slow.
6. Balanceer en egaliseer *daarna* over het volledige slagbereik.

**Gebruik**: kies de kanalen die je wilt balanceren en de volgorde waarin ze
worden weergegeven —

![CH7/CH6 geselecteerd](../assets/model-outputs-balance-ch7-and-ch6.png)

— mixuitgang op de X-as, balanscorrectie-differentieel op de Y-as. Tik op de
grafiek van een kanaal (of selecteer het en druk op `ENT`) om de balanscurve te
bewerken; met `PAGE` wissel je tijdens het bewerken tussen kanalen:

![Balanscurve-editor](../assets/model-outputs-balance-curve-edit.png)

Bediening van de editor:

- **Bron** — normaal gesproken de bron(nen) van de mix zelf, of een andere
  geschikte analoge ingang; **Auto analog input** neemt de eerste
  stick/schuifregelaar/potentiometer die je beweegt als X, zowel in de grafiek als
  in het model zelf.
- **Magneet** — laat de instelling met de draaiknop automatisch naar het
  dichtstbijzijnde curvepunt op de X-as springen:

  ![Magneet uit](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Magneet aan](../assets/model-outputs-balance-ch6-magnet-on.png)

  De ingang moet nog steeds worden bewogen om X met een curvepunt te laten
  samenvallen voordat je dat punt kunt aanpassen.
- **Lock** — wordt in- en uitgeschakeld door op het pictogram te tikken of op
  `ENT` te drukken in de grafiekbewerkmodus; vergrendelt alle ingangen zodat je de
  stick kunt loslaten en de roervlakken kunt observeren terwijl je de curve
  aanpast.
- **Configuratie** — wijzig het aantal punten per kanaal (allemaal of afzonderlijk)
  en of elke curve wordt vloeiend gemaakt.
- **Help** (`?`, tevens de `MDL`-toets) — opent de ingebouwde help.

**Meerdere kanalen**: er kunnen tot 4 kanalen samen worden gebalanceerd —

![Balans over 4 kanalen](../assets/model-outputs-balance-ch2-9-8-1.png)

Zodra een balanscurve is ingesteld, kan deze op de configuratiepagina van het
kanaal zelf worden bekeken, bewerkt of gewist — een balanspictogram markeert dit
bij de kanaalgrafiek (naast een richtingspictogram, als ook dat niet-standaard
is).
