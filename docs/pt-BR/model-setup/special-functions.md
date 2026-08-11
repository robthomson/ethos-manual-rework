---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Funções especiais

![Menu de funções especiais](../assets/model-sf-menu.png)

As funções especiais disparam uma ação — reproduzir áudio, capturar a
tela, gravar logs, feedback de vibração e muito mais — quando uma condição
se torna verdadeira. São suportadas até 100; nenhuma existe por padrão.
Adicione uma com **+**; toque em uma existente para
**Editar**/**Mover**/**Copiar-colar**/**Clonar**/**Excluir**.

![Adicionar função especial](../assets/model-sf-add.png)
![Mover](../assets/model-sf-move.png)

## Campos comuns a todas as ações

- **Estado** — ativa/desativa esta função sem excluí-la.
- **Condição ativa** — **Sempre ativo**, ou condicionada a posições de
  interruptor/interruptor de função/interruptor lógico/trim ou a fases de
  voo. Pressione longamente `ENT` sobre um interruptor e marque
  **Negativo** para invertê-lo (por exemplo, `SG-up` torna-se `!SG-up`,
  ativo sempre que SG *não* estiver para cima).
- **Global** — adiciona esta função a **todos** os modelos, existentes e
  futuros. Se um modelo já possuir uma função local configurada de forma
  idêntica, o Global a adiciona como uma entrada adicional; desativar o
  Global novamente a remove de todos os modelos, exceto do que está
  selecionado no momento. As funções globais residem em `radio.bin`; as
  locais residem no arquivo do modelo.

## Ações {: #actions }

**Redefinir** — redefine **Dados de voo** (telemetria + temporizadores),
**Todos os temporizadores** ou **Toda a telemetria**.

![Redefinir](../assets/model-sf-reset.png)

**Captura de tela** — salva uma captura de tela em `screenshots/` no
SD card/eMMC.

![Captura de tela](../assets/model-sf-screenshot.png)

**Definir failsafe** — captura as posições atuais dos canais como
failsafe, por meio do **Módulo** de RF interno ou externo.

![Definir failsafe](../assets/model-sf-set-failsafe.png)

**Reproduzir áudio** — a ação mais rica, com suporte a uma sequência
completa:

![Reproduzir áudio](../assets/model-sf-play-audio.png)

