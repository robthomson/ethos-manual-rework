---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Interface do usuário e navegação

O Ethos pode ser operado inteiramente com o **encoder rotativo** do lado
direito (gire para mover o destaque, pressione para `ENT`) e a tecla `RTN`
para sair de um menu — a tela sensível ao toque, quando presente, é um atalho
para as mesmas ações, não uma forma de trabalho separada. `MDL`, `DISP` e
`SYS` levam diretamente a Configuração do modelo, Configurar telas e
Configuração do sistema, respectivamente (os mesmos três blocos da barra
inferior); um pressionamento longo em `RTN` a partir de qualquer lugar
retorna diretamente à tela inicial.

## O menu de reset

![Menu contextual](../assets/resetmenu.png)

Um pressionamento longo em `ENT` na tela inicial abre um menu de reset:

- **Reset flight** — reinicia a telemetria, os temporizadores e os
  interruptores de função, além de executar novamente a
  [lista de verificação](../model-setup/checklist.md) pré-voo.
- **Reset telemetry** — reinicia apenas a telemetria.
- **Reset timers** — reinicia apenas os temporizadores.
- **Lock touchscreen** — também acessível pressionando `ENT` + `PAGE`
  juntos por um segundo na tela inicial, ou como acionador de
  [função especial](../model-setup/special-functions.md).

## Controles de edição

**Adicionar elementos funcionais** — um temporizador, interruptor lógico,
função especial, curva ou variável é criado tocando no **+** ao lado dos
títulos das colunas no menu correspondente. Em um rádio sem tela sensível ao
toque, destaque um elemento existente, pressione `ENT` e escolha **Add** no
menu — a mesma opção também está disponível em rádios com tela sensível ao
toque.

### Teclado virtual

![Teclado de texto](../assets/keyboard-text-azerty.png)

