---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Interface utilisateur et navigation

Ethos peut être entièrement piloté avec la **molette rotative** de droite
(tourner pour déplacer la surbrillance, appuyer pour `ENT`) et la touche
`RTN` pour revenir en arrière — l'écran tactile, lorsqu'il est présent,
n'est qu'un raccourci pour les mêmes actions, pas une autre façon de
travailler. `MDL`, `DISP` et `SYS` ouvrent directement Configuration du
modèle, Configurer les écrans et Configuration du système (les trois
mêmes cases que la barre inférieure) ; un appui long sur `RTN` depuis
n'importe où ramène directement à l'écran d'accueil.

## Le menu de réinitialisation

![Menu contextuel](../assets/resetmenu.png)

Un appui long sur `ENT` depuis l'écran d'accueil ouvre un menu de
réinitialisation :

- **Réinitialiser le vol** — réinitialise la télémétrie, les chronomètres
  et les interrupteurs de fonction, et relance la [checklist](../model-setup/checklist.md)
  de pré-vol.
- **Réinitialiser la télémétrie** — réinitialise uniquement la télémétrie.
- **Réinitialiser les chronomètres** — réinitialise uniquement les
  chronomètres.
- **Verrouiller l'écran tactile** — également accessible en appuyant
  simultanément sur `ENT` et `PAGE` pendant une seconde depuis l'écran
  d'accueil, ou via une [fonction
  spéciale](../model-setup/special-functions.md).

## Modifier les réglages

**Ajouter un élément fonctionnel** — un chronomètre, un interrupteur
logique, une fonction spéciale, une courbe ou une variable se crée en
touchant le **+** à côté des en-têtes de colonnes dans le menu concerné.
Sur une radio sans écran tactile, mettez en surbrillance un élément
existant, appuyez sur `ENT`, puis choisissez **Ajouter** dans le menu —
la même option est également disponible sur les radios tactiles.

### Clavier virtuel

![Clavier texte](../assets/keyboard-text-azerty.png)

