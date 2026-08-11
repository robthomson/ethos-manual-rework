---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Sistema de RF

Configura o(s) módulo(s) de RF interno e/ou externo do modelo, o ID de
Registro do Proprietário, o bind do receptor e as opções do receptor. É também
aqui que fica a escolha do modelo entre módulo interno e externo — diferente de
quase todo o resto em [Configuração do sistema](../system-setup/index.md), a
seleção de hardware de RF é **por modelo**, não válida para todo o rádio.

!!! note "Capturas de tela pendentes"
    O conjunto de capturas de tela desta seção ainda não foi produzido (veja
    [Pipeline de capturas de tela](../contributing/screenshot-pipeline.md)) — o
    conteúdo abaixo está correto, mas por enquanto é apenas texto.

## ID de registro do proprietário {: #owner-registration-id }

Um código único de 8 caracteres (combinação de letras maiúsculas/minúsculas e
dígitos, sem caracteres especiais) que se torna o **ID de Registro** de um receptor
quando ele é registrado. Defina o *mesmo* código em vários transmissores para usar
o **Smart Share** entre eles — faça isso antes de criar o modelo que deseja
compartilhar. Compatível com EdgeTX; apenas parcialmente compatível com OpenTX.

## Desativando a saída de RF

Mantenha `PAGE` pressionado durante a inicialização para desativar a saída de RF
interna e externa naquela sessão (um aviso confirma que está desligada). A
configuração **State** (Estado) do módulo permanece ON — uma reinicialização normal
restaura a transmissão normal.

## Modos do módulo interno

O módulo interno do X18/X20/X20S/X20HD (TD-ISRM) opera em um de três
modos — o módulo TD-ISRM Pro do X20 Pro/R/RS é semelhante, mas adiciona LoRa e
variantes tandem dual-band. Qualquer que seja o modo selecionado, ele **deve
corresponder ao que o receptor suporta**, ou o bind falhará; após trocar de modo,
verifique cuidadosamente cada canal e, especialmente, o comportamento do failsafe.

- **ACCESS** — caminhos de 2,4 GHz e 900 MHz operando em tandem sob um único
  conjunto de controles ACCESS. Até três receptores no total, em qualquer
  combinação de 2,4 GHz (24 canais) e 900 MHz (16 canais); a telemetria de ambas
  as bandas fica ativa simultaneamente, identificada por banda. Uma fonte de
  telemetria **RX** informa qual receptor é atualmente a fonte de telemetria ativa.
- **ACCST D16** — um único caminho de 2,4 GHz, para receptores da série "X"
  legados.
- **TD mode** — tandem de baixa latência e longo alcance em 2,4 GHz + 900 MHz para
  receptores Tandem, 24 canais em cada banda.

As versões de **firmware Flex** adicionam uma segunda coluna Type para alternar
entre a modulação FLEX915M (915 MHz padrão FCC) e FLEX868M (868 MHz padrão LBT)
sob qualquer um dos três modos acima — antenas correspondentes devem ser instaladas
para a opção selecionada. Usuários da UE podem usar 200/500 mW em 868 MHz; a
25 mW, a telemetria trafega em 868 MHz; a 200/500 mW, ela passa para 2,4 GHz por
conformidade regulatória.

Cada escolha de modo/faixa de canais implica um compromisso na taxa de
atualização — por exemplo, em ACCESS, 8 canais atualizam a cada 7 ms, 16 a cada
14 ms, 24 a cada 21 ms (alternando em blocos de 8), e um **Racing mode** de 4 ms
está disponível nos canais 1-8 com receptores compatíveis (série RS, v2.1.7+).

## Registrando e fazendo o bind de um receptor (ACCESS) {: #registering-and-binding-a-receiver-access }

O bind de um receptor ACCESS tem duas fases — o **registro** só precisa ser feito
uma vez por par receptor/transmissor; o **bind** pode ser repetido depois, sem fio
e sem necessidade de botão de bind.

**Fase 1 — Registrar**:

1. Toque em **Register** (pule esta etapa completamente se o receptor já estiver
   registrado).
