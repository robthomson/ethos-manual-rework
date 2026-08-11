---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Basisopbouw van een widget

Een aangepaste Lua-widget (zie [Aangepaste widgets](../displays/custom-widgets.md)
voor het installeren ervan) is opgebouwd uit een kleine set benoemde velden/handlers:

- **`key`** *(string)* — een unieke identificatie voor de widget.
- **`name`** *(string of functie)* — de weergavenaam van de widget. Ofwel een
  gewone string, ofwel een functie zonder argumenten die er één teruggeeft —
  nuttig voor een naam die per taal verschilt.
- **`create`** *(functie)* — wordt eenmalig aangeroepen wanneer de widget wordt
  aangemaakt, zonder argumenten. Geeft een **widgettabel** terug, die vervolgens
  aan elke andere handler hieronder wordt doorgegeven — initialiseer hier je
  toestand en sla die op in die tabel.
- **`configure`** *(functie)* — wordt aangeroepen wanneer de gebruiker het
  configuratiescherm van de widget opent, met de widgettabel uit `create()` als
  enige argument en zonder retourwaarde. Bouw hier het configuratieformulier op en
  gebruik dit om waarden in de widgettabel bij te werken.
- **`wakeup`** *(functie)* — wordt elke lus aangeroepen (ongeveer elke 50 ms),
  met de widgettabel en zonder retourwaarde. Controleer hier of er iets is
  gewijzigd; zo ja, roep dan `invalidateWindow()` aan om via `paint()` een
  hertekening te activeren. Houd deze handler snel — idealiter doet hij het
  grootste deel van de tijd helemaal niets.
- **`event`** *(functie)* — wordt aangeroepen wanneer de widget een event
  ontvangt; Ethos stuurt willekeurige events via deze handler naar een widget.
- **`paint`** *(functie)* — tekent de widget, met de widgettabel en zonder
  retourwaarde. Wordt automatisch aangeroepen zodra `lcd.invalidate()` is
  afgevuurd. Mag relatief langzaam zijn, maar moet nog steeds alleen daadwerkelijk
  hertekenen wanneer er iets is gewijzigd.
- **`read`** *(functie, optioneel)* — leest de permanent opgeslagen widgetgegevens.
- **`write`** *(functie, optioneel)* — schrijft de permanent opgeslagen widgetgegevens.
- **`init`** *(functie)* — registreert de widget en zijn callbacks bij
  Ethos. Doorgaans het laatste onderdeel in het script:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` moet uniek zijn binnen alle geïnstalleerde widgets; de overige velden sluiten
aan op de levenscyclus van de widget zoals hierboven beschreven.

Scripts staan onder `scripts/` op de SD card/eMMC, bij voorkeur georganiseerd in
mappen per widget (zie [Bestandsbeheer](../system-setup/file-manager.md#top-level-folders)
en [Voorbeelden van scriptlocaties](example-script-locations.md)). Zie de thread
*FrSky ETHOS Lua Script Programming* op rcgroups voor meer uitgewerkte voorbeelden.
