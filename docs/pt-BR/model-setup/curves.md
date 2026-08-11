---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Curvas

![Tipos de curva](../assets/model-curves-type.png)

Curvas de resposta reutilizáveis para [Mixagens](mixes.md#anatomy-of-a-mix) ou
[Saídas](outputs.md#editing-a-channel) — o Expo integrado está disponível
diretamente em ambos, mas qualquer coisa mais elaborada é definida aqui (ou via
**Adicionar curva**, acessível diretamente de qualquer uma das telas de edição). Até 50
curvas estão disponíveis; nenhuma existe por padrão (o Expo está sempre integrado,
independentemente disso). Adicione uma com **+**; toque em uma curva existente para
**Editar**/**Mover**/**Copiar-colar**/**Clonar**/**Excluir**.

![Adicionar curva](../assets/model-curves-add.png)

## Tipos de curva

- **Expo** — valor padrão 40; valores positivos suavizam a resposta em torno do
  centro, negativos a tornam mais agressiva. Suavizar em torno do meio-curso do stick
  ajuda a evitar comandos excessivos, especialmente para pilotos menos experientes.

  ![Expo](../assets/model-curves-expo.png)

- **Function** — um pequeno conjunto de formas matemáticas fixas:

  ![Tipos de função](../assets/model-curves-fn-types.png)

  - **x > 0** — repassa a fonte sem alteração enquanto ela é positiva;
    envia 0 enquanto é negativa.

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** — o espelho: repassa enquanto negativa, 0 enquanto
    positiva.

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** — repassa a fonte como seu valor absoluto (sempre
    positivo).

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** — envia 100% enquanto a fonte é positiva, 0 enquanto
    negativa (uma chave rígida, não um repasse).

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** — envia −100% enquanto negativa, 0 enquanto positiva.

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** — envia −100% enquanto negativa, +100% enquanto positiva.

    ![|f|](../assets/model-curves-fn-barf.png)

  Todo tipo de curva — inclusive Function — também possui um **Offset**, que a
  desloca para cima ou para baixo no eixo Y (precisão de uma casa decimal, igual aos
  valores de Y em geral):

  ![Offset da função](../assets/model-curves-fn-xgt0-offset.png)

- **Custom** — uma curva baseada em pontos, 5 pontos por padrão, até 21.

  ![Curva personalizada de 5 pontos](../assets/model-curves-custom5.png)

  - **Smooth** — traça uma curva suave passando por todos os pontos, em vez de
    segmentos retos entre eles.

    ![Curva suavizada](../assets/model-curves-custom5-2-smooth.png)

  - **Easy mode** — **On** restringe a edição apenas às coordenadas Y
    igualmente espaçadas (X é fixo); **Off** permite editar tanto X quanto Y
    em cada ponto, exceto as extremidades −100%/+100%, que ficam travadas, pois
    a curva deve sempre cobrir toda a faixa do sinal.

    ![Easy mode desativado](../assets/model-curves-custom-easy-off.png)

  **Controles do editor** (mesmo padrão do [editor de curva de balanceamento das
  Saídas](outputs.md#balance-channels)):

  - **Fonte** — por padrão, a(s) própria(s) fonte(s) de mixagem da curva, ou **Auto
    analog input** para capturar o primeiro stick/slider/potenciômetro movido.
  - Ajuste com atração ao ponto mais próximo pelo encoder rotativo, e uma opção **Lock**
    para congelar as entradas enquanto se observa o movimento resultante da superfície
    de comando.
  - Um cursor ao vivo mostra o valor de entrada atual que aciona a curva, para
    ajudar a alinhá-lo com um ponto antes de ajustar.

## Acionando uma curva a partir de uma Var

Tanto o **Offset** de uma curva Function quanto um ponto individual de uma curva
**Custom** podem ser acionados por uma [Var](variables.md) em vez de um valor fixo —
e essa Var pode, por sua vez, ser ajustada em voo por meio de um trim reaproveitado:

![Offset da função a partir de uma Var](../assets/model-curves-fn-offset-var.png)
![Ponto de curva personalizada a partir de uma Var](../assets/model-curves-custom-with-var.png)

Consulte [Variáveis](variables.md) e [Guia prático: Curva de compensação ajustável
em voo](../how-to/in-flight-compensation-curve.md) para um exemplo completo
e detalhado desse padrão.
