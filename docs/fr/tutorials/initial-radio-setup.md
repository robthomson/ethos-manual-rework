---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuration initiale de la radio

La configuration à effectuer une seule fois, avant de programmer un quelconque modèle. Les [Tutoriels](index.md) qui suivent supposent tous que cette étape a été réalisée au préalable.

!!! note
    Ces tutoriels ne sont pas des recettes strictes — ils supposent une
    connaissance du vocabulaire de base du modélisme RC et une certaine
    aisance dans la navigation des menus Ethos. Si quelque chose n'est pas
    clair ici, consultez d'abord [Interface utilisateur et
    navigation](../getting-started/user-interface-and-navigation.md).

## Étape 1. Charger la batterie de la radio et les batteries de propulsion

Chargez la batterie de la radio conformément aux consignes fournies avec celle-ci, et les batteries de propulsion avec un chargeur adapté à leur chimie — soyez particulièrement vigilant avec les packs Lithium.

## Étape 2. Calibrer le matériel

Vérifiez que la [calibration du
matériel](../system-setup/hardware.md#analogs-calibration) a bien été
effectuée (elle s'exécute automatiquement au premier démarrage), afin que la
radio connaisse le centre et les butées exacts de chaque manche, potentiomètre
et curseur. Recommencez-la dans **Système → Matériel** chaque fois qu'un
manche, un potentiomètre ou un curseur est remplacé.

## Étape 3. Effectuer la configuration du système de la radio

La [Configuration du système](../system-setup/index.md) regroupe tout ce qui
est commun à tous les modèles, par opposition aux réglages propres à chaque
modèle de la [Configuration du modèle](../model-setup/index.md). La plupart des
valeurs par défaut conviennent pour débuter, mais passez en revue :

- **[Date et heure](../system-setup/date-and-time.md)** — à régler correctement.
- **[Audio → Choix des
  voix](../system-setup/general.md#audio-settings)** — configurez les annonces
  vocales, y compris les éventuels fichiers audio personnalisés.
- **[Commandes (Manches)](../system-setup/controls.md)** :
  - **Mode des manches** — Mode 1 (gaz/ailerons à droite, profondeur/dérive
    à gauche) ou Mode 2 (gaz/dérive à gauche, ailerons/profondeur à droite —
    le mode par défaut d'Ethos).

    !!! warning
        Si un modèle est configuré pour un mode de manches alors que
        l'émetteur est réglé sur l'autre, un moteur électrique peut démarrer
        dès la mise sous tension du récepteur.

  - **Ordre des voies** — Ethos utilise par défaut **AETR** (Aileron,
    Elevator, Throttle, Rudder) ; la convention Spektrum/JR est **TAER**,
    celle de Futaba/Hitec est **AETR**. Ce réglage détermine l'ordre dans
    lequel les entrées des manches sont affectées lors de la création d'un
    nouveau modèle — chaque modèle peut toujours être ajusté individuellement
    par la suite.

    !!! note "Récepteurs stabilisés FrSky"
        Ceux-ci exigent spécifiquement l'ordre **AETR**. Avec plusieurs
        surfaces par fonction (par exemple 2 ailerons), l'assistant les
        regroupe normalement (donnant **AAETR**) — mais les récepteurs SRx
        attendent plutôt **AETRA**/**AETRAE** ; activez donc **[Quatre
        premières voies
        fixes](../system-setup/controls.md#first-four-channels-fixed)** dans
        Manches pour conserver dans tous les cas les quatre premières voies
        dans l'ordre strict AETR.

- **[Batterie](../system-setup/battery.md)** — réglez **Tension principale**,
  **Tension basse** et **Plage de tension d'affichage** en fonction de la
  batterie réellement installée dans la radio.
- **[Identifiant d'enregistrement du
  propriétaire](../model-setup/rf-system.md#owner-registration-id)** — utilisé
  par les récepteurs ACCESS, et partagé entre émetteurs pour le Smart Share.
  Il se configure dans la Configuration du modèle, mais fonctionne en pratique
  comme un réglage global, puisque chaque nouveau modèle l'utilise (il peut
  toutefois être modifié récepteur par récepteur lors de l'enregistrement, si
  nécessaire).

!!! note "Unités"
    Ethos ne dispose pas de bascule globale métrique/impérial — les [unités
    des capteurs de
    télémétrie](../model-setup/telemetry.md#editing-a-sensor) se règlent
    individuellement, capteur par capteur.
