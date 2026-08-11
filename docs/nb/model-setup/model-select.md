---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modellvalg

![Modellveiviser – fly](../assets/model-modelselect-model-wizard-airplane.png)

Oppretter, velger, klone og sletter modeller, og administrerer de
brukerdefinerte kategorimappene modellene er organisert i.

## Administrere modellmapper

![Modellmapper](../assets/model-modelselect-folders.png)

Ethos lar deg gruppere modeller i egne mapper – typisk noe som Fly,
Seilfly, Heli, Quad, Warbird, Båt, Bil, Mal eller Arkiv. Før du oppretter
noen, ligger modellene i en automatisk **Uncategorized**-mappe (opprettet
ved oppgradering til Ethos 1.1.0 alpha 17+, eller når en modellfil kopieres
inn i `\Models` fra et annet sted). Ethos sletter mappen igjen så snart den
er tom.

For å opprette en mappe trykker du **+** ved siden av «Uncategorized»
(eller holder inne `PAGE` opp/ned), gir den et navn (opptil 15 tegn) og
bekrefter. Mappene sorteres alfabetisk, med **Uncategorized** alltid
sist, og svarer direkte til undermapper under `\Models` på SD card/eMMC.
Ved å trykke på et mappenavn åpnes gi nytt navn/slett – sletting av en
mappe flytter eventuelle modeller i den tilbake til Uncategorized.

![Bytt mappe](../assets/model-modelselect-folder-change-select.png)

For å flytte en modell trykker du på ikonet dens, velger **Bytt mappe** og
trykker deretter på målmappen:

![Velg mappe](../assets/model-modelselect-folder-airplane-select.png)

## Legge til en ny modell

![Opprett modell](../assets/model-modelselect-model-create.png)

Velg kategorien modellen skal opprettes i, trykk **+** og deretter
**Opprett modell** for å starte veiviseren (opprett kategorien først hvis
den ikke finnes ennå). Det finnes veivisere for **Fly**, **Seilfly**,
**Helikopter**, **Multirotor** og **Annet**; hver av dem går gjennom det
grunnleggende oppsettet for den aktuelle flytypen, inkludert valgfrie
forhåndsdefinerte mikser for FrSky stabiliserte mottakere (gain,
stabiliseringsmodus). Modellnavn kan være opptil 15 tegn.

### Stabiliserte mottakere og kanalrekkefølge

![Veiviser: fly](../assets/model-modelselect-model-wizard-airplane.png)

FrSky stabiliserte mottakere krever spesifikt kanalrekkefølgen **AETR** –
la [Spaker → Kanalrekkefølge](../system-setup/controls.md) stå på
AETR-standarden med **Første fire kanaler låst** aktivert, slik at
veiviserens resultat samsvarer med det mottakeren forventer.

Veiviseren tildeler kanaler fra høyre mot venstre. For 2 krengeror + 1
høyderor + 1 sideror + 1 motor blir det:

| Kanal | Funksjon |
|---|---|
| 1 | Krengeror 1 (høyre krengeror) |
| 2 | Høyderor |
| 3 | Gass |
| 4 | Sideror |
| 5 | Krengeror 2 (venstre krengeror) |

Med denne tildelingen er krengerordifferensial **positiv** i det normale
tilfellet (mer utslag opp enn ned). FrSkys egne mottakermanualer
dokumenterer for tiden den *motsatte* konvensjonen (fra venstre mot høyre,
slik at kanal 1 = venstre krengeror og kanal 5 = høyre krengeror) – i så
fall må differensialen være **negativ** for å gi samme fysiske virkning.

!!! tip
    Det anbefales å bruke Ethos-konvensjonen konsekvent – alle
    stabiliseringsfunksjoner fungerer korrekt uansett, siden
    kompensasjonsretningen settes under stabiliseringsoppsettet. Hvis du
    likevel må følge konvensjonen i mottakermanualen, er den enkleste
    veien å bygge modellen med veiviseren som normalt, og deretter bruke
    **Bytt kanaler** i [Utganger](outputs.md) for å bytte om de to
    krengerorkanalene etterpå – dette beholder positivt fortegn på
    differensialen i krengerormikseren.

