---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Exemple de base : aile volante (elevons)

Une aile volante à 2 servos en elevons, en prenant comme exemple concret
les débattements/Expo/proportions de mixage recommandés pour la
Dreamflight Weasel. Effectuez d'abord la [configuration initiale de la
radio](initial-radio-setup.md).

## Étape 1. Vérifier les réglages système {: #step-1-confirm-system-settings }

Ordre **AETR** par défaut, avec **[Quatre premières voies
fixes](../system-setup/controls.md#first-four-channels-fixed)** sur
**OFF**. Enregistrez (si ACCESS) et appairez le récepteur via le
[système RF](../model-setup/rf-system.md) avant de continuer.

## Étape 2. Identifier les servos/voies nécessaires

Sur une cellule à elevons, les [mixages](../model-setup/mixes.md)
combinent les commandes d'ailerons et de profondeur sur les deux
surfaces physiques — soit seulement 2 voies au total, chacune étant un
mélange des deux commandes.

## Étape 3. Créer un nouveau modèle

![Créer un modèle d'avion](../assets/tut-wing-eg-wiz-create-airplane.png)

Depuis [Choix du modèle](../model-setup/model-select.md), lancez
l'assistant **Avion** et choisissez **Récepteur non stabilisé**.

![Sans moteur](../assets/tut-wing-eg-wiz-no-engine.png)

Sélectionnez **Sans moteur**, acceptez les 2 voies d'ailerons proposées
par défaut, puis sélectionnez **Sans volets**.

![Sans empennage](../assets/tut-wing-eg-wiz-no-tail.png)

Sélectionnez **Aucun** comme type d'empennage — c'est ce qui amène Ethos
à construire automatiquement le mixage elevons (commandes ailerons +
profondeur, toutes deux sur les mêmes deux voies). Nommez le modèle (par
exemple « Weasel »), choisissez une image, puis terminez — il devient le
modèle actif dans la catégorie Avion.

## Étape 4. Vérifier et configurer les mixages

![Vue d'ensemble des mixages](../assets/tut-wing-eg-mixes.png)

L'assistant crée un mixage Ailerons sur les voies 1+2, suivi d'un mixage
Profondeur *également* sur les voies 1+2 — les deux commandes agissent
sur les deux voies d'elevons, ce qui constitue tout l'art du mixage
elevons.

### Ailerons

![Mixage ailerons](../assets/tut-wing-eg-mixes-ail-mix.png)

**Poids/Débattements** — d'après le manuel de la Weasel, le débattement
des ailerons doit valoir environ 3× celui de la profondeur, et les deux
doivent totaliser 100 % : **75 %** ailerons, **25 %** profondeur. Les
petits débattements représentent environ la moitié des grands : **36 %**
ailerons en petit débattement, **12 %** profondeur en petit débattement.

![Poids du mixage ailerons](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — valeurs recommandées pour la Weasel : 35 % en grand
débattement / 20 % en petit, actives interrupteur SB en bas, ce qui
adoucit la réponse autour du neutre du manche.

**Différentiel** — faible sur cette cellule, environ **4 %** :

![Différentiel d'ailerons](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(Voir l'[exemple de base pour aile
fixe](basic-fixed-wing.md#ailerons) pour comprendre l'utilité du
différentiel — le même raisonnement sur le lacet inverse s'applique ici.)

### Profondeur

![Mixage profondeur](../assets/tut-wing-eg-mixes-ele-mix.png)

Même principe : débattements **25 %**/**12 %** grand/petit, avec les
mêmes valeurs d'Expo que pour les ailerons.

### Dérive

![Mixage dérive](../assets/tut-wing-eg-mixes-rud-mix.png)

La Weasel n'en a pas — les ailes volantes n'en nécessitent généralement
pas. Lorsqu'une dérive *est* nécessaire sur un modèle à elevons,
ajoutez-la comme [mixage libre](../model-setup/mixes.md#mix-libraries)
sur la voie 3.

## Étape 5. Appairer le récepteur

Comme à l'[étape 1](#step-1-confirm-system-settings) — enregistrez et
appairez avant de continuer, et envisagez de débrancher les liaisons des
servos ou de réduire les courses jusqu'à ce que les limites Min/Max
soient réglées, afin de ne rien forcer.

## Étape 6. Vérifier les mixages

Les voies de sortie 1/2 peuvent être renommées **Elevon1**/**Elevon2**.
Avec les ailerons à fond à droite, la voie 1 (droite, montante) indique
75 %, tandis que la voie 2 (gauche, descendante) indique 72 % — les 3 %
d'écart *sont* l'effet du différentiel. Ajoutez par-dessus la profondeur
à piquer à fond et la voie 1 devient 75+25 = 100 %, la voie 2 devient
72−25 = 47 %.

## Étape 7. Configurer les débattements maximaux des servos

![Ailerons à fond](../assets/tut-wing-eg-outputs-full-ail.png)
![Ailerons à fond + profondeur à fond](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Centrez d'abord chaque servo avec **PWM center**. Le débattement maximal
recommandé pour la Weasel est de 25 mm d'ailerons + 10 mm de profondeur,
soit 35 mm cumulés — appliquez les commandes ailerons/profondeur à fond
en addition *et* à fond en opposition, et vérifiez que ni les limites
mécaniques ni celles des servos ne sont dépassées avant de fixer les
débattements définitifs.

- **Min/Max** — limites strictes, jamais outrepassées ; les réduire
  diminue le débattement au lieu de l'écrêter. Par défaut ±100 %,
  extensible à ±150 % si nécessaire.
- **Courbe** — souvent plus rapide et plus souple que de jongler
  directement avec Min/Max/Subtrim, avec en plus l'avantage d'un
  graphique en direct. Une courbe à 3 points convient à la plupart des
  sorties ; une courbe à 5 points sur le second elevon permet de
  synchroniser facilement la course en 5 points avec celle du premier.
  Lorsque vous utilisez une courbe à cette fin, laissez Min/Max/Subtrim
  à leurs valeurs neutres (−100/100/0, ou −150/150/0 avec les limites
  étendues) et laissez la courbe assurer la mise en forme.