- **Voz** — qual das até 3 vozes configuradas será usada (consulte
  [Geral](../system-setup/general.md#audio-settings)).
- **Repetir** — reproduzir uma vez ou repetir em um intervalo configurável
  (até 10 minutos).
- **Ignorar na inicialização** — evita que esta função seja disparada
  durante a inicialização.
- **Sequência** — até 100 etapas, cada uma delas:

  - **Reproduzir arquivo** — reproduz um arquivo de áudio escolhido.

    ![Reproduzir arquivo](../assets/model-sf-play-audio-add-play-file.png)

  - **Reproduzir valor** — fala o valor de uma fonte: analógicos,
    interruptores, interruptores lógicos, trims, canais, giroscópio,
    relógio do sistema, trainer, temporizadores ou telemetria.

    ![Reproduzir valor](../assets/model-sf-play-audio-add-play-value.png)

  - **Aguardar duração** — uma pausa fixa, de até 10 minutos.
  - **Aguardar condição** — pausa a sequência até que uma condição seja
    atendida.

  ![Adicionar linha à sequência](../assets/model-sf-play-audio-add-line.png)
  ![Tipo de linha da sequência](../assets/model-sf-play-audio-add-line-type.png)

  Por exemplo: reproduzir `vfrlow.wav` quando o interruptor lógico
  `VFRlow` se tornar ativo e, em seguida, falar o valor mínimo de VFR
  registrado —

  ![Reproduzir valor após arquivo](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — ou pausar uma sequência até que o interruptor SH seja movido para
  baixo antes de continuar:

  ![Sequência com condição de espera](../assets/model-sf-play-audio-add-sequence.png)

  Toque em qualquer linha da sequência para editá-la, adicionar,
  reordenar ou excluí-la:

  ![Gerenciamento da sequência](../assets/model-sf-play-audio-add-sequence-management.png)

**Haptic** — feedback de vibração:

![Haptic](../assets/model-sf-haptic.png)

- **Padrão** — simples, duplo, triplo, quíntuplo ou muito breve.

  ![Padrão de vibração](../assets/model-sf-haptic-pattern.png)

- **Intensidade** — 1–10 (padrão 5).
- **Repetir** — uma vez ou em um intervalo definido.
- **Selecionar motores haptic** — em rádios com motores haptic nos gimbals
  (X20 Pro AW, X20RS ou um X20 Pro/X20R atualizado com gimbals MC20R —
  consulte
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Padrão** (haptic interno), **Todos os motores**, **Stick esquerdo** ou
  **Stick direito**.

  ![Haptic no X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Gravar logs** — grava logs `.csv` em `Logs/` no SD card/eMMC, com marca
de tempo do RTC (essencial para diferenciar as sessões de voo
posteriormente):

![Gravar logs](../assets/model-sf-write-logs.png)

- **Intervalo de gravação** — 100–500 ms.
- **Sticks/Potenciômetros/Sliders**, **Interruptores**, **Interruptores
  lógicos**, **Canais** — categorias de registro ativadas
  independentemente.

  **Visualização dos logs**: abra um arquivo de log em `/Logs` no
  Gerenciador de arquivos. Escolha quais canais plotar (RSSI é selecionado
  por padrão); desloque a visualização com o encoder rotativo ou com um
  gesto de deslizar e aplique zoom girando o encoder enquanto mantém
  `PAGE` pressionado. `DISP` move o foco para o primeiro botão da coluna
  direita.

**Reproduzir texto** (apenas X20 Pro) — conversão de texto em fala no
próprio rádio, em vez de um arquivo pré-gravado:

![Reproduzir texto](../assets/model-sf-x20pro-play-text.png)

- **Texto** — a cadeia a ser falada. LETRAS MAIÚSCULAS são soletradas
  letra por letra (por exemplo, "OFF" → "O-F-F"); letras minúsculas são
  faladas como palavra ("off").
- **Repetir**, **Ignorar na inicialização** — conforme descrito acima.

**Ir para tela** — muda a exibição para uma tela escolhida, por exemplo
saltando para o registro de dados de voo de um receptor quando um botão é
pressionado:

![Ir para tela](../assets/model-sf-go-to-screen.png)
![Opções de tela](../assets/model-sf-go-to-screen-options.png)

**Bloquear tela de toque** — bloqueia a tela de toque contra toques
acidentais (também acessível diretamente mantendo `ENT` + `PAGE`
pressionados juntos por 1 s na tela inicial):

![Bloquear tela de toque](../assets/model-sf-lock-touchscreen.png)

**Carregar modelo** — carrega um **Modelo** especificado quando acionada,
com um aviso opcional de **Confirmação** antes da troca efetiva:

![Carregar modelo](../assets/model-sf-load-model.png)

**Reproduzir vario** — gera o áudio do vario a partir de uma fonte
escolhida (normalmente o sensor VSpeed de um vario FrSky, mas qualquer
sensor com unidade m/s funciona):

![Reproduzir vario](../assets/model-sf-play-vario.png)
![Fonte do vario: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Faixa** — taxa de subida/descida mapeada para o tom, padrão ±10 m/s
  (até ±100 m/s). Acima do **Centro**, o tom sobe linearmente com a taxa
  de subida até o valor máximo da Faixa (o tom da taxa máxima é definido
  em [Geral →
  Vario](../system-setup/general.md#vario)); ao descer, é emitido um tom
  contínuo cuja altura cai em direção ao valor mínimo da Faixa.
- **Centro** — a faixa de "subida zero", padrão ±0,3 m/s (até ±2 m/s); o
  tom permanece constante dentro dela (o tom de taxa zero também é
  definido em Geral → Vario). Mude **Beep**→**Silencioso** para silenciar
  o tom completamente.

  ![Opções de faixa/centro do vario](../assets/model-sf-play-vario-options.png)
