---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Skjermer

![Skjerm hjem](../assets/display-home.png)

Hjem-skjermen består av én eller flere **skjermsider**, hver bygget opp av
**widgeter** som du plasserer og konfigurerer selv. Et trykk på `DISP` åpner
skjermredigereren for den gjeldende skjermen.

Du har opptil **åtte** skjermer tilgjengelig, hver basert på én av
**tretten** oppsett (med plass til opptil **ni** widget-celler). Widgeter kan
vise telemetri, men også hvilken som helst av sytten andre
informasjonskategorier — modell-/senderstatus, timer, kanaler og mer.
Konfigurerte skjermer nås ved å sveipe på berøringsskjermen eller med `PAGE`
opp/ned; den øvre og nedre linjen forblir synlig på alle skjermer bortsett
fra et fullskjermsoppsett.

## Legge til en widget

![Widget-typer](../assets/display-widget-types.png)

Hver skjerm er et rutenett; ved å trykke på en tom celle åpnes
widget-velgeren. Widgetene spenner fra enkle tekst- og tallvisninger til
målere, diagrammer og fullstendige telemetrilogger. Når widgeten er
plassert, åpner et nytt trykk på den den samme alternativmenyen som brukes
til å endre størrelse på, flytte eller fjerne den:

![Konfigurasjonsalternativer for widget](../assets/display-widget-config-options.png)

Når du velger widgetens egne innstillinger, åpnes et widget-spesifikt
konfigurasjonsskjema. Feltet **Kilde** — verdien widgeten viser — bruker den
samme [kildevelgeren](../getting-started/user-interface-and-navigation.md#choosing-a-source)
som alle andre steder i Ethos:

![Endre widget-kilde](../assets/display-change-source.png)

## Widget-typer {: #widget-types }

**Verdi** — en enkelt tall- eller telemetriverdi, vist som tekst:

![Konfigurasjon av verdi-widget](../assets/display-widget-value-config.png)

De fleste kilder støtter også reduksjon til en løpende **min**- eller
**maks**-verdi — etter at du har valgt kilden, holder du inne på den og
velger Min eller Maks — nyttig for eksempelvis dårligste RSSI gjennom en
flyging:

![Verdi-widget min](../assets/display-widget-value-min.png)
![Verdi-widget min RSSI](../assets/display-widget-value-min-rssi.png)

Når widgeten er plassert, vises den som en enkel avlesning på skjermen:

![Telemetriverdi-widget](../assets/display-widget-value-telemetry.png)

**Bitmap** — viser et statisk bilde (f.eks. et modellbilde), eller et sett
bilder som byttes ut basert på verdien til en kilde (f.eks. et batteriikon
som endrer seg med spenningen):

![Konfigurasjon av bitmap-widget](../assets/display-widget-bitmap-config.png)
![Bitmap-widget-type](../assets/display-widget-bitmap-type.png)

**LiPo** — en spesialbygd batterimåler som leser fra en sensor som FLVSS:
total pakkespenning, celleantall og spenningen for hver enkelt celle.
Dersom spenningen faller under den konfigurerte terskelen **Lav spenning**,
blir visningen rød — i eksemplet nedenfor utløses en terskel på 3,3 V av den
laveste cellen:

![Konfigurasjon av LiPo-widget](../assets/display-widget-lipo-config.png)
![LiPo-widget](../assets/display-widget-lipo.png)

**Kanaler** — opptil 8 utgangskanaler som et stolpediagram, horisontalt
eller vertikalt:

![Konfigurasjon av kanal-widget](../assets/display-widget-channels-config.png)
![Kanal-widget](../assets/display-widget-channels.png)

**Linjediagram** — tegner verdien til en kilde over tid, og nullstilles ved
en flynullstilling:

![Konfigurasjon av linjediagram-widget](../assets/display-widget-line-chart-config.png)
![Linjediagram-widget](../assets/display-widget-line-chart.png)

- **Kilde** — hva som skal vises i diagrammet.
- **Pausebetingelse** — en kilde som pauser/gjenopptar loggingen (eller du
  kan bare trykke på den kjørende widgeten hvis ingen kilde er ledig til
  dette).
- **Loggperiode** — målingsintervall; 500 ms dekker omtrent 6 minutter før
  diagrammet ruller, 1 s omtrent 12 minutter.
- **Invertert** — snur diagrammet vertikalt.
- **Autoområde** — skalerer den vertikale aksen automatisk etter dataene;
  slått av brukes faste **Min**-/**Maks**-verdier i stedet (f.eks. et fast
  område på −100 %…+100 %).

Ved å trykke på et kjørende diagram får du opp **Pause/fortsett**,
**Nullstill** (tøm og start på nytt), **Konfigurer widget**, eller du kan
hoppe til **Konfigurer skjermer**:

![Alternativer for linjediagram](../assets/display-widget-line-chart-options.png)

**Tekst** — viser innholdet i en Markdown-tekstfil (leses fra
`documents/user/` — se
[Filbehandler](../system-setup/file-manager.md#top-level-folders)):

![Konfigurasjon av tekst-widget](../assets/display-widget-text-config.png)
![Tekst-widget](../assets/display-widget-text.png)

**Timerlogg** — en rullbar logg over tidligere verdier for en valgt timer,
som skrives hver gang denne timeren nullstilles (nyttig for å holde
oversikt over bruken av flypakkene gjennom en økt); **Omvendt** plasserer
den nyeste oppføringen øverst:

![Konfigurasjon av timerlogg-widget](../assets/display-widget-timer-logs-config.png)
![Timerlogg-widget](../assets/display-widget-timer-log.png)

Hold inne på en oppføring (eller på widgeten) for **Tøm logger**, for å
redigere/nullstille den underliggende timeren, eller for å hoppe til
widget-/skjermkonfigurasjonen:

![Meny for timerloggoppføring](../assets/display-widget-timer-log-menu.png)

**GPS-kart** — tegner den løpende GPS-posisjonen som et spor, for modeller
med en GPS-sensor (se tråden *FrSky - ETHOS Lua Script Programming* på
rcgroups, innlegg #8854, for flere detaljer om nettopp denne widgeten):

![Konfigurasjon av GPS-kart-widget](../assets/display-widget-gps-map-config.png)

## Alternativer på skjermnivå

I tillegg til de enkelte widgetene har hver skjerm sine egne innstillinger —
størrelsen på oppsettets rutenett, bakgrunn, og hvilke skjermer som inngår i
`PAGE`-syklusen:

![Konfigurasjonsalternativer for skjerm](../assets/display-screen-config-options.png)

En fullt konfigurert hjem-skjerm kombinerer flere widgeter i ett oppsett som
gir rask oversikt:

![Hovedvisning](../assets/display-main-view.png)

Se [Flere skjermer](additional-displays.md) for å legge til flere skjermer i
tillegg til standardskjermen, og [Egendefinerte widgeter](custom-widgets.md)
for Lua-skriptede widgeter utover det innebygde utvalget.
