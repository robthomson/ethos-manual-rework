---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Variabler

![Variabler](../assets/model-vars.png)

Variabler («Vars») er navngitte beholdere for en modells egne
innstillingsverdier, og kan refereres hvor som helst ellers i
programmeringen — inkludert i [mikser](mixes.md). Ved å samle dem i sin
egen seksjon skilles modellens *konfigurasjonsdata* fra dens
*programmeringslogikk*: i stedet for å lete gjennom titalls mikser for å
finne og justere en verdi, ligger alt på ett sted med et meningsfylt
navn. Det er 64 Vars tilgjengelig; ingen finnes som standard. Legg til én
med **+**; trykk på en eksisterende Var for **Rediger**/**Flytt**/
**Kopier**/**Klone**/**Slett**.

![Legg til variabel](../assets/model-vars-add.png)

En Var kan inneholde en fast konstant, eller være justerbar innenfor
brukerdefinerte grenser (for å hindre at feilaktige verdier fører til
havari), og den kan inneholde *ulike* verdier per aktiv betingelse (f.eks.
per flymodus). Verdiene bevares mellom økter. En Var kan erstatte enhver
vanlig numerisk verdi overalt der
[Options-funksjonen](../getting-started/user-interface-and-navigation.md#the-options-feature)
er tilgjengelig (feltene med hamburgerikon).

!!! example
    Et seilfly med delte krengeror (der de innerste seksjonene også
    fungerer som landingsklaffer) ønsker én felles innstilling for
    krengeror-differensial som brukes overalt der alle fire rorflater
    virker som krengeror — en Var som inneholder denne ene verdien, og som
    refereres fra hver relevant miks, holder den konsistent og gjør at den
    bare må justeres på ett sted.

## Legge til en Var

![Ny variabel](../assets/model-vars-new_var.png)

- **Verdi** — gjeldende verdi (skrivebeskyttet visning).
- **Navn** — kan redigeres.
- **Kommentar** — fritekst som forklarer formålet.
- **Område** — nedre/øvre grense (én desimal, innenfor ±500%) som Var-ens
  verdi aldri kan overskride.

### Verdier

![Variabelverdier](../assets/model-vars-values.png)

- **Fast** — én enkelt konstant, med én desimal.
- **Flere/variabel** — **Legg til ny verdi** knytter en verdi til hver
  aktiv betingelse. F.eks. viser `Var12` 9% mens flymodus Thermal (FM4) er
  aktiv, og −3% mens Speed (FM5) er aktiv, med området begrenset til
  −10%…+15% slik at ingen av dem kan overskride fornuftige grenser:

  ![Flymodusavhengige verdier](../assets/model-vars-fm-dependent.png)
  ![Legg til en verdi](../assets/model-vars-add-value.png)

### Handlinger

![Variabelhandlinger](../assets/model-vars-actions.png)
![Legg til handling](../assets/model-vars-add-action.png)

Handlinger endrer verdien til en Var over tid, styrt av en inngang.

**Omdisponert trim** — overlater en av de fysiske trimmene til å justere
denne Var-en i stedet for sin normale funksjon, vanligvis begrenset til én
aktiv betingelse:

![Omdisponer en trim](../assets/model-vars-functions-repurpose.png)
![Velg trim som skal omdisponeres](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Omdisponer gasstrimmen til å justere en Var for
    kamberkompensasjon, men bare mens flymodus Landing (FM3) er aktiv, med
    området 0–25% og et steg på 1,0% per klikk. Utenfor denne aktive
    betingelsen går trimmen automatisk tilbake til sin vanlige funksjon.

**Aritmetiske handlinger** — styrt av en vilkårlig inngang:

- **Assign** — setter Var-en til en bestemt verdi.
- **Add** / **Subtract** / **Multiply** / **Divide** — regneoperasjoner mot
  gjeldende verdi.
- **Percentage** — bruker en prosentandel av den styrende inngangen.
- **Min** / **Max** — begrenser Var-en mot den styrende inngangen.

  ![Funksjonshandlinger](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` tildeler en Var 40% direkte; `FS1(edge)` legger til 2 for
    hvert trykk (begrenset av områdets maksimum); `FS2(edge)` trekker fra 2
    for hvert trykk (begrenset av områdets minimum). Alternativet **Edge**
    (langt trykk på funksjonsbryteren) er viktig her — uten det ville
    handlingen bli utført gjentatte ganger så lenge bryteren holdes inne, i
    stedet for én gang per trykk.

  ![Gjennomgått eksempel](../assets/model-vars-calc-example.png)
