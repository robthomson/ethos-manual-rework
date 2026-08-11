---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Sorties

![Sorties](../assets/model-outputs.png)

Les sorties constituent la frontière entre la « logique » pure des [Mixages](mixes.md) et
le monde physique — servos, tringleries, gouvernes, actionneurs,
transducteurs. C'est là que les butées, l'inversion, le centrage et les
courbes de correction sont adaptés aux besoins mécaniques réels du
modèle. Chaque voie de sortie correspond à une sortie servo du récepteur
(CH1 → prise servo n° 1, avec les réglages de protocole par défaut).

Ethos travaille en pourcentages, mais les servos sont en définitive pilotés par
la largeur d'impulsion PWM exprimée en microsecondes :

| % | µs |
|---|---|
| −150 % | 732 |
| −100 % | 988 |
| 0 % | 1500 |
| 100 % | 2012 |
| 150 % | 2268 |

!!! warning
    Une voie **sans mixage actif** délivre le neutre (0 % / 1500 µs) — cela
    inclut une voie dont le ou les seuls mixages sont momentanément inactifs.
    Assurez-vous que chaque voie réellement utilisée dispose toujours d'un
    mixage actif. Sur une voie de gaz en particulier, le neutre correspond à
    **mi-gaz**.

L'écran Sorties affiche deux barres par voie : la barre inférieure (verte) représente
la valeur du mixeur pour cette voie, la barre supérieure (orange) la valeur
après traitement des sorties réellement envoyée au récepteur (en % et en µs).
Les limites Min/Max apparaissent comme des sections grisées de la barre orange. Les voies
qui ne sont pas actuellement transmises au module RF ont un fond plus sombre.
De petites icônes apparaissent sur une voie lorsque ses réglages Direction, Courbe, Ralentissement ou
Équilibrage ont été modifiés par rapport aux valeurs par défaut, afin de repérer d'un coup d'œil les voies
non standard.

!!! tip
    Un appui long sur `ENT` depuis l'écran Mixages ou Phases de vol
    amène directement ici.

## Modification d'une voie

![Modification de la sortie de profondeur](../assets/model-outputs-elevator-edit.png)
![Modification de la sortie des gaz](../assets/model-outputs-throttle-edit.png)

Appuyez sur une voie pour l'ouvrir. Un aperçu en haut de l'écran montre la valeur du mixage
(vert) face à la valeur de sortie (orange), avec un petit repère blanc pour
les points Min/Max.

- **Nom** — modifiable.
- **Direction** — inverse la sortie de la voie, généralement pour inverser
  le sens de rotation du servo. Signalée par une icône à double flèche sur la voie.
  Cela n'affecte **pas** les mixages qui l'alimentent et n'inverse **pas** les
  limites Min/Max.
