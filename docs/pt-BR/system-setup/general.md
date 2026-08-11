---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Geral

![Configurações gerais](../assets/system-general.png)

Abrange atributos de exibição, áudio, vario, vibração e a barra de ferramentas superior.

## Atributos de exibição

- **Language** — o idioma dos menus (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português, entre outros).
- **Keyboard** — layout do teclado virtual: QWERTY, QWERTZ ou AZERTY.
- **Brightness** — um slider para o brilho da luz de fundo; pressione e
  mantenha `ENT` para controlá-lo a partir de uma fonte (por exemplo, um
  slider, conforme o exemplo abaixo), ou forçá-lo ao mínimo/máximo.

  ![Menu de brilho](../assets/system-general-brightness-menu.png)
  ![Slider de brilho](../assets/system-general-brightness-slider.png)

  !!! note
      Se **Brightness** for igual a **Sleep mode brightness**, a tela de
      toque permanece ativa mesmo enquanto "adormecida".

- **Wake up** — quais destes despertam a luz de fundo do modo de repouso
  (mais de um pode ser habilitado): **Always on** (nunca adormece),
  **Sticks**, **Switches**, **Gyro** (inclinar o rádio). As teclas sempre
  despertam o rádio, independentemente dessas configurações.
- **Sleep** — tempo de inatividade antes de a luz de fundo se apagar
  (esmaecido se Wake up estiver definido como Always on).
- **Sleep mode brightness** — brilho da luz de fundo durante o repouso.
- **Dark mode** — tema de exibição claro ou escuro.
- **Highlight Color** — a cor de destaque da interface (padrão `#F8B038`).

## Configurações de áudio {: #audio-settings }

![Configurações de áudio](../assets/system-general-audio.png)

- **Audio language** — idioma dos anúncios de voz.
- **Escolha de vozes** — o Ethos suporta vários pacotes de voz simultâneos:

  - **Voice 1 (main)** — usada para todos os anúncios internos do sistema.
    Para o inglês, a escolha padrão é entre os pacotes americano (`us`) e
    britânico (`gb`), lidos de `audio/en/us/system` e `audio/en/gb/system`.
    Os arquivos de som do usuário para a [função especial Play
    Audio](../model-setup/special-functions.md) ficam em `audio/en/us/`
    ou `audio/en/gb/`, respectivamente.
  - **Voice 2 / Voice 3** — pacotes adicionais, por exemplo uma voz TTS
    personalizada. Cada um precisa da mesma estrutura de pastas da Voice 1
    — por exemplo, uma voz chamada "Susan" precisa de `audio/en/Susan/`
    para os sons do usuário e `audio/en/Susan/system` para os sons de
    sistema (toda voz precisa de uma pasta `/system`, pois é dela que o
    **Play Value** e os anúncios de temporizador leem; uma lista `.csv`
    dos arquivos de som de sistema padrão acompanha cada versão de áudio).
    Uma vez instalada, uma voz pode ser atribuída por temporizador e por
    função Play Audio — ou até definida como Voice 1 para substituir
    completamente os anúncios do sistema.
  - **Voice "default"** — instalada automaticamente como alternativa
    segura (e usada para evitar problemas de conversão em instalações
    1.4.x): se a Voice 1 ainda não estiver definida durante uma
    instalação/atualização, ela é definida como `default`, lendo de
    `audio/en/default/system`. Os arquivos de som personalizados mais
    solicitados para o Play Audio ficam em `audio/en/default/`.

- **Main volume** — um slider para o volume geral do áudio (pressione e
  mantenha `ENT` para controlá-lo por um potenciômetro); bipes são
  reproduzidos durante o ajuste para que você possa avaliar o nível de
  ouvido.
- **Audio mode**:
  - **Silent** — sem áudio (ainda dispara o [alerta de modo
    silencioso](alerts.md) na inicialização, se habilitado).
  - **Alarms only** — apenas os alarmes são audíveis.
  - **Default** — sons normais.
  - **Often** — adiciona bipes de erro quando um valor é levado além de
    seu mínimo/máximo.
  - **Always** — adiciona bipes para a navegação comum pelos menus, além
    do que o Often faz.
  - **Bluetooth** (apenas X20S/HD/Pro/R/RS) — encaminha o áudio para um
    dispositivo Bluetooth emparelhado (headset, etc.). Escolha **Search
    Devices**, coloque o dispositivo desejado em modo de emparelhamento e
    selecione-o quando for encontrado:

    ![Emparelhamento Bluetooth](../assets/system-general-audio-bluetooth.png)
    ![Busca Bluetooth](../assets/system-general-audio-bluetooth-searching.png)
    ![Dispositivo Bluetooth selecionado](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Conectando Bluetooth](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth conectado](../assets/system-general-audio-bluetooth-connected-ok.png)

    O **Speaker mute** então controla o alto-falante interno — sempre
    ativo, apenas enquanto a telemetria estiver ativa, ou controlado por
    uma fonte (por exemplo, um interruptor). O rádio memoriza o
    dispositivo emparelhado; ligue o rádio antes do dispositivo Bluetooth
    para operação normal e aguarde alguns segundos após a conexão para que
    o silenciamento do alto-falante seja reativado.

## Vario {: #vario }

![Áudio do vario](../assets/system-general-audio-vario.png)

- **Volume** — volume relativo do tom do vario.
- **Pitch zero** — altura do tom com taxa de subida zero.
- **Pitch max** — altura do tom na taxa de subida máxima.
- **Repeat** — intervalo entre os bipes na altura zero.

Veja também o sensor VSpeed em [Telemetria](../model-setup/telemetry.md)
e a [função especial Play Vario](../model-setup/special-functions.md)
para mais detalhes sobre o comportamento do vario.

## Vibração

- **Strength** — um slider para a intensidade da vibração.
- **Mode** — o mesmo conjunto de opções do Audio mode acima.

## Local de armazenamento (X18 e X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

Esses rádios possuem um eMMC interno de 8 GB. Por padrão, o Ethos o
utiliza, tornando o SD card opcional — mas você pode selecionar o eMMC, um
SD card ou uma combinação de ambos. Ao mover o sistema e os modelos para um
SD card, copie as pastas/arquivos relevantes (incluindo áudio e imagens)
**antes** de alterar o local de armazenamento.

![Local de armazenamento](../assets/system-general-storage.png)

## Barra de ferramentas superior

![Configurações da barra superior](../assets/system-general-topbar.png)

- **Digital voltage** — mostra a tensão da bateria do rádio como número, em
  vez de uma barra, na barra de ferramentas superior.
- **Digital RSSI** — o mesmo, para o RSSI de 2,4 GHz e 900 MHz.
- **Select model at power on** — mostra a tela de seleção de modelo na
  inicialização, antes de aparecerem os alertas da lista de verificação do
  modelo anterior, permitindo trocar de modelo sem antes descartá-los. O
  último modelo utilizado fica destacado por padrão.

  ![Selecionar modelo na inicialização](../assets/system-general-model-start.png)

## Pré-seleção do modo USB

![Modo USB](../assets/system-general-usb.png)

O que acontece automaticamente quando o rádio se conecta a um PC via USB:

- **Not set** — solicita uma escolha no momento da conexão.
- **Joystick** — entra imediatamente no modo joystick para um simulador de RC.
- **Ethos Suite** — entra imediatamente no modo Ethos para o [Ethos
  Suite](../ethos-suite/index.md).
- **Serial** — entra imediatamente no modo Serial, encaminhando os rastros
  de depuração Lua por USB-Serial a 115200 bps (pode ser necessário um
  driver de porta COM virtual no Windows).
