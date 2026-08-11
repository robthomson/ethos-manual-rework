---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Versionamento

O Ethos atualmente distribui firmware sob números de versão (1.6.x) e já
sinalizou uma mudança para uma identificação baseada no ano (por exemplo,
"Ethos26"). Este manual precisa manter a documentação das versões antigas
disponível e correta enquanto novas versões estão sendo escritas ativamente —
esta página explica como.

## Como funciona

O versionamento é feito pelo [mike](https://github.com/jimporter/mike), a
ferramenta que o próprio Material for MkDocs recomenda. O arquivo
`.github/workflows/deploy.yml` executa `mike deploy` em vez de publicar
diretamente na raiz do `gh-pages`: cada versão é construída e comitada em sua
própria subpasta ali (`/1.6/`, `/26/`, …), e `manual.rt-rc.com/` redireciona
para a versão que detém o alias `latest` no momento. O Material exibe
automaticamente um menu suspenso de seleção de versão, lendo o `versions.json`
(que o `mike` mantém) — isso é independente do alternador de idioma e se
combina perfeitamente com ele: a versão é o segmento externo do caminho e o
idioma (quando houver mais de um além de `en`) é o interno, por exemplo,
`manual.rt-rc.com/26/fr/...`.

Isso reutiliza o mesmo mecanismo de "subpasta no `gh-pages`" usado pelas
[prévias de PR](index.md#pr-previews) — as pastas de versão do `mike` e a pasta
`pr-preview/` coexistem no mesmo branch sem conflito, já que cada uma só
manipula os seus próprios caminhos.

## Organização do código-fonte: `main` + branches congelados

- **O `main` sempre acompanha o conteúdo da versão de firmware atual/mais
  recente.** A edição do dia a dia acontece aqui exatamente como acontece hoje
  — nada muda no fluxo normal de contribuição.
- Quando o manual de uma nova versão de firmware precisar começar a divergir do
  que está no `main`, **crie primeiro um branch com o nome da versão antiga**,
  por exemplo `1.6`, para congelá-la permanentemente. O `main` passa então a ser
  o conteúdo da nova versão.
- Um branch congelado não está morto — ele ainda pode receber correções por
  meio de seus próprios PRs. Ele apenas não acompanha mais o desenvolvimento da
  nova versão.

## Criando uma nova versão

Quando o manual da próxima versão precisar começar (por exemplo, Ethos26):

1. A partir do `main`, crie e envie o branch congelado da versão que está sendo
   deixada para trás:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   A cópia do `.github/workflows/deploy.yml` no branch `1.6` agora executa
   permanentemente `mike deploy --push --update-aliases 1.6 latest` a cada push
   nesse branch — correto como está, sem necessidade de edição, já que um branch
   é um snapshot completo, incluindo sua própria configuração de CI.

2. No `main`, edite o `.github/workflows/deploy.yml`: altere a string de versão
   na etapa `Deploy version 1.6 with mike` (e no nome dela) de `1.6` para o
   rótulo da nova versão (por exemplo, `26`). Essa é a **única** edição
   necessária para começar a publicar a nova versão — o próximo push no `main`
   vai publicá-la em `/26/` e mover o alias `latest` para lá, enquanto `/1.6/`
   permanece exatamente como estava.

3. Atualize o conteúdo da nova versão no `main` conforme o que realmente mudou —
   seções de menu novas ou renomeadas, novas capturas de tela, terminologia
   atualizada. O `nav` do `mkdocs.yml` pode diferir livremente entre os branches;
   não há configuração compartilhada a manter sincronizada.

4. Adicione o nome do novo branch à lista de gatilhos `branches:` do
   `.github/workflows/pr-preview.yml` caso os PRs contra ele também devam
   receber prévias ao vivo (branches congelados geralmente não precisam disso,
   pois recebem apenas PRs de correção ocasionais).

## Capturas de tela entre versões

As capturas de tela são geradas a partir de uma build específica do Ethos (veja
[Pipeline de capturas de tela](screenshot-pipeline.md)) e pertencem ao branch
cuja interface elas mostram — a criação de uma versão naturalmente bifurca o
conjunto de capturas de tela junto com todo o resto, de modo que
`1.6/assets/` e (quando regeneradas para a nova interface) o `docs/en/assets/`
do `main` divergem de forma independente após o ponto de bifurcação.
