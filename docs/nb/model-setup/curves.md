---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Kurver

![Kurvetyper](../assets/model-curves-type.png)

Gjenbrukbare responskurver for [Mikser](mixes.md#anatomy-of-a-mix) eller
[Utganger](outputs.md#editing-a-channel) — den innebygde Expo er tilgjengelig
direkte i begge, men alt mer avansert defineres her (eller via
**Legg til kurve**, som er tilgjengelig direkte fra begge redigeringsskjermene). Opptil 50
kurver er tilgjengelige; ingen finnes som standard (Expo er alltid innebygd
uansett). Legg til en med **+**; trykk på en eksisterende kurve for
**Rediger**/**Flytt**/**Kopier-lim inn**/**Klon**/**Slett**.

![Legg til kurve](../assets/model-curves-add.png)

## Kurvetyper

- **Expo** — standardverdi 40; positiv verdi demper responsen rundt
  senter, negativ verdi gjør den skarpere. Demping rundt midtstilling bidrar til å unngå
  overstyring, særlig for mindre erfarne piloter.

  ![Expo](../assets/model-curves-expo.png)

- **Funksjon** — et lite utvalg faste matematiske former:

  ![Funksjonstyper](../assets/model-curves-fn-types.png)

  - **x > 0** — sender kilden uendret gjennom så lenge den er positiv;
    gir ut 0 når den er negativ.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — speilbildet: sender gjennom når verdien er negativ, 0 når den er
    positiv.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — sender kilden gjennom som absoluttverdi (alltid
    positiv).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — gir ut 100 % når kilden er positiv, 0 når den er
    negativ (en hard bryter, ikke en gjennomsending).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — gir ut −100 % når verdien er negativ, 0 når den er positiv.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — gir ut −100 % når verdien er negativ, +100 % når den er positiv.

    ![|f|](../assets/model-curves-fn-barf.png)

  Alle kurvetyper — også Funksjon — har i tillegg en **Offset**, som forskyver
  kurven opp eller ned på Y-aksen (én desimals presisjon, som for Y-verdier
  generelt):

  ![Funksjons-offset](../assets/model-curves-fn-xgt0-offset.png)

- **Egendefinert** — en punktbasert kurve, 5 punkter som standard, opptil 21.

  ![Egendefinert kurve med 5 punkter](../assets/model-curves-custom5.png)

  - **Myk** — trekker en jevn kurve gjennom alle punktene i stedet for
    rette segmenter mellom dem.

    ![Utjevnet kurve](../assets/model-curves-custom5-2-smooth.png)

  - **Enkel modus** — **På** begrenser redigeringen til jevnt fordelte
    Y-koordinater (X er fast); **Av** tillater redigering av både X og Y
    for hvert punkt, med unntak av endepunktene −100 %/+100 %, som er låst siden
    kurven alltid må dekke hele signalområdet.

    ![Enkel modus av](../assets/model-curves-custom-easy-off.png)

  **Redigeringskontroller** (samme mønster som [redigeringsverktøyet for
  balansekurver under Utganger](outputs.md#balance-channels)):

  - **Kilde** — kurvens egen(e) mikskilde(r) som standard, eller **Automatisk
    analog inngang** for å fange opp den første spaken/glidebryteren/potensiometeret som beveges.
  - Snapping til nærmeste punkt med rotasjonsbryteren, og en **Lås**-veksling
    for å fryse inngangene mens du observerer den resulterende bevegelsen av
    styreflaten.
  - En sanntidsmarkør viser gjeldende inngangsverdi som driver kurven, slik at
    du lettere kan justere den inn mot et punkt før du endrer det.

## Drive en kurve fra en Var

Både en funksjonskurves **Offset** og et enkelt punkt på en **Egendefinert**
kurve kan drives av en [Var](variables.md) i stedet for en fast verdi —
og denne Var-en kan i sin tur justeres under flyging via en omdisponert trim:

![Funksjons-offset fra en Var](../assets/model-curves-fn-offset-var.png)
![Egendefinert kurvepunkt fra en Var](../assets/model-curves-custom-with-var.png)

Se [Variabler](variables.md) og [Praktisk guide: Kompensasjonskurve som kan
justeres under flyging](../how-to/in-flight-compensation-curve.md) for et fullt
gjennomgått eksempel på dette mønsteret.
