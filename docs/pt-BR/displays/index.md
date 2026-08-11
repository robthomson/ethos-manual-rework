---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telas

![Tela inicial](../assets/display-home.png)

A tela inicial é composta por uma ou mais **telas de exibição**, cada uma
construída a partir de **widgets** que você mesmo posiciona e configura.
Pressionar `DISP` abre o editor de exibição da tela atual.

Estão disponíveis até **oito** telas, cada uma partindo de um entre
**treze** layouts (com capacidade para até **nove** células de widget). Os
widgets podem exibir telemetria, mas também qualquer uma das outras
dezessete categorias de informação — status do modelo/rádio,
temporizadores, canais e muito mais. As telas configuradas são acessadas
por deslizamento no touch ou com `PAGE` para cima/baixo; as barras
superior e inferior permanecem visíveis em todas as telas, exceto em um
layout de tela cheia.

## Adicionando um widget

![Tipos de widget](../assets/display-widget-types.png)

Toda tela é uma grade; tocar em uma célula vazia abre o seletor de
widgets. Os widgets vão de simples leituras de texto e numéricas a
medidores, gráficos e registros completos de telemetria. Depois de
posicionado, tocar novamente no widget abre o mesmo menu de opções usado
para redimensioná-lo, movê-lo ou removê-lo:

![Opções de configuração do widget](../assets/display-widget-config-options.png)

Selecionar as configurações próprias de um widget abre um formulário de
configuração específico daquele widget. O campo **fonte** — o valor que o
widget exibe — usa o mesmo
[seletor de fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)
utilizado em todo o restante do Ethos:

![Alterar fonte do widget](../assets/display-change-source.png)

## Tipos de widget {: #widget-types }

**Value** — uma única leitura numérica ou de telemetria, exibida como
texto:

![Configuração do widget Value](../assets/display-widget-value-config.png)

A maioria das fontes também permite reduzir a um **min** ou **max** ao
vivo — após selecionar a fonte, pressione-a longamente e escolha Min ou
Max — útil para coisas como o pior caso de RSSI ao longo de um voo:

![Widget Value com min](../assets/display-widget-value-min.png)
![Widget Value com min de RSSI](../assets/display-widget-value-min-rssi.png)

Depois de posicionado, ele é exibido como uma leitura simples na tela:

![Widget Value de telemetria](../assets/display-widget-value-telemetry.png)

**Bitmap** — exibe uma imagem estática (por exemplo, uma foto do modelo)
ou um conjunto de imagens alternadas conforme o valor de uma fonte (por
exemplo, um ícone de bateria que muda com a tensão):

![Configuração do widget Bitmap](../assets/display-widget-bitmap-config.png)
![Tipo do widget Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — um medidor de bateria dedicado, com leitura a partir de um
sensor como o FLVSS: tensão total do pack, número de células e a tensão de
cada célula individual. Cair abaixo do limite configurado em **Low
voltage** deixa a exibição em vermelho — no exemplo abaixo, um limite de
3,3 V é acionado pela célula mais baixa:

![Configuração do widget LiPo](../assets/display-widget-lipo-config.png)
![Widget LiPo](../assets/display-widget-lipo.png)

**Channels** — até 8 canais de saída em forma de gráfico de barras,
horizontal ou vertical:

![Configuração do widget Channels](../assets/display-widget-channels-config.png)
![Widget Channels](../assets/display-widget-channels.png)

**Line Chart** — traça o valor de uma fonte ao longo do tempo, reiniciando
em um Flight Reset:

![Configuração do widget Line chart](../assets/display-widget-line-chart-config.png)
![Widget Line chart](../assets/display-widget-line-chart.png)

- **Source** — o que está sendo representado no gráfico.
- **Pause condition** — uma fonte que pausa/retoma o registro (ou apenas
  toque no widget em execução, se não houver fonte livre para isso).
- **Log period** — intervalo de amostragem; 500 ms cobre aproximadamente 6
  minutos antes de rolar, 1 s cerca de 12 minutos.
- **Inverted** — inverte o gráfico verticalmente.
- **Auto range** — dimensiona o eixo vertical automaticamente para
  acomodar os dados; desativado, ele usa valores fixos de **Min**/**Max**
  (por exemplo, uma faixa constante de −100%…+100%).

Tocar em um gráfico em execução apresenta **Pause/resume**, **Reset**
(limpar e reiniciar), **Configure widget** ou o atalho para **Configure
screens**:

![Opções do Line chart](../assets/display-widget-line-chart-options.png)

**Text** — exibe o conteúdo de um arquivo de texto Markdown (lido de
`documents/user/` — consulte [Gerenciador de
arquivos](../system-setup/file-manager.md#top-level-folders)):

![Configuração do widget Text](../assets/display-widget-text-config.png)
![Widget Text](../assets/display-widget-text.png)

**Timer Log** — um registro rolável dos valores anteriores de um
temporizador escolhido, gravado a cada vez que esse temporizador é
zerado (útil para acompanhar o uso dos packs de voo ao longo de uma
sessão); **Reverse** coloca a entrada mais recente no topo:

![Configuração do widget Timer log](../assets/display-widget-timer-logs-config.png)
![Widget Timer log](../assets/display-widget-timer-log.png)

Pressione longamente uma entrada (ou o widget) para acessar **Clear
logs**, editar/zerar o temporizador correspondente ou ir para a
configuração do widget/tela:

![Menu de entrada do Timer log](../assets/display-widget-timer-log-menu.png)

**GPS Map** — traça a posição GPS ao vivo como uma trilha, para modelos
com sensor GPS (consulte o tópico *FrSky - ETHOS Lua Script Programming*
no rcgroups, post #8854, para mais detalhes especificamente sobre este
widget):

![Configuração do widget GPS map](../assets/display-widget-gps-map-config.png)

## Opções no nível da tela

Além dos widgets individuais, cada tela tem suas próprias configurações —
tamanho da grade do layout, plano de fundo e quais telas são incluídas no
ciclo do `PAGE`:

![Opções de configuração da tela](../assets/display-screen-config-options.png)

Uma tela inicial totalmente configurada combina vários widgets em um único
layout de leitura rápida:

![Visão principal](../assets/display-main-view.png)

Consulte [Telas adicionais](additional-displays.md) para adicionar mais
telas além da padrão, e [Widgets personalizados](custom-widgets.md) para
widgets criados com scripts Lua além do conjunto integrado.
