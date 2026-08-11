---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Aviso de capacidade da bateria

Aviso baseado na **capacidade consumida** (mAh) em vez da tensão — uma medida
mais direta de quanto do pacote foi realmente utilizado. Há duas maneiras de
chegar lá, dependendo do hardware instalado.

## Opção A: um ESC da série Neuron

Os ESCs Neuron da FrSky informam o consumo diretamente — não é necessário
nenhum sensor calculado. Configure [Receiver Options → Telemetry
Port](../system-setup/devices.md) para S.Port, conecte o cabo de telemetria do
Neuron e [descubra os
sensores](../model-setup/telemetry.md#discovering-sensors) — o sensor de
interesse é **ESC Consumption**.

1. Adicione um [interruptor lógico](../model-setup/logical-switches.md) sobre
   `ESC Consumption`, verdadeiro acima de (por exemplo) 900mAh — cerca de 60%
   de um pacote dimensionado para pousar com ~30% ainda de reserva.
2. Adicione uma [função especial Play audio](../model-setup/special-functions.md),
   com condição de ativação no novo interruptor e uma etapa **Play value** para
   `ESC Consumption`.

Como segunda linha de defesa, os ESCs Neuron também informam a **ESC Voltage** —
configure um segundo interruptor lógico da mesma forma que em [Aviso de tensão
baixa da bateria](low-battery-warning.md) (abaixo de 3,4V/célula para 4s — por
exemplo, 13,6V para um pacote 4S), com sua própria função Play audio repetindo a
cada 5 segundos.

## Opção B: um sensor de corrente + sensor calculado

Se o ESC não informar o consumo, um sensor de corrente (por exemplo, FrSky
FASxxx) combinado com um [sensor **Consumption**
calculado](../model-setup/telemetry.md#calculated-sensors) faz o mesmo
trabalho.

### 1. Conectar e descobrir

![Sensor de corrente](../assets/how-to-consumption-telemetry-current-sensor.png)

Conecte o cabo S.Port do sensor de corrente e faça a descoberta — ele aparece
como **Current**. Ajuste sua **Range** para corresponder ao sensor (por exemplo,
0–100A para um FAS100):

![Edição do sensor de corrente](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Criar o sensor calculado Consumption

![Criar sensor calculado](../assets/how-to-consumption-create-calc-select.png)
![Sensor de consumo](../assets/how-to-consumption-create-calc-sensor.png)

Em Telemetria, **Create Calculated Sensor** → **Consumption**. Defina as
unidades como `mAh` e a **Range** como a capacidade do pacote (por exemplo,
2800mAh); a **Source** como `Current`.

![Edição do sensor](../assets/how-to-consumption-sensor-edit.png)
![Edição do sensor 2](../assets/how-to-consumption-sensor-edit2.png)

Defina **Reset** para o evento de sistema `!Telemetry Active` — selecione
**Telemetry Active**, pressione longamente `ENT` e escolha **Invert** — assim o
total acumulado é zerado automaticamente quando a telemetria cai (ou seja,
quando o modelo é desligado).

### 3. Anúncios de marcos

![Interruptor lógico delta 200mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Adicione um interruptor lógico usando a função **Δ > X** sobre `Consumption`,
disparando a cada vez que ele subir um passo fixo — por exemplo, a cada 200mAh,
uma fração conveniente de um pacote de 2800mAh.

!!! tip
    Defina **Check interval** como `---` (infinito) para que ele continue
    acumulando indefinidamente em direção ao próximo limite, em vez de zerar
    após uma janela fixa. Atribua a **Min Duration** um valor pequeno diferente
    de zero durante os testes — em 0.0 o disparo é breve demais para ser visto
    na tela.

Adicione uma função Play Audio, com condição de ativação neste interruptor e
uma etapa Play value para `Consumption`:

![Anúncio do delta](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value: consumo](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Aviso de capacidade baixa

![Segundo interruptor lógico](../assets/how-to-consumption-lsw2-play-battlow.png)

Um segundo interruptor lógico dispara uma única vez, ao ultrapassar um limite
rígido de capacidade baixa — por exemplo, 2000mAh de um pacote de 2800mAh —
associado a uma função Play Audio repetindo a cada 10 segundos até que o modelo
seja reiniciado:

![Play value em bateria baixa](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value: consumo em bateria baixa](../assets/how-to-consumption-sf2-play-value-consumption.png)
