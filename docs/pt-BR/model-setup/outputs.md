---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Saídas

![Saídas](../assets/model-outputs.png)

Saídas é a fronteira entre a "lógica" pura das [Mixagens](mixes.md) e o
mundo físico — servos, ligações mecânicas, superfícies de comando,
atuadores, transdutores. É onde os limites de curso, a reversão, a
centralização e as curvas de correção são adaptados ao que o modelo
realmente exige mecanicamente. Cada canal de saída corresponde a uma saída
de servo do receptor (CH1 → conector de servo nº 1, com as configurações
de protocolo padrão).

O Ethos trabalha em porcentagens, mas os servos são, no fim, acionados pela
largura de pulso PWM em microssegundos:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Um canal **sem nenhuma mixagem ativa** emite o valor neutro (0% / 1500µs) — isso
    inclui um canal cuja(s) única(s) mixagem(ns) esteja(m) inativa(s) no momento.
    Certifique-se de que todo canal realmente utilizado tenha sempre uma mixagem
    ativa por trás. Especificamente em um canal de acelerador, o neutro significa
    **meio acelerador**.

A tela Saídas mostra duas barras por canal: a barra inferior (verde) é o
valor do mixer para aquele canal, a barra superior (laranja) é o valor
pós-Saídas efetivamente enviado ao receptor (tanto em % quanto em µs).
Os limites Mín/Máx aparecem como seções acinzentadas da barra laranja. Os
canais que não estão sendo transmitidos ao módulo de RF no momento têm
fundo mais escuro. Pequenos ícones aparecem em um canal quando suas
configurações de Direção, Curva, Lento ou Balanceamento foram alteradas em
relação ao padrão, como forma de identificar rapidamente os canais
não padrão.

!!! tip
    Um toque longo em `ENT` na tela de Mixagens ou de Fases de voo leva
    diretamente para cá.

## Editando um canal {: #editing-a-channel }

![Editar saída do profundor](../assets/model-outputs-elevator-edit.png)
![Editar saída do acelerador](../assets/model-outputs-throttle-edit.png)

Toque em um canal para abri-lo. Uma prévia no topo mostra o valor da
mixagem (verde) em relação ao valor de saída (laranja), com um pequeno
marcador branco para os pontos Mín/Máx.

- **Nome** — editável.
- **Direção** — inverte a saída do canal, tipicamente para inverter o
  sentido de rotação do servo. Exibido como um ícone de seta dupla no canal.
  Isso **não** afeta as mixagens que alimentam o canal e **não** troca os
  limites Mín/Máx.
