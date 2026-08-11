---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widgets personalizados

Além dos [tipos de widget integrados](index.md), scripts Lua podem implementar
widgets inteiramente personalizados — normalmente um único arquivo `main.lua` mantido em
uma subpasta cujo nome indica sua função.

## Instalando um widget

Copie a subpasta do widget para `scripts/` no SD card/eMMC (veja
[Gerenciador de arquivos](../system-setup/file-manager.md#top-level-folders)). Ele
se registra automaticamente na próxima inicialização e, a partir de então,
aparece no seletor de categorias **Alterar widget** em [Configurar
telas](additional-displays.md), junto com os tipos integrados — sendo configurado
exatamente da mesma forma.

## Criando um widget

Consulte [Scripts Lua → Estrutura básica de um widget](../lua-scripts/basic-widget-layout.md)
para conhecer a estrutura de código que um script de widget precisa implementar.
