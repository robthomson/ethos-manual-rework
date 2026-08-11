---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Av som standard. Still senderen inn som **Master** (instruktørens sender,
som mottar opptil 16 styresignaler fra eleven) eller **Slave** (elevens
sender, som sender et konfigurerbart antall kanaler til instruktøren).

## Master-modus

![Master-modus](../assets/model-trainer-master.png)
![Trainer-alternativer](../assets/model-trainer-options.png)

### Tilkoblingsmodus

![Alternativer for tilkoblingsmodus](../assets/model-trainer-link-mode-options.png)

- **Trainer cable** — en 3,5 mm mono lydkabel mellom de to senderne.
- **Bluetooth** —

  ![Bluetooth-tilkobling](../assets/model-trainer-link-mode-bt.png)

  - **Mode** — normal eller høy hastighet; bruk høy hastighet for lavere
    forsinkelse dersom begge senderne støtter det.

    ![Bluetooth-modus](../assets/model-trainer-link-mode-bt-mode.png)

  - **Local name** — Bluetooth-navnet som vises for andre enheter
    (standard `FrSkyBT`, kan redigeres).
  - **Local address** — denne senderens Bluetooth-adresse.
  - **Distant address** — adressen til den sammenkoblede senderen, når
    forbindelsen er opprettet.
  - **Search devices** (kun i Master-modus) — søker etter enheter i
    nærheten:

    ![Søker](../assets/model-trainer-link-mode-bt-search.png)
    ![Venter](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Velg enhet](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Tilkoblet](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Connect Last Device** / **Reset Module** — koble til igjen mot
    forrige sammenkobling, eller slette Bluetooth-modulens konfigurasjon
    fullstendig.

- **SBUS external module** — en SBUS-inngang på PXX-IN-pinnen i det
  eksterne modulrommet, for montering av en FrSky-mottaker med
  SBUS-utgang (f.eks. Archer RS) som mottakerende i en trådløs
  forbindelse — slik at **enhver** FrSky-sender kan fungere som elevens
  side (buddy box), bundet til den mottakeren.
- **CPPM external module** — samme prinsipp via en CPPM-inngang, for en
  eldre mottaker med CPPM-utgang.

### Aktiv betingelse

![Aktiv betingelse](../assets/model-trainer-active-condition.png)

En bryter/knapp, funksjonsbryter, logisk bryter, trimposisjon eller
flymodus som overlater kontrollen til eleven mens den er aktiv.

### Trainer-kanaler

![Redigering av aktiv betingelse](../assets/model-trainer-active-condition-edit.png)

Opptil 16 kanaler kan overføres fra eleven til masteren mens Aktiv
betingelse er sann. Trykk på en kanal for å konfigurere den enkeltvis:

- **Active condition** — en overstyring per kanal, f.eks. for å deaktivere
  bare elevens høyderorinngang i deler av en økt.
- **Mode** — **OFF** (deaktivert for trainer-bruk), **Add** (signalene fra
  master og elev summeres, slik at begge kan påvirke styringen samtidig)
  eller **Replace** (normalmodus — eleven har full kontroll over denne
  kanalen mens funksjonen er aktiv).
- **Percent** — skalerer elevens inngang, normalt 100 %.
- **Destination** — hvilken funksjon elevens kanal knyttes til.

Se [Praktisk guide: Umiddelbar tilbaketaking](../how-to/instant-takeback.md)
for et gjennomarbeidet eksempel på hvordan en instruktør kan ta tilbake
kontrollen umiddelbart med en bryter, og [Ignorer
trainer-inngang](../getting-started/user-interface-and-navigation.md#choosing-a-source)
for å utelate elevens spakbevegelser fra en logisk bryter som overvåker
instruktørens egne spaker.

## Slave-modus

![Slave-modus](../assets/model-trainer-slave-mode.png)

- **Link Mode** — samme valg mellom trainer-kabel, Bluetooth eller ekstern
  SBUS/CPPM-modul som for Master (samme Bluetooth-felt
  **Mode**/**Local Name**/**Local Address**/**Dist Address**).

  ![Tilkoblingsmodus for Slave](../assets/model-trainer-slave-link-mode.png)

- **Channel Range** — hvilket område av denne senderens kanaler som sendes
  til masteren.

  ![Slave-kanaler](../assets/model-trainer-slave-channels.png)
  ![Redigering av Slave-kanal](../assets/model-trainer-slave-channel-edit.png)
