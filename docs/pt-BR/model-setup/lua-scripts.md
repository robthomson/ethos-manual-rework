---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Scripts Lua (Modelo)

![Configuração Lua](../assets/model-lua-config.png)

Este menu só aparece depois que um script Lua de **source** ou **task** for
instalado em `scripts/` no SD card/eMMC (consulte [Gerenciador de
arquivos](../system-setup/file-manager.md#top-level-folders)) — ele serve para
ativar e configurar esses scripts **por modelo**, e não para instalá-los.
Uma vez instalado, um source ou task fica disponível globalmente para todos
os modelos; esta página é onde cada modelo adere e define sua própria
configuração. Exemplos de scripts de source e task estão publicados no site
Ethos-Feedback-Community (`/lua/examples/task`, `/lua/examples/source`).

## Tasks Lua

Cada task instalada é listada com um botão de ativação por modelo. Ativar
uma delas exibe seu formulário de configuração (se houver) — o script da
task fornece suas próprias funções de leitura/escrita, de modo que cada
modelo pode salvar seus próprios ajustes. Por exemplo, uma task pode
oferecer uma faixa numérica configurável, definida de forma independente
para cada modelo.

## Sources Lua

O mesmo padrão se aplica aos sources: ative por modelo e, em seguida,
configure pelo formulário que o script do source disponibilizar. Um source
registrado dessa forma passa a ser utilizável como uma
[fonte](../getting-started/user-interface-and-navigation.md#choosing-a-source)
comum em qualquer outro lugar do Ethos, exatamente como uma fonte nativa.

## Para autores de scripts

Sources e tasks são registrados via Lua com `system.registerSource()` e
`system.registerTask()` — consulte o Ethos Lua Reference Guide e
[Scripts Lua](../lua-scripts/index.md) neste manual para conhecer o ambiente
geral de scripts (os widgets são um mecanismo separado, mas relacionado —
consulte [Widgets personalizados](../displays/custom-widgets.md)).