- **Min/Max** — limites strictes qui ne sont jamais outrepassées — à régler pour éviter
  tout blocage mécanique. Elles font office de réglage de butée/gain : les réduire
  diminue le débattement au lieu de provoquer un écrêtage. La valeur par défaut est ±100 %, réglable
  jusqu'à ±150 %. Pendant le réglage, l'extrémité vers laquelle on se déplace
  est affichée en gras (p. ex. poussez le manche de profondeur vers l'avant et la
  valeur Max s'affiche en gras, pour confirmer qu'il s'agit bien de l'extrémité en cours de réglage).

  ![Avertissement redondance SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Redondance SBUS"
      Une configuration de redondance utilisant SBUS ne peut pas déplacer un servo au-delà d'environ
      ±125 %. Les champs Min/Max eux-mêmes possèdent des plages asymétriques (−150–0 %
      et 0–150 %) — si vous les pilotez depuis une [Variable](variables.md), donnez à cette
      variable une plage identique ou activez **Ignorer la plage** (voir [options de
      source](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      sans quoi la conversion automatique de plage produira des valeurs inattendues. Si
      la sortie du récepteur principal dépasse 125 % et qu'il passe en failsafe, le
      récepteur redondant qui prend le relais via SBUS la ramènera à 125 %.

- **Centre/Subtrim** — décale la sortie, généralement pour centrer un bras
  de servo ; les butées ne sont pas affectées.

  !!! warning
      N'utilisez pas le subtrim pour des décalages importants — il introduit un
      différentiel notable dans la réponse du servo. Utilisez plutôt un **mixage d'offset**
      pour tout ce qui va au-delà d'un centrage fin.

- **Centre PWM** — semblable au subtrim, mais décale la plage de débattement *entière* du servo,
  butées strictes incluses, l'opération étant effectuée dans le servo lui-même
  plutôt qu'affichée sur le moniteur de voies. Cela permet de garder le
  centrage mécanique distinct du trim.
- **Courbe** — associe une courbe Expo ou personnalisée (existante ou nouvelle, avec un
  raccourci **Modifier** une fois définie) pour corriger la réponse réelle — p. ex.
  maintenir un suivi précis entre les volets gauche et droit. Signalée par une icône de courbe sur
  la voie.
- **Ralentissement haut/bas** — ralentit la réponse de la sortie aux variations d'entrée, en
  secondes pour parcourir 0→100 % — p. ex. ralentir un train rentrant entraîné par un servo
  proportionnel ordinaire. Signalé par une icône d'horloge sur la voie. (Un **délai**,
  à distinguer du ralentissement, est disponible dans les [interrupteurs
  logiques](logical-switches.md).)

## Permuter les voies

![Permuter les voies](../assets/model-outputs-swap-channels.png)
![Choix de la voie à permuter](../assets/model-outputs-swap-channels-select.png)

Permute deux voies de sortie. La boîte de dialogue s'ouvre avec la voie courante
pré-renseignée ; choisissez l'autre et confirmez — la permutation est immédiate, et chaque
mixage faisant référence à l'une des deux voies est mis à jour en conséquence.

## Réinitialiser les réglages

![Réinitialiser la voie](../assets/model-outputs-reset-select.png)

Remet tous les paramètres d'une voie à leurs valeurs par défaut — utile avant de
réaffecter une voie à un autre usage, avec une boîte de dialogue de confirmation pour
éviter les fausses manœuvres.

## Équilibrer les voies

![Choix des voies à équilibrer](../assets/model-outputs-balance-choose_channels.png)
![Choix de CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Équilibre une paire (ou jusqu'à 4) de voies afin qu'elles se déplacent de façon synchrone — p. ex.
des volets qui ne bougent pas ensemble peuvent induire un roulis indésirable ; des gaz
déséquilibrés sur un modèle multimoteur peuvent induire un lacet indésirable. Ethos crée une
courbe d'équilibrage différentielle pour chaque voie sélectionnée ; en comparant la position physique
des gouvernes à chaque point de la courbe, vous pouvez les ajuster pour les faire correspondre,
jusqu'à obtenir des gouvernes parfaitement synchrones.

**Avant l'équilibrage**, dans l'ordre :

1. Réglez le sens des servos pour un débattement correct.
2. Avec les mixages au neutre, utilisez éventuellement le **Centre PWM** pour aligner les
   palonniers de servo.
3. Réglez Min/Max et le Subtrim.
4. Configurez toutes les autres courbes.
5. Configurez le Ralentissement.
6. *Ensuite* seulement, équilibrez et harmonisez sur toute la plage de débattement.

**Utilisation** : choisissez les voies à équilibrer et l'ordre dans lequel les
afficher —

![CH7/CH6 sélectionnées](../assets/model-outputs-balance-ch7-and-ch6.png)

— la sortie du mixage sur l'axe X, le différentiel d'ajustement d'équilibrage sur l'axe
Y. Appuyez sur le graphique d'une voie (ou sélectionnez-la et appuyez sur `ENT`) pour modifier sa
courbe d'équilibrage ; `PAGE` permet de passer d'une voie à l'autre en cours d'édition :

![Éditeur de courbe d'équilibrage](../assets/model-outputs-balance-curve-edit.png)

Commandes de l'éditeur :

- **Source** — normalement la ou les sources propres du mixage, ou toute autre entrée
  analogique commode ; **Entrée analogique auto** retient comme axe X le premier manche/curseur/potentiomètre
  que vous déplacez, à la fois dans le graphique et dans le modèle lui-même.
- **Aimant** — aligne automatiquement le réglage de l'encodeur rotatif sur le point de courbe
  le plus proche sur l'axe X :

  ![Aimant désactivé](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Aimant activé](../assets/model-outputs-balance-ch6-magnet-on.png)

  L'entrée doit malgré tout être déplacée pour aligner X sur un point de courbe avant
  de pouvoir l'ajuster.
- **Verrou** — activé en appuyant sur son icône ou sur `ENT` en mode d'édition du graphique ;
  verrouille toutes les entrées afin de pouvoir relâcher le manche et observer les
  gouvernes pendant l'ajustement de la courbe.
- **Configuration** — modifie le nombre de points par voie (toutes ensemble ou individuellement)
  et le lissage éventuel de chaque courbe.
- **Aide** (`?`, également la touche `MDL`) — ouvre l'aide intégrée.

**Multivoies** : jusqu'à 4 voies peuvent être équilibrées ensemble —

![Équilibrage sur 4 voies](../assets/model-outputs-balance-ch2-9-8-1.png)

Une fois définie, une courbe d'équilibrage peut être consultée, modifiée ou effacée depuis la
page de configuration de la voie elle-même — une icône d'équilibrage la signale sur le graphique de la voie
(aux côtés d'une icône Direction également, si celle-ci n'est pas non plus à sa valeur par défaut).
