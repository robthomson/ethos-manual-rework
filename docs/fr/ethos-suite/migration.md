---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migration

Passage d'une radio des anciens outils de mise à jour PC séparés vers Ethos Suite,
pour la première fois.

1. **Vérifiez que la version Ethos est ≥ 1.1.4** — la version minimale capable de flasher le nouveau
   bootloader compatible Suite (format FRSK) directement depuis le [Gestionnaire
   de fichiers](../system-setup/file-manager.md). Mettez d'abord à jour manuellement vers la version 1.1.4
   si nécessaire.
2. **Sauvegardez la carte SD/eMMC** — copiez l'intégralité du contenu dans un dossier sur un
   PC.
3. **Téléchargez le bootloader le plus récent** depuis les
   [publications ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   et décompressez l'archive. Chaque publication comporte un fichier `components.json` listant la version
   actuelle de chaque composant — voir [Guide pratique : trouver le bootloader
   le plus récent](../how-to/find-latest-bootloader.md) pour savoir comment le lire.
4. Recherchez la radio dans l'entrée `targets` de ce fichier afin de connaître la version exacte
   du bootloader à utiliser, puis repérez le fichier correspondant parmi les ressources de cette
   publication.
5. Démarrez la radio en [mode bootloader](../getting-started/usb-connection-modes.md#bootloader-mode)
   (maintenez `ENT`, puis mettez sous tension) et connectez-la en USB.
6. Copiez le fichier du bootloader sur la carte SD/eMMC (normalement dans
   `Firmware/`), puis éjectez les lecteurs et déconnectez la radio.
7. Démarrez la radio normalement, allez dans **System → File Manager**, appuyez sur le
   fichier `bootloader.frsk` qui vient d'être copié, puis sur **Flash bootloader**.
8. Téléchargez et installez Ethos Suite — la page [Utilisation](operation.md) décrit la
   mise à jour du firmware et des fichiers ainsi que les autres fonctionnalités de Suite à partir de ce point.
9. Si Ethos Suite ne le fait pas automatiquement, il peut être nécessaire de renommer le dossier
   `bitmaps/user` de la carte SD/eMMC en `bitmaps/models` (c'est là que
   se trouvent les images de modèles de l'utilisateur).
