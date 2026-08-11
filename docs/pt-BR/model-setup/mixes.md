---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Mixagens

![Ícone de Mixagens](../assets/model-icon-mixes.png)

As mixagens são o núcleo da programação de modelos no Ethos — é aqui que as entradas
(sticks, interruptores, sensores, qualquer coisa que uma [fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)
possa alcançar) são roteadas, moldadas e combinadas nos canais de saída. É possível
definir até 120 mixagens por modelo.

![Tabela de mixagens](../assets/model-mixes.png)

Se o modelo foi criado com o assistente de **Seleção de modelo**, suas mixagens básicas
(aileron, profundor, acelerador, leme e o que mais a célula exigir)
já estarão preenchidas aqui. Selecionar uma mixagem e pressionar `ENT` abre um
menu contextual para editá-la, adicionar uma nova mixagem, alternar para a
[visualização por canal](#per-channel-view), reordená-la, duplicá-la ou excluí-la.
Mixagens inativas aparecem em cinza, e a exclusão sempre pede confirmação
antes.

## Anatomia de uma mixagem {: #anatomy-of-a-mix }

Toda mixagem compartilha o mesmo conjunto de campos, independentemente da categoria
de origem. A mixagem de **aileron** é um exemplo representativo — as mixagens de
profundor e leme têm exatamente a mesma estrutura.

![Mixagem de aileron](../assets/model-mixes-ail-edit.png)

![Editor da mixagem de aileron](../assets/model-mixes-ail.png)

**Nome** — o padrão é o tipo da mixagem, podendo ser editado.

**Condição** — o padrão é *Always*. Pode ser restringida a uma posição de
interruptor, um interruptor de função, um interruptor lógico, uma fase de voo, um
evento do sistema (corte/retenção de acelerador) ou uma posição de trim, caso em que
a mixagem só é aplicada enquanto a condição for verdadeira.

**Fases de voo** — se houver fases de voo definidas, a mixagem também pode ser
restringida a uma ou mais delas.

**Curva** — uma curva **Expo** está disponível por padrão (0 = linear; valores positivos
suavizam a resposta em torno do centro, valores negativos a tornam mais agressiva):

![Curva expo](../assets/model-mixes-ail-expo.png)

Qualquer curva previamente definida em [Curvas](curves.md) pode ser selecionada
no lugar. É possível empilhar até 6 curvas em uma mixagem, cada uma com sua própria
condição — se mais de uma condição for verdadeira simultaneamente, prevalece a curva
mais alta na lista. As curvas são aplicadas **antes** das taxas.

**Taxas** — uma ou mais linhas de peso, cada uma opcionalmente condicionada por um
interruptor, interruptor de função, interruptor lógico, posição de trim ou fase de voo.
A primeira linha é a padrão, ativa sempre que nenhuma condição das outras linhas for
atendida:

![Taxas do aileron](../assets/model-mixes-ail-weight.png)

Em vez de uma porcentagem fixa, uma taxa pode ser controlada por uma
[fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)
— por exemplo, um potenciômetro, para ajustar a taxa em voo:

![Taxa controlada por uma fonte](../assets/model-mixes-ail-diff.png)

**Diferencial** (-100 a 100, padrão 0) — proporciona mais curso em uma direção
do que na outra. Para ailerons, esse é o truque clássico de dar mais deflexão
para cima do que para baixo, a fim de reduzir a guinada adversa. Só é exibido quando a
mixagem tem mais de um canal de saída; o diferencial exige especificamente uma
configuração de saída do tipo cauda em V ou aileron duplo para fazer sentido.

**Número de canais / saídas** — quantos canais de saída esta mixagem controla
e a quais saídas físicas eles são mapeados:

![Contagem de canais](../assets/model-mixes-ail-ch-count.png)

Um pressionamento longo de `ENT` sobre um canal de saída em outro ponto da interface
(por exemplo, em [Saídas](outputs.md)) leva diretamente de volta a esta página.

## A mixagem de acelerador

A mixagem de acelerador é uma mixagem de aileron/profundor/leme somada a opções de
segurança específicas do motor.

![Mixagem de acelerador](../assets/model-mixes-thr.png)

**Entrada** — a fonte do acelerador, normalmente o stick de acelerador, mas
substituível por um potenciômetro, slider, interruptor, trim, canal, eixo de giroscópio,
canal de treinador, temporizador ou qualquer outra fonte.

**Trim de marcha lenta** — para motores a combustão, permite que um trim dedicado ajuste
a rotação de marcha lenta sem alterar a posição de aceleração máxima. Com o trim de
marcha lenta ativado, o canal de acelerador fica em -75% com o stick na marcha lenta
baixa, e o trim de acelerador então ajusta a marcha lenta entre -100% e -50%:

![Menu do trim de marcha lenta](../assets/model-mixes-thr-trim-menu.png)

![Trim de marcha lenta na posição baixa](../assets/model-mixes-thr-trim-low-position.png)

**Corte de acelerador** — um bloqueio de segurança rígido: o canal só fica ativo depois
que o stick de acelerador passa pela marcha lenta, de modo que um acionamento acidental
de interruptor não possa acelerar o motor a partir de uma posição de aceleração alta:

![Corte de acelerador](../assets/model-mixes-thr-cut.png)

**Retenção de acelerador** — mantém o canal em um valor fixo independentemente da
posição do stick, sem o bloqueio de segurança que o corte de acelerador oferece:

![Retenção de acelerador](../assets/model-mixes-thr-hold.png)

O acelerador também expõe sua própria contagem de canais de saída, como qualquer outra
mixagem:

![Contagem de canais do acelerador](../assets/model-mixes-thr-ch-count.png)

!!! note "Bloqueio do acelerador"
    O Ethos exige que a entrada da mixagem de acelerador passe por -100% antes de
    armar, independentemente das configurações de corte/retenção de acelerador — um
    modelo criado pelo assistente de seleção de modelo já leva isso em conta, mas
    mixagens de acelerador criadas manualmente também devem fazê-lo.

## Bibliotecas de mixagens {: #mix-libraries }

A biblioteca de mixagens predefinidas da caixa de diálogo **Add mix** é adaptada à
categoria de modelo escolhida quando o modelo foi criado — avião, planador, helicóptero
e multirrotor expõem conjuntos diferentes:

![Biblioteca de mixagens de avião](../assets/model-mixes-library-airplane.png)

![Biblioteca de mixagens de planador](../assets/model-mixes-library-glider.png)

![Biblioteca de mixagens de helicóptero](../assets/model-mixes-library-heli.png)

![Biblioteca de mixagens de multirrotor](../assets/model-mixes-library-multirotor.png)

Todas as bibliotecas também incluem a **Mixagem livre** — um tipo de mixagem de uso
geral, sem entrada/saída pré-definida, mais flexível que as entradas especializadas,
mas exigindo mais configuração para alcançar o mesmo resultado.

## Visualização por canal {: #per-channel-view }

Com muitas mixagens empilhadas na mesma saída, pode ser difícil perceber seu
efeito combinado na tabela plana acima. Selecionar uma mixagem e escolher
**View by channel** agrupa todas as mixagens que afetam uma mesma saída:

![Alternar para a visualização por canal](../assets/model-mixes-chview-select.png)

![Canal recolhido](../assets/model-mixes-chview-collapsed.png)

![Canal do profundor expandido](../assets/model-mixes-chview-elevator.png)

Expandir a linha de resumo de um canal mostra todas as mixagens que contribuem para
ele, cada uma com sua saída numérica e gráfica em tempo real — útil para confirmar
exatamente quanto uma mixagem secundária (por exemplo, compensação de flapes para o
profundor) está somando à entrada primária do stick:

![Detalhe da visualização do canal do profundor](../assets/model-mixes-chview-elevator-channel.png)

![Canal do profundor, mixagem destacada](../assets/model-mixes-chview-elevator-channel-view.png)

Selecionar uma sub-mixagem em vez da linha de resumo abre o mesmo menu contextual
da tabela plana (editar, voltar à visualização em tabela, excluir):

![Selecionar a visualização em tabela a partir da visualização por canal](../assets/model-mixes-chview-table-view-select.png)

![De volta à visualização em tabela](../assets/model-mixes-chview-back-at-mixes-view.png)
