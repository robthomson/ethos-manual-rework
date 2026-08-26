# Layout di base di un widget Lua

Tutti gli script Lua, compresi i widget, utilizzano gli handler (noti anche come moduli di codice) per eseguire operazioni specifiche quali l'elaborazione dei dati in background, il controllo e la visualizzazione dell'interfaccia, la configurazione dei widget, la lettura o il salvataggio delle impostazioni, l'intercettazione e la valutazione degli eventi, ecc.

## init(funzione)

La funzione di gestione init serve a registrare il widget all'avvio del trasmettitore. Utilizza il metodo system.registerWidget() per dichiarare il widget. Inoltre, specifica quali gestori aggiuntivi vengono utilizzati nello script.

Un Esempio di una funzione di gestione init può essere questa:

Code:

local function init()

system.registerWidget({

key = "unique",

name = name,

create = create,

configure = configure,

wakeup = wakeup,

paint = paint,

read = read,

write = write,

})

end

return { init = init }

Nota che "key" è un identificatore unico per il tuo widget. Le varie funzioni elencate sono utilizzate nel ciclo di vita del widget.

## system.registerWidget() method

Il metodo \`system.registerWidget()\` può avere i seguenti parametri

## key (stringa)

Il widget deve avere una chiave unica.

## name (stringa o funzione)

La funzione name non richiede argomenti e restituisce il nome del widget come stringa. Il nome può essere semplicemente una stringa o il risultato di una funzione. Ad esempio, il nome può essere in una lingua diversa a seconda del locale.

## create (funzione)

La funzione create handler viene chiamata alla creazione del widget. Non richiede argomenti e restituisce la tabella dei widget che viene poi passata a tutte le funzioni. Inizializza qui le tue variabili e memorizza lo stato nella tabella dei widget restituita.

## configure (funzione)

La funzione configure handler viene chiamata quando l'utente entra nella configurazione del widget. Prende come unico argomento la tabella dei widget restituita da create() e non restituisce nulla. Viene chiamata quando l'utente entra nella configurazione del widget. Qui puoi creare il modulo di configurazione e utilizzarlo per modificare i valori della tabella dei widget.

build (function, optional)

Il gestore di creazione viene chiamato ad ogni modifica del layout quando il widget viene 	creato nella schermata Home,     nonché dopo la creazione e la configurazione.

## wakeup (funzione)

La funzione di wakeup handler viene chiamata durante ogni ciclo, cioè ogni 50ms. Prende come unico argomento la tabella dei widget e non restituisce nulla.

La funzione wakeup() deve verificare se qualcosa è cambiato. In caso affermativo, è necessario un aggiornamento, quindi deve essere richiamata la funzione invalidateWindow(). In questo modo verrà richiamata la funzione paint(). Dovresti assicurarti che questa funzione sia molto veloce e che non faccia nulla per la maggior parte del tempo.

## event (funzione)

La funzione di gestione degli eventi chiamata quando viene ricevuto un evento. ETHOS offre la possibilità di catturare qualsiasi evento in un widget, attraverso questa funzione evento.

menu (function, optional)

Il gestore del menu opzionale viene chiamato quando viene creato un menu contestuale, 	per consentire l'aggiunta di ulteriori opzioni al menu. Il gestore deve restituire una tabella di 	coppie { nome, funzione }.

## paint (funzione)

La funzione paint "disegna" il widget. Prende come unico argomento la tabella dei widget e non restituisce nulla. Dovrebbe essere chiamata quando è necessario un aggiornamento e viene richiamata automaticamente ogni volta che viene chiamato lcd.invalidate(). Può essere lenta, quindi disegna solo se qualcosa è cambiato.

## read (funzione)

Gestore di lettura opzionale. In ETHOS è possibile utilizzare l'archivio come desidera l'utente.

## write (funzione)

Gestore di scrittura opzionale. In ETHOS è possibile utilizzare l'archivio come desidera l'utente.

## persistent (booleano, facoltativo)  
Gestore dati persistenti facoltativo.  
  
title (booleano, facoltativo)  
Gestore titolo facoltativo. Il titolo del widget viene forzato su ON / OFF.

Gli script Lua sono memorizzati nella cartella scripts/ della scheda SD o eMMC, preferibilmente organizzati in cartelle.

Per maggiori informazioni, consulta il thread di rcgroups "FrSky ETHOS Lua Script Programming".
