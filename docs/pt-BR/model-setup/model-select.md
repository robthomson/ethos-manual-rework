---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Seleção de modelo

![Assistente de modelo - avião](../assets/model-modelselect-model-wizard-airplane.png)

Cria, seleciona, clona e exclui modelos, além de gerenciar as pastas de
categoria definidas pelo usuário nas quais eles são organizados.

## Gerenciando as pastas de modelos

![Pastas de modelos](../assets/model-modelselect-folders.png)

O Ethos permite agrupar modelos em pastas próprias — normalmente algo como
Airplane, Glider, Heli, Quad, Warbird, Boat, Car, Template ou Archive.
Até que você crie alguma, os modelos ficam em uma pasta automática
**Uncategorized** (criada ao atualizar para o Ethos 1.1.0 alpha 17+, ou
quando um arquivo de modelo é copiado para `\Models` a partir de outro
local); o Ethos a exclui novamente quando ela fica vazia.

Para criar uma pasta, toque em **+** ao lado de "Uncategorized" (ou
pressione longamente `PAGE` para cima/para baixo), dê um nome a ela (até 15
caracteres) e confirme. As pastas são ordenadas alfabeticamente, com
**Uncategorized** sempre por último, e correspondem diretamente a subpastas
dentro de `\Models` no SD card/eMMC. Tocar no nome de uma pasta abre as
opções de renomear/excluir — excluir uma pasta move os modelos que estavam
nela de volta para Uncategorized.

![Alterar pasta](../assets/model-modelselect-folder-change-select.png)

Para mover um modelo, toque em seu ícone, escolha **Alterar pasta** e
depois toque no destino:

![Escolher pasta](../assets/model-modelselect-folder-airplane-select.png)

## Adicionando um novo modelo

![Criar modelo](../assets/model-modelselect-model-create.png)

Selecione a categoria na qual o modelo será criado, toque em **+** e depois
em **Criar modelo** para iniciar o assistente (crie a categoria primeiro,
caso ela ainda não exista). Há assistentes disponíveis para **Avião**,
**Planador**, **Helicóptero**, **Multirrotor** e **Outro**; cada um conduz
pela configuração básica daquele tipo de aeronave, incluindo mixagens
pré-definidas opcionais para receptores estabilizados FrSky (ganho, modo de
estabilização). Os nomes de modelo podem ter até 15 caracteres.

### Receptores estabilizados e ordem dos canais

![Assistente: avião](../assets/model-modelselect-model-wizard-airplane.png)

Os receptores estabilizados FrSky exigem especificamente a ordem de canais
**AETR** — mantenha [Sticks → Ordem dos canais](../system-setup/controls.md)
no padrão AETR com **Primeiros quatro canais fixos** ativado, de modo que a
saída do assistente corresponda ao que o receptor espera.

O assistente atribui os canais da direita para a esquerda. Para 2 ailerons
+ 1 profundor + 1 leme + 1 motor, fica assim:

| Ch | Função |
|---|---|
| 1 | Aileron 1 (aileron direito) |
| 2 | Profundor |
| 3 | Acelerador |
| 4 | Leme |
| 5 | Aileron 2 (aileron esquerdo) |

Com essa atribuição, o diferencial de aileron é **positivo** para o caso
normal (mais deflexão para cima do que para baixo). Os manuais de receptor
da própria FrSky atualmente documentam a convenção *oposta* (da esquerda
para a direita, portanto Ch1 = aileron esquerdo, Ch5 = aileron direito) —
nesse caso, o diferencial precisaria ser **negativo** para o mesmo efeito
físico.

!!! tip
    Recomenda-se usar a convenção do Ethos de forma consistente — todas as
    funções de estabilização continuam funcionando corretamente de qualquer
    maneira, já que o sentido da compensação é definido durante a
    configuração da estabilização. Se você realmente precisar seguir a
    convenção do manual do receptor, o caminho mais simples é criar o modelo
    com o assistente normalmente e, depois, usar **Trocar canais** em
    [Saídas](outputs.md) para inverter os dois canais de aileron — isso
    mantém positivo o sinal do diferencial no mixer de aileron.

