---
translated_from: 727b0ba85be63990bda647e617a27dce6b255458
---

# Contribuindo

## Por que este manual existe

O manual anterior ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
dividia-se em duas metades desconectadas por idioma. A árvore em inglês nunca
foi mais do que um **aparato de geração de capturas de tela** — scripts shell
conduzindo o simulador real do Ethos por meio de uma API de macros Lua para
capturar imagens da interface — sem nenhuma fonte em Markdown (ou qualquer
outro texto puro) para a prosa efetiva do manual; o texto em inglês só existiu
como uma pilha de exportações em PDF/ODT. A árvore em francês, por outro lado,
era uma exportação completa do GitBook com conteúdo real, mas construída e
mantida de forma independente, com seu próprio conjunto separado de capturas
de tela coladas à mão. Os demais idiomas não tinham nem uma coisa nem outra.
Não havia uma única fonte de verdade *a partir da qual* traduzir, nem forma de
saber quando uma página traduzida havia se desatualizado em relação à
(inexistente) fonte em inglês.

Este repositório começa de novo com um único formato para cada página, em cada
idioma: Markdown puro, construído com [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(a mesma pilha usada por [wingflight-docs](https://doc.wingflight.org)),
publicado no GitHub Pages a cada push para `main`.

## Fluxo de trabalho

Não há CMS nem editor web à frente do conteúdo — autores e tradutores
trabalham diretamente no git, exatamente como em qualquer outra alteração
neste repositório:

1. Crie um branch a partir de `main` (neste repositório diretamente — veja a
   observação sobre forks abaixo).
2. Edite o(s) arquivo(s) `.md` relevante(s) em `docs/en/`.
3. Visualize localmente com `mkdocs serve` (veja o
   [README](https://github.com/robthomson/ethos-manual-rework) na raiz), ou
   simplesmente abra o pull request e use a pré-visualização automática de PR
   descrita abaixo.
4. Abra um pull request.

As capturas de tela referenciadas por uma página ficam ao lado dela em
`docs/en/assets/` e são apenas links de imagem em Markdown — sem sintaxe
especial. Veja [Pipeline de capturas de tela](screenshot-pipeline.md) para
saber como são geradas.

### Pré-visualizações de PR {: #pr-previews }

Todo pull request contra `main` recebe sua própria pré-visualização ao vivo,
construída e publicada automaticamente por `.github/workflows/pr-preview.yml`:
em `manual.rt-rc.com/pr-preview/<número do PR>/`, com link em um comentário de
bot no PR e atualizada a cada push. Ela é removida automaticamente quando o PR
é fechado. O site principal em si (`manual.rt-rc.com`) não é afetado — as
pré-visualizações convivem com ele em uma pasta `pr-preview/` no branch
`gh-pages`, que sobrevive a cada implantação de produção.

Isso só funciona para branches enviados diretamente a este repositório, não a
forks — um PR a partir de um fork não receberá pré-visualização ao vivo (o
GitHub deliberadamente restringe o acesso de escrita ao `GITHUB_TOKEN` em
workflows `pull_request` disparados por forks, para que um fork não possa usar
a CI para enviar conteúdo arbitrário ao `gh-pages`). Colaboradores usando fork
ainda podem visualizar localmente com `mkdocs serve`.

## Versionamento

Os manuais de múltiplas versões de firmware (por exemplo, 1.6 ao lado de um
futuro Ethos26) convivem no mesmo repositório como branches separados, cada um
publicado em seu próprio caminho `manual.rt-rc.com/<versão>/` com um menu de
seleção de versão — veja [Versionamento](versioning.md) para o esquema
completo e como criar uma nova versão.

## Plano de tradução {: #translation-plan }

Os tradutores (humanos ou IA) trabalham diretamente no git, como em qualquer
outra alteração — sem CMS, sem aplicativo de tradução separado. Um primeiro
piloto em francês (um punhado de páginas) validou a mecânica de ponta a ponta;
veja abaixo como funciona na prática.

### Adicionar/atualizar uma tradução {: #addingupdating-a-translation }

1. Crie um branch e crie/edite `docs/<locale>/<mesmo caminho da página em
   inglês>`, traduzindo a prosa. Mantenha o texto literal de código (nomes de
   teclas como `ENT`, `RTN`, nomes de elementos de interface exibidos na tela)
   como estão.
2. Marque a página indicando de qual commit em inglês ela foi traduzida:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Encontre esse sha com `git log -1 --format=%H -- docs/en/<path>`.
3. **Se a página em inglês tiver um título ao qual outras páginas se ligam por
   âncora** (verifique procurando por `#that-heading-slug` em todo o
   `docs/en/`), não deixe que o slug autogerado do título traduzido altere o
   destino — fixe explicitamente o mesmo ID, estável entre idiomas, com
   `attr_list` (já habilitado):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Ignorar isso não quebra a compilação, mas quebra silenciosamente a rolagem
   até a âncora em qualquer outra página, ainda não traduzida, que aponte para
   esse título por meio do fallback.
4. Abra um PR — [pré-visualize-o](#pr-previews) como qualquer outra alteração,
   incluindo o seletor de idioma.

### Capturas de tela

Não há nada a duplicar de antemão. O [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
recorre ao arquivo em inglês para *qualquer* recurso do qual um idioma não
tenha uma cópia própria — o `../assets/foo.png` de uma página traduzida
simplesmente funciona, sem modificação, exibindo a captura de tela em inglês,
até que uma versão realmente localizada seja colocada com o mesmo nome de
arquivo em `docs/<locale>/assets/`, o que silenciosamente sobrepõe o fallback
a partir de então.

**`de` e `fr` já têm capturas de tela realmente localizadas** — não capturadas
aqui, mas importadas em lote do antigo repositório [`ethos-manual`](https://github.com/FrSkyRC/ethos-manual),
que se revelou ter conjuntos de capturas de tela por idioma praticamente
completos, já capturados pela própria equipe da FrSky (`german/assets/` e,
para o francês, `french_LT/assets/` — o mais completo dos seus dois conjuntos
de recursos em francês, não o menor `french/assets/`, que o README descreve
como "half way"). Os nomes de arquivo correspondem 1:1 aos do nosso
`docs/en/assets/`, então a importação foi uma cópia direta: 586 das nossas 589
capturas de tela atualmente referenciadas foram atendidas para os dois idiomas
de uma só vez, sem envolver o simulador. As poucas que não corresponderam
(2-3 arquivos, em geral páginas mais recentes que as macros do repositório
antigo nunca cobriram) continuam recorrendo ao inglês normalmente.

Para qualquer idioma além de `de`/`fr`, ou para fechar esses últimos poucos
por cento, capturar novas imagens significa usar o [pipeline de capturas de
tela](screenshot-pipeline.md) — portar/executar o aparato real de macros
contra o simulador — já que esse trabalho não havia sido feito upstream.

### Acompanhamento de desatualização

O [Status de tradução](translation-status.md) é gerado automaticamente antes
de cada compilação (`hooks/i18n_status.py`, integrado via a seção `hooks:` do
`mkdocs.yml` — roda localmente, nas pré-visualizações de PR e em produção
igualmente, sempre atualizado, nunca versionado no git) e compara o marcador
`translated_from` de cada idioma com o commit de última alteração real de cada
página em inglês: **atual**, **desatualizada** (o inglês avançou) ou
**ausente**. Essa página é a lista de trabalho — sem GitHub Issues, sem
garimpar logs do Actions.

### Tradução automatizada (opcional)

O `scripts/translate.py` é um script local autônomo (não faz parte da
compilação do site nem da CI) que conduz a mesma lista de trabalho de páginas
ausentes/desatualizadas pela API do Claude para produzir uma primeira versão
de tradução de cada página, marcada automaticamente com o frontmatter
`translated_from:` correto:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Por padrão, ele lê todos os idiomas da configuração do plugin `i18n` no
`mkdocs.yml` (`--only` restringe a idiomas específicos), ignora tudo o que já
está atualizado a menos que `--force` seja passado, e nunca faz commit nem
push — apenas grava arquivos em `docs/<locale>/`, como se você os tivesse
editado à mão. Revise o diff, faça a verificação de [fixação de
âncoras](#addingupdating-a-translation) para qualquer título recém-traduzido e
então abra um PR como de costume.

O prompt de sistema pré-carrega o Claude com o domínio do manual (firmware de
rádio FrSky Ethos, público de aeromodelistas) e uma lista de termos que nunca
devem ser traduzidos (nomes de teclas físicas, nomes de protocolos, nomes de
marcas), a mesma técnica usada pelo `bin/i18n/auto-translate.py` do
repositório irmão
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite).
Um glossário de termos estabelecidos durante o piloto em francês está embutido
para `fr`; estenda `GLOSSARIES` no script da mesma forma quando outro idioma
tiver algumas páginas traduzidas e revisadas.

### Rótulos de navegação (`nav_translations`)

Os rótulos de abas e da barra lateral em `nav:` (por exemplo, "Model Setup")
não assumem automaticamente o título traduzido de uma página, a menos que a
entrada de navegação não tenha nenhum rótulo explícito (por exemplo,
`- how-to/index.md` — nesse caso o MkDocs usa o H1 da própria página). Sempre
que `nav:` fornece uma string explícita `Rótulo: caminho.md`, ou nomeia uma
seção (`Model Setup:` como chave de dicionário com filhos), esse rótulo
permanece em inglês até que o mapa `nav_translations` do idioma no
`mkdocs.yml` o cubra — adicionado para um idioma quando sua cobertura de
páginas é suficientemente ampla para que traduzir a interface antes da maior
parte do conteúdo não pareça estranho. O mapa de `fr` foi preenchido quando o
francês alcançou cobertura completa de páginas; cada rótulo final foi copiado
literalmente do H1 traduzido da própria página, de modo que o texto da barra
lateral corresponde exatamente ao título da página.
