---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Desativado por padrão. Configure o rádio como **Mestre** (o rádio do
instrutor, que recebe até 16 controles do aluno) ou **Escravo** (o rádio do
aluno, que envia um número configurável de canais ao instrutor).

## Modo Mestre

![Modo Mestre](../assets/model-trainer-master.png)
![Opções do trainer](../assets/model-trainer-options.png)

### Modo de conexão

![Opções do modo de conexão](../assets/model-trainer-link-mode-options.png)

- **Cabo trainer** — um cabo de áudio mono de 3,5 mm entre os dois rádios.
- **Bluetooth** —

  ![Conexão Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Modo** — normal ou alta velocidade; use alta velocidade para menor
    latência, se ambos os rádios oferecerem suporte.

    ![Modo Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Nome local** — o nome BT exibido para os outros dispositivos (padrão
    `FrSkyBT`, editável).
  - **Endereço local** — o endereço Bluetooth deste rádio.
  - **Endereço remoto** — o endereço do rádio pareado, após a conexão.
  - **Procurar dispositivos** (somente no modo Mestre) — busca dispositivos
    próximos:

    ![Procurando](../assets/model-trainer-link-mode-bt-search.png)
    ![Aguardando](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Selecionar dispositivo](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Conectado](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Conectar último dispositivo** / **Redefinir módulo** — reconecta ao
    pareamento anterior ou apaga completamente a configuração do módulo
    Bluetooth.

- **Módulo externo SBUS** — uma entrada SBUS no pino PXX-IN do
  compartimento do módulo externo, para instalar um receptor FrSky com
  saída SBUS (por exemplo, Archer RS) como a extremidade receptora de uma
  conexão sem fio — permitindo que **qualquer** rádio FrSky atue como lado
  do aluno (buddy box), vinculado a esse receptor.
- **Módulo externo CPPM** — a mesma ideia por meio de uma entrada CPPM,
  para um receptor antigo com saída CPPM.

### Condição ativa

![Condição ativa](../assets/model-trainer-active-condition.png)

Um interruptor/botão, interruptor de função, interruptor lógico, posição de
trim ou fase de voo que transfere o controle ao aluno enquanto estiver ativo.

### Canais do trainer

![Edição da condição ativa](../assets/model-trainer-active-condition-edit.png)

Até 16 canais podem ser transferidos do aluno para o mestre enquanto a
Condição ativa for verdadeira. Toque em um canal para configurá-lo
individualmente:

- **Condição ativa** — uma substituição por canal, por exemplo, para
  desativar apenas a entrada de profundor do aluno durante parte de uma
  sessão.
- **Modo** — **OFF** (desativado para uso com trainer), **Add** (os sinais
  do mestre e do aluno são somados, de modo que ambos podem atuar no
  controle ao mesmo tempo) ou **Replace** (o modo normal — o aluno tem
  controle total desse canal enquanto ativo).
- **Percentual** — ajusta a escala da entrada do aluno, normalmente 100%.
- **Destino** — a qual função o canal do aluno é atribuído.

Consulte [Guia prático: retomada instantânea do controle](../how-to/instant-takeback.md)
para um exemplo prático de um instrutor recuperando o controle
instantaneamente por meio de um interruptor, e [Ignorar entrada do
trainer](../getting-started/user-interface-and-navigation.md#choosing-a-source)
para excluir o movimento do stick do aluno de um interruptor lógico que
monitora os próprios sticks do instrutor.

## Modo Escravo

![Modo Escravo](../assets/model-trainer-slave-mode.png)

- **Modo de conexão** — as mesmas opções de cabo trainer, Bluetooth ou
  módulo externo SBUS/CPPM disponíveis no modo Mestre (com os mesmos campos
  Bluetooth **Modo**/**Nome local**/**Endereço local**/**Endereço remoto**).

  ![Modo de conexão do escravo](../assets/model-trainer-slave-link-mode.png)

- **Faixa de canais** — qual faixa de canais deste rádio é enviada ao
  mestre.

  ![Canais do escravo](../assets/model-trainer-slave-channels.png)
  ![Edição de canal do escravo](../assets/model-trainer-slave-channel-edit.png)