- **Mín/Máx** — limites rígidos que nunca são ultrapassados — defina-os
  para evitar travamento mecânico. Funcionam como ajustes de limite de
  curso/ganho: reduzi-los diminui o curso em vez de causar corte de sinal.
  O padrão é ±100%, ajustável até ±150%. Durante o ajuste, a extremidade
  na direção da qual o comando está sendo movido é exibida em negrito
  (por exemplo, empurre o stick do profundor para frente e o valor Máx
  fica em negrito, confirmando que é essa a extremidade que você está
  configurando).

  ![Aviso de redundância SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Redundância SBUS"
      Uma configuração de redundância usando SBUS não consegue mover um servo
      além de aproximadamente ±125%. Os próprios campos Mín/Máx têm faixas
      assimétricas (−150–0% e 0–150%) — se você os controlar por uma
      [Var](variables.md), atribua a essa Var uma faixa idêntica ou ative
      **Ignorar faixa** (veja [opções de
      fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      caso contrário a conversão automática de faixa produzirá valores
      inesperados. Se a saída do receptor principal exceder 125% e ele entrar
      em failsafe, o receptor redundante que assume via SBUS a limitará
      novamente a 125%.

- **Centro/Subtrim** — desloca a saída, tipicamente para centralizar o
  braço de um servo; os limites de curso não são afetados.

  !!! warning
      Não use subtrim para deslocamentos grandes — isso introduz um
      diferencial significativo na resposta do servo. Utilize uma
      **mixagem de offset** para qualquer coisa além de um ajuste fino de
      centralização.

- **Centro PWM** — semelhante ao subtrim, mas desloca *toda* a faixa de
  curso do servo, incluindo os limites rígidos, sendo aplicado
  efetivamente dentro do próprio servo em vez de ser mostrado no monitor
  de canais. Isso mantém a centralização mecânica separada do trim.
- **Curva** — associa uma curva Expo ou personalizada (existente ou nova,
  com um atalho **Editar** após definida) para corrigir a resposta no
  mundo real — por exemplo, manter os flaps esquerdo e direito
  acompanhando-se com precisão. Exibido como um ícone de curva no canal.
- **Lento subida/descida** — desacelera a resposta da saída às mudanças de
  entrada, em segundos para percorrer 0→100% — por exemplo, para tornar
  mais lento um trem de pouso retrátil acionado por um servo proporcional
  comum. Exibido como um ícone de relógio no canal. (Um **atraso**,
  diferente do lento, está disponível em [interruptores
  lógicos](logical-switches.md).)

## Trocar canais {: #swap-channels }

![Trocar canais](../assets/model-outputs-swap-channels.png)
![Escolher o canal a trocar](../assets/model-outputs-swap-channels-select.png)

Troca dois canais de saída entre si. A caixa de diálogo abre com o canal
atual já preenchido; escolha o outro e confirme — a troca é imediata, e
toda mixagem que referencie qualquer um dos canais é atualizada
correspondentemente.

## Redefinir configurações

![Redefinir canal](../assets/model-outputs-reset-select.png)

Restaura todos os parâmetros de um canal aos valores padrão — útil antes de
reaproveitar um canal para outra finalidade, com uma caixa de diálogo de
confirmação para evitar acidentes.

## Balancear canais {: #balance-channels }

![Escolher os canais a balancear](../assets/model-outputs-balance-choose_channels.png)
![Escolher CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Balanceia um par (ou até 4) de canais para que se movam em conjunto — por
exemplo, flaps que não se movem juntos podem induzir rolagem indesejada;
aceleradores desbalanceados em um modelo multimotor podem induzir guinada
indesejada. O Ethos cria uma curva de balanceamento diferencial para cada
canal selecionado; comparar as posições físicas das superfícies em cada
ponto da curva permite ajustá-las para coincidirem, resultando em
superfícies perfeitamente sincronizadas.

**Antes de balancear**, nesta ordem:

1. Defina as direções dos servos para o curso correto.
2. Com as mixagens em neutro, opcionalmente use o **Centro PWM** para
   alinhar os braços dos servos.
3. Defina Mín/Máx e Subtrim.
4. Configure quaisquer outras curvas.
5. Configure o Lento.
6. *Então* balanceie e equalize ao longo de toda a faixa de curso.

**Utilização**: escolha os canais a balancear e a ordem em que serão
exibidos —

![CH7/CH6 selecionados](../assets/model-outputs-balance-ch7-and-ch6.png)

— a saída da mixagem no eixo X, o diferencial de ajuste de balanceamento
no eixo Y. Toque no gráfico de um canal (ou selecione-o e pressione `ENT`)
para editar sua curva de balanceamento; `PAGE` alterna entre os canais
durante a edição:

![Editor de curva de balanceamento](../assets/model-outputs-balance-curve-edit.png)

Controles do editor:

- **Fonte** — normalmente a(s) própria(s) fonte(s) da mixagem, ou qualquer
  outra entrada analógica conveniente; **Entrada analógica automática**
  captura como X o primeiro stick/slider/potenciômetro que você mover,
  tanto no gráfico quanto no próprio modelo.
- **Ímã** — faz o ajuste do encoder rotativo saltar automaticamente para o
  ponto de curva mais próximo no eixo X:

  ![Ímã desativado](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Ímã ativado](../assets/model-outputs-balance-ch6-magnet-on.png)

  A entrada ainda precisa ser movida para alinhar X com um ponto da curva
  antes de ajustá-lo.
- **Travar** — alternado tocando em seu ícone ou pressionando `ENT` no modo
  de edição do gráfico; trava todas as entradas para que você possa soltar
  o stick e observar as superfícies de comando enquanto ajusta a curva.
- **Configuração** — altera a quantidade de pontos por canal (todos ou
  individualmente) e se cada curva é suavizada.
- **Ajuda** (`?`, também a tecla `MDL`) — abre a ajuda integrada.

**Multicanal**: até 4 canais podem ser balanceados juntos —

![Balanceamento de 4 canais](../assets/model-outputs-balance-ch2-9-8-1.png)

Uma vez definida, uma curva de balanceamento pode ser revisada, editada ou
apagada na própria página de configuração do canal — um ícone de
balanceamento a identifica no gráfico do canal (ao lado também de um ícone
de Direção, se este também estiver fora do padrão).
