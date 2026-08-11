---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Configurare un sistema FBUS

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (in
precedenza F.Port2) porta comandi e telemetria su un'unica linea,
consentendo a più dispositivi FBUS di condividere un solo collegamento in
cascata (daisy-chain) con configurazione completamente wireless. Questa
guida collega due servi Xact ai canali degli alettoni (1 e 5)
dell'[esempio di aereo ad ala fissa di
base](../tutorials/basic-fixed-wing.md).

!!! note "Screenshot in arrivo"
    Questa pagina non dispone ancora degli screenshot del simulatore —
    consulta [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## 1. Scaricare il firmware più recente

FBUS richiede un firmware aggiornato sia sul ricevitore sia sui
dispositivi — ad esempio i servi Xact necessitano della v2.0.1 o
successiva. Scarica gli aggiornamenti necessari dalla [pagina dei
download FrSky](https://www.frsky-rc.com/download/).

## 2. Aggiornare il firmware

Copia i file del firmware nella cartella `Firmware/` della scheda SD o
eMMC. In [File Manager](../system-setup/file-manager.md), collega il
servo al connettore S.Port della radio (cavo bianco/giallo rivolto verso
la tacca), seleziona il file del firmware e scegli **Flash External
Device**.

## 3 / 5. Configurare i Physical ID

Entrambi i servi hanno come valori predefiniti Physical ID `0C`
esadecimale / Application ID `6800` esadecimale: entreranno in conflitto
sul bus condiviso a meno che uno dei due non venga modificato. Ci sono due
modi per procedere, a seconda del tipo di ricevitore:

**Tramite il connettore S.Port del trasmettitore** (qualsiasi ricevitore):

1. Collega il servo 1, vai in **Device Config → XAct** e imposta **Module**
   su **S.Port connector**. Lascia Physical ID `0C`/Application ID `6800` e
   il canale `CH1` ai valori predefiniti, quindi **Save to flash**.
2. Collega al suo posto il servo 2, stesso menu. Cambia il **Physical ID** in
   `0D` esadecimale e l'**Application ID** in `6801` esadecimale (consulta la
   [tabella dei Physical
   ID](../model-setup/telemetry.md#how-frsky-telemetry-works) per sapere
   quali slot sono liberi), imposta **Channel** su `CH5` e **Save to flash**.

**Direttamente tramite il ricevitore** (ad esempio TD-R18 Tandem, con
entrambi i servi collegati contemporaneamente — vedi il [Passo
4](#4-configure-the-receiver-for-fbus)):

1. Con il solo servo 1 collegato (ad esempio al Pin1 del ricevitore),
   **Device Config → XAct**, **Module** → **Internal module**. Conferma i
   valori predefiniti (`0C`/`6800`/`CH1`), **Save to flash**.
2. Con il solo servo 2 collegato (Pin5), stesso menu (Device Config
   comunica con un servo alla volta) — imposta `0D`/`6801`/`CH5`, **Save to
   flash**. Riseleziona poi Device Config per verificare che la modifica sia
   stata applicata.

## 4. Configurare il ricevitore per FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [RF System](../model-setup/rf-system.md) → pulsante del
ricevitore → **Options** → imposta **Telemetry Port** su **FBUS**. I servi
Xact vengono quindi collegati in cascata su quella porta; poiché ogni servo
dispone di un solo connettore, un extender multicanale F.Port2 (FP2CH4/6/8)
permette di distribuirla su più dispositivi.

**TD-R18 Tandem**: RF System → pulsante del ricevitore → **Options** →
imposta i singoli pin (ad esempio **Pin1**, **Pin5**) su **FBUS**: in questo
modo è possibile riassegnare tutti i pin necessari, evitando completamente
gli extender; ogni pin assegnato a FBUS trasporta il medesimo segnale FBUS.

## 5. Verificare il controllo FBUS dei servi

Collega il servo 1 al Pin1 e il servo 2 al Pin5 (i canali degli alettoni
dell'esempio ad ala fissa), accendi e verifica che i canali 1 e 5 muovano i
servi corretti.

## 6. Verificare la telemetria FBUS

Con entrambi i servi collegati, elimina gli eventuali sensori `SRV` già
presenti in [Telemetria](../model-setup/telemetry.md) e avvia una nuova
ricerca. Ogni servo riporta 4 sensori: corrente, tensione, temperatura e
stato (`OK` in condizioni normali).

## 7. Modificare la configurazione in seguito

Una volta che il modello è completamente cablato, isolare un singolo servo
per riconfigurarlo tramite Device Config non è pratico. Procedi invece così:
vai in Telemetria, individua un sensore appartenente al servo desiderato (ad
esempio `SRV1 curr`) e scegli **Configure** — si aprirà direttamente la
configurazione di quel servo. Esegui **Save to flash** dopo ogni modifica.

!!! warning
    Fai attenzione a non modificare accidentalmente il Physical ID o
    l'Application ID da questa schermata: sono proprio questi valori a
    mantenere ogni servo indirizzabile sul bus condiviso.
