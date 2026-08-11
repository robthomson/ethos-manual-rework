---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Flere skjermer

![Alternativer for skjermkonfigurasjon](../assets/display-screen-config-options.png)

Standardmodellen har én skjerm (et modellbilde pluss tre Timer-widgeter),
men det støttes opptil **åtte** skjermer totalt. Trykk på **+** ved siden
av «Screen1» for å legge til en ny:

- Velg blant **15** oppsett, inkludert to dedikerte oppsett for
  hjemmeskjermen og et fullskjermsalternativ, med plass til opptil 9
  widgeter — konfigureres på akkurat samme måte som den første skjermen.
- Skjermer kan omorganiseres eller slettes fra sin egen redigeringsdialog
  (trykk på Screen1, Screen2 osv.).

## Gjennomgått eksempel

![Hovedvisning](../assets/display-main-view.png)

Et typisk oppsett: modellbildet (konfigureres i [Modellredigering →
Bilde](../model-setup/model-edit.md)) til venstre, med
mottakerbatterispenning, RSSI og en «Throttle ACTIVE»-statuswidget (en
Lua-widget utviklet av brukermiljøet, fra rcgroups-tråden *FrSky - ETHOS
Lua Script Programming*) stablet til høyre. Ved å trykke på en widget
åpnes konfigurasjonen av den, eller du hopper til hovedfunksjonen
Konfigurer skjermer.

## Alternativer på skjermnivå

I tillegg til de enkelte widgetene har hver skjerm sine egne
innstillinger — rutenettstørrelse for oppsettet, bakgrunn, og hvilke
skjermer som inngår i `PAGE`-syklusen.

Se [Skjermer](index.md) for widgetene i seg selv, og [Egendefinerte
widgeter](custom-widgets.md) for å legge til Lua-baserte widgeter utover
det innebygde utvalget.
