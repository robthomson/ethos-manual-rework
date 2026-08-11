---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Phases de vol

![Phases de vol](../assets/model-fm.png)

Les phases de vol permettent à un interrupteur de sélectionner différents
comportements pour un même modèle — un planeur pourra utiliser Lancement/
Croisière/Vitesse/Thermique, un avion motorisé Normal/Décollage/
Atterrissage, un hélicoptère Normal (montée en régime, décollage/
atterrissage) / Idle Up 1 (voltige) / Idle Up 2 (3D). Elles déchargent le
pilote de l'essentiel des manipulations d'interrupteurs et des retrims :
une phase de vol peut disposer de ses propres trims indépendants et peut
conditionner à la fois les [Variables](variables.md) et les
[Mixages](mixes.md) — combinés, cela suffit à gérer une réelle complexité.
Voir l'[Exemple de base pour aile
fixe](../tutorials/basic-fixed-wing.md) pour une mise en œuvre des phases
de vol sur un modèle réel.

Aucune phase de vol n'est définie par défaut. Appuyez sur la phase de vol
par défaut et choisissez **Modifier** pour la renommer, ou **Ajouter**
pour en créer une nouvelle — jusqu'à 20 au total.

## Nom

Un nom descriptif — Croisière, Vitesse, Thermique, Décollage, Atterrissage,
ce qui convient.

## Condition d'activation

![Formulaire de phase de vol](../assets/model-fm-form.png)

Une nouvelle phase de vol est inactive au départ (`---`). Une fois
définie, elle peut être pilotée par la position d'un interrupteur ou d'un
bouton, un interrupteur de fonction, un interrupteur logique, un événement
système (coupure gaz/maintien gaz) ou la position d'un trim.

La phase de vol **par défaut** n'a aucune condition d'activation — c'est
celle qui est active dès lors que la condition d'aucune autre phase de vol
n'est vraie. Une seule phase de vol est active à la fois : la première (par
ordre de priorité) dont la condition est actuellement vraie. La phase
active est affichée en gras.

!!! warning "Ajout d'une phase de vol à un modèle existant"
    Une phase de vol nouvellement ajoutée est, par défaut, active dans
    chaque mixage déjà dépendant des phases de vol — vérifiez que chacun
    de ces mixages se comporte toujours correctement, en particulier un
    mixage **Lock** verrouillant une voie sur une phase de vol donnée.

## Fondu entrant, sortant

Temps de transition permettant un passage progressif d'une phase de vol à
l'autre (par exemple 1 seconde dans chaque sens) — cela n'a d'effet que
sur les mixages eux-mêmes dépendants des phases de vol.

## Gestion des phases de vol

![Déplacer une phase de vol](../assets/model-fm-move.png)
![Sélection pour le déplacement](../assets/model-fm-move-select.png)
![Phases 0-3](../assets/model-fm-0to3.png)

Appuyez sur une phase de vol pour **Modifier**, **Ajouter**, **Cloner** ou
**Supprimer**. Une phase de vol **clonée** hérite des réglages de sa phase
d'origine dans chaque mixage utilisant les phases de vol — même
comportement, même état actif/inactif — c'est pourquoi un clone est ajouté
par défaut en dernière position, afin de ne pas interférer avec les phases
existantes. **Déplacer** modifie la priorité d'une phase de vol : la
priorité s'applique par ordre croissant et (comme indiqué ci-dessus) la
première dont la condition est vraie est celle qui est active.
