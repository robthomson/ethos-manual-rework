---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configurazione modello SR8/SR10 e riordino dei canali

I ricevitori stabilizzati SRx di FrSky si aspettano un ordine dei canali ben preciso. Due
scenari: creare da zero un nuovo modello per uno di essi, oppure convertire un
modello esistente per adeguarlo.

!!! note "Screenshot in arrivo"
    Questa pagina non dispone ancora degli screenshot del simulatore — vedere [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## Creazione di un nuovo modello

La procedura guidata di [Selezione modello](../model-setup/model-select.md) raggruppa
per impostazione predefinita le superfici con la stessa funzione (ad es. 2 alettoni → `AAETR`), mentre i ricevitori
SRx richiedono che i primi quattro canali siano fissi nell'ordine **AETRA**.

1. In [Comandi](../system-setup/controls.md), verificare che **Ordine canali**
   sia `AETR`.
2. Attivare **[Primi quattro canali
   fissi](../system-setup/controls.md#first-four-channels-fixed)** — in questo modo
   la procedura guidata non raggruppa i primi quattro canali, mantenendoli
   rigorosamente nell'ordine `AETRA…` indipendentemente dal numero di superfici di ciascun tipo presenti sul
   modello.
3. Eseguire normalmente la procedura guidata di creazione del modello — i primi 5 canali
   risultano `AETRA`.

!!! note "Auto-test dei ricevitori Archer"
    L'auto-test per i ricevitori Archer viene ora eseguito tramite [Configurazione dispositivo →
    SxR](../system-setup/devices.md) (firmware v2.1.10+) anziché con una
    procedura di auto-test dedicata. Il canale del Gas deve essere a
    −100%, altrimenti l'auto-test non si avvia.

## Riordino di un modello esistente

Convertire un modello esistente (ad es. attualmente `AAETRFF`) nell'ordine
richiesto dai ricevitori stabilizzati (`AETRAE`, quindi canale 9 Gain, 10/11 fasi di
volo, 12 auto-test sulle unità SxR più datate) consiste in una sequenza di scambi di canali
in [Uscite](../model-setup/outputs.md#swap-channels).

Punto di partenza:

| Can. | Funzione |
|---|---|
| 1 | Alettone1 (destro) |
| 2 | Alettone2 (sinistro) |
| 3 | Elevatore |
| 4 | Gas |
| 5 | Timone |
| 6 | Flap1 (destro) |
| 7 | Flap2 (sinistro) |
| 8 | Retrattili |

Ordine di destinazione: `AETRAE` — Can.1 Alettone1, Can.2 Elevatore, Can.3 Gas,
Can.4 Timone, Can.5 Alettone2, Can.6 Elevatore2/AUX2 (quindi Gain/fasi di
volo/auto-test su 9–12).

1. **Sposta prima Alettone2 fuori strada**: in Uscite, seleziona CH2
   (Alettone2), tocca di nuovo, **Scambia canali** e scambialo con un canale
   inutilizzato (ad es. CH9). Lo scambio è immediato — tutti i mix che fanno riferimento
   a uno dei due canali vengono aggiornati automaticamente.
2. **Scambia CH3 (Elevatore) → CH2.**
3. **Scambia CH4 (Gas) → CH3.**
4. **Scambia CH5 (Timone) → CH4.**
5. **Scambia CH9 (Alettone2, parcheggiato al passo 1) → CH5.**

Risultato:

| Can. | Funzione |
|---|---|
| 1 | Alettone1 (destro) |
| 2 | Elevatore |
| 3 | Gas |
| 4 | Timone |
| 5 | Alettone2 (sinistro) |
| 6 | Flap1 (destro) |
| 7 | Flap2 (sinistro) |
| 8 | Retrattili |

— ora nell'ordine che si aspettano i ricevitori stabilizzati FrSky.
