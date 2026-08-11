---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Trims

![Trims](../assets/model-trims.png)

Configura a faixa de trim, o tamanho do passo e o comportamento de cada
stick, além do trim cruzado e do trim instantâneo. O **X20 Pro/R/RS** e o
**X18** acrescentam dois interruptores de trim extras, **T5**/**T6**,
úteis para ajustes em voo além dos quatro sticks principais:

![Trims T5/T6](../assets/model-trims-pro-t5-t6.png)

Cada stick possui seu próprio conjunto independente de configurações de
trim.

## Configurações de trim {: #trim-settings }

- **Faixa** — padrão de ±25%, ajustável até o curso total do stick de
  ±100%. Na tela principal, um trim com a faixa padrão indica de −100 a
  100; um trim de faixa total (100%) indica de −400 a 400 (4× a faixa
  normal).

  !!! warning
      Ampliar a faixa significa que manter uma tecla de trim pressionada
      por tempo demasiado pode adicionar trim suficiente para tornar o
      modelo impossível de pilotar.

- **Passo** — granularidade do interruptor de trim: **Extrafino**,
  **Fino**, **Médio**, **Grosso**, **Exponencial** (fino próximo ao
  centro, grosso mais afastado) ou **Personalizado** (uma porcentagem
  específica por clique).

  ![Opções de passo](../assets/model-trims-step-options.png)

  | Passo | µs por clique (faixa de 25%) |
  |---|---|
  | Extrafino | 0,5 |
  | Fino | 1 |
  | Médio | 2 |
  | Grosso | 4 |
  | Exponencial | 0,3–16 |

  Personalizado, com faixa de 25%: passo de 1% = 1 µs/clique, passo de
  100% = 128 µs/clique. Com faixa de 100%: passo de 1% = 5 µs/clique,
  passo de 100% = 512 µs/clique.

## Modo

![Modo do trim do profundor](../assets/model-trims-mode-elevator.png)

Por padrão, um trim está sempre ativo, mas o **Modo** altera esse
comportamento. Trocar de modo redefine o trim para 0.

- **OFF** — desativa o trim por completo.

  ![Modo: off](../assets/model-trims-mode-option-off.png)

  Útil, por exemplo, em um modelo elétrico que não necessita de trim de
  acelerador — o controle de trim liberado pode então ser
  [reaproveitado para ajustar uma Var](variables.md).

- **Easy** — um único valor de trim compartilhado por todas as fases de
  voo. A escolha usual para aileron e leme, já que estes raramente
  precisam variar conforme a fase de voo.

  ![Modo: easy](../assets/model-trims-mode-option-easy.png)

- **Independente por fase de voo** — o trim afeta apenas a fase de voo
  ativa. A escolha usual para o trim do profundor, pois o trim do
  profundor normalmente precisa ser diferente em cada fase de voo (por
  exemplo, mudanças na curvatura da asa) — na verdade, essa é
  frequentemente a principal razão para configurar fases de voo.

  ![Modo: independente por fase de voo](../assets/model-trims-mode-option-fm.png)

- **Personalizado** — comportamento totalmente personalizado, construído
  a partir de **comportamentos** que você mesmo adiciona.

### Comportamentos de trim personalizados

![Adicionar um comportamento](../assets/model-trims-mode-elevator-add-behaviour.png)
![Opções de comportamento](../assets/model-trims-mode-elevator-edit-behaviour.png)

Cada linha de comportamento possui uma condição e uma das opções a seguir:

- **Unplugged** — desativa o trim seletivamente sob essa condição (em vez
  de desligá-lo por completo com Modo = OFF).

  ![Unplugged](../assets/model-trims-mode-elevator-edit-behaviour-unplugged.png)
  ![Condição de unplugged](../assets/model-trims-mode-unplugged-select.png)

- **Normal** (padrão) — comportamento de trim comum.
- **Igual (a outro trim)** — este trim acompanha exatamente o valor de
  trim de outra condição.

  ![Igual](../assets/model-trims-mode-elevator-edit-behaviour-equal.png)

- **Deslocamento + (outro trim)** — este trim é somado ao valor de trim
  de outra condição.

  ![Deslocamento](../assets/model-trims-mode-elevator-edit-behaviour-offset.png)

**Exemplo prático** — um planador com um trim de profundor base em
**Cruise** e trims dependentes para **Speed** e **Thermal**:

![Selecionar FM5 Speed](../assets/model-trims-mode-elevator-custom-select.png)
![Selecionar FM4 Thermal](../assets/model-trims-mode-elevator-custom-select-2.png)

1. Ajuste o trim para voo nivelado no modo padrão (Cruise).
2. Adicione um comportamento: **Deslocamento + Default**, condição
   `FM5(Speed)`. Agora qualquer ajuste de trim feito no modo Speed é
   salvo como um deslocamento sobre o valor base de Cruise — separado,
   mas ainda dependente dele.

   ![Deslocamento para Speed](../assets/model-trims-mode-elevator-custom-speed.png)

3. Adicione um segundo comportamento: **Deslocamento + Default**,
   condição `FM4(Thermal)`, da mesma forma. (Depois que o primeiro
   comportamento existe, a caixa de diálogo também oferece as opções
   `Equal FM5(Speed)` e `Offset + FM5(Thermal)`, pois agora ela também
   pode referenciar esse comportamento.)

   ![Deslocamento para Speed e Thermal](../assets/model-trims-mode-elevator-custom-speed-thermal.png)

Com essa configuração, ajustar posteriormente o trim base de Cruise
(digamos, após uma mudança de CG) desloca automaticamente os trims de
Speed e Thermal na mesma medida, já que eles são deslocamentos sobre ele,
e não valores independentes.

- **Áudio** — desativa o anúncio padrão de trim para um trim
  reaproveitado, caso não faça mais sentido ouvi-lo.

## Trims adicionais

![Adicionar trim extra](../assets/model-trims-add-trim-select.png)
![Configurações do trim extra](../assets/model-trims-add-trim-edit.png)

**Adicionar um trim extra** cria um trim além dos quatro sticks padrão (e
de T5/T6): **Nome**, fontes de **Subida**/**Descida** para acioná-lo, além
das mesmas opções de **Faixa**, **Passo**, **Modo** e **Áudio** descritas
acima.

