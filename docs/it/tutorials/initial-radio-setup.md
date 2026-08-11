---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configurazione iniziale della radio

La configurazione da eseguire una sola volta, prima di programmare
qualsiasi modello. I [Tutorial](index.md) che seguono presuppongono che
sia già stata completata.

!!! note
    Questi tutorial non sono un manuale di istruzioni rigido: presuppongono
    una conoscenza di base della terminologia RC e una certa dimestichezza
    nella navigazione dei menu di Ethos. Se qualcosa non risulta chiaro,
    consulta prima [Interfaccia utente e
    navigazione](../getting-started/user-interface-and-navigation.md).

## Passo 1. Carica la batteria della radio e le batterie di volo

Carica la batteria della radio seguendo le indicazioni fornite con la
radio stessa, e le batterie di volo con un caricabatterie adatto alla loro
chimica, prestando particolare attenzione ai pacchi al litio.

## Passo 2. Calibra l'hardware

Verifica che la [calibrazione
hardware](../system-setup/hardware.md#analogs-calibration) sia stata
eseguita (viene avviata automaticamente al primo avvio), in modo che la
radio conosca il centro esatto e i limiti di ogni gimbal, potenziometro e
slider. Ripetila in **Sistema → Hardware** ogni volta che sostituisci un
gimbal, un potenziometro o uno slider.

## Passo 3. Esegui la configurazione del sistema radio

La [Configurazione di sistema](../system-setup/index.md) riguarda tutto
ciò che è comune a tutti i modelli, a differenza delle impostazioni
specifiche di ciascun modello contenute nell'[Impostazione del
modello](../model-setup/index.md). La maggior parte dei valori predefiniti
va bene per iniziare, ma è opportuno verificare:

- **[Data e ora](../system-setup/date-and-time.md)** — impostale
  correttamente.
- **[Audio → Scelta delle
  voci](../system-setup/general.md#audio-settings)** — configura gli
  annunci vocali, compresi eventuali file audio personalizzati.
- **[Comandi (Stick)](../system-setup/controls.md)**:
  - **Modalità stick** — Mode 1 (Gas - Throttle/alettoni a destra,
    elevatore/timone a sinistra) o Mode 2 (Gas - Throttle/timone a
    sinistra, alettoni/elevatore a destra — impostazione predefinita di
    Ethos).

    !!! warning
        Se un modello è configurato per una modalità stick mentre la
        trasmittente è impostata sull'altra, un motore elettrico può
        avviarsi nell'istante in cui il ricevitore viene alimentato.

  - **Ordine dei canali** — Ethos utilizza per impostazione predefinita
    l'ordine **AETR** (Alettoni, Elevatore, Motore, Timone); la
    convenzione Spektrum/JR è **TAER**, quella Futaba/Hitec è **AETR**.
    Questo determina l'ordine con cui vengono assegnati gli ingressi degli
    stick quando si crea un nuovo modello — i singoli modelli possono
    comunque essere adattati successivamente.

    !!! note "Ricevitori stabilizzati FrSky"
        Questi richiedono specificamente **AETR**. Con più superfici per
        funzione (ad esempio 2 alettoni), la procedura guidata normalmente
        le raggruppa (ottenendo **AAETR**) — ma i ricevitori SRx si
        aspettano invece **AETRA**/**AETRAE**, quindi attiva l'opzione
        **[Primi quattro canali
        fissi](../system-setup/controls.md#first-four-channels-fixed)**
        nella sezione Stick, per mantenere in ogni caso i primi quattro
        canali nel rigoroso ordine AETR.

- **[Batteria](../system-setup/battery.md)** — imposta **Tensione
  principale**, **Tensione bassa** e **Intervallo di visualizzazione della
  tensione** in base alla batteria effettivamente installata nella radio.
- **[ID di registrazione del
  proprietario](../model-setup/rf-system.md#owner-registration-id)** —
  utilizzato dai ricevitori ACCESS e condiviso tra le trasmittenti per lo
  Smart Share. Viene configurato nell'Impostazione del modello, ma in
  pratica funziona come un'impostazione di sistema, dato che ogni nuovo
  modello lo utilizza (se necessario può comunque essere modificato per
  singolo ricevitore durante la registrazione).

!!! note "Unità di misura"
    Ethos non dispone di un'opzione globale metrico/imperiale — le [unità
    dei sensori di telemetria](../model-setup/telemetry.md#editing-a-sensor)
    si impostano individualmente, per ciascun sensore.
