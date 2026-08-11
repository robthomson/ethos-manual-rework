---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lista de verificación con texto definido por el usuario

![Texto de lista de verificación del usuario](../assets/model-checklist-user-checklist.png)

La función [Lista de verificación](../model-setup/checklist.md) puede mostrar
texto personalizado al arrancar —texto plano o con formato Markdown— de forma
automática, cada vez que se carga ese modelo.

## 1. Cree el texto de la lista de verificación

**Texto plano** — escríbalo en cualquier editor de texto (Notepad++, o incluso
MS Word guardándolo como texto plano) y guárdelo como `<model name>.txt`.

**Texto mejorado (Markdown)** — Ethos admite el formato Markdown, por ejemplo
`##` para un encabezado o `**negrita**` para texto en negrita. Utilice cualquier
editor de texto (introduciendo la sintaxis Markdown a mano) o un editor Markdown
específico (Nextpad, MarkText, etc.), y guárdelo como `<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Cópielo a la emisora

Copie el archivo en la misma carpeta `models/` en la que está el archivo `.bin`
del propio modelo (consulte [Administrador de archivos](../system-setup/file-manager.md#top-level-folders)),
y después expulse de forma segura las unidades de la emisora antes de
desconectarla.

## 3. Compruébelo

Cargue el modelo: el texto de la lista de verificación aparecerá ahora
automáticamente como parte de las comprobaciones de arranque, y podrá
desplazarse por él si ocupa más de una pantalla.
