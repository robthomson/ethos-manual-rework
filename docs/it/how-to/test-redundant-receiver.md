---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Testare una configurazione con ricevitore ridondante

La ridondanza ha senso solo se viene effettivamente verificata prima del volo —
si presuppone che un [ricevitore ridondante](../model-setup/rf-system.md#redundant-receivers)
sia già configurato.

!!! note "Screenshot in arrivo"
    Questa pagina non dispone ancora di screenshot del simulatore — vedere [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## A. Prova sul campo

Con il ricevitore principale a 2,4 GHz e quello ridondante a 900 MHz, avviare un
[Range Check](../model-setup/rf-system.md#range-check) e allontanarsi dal
modello finché il collegamento a 2,4 GHz non viene perso (oltre l'allarme RSSI Critical).
A quel punto il ricevitore ridondante a 900 MHz deve assumere il controllo.

## B. Prova al banco

1. **Verificare la configurazione normale** — entrambi i ricevitori collegati (bind),
   entrambi i LED verdi accesi, comandi che rispondono normalmente.
2. **Eseguire il bind del ricevitore principale su un altro Model ID** — creare un
   modello di prova temporaneo (ad esempio "TestRx") con un Model ID diverso ed
   eseguire il bind del ricevitore *principale* su di esso. Tornare al modello in prova:
   il LED del ricevitore principale deve ora essere **rosso** (associato altrove),
   mentre il LED del ricevitore ridondante rimane **verde** — e i comandi devono
   continuare a funzionare, dimostrando che il solo ricevitore ridondante mantiene
   il modello pilotabile.
3. **Rieseguire il bind del ricevitore principale** sul suo Model ID normale.
   Verificare che entrambi i LED siano nuovamente verdi e che i comandi funzionino
   prima di considerare conclusa la prova.
