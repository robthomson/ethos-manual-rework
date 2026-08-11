---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Gerenciador de arquivos

![Gerenciador de arquivos - rádio](../assets/system-filemanager-radio.png)

O Gerenciador de arquivos permite navegar pelo armazenamento do rádio e gravar
firmware no módulo de RF interno, em dispositivos conectados por S.Port, em
dispositivos OTA (Over-The-Air) e em módulos externos.

## Estrutura de armazenamento

Toque em **Flash** (ou pressione `PAGE` para alternar entre as unidades) para
navegar pela unidade flash USB virtual interna do rádio, usada para os bitmaps e
as fontes do sistema:

![Armazenamento flash](../assets/system-filemanager-flash.png)

- `bitmaps/system` — os bitmaps usados nas telas e nos ícones
- `fonts/` — fontes para as diferentes seleções de idioma

Tanto o bootloader quanto o próprio firmware do sistema residem nessa memória
flash interna, em todos os rádios FrSky desde o X9D original.

A série **X20/X20S/X20HD** aceita um SD card formatado em FAT32, de 32GB ou
menos (um SanDisk Ultra Micro SDHC Classe 10 de 16GB é uma boa escolha).
O **X18** e o **X20 Pro/R/RS** usam um eMMC interno por padrão (um SD card
externo pode ser adicionado em conjunto) — toque em **Radio** para navegar por
ele. O Ethos cria automaticamente `Logs/`, `models/` e `screenshots/` caso não
existam; `Firmware/` é uma convenção manual para arquivos de firmware de
dispositivos, como receptores.

## Pastas de nível superior {: #top-level-folders }

- **`audio/`** — arquivos de som do usuário e do sistema, separados por voz
  (`audio/en/gb`, `audio/en/us`, `audio/en/default`). Os arquivos do usuário
  são reproduzidos pela [função especial Play Audio](../model-setup/special-functions.md);
  os arquivos do sistema incluem `hello.wav` (a saudação "Welcome to Ethos" — um
  `bye.wav` pode ser adicionado, mas não é fornecido). Formato: PCM de 16kHz ou
  32kHz, linear de 16 bits, ou A-law (EU)/µ-law (US) de 8 bits; nomes de arquivo
  de até 31 caracteres mais a extensão. As três pastas de voz são mantidas
  sincronizadas pelo Ethos Suite, independentemente de qual esteja realmente
  selecionada.

  ![Pasta audio](../assets/system-filemanager-audio.png)

- **`bitmaps/`** — `bitmaps/models/` contém as imagens de modelo do usuário
  (definidas em [Model Edit](../model-setup/model-edit.md) ou nos assistentes de
  novo modelo); `bitmaps/user/` contém todo o restante. Formato recomendado: BMP
  de 32 bits, 8 bits por cor, com canal alfa, 300×280px — isso mantém baixo o
  custo de decodificação no rádio. O Ethos redimensiona BMPs em tempo real, mas
  não PNG/JPEG. Os nomes de arquivo podem usar apenas `A-Z a-z 0-9 ()!-_@#;[]+=`
  e espaços, e devem ter 11 caracteres ou menos (mais uma extensão de 4
  caracteres) para aparecer no seletor de imagem de modelo — nomes mais longos
  ainda aparecem no Gerenciador de arquivos, mas não poderão ser selecionados
  ali. As ferramentas de conversão de imagem do Ethos Suite fazem a conversão de
  formato para você.

  ![Pasta bitmaps](../assets/system-filemanager-bitmaps.png)

- **`documents/user/`** — documentos de texto do usuário, chamados pelo widget de
  tela **Text**.

