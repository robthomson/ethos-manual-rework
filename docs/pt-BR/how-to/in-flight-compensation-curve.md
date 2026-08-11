---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Curva de compensação ajustável em voo

## Por quê

Acionar os flaps altera o perfil (camber) da asa — aeronaves de asa alta
tendem a "balonar" para cima, aeronaves de asa baixa tendem a afundar —
exigindo uma correção de profundor que não é linear em relação à deflexão
dos flaps, ou seja, uma curva em vez de um deslocamento fixo. Este passo a
passo usa [Vars](../model-setup/variables.md) para tornar os pontos de uma
curva de compensação ajustáveis **em voo**, por meio de um trim do
acelerador reaproveitado, condicionado ao ponto da curva mais próximo da
posição atual do stick de flaps — dando continuidade à etapa de compensação
de profundor do [Guia prático: Mixagem
Butterfly](butterfly-mixer.md).

## 1. Escolha o tipo de curva

Uma [curva personalizada](../model-setup/curves.md) de 5 pontos é
suficiente para uma compensação suave sem complexidade excessiva. O ponto 5
(o mais à direita, stick de flaps totalmente para cima / sem flaps) fica
sempre fixo em zero — não é necessária compensação quando nenhum flap está
acionado. Os outros 4 pontos são tornados ajustáveis por meio de Vars. Como
o stick de flaps frequentemente ficará entre dois pontos definidos, os dois
pontos de cada lado dele precisam ser ajustáveis em conjunto nessa zona de
sobreposição.

## 2. Calcule as faixas sobrepostas

Faixas ponto a ponto (adaptadas, com permissão, do "Crow-aware adaptive
elevator trim" de Mike Shellim para OpenTX em rc-soar.com — levemente
estendidas para que a faixa do Pt2 alcance até +100%, pelo motivo
explicado na [Etapa 6](#6-apply-the-curve)):

| Faixa do stick de flaps | Ponto(s) ativo(s) |
|---|---|
| +100% a +45% | Somente Pt2 |
| +45% a +20% | Pt2 e Pt3 |
| +20% a −20% | Somente Pt3 |
| −20% a −45% | Pt3 e Pt4 |
| −45% a −90% | Somente Pt4 |
| −90% a −100% | Somente Pt5 |

## 3. Configure os interruptores lógicos

![Interruptores lógicos dos pontos adaptativos](../assets/how-in-flight-comp-lsws.png)

Quatro [interruptores lógicos](../model-setup/logical-switches.md), cada um
usando **Range** no stick de flaps (acelerador), ativos enquanto o stick
estiver na zona do respectivo ponto:

- `AdaptivePt2` — faixa de 20% a 100% (estendida até 100%
  especificamente para que o Pt2 possa ser ajustado mesmo sem flaps
  acionados — veja a Etapa 6).

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` — faixa de −45% a 45%.

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` — faixa de −90% a −20%.

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` — faixa de −100% a −90%.

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. Defina as Vars de ajuste

![Visão geral das Vars](../assets/how-in-flight-comp-vars.png)

Quatro [Vars](../model-setup/variables.md), `VAdjPt2`–`VAdjPt5`, cada uma
com faixa de 0–50% (amplie se necessário) e uma ação de **trim do
acelerador reaproveitado** — tamanho de passo 1,0%, condição de ativação
igual ao interruptor lógico correspondente:

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![Ação da VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![Ação da VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![Ação da VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![Ação da VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5-2.png)

Como apenas um interruptor lógico (no máximo dois, nas zonas de
sobreposição) fica ativo por vez, o mesmo trim físico ajusta com segurança
Vars diferentes conforme a posição dos flaps.

## 5. Defina a curva de compensação

![Curva de compensação](../assets/how-in-flight-comp-var-comp-curve.png)
![Pontos da curva de compensação](../assets/how-in-flight-comp-var-comp-curve-pts.png)

Uma nova curva personalizada de 5 pontos (por exemplo, "EleComp") com
**Smooth** habilitado. Pressione e mantenha `ENT` nos pontos 1–4 e use
**Use a source** para atribuir `VAdjPt5`…`VAdjPt2`, respectivamente (o
ponto 5 permanece fixo em 0, conforme a Etapa 1).

## 6. Aplique a curva {: #6-apply-the-curve }

Use essa curva exatamente onde o [Guia prático: Mixagem
Butterfly](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix)
associa sua curva EleComp à mixagem de compensação do profundor.

Sempre que possível, parta de dados reais (orientações do fabricante,
publicações da comunidade) sobre quanto curso de profundor uma determinada
deflexão de flaps exige; caso contrário, alguns milímetros de compensação
com flaps totais é um ponto de partida razoável.

!!! tip "Abordagem de ajuste"
    Comece com pequenas quantidades de flap e pequenos ajustes de trim.
    O `AdaptivePt2` pode ser ajustado **sem nenhum flap acionado** —
    aplique um pouco de flap, retire-o novamente e acrescente um pouco de
    compensação por vez, em vez de lutar contra um modelo que baloneia ou
    afunda enquanto tenta trimar sob pressão. Reaplique um pouco de flap
    para verificar e ajuste novamente conforme necessário. Quando o Pt2
    estiver satisfatório, passe para o próximo ponto, em torno do meio do
    curso do stick — se o Pt2 exigiu uma grande alteração de trim, vale a
    pena pousar e definir os pontos restantes de modo que cada um seja
    ligeiramente maior que o anterior, em vez de adivinhar às cegas.
