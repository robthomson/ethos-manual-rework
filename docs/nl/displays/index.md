---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Displays

![Display start](../assets/display-home.png)

Het startscherm bestaat uit één of meer **displayschermen**, elk opgebouwd
uit **widgets** die u zelf plaatst en configureert. Met `DISP` opent u de
display-editor voor het huidige scherm.

Er zijn maximaal **acht** schermen beschikbaar, die elk beginnen met één van
**dertien** indelingen (met ruimte voor maximaal **negen** widgetcellen).
Widgets kunnen telemetrie weergeven, maar ook alle zeventien andere
informatiecategorieën — model-/zenderstatus, timers, kanalen en meer.
Geconfigureerde schermen bereikt u door te swipen of met `PAGE` omhoog/omlaag;
de boven- en onderbalk blijven op elk scherm zichtbaar, behalve bij een
volledig schermvullende indeling.

## Een widget toevoegen

![Widgettypen](../assets/display-widget-types.png)

Elk scherm is een raster; door op een lege cel te tikken opent u de
widgetkiezer. De widgets variëren van eenvoudige tekst- en numerieke
uitlezingen tot meters, diagrammen en volledige telemetrielogs. Zodra een
widget is geplaatst, opent u met opnieuw tikken hetzelfde optiemenu waarmee u
de widget kunt vergroten/verkleinen, verplaatsen of verwijderen:

![Configuratieopties widget](../assets/display-widget-config-options.png)

Als u de eigen instellingen van een widget selecteert, wordt een
widgetspecifiek configuratieformulier geopend. Het veld **Bron** — de waarde
die de widget weergeeft — maakt gebruik van dezelfde
[bronkiezer](../getting-started/user-interface-and-navigation.md#choosing-a-source)
als overal elders in Ethos:

![Bron van widget wijzigen](../assets/display-change-source.png)

## Widgettypen {: #widget-types }

**Waarde** — een enkele numerieke of telemetrische uitlezing, weergegeven als
tekst:

![Configuratie waarde-widget](../assets/display-widget-value-config.png)

De meeste bronnen ondersteunen ook een reductie naar een live **min** of
**max** — selecteer de bron, houd deze lang ingedrukt en kies Min of Max —
handig voor zaken als de laagste RSSI-waarde tijdens een vlucht:

![Waarde-widget min](../assets/display-widget-value-min.png)
![Waarde-widget min RSSI](../assets/display-widget-value-min-rssi.png)

Na plaatsing wordt de waarde als eenvoudige uitlezing op het scherm
weergegeven:

![Telemetrie waarde-widget](../assets/display-widget-value-telemetry.png)

**Bitmap** — geeft een statische afbeelding weer (bijvoorbeeld een foto van
het model), of een reeks afbeeldingen die wisselen op basis van de waarde van
een bron (bijvoorbeeld een accupictogram dat meebeweegt met de spanning):

![Configuratie bitmap-widget](../assets/display-widget-bitmap-config.png)
![Type bitmap-widget](../assets/display-widget-bitmap-type.png)

**LiPo** — een speciaal ontworpen accumeter die uitleest van een sensor zoals
de FLVSS: totale pakketspanning, aantal cellen en de spanning van elke
afzonderlijke cel. Bij het onderschrijden van de ingestelde drempel voor
**Lage spanning** wordt de weergave rood — in het onderstaande voorbeeld
wordt een drempel van 3,3 V geactiveerd door de laagste cel:

![Configuratie LiPo-widget](../assets/display-widget-lipo-config.png)
![LiPo-widget](../assets/display-widget-lipo.png)

**Kanalen** — maximaal 8 uitgangskanalen als staafdiagram, horizontaal of
verticaal:

![Configuratie kanalen-widget](../assets/display-widget-channels-config.png)
![Kanalen-widget](../assets/display-widget-channels.png)

**Lijndiagram** — zet de waarde van een bron uit in de tijd en wordt gereset
bij een Flight Reset:

![Configuratie lijndiagram-widget](../assets/display-widget-line-chart-config.png)
![Lijndiagram-widget](../assets/display-widget-line-chart.png)

- **Bron** — wat er in het diagram wordt weergegeven.
- **Pauzevoorwaarde** — een bron die het loggen pauzeert/hervat (of tik
  eenvoudig op de actieve widget als hiervoor geen bron beschikbaar is).
- **Logperiode** — het meetinterval; 500 ms omvat ongeveer 6 minuten voordat
  het diagram gaat schuiven, 1 s ongeveer 12 minuten.
- **Omgekeerd** — spiegelt het diagram verticaal.
- **Automatisch bereik** — schaalt de verticale as automatisch naar de
  gegevens; uitgeschakeld worden in plaats daarvan vaste waarden voor
  **Min**/**Max** gebruikt (bijvoorbeeld een constant bereik van
  −100%…+100%).

Door op een actief diagram te tikken verschijnen **Pauzeren/hervatten**,
**Reset** (wissen en opnieuw starten), **Widget configureren**, of gaat u
naar **Schermen configureren**:

![Opties lijndiagram](../assets/display-widget-line-chart-options.png)

**Tekst** — geeft de inhoud van een Markdown-tekstbestand weer (gelezen uit
`documents/user/` — zie
[Bestandsbeheer](../system-setup/file-manager.md#top-level-folders)):

![Configuratie tekst-widget](../assets/display-widget-text-config.png)
![Tekst-widget](../assets/display-widget-text.png)

**Timerlog** — een schuifbaar logboek met de eerdere waarden van een gekozen
timer, dat elke keer wordt bijgeschreven wanneer die timer wordt gereset
(handig om het gebruik van vluchtaccu's tijdens een sessie bij te houden);
met **Omgekeerd** staat de nieuwste vermelding bovenaan:

![Configuratie timerlog-widget](../assets/display-widget-timer-logs-config.png)
![Timerlog-widget](../assets/display-widget-timer-log.png)

Houd een vermelding (of de widget) lang ingedrukt voor **Logs wissen**, om de
onderliggende timer te bewerken of te resetten, of om naar de configuratie van
de widget of het scherm te gaan:

![Menu timerlog-vermelding](../assets/display-widget-timer-log-menu.png)

**GPS-kaart** — geeft de live GPS-positie weer als een spoor, voor modellen
met een GPS-sensor (zie de thread *FrSky - ETHOS Lua Script Programming* op
rcgroups, bericht #8854, voor meer details over specifiek deze widget):

![Configuratie GPS-kaart-widget](../assets/display-widget-gps-map-config.png)

## Opties op schermniveau

Naast de afzonderlijke widgets heeft elk scherm eigen instellingen — de
rastergrootte van de indeling, de achtergrond en welke schermen zijn opgenomen
in de `PAGE`-cyclus:

![Configuratieopties scherm](../assets/display-screen-config-options.png)

Een volledig geconfigureerd startscherm combineert meerdere widgets in één
overzichtelijke indeling:

![Hoofdweergave](../assets/display-main-view.png)

Zie [Aanvullende displays](additional-displays.md) voor het toevoegen van
extra schermen naast het standaardscherm, en
[Aangepaste widgets](custom-widgets.md) voor met Lua geschreven widgets naast
de ingebouwde set.
