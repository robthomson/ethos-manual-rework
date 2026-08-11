---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Vues principales

## Écran d'accueil

![Écran d'accueil](../assets/mainview.png)

L'écran d'accueil est ce que vous voyez lorsqu'aucun menu n'est ouvert — un empilement de **huit** écrans d'affichage au maximum, que vous configurez vous-même (voir [Écrans](../displays/index.md)), entre lesquels on navigue avec la touche `PAGE` ou par un balayage tactile. Un modèle nouvellement créé ne comporte qu'un seul écran, affichant une image du modèle, trois widgets de chronomètre et les indicateurs de trims/potentiomètres ; tout ce qui s'y trouve est ensuite configurable par l'utilisateur.

Les écrans partagent normalement les barres supérieure et inférieure décrites ci-dessous, mais un écran peut aussi être réglé en plein écran, ce qui masque les deux barres.

## La barre supérieure

La barre supérieure affiche le nom du modèle à gauche (ainsi que la phase de vol active, si une phase est configurée), et une rangée d'icônes d'état à droite :

- Enregistrement des données actif
- État de l'écolage (maître ou élève, selon le cas)
- RSSI — liaison 2,4 GHz
- RSSI — liaison 900 MHz (si un module double bande / longue portée est installé)
- Volume du haut-parleur
- État de la batterie de la radio

Toucher l'icône du haut-parleur ou de la batterie ouvre directement le panneau de réglages correspondant : [Général](../system-setup/general.md) (audio) ou [Batterie](../system-setup/battery.md).

### Avertissement d'erreur

Un triangle rouge apparaît dans la barre supérieure dès qu'Ethos détecte une erreur — une erreur de script Lua, une erreur de sauvegarde de la RAM, ou l'utilisation d'une version de firmware nightly/instable en sont les causes les plus fréquentes. Le détail de l'avertissement se trouve toujours dans **System → Info**, sur la même page que la durée de fonctionnement de la radio et les [journaux d'erreurs](../system-setup/information.md).

## La barre inférieure

![Barre inférieure](../assets/bottombar.png)

Quatre onglets sont alignés en bas de l'écran pour les sections principales — **Accueil**, **Configuration du modèle**, **Configurer les écrans**, **Configuration du système** — avec l'horloge du système à droite (touchez-la pour accéder directement à [Date et heure](../system-setup/date-and-time.md)).

## La zone des widgets

Le milieu de chaque écran est occupé par des **widgets** : image du modèle, chronomètres, affichages de télémétrie, barres de trims/potentiomètres, et bien d'autres, tous placés et configurés par vous. Voir [Écrans](../displays/index.md) pour savoir comment ajouter, déplacer et configurer les widgets, et [Écrans supplémentaires](../displays/additional-displays.md) pour ajouter d'autres écrans au-delà de l'écran unique par défaut.
