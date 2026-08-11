---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Telemetria

![Sensores descobertos](../assets/model-telemetry-discovered-new-sensors.png)

A telemetria traz informações do modelo de volta ao piloto — qualidade de
enlace (RSSI, VFR), tensões e correntes, e qualquer outra coisa que um
sensor conectado informe (posição GPS, altitude e assim por diante). São
suportados até 100 sensores por modelo; a descoberta e a configuração
acontecem aqui, mas a telemetria é de fato *exibida* como [widgets de
telas](../displays/index.md), configurados separadamente em Configurar
telas.

## Como funciona a telemetria FrSky {: #how-frsky-telemetry-works }

Os sensores da FrSky não usam hub: o **Smart Port (S.Port)** é um
barramento de 3 fios (Gnd, V+, Sinal), encadeado em qualquer ordem na
conexão S.Port dos receptores das séries X/S e posteriores, operando em
half-duplex a 57.600 bps (F.Port e FBUS são mais rápidos).

- **Physical ID** — até 28 nós (incluindo o receptor) compartilham o
  barramento, cada um precisando de um Physical ID exclusivo (00–1B em
  hexadecimal). Os dispositivos FrSky vêm com padrões sensatos (por
  exemplo, Vario = 00, FLVSS = 01, Current = 02, GPS = 03) — se você
  conectar dois dispositivos iguais, o Physical ID do segundo deve ser
  alterado em [Device
  Config](../system-setup/devices.md).
- **Application ID** — independente do Physical ID: um sensor pode
  informar múltiplos valores, cada um com seu próprio Application ID. Um
  Vario tem um Physical ID, mas dois Application IDs (Altitude,
  Velocidade Vertical); um FLVSS tem um Physical ID e um Application ID
  (Tensão). Monitorar duas baterias 6S com dois sensores FLVSS significa
  alterar **ambos** os IDs no segundo — o Physical ID para comunicação
  exclusiva no barramento, e o Application ID para que o receptor consiga
  distinguir Lipo 1 de Lipo 2 (por exemplo, `0300` → `0301`). O 4º dígito
  hexadecimal é o que normalmente se varia, de 0 a F.

  !!! note
      Sensores compartilhando um Application ID mas com Physical IDs
      diferentes só é válido com a [detecção de conflito de
      sensores](../system-setup/alerts.md) desativada — uma configuração
      de propósito específico, não o caso padrão.

