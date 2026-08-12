---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Mixagem Butterfly (Corvo)

A frenagem butterfly (também conhecida como crow) controla a taxa de
descida, principalmente em planadores: os ailerons sobem moderadamente
enquanto os flaps descem bastante, criando um arrasto significativo —
ideal para controlar a aproximação de pouso. Este passo a passo pressupõe
um planador cujos canais de Flaps já existem (criados pelo assistente
[Seleção de modelo](../model-setup/model-select.md)), usando o stick do
acelerador como entrada do freio: sem butterfly com o stick para cima e
progressivamente mais conforme ele desce, com compensação de profundor
para que o planador não suba abruptamente quando o crow é aplicado.

## 1. Desative a mixagem de Flaps padrão

![Desativar a mixagem de flaps](../assets/how-to-butterfly-flaps-disable.png)

Defina a **Condição ativa** da mixagem de Flaps criada pelo assistente
como `---` — ela não será utilizada.

## 2. Crie a mixagem Butterfly

![Mixagem Butterfly adicionada](../assets/how-to-butterfly-mix-added.png)

Toque em qualquer mixagem, **Adicionar mixagem** → **Butterfly** na
[biblioteca de mixagens](../model-setup/mixes.md#mix-libraries),
posicionada depois da mixagem de Flaps (agora desativada).

## 3. Configure a entrada

![Entrada do acelerador](../assets/how-to-butterfly-mix-source-thr.png)

Defina a **Entrada** como **Acelerador**. Como o acelerador normalmente
indica o valor máximo com o stick para cima, e o butterfly precisa ser 0
com o stick para cima, pressione e mantenha `ENT` sobre Acelerador e
selecione **Inverter**:

![Inverter o acelerador](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Acelerador invertido](../assets/how-to-butterfly-mix-source-thr-neg.png)

A entrada agora indica 0 com o stick totalmente para cima, e o campo
mostra `-Throttle` para confirmar a inversão. Defina a **Condição ativa**
como uma fase de voo de pouso (ou outro interruptor) caso o butterfly não
deva estar sempre disponível.

## 4. Adicione uma curva com zona morta

![Seleção de curva](../assets/how-to-butterfly-mix-curve-select.png)

Uma pequena zona morta na extremidade zero do stick evita o acionamento
acidental por pequenas variações do stick próximas ao fim de curso.
Adicione uma curva personalizada de 3 pontos (por exemplo, chamada
"Crowdb") com o **Modo fácil** desativado, para que os pontos X possam
ser movidos:

![Curva de 3 pontos](../assets/how-to-butterfly-mix-curve-3pt.png)
![Pontos da curva](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    Adicionar uma curva personalizada à mixagem Butterfly remove o offset
    interno de 0–100 (normalmente aplicado automaticamente) — a própria
    curva agora precisa reproduzir essa transformação de 0–100. Neste
    exemplo, a saída permanece em 0% até que o stick do acelerador
    alcance −90%, subindo então linearmente até 100%:

    ![Curva adicionada](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Configure ailerons e flaps

![Saída de aileron](../assets/how-to-butterfly-mix-ailerons.png)

Uma subida moderada dos ailerons (por exemplo, 20%) combinada com uma
grande deflexão dos flaps é a divisão habitual. Os flaps normalmente
precisam de muito mais curso para baixo do que para cima — o que
geralmente é obtido deslocando os braços dos servos dos flaps 20–30° do
neutro no próprio sistema de comando, o que deixa os flaps
aproximadamente na metade do curso para baixo com o servo no neutro:

![Flaps para cima](../assets/how-to-butterfly-mix-flaps-up.png)
![Flaps para baixo](../assets/how-to-butterfly-mix-flaps-down.png)

Defina um peso alto na mixagem dos flaps (por exemplo, −180%) para obter
o curso máximo; o curso físico real é determinado pelos valores Min/Max
em [Saídas](../model-setup/outputs.md).

!!! tip
    Para evitar forçar os servos, comece com valores Min/Max
    conservadores em Saídas (por exemplo, ±30%) e amplie-os com cuidado
    durante o ajuste final, atento a travamentos mecânicos.

## 6. Adicione uma mixagem de offset "Flaps Neutral"

![Mixagem de offset de 80%](../assets/how-to-butterfly-offset-mix-80.png)

Como o deslocamento dos braços dos servos deixa os flaps defletidos
cerca de 20–30% com o servo no neutro, uma **Mixagem de offset** os
traz de volta à posição realmente neutra da asa para o voo normal.
Comece com um offset de 80% (a ser ajustado), com 2 canais de saída
mapeados para ambos os canais de flap:

![Flaps para cima com offset](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Flaps para baixo com offset](../assets/how-to-butterfly-offset-mix-flaps-down.png)

Com o stick do acelerador totalmente para cima (mixagem Butterfly
desativada), confirme que os valores da mixagem dos flaps estão no valor
do offset (80%); mover o stick dos flaps até a deflexão total deve
deslocar a saída da mixagem pelo peso completo (por exemplo, de 80% até
−100%, uma variação de 180%). Ajuste os limites reais de curso em Saídas
usando Min/Max ou uma curva.

## 7. Adicione a curva e a mixagem de compensação de profundor {: #7-add-the-elevator-compensation-curve-and-mix }

![Curva de compensação](../assets/how-to-butterfly-comp-curve.png)
![Pontos da curva de compensação](../assets/how-to-butterfly-comp-curve-points.png)

Como a compensação necessária é não linear, use uma curva em vez de um
peso fixo. Defina uma curva personalizada de 5 pontos (por exemplo,
"EleComp") — este exemplo começa com 12%/10%/8%/5%/0% ao longo de seus
pontos; sem um ponto de partida conhecido para a sua aeronave, esses
valores precisam ser encontrados empiricamente.

Em seguida, converta essa curva em um valor utilizável como **Peso** de
mixagem: adicione uma [Mixagem livre](../model-setup/mixes.md#mix-libraries)
("EleCompx") com Acelerador como fonte e a curva EleComp associada, com
saída para um canal alto não utilizado (por exemplo, CH20):

![Mixagem de compensação no CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

De volta à mixagem Butterfly, pressione e mantenha `ENT` sobre o **Peso**
da saída de Profundor, escolha **Usar uma fonte** e então selecione CH20
(EleCompx) na categoria Canais:

![Profundor usando CH20 como fonte](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Selecionar fonte](../assets/how-to-butterfly-mix-ele-use-source.png)

A mixagem Butterfly está agora totalmente configurada:

![Compensação de profundor configurada](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Verifique com a visualização por canal

![Visualização por canal](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Mude para [Visualizar por canal](../model-setup/mixes.md#per-channel-view)
no Profundor para observar todas as mixagens que contribuem (entrada do
stick + compensação do Butterfly) sendo atualizadas simultaneamente
conforme o stick de acelerador/freio se move — muito mais fácil de
depurar do que a visualização em tabela simples.

!!! tip
    Vale a pena ter dados sobre o curso de profundor necessário em
    relação à deflexão dos flaps (do fabricante da aeronave ou de fontes
    da comunidade) antes de definir os valores iniciais da curva de
    compensação. Na falta desses dados, comece com alguns milímetros de
    curso de profundor para a deflexão total dos flaps e refine a partir
    daí.
