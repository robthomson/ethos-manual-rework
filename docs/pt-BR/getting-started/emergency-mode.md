---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modo de Emergência

O modo de emergência é a resposta do Ethos a uma falha inesperada de baixo
nível, como uma reinicialização do watchdog. O watchdog é um temporizador
continuamente reiniciado por várias partes do sistema; se algo impedir que
ele seja reiniciado, ele expira e força uma reinicialização do hardware. O
modo de emergência então reinicia o rádio o mais rápido possível, ignorando
todas as verificações normais de inicialização, para que o controle do modelo
seja devolvido com o mínimo de atraso. O SD card/eMMC não é acessado de forma
alguma nesse modo.

Apenas as funções essenciais necessárias para continuar controlando o modelo
ficam disponíveis — nenhum dos recursos de nível mais alto. A tela fica em
branco, exceto pelas palavras **EMERGENCY MODE**, acompanhadas de um bipe
repetido de 300 ms a cada 3 segundos; alertas de voz, scripts Lua, registro de
dados e telemetria são todos interrompidos. Se isso acontecer em voo, pouse o
mais rápido possível.

A causa mais comum é a falha do SD card.

## Testando o modo de emergência

É possível adicionar uma **ferramenta de sistema** para acionar
deliberadamente o modo de emergência para fins de teste, de modo que ele não
seja descoberto pela primeira vez durante o voo. Ao tocar no ícone Emergency
Test, é solicitada uma confirmação e, em seguida, o rádio entra em modo de
emergência exatamente como ocorreria em uma falha real.
