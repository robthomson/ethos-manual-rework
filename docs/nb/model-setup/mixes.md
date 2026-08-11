---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mikser

![Mikser-ikon](../assets/model-icon-mixes.png)

Mikser er kjernen i modellprogrammeringen i Ethos — her rutes, formes og
kombineres inngangssignaler (spaker, brytere, sensorer, alt en
[kilde](../getting-started/user-interface-and-navigation.md#choosing-a-source)
kan nå) til utgangskanaler. Det kan defineres opptil 120 mikser per modell.

![Mikstabell](../assets/model-mixes.png)

Hvis modellen ble opprettet med veiviseren i **Modellvalg**, er de
grunnleggende miksene (krengeror, høyderor, gass, sideror og hva flystellet
ellers krever) allerede lagt inn her. Ved å velge en miks og trykke `ENT`
åpnes en kontekstmeny der du kan redigere den, legge til en ny miks, bytte
til [kanalvisning](#per-channel-view), endre rekkefølgen, duplisere eller
slette den. Inaktive mikser vises nedtonet, og sletting krever alltid
bekreftelse først.

## Oppbygningen av en miks {: #anatomy-of-a-mix }

Alle mikser har samme sett med felter, uansett hvilken kategori de kommer
fra. Miksen for **krengeror** er et representativt eksempel — mikser for
høyderor og sideror er bygget opp på samme måte.

![Krengerormiks](../assets/model-mixes-ail-edit.png)

![Redigering av krengerormiks](../assets/model-mixes-ail.png)

**Navn** — settes som standard til mikstypen, men kan redigeres.

**Betingelse** — standardverdien er *Alltid*. Kan begrenses til en
bryterposisjon, en funksjonsbryter, en logisk bryter, en flymodus, en
systemhendelse (gasskutt/gasshold) eller en trimposisjon, slik at miksen
bare virker så lenge betingelsen er sann.

**Flymoduser** — hvis flymoduser er definert, kan miksen i tillegg
begrenses til én eller flere av dem.

**Kurve** — en **Expo**-kurve er tilgjengelig som standard (0 = lineær;
positiv verdi demper responsen rundt midtstilling, negativ verdi gjør den
skarpere):

![Expo-kurve](../assets/model-mixes-ail-expo.png)

Enhver kurve som tidligere er definert under [Kurver](curves.md), kan
velges i stedet. Opptil 6 kurver kan stables på én miks, hver med sin egen
betingelse — hvis mer enn én betingelse er sann samtidig, gjelder den
kurven som ligger høyest i listen. Kurver brukes **før** rater.

**Rater** — én eller flere vektrader, hver eventuelt styrt av en bryter,
funksjonsbryter, logisk bryter, trimposisjon eller flymodus. Den første
raden er standardraden og er aktiv når ingen av de andre radenes
betingelser er oppfylt:

![Krengerorrater](../assets/model-mixes-ail-weight.png)

I stedet for en fast prosentverdi kan en rate styres fra en
[kilde](../getting-started/user-interface-and-navigation.md#choosing-a-source)
— for eksempel et potensiometer, for å justere raten under flyging:

![Rate styrt fra en kilde](../assets/model-mixes-ail-diff.png)

**Differensial** (-100 til 100, standard 0) — gir større utslag i én
retning enn i den andre. For krengeror er dette det klassiske trikset med
større utslag opp enn ned for å redusere negativ giring. Vises bare når
miksen har mer enn én utgangskanal; differensial krever spesifikt en
utgangskonfigurasjon av typen V-hale eller doble krengeror for å være
meningsfullt.

**Antall kanaler / utganger** — hvor mange utgangskanaler denne miksen
styrer, og hvilke fysiske utganger de tilordnes:

![Antall kanaler](../assets/model-mixes-ail-ch-count.png)

Et langt trykk på `ENT` på en utgangskanal andre steder i
brukergrensesnittet (f.eks. i [Utganger](outputs.md)) hopper direkte
tilbake til denne siden.

## Gassmiksen

Gassmiksen er en miks av samme type som krengeror/høyderor/sideror, men med
motorspesifikke sikkerhetsvalg.

![Gassmiks](../assets/model-mixes-thr.png)

**Inngang** — gasskilden, normalt gasspaken, men den kan byttes ut med et
potensiometer, en glidebryter, en bryter, en trim, en kanal, en gyroakse,
en trenerkanal, en timer eller en annen kilde.

**Tomgangstrim** — for forbrenningsmotorer lar den en egen trim justere
tomgangsturtallet uten å påvirke posisjonen for full gass. Med
tomgangstrim aktivert ligger gasskanalen på -75 % når spaken står på lav
tomgang, og gasstrimmen justerer deretter tomgangen mellom -100 % og -50 %:

![Meny for tomgangstrim](../assets/model-mixes-thr-trim-menu.png)

![Tomgangstrim i lav posisjon](../assets/model-mixes-thr-trim-low-position.png)

**Gasskutt** — en absolutt sikkerhetssperre: kanalen blir først aktiv når
gasspaken har passert tomgang, slik at et utilsiktet bryterslag ikke kan
starte motoren fra en posisjon med høy gass:

![Gasskutt](../assets/model-mixes-thr-cut.png)

**Gasshold** — holder kanalen på en fast verdi uavhengig av spakposisjon,
uten sikkerhetssperren som gasskutt gir:

![Gasshold](../assets/model-mixes-thr-hold.png)

Gass har også sitt eget antall utgangskanaler, på samme måte som alle andre
mikser:

![Antall gasskanaler](../assets/model-mixes-thr-ch-count.png)

!!! note "Gassperre"
    Ethos krever at inngangen til gassmiksen passerer -100 % før den armeres,
    uavhengig av innstillingene for gasskutt/gasshold — en modell opprettet
    med veiviseren i Modellvalg tar allerede hensyn til dette, men det bør
    også håndbygde gassmikser gjøre.

## Miksbiblioteker {: #mix-libraries }

Biblioteket med forhåndsdefinerte mikser i dialogen **Legg til miks** er
tilpasset modellkategorien som ble valgt da modellen ble opprettet — fly,
seilfly, helikopter og multirotor har hvert sitt sett:

![Miksbibliotek for fly](../assets/model-mixes-library-airplane.png)

![Miksbibliotek for seilfly](../assets/model-mixes-library-glider.png)

![Miksbibliotek for helikopter](../assets/model-mixes-library-heli.png)

![Miksbibliotek for multirotor](../assets/model-mixes-library-multirotor.png)

Alle bibliotekene inneholder også **Fri miks** — en universell mikstype
uten forhåndsdefinert inngang/utgang, mer fleksibel enn de spesialiserte
oppføringene, men den krever mer oppsett for å nå samme resultat.

## Kanalvisning {: #per-channel-view }

Når mange mikser er stablet på samme utgang, kan det være vanskelig å se
den samlede effekten i den flate tabellen ovenfor. Ved å velge en miks og
deretter **Vis etter kanal** grupperes i stedet alle mikser som påvirker én
utgang, sammen:

![Bytt til kanalvisning](../assets/model-mixes-chview-select.png)

![Sammenslått kanal](../assets/model-mixes-chview-collapsed.png)

![Høyderorkanal utvidet](../assets/model-mixes-chview-elevator.png)

Når du utvider sammendragsraden for en kanal, vises alle miksene som bidrar
til den, hver med sin sanntidsverdi både numerisk og grafisk — nyttig for å
bekrefte nøyaktig hvor mye en sekundærmiks (f.eks. kompensasjon fra flaps
til høyderor) legger til oppå den primære spakinngangen:

![Detaljer i kanalvisning for høyderor](../assets/model-mixes-chview-elevator-channel.png)

![Høyderorkanal med markert miks](../assets/model-mixes-chview-elevator-channel-view.png)

Hvis du velger en undermiks i stedet for sammendragsraden, åpnes samme
kontekstmeny som i den flate tabellen (rediger, bytt tilbake til
tabellvisning, slett):

![Velg tabellvisning fra kanalvisning](../assets/model-mixes-chview-table-view-select.png)

![Tilbake til tabellvisning](../assets/model-mixes-chview-back-at-mixes-view.png)
