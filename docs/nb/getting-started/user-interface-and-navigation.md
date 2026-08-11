---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Brukergrensesnitt og navigasjon

Ethos kan betjenes utelukkende med **rotasjonsenkoderen** på høyre side (drei
for å flytte markeringen, trykk for `ENT`) og `RTN`-tasten for å gå ut av en
meny — berøringsskjermen, der den finnes, er en snarvei til de samme
handlingene, ikke en egen arbeidsmåte. `MDL`, `DISP` og `SYS` går direkte til
Modelloppsett, Konfigurer skjermer og Systeminnstillinger (de samme tre flisene
som i bunnlinjen); et langt trykk på `RTN` hvor som helst tar deg rett tilbake
til hjemskjermen.

## Nullstillingsmenyen

![Kontekstmeny](../assets/resetmenu.png)

Et langt trykk på `ENT` fra hjemskjermen åpner en nullstillingsmeny:

- **Nullstill flyging** — nullstiller telemetri, timere og funksjonsbrytere, og
  kjører [sjekklisten](../model-setup/checklist.md) før flyging på nytt.
- **Nullstill telemetri** — nullstiller kun telemetrien.
- **Nullstill timere** — nullstiller kun timerne.
- **Lås berøringsskjermen** — kan også nås ved å trykke `ENT` + `PAGE`
  samtidig i ett sekund fra hjemskjermen, eller som utløser for en
  [spesialfunksjon](../model-setup/special-functions.md).

## Redigeringskontroller

**Legge til funksjonelle elementer** — en timer, logisk bryter, spesialfunksjon,
kurve eller variabel opprettes ved å trykke på **+** ved siden av
kolonneoverskriftene i den aktuelle menyen. På en sender uten berøringsskjerm
markerer du et eksisterende element, trykker `ENT` og velger **Legg til** fra
menyen — det samme alternativet er også tilgjengelig på sendere med
berøringsskjerm.

### Virtuelt tastatur

![Teksttastatur](../assets/keyboard-text-azerty.png)

