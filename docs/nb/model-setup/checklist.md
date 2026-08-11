---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Sjekkliste

![Sjekkliste](../assets/model-checklist.png)

Et sett med sikkerhetskontroller før flyging som kjøres når senderen slås på
og/eller en modell lastes inn. Innebygde kontroller omfatter stillemodus,
failsafe ikke satt, bryter- og potensiometerposisjoner samt sender- og
RTC-batteri — bryterkontrollen viser hvilken retning hver bryter må flyttes,
markert med røde punkter på varselskjermen:

![Sjekkliste ved oppstart](../assets/model-checklist-at_start.png)

!!! note
    Både `OK` og `RTN` hopper helt over kontrollene før flyging, uavhengig av
    hva varselet på skjermen antyder.

## Kontroll av gass

![Kontrollfunksjon](../assets/model-checklist-check_function.png)

Aktiver og velg en operator — `<` (mindre enn), `~` (omtrent lik) eller `>`
(større enn) — mot en verdi; varsler hvis gasspaken er utenfor det denne
sammenligningen tillater.

## Kontroll av failsafe

Varsler hvis [failsafe](rf-system.md#failsafe) ikke er satt for gjeldende
modell.

!!! tip
    Det anbefales sterkt å la denne være aktivert.

## Kontroll av brytere

![Brytere](../assets/model-checklist-switches.png)
![Alternativer for bryterkontroll](../assets/model-checklist-switches-options.png)

Angi en bestemt posisjon ved oppstart for hver bryter (brytere med egendefinerte
navn fra [Systeminnstillinger →
Maskinvare](../system-setup/hardware.md#switches-settings) viser disse navnene).
**Last inn alle bryterposisjoner** registrerer de *nåværende* fysiske
posisjonene som ønskede posisjoner for alle brytere som ikke er merket med
**Ingen kontroll**.

## Kontroll av funksjonsbrytere

![Funksjonsbrytere](../assets/model-checklist-function-switches.png)
![Alternativer for kontroll av funksjonsbrytere](../assets/model-checklist-function-switches-options.png)

Samme prinsipp, for de seks
[funksjonsbryterne](model-edit.md#function-switches). **Last inn alle
funksjonsbryterposisjoner** fungerer på samme måte som ovenfor.

## Kontroll av potensiometere / glidebrytere

![Potensiometere](../assets/model-checklist-pots.png)
![Alternativer for potensiometerkontroll](../assets/model-checklist-pots-options.png)

Angir bestemte posisjoner for potensiometere/glidebrytere ved oppstart,
individuelt per betjening (`~`/`<`/`>`, som ved kontroll av gass). **Last inn
alle potensiometerposisjoner** registrerer nåværende posisjoner automatisk —
kontroller de automatisk valgte operatorene nøye etterpå, siden `~` kontra
`<`/`>` kanskje ikke stemmer med det du faktisk hadde tenkt.

## Brukerdefinert tekst

![Brukerdefinert sjekklistetekst](../assets/model-checklist-user-checklist.png)

Viser en fil med ren tekst eller utvidet tekst som en del av sjekklisten ved
oppstart, når den er installert for modellen. Se [Praktisk guide: Brukerdefinert
sjekklistetekst](../how-to/user-defined-checklist.md) for det fullstendige
oppsettet.
