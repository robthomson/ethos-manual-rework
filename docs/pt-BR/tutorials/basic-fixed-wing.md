---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Exemplo básico de asa fixa

Um passo a passo completo para um avião com motor + 2 ailerons + 2 flaps +
profundor + leme, um servo por superfície, construído do início ao fim com o
assistente. Conclua primeiro a [Configuração inicial do rádio](initial-radio-setup.md).

## Etapa 1. Confirme as configurações do sistema

Este exemplo usa a ordem de canais padrão **AETR**.

## Etapa 2. Identifique os servos/canais necessários

[Mixagens](../model-setup/mixes.md) é o coração do rádio — até 100
canais de mixagem, normalmente com os números mais baixos atribuídos aos servos
(já que os números de canal correspondem diretamente aos canais do receptor; o
módulo RF interno do X20 suporta até 24 canais de saída). Os canais mais altos
ficam livres para canais virtuais ou canais reais adicionais por meio de vários
módulos RF e SBUS. Nossa aeronave:

| Função | Canais |
|---|---|
| Motor | 1 |
| Ailerons | 2 |
| Flaps | 2 |
| Profundor | 1 |
| Leme | 1 |

(O trem de pouso retrátil é adicionado depois, na [Etapa 10](#step-10-add-a-mix-for-retracts).)

## Etapa 3. Crie um novo modelo

![Criar modelo de avião](../assets/tut-fw-eg-wiz-create-airplane.png)

Em [Seleção de modelo](../model-setup/model-select.md), escolha uma categoria,
toque em **+** e inicie o assistente **Avião**. Escolha **Receptor não
estabilizado** para este exemplo.

![Canais do motor](../assets/tut-fw-eg-wiz-engine.png)
![Canais de aileron/flap](../assets/tut-fw-eg-wiz-ail-flaps.png)

Aceite 1 canal de motor, depois 2 canais de aileron e selecione 2 canais de
flap.

![Tipo de cauda](../assets/tut-fw-eg-wiz-tail.png)
![Canais de profundor/leme](../assets/tut-fw-eg-wiz-ele-rudd.png)

Aceite a **Cauda tradicional** padrão, com 1 canal de profundor e 1 de leme.

![Nome do modelo](../assets/tut-fw-eg-wiz-name.png)
![Receptor](../assets/tut-fw-eg-wiz-rx.png)

Dê um nome a ele (por exemplo, "FWexample" — até 15 caracteres), conclua o
assistente e ele se torna o modelo ativo, criado na categoria Avião.

## Etapa 4. Revise e configure as mixagens

![Visão geral das mixagens](../assets/tut-fw-eg-mixes.png)

O assistente já criou as mixagens de ailerons (canais 1 e 5), profundor,
acelerador, leme e flaps (os flaps mostram `---` — nenhuma fonte atribuída
ainda).

### Ailerons {: #ailerons }

![Mixagem de aileron](../assets/tut-fw-eg-mixes-ail-mix.png)
![Editar mixagem de aileron](../assets/tut-fw-eg-mixes-ail-edit.png)

**Peso/Taxas** — configure as taxas antes de voar qualquer novidade: um curso
moderado (por exemplo, 30%) é adequado para voo esportivo, e 100% completo é
adequado para 3D. Adicione uma taxa de 60% para o interruptor SB no meio e uma
taxa de 30% para SB para baixo — o padrão (SB para cima) permanece em 100%:

![Taxas de peso](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — uma resposta linear pode parecer nervosa em torno do centro; adicione
taxas de Expo (por exemplo, 60%/40%/20% nas mesmas posições de SB) para achatar
a resposta próxima ao centro sem reduzir o curso máximo:

![Taxas de Expo](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Diferencial** — um curso igual de aileron para cima e para baixo gera mais
arrasto no aileron que desce do que no que sobe, guinando o modelo para fora da
curva ("guinada adversa"). Um diferencial positivo (50% é comum) reduz o curso
para baixo em relação ao curso para cima, compensando isso:

![Diferencial de 50%](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Para ajustar o diferencial em voo, pressione e mantenha `ENT` sobre o valor,
escolha **Usar uma fonte** e selecione Pot1:

![Usar uma fonte](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Pot1 selecionado](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Quando estiver satisfeito com o valor obtido em voo, pressione e mantenha
novamente e escolha **Converter em valor** para fixá-lo permanentemente:

![Converter em valor](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim** — é possível desconectar esta mixagem do seu trim associado sem
desativar o próprio trim, liberando-o para outra finalidade:

![Trim de aileron](../assets/tut-fw-eg-mixes-ail-trim.png)

### Profundor e leme

O mesmo padrão de taxa tripla + Expo, aqui no interruptor SC:

![Taxas de Expo do profundor](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Acelerador

![Mixagem do acelerador](../assets/tut-fw-eg-mixes-thr-edit.png)

Deixe a entrada no stick do acelerador — não são necessárias taxas/Expo —, mas
um interruptor de segurança é essencial; um motor a combustão ou elétrico que
parta inesperadamente pode causar ferimentos graves.

**Trim de posição baixa** (motores glow/gasolina) — ajusta a rotação de marcha
lenta independentemente do acelerador máximo:

![Trim de posição baixa](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Com ele ativado, o canal do acelerador fica em −75% com o stick em marcha lenta;
a alavanca de trim do acelerador então ajusta a marcha lenta entre −100% e −50%.

**Corte de acelerador** — uma trava de segurança. Com o interruptor SA para
baixo como condição ativa (mostrada em negrito quando ativa), a saída do
acelerador é mantida em −100% assim que o stick cai abaixo de −85%:

![Corte de acelerador](../assets/tut-fw-eg-mixes-thr-cut.png)

Com o **Sticky** ativado, o acelerador é cortado **no instante** em que SA vai
para baixo, independentemente da posição do stick:

![Corte de acelerador sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

De qualquer forma, quando a condição ativa é liberada, o stick deve ser trazido
de volta abaixo de −85% antes que o acelerador possa aumentar novamente — o que
impede que o motor salte para uma posição de acelerador alto no momento em que o
interruptor de corte é liberado.

**Retenção de acelerador** — um corte de emergência a partir de *qualquer*
posição do stick, levando a saída direto para −100% (ou um valor configurado) no
instante em que sua condição é atendida:

![Retenção de acelerador](../assets/tut-fw-eg-mixes-thr-hold.png)

### Flaps

![Entrada dos flaps](../assets/tut-fw-eg-mixes-flaps-input.png)

Atribua os flaps ao interruptor SE e defina os pesos de ambos os canais de saída
em 100%:

![Pesos dos flaps](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Etapa 5. Faça o bind do receptor

Registre (se for ACCESS) e faça o bind pelo
[Sistema RF](../model-setup/rf-system.md). Antes de prosseguir para as Saídas,
considere desconectar os links dos servos ou reduzir temporariamente o curso dos
servos, para evitar forçar qualquer componente ao definir os limites Mín/Máx.

## Etapa 6. Configure as saídas

![Saídas](../assets/tut-fw-eg-outputs.png)

[Saídas](../model-setup/outputs.md) adapta a lógica do mixer à mecânica real do
modelo.

**Aileron 1** — centralize o servo com **Centro PWM** após otimizar o link
mecânico, depois defina **Mín**/**Máx**. Atribuir temporariamente um
potenciômetro ao Mín (e depois ao Máx, da mesma forma que no exemplo do
diferencial acima) torna esse ajuste mais rápido:

![Editar saída de aileron](../assets/tut-fw-eg-outputs-edit-ail.png)

**Flaps** — os flaps normalmente precisam de uma grande deflexão para baixo para
uma frenagem eficaz; sacrifique parte do curso para cima no link para consegui-la,
de modo que o flap fique meio abaixado com o servo no centro, e depois use
Mín/Máx para definir as posições reais de recolhido e totalmente abaixado. Uma
curva de 5 pontos é uma forma comum de corrigir qualquer descasamento resultante
de acompanhamento entre flap e aileron. Finalize com
**[Balanceamento de canais](../model-setup/outputs.md#balance-channels)** para
sincronizar os ailerons e os flaps esquerdo e direito.

## Etapa 7. Introdução às fases de voo

As [Fases de voo](../model-setup/flight-modes.md) permitem que um modelo tenha
ajustes específicos para cada tarefa — como trocar de marcha. Das 20
disponíveis, este exemplo usa três: **Default**, **Flaps Half** (interruptor SE
no meio) e **Flaps Full** (SE para cima). A primeira fase de voo cuja condição
for verdadeira fica ativa; a fase **Default** não tem nenhuma condição e assume
o controle sempre que nenhuma outra se aplica — por isso ela não tem opção de
seleção de interruptor. Uma transição (fade) de 1 segundo na entrada/saída suaviza
a mudança conforme os flaps são acionados.

## Etapa 8. Configure os trims

Duas maneiras de lidar com a variação do trim de profundor conforme a posição
dos flaps:

**Trims independentes por fase de voo** — a opção mais simples: o trim de
profundor torna-se totalmente independente em cada fase de voo, alternando
automaticamente conforme SE é movido. Como cada fase é ajustada do zero, o
[Trim instantâneo](../model-setup/trims.md#instant-trim) ajuda — ajuste primeiro
o trim para o voo normal, depois pouse e use isso como ponto de partida para as
fases com flaps.

**Trim base com offset** — ajuste o trim uma única vez na fase Default, com a
compensação de profundor de cada fase de flaps aplicada por cima como um offset:

1. Defina o **Passo** do trim como Médio (para um ajuste inicial mais rápido;
   reduza depois para o ajuste fino), o **Modo** como Personalizado e adicione um
   novo comportamento.
2. **Condição ativa**: `FM1(Flaps Half)`, modo **Offset + Default** — o trim de
   Flaps Half passa a ser o trim base mais qualquer offset ajustado enquanto essa
   fase estiver ativa:

   ![Adicionar comportamento](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Repita para `FM2(Flaps Full)`:

   ![Selecionar FM](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Cada fase de flaps pode agora ser ajustada de forma independente, mas alterar
posteriormente o trim base da fase Default (por exemplo, para corrigir a deriva
térmica do servo) desloca automaticamente os trims de ambas as fases de flaps na
mesma medida.

![Seleção de trim personalizado](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Etapa 9. Configure um temporizador para a bateria de voo

Em [Temporizadores](../model-setup/timers.md), edite o Temporizador 1: modo
**Down**, valor inicial de 5 minutos, funcionando sempre que **Acelerador ativo**
for verdadeiro (e não estiver retido em reset). Opcionalmente, atribua uma fonte
de temporização proporcional (por exemplo, o stick do acelerador) para que o
temporizador corra em velocidade real com acelerador máximo e desacelere
conforme o acelerador é reduzido.

## Etapa 10. Adicione uma mixagem para o trem retrátil {: #step-10-add-a-mix-for-retracts }

![Fonte da mixagem do trem retrátil](../assets/tut-fw-eg-retracts-source.png)

Toque em uma mixagem, **Adicionar mixagem** → **Mixagem livre**, dê o nome
"Retracts", defina a condição como Sempre e a fonte como o interruptor SF. A
ação padrão com Peso = 100% está adequada — isso aloca, por exemplo, o canal 8
para o trem retrátil:

![Saída do trem retrátil](../assets/tut-fw-eg-retracts-outputs.png)
