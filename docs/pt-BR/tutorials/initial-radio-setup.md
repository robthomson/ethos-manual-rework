---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuração inicial do rádio

A configuração única a ser realizada antes de programar qualquer modelo. Os
[Tutoriais](index.md) que seguem partem do princípio de que isso já foi feito.

!!! note
    Estes tutoriais não são um receituário rígido — eles pressupõem
    vocabulário básico de RC e familiaridade com a navegação pelos menus do
    Ethos. Se algo aqui não estiver claro, consulte primeiro [Interface do
    usuário e
    navegação](../getting-started/user-interface-and-navigation.md).

## Passo 1. Carregue a bateria do rádio e as baterias de voo

Carregue a bateria do rádio conforme as orientações que acompanham o rádio, e
as baterias de voo com um carregador adequado à sua química — tenha atenção
especial com os pacotes de Lítio.

## Passo 2. Calibre o hardware

Confirme que a [calibração do
hardware](../system-setup/hardware.md#analogs-calibration) foi
realizada (ela é executada automaticamente na primeira inicialização), para que
o rádio conheça o centro exato e os limites de cada gimbal, potenciômetro e
slider. Refaça o procedimento em **System → Hardware** sempre que um gimbal,
potenciômetro ou slider for substituído.

## Passo 3. Faça a configuração do sistema do rádio

A [Configuração do sistema](../system-setup/index.md) abrange tudo o que é comum
a todos os modelos, ao contrário dos ajustes por modelo da [Configuração do
modelo](../model-setup/index.md). A maioria dos valores padrão é adequada para
começar, mas revise:

- **[Data e hora](../system-setup/date-and-time.md)** — ajuste corretamente.
- **[Áudio → Escolha de
  vozes](../system-setup/general.md#audio-settings)** — configure os anúncios
  por voz, incluindo eventuais arquivos de áudio personalizados.
- **[Controles (Sticks)](../system-setup/controls.md)**:
  - **Modo dos sticks** — Modo 1 (acelerador/aileron à direita,
    profundor/leme à esquerda) ou Modo 2 (acelerador/leme à esquerda,
    aileron/profundor à direita — o padrão do Ethos).

    !!! warning
        Se um modelo estiver configurado para um modo de stick enquanto o
        transmissor está ajustado para o outro, um motor elétrico pode
        acelerar no instante em que o receptor for energizado.

  - **Ordem dos canais** — o Ethos usa por padrão **AETR** (Aileron, Elevator,
    Throttle, Rudder); a convenção Spektrum/JR é **TAER**, e a Futaba/Hitec é
    **AETR**. Isso define a ordem em que as entradas dos sticks são atribuídas
    quando um novo modelo é criado — os modelos ainda podem ser ajustados
    individualmente depois.

    !!! note "Receptores estabilizados FrSky"
        Estes exigem especificamente **AETR**. Com mais de uma superfície
        por função (por exemplo, 2 ailerons), o assistente normalmente as
        agrupa (resultando em **AAETR**) — mas os receptores SRx esperam
        **AETRA**/**AETRAE**, então ative **[Primeiros quatro canais
        fixos](../system-setup/controls.md#first-four-channels-fixed)**
        em Sticks para manter os quatro primeiros canais na ordem AETR
        estrita, de qualquer forma.

- **[Bateria](../system-setup/battery.md)** — ajuste **Main voltage**, **Low
  voltage** e **Display voltage range** para corresponder à bateria real do
  rádio.
- **[Owner Registration ID](../model-setup/rf-system.md#owner-registration-id)**
  — usado pelos receptores ACCESS e compartilhado entre transmissores para o
  Smart Share. É configurado em Configuração do modelo, mas na prática funciona
  como um ajuste geral do sistema, já que todo novo modelo o utiliza (ainda
  pode ser alterado por receptor durante o registro, se necessário).

!!! note "Unidades"
    O Ethos não possui um seletor global métrico/imperial — as [unidades dos
    sensores de telemetria](../model-setup/telemetry.md#editing-a-sensor) são
    definidas individualmente, por sensor.