Når du berører et tekstfelt (eller trykker `ENT` på det), åpnes tastaturet på
skjermen. Tilbaketasten sletter til venstre for markøren; `PAGE` sletter til
høyre, og når markøren har nådd slutten av teksten, fortsetter den å slette fra
venstre. Ved å berøre selve feltet flytter du markøren til den posisjonen —
eller bruk `SYS`/`DISP` for å flytte den til venstre/høyre uten berøring.
Tasten **?123**/**abc** slår det numeriske tastaturet av og på (det inneholder
også spesialtegn):

![Numerisk tastatur](../assets/keyboard-text-numbers.png)

På en **sender uten berøringsskjerm** går du direkte inn i redigeringsmodus ved
å trykke `ENT` på et tekstfelt: drei encoderen for å bla gjennom små bokstaver,
store bokstaver, sifre og deretter spesialtegn, og trykk `ENT` for å sette inn
hvert enkelt tegn. `MDL` veksler mellom store og små bokstaver for tegnet
umiddelbart til høyre for markøren (og alle tegn som skrives etterpå, beholder
denne bokstavstørrelsen til den veksles igjen). `PAGE` sletter til høyre for
markøren; `SYS`/`DISP` flytter den til venstre/høyre.

## Kontroller for tallverdier

![Tallinntasting](../assets/keyboard-numbers.png)

Når du berører et tallfelt, åpnes en kontrollrad nederst på skjermen:
**`<`**/**`>`** endrer trinnstørrelsen (veksler mellom tierpotenser — f.eks.
0,01/0,1/1,0/10,0), **`-`**/**`+`** (eller rotasjonsenkoderen) justerer verdien
med dette trinnet, og **Mer** åpner flere alternativer:

![Alternativer for tallinntasting](../assets/keyboard-numbers-options.png)

- Gå til feltets standardverdi
- Sett til minimum / sett til maksimum
- Erstatt trinnvelgeren med en **glidebryter**

![Inntasting med glidebryter](../assets/keyboard-numbers-slider.png)

Glidebryteren (som også kan justeres med rotasjonsenkoderen) er raskere ved
grove endringer; **Deaktiver glidebryter** går tilbake til trinnvelgeren.
Verdier for telemetriområder redigeres på samme måte:

![Glidebryter deaktivert](../assets/keyboard-numbers-options-disable-slider.png)

## Alternativer-funksjonen {: #the-options-feature }

Nesten overalt der en verdi eller [kilde](#choosing-a-source) forventes, åpner
et langt trykk på `ENT` dialogen **Alternativer** — se etter det lille
menyikonet («hamburger») i øvre venstre hjørne av feltet som tegn på at
funksjonen er tilgjengelig.

### Verdialternativer

![Kildealternativer](../assets/source-with-options.png)

Dialogen for verdialternativer navngir parameteren som redigeres, og gir
valget mellom fast minimum/maksimum og å styre den fra en **kilde** (f.eks. et
potensiometer, for å justere verdien under flyging). Hvis feltet allerede
bruker en kilde, tilbyr det samme lange trykket i stedet å konvertere kildens
gjeldende verdi til en fast verdi:

![Konverter kilde til verdi](../assets/source-convert-to-value.png)

### Velge en kilde {: #choosing-a-source }

Ved å velge **Velg en kilde** åpnes en velger med to kolonner — først en
**kategori** (analoge kontroller, brytere, logiske brytere, trim, kanaler, en
gyroakse, en trenerkanal, en timer, en telemetrisensor eller en håndfull
spesialverdier), deretter det spesifikke elementet i kategorien:

![Kildemeny](../assets/source-menu.png)

Når en kilde er satt, åpner det samme lange trykket alternativer som er
spesifikke for hvilken type kilde det er:

**Alle kilder** —

- **Inverter** — negerer kilden (f.eks. aktiv når en bryter *ikke* er oppe, i
  stedet for når den er det).
- **Edge** — utløses én gang ved en overgang (usann→sann eller sann→usann) i
  stedet for å være aktiv hele tilstanden; vises med prefikset `†` på kilden.
  Tilgjengelig for brytere generelt, og spesielt for utløserbetingelsen til
  [Sticky-logisk bryter](../model-setup/logical-switches.md).

**Spakkilder** — alternativer av typen kalibrering/subtrim:

![Alternativer for spakkilde](../assets/source-stick-options.png)

**Bryterkilder** —

![Alternativer for 2-posisjonsbryter](../assets/source-2pos-options.png)
![Bryteralternativer](../assets/switch-options.png)

- **Negativ** — inverterer bryterhandlingen.
- **HalfRange** — for en 2-posisjonsbryter eller logisk bryter endres
  utgangsområdet fra ±100 % til 0–100 %.

**Trimkilder** —

![Alternativer for trimkilde](../assets/source-trim-options.png)

- **Negativ** — inverterer trimhandlingen (nyttig inne i handlingene til en fri
  miks).
- **Fullt område** — trim har som standard ±25 %; som kilde kan dette utvides
  til ±100 %.
- **Ignorer trenerinngang** — på en [logisk
  bryter](../model-setup/logical-switches.md) utelukkes bevegelse fra
  trenerinngangen fra å utløse bryteren. Typisk bruk: å registrere
  *hovedsenderens* egen spakbevegelse (f.eks. for å gripe inn umiddelbart hvis
  eleven gjør noe feil) uten at elevens spakbevegelser også utløser den.

**Variabelkilder** —

![Alternativer for variabelkilde](../assets/source-var-options.png)

- **Negativ** — negerer variabelens verdi for denne bruken.
- **Ignorer område** — noen felt har asymmetriske områder (f.eks. Min/Maks
  under Utganger, som går fra −150–0 % og 0–150 % respektivt). Med mindre en
  [variabel](../model-setup/variables.md) som brukes som kilde for feltet har
  et identisk område, bør du aktivere dette for å hoppe over Ethos' automatiske
  områdekonvertering og unngå uventede verdier.

**Telemetrisensorkilder** — reduser kilden til dens løpende minimum eller
maksimum i stedet for den momentane verdien (noen sensorer legger til flere
sensorspesifikke alternativer utover dette):

![Alternativer for sensor min/maks](../assets/source-sensor-options.png)
![Sensor maks valgt](../assets/source-sensor-maxi.png)
