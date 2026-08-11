---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Variáveis

![Variáveis](../assets/model-vars.png)

As variáveis ("Vars") são contêineres nomeados para os valores de ajuste
próprios de um modelo, referenciáveis em qualquer outro ponto da
programação — incluindo as [mixagens](mixes.md). Mantê-las em sua própria
seção separa os *dados de configuração* do modelo de sua *lógica de
programação*: em vez de procurar entre dezenas de mixagens para encontrar
e ajustar um valor, tudo fica em um único lugar com um nome significativo.
Estão disponíveis 64 Vars; nenhuma existe por padrão. Adicione uma com
**+**; toque em uma Var existente para **Editar**/**Mover**/
**Copiar**/**Clonar**/**Excluir**.

![Adicionar variável](../assets/model-vars-add.png)

Uma Var pode conter uma constante fixa ou ser ajustável dentro de limites
definidos pelo usuário (para evitar que valores inadequados causem uma
queda), e pode conter um valor *diferente* por condição ativa (por
exemplo, por fase de voo). Os valores são persistentes entre sessões. Uma
Var substitui qualquer valor numérico comum em qualquer lugar onde o
[recurso Opções](../getting-started/user-interface-and-navigation.md#the-options-feature)
esteja disponível (os campos com o ícone de hambúrguer).

!!! example
    Um planador com ailerons divididos (as seções internas atuando também
    como flaps de pouso) precisa de um único ajuste compartilhado de
    diferencial de aileron, usado em todos os casos em que as quatro
    superfícies atuam como ailerons — uma Var contendo esse único valor,
    referenciada em cada mixagem relevante, mantém tudo consistente e faz
    com que o ajuste precise ser feito em apenas um lugar.

## Adicionando uma Var

![Nova variável](../assets/model-vars-new_var.png)

- **Valor** — valor atual (exibição somente leitura).
- **Nome** — editável.
- **Comentário** — texto livre explicando sua finalidade.
- **Faixa** — limites inferior/superior (uma casa decimal, dentro de
  ±500%) que o valor da Var nunca pode exceder.

### Valores

![Valores da variável](../assets/model-vars-values.png)

- **Fixo** — uma única constante, com uma casa decimal.
- **Múltiplo/variável** — **Adicionar novo valor** vincula um valor por
  condição ativa. Por exemplo, `Var12` indica 9% enquanto a fase de voo
  Thermal (FM4) está ativa e −3% enquanto Speed (FM5) está ativa, com sua
  Faixa restrita a −10%…+15%, de modo que nenhum dos dois possa exceder
  limites sensatos:

  ![Valores dependentes da fase de voo](../assets/model-vars-fm-dependent.png)
  ![Adicionar um valor](../assets/model-vars-add-value.png)

### Ações

![Ações da variável](../assets/model-vars-actions.png)
![Adicionar ação](../assets/model-vars-add-action.png)

As ações alteram o valor de uma Var ao longo do tempo, acionadas por uma
entrada.

**Trim reaproveitado** — entrega um dos trims físicos para o ajuste desta
Var em vez de sua função normal, tipicamente restrito a uma condição
ativa:

![Reaproveitar um trim](../assets/model-vars-functions-repurpose.png)
![Selecionar o trim a reaproveitar](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Reaproveite o trim do acelerador para ajustar uma Var de compensação
    de camber, mas apenas enquanto a fase de voo Landing (FM3) estiver
    ativa, com Faixa de 0–25% e passo de 1,0% por clique. Fora dessa
    condição ativa, o trim volta automaticamente à sua função comum.

**Ações aritméticas** — acionadas por qualquer entrada:

- **Atribuir** — define a Var com um valor específico.
- **Somar** / **Subtrair** / **Multiplicar** / **Dividir** — operações
  aritméticas sobre o valor atual.
- **Porcentagem** — aplica uma porcentagem da entrada de acionamento.
- **Mín** / **Máx** — limita a Var em relação à entrada de acionamento.

  ![Ações de função](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` atribui diretamente 40% a uma Var; `FS1(edge)` soma 2 a
    cada acionamento (limitado ao máximo da Faixa); `FS2(edge)` subtrai 2
    a cada acionamento (limitado ao mínimo da Faixa). A opção **Edge**
    (pressione longamente o interruptor de função) é importante aqui —
    sem ela, a ação seria disparada continuamente enquanto o interruptor
    fosse mantido acionado, em vez de uma vez por acionamento.

  ![Exemplo resolvido](../assets/model-vars-calc-example.png)
