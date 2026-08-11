---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Enheter

![Enheter](../assets/system-devices.png)

Kalles **Device config** i menyen — verktøy for å konfigurere eksterne
enheter som er koblet til via S.Port/FBUS: sensorer, mottakere, «Gas
Suite», servoer, VTX og ESC. **DIY sensors** vises automatisk så snart en
DIY-sensor blir oppdaget. Se den enkelte enhetens egen bruksanvisning for
alle detaljer; denne siden dekker det som er felles for dem.

!!! note
    Dette har ingenting å gjøre med å velge hvilken RF-modul (intern eller
    ekstern) en *modell* sender på — det er en innstilling per modell, og
    er beskrevet i [RF System](../model-setup/rf-system.md).

Device config kan utvides: både brukere og FrSky kan legge til sider her
via Lua.

## Endre sensor-ID-er

Skjermene under Device config i Ethos lar deg endre en enhets **Physical
ID** og **Application ID** for S.Port direkte. Har du flere enheter med
samme funksjon, kobler du dem til **én om gangen**: oppdag hver enkelt i
[Telemetri → Oppdag nye sensorer](../model-setup/telemetry.md), endre
Physical ID og Application ID her i Device config, og gå deretter tilbake
og oppdag den på nytt under den nye ID-en.

## Eksempel: mottakere

![Modulvalg](../assets/system-devices-module-choice.png)

FrSkys stabiliserte mottakere kan konfigureres her når oppsett-Lua-skriptet
deres er installert (ett klikk, fra Lua-biblioteket i Ethos Suite). Det
finnes to konfigurasjonsveier, avhengig av mottakergenerasjon:

- **Stabilizer config** — nyere mottakere med «Avansert stabilisering»
  (gain-styring på kanal 13). To uavhengige stabiliseringsgrupper er
  tilgjengelige: Gruppe 1 dekker kanal 1–6, Gruppe 2 dekker 7–11 — slå av
  Gruppe 2 hvis du ikke bruker pinne 7–11 til stabilisering. En
  6-akse-kalibrering er innebygd og må kjøres én gang på en ny mottaker,
  og på nytt etter enhver oppgradering til fastvare v3.0.x (etter en
  fabrikktilbakestilling). Under kalibreringen for hver gruppe er det
  gamle «selvtest»-trinnet erstattet av uavhengig kalibrering av
  flyets horisontalstilling, kanalsenter og kanalendepunkter, og hver
  kanal kan aktiveres/deaktiveres individuelt. Konfigurasjoner (ikke
  kalibreringsdata) kan lagres til og gjenopprettes fra en PC.
- **SxR** — eldre mottakere, inkludert gamle modeller og Archer/Archer Pro,
  samt mottakere som SR10 Pro som (til tross for «SRx»-navnet) har Gain på
  kanal 9 i stedet for 13.

  ![Gjeldende enhet](../assets/system-devices-current.png)

!!! warning "Etter oppdatering til mottakerfastvare v3.0.x"
    Utfør en fabrikktilbakestilling (finnes under mottakerens Options i
    RF-oppsettet), bind på nytt og konfigurer alt på nytt — særlig
    Stab-funksjonene og 6-akse-kalibreringen. Dette kreves av den nye
    funksjonen i v3.0.x for lagring av failsafe-data; kontroller
    failsafe-funksjonen nøye etterpå.

FrSky North America publiserer en detaljert oppsettsguide for stabiliserte
mottakere, og det finnes en gjennomgangsvideo av FrSky Team Pilot Juan
Sanchez Garcia som dekker det samme.

## Konfigurering via senderens S.Port-kontakt

S.Port- og FBUS-enheter kan også konfigureres direkte gjennom
S.Port-kontakten på toppen av senderen, uten å gå via en bundet mottaker.

1. Koble enheten til senderens S.Port-kontakt (hvit/gul leder mot siden med
   hakket).
2. Gå til **System → Device config**, bla til enheten (for eksempel en
   FAS40 ADV strømsensor) og trykk `ENT`.
3. På konfigurasjonssiden setter du **Module** til **S.Port connector**.
4. Gjør endringene dine — Physical ID og Application ID må hver være
   unike — bla deretter ned og trykk **Save to flash**.

Dette gjelder både FBUS-enheter (se også [Praktisk guide: Konfigurere et
FBUS-system](../how-to/fbus-setup.md)) og vanlige S.Port-enheter som en
variometer.
