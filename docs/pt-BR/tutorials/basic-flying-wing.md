---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Exemplo Básico de Asa Voadora (Elevon)

Uma asa voadora com elevons de 2 servos, usando as taxas/Expo/proporções
de mixagem recomendadas do Dreamflight Weasel como exemplo prático
concreto. Complete primeiro a [Configuração Inicial do
Rádio](initial-radio-setup.md).

## Passo 1. Confirme as configurações do sistema {: #step-1-confirm-system-settings }

Ordem padrão **AETR**, com **[Primeiros quatro canais
fixos](../system-setup/controls.md#first-four-channels-fixed)**
**DESLIGADO**. Registre (se ACCESS) e faça o bind do receptor pelo
[Sistema RF](../model-setup/rf-system.md) antes de continuar.

## Passo 2. Identifique os servos/canais necessários

Em uma célula com elevons, as [mixagens](../model-setup/mixes.md)
combinam a entrada de aileron e de profundor em ambas as superfícies
físicas — apenas 2 canais no total, cada um sendo uma combinação das duas
entradas.

## Passo 3. Crie um novo modelo

![Criar modelo de avião](../assets/tut-wing-eg-wiz-create-airplane.png)

Em [Seleção de modelo](../model-setup/model-select.md), inicie o
assistente **Airplane**, escolhendo **Non stabilized receiver**.

![Sem motor](../assets/tut-wing-eg-wiz-no-engine.png)

Selecione **No engine**, aceite os 2 canais de aileron padrão e
selecione **No flaps**.

![Sem cauda](../assets/tut-wing-eg-wiz-no-tail.png)

Selecione **None** para o tipo de cauda — é isso que faz o Ethos
construir automaticamente a mixagem de elevons (entradas de aileron +
profundor, ambas nos mesmos dois canais). Dê um nome ao modelo (por
exemplo, "Weasel"), escolha um bitmap e finalize — ele se torna o modelo
ativo na categoria Airplane.

## Passo 4. Revise e configure as mixagens

![Visão geral das mixagens](../assets/tut-wing-eg-mixes.png)

O assistente cria uma mixagem de Aileron nos canais 1+2, seguida por uma
mixagem de Profundor *também* nos canais 1+2 — ambas as entradas atuam
sobre os dois canais dos elevons, o que é toda a essência da mixagem de
elevons.

### Aileron

![Mixagem de aileron](../assets/tut-wing-eg-mixes-ail-mix.png)

**Peso/Taxas** — conforme o manual do Weasel, a deflexão do aileron deve
ser aproximadamente 3× a do profundor, e as duas devem somar 100%:
**75%** de aileron, **25%** de profundor. As taxas baixas ficam em torno
da metade das taxas altas: **36%** de aileron baixo, **12%** de profundor
baixo.

![Peso da mixagem de aileron](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — recomendado pelo Weasel: 35% alto / 20% baixo, ativo com o
interruptor SB para baixo, suavizando a resposta em torno do centro do
stick.

**Diferencial** — pequeno nesta célula, cerca de **4%**:

![Diferencial de aileron](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Veja o [Exemplo Básico de Asa
Fixa](basic-fixed-wing.md#ailerons) para entender por que o diferencial
importa — o mesmo raciocínio sobre guinada adversa se aplica aqui.)

### Profundor

![Mixagem de profundor](../assets/tut-wing-eg-mixes-ele-mix.png)

O mesmo padrão: taxas alta/baixa de **25%**/**12%**, com os mesmos
valores de Expo do aileron.

### Leme

![Mixagem de leme](../assets/tut-wing-eg-mixes-rud-mix.png)

O Weasel não tem nenhum — asas voadoras geralmente não precisam. Quando
um leme *é* necessário em um modelo com elevons, adicione-o como uma
[Mixagem livre](../model-setup/mixes.md#mix-libraries) no canal 3.

## Passo 5. Faça o bind do receptor

Como no [Passo 1](#step-1-confirm-system-settings) — registre/faça o bind
antes de prosseguir, e considere desconectar os links dos servos ou
reduzir o curso até que os limites Min/Max estejam definidos, para evitar
forçar qualquer componente.

## Passo 6. Revise as mixagens

Os canais de saída 1/2 podem ser renomeados como
**Elevon1**/**Elevon2**. Com aileron totalmente à direita aplicado, o
canal 1 (direito, subindo) indica 75%, enquanto o canal 2 (esquerdo,
descendo) indica 72% — a diferença de 3% *é* o diferencial em ação.
Adicione profundor totalmente para baixo por cima disso e o canal 1
passa a 75+25 = 100%, enquanto o canal 2 passa a 72−25 = 47%.

## Passo 7. Configure os cursos máximos dos servos

![Aileron total](../assets/tut-wing-eg-outputs-full-ail.png)
![Aileron total + profundor total](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Centralize cada servo primeiro com **PWM center**. O curso máximo
recomendado do Weasel é 25mm de aileron + 10mm de profundor = 35mm
combinados — aplique entrada total de aileron/profundor tanto no mesmo
sentido *quanto* em sentidos opostos e confirme que nenhum deles excede
os limites mecânicos ou do servo antes de definir as deflexões finais.

- **Min/Max** — limites rígidos, nunca sobrepostos; reduzi-los diminui o
  curso em vez de recortá-lo. Padrão de ±100%, extensível até ±150% se
  necessário.
- **Curva** — muitas vezes mais rápida e flexível do que ajustar
  Min/Max/Subtrim diretamente, com a vantagem de um gráfico ao vivo. Uma
  curva de 3 pontos atende a maioria das saídas; uma curva de 5 pontos no
  segundo elevon facilita sincronizar o curso em 5 pontos em relação ao
  primeiro. Ao usar uma curva para isso, deixe Min/Max/Subtrim em seus
  valores de passagem direta (−100/100/0, ou −150/150/0 com limites
  estendidos) e deixe a curva fazer a modelagem.
