---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Exemplo Básico de Helicóptero Flybarless

Uma configuração básica de helicóptero flybarless (FBL), usando como exemplo
uma controladora como a Spirit. Diferente de um modelo de asa fixa, um
helicóptero é inerentemente instável — a controladora FBL usa giroscópios
(taxa de rotação) e acelerômetros (movimento/orientação) para calcular as
correções de yaw/pitch/roll por meio de uma malha de controle PID
(Proporcional-Integral-Derivativo) ajustada, equilibrando estabilidade,
resposta e sobressinal conforme as características físicas e elétricas
específicas do helicóptero.

Este tutorial cobre apenas o lado da **programação do rádio** — consulte a
documentação da própria unidade FBL para o restante, e comece já com um
conhecimento geral sólido sobre helicópteros.

!!! danger
    Remova as pás do rotor antes de começar, por segurança.

## Passo 1. Confirme as configurações do Sistema

Ordem de canais **AETR**, **[Primeiros quatro canais
fixos](../system-setup/controls.md#first-four-channels-fixed)** **OFF**
— as unidades FBL Spirit esperam os canais SBUS exatamente nesta ordem
(apesar de usarem TAER internamente na sua própria configuração). Registre (se
for ACCESS) e faça o bind do receptor via [RF System](../model-setup/rf-system.md).

## Passo 2. Identifique os servos/canais necessários

| Função | Canal |
|---|---|
| Roll (aileron) | — |
| Pitch (profundor) | — |
| Acelerador | — |
| Yaw (leme) | — |
| Ganho do giro | 5 |
| Passo coletivo | 6 |
| Banco de configurações | 7 |
| Resgate | 8 |

## Passo 3. Crie um novo modelo

![Criar modelo de heli](../assets/tut-heli-eg-wiz-create-heli.png)

Em [Seleção de modelo](../model-setup/model-select.md), crie/selecione uma
categoria Heli, inicie o assistente e escolha **Flybarless**:

![Seleção FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Nome do modelo](../assets/tut-heli-eg-wiz-name.png)

Dê um nome e escolha uma imagem.

## Passo 4. Revise e configure as mixagens

![Visão geral das mixagens](../assets/tut-heli-eg-mixes.png)

O assistente cria Aileron/Profundor/Acelerador/Leme na ordem AETR, Pitch
no canal 6 e FBL Bank no canal 7:

![Mixagem de pitch](../assets/tut-heli-eg-mixes-pitch.png)

Confirme que o canal 6 é o Passo Coletivo. Outros dois canais precisam de
[Mixagens livres](../model-setup/mixes.md#mix-libraries) adicionadas
manualmente: **Ganho do Giro** (canal 5) e **Resgate/Stabi** (canal 8).

**Aileron/Profundor/Leme** — nada a adicionar; as taxas e o Expo são
tarefa da unidade FBL, portanto o rádio apenas repassa uma entrada linear
limpa.

![Mixagem de aileron](../assets/tut-heli-eg-mixes-ail.png)

**Passo Coletivo** — uma curva linear direta; apenas confirme o canal de
saída (normalmente 6). Como acima, taxas/Expo são tratados pela unidade
FBL, não aqui.

**FBL Bank** — os três bancos de configurações da Spirit (estilos de voo
diferentes, ganhos de sensores em RPMs diferentes, ou Iniciante/Acro/3D —
ou simplesmente presets de ajuste) mapeados para um interruptor de 3
posições, por exemplo SE:

![Mixagem de bank](../assets/tut-heli-eg-mixes-bank.png)

**Ganho do Giro** — adicione como Mixagem livre após o último canal. O
ganho normalmente é um valor fixo: defina a **Fonte** como Valor Especial 0,
ajuste o ganho pelo **Offset** (refinado em voo depois) e envie a saída
para o canal 5:

![Mixagem de ganho do giro](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Configure as fases de voo

![Fases de voo](../assets/tut-heli-eg-flight-modes.png)

Três [fases de voo](../model-setup/flight-modes.md): renomeie a padrão
para **Normal** e adicione **Idle Up 1**/**Idle Up 2** no interruptor SD.

### Configure a mixagem do acelerador

Três curvas de acelerador, uma por fase de voo, cada uma uma [curva
personalizada](../model-setup/curves.md):

- **Normal** — aceleração inicial/decolagem: começa em −100% (motor
  desligado), subindo suavemente. Uma curva de 7 pontos com **Smooth**
  ativado funciona bem; os valores exatos precisam de ajuste em voo.

  ![Curva Normal](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1** — voo geral: uma curva em linha reta para um ajuste de
  acelerador constante mantendo a rotação do rotor estável, com o
  movimento vindo do Passo Coletivo, Aileron (roll) e Profundor (pitch).
  Mantenha suave a transição a partir da Normal — sem grandes saltos. (A
  maioria das unidades FBL também oferece uma função **Governor** para
  manter a rotação do rotor constante durante manobras agressivas — veja o
  manual da própria unidade FBL.)

  ![Curva Idle Up 1](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2** — voo agressivo (acrobacias, 3D); novamente, ajustado em
  voo.

  ![Curva Idle Up 2](../assets/tut-heli-eg-curves-iup2.png)

![Curvas de acelerador nas mixagens](../assets/tut-heli-eg-mixes-thr-curves.png)

**Corte de acelerador** — atribua, por exemplo, o interruptor SG na
posição alta com **Sticky** ativado: mover SG para cima corta o acelerador
instantaneamente e (por causa do Sticky) só é possível rearmar com o stick
de acelerador de volta em baixo/desligado primeiro.

![Corte de acelerador](../assets/tut-heli-eg-mixes-thr-cut.png)

**Resgate/Stabi** — atribua de forma semelhante, por exemplo ao
interruptor SA no canal 8.

![Mixagens finais](../assets/tut-heli-eg-mixes-final.png)

## Passo 5. Configuração da FBL

1. **Instale a ferramenta de configuração da FBL** — por exemplo, o
   Spirit Settings, em um PC.
2. **Conecte o receptor à unidade FBL** conforme seu diagrama de ligação —
   tipicamente a saída SBUS Out do receptor à porta RUD da unidade FBL
   (alguns modelos Spirit precisam de um adaptador SBUS), ou então via
   F.Port1/FBUS.
3. **Conecte a unidade FBL ao PC** — por cabo ou Bluetooth, conforme o
   manual dela.

   !!! danger
       Não conecte nenhum servo ainda.

4. **Atualize o firmware da FBL** se necessário, pela aba Update da
   ferramenta.
5. **Configuração geral** (aba General do Spirit Settings):
   - Tipo de receptor: **Futaba SBUS** ou **FrSky F.Port**, conforme o
     caso, e depois reinicie.
   - Mapeamento de canais (com AETR vindo do assistente):

     | Função | Canal |
     |---|---|
     | Acelerador | 1 |
     | Aileron | 2 |
     | Profundor | 3 |
     | Leme | 4 |
     | Giro | 5 |
     | Pitch | 6 |
     | Bank | 7 |
     | Resgate/Stabi | 8 |

     (Este mapeamento decorre da forma como a unidade Spirit interpreta as
     posições do fluxo de dados SBUS.)

6. **Limites de canal** (aba Diagnostic) — a unidade FBL precisa de
   limites de canal do rádio calibrados e centros verificados:

   - Zere primeiro todos os subtrims e trims no rádio.
   - Centralize o stick de Passo Coletivo para ler exatamente 1500µs em
     [Saídas](../model-setup/outputs.md).
   - Ligue a unidade FBL e confirme que aileron/profundor/pitch/leme todos
     leem 0% na aba Diagnostic (a unidade FBL detecta o neutro
     automaticamente a cada inicialização).
   - Mova cada comando até seus limites e ajuste os valores
     correspondentes de **Min**/**Max** em Saídas até que a aba Diagnostic
     leia exatamente +100%/−100%, confirmando também que a direção da
     barra corresponde à direção do stick.

   !!! warning
       Nunca use subtrim ou trim nesses canais — a unidade FBL Spirit os
       trata como comandos de entrada, não como calibração.

7. Ajuste o **Offset** da mixagem de Ganho do Giro para obter o Heading
   Lock.

Com isso concluído, o lado do transmissor está totalmente configurado —
prossiga com o restante da configuração conforme o manual da própria
unidade FBL.
