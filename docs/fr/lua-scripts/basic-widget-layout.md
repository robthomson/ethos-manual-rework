---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Structure de base d'un widget

Un widget Lua personnalisé (voir [Widgets personnalisés](../displays/custom-widgets.md)
pour la procédure d'installation) est construit à partir d'un petit ensemble de
champs et de gestionnaires nommés :

- **`key`** *(chaîne)* — un identifiant unique pour le widget.
- **`name`** *(chaîne ou fonction)* — le nom affiché du widget. Soit une
  simple chaîne, soit une fonction sans argument renvoyant une chaîne —
  utile pour un nom qui varie selon la langue.
- **`create`** *(fonction)* — appelée une seule fois lors de la création du
  widget, sans argument. Renvoie une **table du widget**, qui est ensuite
  transmise à tous les autres gestionnaires ci-dessous — initialisez votre
  état ici et stockez-le dans cette table.
- **`configure`** *(fonction)* — appelée lorsque l'utilisateur ouvre l'écran
  de configuration du widget, prenant comme unique argument la table du
  widget issue de `create()` et ne renvoyant rien. Construisez ici le
  formulaire de configuration et utilisez-le pour mettre à jour les valeurs
  de la table du widget.
- **`wakeup`** *(fonction)* — appelée à chaque boucle (environ toutes les
  50 ms), prenant la table du widget et ne renvoyant rien. Vérifiez ici si
  quelque chose a changé ; si c'est le cas, appelez `invalidateWindow()`
  pour déclencher un rafraîchissement via `paint()`. Ce gestionnaire doit
  rester rapide — idéalement, il ne fait rien du tout la plupart du temps.
- **`event`** *(fonction)* — appelée lorsque le widget reçoit un événement ;
  Ethos transmet des événements quelconques au widget par ce gestionnaire.
- **`paint`** *(fonction)* — dessine le widget, prenant la table du widget et
  ne renvoyant rien. Appelée automatiquement chaque fois que
  `lcd.invalidate()` a été déclenché. Elle peut être relativement lente,
  mais ne devrait néanmoins redessiner effectivement que lorsque quelque
  chose a changé.
- **`read`** *(fonction, facultative)* — lit les données persistantes du widget.
- **`write`** *(fonction, facultative)* — écrit les données persistantes du widget.
- **`init`** *(fonction)* — enregistre le widget et ses fonctions de rappel
  auprès d'Ethos. Il s'agit généralement du dernier élément du script :

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

`key` doit être unique parmi tous les widgets installés ; les autres champs
s'intègrent au cycle de vie du widget comme décrit ci-dessus.

Les scripts se trouvent dans `scripts/` sur la SD card ou l'eMMC, idéalement
organisés en dossiers distincts par widget (voir [Gestionnaire de
fichiers](../system-setup/file-manager.md#top-level-folders) et [Exemples
d'emplacements de scripts](example-script-locations.md)). Consultez le fil de
discussion *FrSky ETHOS Lua Script Programming* sur rcgroups pour d'autres
exemples concrets.
