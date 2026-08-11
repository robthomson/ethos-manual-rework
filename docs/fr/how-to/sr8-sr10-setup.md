---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configuration du modèle SR8/SR10 et réorganisation des voies

Les récepteurs stabilisés SRx de FrSky attendent un ordre de voies
spécifique. Deux cas de figure : créer un nouveau modèle de toutes pièces
pour l'un d'eux, ou convertir un modèle existant pour qu'il corresponde.

!!! note "Captures d'écran à venir"
    Cette page ne comporte pas encore de captures d'écran du simulateur —
    voir [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## Création d'un nouveau modèle

L'assistant [Choix du modèle](../model-setup/model-select.md) regroupe par
défaut les gouvernes de même fonction (par exemple 2 ailerons → `AAETR`),
mais les récepteurs SRx exigent que les quatre premières voies soient
fixées en **AETRA** à la place.

1. Dans [Commandes](../system-setup/controls.md), vérifiez que **l'ordre
   des voies** est `AETR`.
2. Activez **[Quatre premières voies
   fixes](../system-setup/controls.md#first-four-channels-fixed)** — cela
   empêche l'assistant de regrouper les quatre premières voies, en les
   maintenant strictement dans l'ordre `AETRA…` quel que soit le nombre de
   gouvernes de chaque type que comporte la cellule.
3. Exécutez l'assistant de création de modèle normalement — les 5 premières
   voies sont alors obtenues dans l'ordre `AETRA`.

!!! note "Auto-test des récepteurs Archer"
    L'auto-test des récepteurs Archer s'effectue désormais via
    [Configuration des appareils →
    SxR](../system-setup/devices.md) (firmware v2.1.10 et ultérieur) plutôt
    que par une procédure d'auto-test dédiée. La voie des gaz doit être à
    −100 %, sinon l'auto-test ne démarrera pas.

## Réorganisation d'un modèle existant

Convertir un modèle existant (par exemple actuellement en `AAETRFF`) vers
l'ordre requis par les récepteurs stabilisés (`AETRAE`, puis voie 9 pour le
gain, 10/11 pour les phases de vol, 12 pour l'auto-test sur les anciennes
unités SxR) consiste en une série d'échanges de voies dans
[Sorties](../model-setup/outputs.md#swap-channels).

Point de départ :

| Voie | Fonction |
|---|---|
| 1 | Aileron1 (droit) |
| 2 | Aileron2 (gauche) |
| 3 | Profondeur |
| 4 | Gaz |
| 5 | Dérive |
| 6 | Volet1 (droit) |
| 7 | Volet2 (gauche) |
| 8 | Train rentrant |

Ordre visé : `AETRAE` — Voie 1 Aileron1, Voie 2 Profondeur, Voie 3 Gaz,
Voie 4 Dérive, Voie 5 Aileron2, Voie 6 Profondeur2/AUX2 (puis
gain/phases de vol/auto-test sur les voies 9 à 12).

1. **Commencez par déplacer Aileron2 hors du chemin** : dans Sorties,
   sélectionnez CH2 (Aileron2), appuyez de nouveau, choisissez **Échanger
   les voies**, et échangez-la avec une voie inutilisée (par exemple CH9).
   L'échange est immédiat — tous les mixages faisant référence à l'une ou
   l'autre voie sont mis à jour automatiquement.
2. **Échangez CH3 (Profondeur) → CH2.**
3. **Échangez CH4 (Gaz) → CH3.**
4. **Échangez CH5 (Dérive) → CH4.**
5. **Échangez CH9 (Aileron2, mise de côté à l'étape 1) → CH5.**

Résultat :

| Voie | Fonction |
|---|---|
| 1 | Aileron1 (droit) |
| 2 | Profondeur |
| 3 | Gaz |
| 4 | Dérive |
| 5 | Aileron2 (gauche) |
| 6 | Volet1 (droit) |
| 7 | Volet2 (gauche) |
| 8 | Train rentrant |

— soit désormais l'ordre attendu par les récepteurs stabilisés FrSky.
