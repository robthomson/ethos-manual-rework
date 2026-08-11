---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite est l'application compagnon Windows/Mac permettant de gérer une radio fonctionnant sous Ethos, connectée en USB.

!!! note "Captures d'écran à venir"
    Ethos Suite est une application PC distincte, et non la radio elle-même : cette section n'utilise donc pas les captures d'écran issues du simulateur employées dans le reste du manuel — voir [Chaîne de production des captures d'écran](../contributing/screenshot-pipeline.md).

Une fois la connexion établie, Ethos Suite permet de :

1. Lire le type, l'identifiant et les versions installées sur la radio — firmware, bootloader, module RF interne, fichiers de la mémoire flash et fichiers de la SD card/eMMC.
2. Basculer la radio entre le mode bootloader et l'exécution d'Ethos, et inversement.
3. Comparer les versions installées avec les versions actuelles et effectuer la mise à jour automatiquement — uniquement les composants obsolètes, l'ensemble des composants, ou chaque composant individuellement.
4. Sauvegarder les modèles sur le disque via **Model Manager**, ou restaurer une sauvegarde antérieure (nécessaire car les fichiers de modèles ne sont pas rétrocompatibles entre les versions de firmware).
5. Télécharger n'importe quel firmware depuis le site de téléchargement FrSky via le **Download center**, et utiliser la radio comme relais pour flasher directement un module, un capteur, un servo ou un récepteur.
6. Convertir des images et des fichiers audio vers les formats natifs d'Ethos.
7. Fournir les **Lua development tools** — documentation de l'API, scripts de démonstration et terminal de débogage.
8. Flasher le bootloader de la radio en mode DFU (connexion hors tension), indépendamment du fait que le firmware de la radio fonctionne encore ou non.
9. Réparer le stockage interne des radios X18/S, TW Lite, XE et X20 Pro/R/RS via le **Repair Tool**, si la NAND ne peut pas être lue ou si les réglages ne sont pas enregistrés.
10. Éjecter proprement les lecteurs USB de la radio.
11. Signaler au démarrage la disponibilité d'une mise à jour de Suite elle-même (installée à la fermeture).

## Modes de connexion

Au-delà de ses outils, Suite fonctionne selon trois états de connexion distincts de la radio :

- **Radio en mode bootloader** — l'onglet **Radio** vérifie/met à jour le firmware ainsi que les fichiers de la flash, de la SD card ou de l'eMMC ; **Model Manager** sauvegarde ou restaure la radio.
- **Radio en mode Ethos** — Suite utilise la radio comme relais (via les outils **FRSK Flasher**/Download center) pour flasher directement le module interne, ou tout capteur, servo ou récepteur connecté.
- **Radio en mode DFU** — connexion hors tension, utilisée par le **DFU Flasher** pour flasher le bootloader lui-même, par exemple lorsqu'une corruption du firmware empêche la radio de démarrer normalement.

Voir [Migration](migration.md) pour transférer une radio existante vers Ethos Suite pour la première fois, et [Utilisation](operation.md) pour l'interface de Suite proprement dite.
