---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Display aggiuntivi

![Opzioni di configurazione della schermata](../assets/display-screen-config-options.png)

Il modello predefinito prevede una sola schermata (un'immagine del modello più tre
widget timer), ma sono supportate fino a **otto** schermate in totale. Toccare il **+**
accanto a "Screen1" per aggiungerne un'altra:

- Si può scegliere tra **15** layout, inclusi due layout dedicati alla schermata Home
  e un'opzione a schermo intero, con un massimo di 9 widget — configurabili esattamente
  come la prima schermata.
- Le schermate possono essere riordinate o eliminate dalla rispettiva finestra di modifica
  (toccare Screen1, Screen2, ecc.).

## Esempio pratico

![Vista principale](../assets/display-main-view.png)

Un layout tipico: l'immagine del modello (configurata in [Modifica modello →
Immagine](../model-setup/model-edit.md)) a sinistra, con la tensione della batteria
del ricevitore, l'RSSI e un widget di stato "Throttle ACTIVE" (un widget Lua
realizzato dalla community, tratto dal thread rcgroups *FrSky - ETHOS Lua Script
Programming*) impilati a destra. Toccando un widget qualsiasi si apre la relativa
configurazione, oppure si passa alla funzione principale Configura schermate.

## Opzioni a livello di schermata

Oltre ai singoli widget, ogni schermata dispone di impostazioni proprie: dimensione
della griglia del layout, sfondo e quali schermate sono incluse nel ciclo `PAGE`.

Consultare [Display](index.md) per i widget veri e propri e [Widget
personalizzati](custom-widgets.md) per aggiungere widget in script Lua oltre a quelli
integrati.
