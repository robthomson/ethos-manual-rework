---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Chronos

![Chronos](../assets/model-timers.png)

Huit chronos entièrement programmables, comptant chacun vers le haut ou
vers le bas. Ajoutez-en un avec le **+** situé à côté des en-têtes de
colonnes, ou via **Ajouter** en dessous. Toucher un chrono ouvre les
options de réinitialisation/édition/ajout/déplacement/copier-coller.

![Édition d'un chrono](../assets/model-timer1-edit.png)

## Champs communs (décompte et comptage)

- **Valeur** — la lecture actuelle du chronomètre.
- **Nom** — modifiable.
- **Mode** — **Haut** ou **Bas**.
- **Valeur de départ** (décompte uniquement) — la valeur à partir de
  laquelle le décompte s'effectue.
- **Valeur d'alarme** (comptage uniquement) — la valeur à laquelle le
  chronomètre est considéré comme écoulé ; il continue de compter au-delà,
  mais s'affiche en rouge dans les widgets de chrono.
- **Condition de démarrage** — démarre le chronomètre. Si la **Condition
  d'arrêt** est laissée à sa valeur par défaut, la condition de démarrage
  contrôle à elle seule le démarrage *et* l'arrêt. Sinon, le chronomètre
  démarre la première fois que la condition de démarrage devient vraie,
  puis continue de tourner.
- **Condition d'arrêt** — si elle n'est pas laissée à sa valeur par défaut,
  elle contrôle le chronomètre une fois celui-ci lancé : arrêté tant qu'elle
  est vraie, en marche lorsqu'elle est fausse. Dans l'exemple ci-dessous, un
  chronomètre démarre lorsque `ThrottleActive` devient vrai et s'arrête dès
  que la télémétrie n'est plus active :

  ![Condition d'arrêt](../assets/model-timer1-edit-stop.png)

- **Source de comptage proportionnel** — `---` compte en temps réel. Toute
  autre source (par exemple le manche des gaz ou la voie des gaz) module la
  vitesse du chronomètre : à −100 % le chronomètre est arrêté, à +100 % il
  tourne à la vitesse réelle, et l'évolution est proportionnelle entre les
  deux.
- **Réinitialisation** — un interrupteur, un interrupteur de fonction, un
  interrupteur logique ou une position de trim qui réinitialise le
  chronomètre ; celui-ci reste maintenu à zéro aussi longtemps que la
  condition est vraie.
- **Persistant** — conserve la valeur du chronomètre après une mise hors
  tension ou un changement de modèle, et la recharge lors de la prochaine
  utilisation du modèle.
- **Voix** — quel [pack vocal](../system-setup/general.md#audio-settings)
  annonce ce chronomètre.

## Actions audio

![Ajouter une action audio](../assets/model-timer1-add-action.png)
![Type d'action](../assets/model-timer1-action-type-select.png)
![Action de décompte](../assets/model-timer1-action-countdown.png)

Configuration des alertes entièrement flexible, propre à chaque chrono.
Chaque action possède un type — **Décompte** (vocal), **Décompte sonore**
(bips au lieu de la voix), **Jouer un fichier** ou **Annoncer une valeur** —
ainsi que :

- **Départ** — la valeur à partir de laquelle le décompte de cette action
  commence.
- **Pas** — l'intervalle entre les annonces, jusqu'à 10 minutes (600 s).
- **Vibreur** — accompagner l'annonce d'une vibration.

Un empilement typique de trois actions :

![Résumé des actions](../assets/model-timer1-actions-summary.png)
![Actions du chrono 2](../assets/model-timer2-actions-summary.png)

1. Décompte vocal débutant à 2:00 restantes, toutes les 30 s, avec vibreur.
2. Décompte sonore débutant à 0:10 restantes, toutes les 1 s, avec vibreur.
3. Un fichier personnalisé (par exemple `timer-1-elapsed`) joué à
   l'échéance, avec vibreur.

Ajoutez d'autres actions avec **Ajouter** ; la liste est traitée par ordre
de priorité, la **priorité la plus élevée en dernier**.

Voir également le [widget d'écran Journal des chronos](../displays/index.md#widget-types)
pour un journal des séquences de chronométrage passées.

![Widget de chrono](../assets/model-timers-widget.png)
