---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Nødmodus

Nødmodus er Ethos' respons på en uventet lavnivåfeil, for eksempel en
watchdog-tilbakestilling. Watchdogen er en timer som stadig startes på nytt av
ulike deler av systemet; dersom noe hindrer den fra å bli startet på nytt, vil
den løpe ut og tvinge en maskinvaretilbakestilling. Nødmodus starter deretter
senderen på nytt så raskt som mulig, og hopper over alle de vanlige
oppstartskontrollene slik at kontrollen over modellen gis tilbake med minimal
forsinkelse. SD card/eMMC brukes ikke i det hele tatt i denne modusen.

Kun de nødvendige funksjonene som trengs for å fortsette å styre modellen er
tilgjengelige — ingen av de mer avanserte funksjonene. Skjermen blir tom
bortsett fra teksten **EMERGENCY MODE**, ledsaget av et gjentakende pip på
300 ms hvert 3. sekund; talemeldinger, Lua-skript, logging og telemetri stopper
alle. Hvis dette skjer i luften, land så snart som mulig.

Den vanligste årsaken er feil på SD card.

## Testing av nødmodus

Et **systemverktøy** kan legges til for å utløse nødmodus med hensikt for
testing, slik at man ikke opplever det for første gang under flyvning.
Når du trykker på Emergency Test-ikonet, blir du bedt om å bekrefte, og
deretter settes senderen i nødmodus på akkurat samme måte som ved en reell feil.
