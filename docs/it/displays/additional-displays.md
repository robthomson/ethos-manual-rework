---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Schermate aggiuntive

![Opzioni di configurazione della schermata](../assets/display-screen-config-options.png)

Il modello predefinito prevede una sola schermata (una bitmap del modello più tre
widget timer), ma sono supportate fino a **otto** schermate in totale. Tocca il **+**
accanto a "Schermo1" per aggiungerne un'altra:

- Puoi scegliere tra **15** layout diversi, tra cui due layout dedicati alla schermata
  iniziale e un'opzione a schermo intero, con un massimo di 9 widget: si configurano
  esattamente come la prima schermata.
- Le schermate possono essere riordinate o addirittura eliminate dalla rispettiva
  finestra di dialogo di modifica (tocca Schermo1, Schermo2, ecc.).

## Esempio pratico

![Vista principale](../assets/display-main-view.png)

Un layout tipico: a sinistra la bitmap del modello (configurata in [Modifica modello →
Immagine](../model-setup/model-edit.md)), mentre a destra sono impilati la tensione
della batteria del ricevitore, l'RSSI e un widget di stato "Throttle ACTIVE" (un widget
Lua realizzato dalla community, disponibile nella discussione *FrSky - ETHOS Lua Script
Programming* su rcgroups). Tocca un qualsiasi widget per aprire la sua configurazione
oppure per accedere alla funzione principale Configura schermate.

## Opzioni a livello di schermata

Oltre ai singoli widget, ogni schermata dispone di impostazioni proprie: dimensione
della griglia del layout, sfondo e quali schermate sono incluse nel ciclo `PAGE`.

Consulta [Display](index.md) per i widget veri e propri e [Widget
personalizzati](custom-widgets.md) per aggiungere widget in script Lua oltre a quelli
integrati.
