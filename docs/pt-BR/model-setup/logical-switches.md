---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Interruptores lógicos

![Menu de interruptores lógicos](../assets/model-lsw-menu.png)

Interruptores lógicos são interruptores *virtuais* programados pelo
usuário — não são controles físicos, mas podem ser usados em qualquer
lugar onde um interruptor físico possa ser usado, como gatilho de
programação. Cada um avalia a condição configurada em relação às suas
entradas (outros interruptores, valores de telemetria, valores de
mixagem, valores de temporizador, canais de giroscópio/trainer e mais)
para se tornar Verdadeiro ou Falso. São suportados até 100; nenhum existe
por padrão. Adicione um com **+**; o rótulo de menu de um interruptor
definido aparece em verde quando Verdadeiro e em vermelho quando Falso.
Toque em um existente para **Editar**/**Mover**/**Copiar-colar**/**Clonar**/**Excluir**.

![Adicionar interruptor lógico](../assets/model-lsw-add.png)

## Função

Toda função admite saída normal ou invertida.

- **A ~ X** — verdadeiro quando a fonte `A` é *aproximadamente* igual
  (dentro de ~10%) a um valor fixo `X`. Geralmente preferível à igualdade
  exata —

  ![A ~ X](../assets/model-lsw-A~X.png)

  — pois, com `A = X`, uma leitura de telemetria que oscila entre, por
  exemplo, 8,5 V e 8,35 V em torno de um alvo de 8,4 V pode simplesmente
  nunca cair exatamente em 8,4 V, e assim o interruptor nunca acionaria.
- **A = X** — verdadeiro somente quando `A` é exatamente igual a `X`.
- **A > X** / **A < X** — verdadeiro quando `A` é maior/menor que `X`.
- **|A| > X** / **|A| < X** — como acima, mas comparando o valor absoluto
  de `A` (o sinal é ignorado).
- **Δ > X** — verdadeiro quando a variação de `A` (delta) ao longo do
  **Intervalo de verificação** atinge ao menos `X`. Um intervalo de `---`
  significa uma janela infinita.

  ![Delta maior que X](../assets/model-lsw-delta-gtX.png)
  ![Delta absoluto maior que X](../assets/model-lsw-delta-AgtX.png)

- **|Δ| > X** — como acima, usando o valor absoluto da variação.
- **Faixa** — verdadeiro quando `A` está dentro de uma faixa especificada.

  ![Faixa](../assets/model-lsw-range.png)

- **AND** — verdadeiro somente se todas as fontes listadas (Valor 1…N)
  forem verdadeiras.

  ![AND](../assets/model-lsw-AND.png)

- **OR** — verdadeiro se ao menos uma das fontes listadas for verdadeira.

  ![OR](../assets/model-lsw-OR.png)

- **XOR** (OU exclusivo) — verdadeiro se *exatamente uma* das fontes
  listadas for verdadeira.

  ![XOR](../assets/model-lsw-XOR.png)

- **Gerador de temporizador** — alterna livremente entre ligado e
  desligado de forma contínua: ligado durante **Duração ativo** e
  desligado durante **Duração inativo**.

  ![Gerador de temporizador](../assets/model-lsw-timer-generator.png)