Cada valor recebido é tratado como um sensor próprio: valor, Physical/
Application ID, um nome editável, unidade, precisão decimal, um sinalizador
opcional de registro no SD card e seus próprios mín./máx. acumulados. Os
sensores são descobertos automaticamente a cada ligamento, uma vez
configurados, mas precisam ser descobertos **manualmente** na primeira
vez. Depois de descoberto, um sensor pode ser anunciado por voz,
alimentado em [sensores calculados](#calculated-sensors), usado em
[interruptores lógicos](logical-switches.md), [Vars](variables.md) ou
[mixagens](mixes.md), exibido em uma tela de telemetria personalizada, ou
lido diretamente nesta página de configuração sem criar tela alguma.

O **FBUS** (antigo F.Port2) aprimora ainda mais isso, reunindo o controle
SBUS e a telemetria S.Port em uma única linha a 460.800 bps (contra
115.200 do F.Port e 57.600 do S.Port — as três taxas de bits são
mutuamente incompatíveis) e permite que um host converse com vários
acessórios escravos nessa única linha, todos configuráveis sem fio a
partir do rádio.

### Telemetria com múltiplos receptores (ACCESS Trio)

Com até três receptores registrados em [RF
System](rf-system.md#registering-and-binding-a-receiver-access), cada
receptor vinculado pode ser configurado individualmente (pinos de porta,
etc.) via RX1/RX2/RX3. Normalmente há um caminho de telemetria de entrada
por enlace RF — os sistemas Tandem/TD são a exceção, operando 2,4GHz e
900MHz como dois caminhos em um só módulo. A fonte de telemetria ativa
pode mudar durante o voo, dependendo das condições de RF; o sensor **RX**
informa qual receptor está enviando telemetria em tempo real (e o
registra).

A configuração comum: encadeie o barramento de sensores S.Port entre
todos os três receptores, compartilhando uma fonte de alimentação comum,
depois registre/vincule cada receptor e faça a descoberta de sensores
normalmente — a fonte de telemetria alterna automaticamente conforme o RX
ativo muda, e os dados dos sensores S.Port *externos* acompanham de forma
transparente. (Sensores internos do receptor — RSSI, VFR, RxBatt, ADC2, o
próprio RX — não se vinculam dessa forma; são sempre informados para o
receptor que estiver sendo a fonte no momento. A telemetria simultânea
dos três ao mesmo tempo está planejada, mas ainda não está disponível.)

## Sensores de qualidade de enlace

- **RSSI** (Receiver Signal Strength Indicator) — quão forte é a
  transmissão do rádio no receptor. Alarmes padrão: **ACCESS**/**TD**/
  **TW** 35 (baixo) / 32 (crítico), perda de controle em torno de 28;
  **ACCST** 45 / 42, perda de controle em torno de 38. "Telemetria
  perdida" é acionado quando o enlace desaparece por completo — nesse
  ponto **nenhum outro alarme pode soar**, já que o rádio não tem mais
  telemetria para avaliar; trate isso como um sinal para retornar
  imediatamente. (A menos de ~1m de separação, o receptor pode ser
  saturado e produzir ciclos espúrios de alarme Perdido/Recuperado — não
  é uma falha real.) O RSSI aproxima bem o alcance efetivo, mas o VFR é o
  indicador de qualidade de enlace mais confiável.

  ![Sensor RSSI](../assets/model-telemetry-edit-rssi-sensor.png)

  Receptores TD informam um RSSI por banda (2.4G, 900M); receptores TW
  também informam um por banda (2.4FSK, 2.4LoRa, 900M) — ative **Alerta
  de RSSI individual por banda** para obter alertas de voz separados para
  cada uma, em vez de um único alerta combinado:

  ![Alerta de RSSI individual](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — pacotes válidos a cada 100 recebidos; a
  substituição, após o ACCESS 2.1, da prática de incorporar a taxa de
  quadros perdidos ao RSSI. O **aviso de valor baixo** padrão é 50%.

  ![Sensor VFR](../assets/model-telemetry-edit-vfr-sensor.png)

  Receptores TD/TW informam dois fluxos de VFR (um por banda); o **Rx
  VFR** (em receptores TD/TW/AP/AP Plus) em vez disso conta todos os
  quadros válidos, independentemente da banda em que chegaram — é o que
  se deve observar se você acompanha apenas um único valor de VFR.

- **RxBatt** — tensão da bateria do receptor.
- **ADC2** — uma segunda entrada analógica de tensão, em receptores que a
  suportam.
- **SWR** — SWR da antena, ao usar uma antena externa.
- Sensores de atitude/movimento, quando suportados: **R.Angle**,
  **P.Angle**, **AccX/Y/Z**.

Todo sensor numérico também recebe automaticamente sensores de mín./máx.
`<name>-`/`<name>+`, mesmo que não sejam mostrados na lista principal de
sensores.

## Descobrindo sensores {: #discovering-sensors }

![Descobrir novos sensores: ligado](../assets/model-telemetry-discover-new-sensors-on.png)

Com tudo vinculado e energizado, ative **Descobrir novos sensores** — um
ponto piscando (ou um valor em vermelho, se ainda não houver dados) marca
cada sensor conforme ele é encontrado, e a tela é preenchida
automaticamente. Isso precisa ser repetido **por modelo**, e novamente
sempre que um novo sensor for adicionado.

![Descobrir novos sensores: desligado](../assets/model-telemetry-discover-new-sensors-off.png)

- Volte a descoberta para **Off** quando terminar.
- **Excluir tudo** apaga todos os sensores para começar de novo.

  ![Sensores excluídos](../assets/model-telemetry-sensors-deleted.png)

- O **modo competição** reduz a telemetria apenas a RSSI e RxBatt — para
  competições que permitem somente sensores de status de enlace.
  Desativá-lo novamente exige um ciclo de energia antes que os sensores
  possam ser redescobertos.

  ![Confirmação do modo competição](../assets/model-telemetry-comp-only-confirm.png)

- O modo de telemetria por **Bluetooth** emparelha com o aplicativo de
  celular FrSky FreeLink, que pode exibir telemetria ao vivo e também
  configurar dispositivos FrSky, como receptores estabilizados.

  ![Telemetria por Bluetooth](../assets/model-telemetry-bt-option.png)

## Editando um sensor {: #editing-a-sensor }

![Seleção de opção de edição](../assets/model-telemetry-edit-option-select.png)

Toque em um sensor para **Editar**, **Mover**, **Redefinir** ou
**Excluir**. Campos comuns: **Valor** (somente leitura), **ID** (Physical
+ Application ID e o receptor que envia), **Nome**, **Unidade**,
**Decimais**, **Faixa** (limites fixos de escala — relevante
principalmente quando o sensor é usado como fonte de canal), **Gravar
logs**, **Redefinir** (uma fonte que redefine este sensor) e **Atraso do
aviso de sensor perdido** (desativar por completo, ou de 1 a 30s, padrão
10s, para filtrar quedas breves — entenda o risco de definir um valor
muito alto; a mensagem de "sensor perdido" é reproduzida apenas uma vez,
mesmo que muitos sensores caiam ao mesmo tempo; desativado por padrão
para sensores internos do receptor, já que raramente somem).

Alguns sensores adicionam seus próprios campos:

- **ADC2** — **Ratio** e **Offset**, para corrigir a escala.

  ![Edição do sensor ADC2](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — limiares de **valor crítico** e **aviso de valor baixo**.
- **VFR** — **aviso de valor baixo** (padrão 50%).
- **VSpeed** (velocidade vertical do vario) — **Faixa** de até ±100m/s
  (padrão ±10m/s). O comportamento do áudio do vario agora fica na
  [função especial Play Vario](special-functions.md), não aqui.

  ![Edição do sensor VSpeed](../assets/model-telemetry-edit-vspeed-sensor.png)

## Sensores DIY / de terceiros

![Criar sensor DIY](../assets/model-telemetry-diy-sensor-select.png)

**Criar sensor DIY** adiciona manualmente um sensor que não é FrSky:
**detecção automática** (preenche Physical ID, Application ID e Módulo
automaticamente, se possível), ou defina-os manualmente, além de
**decimais/unidade de protocolo** (precisão de entrada, 0–3 decimais, e
sua unidade nativa) e **decimais/unidade de exibição** (independentes dos
do próprio protocolo), junto com os mesmos campos **Faixa**/**Ratio**/
**Offset**/**Gravar logs**/**Redefinir**/**Atraso do aviso de sensor
perdido** de qualquer outro sensor.

![Detecção automática de sensor DIY](../assets/model-telemetry-diy-sensor-auto-detect.png)

## Sensores calculados {: #calculated-sensors }

![Criar sensor calculado](../assets/model-telemetry-calculated-sensor-select.png)

Derive um novo sensor a partir de um ou mais sensores existentes:

- **Consumption** — energia utilizada, integrada a partir de um sensor de
  corrente (por exemplo, a série FAS). Unidade mAh/Ah, faixa de até
  1000Ah.

  ![Sensor de consumo](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Distance** — a partir de uma fonte GPS (mais uma fonte de altitude,
  para distância 3D). Unidades cm/m/km/ft, até 20km.

  ![Sensor de distância](../assets/model-telemetry-calculated-sensor-distance.png)

- **Trip** — distância acumulada entre fixes de GPS sucessivos. Mesmas
  unidades, até 1000km.

  ![Sensor de trip](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — encadeia dois ou mais sensores de tensão Lipo para
  monitorar baterias maiores que 6S (até 67,2V/8S). Selecione cada sensor
  de células do menor para o maior; cada sensor Lipo adicional precisa
  ter seus IDs Physical **e** Application alterados previamente em
  [Device Config](../system-setup/devices.md) (a ferramenta de
  configuração Lipo Voltage lá ajuda), descobertos um por vez, e
  renomeados para que sejam distinguíveis.

  ![Sensor Multi Lipo](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Percent** — redimensiona um sensor para 0–100%, com uma opção
  **Invert** (por exemplo, para mostrar a porcentagem *restante* em vez
  da consumida).

  ![Sensor de porcentagem](../assets/model-telemetry-calculated-sensor-percent.png)

- **Power** — potência em watts a partir de um par de fontes **Current** e
  **Voltage**, até 1.000.000W.

  ![Sensor de potência](../assets/model-telemetry-calculated-sensor-power.png)

- **Custom** — uma fórmula arbitrária encadeada a partir de uma ou mais
  fontes.

Todo sensor calculado também possui **Persistent** (sobrevive ao
desligamento/troca de modelo, sendo recarregado no próximo uso) e um botão
**Redefinir** na própria tela de edição.

### Sensores personalizados

![Sensor personalizado](../assets/model-telemetry-edit-custom-sensor.png)

Começa a partir de uma fonte, e então **Add** encadeia operações
adicionais: **Add(+)**, **Minus(-)**, **Multiply(×)**, **Divide(/)**,
**Min**, **Max**, **Sqrt**. As unidades podem ser escolhidas em uma longa
lista que abrange tensão, corrente, capacidade, potência, distância,
velocidade, tempo, temperatura, porcentagem, ângulos, pressão e mais;
faixa de −1.000.000 a 1.000.000, 0–4 decimais.

![Adicionar uma linha de cálculo](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "Potência de pico"
    Multiplique um sensor de tensão (`VFAS`) por um sensor de corrente
    (`Current`), depois adicione uma etapa **Max** referenciando o valor
    atual do próprio sensor (`MaxPower`) para acompanhar a maior leitura
    observada — 288W nesta execução de exemplo:

    ![Exemplo MaxPower](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "Aritmética com uma constante"
    Fonte definida como `RSSI 2.4G` (lendo 64dB), depois uma ação
    **Subtract** cuja própria fonte recebe um toque longo e à qual se
    aplica **Convert to value**, transformando-a em uma constante editável
    (20) em vez de uma fonte ao vivo — o resultado é um valor estável de
    44dB (64 − 20):

    ![Exemplo de subtração](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![Convert to value](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "O valor interno de uma fonte"
    Toda [fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    tem uma faixa interna de inteiros de ±1024 correspondente à sua faixa
    exibida de ±100% — visível diretamente ao apontar um sensor Custom
    para, digamos, o Acelerador: acelerador máximo lê **+1024**
    internamente, reverso total lê **−1024**.

    ![Valor interno no máximo](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![Valor interno no mínimo](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
