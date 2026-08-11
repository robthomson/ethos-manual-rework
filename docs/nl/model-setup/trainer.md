---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Standaard uitgeschakeld. Stel de zender in als **Master** (de zender van de
instructeur, die tot 16 besturingen van de leerling ontvangt) of als **Slave**
(de zender van de leerling, die een instelbaar aantal kanalen naar de
instructeur verzendt).

## Master-modus

![Master-modus](../assets/model-trainer-master.png)
![Trainer-opties](../assets/model-trainer-options.png)

### Verbindingsmodus

![Opties verbindingsmodus](../assets/model-trainer-link-mode-options.png)

- **Trainerkabel** — een 3,5 mm mono audiokabel tussen de twee zenders.
- **Bluetooth** —

  ![Bluetooth-verbinding](../assets/model-trainer-link-mode-bt.png)

  - **Modus** — normaal of hoge snelheid; gebruik hoge snelheid voor een
    lagere latentie als beide zenders dit ondersteunen.

    ![Bluetooth-modus](../assets/model-trainer-link-mode-bt-mode.png)

  - **Lokale naam** — de BT-naam die aan andere apparaten wordt getoond
    (standaard `FrSkyBT`, aanpasbaar).
  - **Lokaal adres** — het Bluetooth-adres van deze zender.
  - **Extern adres** — het adres van de gekoppelde zender, zodra de
    verbinding tot stand is gebracht.
  - **Apparaten zoeken** (alleen in Master-modus) — zoekt naar apparaten in
    de buurt:

    ![Zoeken](../assets/model-trainer-link-mode-bt-search.png)
    ![Wachten](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Apparaat selecteren](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Verbonden](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Laatste apparaat verbinden** / **Module resetten** — opnieuw verbinden
    met de vorige koppeling, of de configuratie van de Bluetooth-module
    volledig wissen.

- **SBUS externe module** — een SBUS-ingang op de PXX-IN-pin van het
  externe modulevak, voor het aansluiten van een FrSky-ontvanger met
  SBUS-uitgang (bijv. Archer RS) als ontvangende zijde van een draadloze
  verbinding — waardoor **elke** FrSky-zender als leerlingzijde (buddy box)
  kan dienen, gebonden aan die ontvanger.
- **CPPM externe module** — hetzelfde principe via een CPPM-ingang, voor een
  oudere ontvanger met CPPM-uitgang.

### Actieve voorwaarde

![Actieve voorwaarde](../assets/model-trainer-active-condition.png)

Een schakelaar/knop, functieschakelaar, logische schakelaar, trimpositie of
vluchtmodus die de besturing aan de leerling overdraagt zolang deze actief
is.

### Trainerkanalen

![Actieve voorwaarde bewerken](../assets/model-trainer-active-condition-edit.png)

Er kunnen tot 16 kanalen van de leerling naar de master worden overgedragen
zolang de actieve voorwaarde waar is. Tik op een kanaal om het afzonderlijk
te configureren:

- **Actieve voorwaarde** — een override per kanaal, bijvoorbeeld om alleen
  het hoogteroer van de leerling tijdens een deel van de sessie uit te
  schakelen.
- **Modus** — **OFF** (uitgeschakeld voor trainergebruik), **Add** (de
  signalen van master en leerling worden bij elkaar opgeteld, zodat beiden
  gelijktijdig op de besturing kunnen werken), of **Replace** (de normale
  modus — de leerling heeft volledige controle over dit kanaal zolang het
  actief is).
- **Percentage** — schaalt de invoer van de leerling, normaal 100%.
- **Bestemming** — de functie waaraan het kanaal van de leerling wordt
  toegewezen.

Zie [Handleiding: Direct terugnemen van de besturing](../how-to/instant-takeback.md)
voor een uitgewerkt voorbeeld waarbij een instructeur de besturing
onmiddellijk via een schakelaar terugneemt, en [Trainerinvoer
negeren](../getting-started/user-interface-and-navigation.md#choosing-a-source)
om de stickbeweging van de leerling uit te sluiten bij een logische
schakelaar die de sticks van de instructeur zelf bewaakt.

## Slave-modus

![Slave-modus](../assets/model-trainer-slave-mode.png)

- **Verbindingsmodus** — dezelfde keuze uit trainerkabel, Bluetooth of
  SBUS/CPPM externe module als bij Master (met dezelfde
  Bluetooth-velden **Modus**/**Lokale naam**/**Lokaal adres**/**Extern
  adres**).

  ![Verbindingsmodus slave](../assets/model-trainer-slave-link-mode.png)

- **Kanaalbereik** — welk bereik van de kanalen van deze zender naar de
  master wordt verzonden.

  ![Slave-kanalen](../assets/model-trainer-slave-channels.png)
  ![Slave-kanaal bewerken](../assets/model-trainer-slave-channel-edit.png)
