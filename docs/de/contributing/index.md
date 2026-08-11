---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Mitwirken

## Warum dieses Handbuch existiert

Das bisherige Handbuch ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
zerfiel je Sprache in zwei voneinander getrennte Hälften. Der englische Zweig war
immer nur eine **Vorrichtung zur Screenshot-Erzeugung** – Shell-Skripte, die den
echten Ethos-Simulator über eine Lua-Makro-API steuerten, um UI-Screenshots
aufzunehmen – ohne Markdown-Quelle (oder irgendeine andere Klartextquelle) für
den eigentlichen Fließtext des Handbuchs; der englische Text existierte stets nur
als Stapel von PDF-/ODT-Exporten. Der französische Zweig war demgegenüber ein
vollständig ausformulierter GitBook-Export mit echten Inhalten, wurde aber
unabhängig davon erstellt und gepflegt, mit einem eigenen, separaten Satz von
Hand eingefügter Screenshots. Andere Sprachen hatten weder das eine noch das
andere. Es gab keine einzige verbindliche Quelle, *aus der* übersetzt werden
konnte, und keine Möglichkeit festzustellen, wann eine übersetzte Seite gegenüber
der (nicht vorhandenen) englischen Vorlage veraltet war.

Dieses Repository beginnt von vorn – mit einem einzigen Format für jede Seite in
jeder Sprache: reines Markdown, erstellt mit
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(derselbe Stack wie bei [wingflight-docs](https://doc.wingflight.org)) und bei
jedem Push auf `main` auf GitHub Pages veröffentlicht.

## Arbeitsablauf

Vor den Inhalten steht kein CMS und kein Web-Editor – Autoren und Übersetzer
arbeiten direkt in git, genau wie bei jeder anderen Änderung an diesem
Repository:

1. Einen Branch von `main` erstellen (direkt in diesem Repository – siehe den
   Hinweis zu Forks weiter unten).
2. Die betreffende(n) `.md`-Datei(en) unter `docs/en/` bearbeiten.
3. Lokal mit `mkdocs serve` vorschauen (siehe die
   [README](https://github.com/robthomson/ethos-manual-rework) im Wurzelverzeichnis)
   oder einfach den Pull Request eröffnen und die unten beschriebene automatische
   PR-Vorschau nutzen.
4. Einen Pull Request eröffnen.

Von einer Seite referenzierte Screenshots liegen daneben in `docs/en/assets/` und
sind schlicht Markdown-Bildlinks – keine besondere Syntax. Siehe
[Screenshot-Pipeline](screenshot-pipeline.md) dazu, wie sie erzeugt werden.

### PR-Vorschauen {: #pr-previews }

Jeder Pull Request gegen `main` erhält seine eigene Live-Vorschau, die von
`.github/workflows/pr-preview.yml` automatisch erstellt und bereitgestellt wird:
unter `manual.rt-rc.com/pr-preview/<PR-Nummer>/`, verlinkt in einem
Bot-Kommentar am PR und bei jedem Push aktualisiert. Sie wird automatisch
entfernt, sobald der PR geschlossen wird. Die eigentliche Website
(`manual.rt-rc.com`) bleibt davon unberührt – die Vorschauen liegen daneben in
einem Ordner `pr-preview/` im Branch `gh-pages`, der jeden Produktions-Deploy
überdauert.

Das funktioniert nur für Branches, die direkt in dieses Repository gepusht
werden, nicht für Forks – ein PR aus einem Fork erhält keine Live-Vorschau
(GitHub verweigert `GITHUB_TOKEN` bewusst Schreibzugriff bei
`pull_request`-Workflows, die von Forks ausgelöst werden, damit ein Fork die CI
nicht dazu verwenden kann, beliebige Inhalte nach `gh-pages` zu pushen).
Mitwirkende mit Fork können weiterhin lokal mit `mkdocs serve` vorschauen.

## Versionierung

Die Handbücher mehrerer Firmware-Versionen (z. B. 1.6 neben einem künftigen
Ethos26) liegen als separate Branches im selben Repository und werden jeweils
unter einem eigenen Pfad `manual.rt-rc.com/<version>/` mit einem
Versionsauswahl-Menü bereitgestellt – siehe
[Versionierung](versioning.md) für das vollständige Schema und die Vorgehensweise
beim Anlegen einer neuen Version.

## Übersetzungsplan {: #translation-plan }

Übersetzer (Mensch oder KI) arbeiten direkt in git, genau wie bei jeder anderen
Änderung – kein CMS, keine separate Übersetzungsanwendung. Ein erster
französischer Pilotversuch (eine Handvoll Seiten) hat den Ablauf durchgängig
bestätigt; so funktioniert er in der Praxis.

### Eine Übersetzung hinzufügen/aktualisieren {: #addingupdating-a-translation }

1. Branch anlegen, `docs/<locale>/<gleicher Pfad wie die englische Seite>`
   erstellen/bearbeiten und den Fließtext übersetzen. Code-wörtlichen Text
   (Tastenbezeichnungen wie `ENT`, `RTN`, auf dem Bildschirm angezeigte
   UI-Elementnamen) unverändert lassen.
2. Die Seite damit kennzeichnen, aus welchem englischen Commit sie übersetzt
   wurde:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Diese SHA findet sich mit `git log -1 --format=%H -- docs/en/<path>`.
3. **Wenn die englische Seite eine Überschrift enthält, auf die andere Seiten
   per Anker verlinken** (durch Suche nach `#that-heading-slug` in `docs/en/`
   prüfbar), darf der automatisch erzeugte Slug der übersetzten Überschrift das
   Ziel nicht verändern – dieselbe, sprachunabhängig stabile ID explizit mit
   `attr_list` (bereits aktiviert) festlegen:

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Wird das ausgelassen, bricht der Build zwar nicht, aber das Anspringen des
   Ankers ist für jede andere, noch unübersetzte Seite, die per Fallback auf
   diese Überschrift verlinkt, stillschweigend defekt.
4. Einen PR eröffnen – [Vorschau](#pr-previews) wie bei jeder anderen Änderung,
   einschließlich der Sprachumschaltung.

### Screenshots

Es muss nichts im Voraus dupliziert werden.
[`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
greift für *jedes* Asset, von dem eine Sprache keine eigene Kopie besitzt, auf
die englische Datei zurück – das `../assets/foo.png` einer übersetzten Seite
funktioniert unverändert und zeigt den englischen Screenshot, bis eine echte
lokalisierte Fassung (aufgenommen, sobald die
[Screenshot-Pipeline](screenshot-pipeline.md) portiert und gegen die
Sendereinstellungen der jeweiligen Sprache ausgeführt wurde) unter demselben
Dateinamen in `docs/<locale>/assets/` abgelegt wird, was den Fallback von da an
stillschweigend überschreibt.

### Verfolgung veralteter Übersetzungen

Der [Übersetzungsstatus](translation-status.md) wird vor jedem Build automatisch
erzeugt (`hooks/i18n_status.py`, eingebunden über den Abschnitt `hooks:` in
`mkdocs.yml` – läuft lokal, in PR-Vorschauen und in der Produktion
gleichermaßen, stets aktuell, nie in git eingecheckt) und vergleicht die
`translated_from`-Markierung jeder Sprache mit dem tatsächlichen Commit der
letzten Änderung der jeweiligen englischen Seite: **aktuell**, **veraltet**
(die englische Fassung hat sich weiterentwickelt) oder **fehlend**. Diese Seite
ist die Arbeitsliste – keine GitHub Issues, kein Durchforsten von
Actions-Protokollen.

### Automatisierte Übersetzung (optional)

`scripts/translate.py` ist ein eigenständiges lokales Skript (nicht Teil des
Site-Builds oder der CI), das dieselbe Arbeitsliste fehlender/veralteter Seiten
über die Claude-API abarbeitet und für jede Seite einen ersten
Übersetzungsentwurf erzeugt, automatisch mit dem korrekten
`translated_from:`-Frontmatter versehen:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Es liest standardmäßig alle Sprachen aus der `i18n`-Plugin-Konfiguration in
`mkdocs.yml` (`--only` schränkt auf bestimmte ein), überspringt alles bereits
Aktuelle, sofern nicht `--force` übergeben wird, und committet oder pusht
niemals – es schreibt lediglich Dateien unter `docs/<locale>/`, genauso, als
hätte man sie von Hand bearbeitet. Das Diff prüfen, für jede neu übersetzte
Überschrift die [Anker-Festlegung](#addingupdating-a-translation) kontrollieren
und dann wie gewohnt einen PR eröffnen.

Der System-Prompt gibt Claude vorab die Domäne des Handbuchs mit (FrSky
Ethos-Senderfirmware, RC-Hobby-Zielgruppe) sowie eine Liste von Begriffen, die
niemals übersetzt werden dürfen (Bezeichnungen physischer Tasten, Protokollnamen,
Markennamen) – dieselbe Technik, die auch das Schwester-Repository
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite)
in seinem `bin/i18n/auto-translate.py` verwendet. Ein während des französischen
Pilotversuchs erarbeitetes Glossar ist für `fr` fest hinterlegt; `GLOSSARIES` im
Skript lässt sich auf dieselbe Weise erweitern, sobald für eine weitere Sprache
einige Seiten übersetzt und geprüft sind.

### Navigationsbeschriftungen (`nav_translations`)

Tab- und Seitenleistenbeschriftungen in `nav:` (z. B. „Model Setup“) übernehmen
den übersetzten Seitentitel einer Sprache nicht automatisch, es sei denn, der
Navigationseintrag hat überhaupt keine explizite Beschriftung (z. B.
`- how-to/index.md` – MkDocs verwendet dann die H1 der Seite selbst). Überall
dort, wo `nav:` eine explizite Zeichenkette `Label: path.md` angibt oder einen
Abschnitt benennt (`Model Setup:` als Dictionary-Schlüssel mit Unterpunkten),
bleibt diese Beschriftung englisch, bis die `nav_translations`-Zuordnung der
Sprache in `mkdocs.yml` sie abdeckt – hinzugefügt wird sie für eine Sprache erst
dann, wenn deren Seitenabdeckung so weit fortgeschritten ist, dass eine
Übersetzung der Rahmenelemente vor dem Großteil der Inhalte nicht befremdlich
wirkt. Die Zuordnung für `fr` wurde ausgefüllt, sobald Französisch die
vollständige Seitenabdeckung erreicht hatte; jede Blattbeschriftung wurde
wortwörtlich aus der übersetzten H1 der jeweiligen Seite übernommen, sodass der
Text in der Seitenleiste exakt der Seitenüberschrift entspricht.
