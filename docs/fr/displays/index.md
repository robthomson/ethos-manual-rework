---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Écrans

![Écran d'accueil](../assets/display-home.png)

L'écran d'accueil est constitué d'un ou plusieurs **écrans d'affichage**,
chacun construit à partir de **widgets** que vous placez et configurez
vous-même. Une pression sur `DISP` ouvre l'éditeur d'affichage de l'écran
courant.

Jusqu'à **huit** écrans sont disponibles, chacun basé sur l'une des
**treize** dispositions (contenant jusqu'à **neuf** cellules de widget).
Les widgets peuvent afficher de la télémétrie, mais également l'une des
dix-sept autres catégories d'informations — état du modèle et de la radio,
chronos, voies, et bien plus. Les écrans configurés sont accessibles par
balayage tactile ou avec `PAGE` haut/bas ; les barres supérieure et
inférieure restent visibles sur chaque écran, sauf dans une disposition
plein écran.

## Ajouter un widget

![Types de widgets](../assets/display-widget-types.png)

Chaque écran est une grille ; toucher une cellule vide ouvre le sélecteur
de widgets. Les widgets vont du simple texte et des affichages numériques
aux jauges, graphiques et journaux de télémétrie complets. Une fois placé,
toucher à nouveau un widget ouvre le même menu d'options que celui utilisé
pour le redimensionner, le déplacer ou le supprimer :

![Options de configuration du widget](../assets/display-widget-config-options.png)

Sélectionner les réglages propres à un widget ouvre un formulaire de
configuration spécifique à celui-ci. Le champ **source** — la valeur
affichée par le widget — utilise le même
[sélecteur de source](../getting-started/user-interface-and-navigation.md#choosing-a-source)
que partout ailleurs dans Ethos :

![Modifier la source du widget](../assets/display-change-source.png)

## Types de widgets {: #widget-types }

**Value** — une seule valeur numérique ou de télémétrie, affichée sous
forme de texte :

![Configuration du widget Value](../assets/display-widget-value-config.png)

La plupart des sources permettent également de réduire la valeur à un
**min** ou un **max** en temps réel — après avoir sélectionné la source,
faites un appui long dessus et choisissez Min ou Max — pratique par exemple
pour le RSSI le plus faible relevé pendant un vol :

![Widget Value min](../assets/display-widget-value-min.png)
![Widget Value min RSSI](../assets/display-widget-value-min-rssi.png)

Une fois placé, il s'affiche à l'écran comme une simple valeur :

![Widget Value télémétrie](../assets/display-widget-value-telemetry.png)

**Bitmap** — affiche une image statique (par exemple une photo du modèle),
ou un jeu d'images alternées en fonction de la valeur d'une source (par
exemple une icône de batterie qui change avec la tension) :

![Configuration du widget Bitmap](../assets/display-widget-bitmap-config.png)
![Type du widget Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — une jauge de batterie dédiée, lisant les données d'un capteur
tel que le FLVSS : tension totale du pack, nombre d'éléments et tension de
chaque élément. Une descente sous le seuil **Low voltage** configuré fait
passer l'affichage en rouge — dans l'exemple ci-dessous, un seuil de 3,3 V
se déclenche sur l'élément le plus bas :

![Configuration du widget LiPo](../assets/display-widget-lipo-config.png)
![Widget LiPo](../assets/display-widget-lipo.png)

**Channels** — jusqu'à 8 voies de sortie sous forme de graphique à barres,
horizontal ou vertical :

![Configuration du widget Channels](../assets/display-widget-channels-config.png)
![Widget Channels](../assets/display-widget-channels.png)

**Line Chart** — trace la valeur d'une source dans le temps, avec remise à
zéro lors d'une réinitialisation de vol :

![Configuration du widget Line Chart](../assets/display-widget-line-chart-config.png)
![Widget Line Chart](../assets/display-widget-line-chart.png)

- **Source** — la valeur tracée.
- **Pause condition** — une source qui met en pause / relance
  l'enregistrement (ou touchez simplement le widget en cours d'exécution,
  si aucune source n'est disponible pour cela).
- **Log period** — intervalle d'échantillonnage ; 500 ms couvre environ
  6 minutes avant défilement, 1 s environ 12 minutes.
- **Inverted** — inverse le graphique verticalement.
- **Auto range** — met automatiquement l'axe vertical à l'échelle des
  données ; désactivé, il utilise des valeurs **Min**/**Max** fixes (par
  exemple une plage constante de −100 % à +100 %).

Toucher un graphique en cours d'exécution fait apparaître
**Pause/resume**, **Reset** (effacer et redémarrer), **Configure widget**,
ou permet d'accéder à **Configure screens** :

![Options du widget Line Chart](../assets/display-widget-line-chart-options.png)

**Text** — affiche le contenu d'un fichier texte Markdown (lu depuis
`documents/user/` — voir le [Gestionnaire de
fichiers](../system-setup/file-manager.md#top-level-folders)) :

![Configuration du widget Text](../assets/display-widget-text-config.png)
![Widget Text](../assets/display-widget-text.png)

**Timer Log** — un journal défilant des valeurs passées d'un chronomètre
choisi, enregistrées à chaque remise à zéro de ce chronomètre (utile pour
suivre l'utilisation des packs de vol au cours d'une session) ;
**Reverse** place l'entrée la plus récente en haut :

![Configuration du widget Timer Log](../assets/display-widget-timer-logs-config.png)
![Widget Timer Log](../assets/display-widget-timer-log.png)

Faites un appui long sur une entrée (ou sur le widget) pour accéder à
**Clear logs**, modifier ou réinitialiser le chronomètre associé, ou
accéder à la configuration du widget ou de l'écran :

![Menu d'une entrée du Timer Log](../assets/display-widget-timer-log-menu.png)

**GPS Map** — trace la position GPS en direct sous forme de trajectoire,
pour les modèles équipés d'un capteur GPS (voir le fil de discussion
*FrSky - ETHOS Lua Script Programming* sur rcgroups, message n° 8854, pour
plus de détails sur ce widget en particulier) :

![Configuration du widget GPS Map](../assets/display-widget-gps-map-config.png)

## Options au niveau de l'écran

Au-delà des widgets individuels, chaque écran possède ses propres réglages
— taille de la grille de disposition, arrière-plan, et écrans inclus dans
le cycle de la touche `PAGE` :

![Options de configuration de l'écran](../assets/display-screen-config-options.png)

Un écran d'accueil entièrement configuré combine plusieurs widgets en une
disposition lisible d'un seul coup d'œil :

![Vue principale](../assets/display-main-view.png)

Voir [Écrans supplémentaires](additional-displays.md) pour ajouter d'autres
écrans au-delà de celui par défaut, et [Widgets
personnalisés](custom-widgets.md) pour les widgets programmés en Lua, au-delà
de l'ensemble intégré.
