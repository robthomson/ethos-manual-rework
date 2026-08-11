---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lista de verificação

![Lista de verificação](../assets/model-checklist.png)

Um conjunto de verificações de segurança pré-voo que são executadas quando o
rádio é ligado e/ou quando um modelo é carregado. As verificações integradas
incluem modo silencioso, failsafe não configurado, posições de
interruptores/potenciômetros, bateria do rádio e bateria do RTC — a verificação
de interruptores mostra em qual direção cada interruptor precisa ser movido,
indicada por pontos vermelhos na tela de aviso:

![Lista de verificação na inicialização](../assets/model-checklist-at_start.png)

!!! note
    Tanto `OK` quanto `RTN` ignoram completamente as verificações pré-voo,
    independentemente do que o aviso na tela sugira.

## Verificação do acelerador

![Função de verificação](../assets/model-checklist-check_function.png)

Ative e escolha um operador — `<` (menor que), `~` (aproximadamente igual) ou
`>` (maior que) — em relação a um valor; avisa se o stick do acelerador estiver
fora do que essa comparação permite.

## Verificação de failsafe

Avisa se o [failsafe](rf-system.md#failsafe) não foi configurado para o modelo
atual.

!!! tip
    É fortemente recomendado manter esta opção ativada.

## Verificação de interruptores

![Interruptores](../assets/model-checklist-switches.png)
![Opções de verificação de interruptor](../assets/model-checklist-switches-options.png)

Para cada interruptor, é possível exigir uma posição específica na inicialização
(interruptores com nomes personalizados em [Configuração do sistema →
Hardware](../system-setup/hardware.md#switches-settings) exibem esses nomes).
**Carregar todas as posições dos interruptores** captura as posições físicas
*atuais* como as desejadas para todos os interruptores que não estejam marcados
como **Sem verificação**.

## Verificação dos interruptores de função

![Interruptores de função](../assets/model-checklist-function-switches.png)
![Opções de verificação do interruptor de função](../assets/model-checklist-function-switches-options.png)

A mesma ideia, aplicada aos seis [interruptores de
função](model-edit.md#function-switches). **Carregar todas as posições dos
interruptores de função** funciona da mesma forma descrita acima.

## Verificação de potenciômetros / sliders

![Potenciômetros](../assets/model-checklist-pots.png)
![Opções de verificação de potenciômetro](../assets/model-checklist-pots-options.png)

Exige posições específicas de potenciômetros/sliders na inicialização,
individualmente para cada controle (`~`/`<`/`>`, igual à verificação do
acelerador). **Carregar todas as posições dos potenciômetros** captura as
posições atuais automaticamente — verifique cuidadosamente os operadores
selecionados automaticamente depois disso, pois `~` em vez de `<`/`>` pode não
corresponder ao que você realmente pretendia.

## Texto definido pelo usuário

![Texto de lista de verificação do usuário](../assets/model-checklist-user-checklist.png)

Exibe um arquivo de texto simples ou de texto aprimorado como parte da lista de
verificação de inicialização, uma vez instalado para o modelo. Consulte [Guia
prático: Lista de verificação com texto definido pelo
usuário](../how-to/user-defined-checklist.md) para a configuração completa.
