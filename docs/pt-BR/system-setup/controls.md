---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Controles

![Sticks](../assets/system-sticks.png)

Chamado de **Sticks** no menu — modo dos sticks e a ordem padrão de
atribuição de canais.

## Modo dos sticks

- **Modo 1** — acelerador e aileron no stick direito, profundor e
  leme no esquerdo.
- **Modo 2** — acelerador e leme no stick esquerdo, aileron e profundor
  no direito.

Por padrão, os sticks recebem os nomes dos modos padronizados pela
indústria, e podem ser renomeados.

## Ordem dos canais

Define a ordem em que as quatro entradas dos sticks são atribuídas aos
canais quando um novo modelo é criado pelos assistentes de
[Seleção de modelo](../model-setup/model-select.md). O padrão é **AETR**.
Quando a aeronave possui mais de uma superfície de um mesmo tipo, elas são
agrupadas, a menos que [Primeiros quatro canais
fixos](#first-four-channels-fixed) esteja ativado — por exemplo, 2 ailerons
resulta em **AAETR**.

![Ordem dos canais do receptor](../assets/system-sticks-rx-order.png)

## Primeiros quatro canais fixos {: #first-four-channels-fixed }

Com esta opção ativada, os primeiros quatro canais nunca são agrupados. Com
a ordem **AETR** e uma aeronave com 2 ailerons, 1 profundor, 1 motor, 1 leme
e 2 flaps, o assistente produz **AETRAFF** (os canais 1–4 permanecem
exatamente A-E-T-R, com o segundo aileron e ambos os flaps acrescentados
depois) em vez de **AAETRFF**. Esta é a configuração que faz o assistente
criar modelos adequados aos receptores estabilizados SRx, que esperam esse
layout fixo.

![Ordem fixa de 4 canais](../assets/system-sticks-4ch-fixed.png)
