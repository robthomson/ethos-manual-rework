---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Versioning

Ethos distribuisce attualmente il firmware con numeri di versione (1.6.x) e
ha annunciato un passaggio verso un marchio basato sull'anno (ad es. "Ethos26").
Questo manuale deve mantenere disponibile e corretta la documentazione delle
versioni precedenti mentre si scrivono attivamente quelle nuove — questa pagina
spiega come.

## Come funziona

Il versioning è gestito da [mike](https://github.com/jimporter/mike), lo
strumento raccomandato da Material for MkDocs stesso. `.github/workflows/deploy.yml`
esegue `mike deploy` invece di pubblicare direttamente nella radice di `gh-pages`:
ogni versione viene compilata e sottoposta a commit in una propria sottocartella
(`/1.6/`, `/26/`, …), e `manual.rt-rc.com/` reindirizza alla versione che al
momento detiene l'alias `latest`. Material mostra automaticamente un menu a
tendina di selezione della versione, leggendo `versions.json` (mantenuto da
`mike`) — questo è indipendente dal selettore di lingua e si combina con esso
in modo pulito: la versione è il segmento di percorso esterno, la lingua (quando
ne esisterà più di `en`) è quello interno, ad es. `manual.rt-rc.com/26/fr/...`.

Viene riutilizzato lo stesso meccanismo di "sottocartella su `gh-pages`" delle
[anteprime delle PR](index.md#pr-previews) — le cartelle di versione di `mike`
e la cartella `pr-preview/` coesistono sullo stesso branch senza conflitti,
poiché ciascuna interviene esclusivamente sui propri percorsi.

## Struttura dei sorgenti: `main` + branch congelati

- **`main` traccia sempre il contenuto della versione firmware corrente/più recente.**
  La modifica quotidiana avviene qui esattamente come oggi — nulla cambia
  nel normale flusso di lavoro dei contributi.
- Quando il manuale di una nuova versione firmware deve iniziare a divergere
  da quanto presente su `main`, **creare prima un branch con il nome della
  vecchia versione**, ad es. `1.6`, per congelarlo definitivamente. `main`
  diventa quindi il contenuto della nuova versione.
- Un branch congelato non è morto — può comunque ricevere correzioni tramite
  PR dedicate. Semplicemente non traccia più lo sviluppo della nuova versione.

## Creazione di una nuova versione

Quando deve iniziare il manuale della versione successiva (ad es. Ethos26):

1. Da `main`, creare e pubblicare il branch congelato per la versione che
   viene lasciata indietro:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   La copia di `.github/workflows/deploy.yml` presente in `1.6` esegue ora
   permanentemente `mike deploy --push --update-aliases 1.6 latest` a ogni
   push su quel branch — corretta così com'è, senza necessità di modifiche,
   poiché un branch è uno snapshot completo che include la propria
   configurazione CI.

2. Su `main`, modificare `.github/workflows/deploy.yml`: cambiare la stringa
   di versione nello step `Deploy version 1.6 with mike` (e il suo nome) da
   `1.6` all'etichetta della nuova versione (ad es. `26`). Questa è l'**unica**
   modifica necessaria per iniziare a pubblicare la nuova versione — il push
   successivo su `main` la pubblicherà in `/26/` e sposterà lì l'alias
   `latest`, mentre `/1.6/` rimarrà esattamente com'era.

3. Aggiornare su `main` il contenuto della nuova versione in base a ciò che è
   effettivamente cambiato — sezioni di menu nuove o rinominate, nuove
   schermate, terminologia aggiornata. La sezione `nav` di `mkdocs.yml` può
   differire liberamente tra i branch; non esiste alcuna configurazione
   condivisa da mantenere sincronizzata.

4. Aggiungere il nome del nuovo branch all'elenco dei trigger `branches:` in
   `.github/workflows/pr-preview.yml` se anche le PR verso di esso devono
   ottenere anteprime live (i branch congelati generalmente non ne hanno
   bisogno, poiché ricevono solo PR di correzione occasionali).

## Schermate tra le versioni

Le schermate sono acquisite da una build specifica di Ethos (vedere [Pipeline
delle schermate](screenshot-pipeline.md)) e appartengono al branch di cui
mostrano l'interfaccia — la creazione di una versione biforca naturalmente
l'insieme delle schermate insieme a tutto il resto, quindi `1.6/assets/` e
(una volta rigenerata per la nuova interfaccia) `docs/en/assets/` di `main`
divergono in modo indipendente dopo il punto di diramazione.
