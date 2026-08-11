---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Choix du modèle

![Assistant de création - avion](../assets/model-modelselect-model-wizard-airplane.png)

Permet de créer, sélectionner, cloner et supprimer des modèles, et de gérer les
dossiers de catégories définis par l'utilisateur dans lesquels ils sont organisés.

## Gestion des dossiers de modèles

![Dossiers de modèles](../assets/model-modelselect-folders.png)

Ethos permet de regrouper les modèles dans vos propres dossiers — typiquement
Avion, Planeur, Héli, Quad, Warbird, Bateau, Voiture, Modèle type ou Archive.
Tant que vous n'en avez créé aucun, les modèles résident dans un dossier
automatique **Uncategorized** (créé lors de la mise à jour vers Ethos 1.1.0
alpha 17 ou ultérieur, ou lorsqu'un fichier de modèle est copié dans `\Models`
depuis un autre emplacement) ; Ethos le supprime dès qu'il est vide.

Pour créer un dossier, appuyez sur **+** à côté de « Uncategorized » (ou appui
long sur `PAGE` haut/bas), nommez-le (jusqu'à 15 caractères) et validez. Les
dossiers sont triés par ordre alphabétique, **Uncategorized** figurant toujours
en dernier, et correspondent directement aux sous-dossiers de `\Models` sur la
carte SD/eMMC. Un appui sur le nom d'un dossier ouvre les options de
renommage/suppression — la suppression d'un dossier replace les modèles qu'il
contient dans Uncategorized.

![Changer de dossier](../assets/model-modelselect-folder-change-select.png)

Pour déplacer un modèle, appuyez sur son icône, choisissez **Changer de
dossier**, puis appuyez sur la destination :

![Choisir un dossier](../assets/model-modelselect-folder-airplane-select.png)

## Ajout d'un nouveau modèle

![Créer un modèle](../assets/model-modelselect-model-create.png)

Sélectionnez la catégorie dans laquelle créer le modèle, appuyez sur **+**, puis
sur **Créer un modèle** pour lancer l'assistant (créez d'abord la catégorie si
elle n'existe pas encore). Des assistants sont disponibles pour **Avion**,
**Planeur**, **Hélicoptère**, **Multirotor** et **Autre** ; chacun guide la
configuration de base propre à ce type de cellule, y compris des mixages
préétablis facultatifs pour les récepteurs stabilisés FrSky (gain, mode de
stabilisation). Les noms de modèles peuvent comporter jusqu'à 15 caractères.

### Récepteurs stabilisés et ordre des voies

![Assistant : avion](../assets/model-modelselect-model-wizard-airplane.png)

Les récepteurs stabilisés FrSky exigent spécifiquement l'ordre des voies
**AETR** — laissez [Manches → Ordre des voies](../system-setup/controls.md) sur
sa valeur par défaut AETR avec l'option **Quatre premières voies fixes**
activée, afin que le résultat de l'assistant corresponde à ce qu'attend le
récepteur.

L'assistant attribue les voies de droite à gauche. Pour 2 ailerons + 1
profondeur + 1 dérive + 1 moteur, cela donne :

| Voie | Fonction |
|---|---|
| 1 | Aileron 1 (aileron droit) |
| 2 | Profondeur |
| 3 | Gaz |
| 4 | Dérive |
| 5 | Aileron 2 (aileron gauche) |

Avec cette affectation, le différentiel d'ailerons est **positif** dans le cas
normal (débattement vers le haut supérieur au débattement vers le bas). Les
manuels des récepteurs FrSky documentent actuellement la convention *inverse*
(de gauche à droite, donc voie 1 = aileron gauche, voie 5 = aileron droit) —
dans ce cas, le différentiel devrait être **négatif** pour obtenir le même effet
physique.

!!! tip
    Il est recommandé d'utiliser la convention Ethos de manière cohérente —
    toutes les fonctions de stabilisation fonctionnent correctement dans les
    deux cas, puisque le sens de compensation est défini lors de la
    configuration de la stabilisation. Si vous devez néanmoins respecter la
    convention des manuels de récepteurs, la solution la plus simple consiste à
    construire le modèle normalement avec l'assistant, puis à utiliser
    **Échanger les voies** dans [Sorties](outputs.md) pour permuter ensuite les
    deux voies d'ailerons — cela conserve un signe positif pour le différentiel
    du mixeur d'ailerons.

### Étapes de l'assistant

![Assistant : type d'empennage](../assets/model-modelselect-model-wizard-tail.png)
![Assistant : nombre d'ailerons/volets](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![Assistant : nombre de voies de profondeur/dérive](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![Assistant : motorisation](../assets/model-modelselect-model-wizard-engine.png)
![Assistant : réaffectation des voies](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![Assistant : nom](../assets/model-modelselect-model-wizard-name.png)
![Assistant : récepteur](../assets/model-modelselect-model-wizard-rx.png)

Pour un **Avion**, après le type d'empennage et le nombre de surfaces,
l'assistant traite le nombre de voies moteur, puis le nombre de voies
d'ailerons/volets.

La **configuration de l'empennage** propose un empennage classique en croix, un
empennage en V, ou aucun empennage (aile delta/aile volante) :

- **Aile delta/aile volante** — la création d'un modèle Avion avec 2 ailerons et
  aucune surface d'empennage génère automatiquement le mixage des élevons, avec
  des pondérations par défaut de 50 % afin que des ordres simultanés d'ailerons
  et de profondeur à fond totalisent toujours 100 %.
- **Aile delta avec un récepteur stabilisé assurant le mixage** — sélectionnez
  plutôt 1 aileron et 1 profondeur ; le mixage des élevons est réalisé dans le
  récepteur, conformément à son propre manuel.
- **Aile delta avec des surfaces d'ailerons et de profondeur dédiées** —
  laissez l'assistant se dérouler comme si le modèle avait un empennage ; il
  configure les voies d'ailerons et de profondeur nécessaires (avec ou sans
  dérive), et aucun mixage d'élevons n'est créé.

L'étape de **réaffectation des voies** permet de remplacer l'affectation par
défaut de l'assistant, en gardant à l'esprit que les récepteurs stabilisés
exigent leurs voies dans un ordre précis (consultez les instructions du
récepteur). La dernière étape définit le nom du modèle et y associe une image.

Le modèle terminé est placé dans le dossier de catégorie actif au lancement de
l'assistant, trié par ordre alphabétique au sein de celui-ci. Voir [Exemple de
base pour aile fixe](../tutorials/basic-fixed-wing.md) pour un déroulé complet.

## Réception d'un modèle depuis une autre radio Ethos

![Recevoir un modèle](../assets/model-modelselect-model-receive.png)

Sélectionnez la catégorie de destination, appuyez sur **+**, puis sur **Recevoir
un modèle** — la radio se met en attente et affiche son adresse Bluetooth afin
que l'émetteur puisse la trouver. Sur la radio émettrice, appuyez sur le modèle
et choisissez **Envoyer le modèle** ; la radio réceptrice demande confirmation
du nom de fichier entrant avant de l'accepter.

## Sélection d'un modèle

Appuyez sur **Choix du modèle** pour afficher la liste des modèles.

!!! note "Conversion des modèles après une mise à jour d'Ethos"
    Ethos convertit chaque modèle individuellement la première fois qu'il est
    *sélectionné* après une mise à jour de version, et non tous en même temps
    lors de la mise à jour — il n'y a aucun délai perceptible, et l'opération
    peut être effectuée en toute sécurité à n'importe quel moment ultérieur,
    même sous une version d'Ethos encore plus récente. La date de **Dernière
    modification** en bas de l'écran de sélection est mise à jour lorsqu'une
    conversion a lieu (ou lorsque vous modifiez le modèle — sinon elle reste
    inchangée).

**Sélection rapide** — un appui long tactile ou un appui long sur `ENT` sur
l'icône d'un modèle bascule immédiatement vers celui-ci.

**Menu de gestion des modèles** — appuyez sur un modèle pour le mettre en
surbrillance, puis appuyez à nouveau pour ouvrir le menu :

- **Définir comme modèle courant**
- **Cloner** — duplique le modèle. Un clone reçoit automatiquement un nouveau
  numéro de récepteur ; si vous réaffectez à la place le numéro de récepteur de
  l'original, il fonctionne sans nouvelle association.
- **Changer de dossier**
- **Envoyer**/**Recevoir** — vers ou depuis une autre radio, comme ci-dessus.
- **Supprimer** — proposé uniquement pour un modèle qui n'est pas le modèle
  courant.
