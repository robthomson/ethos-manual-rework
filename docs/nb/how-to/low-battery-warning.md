---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Varsel om lav batterispenning

Å overvåke spenningen i flypakken **under belastning** og varsle når den
faller under en terskel, er en mer pålitelig metode enn å basere seg på en
fast timer — en sensor som FrSky FLVSS gjør dette enkelt.

## 1. Koble til og oppdag sensoren

![Telemetrisensor for LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Sett [Mottakervalg → Telemetriport](../system-setup/devices.md) til
**S.Port**, koble FLVSS til mottakeren med en S.Port-kabel, og aktiver
deretter **Oppdag nye sensorer** under
[Telemetri](../model-setup/telemetry.md) — LiPo-sensoren vises sammen med
de andre som allerede er oppdaget.

## 2. Legg til en logisk bryter

![Logisk bryter for lavt batteri](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Legg til en ny [logisk bryter](../model-setup/logical-switches.md) med
LiPo-sensoren som kilde. Hold `ENT` inne på den markerte sensoren for å
velge hvilken av verdiene den skal bruke:

![Velg laveste celle](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Min. pakkespenning / Maks. pakkespenning
- **Laveste cellespenning** / Høyeste cellespenning
- Antall celler
- Spenning for enkeltceller (kan bare velges når sensoren faktisk er
  tilkoblet en bundet mottaker med et LiPo-batteri tilkoblet)

Velg **Laveste** (cellespenning) — verdien som er avgjørende for
LVC-lignende beskyttelse.

![Laveste celle valgt](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Sett sammenligningsverdien til omkring **3,4 V** og **Forsinkelse før
aktiv** til **4 sekunder** — bryteren blir sann når den laveste cellen har
vist under 3,4 V per celle sammenhengende i 4 s eller mer. (3,4 V *under
belastning* stiger vanligvis til omkring 3,7 V når belastningen fjernes,
så denne terskelen gjenspeiler et reelt spenningsfall og ikke bare
kortvarig støy.)

![Fullført logisk bryter](../assets/how-to-low-batt-lsw-summary.png)

## 3. Legg til en spesialfunksjon

![Spesialfunksjon: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Legg til en [spesialfunksjon av typen Spill
lyd](../model-setup/special-functions.md), sett **Aktiv betingelse** til
den logiske bryteren `BattLow`, velg en stemme, og legg under **Sekvens**
til et **Spill verdi**-trinn for den totale LiPo-spenningen:

![Spill verdi: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Sammendrag av sekvensen](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Med **Gjenta** satt til 10 sekunder blir LiPo-spenningen lest opp hvert
10. sekund så lenge den laveste cellen holder seg under terskelen på
3,4 V/4 s.
