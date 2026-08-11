---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migração

Migrar um rádio das antigas ferramentas de atualização para PC, separadas, para o Ethos Suite, pela primeira vez.

1. **Confirme o Ethos ≥ 1.1.4** — a versão mínima capaz de gravar o novo bootloader compatível com o Suite (formato FRSK) diretamente pelo [Gerenciador de arquivos](../system-setup/file-manager.md). Se necessário, atualize manualmente para a 1.1.4 primeiro.
2. **Faça backup do SD card/eMMC** — copie todo o conteúdo para uma pasta em um PC.
3. **Baixe o bootloader mais recente** em [releases do ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases) e descompacte o arquivo. Cada release publica um `components.json` que lista a versão atual de cada componente — consulte [Guia prático: encontrar o bootloader mais recente](../how-to/find-latest-bootloader.md) para saber como interpretá-lo.
4. Localize o rádio na entrada `targets` desse arquivo para saber a versão exata do bootloader a ser usada e encontre o arquivo correspondente nos assets daquele release.
5. Ligue o rádio em [modo bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) (mantenha `ENT` pressionado e ligue) e conecte-o via USB.
6. Copie o arquivo do bootloader para o SD card/eMMC (normalmente na pasta `Firmware/`), depois ejete as unidades e desconecte.
7. Ligue o rádio normalmente, vá em **Sistema → Gerenciador de arquivos**, toque no arquivo `bootloader.frsk` que acabou de ser copiado e selecione **Flash bootloader**.
8. Baixe e instale o Ethos Suite — a página [Operação](operation.md) trata da atualização de firmware/arquivos e dos demais recursos do Suite a partir daqui.
9. Se o Ethos Suite não fizer isso automaticamente, pode ser necessário renomear a pasta `bitmaps/user` do SD card/eMMC para `bitmaps/models` (é onde ficam os bitmaps de modelos do usuário).
