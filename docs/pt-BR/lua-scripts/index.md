---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Scripts Lua

Os scripts Lua permitem criar [widgets de tela personalizados](../displays/custom-widgets.md)
para exibir informações que o Ethos não cobre nativamente e, por modelo,
[fontes e tarefas](../model-setup/lua-scripts.md) personalizadas — uma base
que deve crescer ainda mais, no sentido de funções personalizadas
especializadas e integração com controladores de voo.

O Lua em si é uma linguagem de script de propósito geral, leve e
incorporável (usada em tudo, de jogos a aplicações web); o Ethos a incorpora
exatamente para esse tipo de personalização no rádio.

!!! warning
    Os scripts Lua aumentam o tempo de inicialização do rádio. O atraso
    causado por um script bem escrito deve ser imperceptível — já um script
    mal escrito pode atrasar a inicialização quase indefinidamente.

- [Interpretador Lua](lua-interpreter.md) — qual versão do Lua e quais
  bibliotecas o Ethos incorpora.
- [Documentação do Lua do Ethos](ethos-lua-documentation.md) — onde está a
  referência completa da API.
- [Locais de scripts de exemplo](example-script-locations.md) — onde
  encontrar e baixar exemplos funcionais.
- [Limites de configuração](configuration-limits.md) — orçamentos de memória
  para bitmaps e scripts.
- [Estrutura básica de um widget](basic-widget-layout.md) — a estrutura de
  código que um script de widget personalizado precisa ter.
