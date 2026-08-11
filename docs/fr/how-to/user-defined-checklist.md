---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Liste de vérification à texte personnalisé

![Texte de liste de vérification utilisateur](../assets/model-checklist-user-checklist.png)

La fonction [Liste de vérification](../model-setup/checklist.md) peut afficher
un texte personnalisé au démarrage — en texte brut ou formaté en Markdown — automatiquement,
à chaque chargement de ce modèle.

## 1. Créer le texte de la liste de vérification

**Texte brut** — rédigez-le dans n'importe quel éditeur de texte (Notepad++, ou même MS
Word enregistré en texte brut) et enregistrez-le sous `<model name>.txt`.

**Texte enrichi (Markdown)** — Ethos prend en charge le formatage Markdown, par exemple
`##` pour un titre, `**bold**` pour du texte en gras. Utilisez n'importe quel éditeur de texte
(en saisissant la syntaxe Markdown à la main) ou un éditeur Markdown dédié
(Nextpad, MarkText, etc.), et enregistrez-le sous `<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Le copier sur la radio

Copiez le fichier dans le même dossier `models/` que le fichier `.bin` propre au modèle
(voir [Gestionnaire de fichiers](../system-setup/file-manager.md#top-level-folders)),
puis éjectez les lecteurs de la radio en toute sécurité avant de la déconnecter.

## 3. Le vérifier

Chargez le modèle — le texte de la liste de vérification apparaît désormais automatiquement
dans le cadre des contrôles de démarrage, avec défilement s'il dépasse la hauteur d'un écran.
