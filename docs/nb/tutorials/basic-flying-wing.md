---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Grunnleggende eksempel med flyvende vinge (elevon)

En flyvende vinge med elevon og to servoer, der de anbefalte rate-/Expo-/miksforholdene fra Dreamflight Weasel brukes som et konkret gjennomarbeidet eksempel. Fullfør [Første oppsett av senderen](initial-radio-setup.md) først.

## Trinn 1. Kontroller systeminnstillingene {: #step-1-confirm-system-settings }

Standardrekkefølgen **AETR**, med **[Første fire kanaler låst](../system-setup/controls.md#first-four-channels-fixed)** slått **AV**. Registrer (hvis ACCESS) og bind mottakeren via [RF-system](../model-setup/rf-system.md) før du fortsetter.

## Trinn 2. Finn ut hvilke servoer/kanaler som kreves

På en elevon-flykropp kombinerer [mikser](../model-setup/mixes.md) inngangene fra krengeror og høyderor på begge de fysiske rorflatene — til sammen bare 2 kanaler, der hver av dem er en blanding av begge inngangene.

## Trinn 3. Opprett en ny modell

![Opprett flymodell](../assets/tut-wing-eg-wiz-create-airplane.png)

Start veiviseren **Airplane** fra [Modellvalg](../model-setup/model-select.md), og velg **Non stabilized receiver**.

![Ingen motor](../assets/tut-wing-eg-wiz-no-engine.png)

Velg **No engine**, godta standardvalget med 2 krengerorkanaler, og velg **No flaps**.

![Ingen halefinne](../assets/tut-wing-eg-wiz-no-tail.png)

Velg **None** som haletype — dette er det som får Ethos til å bygge elevon-miksen automatisk (inngangene fra krengeror + høyderor, begge på de samme to kanalene). Gi modellen et navn (f.eks. «Weasel»), velg et bilde, og fullfør — modellen blir den aktive modellen i kategorien Airplane.

## Trinn 4. Gjennomgå og konfigurer miksene

![Oversikt over mikser](../assets/tut-wing-eg-mixes.png)

Veiviseren oppretter en Ailerons-miks på kanal 1+2, fulgt av en Elevators-miks *også* på kanal 1+2 — begge inngangene virker på begge elevon-kanalene, og det er hele poenget med elevon-miksing.

### Krengeror

![Krengerormiks](../assets/tut-wing-eg-mixes-ail-mix.png)

**Weight/Rates** — ifølge håndboken til Weasel bør utslaget på krengeroret være omtrent 3× utslaget på høyderoret, og de to skal summere seg til 100 %: **75 %** krengeror, **25 %** høyderor. Low rates ligger på omtrent halvparten av high rates: **36 %** krengeror low, **12 %** høyderor low.

![Vekting for krengerormiks](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — Weasel anbefaler 35 % high / 20 % low, aktivert med bryter SB nede, noe som flater ut responsen rundt spaknøytral.

**Differensial** — lite på denne flykroppen, omtrent **4 %**:

![Krengerordifferensial](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Se [Grunnleggende eksempel med fastvinge](basic-fixed-wing.md#ailerons) for hvorfor differensial er viktig — samme resonnement om negativ gir gjelder her.)

### Høyderor

![Høyderormiks](../assets/tut-wing-eg-mixes-ele-mix.png)

Samme mønster: **25 %**/**12 %** high/low rates, og samme Expo-verdier som for krengeroret.

### Sideror

![Sidrorormiks](../assets/tut-wing-eg-mixes-rud-mix.png)

Weasel har ikke sideror — flyvende vinger trenger vanligvis ikke det. Hvis en elevon-modell *likevel* trenger sideror, legg det til som en [Fri miks](../model-setup/mixes.md#mix-libraries) på kanal 3.

## Trinn 5. Bind mottakeren

Som i [Trinn 1](#step-1-confirm-system-settings) — registrer/bind før du går videre, og vurder å koble fra servolenkene eller redusere utslagene til Min/Max-grensene er satt, for å unngå å overbelaste noe.

## Trinn 6. Gjennomgå miksene

Utgangskanal 1/2 kan gis navnene **Elevon1**/**Elevon2**. Med fullt krengerorutslag til høyre viser kanal 1 (høyre, oppgående) 75 %, mens kanal 2 (venstre, nedgående) viser 72 % — differansen på 3 % *er* differensialet i praksis. Legg fullt høyderorutslag ned på toppen av dette, og kanal 1 blir 75+25 = 100 %, mens kanal 2 blir 72−25 = 47 %.

## Trinn 7. Konfigurer maksimale servoutslag

![Fullt krengerorutslag](../assets/tut-wing-eg-outputs-full-ail.png)
![Fullt krengerorutslag + fullt høyderorutslag](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Sentrer hver servo med **PWM center** først. Anbefalt maksimalt utslag for Weasel er 25 mm krengeror + 10 mm høyderor = 35 mm totalt — gi både fullt samvirkende *og* fullt motvirkende krengerors-/høyderorutslag, og kontroller at ingen av dem overskrider mekaniske grenser eller servogrensene før du setter de endelige utslagene.

- **Min/Max** — absolutte grenser som aldri overstyres; å redusere dem reduserer utslaget i stedet for å kutte det av. Standard ±100 %, kan utvides til ±150 % om nødvendig.
- **Curve** — ofte raskere og mer fleksibelt enn å justere Min/Max/Subtrim direkte, med fordelen av en live graf. En 3-punktskurve passer for de fleste utganger; en 5-punktskurve på den andre elevonen gjør det enkelt å synkronisere utslaget i 5 punkter mot den første. Når du bruker en kurve til dette, la Min/Max/Subtrim stå på gjennomgangsverdiene (−100/100/0, eller −150/150/0 med utvidede grenser) og la kurven stå for formingen i stedet.