### Trinn i veiviseren

![Veiviser: haletype](../assets/model-modelselect-model-wizard-tail.png)
![Veiviser: antall krengeror/flaps](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Veiviser: antall høyderor/sideror](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Veiviser: motor](../assets/model-modelselect-model-wizard-engine.png)
![Veiviser: omfordeling av kanaler](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Veiviser: navn](../assets/model-modelselect-model-wizard-name.png)
![Veiviser: mottaker](../assets/model-modelselect-model-wizard-rx.png)

For et **Fly** går veiviseren, etter haletype og antall styreflater, videre
til antall motorkanaler og deretter antall kanaler for krengeror/flaps.

**Halekonfigurasjon** er et valg mellom tradisjonelt krysshale, V-hale
eller ingen hale (delta/flygende vinge):

- **Delta/flygende vinge** – når du oppretter en Fly-modell med 2
  krengeror og ingen halestyreflater, bygges elevon-miksing automatisk,
  med standardvekter på 50 % slik at fullt samtidig utslag på krengeror +
  høyderor fortsatt gir 100 % totalt.
- **Delta der en stabilisert mottaker gjør miksingen** – velg i stedet 1
  krengeror og 1 høyderor; elevon-miksingen skjer i mottakeren, i henhold
  til dens egen manual.
- **Delta med egne krengeror- og høyderorflater** – la veiviseren kjøre som
  om modellen har hale; den konfigurerer de nødvendige krengeror- og
  høyderorkanalene (med eller uten sideror), og det opprettes ingen
  elevon-miksing.

Trinnet for **omfordeling av kanaler** lar deg overstyre veiviserens
standardtildeling, men husk at stabiliserte mottakere krever kanalene i en
bestemt rekkefølge (sjekk mottakerens egen dokumentasjon). Det siste
trinnet setter modellnavnet og knytter til et bilde.

Den ferdige modellen havner i den kategorimappen som var aktiv da
veiviseren ble startet, alfabetisk sortert innenfor mappen. Se [Enkelt
eksempel med fastvinge](../tutorials/basic-fixed-wing.md) for en
fullstendig gjennomgang.

## Motta en modell fra en annen Ethos-sender

![Motta modell](../assets/model-modelselect-model-receive.png)

Velg målkategorien, trykk **+** og deretter **Motta modell** – senderen
venter og viser sin Bluetooth-adresse slik at avsenderen kan finne den. På
sendersiden trykker du på modellen og velger **Send modell**; den
mottakende senderen ber om bekreftelse av det innkommende filnavnet før
den godtar.

## Velge en modell

Trykk **Modellvalg** for å få opp modellisten.

!!! note "Modellkonvertering etter en Ethos-oppgradering"
    Ethos konverterer hver modell enkeltvis første gang den blir *valgt*
    etter en versjonsoppgradering, ikke alle samtidig ved oppgraderingen –
    det er ingen merkbar forsinkelse, og det er trygt å gjøre på et
    senere tidspunkt, også under en enda nyere Ethos-versjon. Datoen for
    **Sist endret** nederst på valgskjermen oppdateres når en konvertering
    skjer (eller når du redigerer modellen – ellers er den uendret).

**Hurtigvalg** – et langt trykk på skjermen eller langt trykk på `ENT` på
et modellikon bytter til modellen umiddelbart.

**Meny for modelladministrasjon** – trykk på en modell for å markere den,
og trykk igjen for å åpne menyen:

- **Sett som gjeldende modell**
- **Klon** – dupliserer modellen. En klone får automatisk et nytt
  mottakernummer; hvis du i stedet endrer mottakernummeret på originalen,
  fungerer den uten at det er nødvendig å binde på nytt.
- **Bytt mappe**
- **Send**/**Motta** – til eller fra en annen sender, som beskrevet over.
- **Slett** – tilbys bare for en modell som ikke er den gjeldende.
