---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Plassering av eksempelskript

Offisielle eksempelskript er publisert på
[github.com/FrSkyRC/ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/tree/main/lua)
(særlig `/lua/examples/task` og `/lua/examples/source`). De fleste
eksemplene er Lua-widgeter (som konfigureres under [Konfigurer
skjermer](../displays/custom-widgets.md)); eksempelet **`servo`** viser
spesifikt et **Systemverktøy** — et skript som vises etter **Info** i
System-menyen i stedet for som en widget på en skjerm.

## Laste ned et skript

1. Åpne repositoriumslenken ovenfor i en nettleser og naviger til den
   mappen, og deretter den `main.lua`-filen, du ønsker.
2. Klikk på filen for å vise den, og klikk deretter **Raw**.
3. Høyreklikk på siden → **Lagre side som…**, og lagre den som `main.lua`.
4. For å unngå konflikt med andre skripts `main.lua` bør du flytte filen
   inn i en mappe med et passende navn — navnet på selve kildemappen er
   et fornuftig valg.

For eventuelle andre filer et skript trenger (bilder osv.): klikk på
filen, klikk **Download**, og høyreklikk deretter og velg **Lagre bilde
som…** (eller tilsvarende) for å lagre den sammen med skriptet.

Skript installeres under `scripts/` på SD card/eMMC — se
[Filbehandler](../system-setup/file-manager.md#top-level-folders).

Se også tråden *FrSky ETHOS Lua Script Programming* på rcgroups for
skript og diskusjoner fra brukermiljøet utover de offisielle eksemplene.
