---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Modification du modèle

![Modification du modèle](../assets/model-editmodel.png)

Permet de modifier les paramètres au niveau du modèle initialement définis
par l'assistant — principalement l'identité, mais aussi quelques
substitutions propres au modèle et divers utilitaires.

## Nom, Image

Renommez le modèle ou changez son image ; la recherche d'une image affiche
une vignette d'aperçu.

## Type de modèle

![Type de modèle](../assets/model-edit-modeltype.png)

!!! warning
    Changer le type de modèle réinitialise **tous** les mixages.

## Affectation des voies

Modifier le type d'empennage ou (sur un hélicoptère) le type de plateau
cyclique réinitialise également tous les mixages. Pour les autres voies, il
est possible de modifier le nombre de voies affectées ou de les désaffecter.

## Filtre des analogiques

![Filtre analogique](../assets/model-edit-analog-filter.png)

[Configuration du système → Matériel](../system-setup/hardware.md) propose un
filtre analogique-numérique global capable de réduire les tremblements autour
du neutre des manches ; ce réglage propre au modèle le remplace uniquement
pour ce modèle.

![Options du filtre analogique](../assets/model-edit-analog-filter-select.png)

## Interrupteurs de fonction

![Interrupteurs de fonction](../assets/model-edit-fn-switches.png)

Les six interrupteurs de fonction sont disponibles partout où un paramètre
**Condition d'activation** apparaît, mais — contrairement aux interrupteurs
ordinaires — ne peuvent pas être utilisés comme source polyvalente. Ils se
configurent selon l'un des modes suivants :

- **6 positions avec OFF** — appuyer sur un interrupteur de fonction le
  verrouille en position active ; appuyer de nouveau sur le *même*
  interrupteur désactive les six.
- **6 positions** — appuyer sur un interrupteur de fonction le verrouille en
  position active jusqu'à ce qu'un *autre* interrupteur soit pressé, qui
  prend alors le relais.
- **2 × 3 positions** — divise les six interrupteurs en deux groupes de
  trois, avec un interrupteur actif par groupe.
- **6 × 2 positions** — six interrupteurs marche/arrêt verrouillables
  indépendants.
- **Momentané** — six interrupteurs indépendants, chacun actif uniquement
  tant qu'il est maintenu.
- **Persistant** — si cette option est activée, un interrupteur de fonction
  conserve son état après une mise hors tension ou un rechargement du modèle
  au lieu d'être réinitialisé.

![Options des interrupteurs de fonction](../assets/model-edit-fn-switches-select.png)

## Connecteur SPort

La broche 5V du connecteur S.Port de l'émetteur peut être commutée par
modèle — utile par exemple pour alimenter un récepteur externe dans une
configuration écolage.

## Temps d'utilisation du modèle

![Temps d'utilisation du modèle](../assets/model-edit-model-runtime.png)

Comptabilise le temps total de vol/d'utilisation de ce modèle.

## Réinitialiser tous les mixages

![Réinitialiser tous les mixages](../assets/model-edit-model-reset_all_mixes.png)

Réinitialise tous les mixages du modèle à leur état par défaut.