2. Mantenha o botão de bind do receptor pressionado ao ligá-lo; aguarde até que
   ambos os LEDs acendam. A caixa de diálogo muda de "Waiting for receiver…" para
   "Receiver connected" e preenche o nome do receptor automaticamente.
3. Confirme/edite o **Registration ID** (por padrão, o ID de Registro do
   Proprietário acima — IDs iguais entre transmissores é o que faz o
   Smart Share funcionar), o **Rx name** e o **UID**. O UID distingue
   vários receptores usados juntos em um mesmo modelo — deixe em 0 para um
   único receptor; para vários (por exemplo, um por bloco de 8 canais), é
   convencional usar 0/1/2. O UID não pode ser lido de volta do receptor
   depois, então identifique-o fisicamente.
4. Toque em **Register**, confirme "Registration ok" e então desligue o receptor
   — ele está registrado, mas ainda não vinculado.

**Fase 2 — Bind**:

!!! warning
    Nunca faça o bind com um motor elétrico conectado ou um motor a combustão em
    funcionamento.

1. Receptor desligado; confirme que você está no modo de módulo correto.
2. Toque em **RX1** (ou 2/3) → **Bind**. Um alerta de voz repetido "Bind"
   confirma o modo de bind.
3. Ligue o receptor **sem** tocar em seu botão de bind; selecione-o
   na lista "Select device" que aparece.
4. Confirme "Bind successful". Desligue e ligue novamente o rádio e o receptor —
   LED verde do receptor aceso e vermelho apagado significa que ele está vinculado.
   Não é necessário repetir o bind, a menos que um dos lados seja substituído.
5. Repita para receptores adicionais (RX2, RX3), se utilizados.

## Opções do receptor

Com o receptor ligado, toque em seu botão RX para acessar:

- **Options** — **Telemetry** (liga/desliga para este receptor), **Reduced
  telemetry power 25mW** (em vez dos 100 mW normais — útil se servos próximos
  captarem interferência de RF), **High PWM Speed** (atualização de servo de 7 ms
  em vez de 18 ms — confirme se seus servos suportam), **Telemetry port**
  (S.Port/F.Port/FBUS), **SBUS** (16 ou 24 canais — todo dispositivo SBUS
  conectado deve suportar SBUS-24 antes de ativá-lo) e **Channel
  Mapping** para remapear canais para pinos específicos do receptor.
- **Share** — entrega o receptor a outro rádio ACCESS com um ID de Registro do
  Proprietário *diferente*. No rádio de origem, toque em Share (seu
  LED verde apaga); no rádio de destino, faça o Bind normalmente — o Share
  dispensa o novo registro, já que o ID é transferido automaticamente. Saia no
  rádio de origem para encerrar o compartilhamento; um novo bind o traz de volta.
  (Não é necessário se todos os rádios já compartilham o mesmo ID de Registro do
  Proprietário — basta fazer o bind diretamente no rádio que deve controlá-lo.)
- **Reset bind** — limpa a configuração após um Share e restaura seu próprio bind;
  desligue e ligue o receptor em seguida.
- **Factory reset** — restaura o receptor e apaga seu UID,
  cancelando totalmente o registro.

Com o receptor **desligado**, o mesmo botão RX oferece **Options** (aguarda
a conexão do receptor), **Bind** (por exemplo, para refazer o bind de um receptor
previamente vinculado a outro rádio) e **Clear** (equivalente a Reset bind).

## Receptores redundantes {: #redundant-receivers }

Um segundo receptor pode ser vinculado a um slot RX não utilizado para redundância
— 2.4G ou 900M podem servir de backup um para o outro. A redundância FrSky avalia
**quadro por quadro**, sempre usando o melhor quadro disponível (failover
ativo/ativo), de modo que o controle pode alternar entre receptores de quadro em
quadro conforme necessário.

1. Conecte a saída SBUS Out do receptor redundante à entrada SBUS In do receptor
   principal.
2. Ative o módulo de RF interno correspondente (por exemplo, 900M) e defina sua
   antena/potência.