Tocar em qualquer campo de texto (ou pressionar `ENT` sobre ele) abre o
teclado na tela. A tecla de retrocesso apaga à esquerda do cursor; `PAGE`
apaga à direita e, quando o cursor chega ao fim do texto, continua apagando
a partir da esquerda. Tocar no próprio campo move o cursor para aquela
posição — ou use `SYS`/`DISP` para movê-lo para a esquerda/direita sem o
toque. A tecla **?123**/**abc** alterna o teclado numérico (que também
contém caracteres especiais):

![Teclado numérico](../assets/keyboard-text-numbers.png)

Em um **rádio sem tela sensível ao toque**, pressionar `ENT` sobre um campo
de texto entra diretamente no modo de edição: gire o encoder para percorrer
minúsculas, maiúsculas, dígitos e, por fim, caracteres especiais,
pressionando `ENT` para inserir cada um. `MDL` alterna entre maiúscula e
minúscula do caractere imediatamente à direita do cursor (e todo caractere
digitado em seguida permanece nesse formato até ser alternado novamente).
`PAGE` apaga à direita do cursor; `SYS`/`DISP` o movem para a
esquerda/direita.

## Controles de valores numéricos

![Entrada de números](../assets/keyboard-numbers.png)

Tocar em um campo numérico abre uma faixa de controles na parte inferior da
tela: **`<`**/**`>`** alteram o tamanho do passo (alternando entre décadas —
por exemplo, 0,01/0,1/1,0/10,0), **`-`**/**`+`** (ou o encoder rotativo)
ajustam o valor conforme esse passo, e **More** abre opções adicionais:

![Opções de entrada de números](../assets/keyboard-numbers-options.png)

- Ir para o valor padrão do campo
- Definir o mínimo / definir o máximo
- Substituir o controle de passos por um **slider**

![Entrada por slider](../assets/keyboard-numbers-slider.png)

O slider (também ajustável com o encoder rotativo) é mais rápido para
alterações grosseiras; **Disable slider** volta ao controle de passos. Os
valores de faixa de telemetria são editados da mesma maneira:

![Slider desativado](../assets/keyboard-numbers-options-disable-slider.png)

## O recurso Options {: #the-options-feature }

Em praticamente todo lugar em que se espera um valor ou uma
[fonte](#choosing-a-source), um pressionamento longo em `ENT` abre uma caixa
de diálogo **Options** — procure o pequeno ícone de menu ("hambúrguer") no
canto superior esquerdo do campo como sinal de que o recurso está disponível.

### Opções de valor

![Opções de fonte](../assets/source-with-options.png)

A caixa de diálogo de opções de valor indica o parâmetro que está sendo
editado e oferece a escolha entre mínimo/máximo fixos ou controlá-lo por uma
**fonte** (por exemplo, um potenciômetro, para ajustar o valor em voo). Se o
campo já utiliza uma fonte, o mesmo pressionamento longo oferece, em vez
disso, converter o valor atual dessa fonte em um valor fixo:

![Converter fonte em valor](../assets/source-convert-to-value.png)

### Escolhendo uma fonte {: #choosing-a-source }

Selecionar **Choose a source** abre um seletor de duas colunas — primeiro uma
**categoria** (analógicos, interruptores, interruptores lógicos, trims,
canais, um eixo do giroscópio, um canal de treinador, um temporizador, um
sensor de telemetria ou alguns valores especiais) e, em seguida, o membro
específico dela:

![Menu de fontes](../assets/source-menu.png)

Definida a fonte, o mesmo pressionamento longo abre opções específicas para
o tipo de fonte em questão:

**Qualquer fonte** —

- **Invert** — nega a fonte (por exemplo, ativa quando um interruptor *não*
  está para cima, em vez de quando está).
- **Edge** — dispara uma única vez em uma transição (falso→verdadeiro ou
  verdadeiro→falso), em vez de permanecer ativa durante todo o estado;
  exibida com o prefixo `†` na fonte. Disponível em interruptores de forma
  geral e, especificamente, na condição de acionamento do
  [interruptor lógico Sticky](../model-setup/logical-switches.md).

**Fontes de stick** — opções no estilo calibração/subtrim:

![Opções de fonte de stick](../assets/source-stick-options.png)

**Fontes de interruptor** —

![Opções de interruptor de 2 posições](../assets/source-2pos-options.png)
![Opções de interruptor](../assets/switch-options.png)

- **Negative** — inverte a ação do interruptor.
- **HalfRange** — para um interruptor de 2 posições ou interruptor lógico,
  altera sua faixa de saída de ±100% para 0–100%.

**Fontes de trim** —

![Opções de fonte de trim](../assets/source-trim-options.png)

- **Negative** — inverte a ação do trim (útil dentro das Actions de uma
  mixagem livre).
- **Full range** — os trims têm por padrão ±25%; como fonte, isso pode ser
  ampliado para ±100%.
- **Ignore trainer input** — em um
  [interruptor lógico](../model-setup/logical-switches.md), exclui o
  movimento da entrada de treinador do acionamento do interruptor. Uso
  típico: detectar o movimento do stick do próprio treinador *mestre* (por
  exemplo, para intervir instantaneamente se o aluno fizer algo errado) sem
  que as entradas de stick do aluno também o acionem.

**Fontes de variável** —

![Opções de fonte de variável](../assets/source-var-options.png)

- **Negative** — nega o valor da variável para este uso.
- **Ignore range** — alguns campos têm faixas assimétricas (por exemplo,
  Min/Max das Saídas, que vão de −150–0% e 0–150%, respectivamente). A menos
  que uma [variável](../model-setup/variables.md) usada como fonte desse
  campo tenha uma faixa idêntica, ative esta opção para ignorar a conversão
  automática de faixa do Ethos e evitar valores inesperados.

**Fontes de sensor de telemetria** — reduzem a fonte ao seu mínimo ou máximo
ao vivo, em vez da leitura instantânea (alguns sensores acrescentam outras
opções específicas do sensor além desta):

![Opções de mín./máx. do sensor](../assets/source-sensor-options.png)
![Máximo do sensor selecionado](../assets/source-sensor-maxi.png)
