---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Informações

![Informações do sistema](../assets/system-info.png)

Detalhes do firmware do sistema, tipo de gimbal, informações do módulo de RF interno/externo, informações do receptor vinculado, tempo de uso do rádio, registros de erros e restauração de fábrica.

## Informações do rádio

- **Número de série** — o número de série do rádio.
- **Firmware** — versão do Ethos e tipo de rádio (por exemplo, X20).
- **Versão do firmware** — variante de compilação, por exemplo FCC, LBT ou Flex.
- **Data** — data/hora de compilação do firmware.
- **RAM disponível** — memória RAM livre do sistema, útil para identificar
  um script Lua com comportamento inadequado; também está disponível como
  [fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)
  do tipo System, podendo ser exibida em um widget.
- **Sticks** — versão do sensor Hall do gimbal instalado (ou "ADC" para
  gimbals analógicos).
- **Módulo interno** — versões de hardware e firmware do módulo de RF
  interno.
- **Receptor** — detalhes do receptor atualmente vinculado, exibidos após o
  módulo interno. Se um receptor redundante compartilhar o mesmo slot do
  principal, os dois são exibidos alternadamente na tela (por exemplo, um
  Archer SR10 Pro mostrado junto com seu R9MM-OTA redundante em
  "Receiver1").
- **Módulo externo** — detalhes de hardware/firmware de um módulo de RF
  externo FrSky instalado que utilize o protocolo ACCESS. Módulos
  Multi-protocol não são exibidos aqui.

![Informações do X20 Pro](../assets/system-info-x20pro.png)

## Tempo de uso do rádio

![Tempo de uso do rádio](../assets/system-info-radio-runtime.png)

Registra o tempo total de uso do transmissor; **Reset** zera o contador.

## Erros

![Erros](../assets/system-info-errors.png)

Um triângulo vermelho na barra superior da tela principal indica que o
Ethos registrou um erro, detalhado aqui. As causas incluem:

- **Erros de script Lua** — um problema em um script Lua em execução.
- **Erro de backup da RAM** — um modelo muito grande para a RAM de backup
  de modelo. O Ethos ampliou esse espaço de 4K para 32K, portanto é pouco
  provável que isso ocorra, mas, se ocorrer, trata-se de um erro
  significativo: o modelo é carregado mais lentamente a partir do SD card,
  em vez da RAM de backup, caso o [Modo de
  emergência](../getting-started/emergency-mode.md) seja acionado.
- **Uso de uma compilação nightly do firmware** — um lembrete de que as
  compilações nightly não são destinadas ao voo.

**Reset** apaga os erros registrados — útil durante uma sessão de
depuração de scripts Lua.

## Restauração de fábrica

![Restauração de fábrica](../assets/system-info-factory-reset.png)

Restaura o rádio às configurações de fábrica inteiramente no próprio
aparelho — sem necessidade de conexão com um PC.

![Confirmação da restauração de fábrica](../assets/system-info-factory-reset-confirm.png)

!!! danger
    A confirmação apaga **todos** os modelos, registros, capturas de tela,
    documentos, scripts, bitmaps e configurações do rádio. Uma barra de
    progresso acompanha o processo de apagamento, após o qual todas as
    unidades são desmontadas e o rádio é reiniciado.

A página de Informações do X20 Pro/R/RS exibe as informações equivalentes
para essa família de rádios.
