---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Temporizadores

![Temporizadores](../assets/model-timers.png)

Oito temporizadores totalmente programáveis, cada um contando de forma
crescente ou decrescente. Adicione um com o **+** ao lado dos títulos das
colunas, ou pela opção **Adicionar** abaixo. Ao tocar em um temporizador,
abrem-se as opções de reset/editar/adicionar/mover/copiar-colar.

![Edição do temporizador](../assets/model-timer1-edit.png)

## Campos comuns (contagem decrescente e crescente)

- **Valor** — a leitura atual do temporizador.
- **Nome** — editável.
- **Modo** — **Up** (crescente) ou **Down** (decrescente).
- **Valor inicial** (somente contagem decrescente) — o valor a partir do
  qual a contagem regressiva é feita.
- **Valor de alarme** (somente contagem crescente) — o valor no qual o
  temporizador é considerado esgotado; ele continua contando além desse
  ponto, mas é exibido em vermelho nos widgets de temporizador.
- **Condição de início** — inicia o temporizador. Se a **Condição de
  parada** for mantida no padrão, a condição de início controla sozinha o
  início *e* a parada. Caso contrário, o temporizador inicia na primeira
  vez que a condição de início se torna verdadeira e continua contando a
  partir daí.
- **Condição de parada** — se não for mantida no padrão, controla o
  temporizador uma vez em funcionamento: parado enquanto verdadeira, em
  funcionamento enquanto falsa. No exemplo abaixo, um temporizador inicia
  quando `ThrottleActive` se torna verdadeiro e para quando a telemetria
  deixa de estar ativa:

  ![Condição de parada](../assets/model-timer1-edit-stop.png)

- **Fonte de temporização proporcional** — `---` conta em tempo real.
  Qualquer outra fonte (por exemplo, o stick de acelerador ou o canal de
  acelerador) altera a velocidade do temporizador: em −100% o temporizador
  fica parado, em +100% ele funciona em velocidade de tempo real, e a
  escala é proporcional entre esses extremos.
- **Reset** — um interruptor, interruptor de função, interruptor lógico ou
  posição de trim que zera o temporizador; ele permanece zerado enquanto a
  condição for verdadeira.
- **Persistente** — mantém o valor do temporizador após o desligamento ou
  a troca de modelo, recarregando-o na próxima vez que o modelo for
  utilizado.
- **Voz** — qual [pacote de voz](../system-setup/general.md#audio-settings)
  anuncia este temporizador.

## Ações de áudio

![Adicionar ação de áudio](../assets/model-timer1-add-action.png)
![Tipo de ação](../assets/model-timer1-action-type-select.png)
![Ação de contagem regressiva](../assets/model-timer1-action-countdown.png)

Configuração de alertas totalmente flexível, individual para cada
temporizador. Cada ação tem um tipo — **Countdown** (contagem regressiva
falada), **Beep countdown** (bipes em vez de voz), **Play file**
(reproduzir arquivo) ou **Play value** (reproduzir valor) — além de:

- **Início** — o valor a partir do qual a contagem regressiva desta ação
  começa.
- **Passo** — intervalo entre os anúncios, até 10 minutos (600 s).
- **Haptic** — acompanha o anúncio com vibração.

Um conjunto típico de três ações:

![Resumo das ações](../assets/model-timer1-actions-summary.png)
![Ações do temporizador 2](../assets/model-timer2-actions-summary.png)

1. Contagem regressiva falada a partir de 2:00 restantes, a cada 30 s, com
   vibração.
2. Contagem regressiva com bipes a partir de 0:10 restantes, a cada 1 s,
   com vibração.
3. Um arquivo personalizado (por exemplo, `timer-1-elapsed`) reproduzido ao
   esgotar, com vibração.

Adicione mais ações com **Adicionar**; a lista é executada em ordem de
prioridade, com a **maior prioridade por último**.

Veja também o [widget de tela Timer Log](../displays/index.md#widget-types)
para obter um registro contínuo das contagens anteriores.

![Widget de temporizador](../assets/model-timers-widget.png)
