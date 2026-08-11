---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Hardware

![Verificação de hardware](../assets/system-hardware-check-x20s.png)

Teste e calibração dos controles físicos do rádio, definições dos tipos de
interruptor e o mapa das teclas de início.

## Verificação de hardware {: #hardware-check }

Exercita cada entrada física para que você possa confirmar que todas são
registradas corretamente.

![Verificação de hardware do X20 Pro](../assets/system-hardware-check-x20pro.png)
![Verificação de hardware do X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — também verifica os dois interruptores de botão com
  travamento **K** e **L** nos ombros traseiros, além dos trims adicionais
  **T5**/**T6**.
- **X18** — também verifica os trims adicionais **T5**/**T6**.

## Calibração dos analógicos {: #analogs-calibration }

![Calibração dos analógicos](../assets/system-hardware-analogs-calibration.png)

Ensina ao rádio exatamente onde estão o centro e os limites de cada gimbal,
potenciômetro e slider. É executada automaticamente na primeira
inicialização; repita-a após substituir um gimbal, potenciômetro ou slider.

## Calibração do giroscópio

![Calibração do giroscópio](../assets/system-hardware-gyro-calibration.png)

Calibra o giroscópio interno para que as entradas baseadas em inclinação
respondam corretamente ao inclinar o rádio — a posição "nivelada" passa a
ser aquela em que você normalmente o segura. Também é executada
automaticamente na primeira inicialização.

## Filtro dos analógicos

Um filtro de ADC (liga/desliga) para os sticks, ativado por padrão — reduz
oscilações em torno do centro do stick. Este é o ajuste **global**; existe
também uma substituição do Filtro dos analógicos **por modelo** em
[Edição do modelo](../model-setup/model-edit.md).

## Ajustes de potenciômetros/sliders {: #potssliders-settings }

Renomeia os potenciômetros e sliders. O **X20 Pro/R/RS** suporta
adicionalmente dois potenciômetros extras, **Ext1**/**Ext2**, normalmente
usados em gimbals de 3 eixos.

![Valores de ADC, potenciômetros](../assets/system-hardware-pots-x20s.png)
![Valores de ADC, potenciômetros (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Ajustes dos interruptores {: #switches-settings }

![Interruptores](../assets/system-hardware-switches.png)

- **Atraso de detecção do meio do interruptor** — evita que uma mudança
  rápida de cima→baixo (ou baixo→cima) de um interruptor de 3 posições
  registre momentaneamente a posição do meio; o meio só deve ser registrado
  quando o interruptor realmente parar nessa posição. O padrão é 0 ms,
  escolhido para se adequar à detecção de "autoverificação" dos receptores
  estabilizados FrSky no CH12.
- **Tipo de interruptor** — SA–SJ podem ser definidos individualmente como
  **None**, **Momentary**, **2 POS** ou **3 POS**, permitindo trocar
  funcionalidades entre interruptores físicos (por exemplo, dar ao
  interruptor momentâneo SH o papel normalmente desempenhado pelo SF de 2
  posições) — sujeito ao que a fiação do rádio realmente suporta (um papel
  de 3 posições geralmente não pode ser atribuído a um hardware que não
  esteja preparado para isso).

  ![Opções de interruptor](../assets/system-hardware-switches-options.png)
  ![Interruptores adicionais](../assets/system-hardware-switches-2.png)

- **Renomeação** — os interruptores podem ser renomeados de SA–SJ para
  nomes personalizados; os nomes são globais para todos os modelos.
- **X20 Pro** — adiciona os interruptores de botão **K**/**L** nos ombros
  traseiros, além das posições **M**/**N** se estiverem conectadas
  (normalmente para interruptores na ponta dos sticks).

## Mapa de teclas de início

Reatribui o destino das teclas de início `SYS`, `MDL` e `DISP` (`TELE` em
rádios mais antigos).

- **`DISP`** — tanto o toque curto quanto o longo podem ser reatribuídos a
  qualquer página de Modelo, página de Sistema, Configurar telas, Início ou
  o Registro de dados de voo. Para manter a consistência com a série X10, o
  toque longo em `DISP` é convencionalmente configurado para Configurar
  telas.
- **`SYS`/`MDL`** — apenas o toque longo é reatribuível (para o mesmo
  conjunto de destinos); um toque curto sempre abre a seção Sistema ou
  Modelo, respectivamente.

## Opções de hardware específicas do rádio {: #radio-specific-hardware-options }

- **Habilitar upgrades de gimbal háptico** (X20 Pro, X20R) — o X20 Pro AW e
  o X20RS vêm com gimbals MC20R que possuem motores hápticos de vibração no
  stick; se gimbals MC20R foram instalados posteriormente em um X20 Pro ou
  X20R, habilite-os aqui (consulte
  [Funções especiais](../model-setup/special-functions.md) para configurar
  os próprios padrões hápticos).

  ![Háptico (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Háptico (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Opção do encoder** (X20 Pro AW, X20R/RS) — esses rádios possuem um
  encoder rotativo mais sensível; habilite **meios passos** para reduzir
  essa sensibilidade.

  ![Opção do encoder (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Inspetor de valores de ADC {: #adc-value-inspector }

Mostra os valores brutos da conversão analógico-digital que a CPU lê para
cada entrada analógica:

![Verificação de ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Verificação de ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S**: 1 stick esquerdo horizontal, 2 stick esquerdo vertical, 3 stick
direito vertical, 4 stick direito horizontal, 5 Pot 1, 6 Pot 2, 7 slider
central, 8 slider esquerdo, 9 slider direito.

**X20 Pro**: como acima, mas com dois canais extras de potenciômetro externo
(7 Ext1, 8 Ext2 — por exemplo, potenciômetros montados nos sticks)
inseridos antes dos sliders, que passam a ser 9 slider central, 10 slider
esquerdo, 11 slider direito.
