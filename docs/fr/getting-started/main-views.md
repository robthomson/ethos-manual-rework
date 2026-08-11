---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Vues principales

## Écran d'accueil

![Écran d'accueil](../assets/mainview.png)

L'écran d'accueil est ce que vous voyez lorsqu'aucun menu n'est ouvert —
un empilement pouvant aller jusqu'à **huit** écrans que vous configurez
vous-même (voir [Écrans](../displays/index.md)), auxquels on accède en
faisant glisser le doigt ou avec la touche `PAGE`. Un modèle fraîchement
créé démarre avec un seul écran affichant une image du modèle, trois
widgets de chronomètre, ainsi que les indicateurs de trims et de
potentiomètres ; tout y est configurable par l'utilisateur.

Les écrans partagent normalement les barres supérieure et inférieure
décrites ci-dessous, mais un écran peut aussi être configuré en plein
écran, masquant les deux.

## La barre supérieure

La barre supérieure affiche le nom du modèle à gauche (ainsi que la phase
de vol active, si elle est configurée), et une rangée d'icônes d'état à
droite :

- Enregistrement de données actif
- État du formateur (maître ou élève, selon le cas)
- RSSI — liaison 2,4 GHz
- RSSI — liaison 900 MHz (si un module bi-bande / longue portée est
  installé)
- Volume du haut-parleur
- État de la batterie radio

Toucher l'icône du haut-parleur ou de la batterie ouvre directement le
panneau de réglage correspondant, [Général](../system-setup/general.md)
(audio) ou [Batterie](../system-setup/battery.md).

### Avertissement d'erreur

Un triangle rouge apparaît dans la barre supérieure lorsque Ethos détecte
une erreur — une erreur de script Lua, une erreur de sauvegarde RAM, ou
l'utilisation d'une version de firmware nightly/instable en sont les
causes courantes. Le détail de l'avertissement se trouve toujours dans
**Système → Info**, sur la même page que le temps d'utilisation radio et
les [journaux d'erreurs](../system-setup/information.md).

## La barre inférieure

![Barre inférieure](../assets/bottombar.png)

Quatre onglets sont disposés en bas pour les sections principales —
**Accueil**, **Configuration du modèle**, **Configurer les écrans**,
**Configuration du système** — avec l'horloge système à droite (la
toucher ouvre directement [Date et
heure](../system-setup/date-and-time.md)).

## La zone des widgets

Le centre de chaque écran est rempli de **widgets** : image du modèle,
chronomètres, valeurs de télémétrie, barres de trims/potentiomètres, et
plus encore, tous placés et configurés par vos soins. Voir
[Écrans](../displays/index.md) pour ajouter, déplacer et configurer des
widgets, et [Écrans supplémentaires](../displays/additional-displays.md)
pour ajouter d'autres écrans au-delà de celui par défaut.
