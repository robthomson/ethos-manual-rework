---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Modos de conexão USB

![Menu USB](../assets/usbmenu.png)

O que uma conexão USB com um PC faz depende de como o rádio estava
alimentado quando você o conectou.

## Modo desligado

Conectar o rádio a um PC via USB **enquanto ele está desligado** o coloca
em modo DFU, usado para gravar o próprio bootloader.

## Modo bootloader {: #bootloader-mode }

Ligue o rádio **mantendo `ENT` pressionado** para iniciar no modo
bootloader (a tela mostra "Bootloader"). Conectar o USB agora altera o
status para "USB Plugged" e o PC monta **duas** unidades: a memória flash
interna do rádio e o conteúdo do SD card/eMMC. Esse é o modo para ler e
gravar arquivos diretamente em qualquer uma das áreas de armazenamento, e
também é como o [Ethos Suite](../ethos-suite/index.md) atualiza o firmware
do rádio — consulte a seção Modo Bootloader do próprio Ethos Suite.

## Modo ligado

Conectar o USB enquanto o rádio está **ligado normalmente** exibe um
seletor de modo:

- **Joystick** — apresenta o rádio como um joystick USB HID, para operar
  simuladores de voo no PC.
- **FrSky Suite** — coloca o rádio em "modo Ethos" para comunicação com o
  [Ethos Suite](../ethos-suite/index.md).
- **Serial** — encaminha os rastreamentos de depuração Lua pela porta
  serial USB (115200 bps). A aba Lua Development Tools do Ethos Suite tem
  um terminal integrado para exibi-los; pode ser necessário um driver de
  porta COM virtual no Windows.
