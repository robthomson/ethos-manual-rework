---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Mode d'urgence

Le mode d'urgence est la réponse d'Ethos à un défaut inattendu de bas
niveau, comme une réinitialisation par watchdog. Le watchdog est un
minuteur continuellement relancé par différentes parties du système ; si
quelque chose empêche son redémarrage, il expire et force une
réinitialisation matérielle de la radio. Le mode d'urgence redémarre
alors la radio aussi vite que possible, en sautant toutes les
vérifications de démarrage habituelles afin de rendre le contrôle du
modèle avec un délai minimal. La carte SD/eMMC n'est pas du tout
sollicitée dans ce mode.

Seules les fonctions essentielles nécessaires pour continuer à contrôler
le modèle sont disponibles — aucune des fonctionnalités de plus haut
niveau. L'écran devient noir à l'exception des mots **EMERGENCY MODE**,
accompagnés d'un bip de 300 ms répété toutes les 3 secondes ; les
alertes vocales, les scripts Lua, l'enregistrement et la télémétrie
s'arrêtent tous. Si cela se produit en vol, atterrissez dès que
possible.

La cause la plus fréquente est une défaillance de la carte SD.

## Tester le mode d'urgence

Un **outil système** peut être ajouté pour déclencher volontairement le
mode d'urgence à des fins de test, afin de ne pas avoir à le découvrir
pour la première fois en vol. Toucher l'icône de test d'urgence demande
une confirmation, puis place la radio en mode d'urgence exactement comme
le ferait un défaut réel.
