---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Modes de connexion USB

![Menu USB](../assets/usbmenu.png)

Ce que fait une connexion USB à un PC dépend de l'état d'alimentation de
la radio au moment du branchement.

## Mode radio éteinte

Brancher la radio à un PC en USB **alors qu'elle est éteinte** la place
en mode DFU, utilisé pour flasher le bootloader lui-même.

## Mode bootloader {: #bootloader-mode }

Allumez la radio **en maintenant `ENT` enfoncé** pour démarrer en mode
bootloader (l'écran affiche « Bootloader »). Brancher l'USB fait alors
passer le statut à « USB branché » et le PC monte **deux** lecteurs : la
mémoire flash interne de la radio, et le contenu de la carte SD/eMMC.
C'est le mode permettant de lire et écrire des fichiers directement sur
l'un ou l'autre espace de stockage, et c'est aussi celui utilisé par
[Ethos Suite](../ethos-suite/index.md) pour mettre à jour le firmware de
la radio — voir la section Mode Bootloader d'Ethos Suite.

## Mode radio allumée

Brancher l'USB alors que la radio est **allumée normalement** fait
apparaître un sélecteur de mode :

- **Joystick** — présente la radio comme un joystick USB HID, pour
  piloter des simulateurs de vol PC.
- **FrSky Suite** — place la radio en « mode Ethos » pour communiquer
  avec [Ethos Suite](../ethos-suite/index.md).
- **Série** — envoie les traces de débogage Lua via USB-série (115200
  bps). L'onglet Outils de développement Lua d'Ethos Suite dispose d'un
  terminal intégré pour les afficher ; un pilote de port COM virtuel
  Windows peut être nécessaire.