## Trim cruzado

![Trim cruzado](../assets/model-trims-cross.png)
![Edição do trim cruzado](../assets/model-trims-cross-edit.png)

Define qual interruptor de trim efetivamente ajusta cada stick — ou seja,
permite que o trim de um stick seja acionado por um controle físico de
trim diferente do habitual. (T5/T6 estão disponíveis somente no X20 Pro e
no X18.)

## Trim instantâneo {: #instant-trim }

![Trim instantâneo](../assets/model-trims-instant-trim.png)

Enquanto ativo, adiciona as posições atuais dos sticks aos trims padrão
(e cruzados) correspondentes. É melhor atribuí-lo a um interruptor
alcançável sem soltar os sticks — acione-o durante voo reto e nivelado
para definir os trims instantaneamente, em vez de clicar repetidamente em
uma tecla de trim quando os trims estão muito desajustados. Desative-o
novamente após o voo de ajuste, para evitar alterar os trims
acidentalmente mais tarde.

!!! note
    O trim instantâneo só está ativo enquanto uma das telas principais
    está sendo exibida.

## Mover trims para subtrims

![Mover trims para subtrims](../assets/model-trims-move-trims-to-subtrims.png)

Após ajustar o trim para voo nivelado, transfere o valor de trim de um
canal (por exemplo, do profundor) para a configuração de
[Subtrim](outputs.md) correspondente e redefine o trim na tela para zero
— uma forma limpa de confirmar depois que os trims de voo não sofreram
desvios.

Com fases de voo envolvidas, um canal pode ter mais de um valor de trim
relevante, enquanto o Subtrim em Saídas é uma única configuração global
aplicada a todas as fases de voo. Esta função leva isso em conta: ela
pega o trim da fase de voo **atualmente selecionada**, transfere-o para o
Subtrim, redefine esse trim e ajusta o trim de todas as *outras* fases de
voo no mesmo canal para compensar — de modo que a posição real da
superfície em cada fase de voo permaneça inalterada no conjunto.

!!! tip
    Execute isso sempre a partir da mesma fase de voo "base" (por
    exemplo, Cruise em um planador) para manter a consistência — desde
    que você faça assim, pode repetir a operação com segurança.

Valores elevados de trim ou de subtrim criam cursos muito assimétricos —
é melhor corrigir a causa raiz mecanicamente. Procure manter os
tirantes/varões a 90° com as superfícies neutras (com exceção dos flaps,
em que se troca parte do curso para cima por mais curso para baixo) e
depois use o **centro PWM** para ajustar com precisão exatamente 90°,
quando o acionamento já estiver próximo disso.
