---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

O Ethos Suite é o aplicativo complementar para Windows/Mac usado para gerenciar um rádio
executando o Ethos, conectado via USB.

![Aba Radio do Ethos Suite](../assets/ethos-suite-radio-tab.png)

Uma vez conectado, o Ethos Suite pode:

1. Ler o tipo, o ID e as versões instaladas no rádio — firmware,
   bootloader, módulo RF interno, arquivos da memória flash e arquivos do
   SD card/eMMC.
2. Alternar o rádio entre o modo bootloader e a execução do Ethos, e vice-versa.
3. Comparar as versões instaladas com as atuais e atualizar automaticamente —
   apenas os componentes desatualizados, tudo independentemente do estado, ou
   componentes individualmente.
4. Fazer backup dos modelos em disco pelo **Model Manager**, ou restaurar um backup
   anterior (necessário porque os arquivos de modelo não são compatíveis retroativamente
   entre versões de firmware).
5. Baixar qualquer firmware do site de downloads da FrSky pelo **Download
   center**, e usar o rádio como proxy para gravar diretamente um módulo, sensor,
   servo ou receptor.
6. Converter imagens e arquivos de áudio para os formatos nativos do Ethos.
7. Oferecer **ferramentas de desenvolvimento Lua** — documentação da API, scripts de
   demonstração e um terminal de depuração.
8. Gravar o bootloader do rádio em modo DFU (conexão com o rádio desligado),
   independentemente de o firmware do próprio rádio ainda funcionar.
9. Reparar o armazenamento interno nos rádios X18/S, TW Lite, XE e X20 Pro/R/RS
   pela **Repair Tool**, caso a NAND não possa ser lida ou as configurações não sejam salvas.
10. Ejetar as unidades USB do rádio de forma segura.
11. Notificar na inicialização quando houver uma atualização do próprio Suite disponível
    (instalada ao sair).

## Modos de conexão

Além de suas ferramentas, o Suite opera em três estados distintos de conexão com o
rádio:

- **Rádio em modo Bootloader** — a aba **Radio** verifica/atualiza o
  firmware e os arquivos da flash/SD card/eMMC; o **Model Manager** faz backup
  ou restaura o rádio.
- **Rádio em modo Ethos** — o Suite usa o rádio como proxy (por meio das
  ferramentas **FRSK Flasher**/Download center) para gravar diretamente o módulo
  interno, ou qualquer sensor/servo/receptor conectado.
- **Rádio em modo DFU** — conexão com o rádio desligado, usada pelo **DFU
  Flasher** para gravar o próprio bootloader, por exemplo, quando uma corrupção do firmware
  impede que o rádio ligue normalmente.

Consulte [Migração](migration.md) para transferir um rádio existente para o Ethos
Suite pela primeira vez, e [Operação](operation.md) para a interface do Suite
em si.
