---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lista de verificação com texto definido pelo usuário

![Texto da lista de verificação do usuário](../assets/model-checklist-user-checklist.png)

A função [Lista de verificação](../model-setup/checklist.md) pode exibir texto
personalizado na inicialização — texto simples ou formatado em Markdown — de forma
automática, cada vez que aquele modelo é carregado.

## 1. Crie o texto da lista de verificação

**Texto simples** — escreva-o em qualquer editor de texto (Notepad++, ou até
mesmo o MS Word salvo como texto simples) e salve como `<model name>.txt`.

**Texto aprimorado (Markdown)** — o Ethos suporta formatação Markdown, por exemplo,
`##` para um título, `**negrito**` para texto em negrito. Use qualquer editor de texto
(inserindo a sintaxe Markdown manualmente) ou um editor Markdown dedicado
(Nextpad, MarkText, etc.), e salve como `<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Copie o arquivo para o rádio

Copie o arquivo para a mesma pasta `models/` onde está o arquivo `.bin` do próprio
modelo (consulte [Gerenciador de arquivos](../system-setup/file-manager.md#top-level-folders)),
e então ejete com segurança as unidades do rádio antes de desconectá-lo.

## 3. Revise o resultado

Carregue o modelo — o texto da lista de verificação agora aparece automaticamente
como parte das verificações de inicialização, com rolagem caso seja mais extenso
que uma tela.