- **`Firmware/`** — arquivos de firmware para o módulo de RF interno, módulos
  externos e outros dispositivos (receptores, etc.), gravados a partir daqui via
  S.Port ou OTA. Copie o novo firmware para cá enquanto o rádio estiver em
  [modo bootloader](../getting-started/usb-connection-modes.md) e conectado por
  USB; ao tocar em um arquivo de firmware e escolher **Flash**, a atualização é
  iniciada:

  ![Gravar o módulo de RF interno](../assets/system-filemanager-flash.png)
  ![Gravar o receptor S8R via S.Port](../assets/system-filemanager-flash-S8R.png)
  ![Gravar o receptor TD-R18 por OTA](../assets/system-filemanager-flash-TD-ISRM.png)
  ![Gravar o bootloader](../assets/system-filemanager-flash-bootloader.png)

- **`I18n/`** — arquivos de tradução de idioma.

- **`Logs/`** — logs de dados.

- **`models/`** — os próprios arquivos de modelo. Eles não podem ser editados
  diretamente aqui, apenas copiados como backup ou compartilhados. Desde o Ethos
  v1.2.11, o modelo é nomeado a partir do seu nome de modelo, em vez de
  `model01.bin` em diante (por exemplo, um modelo chamado "Extra" se torna
  `Extra.bin`; um segundo "Extra" se torna `Extra01.bin`). Renomear um modelo em
  [Model Edit](../model-setup/model-edit.md) também renomeia o seu arquivo —
  sempre em letras minúsculas (o nome de exibição com maiúsculas e minúsculas é
  armazenado dentro do arquivo), e não todos os caracteres de um nome de modelo
  sobrevivem no nome do arquivo. Desde a v1.1.0 Alpha 17, cada categoria de
  modelo criada pelo usuário recebe a sua própria subpasta.

- **`screenshots/`** — saída da [função especial
  Screenshot](../model-setup/special-functions.md).

- **`scripts/`** — Scripts Lua, opcionalmente organizados em suas próprias
  subpastas com arquivos de apoio. Os tipos de script são **widgets** (consulte
  [Telas](../displays/index.md)), **tasks e sources** (sensores personalizados
  ou ações pós-voo — instalados aqui, aparecem no menu
  [Lua](../model-setup/lua-scripts.md) do modelo) e **tools** (por exemplo, as
  ferramentas de configuração de receptores estabilizados nos menus do sistema).
  Cada módulo externo de terceiros recebe o seu próprio script e pasta, por
  exemplo `scripts/multi`, `scripts/elrs`, `scripts/ghost`,
  `scripts/crossfire`.

  !!! warning
      Os scripts Lua aumentam o tempo de inicialização do rádio. O atraso de um
      script bem escrito é imperceptível — um script mal escrito pode atrasar a
      inicialização quase indefinidamente.

- **`radio.bin`** (pasta raiz) — o arquivo de configurações do sistema, gravado
  pelo próprio rádio na inicialização. Faça o backup dele junto com `models/`
  antes de uma atualização de firmware, para que você possa retornar a uma
  versão anterior se necessário.

- **`firmware.bin`** (pasta raiz) — coloque um novo arquivo de firmware do rádio
  aqui para que ele seja gravado automaticamente na próxima vez que o rádio for
  desconectado do PC. O conteúdo do SD card/eMMC e da unidade flash interna pode
  precisar ser atualizado na mesma passagem.

- **`sdcard.version`** (pasta raiz) — a versão do conteúdo do SD card, mantida
  pelo Ethos Suite.

## Compartilhamento de arquivos por Bluetooth

O Ethos pode transferir arquivos entre rádios via Bluetooth. No rádio
**receptor**, navegue até a pasta de destino no Gerenciador de arquivos,
pressione longamente `ENT` e escolha **Receive file here**:

![Recepção por Bluetooth](../assets/system-filemanager-bluetooth-receive.png)

No rádio **emissor**, toque no arquivo, escolha **Send file** e siga as
instruções em ambos os rádios:

![Envio por Bluetooth](../assets/system-filemanager-bluetooth-send.png)

Se algum dos rádios já tiver uma conexão Bluetooth ativa (telemetria, link de
treinamento ou — no X20S/Pro — áudio), será perguntado se você deseja
desconectar esse dispositivo primeiro.
