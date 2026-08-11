---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Exemple de base pour aile fixe

Un déroulé complet pour un avion moteur + 2 ailerons + 2 volets +
profondeur + dérive, avec un servo par surface, réalisé de bout en bout
avec l'assistant. Effectuez d'abord la
[Configuration initiale de la radio](initial-radio-setup.md).

## Étape 1. Vérifier les réglages système

Cet exemple utilise l'ordre des voies **AETR** par défaut.

## Étape 2. Identifier les servos/voies nécessaires

Les [Mixages](../model-setup/mixes.md) sont le cœur de la radio — jusqu'à
100 voies de mixage, les numéros les plus bas étant normalement attribués
aux servos (puisque les numéros de voies correspondent directement aux
voies du récepteur ; le module RF interne du X20 prend en charge jusqu'à
24 voies de sortie). Les voies supérieures restent disponibles pour des
voies virtuelles ou des voies réelles supplémentaires via plusieurs
modules RF et le SBUS. Notre cellule :

| Fonction | Voies |
|---|---|
| Moteur | 1 |
| Ailerons | 2 |
| Volets | 2 |
| Profondeur | 1 |
| Dérive | 1 |

(Le train rentrant est ajouté plus tard, à l'[Étape 10](#step-10-add-a-mix-for-retracts).)

## Étape 3. Créer un nouveau modèle

![Créer un modèle d'avion](../assets/tut-fw-eg-wiz-create-airplane.png)

Depuis [Choix du modèle](../model-setup/model-select.md), sélectionnez une
catégorie, appuyez sur **+** et lancez l'assistant **Avion**. Choisissez
**Récepteur non stabilisé** pour cet exemple.

![Voies moteur](../assets/tut-fw-eg-wiz-engine.png)
![Voies ailerons/volets](../assets/tut-fw-eg-wiz-ail-flaps.png)

Acceptez 1 voie moteur, puis 2 voies d'ailerons et sélectionnez 2 voies de
volets.

![Type d'empennage](../assets/tut-fw-eg-wiz-tail.png)
![Voies profondeur/dérive](../assets/tut-fw-eg-wiz-ele-rudd.png)

Acceptez l'**empennage traditionnel** par défaut, avec 1 voie de
profondeur et 1 voie de dérive.

![Nom du modèle](../assets/tut-fw-eg-wiz-name.png)
![Récepteur](../assets/tut-fw-eg-wiz-rx.png)

Nommez-le (par exemple « FWexample » — jusqu'à 15 caractères), terminez
l'assistant : il devient le modèle actif, créé dans la catégorie Avion.

## Étape 4. Vérifier et configurer les mixages

![Vue d'ensemble des mixages](../assets/tut-fw-eg-mixes.png)

L'assistant a déjà créé les mixages d'ailerons (voies 1 et 5), de
profondeur, de gaz, de dérive et de volets (les volets affichent `---` —
aucune source attribuée pour l'instant).

### Ailerons

![Mixage ailerons](../assets/tut-fw-eg-mixes-ail-mix.png)
![Modifier le mixage ailerons](../assets/tut-fw-eg-mixes-ail-edit.png)

**Course/Débattements** — réglez les débattements avant de faire voler
quelque chose de neuf : un débattement modéré (par exemple 30 %) convient
au vol sportif, 100 % convient à la 3D. Ajoutez un débattement de 60 %
pour l'interrupteur SB en position milieu, et de 30 % pour SB en bas — la
valeur par défaut (SB en haut) reste à 100 % :

![Débattements de course](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo** — une réponse linéaire peut sembler nerveuse autour du neutre ;
ajoutez des valeurs d'Expo (par exemple 60 %/40 %/20 % sur les mêmes
positions de SB) pour aplatir la réponse près du neutre sans réduire le
débattement maximal :

![Valeurs d'Expo](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Différentiel** — un débattement d'aileron identique vers le haut et vers
le bas génère plus de traînée sur l'aileron qui descend que sur celui qui
monte, ce qui fait lacet le modèle à l'opposé du virage (« lacet
inverse »). Un différentiel positif (50 % est courant) réduit le
débattement vers le bas par rapport à celui vers le haut pour compenser ce
phénomène :

![Différentiel de 50 %](../assets/tut-fw-eg-mixes-ail-diff-50.png)

Pour régler le différentiel en vol, faites un appui long sur `ENT` sur la
valeur, choisissez **Utiliser une source** et sélectionnez Pot1 :

![Utiliser une source](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![Pot1 sélectionné](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

Lorsque la valeur trouvée en vol vous satisfait, faites de nouveau un
appui long et choisissez **Convertir en valeur** pour la fixer
définitivement :

![Convertir en valeur](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim** — permet de déconnecter ce mixage de son trim associé sans
désactiver le trim lui-même, ce qui le libère pour un autre usage :

![Trim des ailerons](../assets/tut-fw-eg-mixes-ail-trim.png)

### Profondeur et dérive

Le même schéma triple débattement + Expo, ici sur l'interrupteur SC :

![Valeurs d'Expo de la profondeur](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### Gaz

![Mixage des gaz](../assets/tut-fw-eg-mixes-thr-edit.png)

Laissez l'entrée sur le manche des gaz — aucun débattement ni Expo n'est
nécessaire — mais un interrupteur de sécurité est indispensable ; un moteur
thermique ou électrique qui démarre à l'improviste peut provoquer des
blessures graves.

**Trim en position basse** (moteurs thermiques/essence) — règle le régime
de ralenti indépendamment du plein gaz :

![Trim en position basse](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

Lorsqu'il est activé, la voie des gaz se situe à −75 % avec le manche au
ralenti ; le levier de trim des gaz ajuste alors le ralenti entre −100 % et
−50 %.

**Coupure gaz** — un verrou de sécurité. Avec l'interrupteur SA en bas
comme condition active (affichée en gras lorsqu'elle est active), la sortie
des gaz reste à −100 % dès que le manche descend sous −85 % :

![Coupure gaz](../assets/tut-fw-eg-mixes-thr-cut.png)

Avec l'option **Sticky** activée à la place, les gaz sont coupés à
l'**instant** où SA passe en bas, quelle que soit la position du manche :

![Coupure gaz Sticky](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

Dans les deux cas, une fois la condition active levée, le manche doit être
ramené sous −85 % avant que les gaz puissent remonter — ce qui évite que
le moteur ne saute à une position de gaz élevée au moment où
l'interrupteur de coupure est relâché.

**Maintien gaz** — une coupure d'urgence depuis *n'importe quelle*
position de manche, qui ramène la sortie directement à −100 % (ou à une
valeur configurée) dès que sa condition est remplie :

![Maintien gaz](../assets/tut-fw-eg-mixes-thr-hold.png)

### Volets

![Entrée des volets](../assets/tut-fw-eg-mixes-flaps-input.png)

Attribuez les volets à l'interrupteur SE et réglez la course des deux
voies de sortie à 100 % :

![Courses des volets](../assets/tut-fw-eg-mixes-flaps-weights.png)

## Étape 5. Appairer le récepteur

Enregistrez (si ACCESS) et appairez via
[Système RF](../model-setup/rf-system.md). Avant de passer aux Sorties,
envisagez de débrancher les commandes des servos ou de réduire
temporairement leur débattement, afin d'éviter de forcer sur la mécanique
pendant le réglage des limites Min/Max.

## Étape 6. Configurer les sorties

![Sorties](../assets/tut-fw-eg-outputs.png)

Les [Sorties](../model-setup/outputs.md) adaptent la logique du mixeur à
la mécanique réelle du modèle.

**Aileron 1** — centrez le servo avec **Centre PWM** après avoir optimisé
la liaison mécanique, puis réglez **Min**/**Max**. Attribuer temporairement
un potentiomètre à Min (puis à Max, de la même manière que dans l'exemple
du différentiel ci-dessus) permet de faire ce réglage plus rapidement :

![Modifier la sortie de l'aileron](../assets/tut-fw-eg-outputs-edit-ail.png)

**Volets** — les volets nécessitent généralement un fort débattement vers
le bas pour un freinage efficace ; on sacrifie une partie de la course
vers le haut dans la liaison mécanique pour l'obtenir, de sorte que le
volet se trouve à mi-course vers le bas lorsque le servo est au neutre, puis
on utilise Min/Max pour définir les positions réelles haute et pleine
descente. Une courbe à 5 points est une méthode courante pour corriger tout
écart de concordance entre volets et ailerons qui en résulterait. Terminez
avec **[Équilibrage des voies](../model-setup/outputs.md#balance-channels)**
pour synchroniser les ailerons et les volets gauche/droite.

## Étape 7. Introduction aux phases de vol

Les [Phases de vol](../model-setup/flight-modes.md) permettent à un modèle
de disposer de réglages propres à chaque tâche — comme changer de vitesse.
Sur les 20 disponibles, cet exemple en utilise trois : **Default**,
**Flaps Half** (interrupteur SE au milieu) et **Flaps Full** (SE en haut).
La première phase de vol dont la condition est vraie est active ; la phase
**Default** n'a aucune condition et prend le relais dès qu'aucune autre ne
s'applique — c'est pourquoi elle n'offre pas d'option de sélection
d'interrupteur. Un fondu d'entrée/sortie de 1 seconde adoucit la transition
lors du déploiement des volets.

## Étape 8. Configurer les trims

Deux façons de gérer un trim de profondeur variant selon la position des
volets :

**Trims indépendants par phase de vol** — l'option la plus simple : le
trim de profondeur devient totalement indépendant pour chaque phase de vol
et commute automatiquement au déplacement de SE. Comme chaque phase se
trime à partir de zéro, le [Trim instantané](../model-setup/trims.md#instant-trim)
est utile — trimez d'abord pour le vol normal, puis atterrissez et utilisez
ce réglage comme point de départ pour les phases avec volets.

**Trim de base avec offset** — on trime une seule fois en Default, la
compensation de profondeur de chaque phase de volets venant s'y superposer
comme un offset :

1. Réglez le **Pas** de trim sur Medium (pour un trimage initial plus
   rapide ; réduisez-le ensuite pour l'ajustement fin), le **Mode** sur
   Custom, puis ajoutez un nouveau comportement.
2. **Condition active** : `FM1(Flaps Half)`, mode **Offset + Default** — le
   trim de la phase Flaps Half devient le trim de base plus l'offset réglé
   pendant que cette phase est active :

   ![Ajouter un comportement](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default, FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. Répétez l'opération pour `FM2(Flaps Full)` :

   ![Sélectionner la phase de vol](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default, FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

Chaque phase avec volets peut désormais être trimée indépendamment, mais
une modification ultérieure du trim de base Default (par exemple pour
corriger une dérive thermique des servos) décale automatiquement les trims
des deux phases avec volets de la même valeur.

![Sélection du trim personnalisé](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## Étape 9. Configurer un chronomètre de batterie de vol

Dans [Chronos](../model-setup/timers.md), modifiez le Chronomètre 1 : mode
**Down**, valeur de départ de 5 minutes, fonctionnant dès que **Gaz
actifs** est vrai (et qu'il n'est pas maintenu en remise à zéro).
Éventuellement, attribuez une source de cadence proportionnelle (par
exemple le manche des gaz) afin que le chronomètre s'écoule en temps réel
à plein gaz et ralentisse lorsque les gaz sont réduits.

## Étape 10. Ajouter un mixage pour le train rentrant

![Source du mixage du train rentrant](../assets/tut-fw-eg-retracts-source.png)

Appuyez sur un mixage, **Ajouter un mixage** → **Mixage libre**, nommez-le
« Retracts », réglez la condition sur Always et la source sur
l'interrupteur SF. L'action par défaut avec Course = 100 % convient — cela
attribue par exemple la voie 8 au train rentrant :

![Sortie du train rentrant](../assets/tut-fw-eg-retracts-outputs.png)
