---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Justerbar kompensasjonskurve under flyging

## Hvorfor

Når flapsene settes ut, endres vingens profilkrumning – høyvingede fly har
en tendens til å stige brått («ballooning»), mens lavvingede fly har en
tendens til å synke – noe som krever en høyrorkorreksjon som ikke er
lineær med flapsutslaget, altså en kurve i stedet for en fast forskyvning.
Denne gjennomgangen bruker [Vars](../model-setup/variables.md) for å gjøre
punktene i en kompensasjonskurve justerbare **under flyging**, via en
omdisponert gasstrim, styrt av hvilket kurvepunkt flapsspaken befinner seg
nærmest – og bygger videre på trinnet med høyrorkompensasjon i [Praktisk
guide: Butterfly-mikser](butterfly-mixer.md).

## 1. Velg kurvetype

En [egendefinert kurve](../model-setup/curves.md) med 5 punkter er
tilstrekkelig for jevn kompensasjon uten unødvendig kompleksitet. Punkt 5
(helt til høyre, flapsspaken helt opp / ingen flaps) er alltid låst til
null – ingen kompensasjon er nødvendig når flapsene ikke er ute. De øvrige
4 punktene gjøres justerbare med Vars. Siden flapsspaken ofte vil stå
mellom to definerte punkter, må begge punktene på hver side av spaken
kunne justeres samtidig i denne overlappsonen.

## 2. Beregn overlappende områder

Områder fra punkt til punkt (tilpasset, med tillatelse, fra Mike Shellims
«Crow-aware adaptive elevator trim» for OpenTX på rc-soar.com – utvidet
noe slik at området for Pt2 strekker seg helt til +100 %, av grunnen som
forklares i [Trinn 6](#6-apply-the-curve)):

| Område for flapsspaken | Aktive punkt(er) |
|---|---|
| +100 % til +45 % | Kun Pt2 |
| +45 % til +20 % | Pt2 og Pt3 |
| +20 % til −20 % | Kun Pt3 |
| −20 % til −45 % | Pt3 og Pt4 |
| −45 % til −90 % | Kun Pt4 |
| −90 % til −100 % | Kun Pt5 |

## 3. Konfigurer de logiske bryterne

![Logiske brytere for adaptive punkter](../assets/how-in-flight-comp-lsws.png)

Fire [logiske brytere](../model-setup/logical-switches.md), hver med
funksjonen **Range** på flapsspaken (gasspaken), aktive når spaken står i
sonen til det aktuelle punktet:

- `AdaptivePt2` – område 20 % til 100 % (utvidet til 100 % nettopp for at
  Pt2 skal kunne justeres selv uten flaps ute – se Trinn 6).

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` – område −45 % til 45 %.

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` – område −90 % til −20 %.

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` – område −100 % til −90 %.

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. Definer justerings-Vars

![Oversikt over Vars](../assets/how-in-flight-comp-vars.png)

Fire [Vars](../model-setup/variables.md), `VAdjPt2`–`VAdjPt5`, hver med
område 0–50 % (utvid ved behov) og en **omdisponert gasstrim** som handling
– trinnstørrelse 1,0 % og den tilhørende logiske bryteren som aktiv
betingelse:

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![VAdjPt2-handling](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![VAdjPt3-handling](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![VAdjPt4-handling](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![VAdjPt5-handling](../assets/how-in-flight-comp-var-vadjpt5-2.png)

Siden bare én logisk bryter (høyst to, i overlappsonene) er aktiv om
gangen, kan samme fysiske trim trygt justere ulike Vars avhengig av
flapsposisjonen.

## 5. Definer kompensasjonskurven

![Kompensasjonskurve](../assets/how-in-flight-comp-var-comp-curve.png)
![Punkter i kompensasjonskurven](../assets/how-in-flight-comp-var-comp-curve-pts.png)

En ny egendefinert kurve med 5 punkter (f.eks. «EleComp») med **Smooth**
aktivert. Hold `ENT` inne på punktene 1–4 og velg **Use a source** for å
tilordne henholdsvis `VAdjPt5`…`VAdjPt2` (punkt 5 forblir låst til 0, i
henhold til Trinn 1).

## 6. Bruk kurven {: #6-apply-the-curve }

Bruk denne kurven på nøyaktig samme sted som i [Praktisk guide:
Butterfly-mikser](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix),
der EleComp-kurven kobles til miksen for høyrorkompensasjon.

Der det er mulig, bør du starte med reelle data (anbefalinger fra
produsenten, innlegg fra miljøet) om hvor mye høyrorutslag et gitt
flapsutslag krever; ellers er noen få millimeter kompensasjon ved fulle
flaps et rimelig utgangspunkt.

!!! tip "Fremgangsmåte for innstilling"
    Start med små flapsutslag og små trimjusteringer. `AdaptivePt2` kan
    stilles inn **helt uten flaps ute** – legg inn litt flaps, ta dem inn
    igjen, og legg til litt kompensasjon om gangen, i stedet for å kjempe
    mot en modell som stiger eller synker mens du prøver å trimme under
    press. Legg inn litt flaps igjen for å kontrollere, og juster videre
    ved behov. Når Pt2 føles riktig, går du videre til neste punkt rundt
    midtstilling av spaken – hvis Pt2 krevde en stor trimendring, er det
    verdt å lande og sette de gjenværende punktene til å være litt større
    enn det forrige, i stedet for å gjette i blinde.
