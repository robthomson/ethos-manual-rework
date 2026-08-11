---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Layout básico de um widget

Um widget Lua personalizado (consulte [Widgets personalizados](../displays/custom-widgets.md)
para instalar um) é construído a partir de um pequeno conjunto de campos/manipuladores nomeados:

- **`key`** *(string)* — um identificador único para o widget.
- **`name`** *(string ou função)* — o nome de exibição do widget. Pode ser uma
  string simples ou uma função que não recebe argumentos e retorna uma —
  útil para um nome que varia conforme o idioma.
- **`create`** *(função)* — chamada uma única vez quando o widget é criado,
  sem receber argumentos. Retorna uma **tabela do widget**, que é então passada
  a todos os outros manipuladores abaixo — inicialize seu estado aqui e armazene-o
  nessa tabela.
- **`configure`** *(função)* — chamada quando o usuário abre a tela de
  configuração do widget, recebendo a tabela do widget de `create()` como seu
  único argumento e não retornando nada. Monte o formulário de configuração aqui e
  utilize-o para atualizar valores na tabela do widget.
- **`wakeup`** *(função)* — chamada a cada ciclo (aproximadamente a cada 50 ms),
  recebendo a tabela do widget e não retornando nada. Verifique aqui se algo
  mudou; em caso afirmativo, chame `invalidateWindow()` para acionar um redesenho por
  meio de `paint()`. Mantenha este manipulador rápido — idealmente não fazendo nada na
  maior parte das vezes em que é chamado.
- **`event`** *(função)* — chamada quando o widget recebe um evento;
  o Ethos encaminha eventos arbitrários a um widget por meio deste manipulador.
- **`paint`** *(função)* — desenha o widget, recebendo a tabela do widget e
  não retornando nada. Chamada automaticamente sempre que `lcd.invalidate()` for
  acionada. Pode ser comparativamente lenta, mas ainda assim deve efetivamente redesenhar
  apenas quando algo mudou.
- **`read`** *(função, opcional)* — lê o armazenamento persistente do widget.
- **`write`** *(função, opcional)* — escreve no armazenamento persistente do widget.
- **`init`** *(função)* — registra o widget e seus callbacks no
  Ethos. Normalmente é a última coisa no script:

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` deve ser único entre os widgets instalados; os outros campos se conectam ao
ciclo de vida do widget conforme descrito acima.

Os scripts ficam em `scripts/` no SD card/eMMC, idealmente organizados em
pastas por widget (consulte [Gerenciador de
arquivos](../system-setup/file-manager.md#top-level-folders) e [Exemplos de
localização de scripts](example-script-locations.md)). Consulte o tópico *FrSky ETHOS Lua
Script Programming* no rcgroups para mais exemplos práticos.
