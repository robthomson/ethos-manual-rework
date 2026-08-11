---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Alertes

![Alertes](../assets/system-alerts.png)

Quatre alertes valables pour l'ensemble de la radio, chacune activable
indépendamment — distinctes des [fonctions spéciales](../model-setup/special-functions.md)
et des [interrupteurs logiques](../model-setup/logical-switches.md)
propres à chaque modèle que vous créez vous-même.

- **Mode silencieux** — une alerte vocale au démarrage lorsque ce contrôle
  est activé et que [Général → Mode audio](general.md) est réglé sur
  Silencieux, afin de rappeler que la radio est muette.
- **Tension principale** — « La batterie de la radio est faible » lorsque
  la batterie principale de la radio descend sous le seuil de **Tension
  basse** défini dans [Batterie](battery.md).
- **Tension RTC** — « La batterie RTC est faible » lorsque la pile bouton
  RTC descend sous 2,5 V (le seuil par défaut). L'enregistrement des
  données repose sur l'horloge temps réel ; une heure invalide rend les
  journaux difficiles à exploiter, notamment pour distinguer les sessions
  de vol. Cette alerte peut être désactivée temporairement en attendant de
  remplacer la pile, mais elle ne devrait pas rester désactivée
  indéfiniment.
- **Alerte de conflit de capteurs** — détecte les identifiants de capteurs
  de télémétrie en conflit. Il n'est utile de la désactiver que si vous
  utilisez des capteurs non conformes à la spécification S.Port.
- **Inactivité** — une alerte vocale « Inactivité prolongée » (accompagnée
  d'une vibration, au cas où le volume serait baissé) après que la radio
  soit restée inutilisée plus longtemps que la durée configurée —
  10 minutes par défaut.
