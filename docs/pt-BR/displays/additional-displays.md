---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Telas adicionais

![Opções de configuração de tela](../assets/display-screen-config-options.png)

O modelo padrão vem com uma tela (uma imagem do modelo mais três widgets
de temporizador), mas há suporte para até **oito** telas no total. Toque
no **+** ao lado de "Screen1" para adicionar outra:

- Escolha entre **15** layouts, incluindo dois layouts dedicados à tela
  inicial e uma opção de tela cheia, com capacidade para até 9 widgets —
  configurados exatamente como a primeira tela.
- As telas podem ser reordenadas ou excluídas em sua própria caixa de
  diálogo de edição (toque em Screen1, Screen2 etc.).

## Exemplo prático

![Visão principal](../assets/display-main-view.png)

Um layout típico: a imagem do modelo (configurada em [Model Edit →
Picture](../model-setup/model-edit.md)) à esquerda, com a tensão da
bateria do receptor, o RSSI e um widget de status "Throttle ACTIVE" (um
widget Lua criado pela comunidade, do tópico *FrSky - ETHOS Lua Script
Programming* no rcgroups) empilhados à direita. Tocar em qualquer widget
abre sua configuração ou leva diretamente à função principal Configurar
telas.

## Opções no nível da tela

Além dos widgets individuais, cada tela possui suas próprias
configurações — tamanho da grade do layout, plano de fundo e quais telas
são incluídas no ciclo do `PAGE`.

Consulte [Telas](index.md) para conhecer os widgets em si, e [Widgets
personalizados](custom-widgets.md) para adicionar widgets em script Lua
além do conjunto integrado.
