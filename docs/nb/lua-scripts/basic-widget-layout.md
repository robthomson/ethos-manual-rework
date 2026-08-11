---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Grunnleggende widget-oppbygning

En egendefinert Lua-widget (se [Egendefinerte widgets](../displays/custom-widgets.md)
for hvordan du installerer en) bygges opp av et lite sett med navngitte felt/behandlere:

- **`key`** *(streng)* — en unik identifikator for widgeten.
- **`name`** *(streng eller funksjon)* — widgetens visningsnavn. Enten en
  ren streng, eller en funksjon som ikke tar noen argumenter og returnerer
  navnet — nyttig for et navn som varierer med språkinnstillingen.
- **`create`** *(funksjon)* — kalles én gang når widgeten opprettes, og tar
  ingen argumenter. Returnerer en **widget-tabell**, som deretter sendes
  videre til alle de andre behandlerne nedenfor — initialiser tilstanden
  din her og lagre den i denne tabellen.
- **`configure`** *(funksjon)* — kalles når brukeren åpner widgetens
  konfigurasjonsskjerm, og tar widget-tabellen fra `create()` som sitt
  eneste argument, uten å returnere noe. Bygg konfigurasjonsskjemaet her og
  bruk det til å oppdatere verdier i widget-tabellen.
- **`wakeup`** *(funksjon)* — kalles hver runde i løkken (omtrent hvert
  50 ms), tar widget-tabellen og returnerer ingenting. Sjekk her om noe har
  endret seg; hvis så, kall `invalidateWindow()` for å utløse en ny
  opptegning via `paint()`. Hold denne behandleren rask — ideelt sett skal
  den ikke gjøre noe som helst det meste av tiden den kalles.
- **`event`** *(funksjon)* — kalles når widgeten mottar en hendelse; Ethos
  ruter vilkårlige hendelser til en widget gjennom denne behandleren.
- **`paint`** *(funksjon)* — tegner widgeten, tar widget-tabellen og
  returnerer ingenting. Kalles automatisk hver gang `lcd.invalidate()` har
  blitt utløst. Kan være forholdsvis langsom, men bør likevel bare tegne på
  nytt når noe har endret seg.
- **`read`** *(funksjon, valgfri)* — leser lagrede widget-data.
- **`write`** *(funksjon, valgfri)* — skriver lagrede widget-data.
- **`init`** *(funksjon)* — registrerer widgeten og dens tilbakekall hos
  Ethos. Vanligvis det siste i skriptet:

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

`key` må være unik blant alle installerte widgets; de andre feltene knytter
seg til widgetens livsløp slik det er beskrevet ovenfor.

Skript ligger under `scripts/` på SD card/eMMC, ideelt organisert i egne
mapper per widget (se [Filbehandler](../system-setup/file-manager.md#top-level-folders)
og [Eksempler på skriptplasseringer](example-script-locations.md)). Se tråden
*FrSky ETHOS Lua Script Programming* på rcgroups for flere gjennomgåtte
eksempler.
