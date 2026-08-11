---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Retomada Instantânea para a Função Trainer

Um aprimoramento útil para a função [Trainer](../model-setup/trainer.md):
em vez de depender apenas de um interruptor, o instrutor pode retomar o
controle instantaneamente apenas movendo o stick de aileron ou profundor —
sem precisar localizar o interruptor de trainer primeiro caso algo dê
errado.

O interruptor de trainer continua iniciando a sessão; um [interruptor
lógico Sticky](../model-setup/logical-switches.md#sticky) comanda a própria
função Trainer, sendo cancelado tanto pelo desligamento do interruptor
**quanto** pela detecção do movimento do stick do instrutor.

![Trainer ativo](../assets/trainer-take-back-trainer-active.png)

## 1. Interruptor lógico de detecção de aileron

![Detecção de entrada de aileron](../assets/trainer-take-back-ailinput.png)

Um interruptor lógico usando **|A| > X** no stick de aileron, verdadeiro
quando ele se move mais de 10% fora do centro em qualquer direção.
Pressione e mantenha a fonte de aileron e selecione **Ignore trainer
input**, para que o movimento de aileron do *aluno* (chegando pelo enlace
de trainer) não o acione também:

![Ignorar entrada do trainer](../assets/trainer-take-back-ailinput-ignore.png)

## 2. Interruptor lógico de detecção de profundor

![Detecção de entrada de profundor](../assets/trainer-take-back-eleinput.png)

O mesmo padrão, aplicado ao stick de profundor.

## 3. Interruptor lógico de cancelamento

Um interruptor lógico **OR**, verdadeiro quando o interruptor de detecção
de aileron ou o de detecção de profundor for verdadeiro, **ou** quando o
interruptor de trainer (por exemplo, SD) não estiver para baixo — isto é,
qualquer uma das condições "o instrutor moveu um stick" ou "o interruptor
de trainer foi desligado" encerra a sessão.

## 4. Interruptor lógico Sticky de habilitação do trainer

![Desabilitar trainer](../assets/trainer-take-back-disable-trainer.png)

Um interruptor lógico **Sticky**: o **Trigger ON** é o interruptor de
trainer (SD para baixo) e o **Trigger OFF** é o interruptor de
cancelamento do Passo 3. Use esse interruptor Sticky — chame-o de
`TrainerActive` — como a condição de ativação da própria função Trainer,
em vez do interruptor direto.

## 5. Retorno sonoro

Adicione [funções especiais Play Audio](../model-setup/special-functions.md)
anunciando quando `TrainerActive` se tornar verdadeiro e quando ele for
desativado, de modo que ambos os pilotos recebam uma indicação sonora
clara do momento exato em que o controle muda de mãos.
