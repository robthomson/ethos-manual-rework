---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Pipeline for skjermbilder

Alle skjermbilder i denne håndboken (for øyeblikket ca. 590 av dem, under
`docs/en/assets/`) er tatt opp ved å skripte den virkelige Ethos-simulatoren, ikke
manuelt. Oppsettet ligger i det gamle
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual)-repoet, under
`english/manual/`, og er **ennå ikke portert inn i dette repoet** — denne
siden dokumenterer hvordan det fungerer, slik at det kan porteres, og slik at skjermbilder
kan regenereres eller utvides i mellomtiden uten å starte fra bunnen av.

## Hvordan det er strukturert

For hver meny/seksjon i håndboken finnes det et par filer:

- `manual/macros/<name>.lua` — et skript skrevet mot simulatorens Lua-API
  (se nedenfor) som navigerer til en bestemt skjerm og kaller
  `simulator.screenshot(path)` på hvert punkt som er verdt å fange opp.
- `manual/<name>.sh` — en enlinjes wrapper som starter simulator-binærfilen
  for en bestemt sender, pekt mot den makroen, f.eks.:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` kjører alle makroene i rekkefølge for å regenerere
hele settet. Individuelle `.sh`-filer finnes per seksjon, slik at skjermbildene for
en enkelt side kan regenereres uten å kjøre alt på nytt (hver makro
tar fra noen sekunder til over ett minutt).

Viktige CLI-flagg:

- `--read-only` — ikke lagre noen endringer som gjøres under kjøringen.
- `--no-gui` / `--no-audio` — nesten headless; noen makroer trenger fortsatt GUI-et
  fordi simulatoren «hopper over» uten det (se kommentaren i `screenshots.sh`).
- `--radio-settings <file>.bin` — hvilken senders lagrede innstillinger som skal brukes ved oppstart
  (dette er det som gjør skjermbildene språk- og senderspesifikke — en tysk
  kjøring bruker en tysk `.bin`).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — peker simulatoren mot de modellene/den fastvaren/de dokumentene/den lyden
  den skal se, slik at skjermbildene viser bevisst tilrettelagt innhold i stedet
  for hva som nå tilfeldigvis ligger på et virkelig SD card.
- `--exec <script>.lua` — makroen som skal kjøres etter oppstart.

Hver senderfamilie (X20S, X20 PRO, X20 PRO AW, X18S) har sin egen simulator-binærfil
og trenger sin egen `--radio-settings`-fil per språk (f.eks.
`x20s-en.bin`, `x20pro-en.bin`), siden brukergrensesnittet skiller seg litt mellom
sendere og innstillingsfilen også bærer språket.

## Makro-API-et

Makroer er ren Lua som styrer en global `simulator`:

| Kall | Formål |
|---|---|
| `simulator.loadModel("name.bin")` | Last inn en bestemt modellfil før navigering — hver seksjon i håndboken bruker en modell som er satt opp for å demonstrere den seksjonen (se modellisten nedenfor). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Trykk en fysisk tast — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE` osv. En holdevarighet utløser et langt trykk (åpner kontekstmenyer). |
| `simulator.turnRotaryEncoder(n)` | Flytt encoderen `n` klikk (negativt = motsatt retning) — den primære måten å flytte markøren mellom felt. |
| `simulator.touch(x, y)` | Trykk på en bestemt skjermkoordinat — brukes der berøring er den eneste måten å nå noe (f.eks. bytte tastaturoppsett). |
| `simulator.setAnalog(channel, value)` | Sett en spak-/potensiometer-/glidebryterposisjon direkte (`0`-`3` er de fire hovedspakene, `ANALOG_LAST_SLIDER` den siste glidebryteren), slik at skjermbildene viser en bevisst, reproduserbar verdi i stedet for hva simulatoren tilfeldigvis har som standard. |
| `simulator.setSwitch(n, position)` | Sett posisjonen til en fysisk bryter. |
| `simulator.setDateTime({...})` | Lås simulatorens klokke, slik at tidsstempler i skjermbilder (og alt tidsavhengig) er reproduserbare mellom kjøringer. |
| `simulator.screenshot(path)` | Fang gjeldende skjerm til en PNG, relativt til makroens arbeidskatalog (derav `../assets/...`-stiene inne i hver makro). |
| `simulator.connectUsb()` | Simuler tilkobling til USB, for å fange opp USB-menyen. |
| `simulator.sleep(seconds)` | Vent på at en animasjon/telemetriverdi stabiliserer seg før opptak. |

`manual/macros/common.lua` blir `dofile`-kjørt fra de fleste makroene og låser bare
dato/klokkeslett slik at hver makro starter fra samme simulerte tidspunkt.

## Modeller brukt per seksjon

`manual/notes.txt` (videreført uformelt, ennå ikke kopiert inn i dette repoet)
kobler hver makro til `.bin`-modellfilen den avhenger av og hvorfor — f.eks.
bruker `model-mixes.lua` `rarebear.bin`, `model-fm.lua` bruker `zblank.bin` (en
modell med et bevisst tomt flymodus-oppsett), `model-trims.lua` bruker
`blaster.bin` (satt opp med forskjøvede trim for å demonstrere trimområdet).
Å porte notatene i denne filen til ordentlig dokumentasjon her er en del av
fase 2-arbeidet nedenfor.

## Hva portering av dette til det nye repoet innebærer (ikke gjort ennå)

- Bestemme om makroene skal kjøres direkte fra dette repoet (som krever en
  lokal installasjon av Ethos-simulatoren, slik det gamle repoet gjorde) eller via CI med
  simulatoren pakket med / lastet ned i workflowen.
- Restrukturere de flate `../assets/...`-utdatastiene slik at de samsvarer med dette repoets
  ressursstruktur per side og per lokalitet (`docs/<locale>/assets/`).
- Én `--radio-settings ... .bin` og én skjermbildekjøring per lokalitet, så snart en
  lokalitet utover `en` finnes — skjermbilder er spesifikke for brukergrensesnittets språk og
  kan ikke deles på tvers av lokaliteter.
- Bestemme hvor mange av de ca. 40 eksisterende makroene som skal videreføres som de er, kontra
  skrives om mot den nåværende navigasjonsstrukturen i dette repoet (noen makroer
  produserer skjermbilder for seksjoner som ikke lenger tilsvarer 1:1 denne
  håndbokens sidestruktur).
