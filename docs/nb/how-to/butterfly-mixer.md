---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Butterfly-miks (krokodille)

Butterfly-bremsing (også kalt crow) styrer synkehastigheten, hovedsakelig
på seilfly: krengerorene går moderat opp mens flapsene går mye ned, noe
som gir betydelig luftmotstand — ideelt for å styre en landingsinnflyging.
Denne gjennomgangen forutsetter et seilfly der flapskanalene allerede
finnes (opprettet av veiviseren i
[Modellvalg](../model-setup/model-select.md)), og bruker gasspaken som
bremseinngang: ingen butterfly med spaken opp, gradvis mer etter hvert som
den føres ned, med høyderorkompensasjon slik at seilflyet ikke stiger når
crow legges inn.

## 1. Deaktiver standard flapsmiksen

![Deaktiver flapsmiks](../assets/how-to-butterfly-flaps-disable.png)

Sett **Aktiv betingelse** for flapsmiksen som veiviseren opprettet, til
`---` — den skal ikke brukes.

## 2. Opprett Butterfly-miksen

![Butterfly-miks lagt til](../assets/how-to-butterfly-mix-added.png)

Trykk på en vilkårlig miks, velg **Legg til miks** → **Butterfly** fra
[mikssamlingen](../model-setup/mixes.md#mix-libraries), plassert etter den
(nå deaktiverte) flapsmiksen.

## 3. Konfigurer inngangen

![Gassinngang](../assets/how-to-butterfly-mix-source-thr.png)

Sett **Inngang** til **Gass**. Siden gass normalt leser maksimum med
spaken opp, og butterfly må være 0 med spaken opp, holder du `ENT` inne på
Gass og velger **Inverter**:

![Inverter gass](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Invertert gass](../assets/how-to-butterfly-mix-source-thr-neg.png)

Inngangen leser nå 0 med spaken helt opp, og feltet viser `-Throttle` som
bekreftelse på inverteringen. Sett **Aktiv betingelse** til en
landingsflymodus (eller en annen bryter) hvis butterfly ikke alltid skal
være tilgjengelig.

## 4. Legg til en dødsonekurve

![Kurvevalg](../assets/how-to-butterfly-mix-curve-select.png)

En liten dødsone i spakens nullende hindrer utilsiktet utslag som følge av
små spakvariasjoner nær endestoppet. Legg til en egendefinert 3-punktskurve
(f.eks. med navnet «Crowdb») med **Enkel modus** av, slik at X-punktene kan
flyttes:

![3-punktskurve](../assets/how-to-butterfly-mix-curve-3pt.png)
![Kurvepunkter](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    Når du legger en egendefinert kurve til Butterfly-miksen, fjernes
    miksens interne 0–100-forskyvning (som normalt legges på automatisk) —
    kurven selv må nå gjengi denne 0–100-transformasjonen. I dette
    eksempelet holder utgangen seg på 0 % til gasspaken når −90 %, og
    stiger deretter lineært til 100 %:

    ![Kurve lagt til](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Konfigurer krengeror og flaps

![Krengerorutgang](../assets/how-to-butterfly-mix-ailerons.png)

En moderat heving av krengerorene (f.eks. 20 %) kombinert med et stort
flapsutslag er den vanlige fordelingen. Flaps trenger vanligvis langt mer
vandring nedover enn oppover — dette oppnås ofte ved å forskyve
flapsservoenes servoarmer 20–30° fra nøytral i selve linkasjen, slik at
flapsene står omtrent halvveis nede ved servonøytral:

![Flaps opp](../assets/how-to-butterfly-mix-flaps-up.png)
![Flaps ned](../assets/how-to-butterfly-mix-flaps-down.png)

Sett vekten på flapsmiksen høyt (f.eks. −180 %) for maksimal vandring; den
faktiske fysiske vandringen bestemmes av Min/Maks under
[Utganger](../model-setup/outputs.md).

!!! tip
    For å unngå å overbelaste servoene bør du starte med konservative
    Min/Maks-verdier under Utganger (f.eks. ±30 %) og utvide dem forsiktig
    under den endelige innstillingen, med øye for at noe kjører seg fast.

## 6. Legg til en offsetmiks for «flaps nøytral»

![Offsetmiks på 80 %](../assets/how-to-butterfly-offset-mix-80.png)

Siden forskyvningen av servoarmene gjør at flapsene står med ~20–30 %
utslag ved servonøytral, brukes en **Offsetmiks** for å føre dem tilbake
til reell nøytralstilling for normal flyging. Start med en offset på 80 %
(skal finjusteres), med 2 utgangskanaler tilordnet begge flapskanalene:

![Flaps opp med offset](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Flaps ned med offset](../assets/how-to-butterfly-offset-mix-flaps-down.png)

Med gasspaken helt opp (Butterfly-miksen av) kontrollerer du at
flapsmikserverdiene ligger på offsetverdien (80 %); når flapsspaken føres
til fullt utslag, skal mikserutgangen flytte seg tilsvarende hele vekten
(f.eks. fra 80 % ned til −100 %, et utsving på 180 %). Finjuster de
faktiske vandringsgrensene under Utganger med Min/Maks eller en kurve.

## 7. Legg til kompensasjonskurve og miks for høyderoret {: #7-add-the-elevator-compensation-curve-and-mix }

![Kompensasjonskurve](../assets/how-to-butterfly-comp-curve.png)
![Punkter på kompensasjonskurven](../assets/how-to-butterfly-comp-curve-points.png)

Siden kompensasjonen som kreves er ikke-lineær, bør du bruke en kurve
istedenfor en fast vekt. Definer en egendefinert 5-punktskurve (f.eks.
«EleComp») — i dette eksempelet starter den på 12 %/10 %/8 %/5 %/0 % over
punktene; uten et kjent utgangspunkt for din flykropp må disse finnes
empirisk.

Deretter gjør du kurven om til en verdi som kan brukes som **Vekt** i en
miks: legg til en [Fri miks](../model-setup/mixes.md#mix-libraries)
(«EleCompx») med Gass som kilde og EleComp-kurven tilknyttet, med utgang
til en høy, ubrukt kanal (f.eks. CH20):

![Kompensasjonsmiks på CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

Tilbake i Butterfly-miksen holder du `ENT` inne på **Vekt** for
høyderorutgangen, velger **Bruk en kilde** og deretter CH20 (EleCompx) fra
kategorien Kanaler:

![Høyderor med CH20 som kilde](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Velg kilde](../assets/how-to-butterfly-mix-ele-use-source.png)

Butterfly-miksen er nå ferdig konfigurert:

![Høyderorkompensasjon konfigurert](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Kontroller med kanalvisning

![Kanalvisning](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Bytt til [kanalvisning](../model-setup/mixes.md#per-channel-view) for
høyderoret for å se alle bidragende mikser (spakinngang +
butterfly-kompensasjon) oppdatere seg samtidig når gass-/bremsespaken
beveges — mye enklere å feilsøke enn den flate tabellvisningen.

!!! tip
    Data om nødvendig høyderorvandring i forhold til flapsutslag (fra
    flykroppens produsent eller fra fellesskapet) er verdt å ha før du
    stiller inn startverdiene i kompensasjonskurven. Mangler du dette, kan
    du starte med noen få millimeter høyderorvandring per fullt flapsutslag
    og finjustere derfra.
