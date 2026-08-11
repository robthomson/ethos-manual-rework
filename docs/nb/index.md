---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos-manual

**Ethos** er operativsystemet som kjører på FrSky-sendere i Ethos-familien
(X20S, X20 Pro, X20 Pro AW, X18S med flere). Denne manualen dekker oppsett av
en modell fra grunnen av, konfigurasjon av senderens systeminnstillinger,
oppbygging av egendefinerte telemetriskjermer og Lua-skriptmiljøet som ligger
over alt dette.

!!! note "Under arbeid"
    Denne manualen er bygd opp fra grunnen av med utgangspunkt i den offisielle
    Ethos 1.6.3-manualen og det eksisterende settet med skjermbilder. Noen få
    sider (Ethos Suite, RF-system og et par praktiske guider) er ferdigskrevet,
    men mangler fortsatt skjermbilder — se [Skjermbilde-arbeidsflyt](contributing/screenshot-pipeline.md) og
    [Bidra](contributing/index.md) hvis du vil hjelpe til.

## Hvor du bør begynne

- Ny med Ethos? Begynn med [Komme i gang](getting-started/index.md) —
  oppbyggingen av hovedskjermen og hvordan navigasjonen fungerer, før du gjør
  endringer i innstillingene.
- Skal du sette opp en ny sender? Se [Systeminnstillinger](system-setup/index.md) for
  engangsinnstillingene som gjelder hele senderen (maskinvarekalibrering,
  varsler, batteri).
- Skal du programmere en modell? [Modelloppsett](model-setup/index.md) dekker mikser,
  utganger, flymoduser og alt annet som lagres per modell, og
  [Veiledningene](tutorials/index.md) går gjennom oppbygging av modeller med
  fast vinge, flyvende vinge og helikopter fra start til slutt.
- Skal du bygge en telemetriskjerm? Se [Skjermer](displays/index.md).
- Vil du løse en konkret oppgave raskt? Se [Praktiske guider](how-to/index.md).
- Skal du skrive eller installere Lua-skript/widgeter? Se [Lua-skript](lua-scripts/index.md).

## Sendere som dekkes

Denne manualen er primært skrevet med utgangspunkt i **X20S**, med
senderspesifikke forskjeller (X20 Pro, X20 Pro AW, X18S) omtalt i
[Merknader om senderen](radio-notes/index.md) der brukergrensesnittet avviker.