- **Sticky** — um travamento (flip-flop SR); veja [abaixo](#sticky).
- **Edge** — um pulso momentâneo; veja [abaixo](#edge).

### Sticky

![Sticky](../assets/model-lsw-sticky.png)

Trava em **Verdadeiro** assim que sua condição de **Gatilho ON** é
atendida e permanece Verdadeiro até que o **Gatilho OFF** seja atendido —
condicionado, opcionalmente, à **Condição ativa** (enquanto esta for
Falsa, a saída é mantida em Falso independentemente do restante; o
travamento interno do Sticky continua sendo avaliado em segundo plano e é
repassado à saída novamente tão logo a Condição ativa volte a ser
Verdadeira, sujeito aos atrasos).

Desde o Ethos 1.6.2, ambos os gatilhos aceitam um modificador **Edge**
(pressione longamente `ENT` sobre a condição do gatilho e selecione Edge —
mostrado com um prefixo `†`), permitindo um controle muito mais refinado:

![Sticky com edge](../assets/model-lsw-sticky-with-edge.png)
![Seleção da opção Edge](../assets/model-lsw-sticky-edge-select.png)

- **Gatilho ON `SA` (sem atraso)** — trava em Verdadeiro no instante em
  que SA vai para o nível alto.
- **Gatilho ON `SA` (atraso = 1s)** — trava em Verdadeiro 1s depois de SA
  ir para o nível alto, *desde que* SA continue em nível alto ao final
  desse segundo.
- **Gatilho ON `†SA` (atraso = 1s)** — trava em Verdadeiro→Falso 1s depois
  de SA ir para o nível alto, **independentemente** de SA ainda estar em
  nível alto nesse momento (a borda já ocorreu; o atraso apenas temporiza
  o resultado).

O Gatilho OFF se comporta da mesma maneira, no sentido inverso. Os atrasos
se aplicam **depois** da Condição ativa — portanto, uma mudança na
Condição ativa reinicia a contagem do atraso antes que o valor travado
chegue novamente à saída. Levar ambos os gatilhos de Falso→Verdadeiro
simultaneamente **inverte** a saída do Sticky uma vez. Veja também
[Parâmetros compartilhados](#shared-parameters) abaixo.

### Edge

![Edge](../assets/model-lsw-edge.png)

Um pulso momentâneo: Verdadeiro durante a **Duração**, uma vez satisfeita
sua condição de gatilho. **Durante** é um par `[t1:t2]` que controla
exatamente quando:

- **Borda de subida, Durante = 0,0s** — dispara no instante em que o
  Gatilho ON vai de Falso→Verdadeiro.

  ![Borda de subida](../assets/model-lsw-edge-rising-edge.png)
  ![Durante = 0](../assets/model-lsw-edge-during-eq0.png)

- **Borda de subida, Durante ≥ 0,0s (por exemplo, 5,0s)** — dispara 5s
  depois de o Gatilho ON se tornar Verdadeiro, ignorando quaisquer
  "picos" mais curtos dentro dessa janela de 5s.

  ![Durante > 0, borda de subida](../assets/model-lsw-edge-during-gt0-rising-edge.png)
  ![Durante > 0](../assets/model-lsw-edge-during-gt0.png)

- **Borda de descida, Durante = 0,0s** — dispara no instante em que o
  Gatilho ON vai de Verdadeiro→Falso.
- **Borda de descida, Durante ≥ 0,0s (por exemplo, 3,0s)** — dispara na
  transição Verdadeiro→Falso, mas apenas se antes tiver permanecido
  Verdadeiro por ao menos 3s.
- **Pulso (t1 e t2 ambos definidos)** — dispara somente se o Gatilho ON
  fizer Falso→Verdadeiro→Falso dentro dessa janela (por exemplo, entre 2s
  e 5s depois).

## Parâmetros compartilhados {: #shared-parameters }

![Parâmetros comuns](../assets/model-lsw-common-parameters.png)

- **Condição ativa** — condiciona a saída do interruptor da mesma forma
  que no Sticky, acima. Opções: Sempre ligado, posições de
  interruptor/interruptor de função/interruptor lógico/trim, Telemetria,
  Fases de voo ou um evento de sistema (Retenção de acelerador, Corte de
  acelerador, Acelerador ativo, Telemetria ativa, RSSI baixo, Trainer
  ativo, Reset de voo).
- **Atraso antes de ativar** / **Atraso antes de desativar** — por quanto
  tempo a condição deve permanecer Verdadeira (ou Falsa) antes de a saída
  acompanhá-la, até 60s. Não se aplica ao Gerador de temporizador nem ao
  Edge. (Veja [Guia prático: Aviso de capacidade da
  bateria](../how-to/battery-capacity-warning.md) para um atraso usado
  para filtrar uma queda de tensão.)
- **Confirmação antes de ativar** / **antes de desativar** — solicita
  confirmação do usuário antes de o estado efetivamente mudar (com opção
  de Cancelar, para casos em que o disparo é frequente demais para ser
  útil) — útil para condicionar algo arriscado, como confirmar antes de
  desligar remotamente um veículo terrestre.

  ![Confirmar verdadeiro](../assets/model-lsw-confirm-lsw-true.png)
  ![Confirmar falso](../assets/model-lsw-confirm-lsw-false.png)

- **Duração mínima** — uma vez Verdadeiro, permanece Verdadeiro por ao
  menos esse tempo. Deixada em `---`, a saída pode ficar Verdadeira por
  apenas um ciclo do mixer — breve demais até para ver a linha ficar em
  negrito na interface.
- **Duração máxima** — uma vez Verdadeiro, retorna automaticamente a
  Falso depois desse tempo, mesmo que a condição continue satisfeita.
  Ambas as durações vão até 60s.
- **Comentário** — texto livre, exibido em qualquer lugar em que este
  interruptor seja adicionado a um widget de valor, para documentar sua
  finalidade.

## Uso com telemetria

Um evento de sistema **Telemetria ativa** (ou um interruptor cuja fonte
seja um sensor de telemetria, ativo apenas enquanto esse sensor reporta
dados) cobre condições do tipo "a telemetria está sendo recebida neste
momento".

!!! warning
    Uma [mixagem](mixes.md) condicionada por um interruptor lógico
    baseado em telemetria precisa de uma **segunda** ação de mixagem
    usando o mesmo interruptor **invertido**, para que a mixagem ainda
    tenha um valor válido quando a telemetria for perdida — lembre-se de
    que uma mixagem inativa produz o neutro (0% / 1500µs, ou **meio
    acelerador** em um canal de acelerador). Como alternativa, use uma
    ação **Offset**, que já possui valores ativo/inativo separados
    embutidos — por exemplo, a fonte **0** (o valor especial) com o offset
    ajustado para que a mixagem leia +100% enquanto `LS3` estiver ativo e
    −100% enquanto estiver inativo cobre ambos os casos em uma única ação.

## Comparação de fontes

Normalmente uma fonte é comparada a um valor fixo, mas duas fontes do
*mesmo* tipo podem ser comparadas diretamente entre si — por exemplo,
dois temporizadores, duas tensões ou dois sensores de RPM.

## Ignorar entrada de trainer do slave

![Ignorar entrada de trainer](../assets/model-lsw-ignore-trainer-input.png)

As [opções](../getting-started/user-interface-and-navigation.md#choosing-a-source)
de uma fonte podem excluir a entrada de trainer proveniente de um rádio
de aluno (slave) conectado — tipicamente usado em um interruptor lógico
que monitora o movimento do stick do próprio **mestre** (por exemplo,
para intervir imediatamente se algo der errado), sem que as entradas do
aluno também o acionem. Comumente combinado com um interruptor de trainer
que condiciona a Condição ativa do próprio mestre.
