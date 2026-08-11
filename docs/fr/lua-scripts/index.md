---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Scripts Lua

Les scripts Lua permettent de créer des [widgets d'affichage](../displays/custom-widgets.md)
personnalisés pour présenter des informations qu'Ethos ne gère pas nativement, ainsi que
(par modèle) des [sources et tâches](../model-setup/lua-scripts.md) personnalisées — une base
qu'il est prévu d'étoffer davantage, vers des fonctions personnalisées spécialisées et
l'intégration de contrôleurs de vol.

Lua est en soi un langage de script généraliste léger et embarquable (utilisé partout, des
jeux vidéo aux applications web) ; Ethos l'intègre précisément pour ce type de
personnalisation directement sur la radio.

!!! warning
    Les scripts Lua allongent le temps de démarrage de la radio. Le délai induit par un
    script bien écrit devrait être imperceptible — un script mal écrit peut retarder le
    démarrage presque indéfiniment.

- [Interpréteur Lua](lua-interpreter.md) — quelle version de Lua et quelles bibliothèques
  Ethos intègre.
- [Documentation Lua d'Ethos](ethos-lua-documentation.md) — où se trouve la référence
  complète de l'API.
- [Emplacements des scripts d'exemple](example-script-locations.md) — où trouver et
  télécharger des exemples fonctionnels.
- [Limites de configuration](configuration-limits.md) — budgets mémoire pour les images
  bitmap et les scripts.
- [Structure de base d'un widget](basic-widget-layout.md) — la structure de code
  nécessaire à un script de widget personnalisé.
