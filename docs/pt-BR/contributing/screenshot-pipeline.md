---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# Pipeline de capturas de tela

Cada captura de tela deste manual (atualmente cerca de 590 delas, em
`docs/en/assets/`) foi obtida por meio de scripts executados no simulador real do Ethos, e não
manualmente. A estrutura fica no antigo repositório
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), em
`english/manual/`, e **ainda não foi portada para este repositório** — esta
página documenta como ela funciona, para que a portabilidade possa ser feita e para que as capturas de tela possam ser
regeradas ou ampliadas nesse meio-tempo sem começar do zero.

## Como está estruturado

Para cada menu/seção do manual existe um par de arquivos:

- `manual/macros/<name>.lua` — um script escrito com base na API Lua do simulador
  (veja abaixo) que navega até uma tela específica e chama
  `simulator.screenshot(path)` em cada ponto que vale capturar.
- `manual/<name>.sh` — um wrapper de uma linha que inicia o binário do
  simulador para um rádio específico, apontando para aquela macro, por exemplo:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` executa todas as macros em sequência para regerar o
conjunto completo. Existem arquivos `.sh` individuais por seção, de modo que as capturas de tela de uma única
página possam ser regeradas sem executar tudo novamente (cada macro
leva de alguns segundos a mais de um minuto).

Principais flags de linha de comando:

- `--read-only` — não persiste nenhuma alteração feita durante a execução.
- `--no-gui` / `--no-audio` — quase headless; algumas macros ainda precisam da interface gráfica
  porque o simulador "pula" etapas sem ela (veja o comentário em `screenshots.sh`).
- `--radio-settings <file>.bin` — quais configurações salvas de rádio usar na inicialização
  (é isso que torna as capturas de tela específicas por idioma e por rádio — uma execução em alemão
  usa um `.bin` alemão).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — apontam o simulador para os modelos/firmware/documentos/áudios
  que ele deve enxergar, de modo que as capturas de tela reflitam conteúdo preparado deliberadamente, e não
  o que estiver em um SD card real.
- `--exec <script>.lua` — a macro a executar após a inicialização.

Cada família de rádios (X20S, X20 Pro, X20 Pro AW, X18S) tem seu próprio binário de
simulador e precisa de seu próprio arquivo `--radio-settings` por idioma (por exemplo,
`x20s-en.bin`, `x20pro-en.bin`), já que a interface difere ligeiramente entre
rádios e o arquivo de configurações também carrega o idioma.

## A API das macros

As macros são Lua puro, controlando uma variável global `simulator`:

| Chamada | Finalidade |
|---|---|
| `simulator.loadModel("name.bin")` | Carrega um arquivo de modelo específico antes de navegar — cada seção do manual usa um modelo configurado para demonstrar aquela seção (veja a lista de modelos abaixo). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Pressiona uma tecla física — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE`, etc. Uma duração de retenção aciona um pressionamento longo (abre menus contextuais). |
| `simulator.turnRotaryEncoder(n)` | Move o encoder `n` cliques (negativo = sentido inverso) — a principal forma de mover o cursor entre campos. |
| `simulator.touch(x, y)` | Toca em uma coordenada específica da tela — usado onde o toque é a única forma de alcançar algo (por exemplo, alternar o layout do teclado). |
| `simulator.setAnalog(channel, value)` | Define diretamente a posição de um stick/potenciômetro/slider (`0`-`3` são os quatro sticks principais, `ANALOG_LAST_SLIDER` o último slider), para que as capturas de tela mostrem um valor deliberado e reproduzível, e não o padrão do simulador. |
| `simulator.setSwitch(n, position)` | Define a posição de um interruptor físico. |
| `simulator.setDateTime({...})` | Fixa o relógio do simulador, para que os registros de data/hora nas capturas de tela (e tudo que dependa do tempo) sejam reproduzíveis entre execuções. |
| `simulator.screenshot(path)` | Captura a tela atual em um PNG, relativo ao diretório de trabalho da macro (daí os caminhos `../assets/...` dentro de cada macro). |
| `simulator.connectUsb()` | Simula a conexão via USB, para capturar o menu USB. |
| `simulator.sleep(seconds)` | Aguarda que uma animação/valor de telemetria se estabilize antes da captura. |

`manual/macros/common.lua` é carregado com `dofile` pela maioria das macros e apenas fixa a
data/hora, para que toda macro comece a partir do mesmo instante simulado.

## Modelos usados por seção

`manual/notes.txt` (mantido informalmente, ainda não copiado para este repositório)
associa cada macro ao arquivo de modelo `.bin` do qual ela depende e explica o motivo — por exemplo,
`model-mixes.lua` usa `rarebear.bin`, `model-fm.lua` usa `zblank.bin` (um
modelo com configuração de fase de voo deliberadamente em branco), `model-trims.lua` usa
`blaster.bin` (configurado com trims deslocados para demonstrar a faixa de trim).
Portar as anotações desse arquivo para uma documentação adequada aqui faz parte do
trabalho de fase 2 descrito abaixo.

## O que envolve portar isso para o novo repositório (ainda não feito)

- Decidir se as macros serão executadas diretamente a partir deste repositório (exigindo uma
  instalação local do simulador do Ethos, como fazia o repositório antigo) ou via CI com o
  simulador empacotado/baixado no workflow.
- Reestruturar os caminhos de saída planos `../assets/...` para corresponder ao layout de assets
  por página e por localidade deste repositório (`docs/<locale>/assets/`).
- Um `--radio-settings ... .bin` e uma execução de capturas de tela por localidade, tão logo exista uma
  localidade além de `en` — as capturas de tela são específicas do idioma da interface e
  não podem ser compartilhadas entre localidades.
- Decidir quanto das cerca de 40 macros existentes será aproveitado como está versus
  reescrito de acordo com a estrutura de navegação atual deste repositório (algumas macros
  produzem capturas de tela para seções que não correspondem mais 1:1 ao
  layout de páginas deste manual).
