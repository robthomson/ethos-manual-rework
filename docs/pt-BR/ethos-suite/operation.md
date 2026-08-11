---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Operação

## Seção Boas-vindas

**Novidades da atualização** — notas de lançamento e recomendações de
backup antes de atualizar. O Ethos 1.6.0+ exige que o módulo de RF interno
e os receptores TD/TW/AP/AP Plus estejam na v3.0.1+ para usar suas
melhorias. Ativar **Pré-lançamentos** (com o servidor definido como
GitHub — veja [Configurações do Suite](#suite-settings)) também lista aqui
as versões de pré-lançamento, juntamente com todo o histórico de
lançamentos.

**Página web do Ethos** — uma visualização integrada de
ethos.frsky-rc.com: recursos, links de modelos de exemplo e a lista de
rádios compatíveis.

## Seção Rádio

Gerencia o rádio conectado. Ligue-o em [modo
bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) e
conecte via USB — o Suite mostra o tipo de rádio (por exemplo, "X20") após
detectá-lo.

### Informações do rádio

- **Ethos** — versões instaladas do firmware/bootloader; **Gerenciar
  Ethos** leva diretamente à atualização caso estejam desatualizados.
- **Módulo de RF** — firmware instalado do módulo de RF interno;
  **Gerenciar módulo interno** leva diretamente à sua atualização caso
  esteja desatualizado.
- **Gerenciador de modelos** / **Biblioteca Lua** / **Central de
  downloads** — atalhos para essas ferramentas.

### Atualizando o Ethos {: #updating-ethos }

A aba **Ethos** mostra lado a lado as versões do Firmware, do Bootloader,
do SD card/eMMC (arquivos de áudio) e da memória flash (bitmaps do
sistema) — os arquivos de sistema na flash agora são atualizados junto com
o firmware, não sendo mais gerenciados separadamente.

- **Gravar componentes desatualizados** — atualiza apenas o que está
  atrasado.
- **Gravar todos os componentes** — atualiza tudo, independentemente da
  versão.
- Opções individuais **Gravar firmware**, **Gravar bootloader** e **Gravar
  arquivos de áudio**, cada uma executada clicando no botão cinza-escuro
  ao lado da opção escolhida.
- **Gravar a partir de um arquivo local** — dispensa o download, usando um
  arquivo de firmware já presente no disco.

Selecionar um lançamento significa primeiro escolher um **branch**
(Stable/Testing) e depois uma versão. A atualização solicita primeiro um
backup (**Ir para a página de backup**) — faça-o. Se o módulo de RF
interno não estiver na v3.0.1+, o Ethos 1.6.0+ exige atualizá-lo antes de
continuar (**Ir para o Gerenciador de módulos** o grava automaticamente, e
então a atualização do Ethos é retomada) — e os receptores TD/TW/AP/AP
Plus precisam ter sua telemetria excluída e redescoberta em seguida para
adotar os nomes de sensores atualizados.

O progresso da atualização é exibido passo a passo (mudança para
bootloader, download, cópia, desmontagem, gravação, atualização,
"Atualização concluída com sucesso!") — a própria tela do rádio também
espelha o progresso da gravação.

!!! note "Atualizações de pré-lançamento"
    Os arquivos de um pré-lançamento podem mudar sem que o número da
    versão mude, o que o Suite não consegue detectar — regrave sempre uma
    versão de pré-lançamento que você já esteja usando quando ela se
    tornar um lançamento completo. Verifique a data do firmware em
    [Sistema → Informações](../system-setup/information.md) em caso de
    dúvida.

!!! note "Atualizando a partir do Ethos 1.2.8 ou anterior"
    O Suite pode não conseguir gravar o firmware/bootloader de forma
    totalmente automática a partir de uma versão tão antiga — em vez
    disso, aparece uma caixa de diálogo com gravação manual guiada.
    Ejete as unidades manualmente antes de desconectar o USB, em qualquer
    dos casos.

Os arquivos de bitmap do sistema agora são atualizados automaticamente
junto com o firmware (sem necessidade de gerenciamento separado); os
arquivos de áudio são atualizados por meio de **Gravar todos os
componentes** ou **Gravar arquivos de áudio** (baixa o pacote de idioma
selecionado, por exemplo, "English audio pack").

### Gerenciador do módulo de RF

Selecione uma versão (normalmente a mais recente) e **Gravar módulo** para
atualizar diretamente o firmware do módulo de RF interno — ao concluir,
confirma "...has been flashed successfully". Isso também é acionado
automaticamente pelo caminho obrigatório de atualização para a v3.0.1
descrito acima.

### Modo Ethos

**Mudar para Ethos** reinicia o rádio, saindo do modo bootloader e
executando o Ethos (indicado por um ícone USB verde no rádio e pela
remoção de "(Bootloader Mode)" do cabeçalho do Suite). Isso é necessário
para que a **Central de downloads** use o rádio como intermediário na
gravação de módulos, receptores, sensores e servos. O botão então se torna
**Mudar para Bootloader** para reverter a operação. **Ejetar unidades**
desconecta o rádio de forma segura.

### Gerenciador de modelos

Faz backup dos arquivos de modelo e das configurações no disco, ou
restaura um backup anterior.

!!! warning
    A restauração **não** restaura o firmware — após restaurar
    modelos/configurações, regrave separadamente a versão de firmware que
    corresponda de fato a esse backup (veja [Atualizando o
    Ethos](#updating-ethos)), já que os arquivos de modelo não são
    retrocompatíveis.

- **Local do backup** — navegue até uma pasta (memorizada por tipo de
  rádio); a data/hora do último backup é exibida abaixo dela.
- **Backup** — salva os arquivos de modelo, registrando junto a versão
  atual do Ethos.
- **Restaurar** — selecione quais componentes recuperar: Áudio (desativado
  por padrão), Scripts, Capturas de tela, Bitmaps do sistema (desativado
  por padrão — agora gerenciados junto com o firmware), Modelos (incluindo
  quaisquer arquivos de texto de [lista de verificação definida pelo
  usuário](../how-to/user-defined-checklist.md) armazenados junto a eles),
  Idioma, Bitmaps do usuário, Logs, Configurações do sistema.

### Biblioteca Lua

Navegue e instale com um clique scripts/ferramentas Lua da biblioteca
remota da FrSky (ou instale a partir de um zip local), com os scripts
instalados exibidos ao lado do catálogo remoto quando existir algum.

## Seção Ferramentas

- **Central de downloads** — baixe qualquer firmware do site da FrSky e
  (enquanto o rádio estiver no modo Ethos) use-o como intermediário para
  gravar um módulo, sensor, servo ou receptor conectado por meio de uma
  conexão de atualização S.Port. Escolha o produto na lista (por exemplo,
  um receptor TW SR8), navegue pelos **assets** disponíveis, use
  **Download** para salvar localmente ou **Gravar** para escrever
  diretamente no dispositivo conectado — uma barra de progresso acompanha
  a gravação, terminando em "...has been flashed successfully!"

- **Gerenciador de imagens** — converte imagens para o formato nativo do
  Ethos (BMP de 32 bits, RGB, com canal alfa adicionado somente se
  necessário) no tamanho escolhido, preservando a proporção. Tamanhos de
  referência: imagens de modelo 300×280 (X20) / 180×168 (X18); imagens de
  tela cheia 800×480 (X20) / 480×320 (X18) — veja [Gerenciador de
  arquivos](../system-setup/file-manager.md#top-level-folders) para as
  regras de nomenclatura de bitmaps. Também navega diretamente pelas
  pastas `bitmaps/gps`, `bitmaps/models` e `bitmaps/user` do rádio, com
  suporte a upload. Adicione imagens à lista de transcodificação com **+**
  (TIFF não é suportado), escolha um caminho de saída (uma pasta local;
  diretamente no rádio, em imagens de modelo/usuário/GPS; ou a pasta do
  rádio atualmente aberta) e, opcionalmente, abra automaticamente a pasta
  de saída ou force um canal alfa.

- **Gerenciador de áudio** — converte áudio para o formato do Ethos (PCM
  linear, 32 kHz, mono, 16 bits little-endian). Adicione arquivos com
  **+**, escolha uma pasta local ou envie diretamente para a pasta `audio`
  do rádio (movendo-o depois para a subpasta de voz correta), abrindo
  opcionalmente o destino de forma automática.

- **Ferramentas de desenvolvimento Lua** — **Lua Docs** aponta para o guia
  de referência Lua do Ethos (veja também o tópico do rcgroups *FrSky -
  ETHOS Lua Script Programming*); **Lua Demo Scripts** aponta para scripts
  de exemplo no GitHub da Ethos-Feedback-Community; **Debug** abre uma
  janela de log ao vivo para os rastreamentos `print()` de Lua enviados
  por USB-Serial enquanto o rádio está em modo Serial:

  1. Conecte o rádio ao Suite normalmente e mude para o modo Ethos.
  2. Edite os scripts Lua diretamente na unidade montada do rádio, em
     qualquer editor de código.
  3. Abra **Lua Development Tools** → **START DEBUG** — isso reinicia o
     rádio em modo Serial/depuração e reinicializa os scripts.
  4. A saída `print()` de cada script ativo é transmitida para o terminal
     do Suite.
  5. **STOP DEBUG** retorna ao modo Ethos normal para continuar editando.

- **DFU Flasher** — grava o bootloader por meio de uma conexão USB com o
  rádio desligado (DFU), funcionando mesmo com o firmware totalmente
  corrompido, já que o bootloader ST subjacente reside na ROM. Use
  **Select Bootloader** para escolher um arquivo baixado (o Suite informa
  sua versão/adequação), conecte o rádio **desligado** e então **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Normalmente é um driver DFU ausente/incorreto. A maioria dos PCs com
      Windows 10+ lida com sistemas Tandem usando o driver USB DFU padrão,
      mas o Windows Update às vezes o substitui por um genérico que não
      funciona — verifique o Gerenciador de Dispositivos e considere uma
      ferramenta como o Impulse Driver Fixer. Usuários do Horus X10, em
      particular, podem precisar instalar manualmente o driver USB do
      bootloader STM32 (Impulse Driver Fixer ou Zadig), já que o Windows
      10 não o instala por padrão.

- **Ferramenta de reparo** — para X18/S, TW Lite, XE e X20 Pro/R/RS:
  reformata o armazenamento interno quando o rádio não consegue ler a NAND
  ou salvar configurações.

## Seção Outros

- **Documentação** — links para o GitHub da Ethos-Feedback-Community, os
  manuais oficiais do Ethos (para download) e um FAQ do Ethos Suite.
- **Ethos Github** — lançamentos e rastreador de problemas (pesquise os
  problemas existentes antes de abrir um novo).

### Configurações do Suite {: #suite-settings }

- **Idioma** — tcheco, alemão, inglês, espanhol, francês, hebraico,
  italiano, holandês, norueguês, português, esloveno, chinês.
- **Localização do servidor** — **FrSky server** ou **GitHub** (necessário
  para o acesso a pré-lançamentos citado acima).
- **Opções de depuração** — ativa/desativa o pop-up de erro fatal; habilita
  o log de depuração completo do Suite (não apenas falhas); abre a pasta
  de logs.
- **Versão** / **Atualizar Suite** — versão atual e uma verificação manual
  de atualizações.
- **Sobre** — agradecimentos pelos componentes reutilizados.

## Operação por linha de comando

O Ethos Suite pode ser executado a partir de um terminal:

| Flag | Efeito |
|---|---|
| `--help` | Mostra a ajuda da linha de comando. |
| `--version` | Mostra a versão instalada do Suite. |
| `--list-radios` | Lista todos os rádios FrSky compatíveis. |
| `--radio-components --radio {RADIO}` (ou `--radio auto`) | Lista os componentes de um rádio conectado e seus caminhos. `auto` detecta automaticamente; especifique `{RADIO}` se houver mais de um conectado. |
| `--get-path {COMPONENT}` | Obtém o caminho de um componente — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` ou `I18N`. |
| `--serial start` \| `--serial stop` | Ativa/desativa o modo de depuração serial. |

!!! note
    O Suite não inicia se não reconhecer um comando válido.
