---
translated_from: 727b0ba85be63990bda647e617a27dce6b255458
---

# Contribuire

## Perché esiste questo manuale

Il manuale precedente ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
si era diviso in due metà scollegate tra loro per ciascuna lingua. L'albero
inglese non è mai stato altro che un **impianto per la generazione di
screenshot** — script shell che pilotavano il vero simulatore Ethos attraverso
una API di macro Lua per catturare le schermate dell'interfaccia — senza alcun
sorgente Markdown (o di qualsiasi altro formato testuale) per il testo vero e
proprio del manuale; il testo inglese è sempre esistito soltanto come una pila
di esportazioni PDF/ODT. L'albero francese, al contrario, era un'esportazione
GitBook completamente redatta con contenuti reali, ma costruita e mantenuta in
modo indipendente, con il proprio insieme separato di screenshot incollati a
mano. Le altre lingue non avevano né l'uno né l'altro. Non esisteva un'unica
fonte di verità *da cui* tradurre, né alcun modo per sapere quando una pagina
tradotta si fosse disallineata rispetto al sorgente inglese (inesistente).

Questo repository riparte da zero con un unico formato per ogni pagina, in ogni
lingua: Markdown puro, generato con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(lo stesso stack usato per [wingflight-docs](https://doc.wingflight.org)),
pubblicato su GitHub Pages a ogni push su `main`.

## Flusso di lavoro

Non c'è alcun CMS o editor web davanti ai contenuti — autori e traduttori
lavorano direttamente in git, esattamente come per qualsiasi altra modifica a
questo repository:

1. Creare un branch da `main` (direttamente in questo repository — vedere la
   nota sui fork più avanti).
2. Modificare i file `.md` interessati sotto `docs/en/`.
3. Visualizzare l'anteprima in locale con `mkdocs serve` (vedere il
   [README](https://github.com/robthomson/ethos-manual-rework) principale),
   oppure semplicemente aprire la pull request e usare l'anteprima automatica
   descritta di seguito.
4. Aprire una pull request.

Gli screenshot richiamati da una pagina risiedono accanto ad essa in
`docs/en/assets/` e sono semplici link immagine Markdown — nessuna sintassi
particolare. Vedere [Pipeline degli screenshot](screenshot-pipeline.md) per
sapere come vengono generati.

### Anteprime delle PR {: #pr-previews }

Ogni pull request verso `main` ottiene la propria anteprima live, costruita e
pubblicata automaticamente da `.github/workflows/pr-preview.yml`: all'indirizzo
`manual.rt-rc.com/pr-preview/<numero PR>/`, indicata in un commento del bot
sulla PR e aggiornata a ogni push. Viene rimossa automaticamente alla chiusura
della PR. Il sito principale (`manual.rt-rc.com`) non ne risente — le anteprime
risiedono accanto ad esso in una cartella `pr-preview/` sul branch `gh-pages`,
che sopravvive a ogni deploy di produzione.

Questo meccanismo funziona solo per i branch inviati direttamente a questo
repository, non per i fork — una PR proveniente da un fork non otterrà
un'anteprima live (GitHub nega deliberatamente l'accesso in scrittura al
`GITHUB_TOKEN` per i workflow `pull_request` innescati da fork, in modo che un
fork non possa usare la CI per pubblicare contenuti arbitrari su `gh-pages`).
Chi contribuisce da un fork può comunque generare l'anteprima in locale con
`mkdocs serve`.

## Versionamento

I manuali di più versioni del firmware (ad esempio la 1.6 accanto a un futuro
Ethos26) risiedono nello stesso repository come branch separati, ciascuno
pubblicato sul proprio percorso `manual.rt-rc.com/<versione>/` con un menu a
tendina di selezione della versione — vedere [Versionamento](versioning.md) per
lo schema completo e per sapere come crearne una nuova.

## Piano di traduzione {: #translation-plan }

I traduttori (umani o IA) lavorano direttamente in git, esattamente come per
qualsiasi altra modifica — nessun CMS, nessuna applicazione di traduzione
separata. Un primo progetto pilota in francese (una manciata di pagine) ha
validato il meccanismo dall'inizio alla fine; ecco come funziona in concreto.

### Aggiungere/aggiornare una traduzione {: #addingupdating-a-translation }

1. Creare un branch, creare/modificare `docs/<locale>/<stesso percorso della
   pagina inglese>`, traducendo il testo. Mantenere invariato il testo letterale
   di codice (nomi di tasti come `ENT`, `RTN`, nomi di elementi dell'interfaccia
   mostrati a schermo).
2. Marcare la pagina indicando da quale commit inglese è stata tradotta:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Lo sha si ricava con `git log -1 --format=%H -- docs/en/<path>`.
3. **Se la pagina inglese contiene un'intestazione a cui altre pagine si
   collegano tramite ancora** (verificabile cercando `#that-heading-slug` in
   tutto `docs/en/`), non lasciare che lo slug auto-generato dall'intestazione
   tradotta cambi la destinazione — fissare esplicitamente lo stesso ID, stabile
   tra le lingue, con `attr_list` (già abilitato):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Ometterlo non compromette la build, ma interrompe silenziosamente lo
   scorrimento all'ancora per qualsiasi altra pagina, ancora non tradotta, che
   punti a quell'intestazione tramite fallback.
4. Aprire una PR — [visualizzarne l'anteprima](#pr-previews) come per qualsiasi
   altra modifica, incluso il selettore di lingua.

### Screenshot

Non c'è nulla da duplicare in anticipo. [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
ricade sul file inglese per *qualsiasi* risorsa di cui una lingua non abbia una
propria copia — il `../assets/foo.png` di una pagina tradotta funziona così
com'è, senza modifiche, mostrando lo screenshot inglese, finché non se ne
inserisce uno localizzato reale con lo stesso nome file sotto
`docs/<locale>/assets/`, che da quel momento sovrascrive silenziosamente il
fallback.

**`de` e `fr` dispongono già di screenshot localizzati reali** — non catturati
qui, ma importati in blocco dal vecchio repository [`ethos-manual`](https://github.com/FrSkyRC/ethos-manual),
che si è rivelato contenere insiemi di screenshot per lingua quasi completi già
catturati dal team di FrSky (`german/assets/` e, per il francese,
`french_LT/assets/` — il più completo dei suoi due insiemi di risorse francesi,
non il più ridotto `french/assets/` che il suo README descrive come "half way").
I nomi dei file corrispondono 1:1 ai nostri in `docs/en/assets/`, quindi
l'importazione è stata una semplice copia: 586 dei nostri 589 screenshot
attualmente referenziati sono stati acquisiti per entrambe le lingue in un'unica
passata, senza coinvolgere il simulatore. I pochi che non corrispondevano (2-3
file, per lo più pagine più recenti mai coperte dalle macro del vecchio
repository) ricadono normalmente sull'inglese.

Per qualsiasi lingua diversa da `de`/`fr`, o per colmare quell'ultimo piccolo
scarto, catturare nuovi screenshot significa ricorrere alla
[pipeline degli screenshot](screenshot-pipeline.md) — portare/eseguire il vero
impianto di macro contro il simulatore — dato che quel lavoro non era già stato
fatto a monte.

### Monitoraggio dell'obsolescenza

[Stato delle traduzioni](translation-status.md) viene generato automaticamente
prima di ogni build (`hooks/i18n_status.py`, collegato tramite la voce `hooks:`
di `mkdocs.yml` — viene eseguito in locale, nelle anteprime delle PR e in
produzione allo stesso modo, sempre aggiornato, mai committato in git) e
confronta il marcatore `translated_from` di ogni lingua con l'ultimo commit di
modifica effettivo di ciascuna pagina inglese: **aggiornata**, **obsoleta**
(l'inglese è andato avanti) o **mancante**. Quella pagina è la lista di lavoro —
niente GitHub Issues, niente ricerche nei log delle Actions.

### Traduzione automatica (opzionale)

`scripts/translate.py` è uno script locale autonomo (non fa parte della build
del sito né della CI) che elabora la stessa lista di lavoro
mancanti/obsolete tramite l'API di Claude per produrre una prima bozza di
traduzione per ogni pagina, marcata automaticamente con il frontmatter
`translated_from:` corretto:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Per impostazione predefinita legge tutte le lingue dalla configurazione del
plugin `i18n` in `mkdocs.yml` (`--only` limita a lingue specifiche), salta tutto
ciò che è già aggiornato a meno che non si passi `--force`, e non esegue mai
commit né push — si limita a scrivere file sotto `docs/<locale>/`, esattamente
come se fossero stati modificati a mano. Rivedere il diff, effettuare la verifica
di [fissaggio delle ancore](#addingupdating-a-translation) per ogni intestazione
appena tradotta, quindi aprire una PR come di consueto.

Il prompt di sistema fornisce preventivamente a Claude il dominio del manuale
(firmware radio FrSky Ethos, pubblico di appassionati RC) e un elenco di termini
che non devono mai essere tradotti (nomi dei tasti fisici, nomi di protocolli,
nomi di marchi), la stessa tecnica usata dallo script `bin/i18n/auto-translate.py`
del repository gemello
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite).
Un glossario di termini definito durante il progetto pilota francese è integrato
per `fr`; estendere allo stesso modo `GLOSSARIES` nello script una volta che
un'altra lingua abbia qualche pagina tradotta e revisionata.

### Etichette di navigazione (`nav_translations`)

Le etichette delle schede e della barra laterale in `nav:` (ad esempio "Model
Setup") non assumono automaticamente il titolo tradotto della pagina di una
lingua, a meno che la voce di navigazione non abbia alcuna etichetta esplicita
(ad esempio `- how-to/index.md` — in tal caso MkDocs usa l'H1 della pagina
stessa). Ovunque `nav:` fornisca una stringa esplicita `Etichetta: percorso.md`,
o dia un nome a una sezione (`Model Setup:` come chiave di dizionario con figli),
tale etichetta resta in inglese finché la mappa `nav_translations` della lingua
in `mkdocs.yml` non la copre — aggiunta per una lingua solo quando la copertura
delle pagine è sufficientemente ampia da evitare che tradurre l'interfaccia prima
della maggior parte dei contenuti risulti stonato. La mappa di `fr` è stata
compilata una volta raggiunta la copertura completa delle pagine in francese;
ogni etichetta finale è stata copiata testualmente dall'H1 tradotto della pagina
corrispondente, così che il testo della barra laterale corrisponda esattamente
all'intestazione della pagina.
