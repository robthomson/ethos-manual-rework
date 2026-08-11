---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Vistas principais

## Tela inicial

![Tela inicial](../assets/mainview.png)

A tela inicial é o que você vê sempre que nenhum menu está aberto — um conjunto
de até **oito** telas de exibição que você mesmo configura (consulte
[Telas](../displays/index.md)), navegadas com a tecla `PAGE` ou por deslize
na tela sensível ao toque. Um modelo recém-criado começa com apenas uma tela,
mostrando uma imagem do modelo, três widgets de temporizador e os indicadores
de trim/potenciômetro; tudo nela é configurável pelo usuário a partir daí.

Normalmente as telas compartilham as barras superior e inferior descritas
abaixo, mas uma tela também pode ser definida como tela cheia, ocultando ambas.

## A barra superior

A barra superior mostra o nome do modelo à esquerda (além da fase de voo ativa,
se alguma estiver configurada) e uma linha de ícones de status à direita:

- Registro de dados ativo
- Status do trainer (mestre ou escravo, conforme o caso)
- RSSI — link de 2.4GHz
- RSSI — link de 900MHz (se um módulo de banda dupla/longo alcance estiver instalado)
- Volume do alto-falante
- Status da bateria do rádio

Tocar no ícone do alto-falante ou da bateria leva diretamente ao painel de
configurações correspondente: [Geral](../system-setup/general.md) (áudio) ou
[Bateria](../system-setup/battery.md).

### Aviso de erro

Um triângulo vermelho aparece na barra superior sempre que o Ethos detecta um
erro — as causas mais comuns são um erro em script Lua, um erro de backup da
RAM ou o uso de uma versão de firmware nightly/instável. O detalhe por trás do
aviso está sempre em **System → Info**, na mesma página do tempo de uso do
rádio e dos [registros de erro](../system-setup/information.md).

## A barra inferior

![Barra inferior](../assets/bottombar.png)

Quatro abas se estendem ao longo da parte inferior para as seções principais —
**Início**, **Configuração do modelo**, **Configurar telas**, **Configuração do
sistema** — com o relógio do sistema à direita (toque nele para ir diretamente
para [Data e Hora](../system-setup/date-and-time.md)).

## A área de widgets

O centro de cada tela é preenchido por **widgets**: imagem do modelo,
temporizadores, leituras de telemetria, barras de trim/potenciômetro e muito
mais, todos posicionados e configurados por você. Consulte
[Telas](../displays/index.md) para saber como adicionar, mover e configurar
widgets, e [Telas adicionais](../displays/additional-displays.md) para
adicionar mais telas além da única tela padrão.
