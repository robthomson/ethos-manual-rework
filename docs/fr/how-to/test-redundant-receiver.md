---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Tester une configuration à récepteur redondant

La redondance n'a d'intérêt que si elle est réellement testée avant le vol —
ceci suppose qu'un [récepteur redondant](../model-setup/rf-system.md#redundant-receivers)
est déjà configuré.

!!! note "Captures d'écran à venir"
    Cette page ne comporte pas encore de captures d'écran du simulateur — voir [Chaîne
    de production des captures d'écran](../contributing/screenshot-pipeline.md).

## A. Test en conditions réelles

Avec le récepteur principal en 2,4 GHz et le récepteur redondant en 900 MHz, lancez un
[test de portée](../model-setup/rf-system.md#range-check) et éloignez-vous du
modèle jusqu'à ce que la liaison 2,4 GHz soit perdue (au-delà de l'alerte RSSI Critique). Le
récepteur redondant 900 MHz doit alors prendre le relais du contrôle.

## B. Test au banc

1. **Vérifier la configuration normale** — les deux récepteurs appairés, les deux LED vertes allumées,
   les commandes répondant normalement.
2. **Appairer le récepteur principal à un autre Model ID** — créez un modèle
   de test jetable (par exemple « TestRx ») avec un Model ID différent, et appairez-y le
   récepteur *principal*. Revenez ensuite au modèle testé : la LED du récepteur
   principal doit maintenant être **rouge** (appairé ailleurs), celle du récepteur
   redondant reste **verte** — et les commandes doivent toujours fonctionner,
   ce qui prouve que le récepteur redondant seul maintient le modèle pilotable.
3. **Réappairer le récepteur principal** à son Model ID normal. Vérifiez que les deux
   LED sont de nouveau vertes et que les commandes fonctionnent avant de considérer
   le test comme terminé.
