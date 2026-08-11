---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Encontrar o bootloader mais recente ou outro componente

As versões do firmware Ethos publicam um arquivo `components.json` que lista a
versão atual de cada componente por rádio, útil para confirmar
se uma determinada versão de bootloader/firmware/áudio/arquivos de sistema é
realmente a atual antes de gravá-la.

!!! note "Capturas de tela pendentes"
    Esta página ainda não possui capturas de tela do simulador — consulte [Pipeline
    de capturas de tela](../contributing/screenshot-pipeline.md).

1. Baixe o arquivo `components.json` da versão mais recente do Ethos.
2. Abra-o em um editor de texto (VS Code, Notepad, etc.).
3. Localize a seção correspondente ao seu rádio — por exemplo, `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (Um exemplo pontual — sempre verifique o arquivo da versão *atual* para
   obter os números de versão reais.)

4. Leia a versão do componente que você precisa — no
   exemplo acima, o bootloader mais recente para a família X20 é `1.4.15`.

Consulte [Gerenciador de arquivos](../system-setup/file-manager.md#top-level-folders) para
saber onde colocar o arquivo de firmware baixado, e [Modos de conexão
USB](../getting-started/usb-connection-modes.md#bootloader-mode) para
colocar o rádio em modo bootloader e gravá-lo — ou use o [Ethos
Suite](../ethos-suite/index.md), que cuida da verificação de versão e da
gravação automaticamente.
