---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Configurar um sistema FBUS

O [FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (antigo
F.Port2) coloca controle e telemetria na mesma linha, permitindo que
vários dispositivos FBUS compartilhem uma única conexão em cascata
(daisy-chain) com configuração totalmente sem fio. Este passo a passo
liga dois servos Xact aos canais de aileron (1 e 5) do [Exemplo básico de
asa fixa](../tutorials/basic-fixed-wing.md).

!!! note "Capturas de tela pendentes"
    Esta página ainda não possui capturas de tela do simulador — consulte
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md).

## 1. Baixe o firmware mais recente

O FBUS exige firmware atualizado tanto no receptor quanto nos
dispositivos — por exemplo, servos Xact precisam da versão v2.0.1 ou
superior. Obtenha as atualizações necessárias na
[página de downloads da FrSky](https://www.frsky-rc.com/download/).

## 2. Grave o firmware

Copie os arquivos de firmware para a pasta `Firmware/` no SD card/eMMC.
No [Gerenciador de arquivos](../system-setup/file-manager.md), conecte o
servo ao conector S.Port do rádio (fio branco/amarelo voltado para o
encaixe), selecione o arquivo de firmware e escolha **Flash External
Device**.

## 3 / 5. Configure os Physical IDs

Ambos os servos vêm de fábrica com Physical ID `0C` hex / Application ID
`6800` hex — eles entrarão em conflito no barramento compartilhado, a
menos que um deles seja alterado. Existem duas maneiras de fazer isso,
dependendo do tipo de receptor:

**Pelo conector S.Port do transmissor** (qualquer receptor):

1. Conecte o servo 1, vá para **Device Config → XAct** e defina
   **Module** como **S.Port connector**. Mantenha o Physical ID
   `0C`/Application ID `6800` e o canal `CH1` nos valores padrão e então
   use **Save to flash**.
2. Conecte o servo 2 no lugar dele e acesse o mesmo menu. Altere o
   **Physical ID** para `0D` hex e o **Application ID** para `6801` hex
   (consulte a [tabela de Physical
   ID](../model-setup/telemetry.md#how-frsky-telemetry-works) para saber
   quais posições estão livres), defina o **Channel** como `CH5` e use
   **Save to flash**.

**Diretamente pelo receptor** (por exemplo, TD-R18 Tandem, com os dois
servos ligados simultaneamente — veja o
[Passo 4](#4-configure-the-receiver-for-fbus)):

1. Com apenas o servo 1 conectado (por exemplo, no Pin1 do receptor),
   acesse **Device Config → XAct** e defina **Module** → **Internal
   module**. Confirme os padrões (`0C`/`6800`/`CH1`) e use **Save to
   flash**.
2. Com apenas o servo 2 conectado (Pin5), acesse o mesmo menu (o Device
   Config se comunica com um servo por vez) — altere para
   `0D`/`6801`/`CH5` e use **Save to flash**. Selecione o Device Config
   novamente depois para confirmar que a alteração foi mantida.

## 4. Configure o receptor para FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**: [Sistema RF](../model-setup/rf-system.md) → botão do
receptor → **Options** → defina **Telemetry Port** como **FBUS**. Os
servos Xact são então ligados em cascata a partir dessa porta; como cada
servo possui apenas um conector, um extensor multicanal F.Port2
(FP2CH4/6/8) distribui o sinal para vários deles.

**TD-R18 Tandem**: Sistema RF → botão do receptor → **Options** → defina
pinos individuais (por exemplo, **Pin1**, **Pin5**) como **FBUS** —
quantos pinos forem necessários podem ser reatribuídos dessa forma,
dispensando totalmente os extensores; cada pino atribuído como FBUS
transporta o mesmo sinal FBUS.

## 5. Verifique o controle FBUS dos servos

Conecte o servo 1 ao Pin1 e o servo 2 ao Pin5 (os canais de aileron do
exemplo de asa fixa), ligue o sistema e confirme que os canais 1 e 5
movimentam os servos corretos.

## 6. Verifique a telemetria FBUS

Com os dois servos conectados, exclua quaisquer sensores `SRV` existentes
em [Telemetria](../model-setup/telemetry.md) e faça a descoberta
novamente. Cada servo informa 4 sensores: corrente, tensão, temperatura e
status (`OK` quando normal).

## 7. Fazendo alterações de configuração posteriormente

Depois que um modelo está totalmente montado, isolar um servo para
reconfigurá-lo pelo Device Config não é prático. Em vez disso: vá para
Telemetria, localize um sensor pertencente ao servo desejado (por
exemplo, `SRV1 curr`) e escolha **Configure** — isso abre diretamente a
configuração daquele servo. Use **Save to flash** após qualquer
alteração.

!!! warning
    Não altere acidentalmente o Physical ID ou o Application ID nessa
    tela — é isso que mantém cada servo endereçável no barramento
    compartilhado.