Toucher un champ de texte (ou appuyer sur `ENT` dessus) ouvre le clavier
à l'écran. La touche de retour arrière efface à gauche du curseur ;
`PAGE` supprime à droite, et une fois le curseur arrivé en fin de texte,
continue à supprimer depuis la gauche. Toucher le champ déplace le
curseur à cet endroit — ou utilisez `SYS`/`DISP` pour le déplacer à
gauche/droite sans le tactile. La touche **?123**/**abc** bascule vers
le clavier numérique (qui comporte aussi les caractères spéciaux) :

![Clavier numérique](../assets/keyboard-text-numbers.png)

Sur une **radio sans écran tactile**, appuyer sur `ENT` sur un champ de
texte entre directement en mode édition : tournez la molette pour faire
défiler les minuscules, majuscules, chiffres, puis caractères spéciaux,
en appuyant sur `ENT` pour insérer chacun d'eux. `MDL` bascule la casse
du caractère immédiatement à droite du curseur (et chaque caractère
saisi ensuite conserve cette casse jusqu'au prochain basculement).
`PAGE` supprime à droite du curseur ; `SYS`/`DISP` le déplacent à
gauche/droite.

## Réglage des valeurs numériques

![Saisie de nombre](../assets/keyboard-numbers.png)

Toucher un champ numérique ouvre une barre de contrôle en bas de
l'écran : **`<`**/**`>`** changent le pas d'incrémentation (en tournant
entre les décades — par ex. 0,01/0,1/1,0/10,0), **`-`**/**`+`** (ou la
molette rotative) ajustent la valeur de ce pas, et **Plus** ouvre
d'autres options :

![Options de saisie numérique](../assets/keyboard-numbers-options.png)

- Revenir à la valeur par défaut du champ
- Mettre au minimum / au maximum
- Remplacer les boutons +/- par un **curseur**

![Saisie par curseur](../assets/keyboard-numbers-slider.png)

Le curseur (également ajustable avec la molette rotative) est plus
rapide pour les grands changements ; **Désactiver le curseur** revient
aux boutons +/-. Les plages de valeurs de télémétrie se modifient de la
même manière :

![Curseur désactivé](../assets/keyboard-numbers-options-disable-slider.png)

## La fonctionnalité Options {: #the-options-feature }

Presque partout où une valeur ou une [source](#choosing-a-source) est
attendue, un appui long sur `ENT` ouvre une boîte de dialogue
**Options** — repérable par la petite icône de menu (« hamburger ») dans
le coin supérieur gauche du champ.

### Options de valeur

![Options de source](../assets/source-with-options.png)

La boîte de dialogue des options de valeur indique le paramètre en cours
de modification et propose de choisir entre un minimum/maximum fixe ou
de le piloter par une **source** (par ex. un potentiomètre, pour ajuster
la valeur en vol). Si le champ utilise déjà une source, le même appui
long propose plutôt de convertir la valeur actuelle de cette source en
valeur fixe :

![Convertir la source en valeur](../assets/source-convert-to-value.png)

### Choisir une source {: #choosing-a-source }

Sélectionner **Choisir une source** ouvre un sélecteur à deux colonnes —
d'abord une **catégorie** (analogiques, interrupteurs, interrupteurs
logiques, trims, voies, un axe gyroscopique, une voie élève, un
chronomètre, un capteur de télémétrie, ou quelques valeurs spéciales),
puis le membre précis de cette catégorie :

![Menu source](../assets/source-menu.png)

Une fois la source définie, le même appui long ouvre des options
propres au type de source :

**Toute source** —

- **Inverser** — inverse la source (par ex. active quand un interrupteur
  n'est *pas* en position haute, plutôt que quand il l'est).
- **Front** (Edge) — se déclenche une seule fois lors d'une transition
  (faux→vrai ou vrai→faux) au lieu de rester actif pendant tout l'état ;
  affiché avec un préfixe `†` sur la source. Disponible sur les
  interrupteurs en général, et spécifiquement sur la condition de
  déclenchement de l'[interrupteur logique
  Sticky](../model-setup/logical-switches.md).

**Sources manche** — options de type calibration/subtrim :

![Options source manche](../assets/source-stick-options.png)

**Sources interrupteur** —

![Options interrupteur 2 positions](../assets/source-2pos-options.png)
![Options interrupteur](../assets/switch-options.png)

- **Négatif** — inverse l'action de l'interrupteur.
- **DemiPlage** (HalfRange) — pour un interrupteur 2 positions ou un
  interrupteur logique, change sa plage de sortie de ±100 % à 0–100 %.

**Sources trim** —

![Options source trim](../assets/source-trim-options.png)

- **Négatif** — inverse l'action du trim (utile dans les Actions d'un
  mixage libre).
- **Pleine plage** — les trims valent par défaut ±25 % ; en tant que
  source, cette plage peut être élargie à ±100 %.
- **Ignorer l'entrée formateur** — sur un [interrupteur
  logique](../model-setup/logical-switches.md), exclut les mouvements
  provenant de l'entrée formateur du déclenchement de l'interrupteur.
  Usage typique : détecter le mouvement des manches du formateur
  **maître** lui-même (par ex. pour intervenir instantanément si l'élève
  fait une erreur) sans que les entrées manche de l'élève ne déclenchent
  aussi l'interrupteur.

**Sources variable** —

![Options source variable](../assets/source-var-options.png)

- **Négatif** — inverse la valeur de la variable pour cet usage.
- **Ignorer la plage** — certains champs ont des plages asymétriques
  (par ex. Min/Max des Sorties, qui vont de −150 à 0 % et de 0 à 150 %
  respectivement). À moins qu'une [variable](../model-setup/variables.md)
  utilisée comme source de ce champ n'ait une plage identique, activez
  cette option pour éviter la conversion de plage automatique d'Ethos et
  des valeurs inattendues.

**Sources capteur de télémétrie** — réduisent la source à son minimum ou
maximum en direct plutôt qu'à la valeur instantanée (certains capteurs
ajoutent des options supplémentaires propres au capteur) :

![Options min/max capteur](../assets/source-sensor-options.png)
![Maximum du capteur sélectionné](../assets/source-sensor-maxi.png)