3. Registre o novo receptor (se ainda não estiver registrado) e faça o bind dele
   no slot RX livre, conforme acima.
4. Confirme que seu LED verde está aceso — ele agora está listado como o receptor
   redundante.

## Failsafe {: #failsafe }

Os dados de failsafe são reenviados pelo transmissor a cada 10 segundos
aproximadamente; nos receptores TD/TW/AP/AP Plus eles também são salvos no
receptor, de modo que sobrevivem a uma reinicialização do receptor. Verifique
novamente o failsafe com cuidado após qualquer atualização de firmware do receptor
que adicione esse comportamento.

- **Hold** — mantém as últimas posições de canal recebidas.
- **Custom** — por canal: **Not Set**, **Hold**, **Custom** (um valor
  fixo — toque no ícone de seta para capturar o valor atual, ou insira um
  diretamente) ou **No Pulses**.
- **No Pulses** — interrompe totalmente os pulsos, para controladoras de voo que
  têm seu próprio comportamento de retorno ao ponto de partida em caso de perda de
  sinal.
- **Receiver** — (receptores série X ou posteriores) define o failsafe no
  próprio receptor.

!!! warning
    Teste cuidadosamente a configuração de failsafe escolhida antes de confiar
    nela.

## Teste de alcance {: #range-check }

Execute este teste no campo antes de cada sessão de voo com uma configuração nova
ou alterada. Selecionar **Range Check** reduz deliberadamente a potência de
transmissão (um alerta de voz repetido confirma o modo) e exibe VFR%/RSSI em tempo
real para avaliar a qualidade do enlace. O nível de potência do teste de alcance da
FrSky é de aproximadamente −10 dB em relação ao nível normal de operação de +20 dB;
com 1 m de altura tanto para o rádio quanto para o receptor, espere um alarme
crítico em torno de 30 m — uma distância menor que isso em condições normais pode
indicar um problema.

Com vários receptores vinculados, os dados do teste de alcance são exibidos para um
receptor ativo por vez em cada banda — desligar o que está ativo permite que o
próximo (na prioridade 0/1/2, indicada pelo sensor **RX**) assuma, de modo que cada
um possa ser verificado por sua vez.

## Módulos de RF externos e de terceiros

Os módulos externos FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
seguem o mesmo padrão de Register/Bind do módulo interno, com
quantidades de canais, níveis de potência e requisitos de antena específicos de cada
protocolo — consulte o manual do módulo específico para os valores exatos.

O **ELRS** (ExpressLRS) é suportado tanto pelo modo ELRS do módulo TWIN Lite Pro
quanto por módulos ELRS genuínos (que precisam do script Lua do ELRS
instalado em `scripts/elrs` antes de aparecerem como opção de módulo). São doze
canais; as configurações principais são **Packet Rate** (compromisso entre latência
e alcance), **Telemetry Ratio** (com que frequência a telemetria é enviada, de 1:1
a 1:128), **Switch Mode** (**Hybrid** — a maioria dos canais auxiliares reduzida a
2–3 posições para menor latência — ou **Wide** — resolução completa de 64–128
passos), **Model Match** e **Tx Power** (10 mW–1000 mW, opcionalmente
**Dynamic Power** para escalar automaticamente conforme a qualidade do enlace —
requer telemetria ativada).

Os **módulos de terceiros** (atualmente Ghost, Multi-protocol, Crossfire, além do
ELRS) exigem, cada um, seu próprio script Lua instalado pelo usuário — veja
as notas do [Pipeline de capturas de tela](../contributing/screenshot-pipeline.md)
sobre `scripts/` e o tópico *Third-Party External Modules* no rcgroups. A
entrada de um módulo só aparece na tela de RF depois que seu script estiver
instalado. O módulo Multi-protocol (IRX4 Lite) pode, além disso, ter seu firmware
gravado diretamente a partir do [Gerenciador de arquivos](../system-setup/file-manager.md):
copie o arquivo de firmware para `Firmware/` e então use **Flash external
multimodule**.
