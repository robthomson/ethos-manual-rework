---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Dispositivos

![Dispositivos](../assets/system-devices.png)

Chamado **Device config** no menu — ferramentas para configurar dispositivos
periféricos conectados via S.Port/FBUS: sensores, receptores, o "gas suite",
servos, VTX e ESC. **DIY sensors** aparece automaticamente quando um sensor
DIY é detectado. Consulte o manual específico de cada dispositivo para os
detalhes completos; esta página cobre o que é comum a todos eles.

!!! note
    Isso não tem relação com a escolha de qual módulo de RF (interno ou externo)
    um *modelo* utiliza para transmitir — essa é uma configuração por modelo,
    tratada em [Sistema RF](../model-setup/rf-system.md).

O Device Config é extensível: tanto os usuários quanto a FrSky podem
adicionar páginas aqui por meio de Lua.

## Reatribuindo IDs de sensores

As telas de Device config do Ethos permitem alterar diretamente o **Physical
ID** e o **Application ID** S.Port de um dispositivo. Se você tiver mais de um
dispositivo com a mesma função, conecte-os **um por vez**: descubra cada um em
[Telemetria → Descobrir novos sensores](../model-setup/telemetry.md), altere
seu Physical ID e Application ID aqui no Device config, depois volte e
descubra-o novamente com o novo ID.

## Exemplo de receptores

![Escolha do módulo](../assets/system-devices-module-choice.png)

Os receptores estabilizados FrSky podem ser configurados aqui após a
instalação do respectivo script Lua de configuração (um clique, a partir da
Lua Library do Ethos Suite). Existem dois caminhos de configuração,
dependendo da geração do receptor:

- **Stabilizer config** — receptores mais recentes com "estabilização
  avançada" (controle de ganho no canal 13). São expostos dois grupos de
  estabilização independentes: o Grupo 1 abrange os canais 1–6 e o Grupo 2
  abrange os canais 7–11 — desative o Grupo 2 se você não estiver usando os
  pinos 7–11 para estabilização. Há uma calibração de 6 eixos integrada, que
  deve ser executada uma vez em um receptor novo e novamente após qualquer
  atualização de firmware v3.0.x (depois de um reset de fábrica). Na
  calibração de cada grupo, a antiga etapa de "self-check" foi substituída
  pela calibração independente do nivelamento da aeronave, do centro dos
  canais e dos pontos extremos dos canais, e cada canal pode ser
  ativado/desativado individualmente. As configurações (não os dados de
  calibração) podem ser salvas e restauradas a partir de um PC.
- **SxR** — receptores mais antigos, incluindo unidades legadas e
  Archer/Archer Pro, além de receptores como o SR10 Pro que (apesar do nome
  "SRx") têm o ganho no canal 9 em vez do 13.

  ![Dispositivo atual](../assets/system-devices-current.png)

!!! warning "Após atualizar para o firmware de receptor v3.0.x"
    Faça um reset de fábrica (encontrado em Options do receptor, na
    configuração de RF), depois refaça o bind e reconfigure tudo —
    especialmente as funções Stab e a calibração de 6 eixos. Isso é exigido
    pelo novo recurso de salvamento de dados de failsafe da v3.0.x; verifique
    cuidadosamente a função failsafe depois.

A FrSky North America publica um guia detalhado de configuração de
receptores estabilizados, e existe um vídeo passo a passo do FrSky Team Pilot
Juan Sanchez Garcia cobrindo o mesmo assunto.

## Configurando pelo conector S.Port do transmissor

Dispositivos S.Port e FBUS também podem ser configurados diretamente pelo
conector S.Port no topo do transmissor, sem passar por um receptor
vinculado.

1. Conecte o dispositivo ao conector S.Port do transmissor (fio
   branco/amarelo voltado para o lado com a ranhura).
2. Vá em **System → Device config**, navegue até o dispositivo (por exemplo,
   um sensor de corrente FAS40 ADV) e pressione `ENT`.
3. Na página de configuração, defina **Module** como **S.Port connector**.
4. Faça as alterações desejadas — o Physical ID e o Application ID devem ser
   únicos — depois desça a tela e toque em **Save to flash**.

Isso se aplica tanto a dispositivos FBUS (veja também [Guia prático:
Configurar um sistema FBUS](../how-to/fbus-setup.md)) quanto a dispositivos
S.Port comuns, como um variômetro.