### Etapas do assistente

![Assistente: tipo de cauda](../assets/model-modelselect-model-wizard-tail.png)
![Assistente: quantidade de ailerons/flaps](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Assistente: quantidade de profundor/leme](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Assistente: motor](../assets/model-modelselect-model-wizard-engine.png)
![Assistente: reatribuição de canais](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Assistente: nome](../assets/model-modelselect-model-wizard-name.png)
![Assistente: receptor](../assets/model-modelselect-model-wizard-rx.png)

Para um **Avião**, após o tipo de cauda e as quantidades de superfícies, o
assistente trata da quantidade de canais do motor e, em seguida, da
quantidade de canais de aileron/flap.

A **configuração de cauda** oferece a escolha entre cauda cruzada
tradicional, cauda em V ou nenhuma cauda (delta/asa voadora):

- **Delta/asa voadora** — criar um modelo Avião com 2 ailerons e nenhuma
  superfície de cauda gera automaticamente a mixagem de elevons, com pesos
  padrão de 50%, para que comandos simultâneos completos de aileron +
  profundor ainda totalizem 100%.
- **Delta com um receptor estabilizado fazendo a mixagem** — selecione, em
  vez disso, 1 aileron e 1 profundor; a mixagem de elevons ocorre no
  receptor, conforme o manual dele.
- **Delta com superfícies dedicadas de aileron e profundor** — deixe o
  assistente prosseguir como se o modelo tivesse cauda; ele configura os
  canais de aileron e profundor necessários (com ou sem leme), e nenhuma
  mixagem de elevons é criada.

A etapa de **reatribuição de canais** permite substituir o mapeamento
padrão do assistente, tendo em mente que receptores estabilizados precisam
de seus canais em uma ordem específica (consulte as instruções do próprio
receptor). A etapa final define o nome do modelo e vincula uma imagem.

O modelo concluído é colocado na pasta de categoria que estava ativa quando
o assistente foi iniciado, ordenado alfabeticamente dentro dela. Consulte
[Exemplo básico de asa fixa](../tutorials/basic-fixed-wing.md) para um
passo a passo completo.

## Recebendo um modelo de outro rádio Ethos

![Receber modelo](../assets/model-modelselect-model-receive.png)

Selecione a categoria de destino, toque em **+** e depois em **Receber
modelo** — o rádio aguarda e mostra seu endereço Bluetooth para que o
remetente possa encontrá-lo. No rádio que envia, toque no modelo e escolha
**Enviar modelo**; o rádio receptor confirma o nome do arquivo recebido
antes de aceitá-lo.

## Selecionando um modelo

Toque em **Seleção de modelo** para ver a lista de modelos.

!!! note "Conversão de modelos após uma atualização do Ethos"
    O Ethos converte cada modelo individualmente na primeira vez em que ele
    é *selecionado* após uma atualização de versão, e não todos de uma vez
    durante a atualização — não há atraso perceptível, e é seguro fazer isso
    em qualquer momento posterior, mesmo sob uma versão ainda mais nova do
    Ethos. A data de **Última modificação** na parte inferior da tela de
    seleção é atualizada quando ocorre uma conversão (ou quando você edita o
    modelo — caso contrário, permanece inalterada).

**Seleção rápida** — um toque longo ou um `ENT` longo no ícone de um modelo
alterna imediatamente para ele.

**Menu de gerenciamento de modelos** — toque em um modelo para destacá-lo e
toque novamente para abrir o menu:

- **Definir modelo atual**
- **Clonar** — duplica o modelo. Um clone recebe automaticamente um novo
  número de receptor; se, em vez disso, você reatribuir o número de receptor
  do original, ele funciona sem necessidade de novo bind.
- **Alterar pasta**
- **Enviar**/**Receber** — para ou de outro rádio, como descrito acima.
- **Excluir** — oferecido apenas para um modelo que não seja o atual.
