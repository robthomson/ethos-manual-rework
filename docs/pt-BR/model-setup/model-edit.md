---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Edição do modelo

![Editar modelo](../assets/model-editmodel.png)

Edita os parâmetros de nível de modelo que o assistente configurou inicialmente — em
sua maioria de identificação, mas também algumas substituições e utilitários por modelo.

## Nome, Imagem

Renomeie o modelo ou altere sua imagem; ao procurar por uma imagem, é exibida uma
miniatura de pré-visualização.

## Tipo de modelo

![Tipo de modelo](../assets/model-edit-modeltype.png)

!!! warning
    Alterar o tipo de modelo redefine **todas** as mixagens.

## Atribuições de canais

Alterar o tipo de cauda ou (em um helicóptero) o tipo de prato cíclico também redefine todas as mixagens.
Outros canais podem ter a quantidade atribuída alterada ou ser desatribuídos.

## Filtro de analógicos

![Filtro de analógicos](../assets/model-edit-analog-filter.png)

[Configuração do sistema → Hardware](../system-setup/hardware.md) possui um filtro
analógico-digital global que pode reduzir a oscilação em torno do centro do stick; este
ajuste por modelo o substitui apenas para este modelo.

![Opções do filtro de analógicos](../assets/model-edit-analog-filter-select.png)

## Interruptores de função {: #function-switches }

![Interruptores de função](../assets/model-edit-fn-switches.png)

Os seis interruptores de função estão disponíveis em qualquer lugar onde apareça um parâmetro
**Condição ativa**, mas — diferentemente dos interruptores comuns — não podem ser usados como
fonte de uso geral. Eles são configurados como uma das seguintes opções:

- **6-Pos with OFF** — pressionar um interruptor de função o mantém acionado; pressionar
  o *mesmo* interruptor novamente desliga todos os seis.
- **6-POS** — pressionar um interruptor de função o mantém acionado até que um *outro*
  seja pressionado, assumindo o lugar dele.
- **2 × 3-Pos** — divide os seis em dois grupos de três, com um interruptor ativo
  por grupo.
- **6 × 2-Pos** — seis interruptores independentes de liga/desliga com retenção.
- **Momentâneo** — seis interruptores independentes, cada um acionado apenas enquanto mantido pressionado.
- **Persistente** — se habilitado, um interruptor de função mantém seu estado após o
  desligamento/recarregamento do modelo, em vez de ser redefinido.

![Opções dos interruptores de função](../assets/model-edit-fn-switches-select.png)

## Conector SPort

O pino de 5 V do conector S.Port do transmissor pode ser ligado ou desligado por modelo —
útil, por exemplo, para alimentar um receptor externo em uma configuração de instrutor.

## Tempo de uso do modelo

![Tempo de uso do modelo](../assets/model-edit-model-runtime.png)

Registra o tempo total em que este modelo foi voado/utilizado.

## Redefinir todas as mixagens

![Redefinir todas as mixagens](../assets/model-edit-model-reset_all_mixes.png)

Redefine todas as mixagens do modelo para seu estado padrão.
