---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Flymoduser

![Flymoduser](../assets/model-fm.png)

Flymoduser (flyfaser) gjør det mulig å velge mellom ulike oppsett for
samme modell med en bryter — seilfly kan bruke Start/Cruise/Speed/Termikk,
motorfly Normal/Takeoff/Landing, helikoptre Normal (oppspinning,
takeoff/landing) / Idle Up 1 (akrobatikk) / Idle Up 2 (3D). De fjerner det
meste av behovet for manuell omkobling og ny trimming underveis: en
flymodus kan ha sine egne uavhengige trim, og kan styre både
[Vars](variables.md) og [Mikser](mixes.md) — til sammen er det nok til å
dekke reelt kompliserte oppsett. Se [Enkelt eksempel med
fastvinge](../tutorials/basic-fixed-wing.md) for flymoduser brukt på en
virkelig modell.

Ingen flymoduser er definert som standard. Trykk på standardflymodusen og
velg **Rediger** for å gi den nytt navn, eller **Legg til** for å opprette
en ny — opptil 20 i alt.

## Navn

Et beskrivende navn — Cruise, Speed, Termikk, Takeoff, Landing, eller det
som passer.

## Aktiveringsbetingelse

![Skjema for flymodus](../assets/model-fm-form.png)

En ny flymodus er inaktiv til å begynne med (`---`). Når betingelsen er
satt, kan den styres av en bryter- eller knappeposisjon, en funksjonsbryter,
en logisk bryter, en systemhendelse (gasskutt/gasshold) eller en
trimposisjon.

**Standard**-flymodusen har ingen aktiveringsbetingelse i det hele tatt —
den er aktiv når ingen annen flymodus har en oppfylt betingelse. Bare én
flymodus er aktiv om gangen: den første (i prioritetsrekkefølge) hvis
betingelse er oppfylt. Den aktive modusen vises i halvfet skrift.

!!! warning "Legge til en flymodus i en eksisterende modell"
    En nylig lagt til flymodus er som standard aktiv i alle mikser som
    allerede er flymodusavhengige — kontroller at hver slik miks fortsatt
    fungerer riktig, særlig en **Lock**-miks som låser en kanal til en
    bestemt flymodus.

## Inn- og uttoning

Overgangstider for å tone jevnt mellom flymoduser (f.eks. 1 sekund hver
vei) — dette har bare effekt på mikser som selv er flymodusavhengige.

## Håndtering av flymoduser

![Flytt flymodus](../assets/model-fm-move.png)
![Velg for flytting](../assets/model-fm-move-select.png)
![Moduser 0–3](../assets/model-fm-0to3.png)

Trykk på en flymodus for **Rediger**, **Legg til**, **Klon** eller
**Slett**. En **klonet** flymodus arver innstillingene til opphavet i alle
mikser som bruker flymoduser — samme oppførsel, samme aktiv/inaktiv-status
— og derfor legges en klon som standard til som siste flymodus, for å
unngå at den forstyrrer de eksisterende. **Flytt** endrer prioriteten til
en flymodus: prioriteten går i stigende rekkefølge, og (som nevnt over) er
det den første med oppfylt betingelse som er aktiv.
