---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Fases de voo

![Fases de voo](../assets/model-fm.png)

As fases de voo (flight modes) permitem que um interruptor selecione
comportamentos distintos para o mesmo modelo — planadores podem usar
Lançamento/Cruzeiro/Velocidade/Térmica, aviões a motor Normal/Decolagem/
Pouso, helicópteros Normal (aceleração inicial, decolagem/pouso) / Idle Up
1 (acrobacia) / Idle Up 2 (3D). Elas retiram do piloto a maior parte do
trabalho de acionar interruptores e reajustar trims manualmente: uma fase
de voo pode ter seus próprios trims independentes e pode condicionar tanto
[Variáveis](variables.md) quanto [Mixagens](mixes.md) — juntas, isso é
suficiente para configurações realmente complexas. Consulte o [Exemplo
básico de asa fixa](../tutorials/basic-fixed-wing.md) para ver as fases de
voo aplicadas a um modelo real.

Nenhuma fase de voo é definida por padrão. Toque na fase de voo padrão e
escolha **Editar** para renomeá-la, ou **Adicionar** para criar uma nova —
até 20 no total.

## Nome

Um nome descritivo — Cruzeiro, Velocidade, Térmica, Decolagem, Pouso, o
que for mais adequado.

## Condição de ativação

![Formulário da fase de voo](../assets/model-fm-form.png)

Uma nova fase de voo começa inativa (`---`). Depois de definida, ela pode
ser acionada pela posição de um interruptor ou botão, por um interruptor
de função, por um interruptor lógico, por um evento do sistema (corte/
retenção de acelerador) ou pela posição de um trim.

A fase de voo **padrão** não tem nenhuma Condição de ativação — ela é a
que fica ativa sempre que a condição de nenhuma outra fase de voo é
verdadeira. Apenas uma fase de voo fica ativa por vez: a primeira (na
ordem de prioridade) cuja condição seja verdadeira naquele momento. A fase
ativa é exibida em negrito.

!!! warning "Adicionando uma fase de voo a um modelo existente"
    Uma fase de voo recém-adicionada fica, por padrão, ativa em todas as
    mixagens que já dependem de fases de voo — verifique se cada uma
    dessas mixagens continua se comportando corretamente, em especial uma
    mixagem **Lock** que travе um canal em uma fase de voo específica.

## Fade in, out

Tempos de transição para mesclar suavemente as fases de voo (por exemplo,
1 segundo em cada sentido) — isso só tem efeito em mixagens que sejam elas
mesmas dependentes de fases de voo.

## Gerenciamento das fases de voo

![Mover fase de voo](../assets/model-fm-move.png)
![Selecionar para mover](../assets/model-fm-move-select.png)
![Fases 0-3](../assets/model-fm-0to3.png)

Toque em uma fase de voo para **Editar**, **Adicionar**, **Clonar** ou
**Excluir**. Uma fase de voo **clonada** herda as configurações da fase de
origem em todas as mixagens que usam fases de voo — mesmo comportamento,
mesmo estado ativo/inativo — por isso um clone é adicionado como a última
fase de voo por padrão, para evitar interferência com as existentes.
**Mover** altera a prioridade de uma fase de voo: a prioridade segue a
ordem crescente e, como já indicado, a primeira cuja condição for
verdadeira é a que fica ativa.
