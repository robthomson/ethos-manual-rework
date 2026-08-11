---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Hovedvisninger

## Hjem-skjermen

![Hjem-skjermen](../assets/mainview.png)

Hjem-skjermen er det du ser når ingen meny er åpen — en stabel med opptil
**åtte** visningsskjermer som du konfigurerer selv (se
[Skjermer](../displays/index.md)), som du blar mellom med `PAGE`-tasten
eller ved å sveipe på skjermen. En nyopprettet modell starter med bare én
skjerm som viser et modellbilde, tre timer-widgeter og indikatorene for
trim/potensiometer; alt på den kan brukeren konfigurere videre derfra.

Skjermene deler normalt topp- og bunnlinjen som beskrives nedenfor, men en
skjerm kan også settes til fullskjerm, slik at begge skjules.

## Topplinjen

Topplinjen viser modellnavnet til venstre (samt aktiv flymodus, dersom en
er konfigurert), og en rad med statusikoner til høyre:

- Datalogging aktiv
- Trenerstatus (master eller slave, alt etter hva som gjelder)
- RSSI — 2,4 GHz-forbindelse
- RSSI — 900 MHz-forbindelse (dersom en dobbeltbånds-/langdistansemodul er montert)
- Høyttalervolum
- Batteristatus for senderen

Ved å berøre høyttaler- eller batteriikonet går du direkte til det
tilhørende innstillingspanelet [Generelt](../system-setup/general.md) (lyd)
eller [Batteri](../system-setup/battery.md).

### Feilvarsel

En rød trekant vises i topplinjen når Ethos oppdager en feil — vanlige
årsaker er en feil i et Lua-skript, en feil i RAM-sikkerhetskopien, eller at
det kjøres en nightly/ustabil fastvareversjon. Detaljene bak varselet finnes
alltid i **System → Info**, på samme side som senderens driftstid og
[feillogger](../system-setup/information.md).

## Bunnlinjen

![Bunnlinjen](../assets/bottombar.png)

Fire faner går langs bunnen for hovedseksjonene — **Hjem**,
**Modelloppsett**, **Konfigurer skjermer**, **Systeminnstillinger** — med
systemklokken til høyre (berør den for å gå direkte til
[Dato og klokkeslett](../system-setup/date-and-time.md)).

## Widget-området

Midten av hver skjerm fylles med **widgeter**: modellbilde, timer,
telemetriverdier, trim-/potensiometerindikatorer og mer, alt plassert og
konfigurert av deg. Se [Skjermer](../displays/index.md) for hvordan du
legger til, flytter og konfigurerer widgeter, og
[Flere skjermer](../displays/additional-displays.md) for hvordan du legger
til mer enn den ene standardskjermen.
