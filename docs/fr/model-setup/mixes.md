---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Mixages

![Icône Mixages](../assets/model-icon-mixes.png)

Les mixages sont le cœur de la programmation d'un modèle dans Ethos —
c'est ici que les entrées (manches, interrupteurs, capteurs, tout ce
qu'une [source](../getting-started/user-interface-and-navigation.md#choosing-a-source)
peut atteindre) sont acheminées, mises en forme et combinées vers les
voies de sortie. Jusqu'à 120 mixages peuvent être définis par modèle.

![Table des mixages](../assets/model-mixes.png)

Si un modèle a été créé avec l'assistant **Choix du modèle**, ses
mixages de base (ailerons, profondeur, gaz, dérive, et tout ce dont la
cellule a besoin) sont déjà présents ici. Sélectionner un mixage et
appuyer sur `ENT` ouvre un menu contextuel permettant de le modifier,
d'ajouter un nouveau mixage, de basculer vers la [vue par
voie](#per-channel-view), de le réordonner, de le dupliquer, ou de le
supprimer. Les mixages inactifs apparaissent grisés, et la suppression
d'un mixage demande toujours une confirmation au préalable.

## Anatomie d'un mixage {: #anatomy-of-a-mix }

Chaque mixage partage le même ensemble de champs, quelle que soit la
catégorie dont il provient. Le mixage **ailerons** sert d'exemple
représentatif — les mixages profondeur et dérive sont organisés de
manière identique.

![Mixage ailerons](../assets/model-mixes-ail-edit.png)

![Éditeur de mixage ailerons](../assets/model-mixes-ail.png)

**Nom** — reprend par défaut le type de mixage, modifiable.

**Condition** — vaut *Toujours* par défaut. Peut être restreinte à une
position d'interrupteur, un interrupteur de fonction, un interrupteur
logique, une phase de vol, un événement système (coupure/maintien gaz),
ou une position de trim, auquel cas le mixage ne s'applique que tant que
la condition est vraie.

**Phases de vol** — si des phases de vol sont définies, le mixage peut
en plus être restreint à une ou plusieurs d'entre elles.

**Courbe** — une courbe **Expo** est disponible par défaut (0 =
linéaire ; une valeur positive adoucit la réponse autour du centre, une
valeur négative l'accentue) :

![Courbe Expo](../assets/model-mixes-ail-expo.png)

Toute courbe préalablement définie dans [Courbes](curves.md) peut être
sélectionnée à la place. Jusqu'à 6 courbes peuvent être empilées sur un
même mixage, chacune avec sa propre condition — si plusieurs conditions
sont vraies simultanément, la courbe la plus haute dans la liste
l'emporte. Les courbes s'appliquent **avant** les taux.

**Taux** — une ou plusieurs lignes de débattement, chacune
optionnellement conditionnée par un interrupteur, un interrupteur de
fonction, un interrupteur logique, une position de trim ou une phase de
vol. La première ligne est celle par défaut, active dès qu'aucune autre
condition n'est remplie :

![Taux ailerons](../assets/model-mixes-ail-weight.png)

Plutôt qu'un pourcentage fixe, un taux peut être piloté par une
[source](../getting-started/user-interface-and-navigation.md#choosing-a-source)
— par exemple un potentiomètre, pour ajuster le taux en vol :

![Taux piloté par une source](../assets/model-mixes-ail-diff.png)

**Différentiel** (-100 à 100, par défaut 0) — donne plus de débattement
dans une direction que dans l'autre. Pour les ailerons, c'est la
technique classique consistant à donner plus de débattement vers le
haut que vers le bas pour réduire le lacet inverse. Affiché uniquement
lorsque le mixage a plus d'une voie de sortie ; le différentiel n'a de
sens que pour une configuration de sortie en V ou à double aileron.

**Nombre de voies / sorties** — combien de voies de sortie ce mixage
pilote et vers quelles sorties physiques elles sont associées :

![Nombre de voies](../assets/model-mixes-ail-ch-count.png)

Un appui long sur `ENT` sur une voie de sortie ailleurs dans
l'interface (par ex. dans [Sorties](outputs.md)) ramène directement à
cette page.

## Le mixage des gaz

Le mixage des gaz est un mixage de type ailerons/profondeur/dérive
auquel s'ajoutent des options de sécurité spécifiques au moteur.

![Mixage gaz](../assets/model-mixes-thr.png)

**Entrée** — la source des gaz, normalement le manche des gaz mais
remplaçable par un potentiomètre, un curseur, un interrupteur, un trim,
une voie, un axe gyroscopique, une voie élève, un chronomètre, ou toute
autre source.

**Trim ralenti** — pour les moteurs thermiques, permet à un trim dédié
d'ajuster le régime de ralenti sans toucher à la position pleins gaz.
Avec le trim ralenti activé, la voie des gaz se positionne à -75 %
lorsque le manche est au ralenti, et le trim des gaz ajuste alors le
ralenti entre -100 % et -50 % :

![Menu trim ralenti](../assets/model-mixes-thr-trim-menu.png)

![Trim ralenti en position basse](../assets/model-mixes-thr-trim-low-position.png)

**Coupure gaz** — un verrou de sécurité matériel : la voie n'est active
qu'une fois que le manche des gaz est passé par le ralenti, de sorte
qu'un actionnement accidentel de l'interrupteur ne puisse pas faire
démarrer le moteur depuis une position pleins gaz :

![Coupure gaz](../assets/model-mixes-thr-cut.png)

**Maintien gaz** — maintient la voie à une valeur fixe quelle que soit
la position du manche, sans le verrou de sécurité qu'offre la coupure
gaz :

![Maintien gaz](../assets/model-mixes-thr-hold.png)

Les gaz disposent également de leur propre réglage de nombre de voies
de sortie, comme tout autre mixage :

![Nombre de voies gaz](../assets/model-mixes-thr-ch-count.png)

!!! note "Verrouillage des gaz"
    Ethos exige que l'entrée du mixage des gaz passe par -100 % avant
    d'armer, quels que soient les réglages de coupure/maintien gaz — un
    modèle créé par l'assistant Choix du modèle en tient déjà compte,
    mais un mixage des gaz construit manuellement doit également le
    respecter.

## Bibliothèques de mixages {: #mix-libraries }

La bibliothèque de mixages prédéfinis de la boîte de dialogue **Ajouter
un mixage** est adaptée à la catégorie de modèle choisie à sa création
— avion, planeur, hélicoptère et multirotor proposent chacun un
ensemble différent :

![Bibliothèque de mixages avion](../assets/model-mixes-library-airplane.png)

![Bibliothèque de mixages planeur](../assets/model-mixes-library-glider.png)

![Bibliothèque de mixages hélicoptère](../assets/model-mixes-library-heli.png)

![Bibliothèque de mixages multirotor](../assets/model-mixes-library-multirotor.png)

Chaque bibliothèque comprend également le **Mixage libre** — un type de
mixage polyvalent sans entrée/sortie prédéfinie, plus flexible que les
mixages spécialisés mais demandant davantage de configuration pour
obtenir le même résultat.

## Vue par voie {: #per-channel-view }

Avec suffisamment de mixages empilés sur une même sortie, il peut
devenir difficile de percevoir leur effet combiné dans le tableau plat
ci-dessus. Sélectionner un mixage et choisir **Afficher par voie**
regroupe alors tous les mixages affectant une même sortie :

![Basculer vers la vue par voie](../assets/model-mixes-chview-select.png)

![Voie repliée](../assets/model-mixes-chview-collapsed.png)

![Voie profondeur développée](../assets/model-mixes-chview-elevator.png)

Développer la ligne récapitulative d'une voie montre chaque mixage y
contribuant, avec sa sortie numérique et graphique en direct — utile
pour vérifier précisément la contribution d'un mixage secondaire (par
ex. une compensation volets→profondeur) par rapport à l'entrée manche
principale :

![Détail de la vue par voie profondeur](../assets/model-mixes-chview-elevator-channel.png)

![Voie profondeur, mixage en surbrillance](../assets/model-mixes-chview-elevator-channel-view.png)

Sélectionner un sous-mixage plutôt que la ligne récapitulative ouvre le
même menu contextuel que la vue tableau (modifier, revenir à la vue
tableau, supprimer) :

![Retour à la vue tableau depuis la vue par voie](../assets/model-mixes-chview-table-view-select.png)

![Retour à la vue tableau](../assets/model-mixes-chview-back-at-mixes-view.png)
