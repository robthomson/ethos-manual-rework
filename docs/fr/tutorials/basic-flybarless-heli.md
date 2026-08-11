---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Exemple de base d'hélicoptère flybarless

Configuration de base d'un hélicoptère flybarless (FBL), en prenant comme
exemple un contrôleur de type Spirit. Contrairement à un modèle à voilure
fixe, un hélicoptère est intrinsèquement instable — le contrôleur FBL
utilise des gyroscopes (vitesse de rotation) et des accéléromètres
(mouvement/orientation) pour calculer les corrections de lacet/tangage/
roulis via une boucle de régulation PID (proportionnelle-intégrale-dérivée)
réglée de manière à équilibrer stabilité, réactivité et dépassement en
fonction des caractéristiques physiques et électriques propres à
l'hélicoptère.

Ce tutoriel ne traite que de la partie **programmation de la radio** —
reportez-vous à la documentation de votre unité FBL pour le reste, et
abordez-le avec de solides connaissances générales en hélicoptère.

!!! danger
    Retirez les pales avant de commencer, par sécurité.

## Step 1. Vérifier les réglages système

Ordre des voies **AETR**, **[Quatre premières voies
fixes](../system-setup/controls.md#first-four-channels-fixed)** sur
**OFF** — les unités FBL Spirit attendent les voies SBUS précisément dans
cet ordre (bien qu'elles utilisent l'ordre TAER en interne dans leur propre
configuration). Enregistrez (si ACCESS) et appairez le récepteur via [RF
System](../model-setup/rf-system.md).

## Step 2. Identifier les servos/voies nécessaires

| Fonction | Voie |
|---|---|
| Roulis (aileron) | — |
| Tangage (profondeur) | — |
| Gaz | — |
| Lacet (dérive) | — |
| Gain gyro | 5 |
| Pas collectif | 6 |
| Banque de réglages | 7 |
| Rescue (secours) | 8 |

## Step 3. Créer un nouveau modèle

![Créer un modèle d'hélicoptère](../assets/tut-heli-eg-wiz-create-heli.png)

Depuis [Choix du modèle](../model-setup/model-select.md), créez/sélectionnez
une catégorie Heli, lancez l'assistant et choisissez **Flybarless** :

![Sélection FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Nom du modèle](../assets/tut-heli-eg-wiz-name.png)

Nommez-le et choisissez une image.

## Step 4. Vérifier et configurer les mixages

![Vue d'ensemble des mixages](../assets/tut-heli-eg-mixes.png)

L'assistant crée Ailerons/Profondeur/Gaz/Dérive dans l'ordre AETR, le Pas
sur la voie 6 et la banque FBL sur la voie 7 :

![Mixage du pas](../assets/tut-heli-eg-mixes-pitch.png)

Vérifiez que la voie 6 correspond bien au pas collectif. Deux voies
supplémentaires doivent être ajoutées manuellement en tant que [mixages
libres](../model-setup/mixes.md#mix-libraries) : **Gain gyro** (voie 5) et
**Rescue/Stabi** (voie 8).

**Aileron/Profondeur/Dérive** — rien à ajouter ; les rates et l'Expo sont
du ressort de l'unité FBL, la radio se contente donc de transmettre une
entrée linéaire propre.

![Mixage d'aileron](../assets/tut-heli-eg-mixes-ail.png)

**Pas collectif** — une courbe strictement linéaire ; vérifiez simplement
la voie de sortie (normalement 6). Comme ci-dessus, les rates et l'Expo
sont gérés par l'unité FBL, pas ici.

**Banque FBL** — les trois banques de réglages du Spirit (styles de vol
différents, gains de capteurs à différents régimes, ou Débutant/Acro/3D —
ou simplement des préréglages de tuning) affectées à un interrupteur
3 positions, par exemple SE :

![Mixage de banque](../assets/tut-heli-eg-mixes-bank.png)

**Gain gyro** — à ajouter comme mixage libre après la dernière voie. Le
gain est généralement une valeur fixe : réglez la **Source** sur Valeur
spéciale 0, ajustez le gain via l'**Offset** (affiné plus tard en vol) et
sortez sur la voie 5 :

![Mixage de gain gyro](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Configurer les phases de vol

![Phases de vol](../assets/tut-heli-eg-flight-modes.png)

Trois [phases de vol](../model-setup/flight-modes.md) : renommez celle par
défaut en **Normal**, et ajoutez **Idle Up 1**/**Idle Up 2** sur
l'interrupteur SD.

### Configurer le mixage des gaz

Trois courbes de gaz, une par phase de vol, chacune étant une [courbe
personnalisée](../model-setup/curves.md) :

- **Normal** — montée en régime/décollage : démarre à −100 % (moteur
  arrêté) puis monte progressivement. Une courbe à 7 points avec
  **Smooth** activé fonctionne bien ; les valeurs exactes doivent être
  affinées en vol.

  ![Courbe Normal](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1** — vol général : une courbe en ligne droite correspondant à
  une valeur de gaz constante maintenant un régime rotor stable, le
  mouvement étant obtenu par le pas collectif, l'aileron (roulis) et la
  profondeur (tangage). Veillez à ce que la transition depuis Normal reste
  douce — sans grand écart. (La plupart des unités FBL proposent également
  une fonction **Governor** pour maintenir un régime rotor constant lors de
  manœuvres agressives — voir le manuel de l'unité FBL.)

  ![Courbe Idle Up 1](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2** — vol agressif (voltige, 3D) ; à affiner également en vol.

  ![Courbe Idle Up 2](../assets/tut-heli-eg-curves-iup2.png)

![Courbes de gaz dans les mixages](../assets/tut-heli-eg-mixes-thr-curves.png)

**Coupure gaz** — affectez par exemple l'interrupteur SG en position haute
avec l'option **Sticky** activée : basculer SG vers le haut coupe les gaz
instantanément et, du fait de l'option Sticky, le réarmement n'est possible
qu'après avoir ramené le manche des gaz au ralenti/arrêt.

![Coupure gaz](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescue/Stabi** — à affecter de la même manière, par exemple à
l'interrupteur SA sur la voie 8.

![Mixages finaux](../assets/tut-heli-eg-mixes-final.png)

## Step 5. Configuration du FBL

1. **Installez l'outil de configuration du FBL** — par exemple Spirit
   Settings, sur un PC.
2. **Connectez le récepteur à l'unité FBL** conformément à son schéma de
   câblage — généralement la sortie SBUS du récepteur vers le port RUD de
   l'unité FBL (certains modèles Spirit nécessitent un adaptateur SBUS), ou
   bien via F.Port1/FBUS.
3. **Connectez l'unité FBL au PC** — par câble ou Bluetooth, selon son
   manuel.

   !!! danger
       Ne connectez encore aucun servo.

4. **Mettez à jour le firmware du FBL** si nécessaire, depuis l'onglet
   Update de l'outil.
5. **Configuration générale** (onglet General de Spirit Settings) :
   - Type de récepteur : **Futaba SBUS** ou **FrSky F.Port** selon le cas,
     puis redémarrez.
   - Affectation des voies (avec l'ordre AETR de l'assistant) :

     | Fonction | Voie |
     |---|---|
     | Gaz | 1 |
     | Aileron | 2 |
     | Profondeur | 3 |
     | Dérive | 4 |
     | Gyro | 5 |
     | Pas | 6 |
     | Banque | 7 |
     | Rescue/Stabi | 8 |

     (Cette affectation découle de la façon dont l'unité Spirit interprète
     les positions dans le flux de données SBUS.)

6. **Limites des voies** (onglet Diagnostic) — l'unité FBL nécessite des
   limites de voies radio calibrées et des neutres vérifiés :

   - Remettez d'abord à zéro tous les subtrims et trims de la radio.
   - Centrez le manche de pas collectif pour lire exactement 1500 µs dans
     [Sorties](../model-setup/outputs.md).
   - Mettez l'unité FBL sous tension et vérifiez que aileron/profondeur/
     pas/dérive affichent tous 0 % dans l'onglet Diagnostic (l'unité FBL
     détecte automatiquement le neutre à chaque initialisation).
   - Déplacez chaque commande jusqu'à ses butées et ajustez les valeurs
     **Min**/**Max** correspondantes dans Sorties jusqu'à ce que l'onglet
     Diagnostic affiche exactement +100 %/−100 %, en vérifiant également
     que le sens des barres correspond au sens des manches.

   !!! warning
       N'utilisez jamais de subtrim ni de trim sur ces voies — l'unité FBL
       Spirit les interprète comme des commandes d'entrée, et non comme un
       calibrage.

7. Ajustez l'**Offset** du mixage de gain gyro pour obtenir le verrouillage
   de cap (Heading Lock).

Une fois ces étapes réalisées, le côté émetteur est entièrement configuré —
poursuivez le reste de la configuration selon le manuel de l'unité FBL.
