---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Aviso de Tensão Baixa de Bateria

Monitorar a tensão do pack de voo **sob carga** e alertar abaixo de um
limite é uma abordagem mais confiável do que depender de um temporizador
fixo — um sensor como o FrSky FLVSS torna isso simples.

## 1. Conecte e descubra o sensor

![Sensor de telemetria LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Defina [Opções do receptor → Porta de
telemetria](../system-setup/devices.md) como **S.Port**, conecte o FLVSS ao
receptor por meio de um cabo S.Port e então ative **Descobrir novos sensores** em
[Telemetria](../model-setup/telemetry.md) — o sensor LiPo aparece
junto aos outros já descobertos.

## 2. Adicione um interruptor lógico

![Interruptor lógico de bateria baixa](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Adicione um novo [interruptor lógico](../model-setup/logical-switches.md) com o
sensor Lipo como fonte. Pressione e mantenha `ENT` sobre o sensor destacado para
escolher qual de seus valores utilizar:

![Selecionar célula mais baixa](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Tensão mínima do pack / Tensão máxima do pack
- **Tensão da célula mais baixa** / Tensão da célula mais alta
- Contagem de células
- Tensões individuais das células (selecionáveis apenas enquanto o sensor estiver
  efetivamente conectado a um receptor vinculado com uma LiPo ligada)

Selecione **Lowest** (tensão de célula) — o valor que importa para a
proteção do tipo LVC.

![Célula mais baixa selecionada](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Defina o valor de comparação em torno de **3,4 V** e o **Atraso antes de ativar**
em **4 segundos** — o interruptor torna-se verdadeiro quando a célula mais baixa
registrar menos de 3,4 V por célula de forma contínua por 4 s ou mais. (3,4 V *sob carga*
normalmente recupera para cerca de 3,7 V quando a carga é removida, portanto esse limite
reflete uma queda real, e não apenas ruído momentâneo.)

![Interruptor lógico concluído](../assets/how-to-low-batt-lsw-summary.png)

## 3. Adicione uma função especial

![Função especial: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Adicione uma [função especial Reproduzir áudio](../model-setup/special-functions.md),
com a **Condição ativa** definida para o interruptor lógico `BattLow`, escolha uma voz
e, em **Sequência**, adicione uma etapa **Reproduzir valor** para a tensão total
da LiPo:

![Reproduzir valor: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Resumo da sequência](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Com **Repetir** definido em 10 segundos, a tensão da LiPo é anunciada a cada 10 s
enquanto a célula mais baixa permanecer abaixo do limite de 3,4 V/4 s.
