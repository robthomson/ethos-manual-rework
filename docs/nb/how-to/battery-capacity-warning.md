---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Advarsel om batterikapasitet

Advarsel basert på **forbrukt kapasitet** (mAh) i stedet for spenning — et mer
direkte mål på hvor mye av pakken som faktisk er brukt opp. Det finnes to måter
å gjøre dette på, avhengig av hvilken maskinvare som er montert.

## Alternativ A: en ESC fra Neuron-serien

FrSkys Neuron-ESC-er rapporterer forbruket direkte — det er ikke nødvendig med
en beregnet sensor. Sett [Receiver Options → Telemetry
Port](../system-setup/devices.md) til S.Port, koble til telemetrikabelen fra
Neuron, og [søk opp
sensorer](../model-setup/telemetry.md#discovering-sensors) — sensoren du er
interessert i, er **ESC Consumption**.

1. Legg til en [logisk bryter](../model-setup/logical-switches.md) på `ESC
   Consumption`, sann over (for eksempel) 900mAh — omtrent 60 % av en pakke
   dimensjonert for å lande med ~30 % igjen i reserve.
2. Legg til [spesialfunksjonen Play
   audio](../model-setup/special-functions.md), med den nye bryteren som
   aktiveringsvilkår, og et **Play value**-steg for `ESC Consumption`.

Som en ekstra sikkerhet rapporterer Neuron-ESC-er også **ESC Voltage** — sett
opp en ny logisk bryter på samme måte som i [Advarsel om lav
batterispenning](low-battery-warning.md) (under 3,4 V/celle for 4s — f.eks.
13,6 V for en 4S-pakke), med sin egen Play audio-funksjon som gjentas hvert 5.
sekund.

## Alternativ B: en strømsensor + beregnet sensor

Hvis ESC-en ikke rapporterer forbruk, gjør en strømsensor (f.eks. FrSky
FASxxx) kombinert med en [beregnet **Consumption**-sensor](../model-setup/telemetry.md#calculated-sensors)
samme jobb.

### 1. Koble til og søk opp

![Strømsensor](../assets/how-to-consumption-telemetry-current-sensor.png)

Koble til S.Port-kabelen fra strømsensoren og søk den opp — den vises som
**Current**. Sett **Range** slik at den samsvarer med sensoren (f.eks. 0–100 A
for en FAS100):

![Redigering av strømsensor](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Opprett den beregnede Consumption-sensoren

![Opprett beregnet sensor](../assets/how-to-consumption-create-calc-select.png)
![Consumption-sensor](../assets/how-to-consumption-create-calc-sensor.png)

I Telemetry velger du **Create Calculated Sensor** → **Consumption**. Sett
enheten til `mAh` og **Range** til pakkens kapasitet (f.eks. 2800mAh);
**Source** settes til `Current`.

![Sensorredigering](../assets/how-to-consumption-sensor-edit.png)
![Sensorredigering 2](../assets/how-to-consumption-sensor-edit2.png)

Sett **Reset** til systemhendelsen `!Telemetry Active` — velg **Telemetry
Active**, hold `ENT` inne, og velg **Invert** — slik at den løpende summen
nullstilles automatisk når telemetrien faller ut (det vil si når modellen slås
av).

### 3. Varsler ved milepæler

![Logisk bryter for delta 200mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Legg til en logisk bryter som bruker funksjonen **Δ > X** på `Consumption`, slik
at den utløses hver gang verdien stiger med et fast trinn — f.eks. hver 200mAh,
som er en praktisk andel av en pakke på 2800mAh.

!!! tip
    Sett **Check interval** til `---` (uendelig), slik at den fortsetter å
    akkumulere mot neste terskel i det uendelige i stedet for å nullstilles
    etter et fast tidsvindu. Gi **Min Duration** en liten verdi større enn null
    under feilsøking — ved 0.0 er utløsningen for kortvarig til å kunne ses på
    skjermen.

Legg til en Play Audio-funksjon med denne bryteren som aktiveringsvilkår, og et
Play value-steg for `Consumption`:

![Avspilling av delta-varsel](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Advarsel om lav kapasitet

![Andre logiske bryter](../assets/how-to-consumption-lsw2-play-battlow.png)

En ny logisk bryter utløses én gang, når en fast terskel for lav kapasitet
passeres — f.eks. 2000mAh av en pakke på 2800mAh — kombinert med en Play
Audio-funksjon som gjentas hvert 10. sekund til modellen nullstilles:

![Play value ved lavt batteri](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value: consumption ved lavt batteri](../assets/how-to-consumption-sf2-play-value-consumption.png)
