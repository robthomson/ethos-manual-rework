---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuração de modelo SR8/SR10 e reordenação de canais

Os receptores estabilizados SRx da FrSky esperam uma ordem específica de canais. Há dois
cenários: criar um novo modelo para eles a partir do zero, ou converter um
modelo existente para essa ordem.

!!! note "Capturas de tela pendentes"
    Esta página ainda não possui capturas de tela do simulador — consulte [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## Criando um novo modelo

O assistente de [Seleção de modelo](../model-setup/model-select.md) agrupa
por padrão as superfícies de mesma função (por exemplo, 2 ailerons → `AAETR`), mas os receptores
SRx exigem que os quatro primeiros canais sejam fixados como **AETRA**.

1. Em [Comandos](../system-setup/controls.md), confirme que a **Ordem dos canais**
   está definida como `AETR`.
2. Ative **[Primeiros quatro canais
   fixos](../system-setup/controls.md#first-four-channels-fixed)** — isso
   impede que o assistente agrupe os quatro primeiros canais, mantendo-os
   estritamente na ordem `AETRA…`, independentemente de quantas superfícies de cada
   tipo a aeronave possua.
3. Execute o assistente de criação de modelo normalmente — os 5 primeiros canais
   resultarão em `AETRA`.

!!! note "Autoteste dos receptores Archer"
    O autoteste dos receptores Archer agora é executado por meio de [Configuração do dispositivo →
    SxR](../system-setup/devices.md) (firmware v2.1.10+), em vez de um
    procedimento de autoteste dedicado. O canal do acelerador deve estar em
    −100%, caso contrário o autoteste não será iniciado.

## Reordenando um modelo existente

Converter um modelo existente (por exemplo, atualmente `AAETRFF`) para a
ordem do receptor estabilizado (`AETRAE`, com o canal 9 como Ganho, 10/11 como fases de voo
e 12 como autoteste em unidades SxR mais antigas) consiste em uma sequência de trocas de canais
em [Saídas](../model-setup/outputs.md#swap-channels).

Ponto de partida:

| Can | Função |
|---|---|
| 1 | Aileron1 (direito) |
| 2 | Aileron2 (esquerdo) |
| 3 | Profundor |
| 4 | Acelerador |
| 5 | Leme |
| 6 | Flap1 (direito) |
| 7 | Flap2 (esquerdo) |
| 8 | Trem retrátil |

Ordem desejada: `AETRAE` — CH1 Aileron1, CH2 Profundor, CH3 Acelerador,
CH4 Leme, CH5 Aileron2, CH6 Profundor2/AUX2 (em seguida, Ganho/fases de
voo/autoteste nos canais 9–12).

1. **Primeiro, retire o Aileron2 do caminho**: em Saídas, selecione o CH2
   (Aileron2), toque novamente, escolha **Trocar canais** e faça a troca com um canal
   não utilizado (por exemplo, CH9). A troca é imediata — todas as mixagens que referenciam
   qualquer um dos canais são atualizadas automaticamente.
2. **Troque o CH3 (Profundor) → CH2.**
3. **Troque o CH4 (Acelerador) → CH3.**
4. **Troque o CH5 (Leme) → CH4.**
5. **Troque o CH9 (Aileron2, estacionado no passo 1) → CH5.**

Resultado:

| Can | Função |
|---|---|
| 1 | Aileron1 (direito) |
| 2 | Profundor |
| 3 | Acelerador |
| 4 | Leme |
| 5 | Aileron2 (esquerdo) |
| 6 | Flap1 (direito) |
| 7 | Flap2 (esquerdo) |
| 8 | Trem retrátil |

— agora na ordem que os receptores estabilizados FrSky esperam.
