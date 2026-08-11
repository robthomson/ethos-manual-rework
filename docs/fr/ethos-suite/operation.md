---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Utilisation

## Section Bienvenue

**Update News** — notes de version et recommandations de sauvegarde avant
la mise à jour. Ethos 1.6.0+ exige que le module RF interne et les
récepteurs TD/TW/AP/AP Plus soient en v3.0.1+ pour bénéficier de ses
améliorations. L'activation des **Pre-releases** (avec le serveur réglé sur
GitHub — voir [Paramètres de Suite](#suite-settings)) fait également
apparaître ici les versions préliminaires, aux côtés de l'historique
complet des versions.

**Ethos web page** — une vue intégrée de ethos.frsky-rc.com : ressources,
liens vers les modèles types et liste des radios prises en charge.

## Section Radio

Gère la radio connectée. Démarrez-la en [mode
bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) et
connectez-la en USB — Suite affiche le type de radio (par exemple « X20 »)
dès sa détection.

### Informations sur la radio

- **Ethos** — versions du firmware/bootloader installées ; **Manage Ethos**
  ouvre directement leur mise à jour si elles ne sont pas à jour.
- **RF Module** — firmware du module RF interne installé ; **Manage
  internal module** ouvre directement sa mise à jour si nécessaire.
- **Model manager** / **Lua library** / **Download center** — raccourcis
  vers ces outils.

### Mise à jour d'Ethos

L'onglet **Ethos** affiche côte à côte les versions du firmware, du
bootloader, de la SD card/eMMC (fichiers audio) et de la mémoire flash
(bitmaps système) — les fichiers système en mémoire flash sont désormais
mis à jour avec le firmware et ne sont plus gérés séparément.

- **Write outdated components** — met à jour uniquement ce qui est obsolète.
- **Write all components** — met tout à jour, quelle que soit la version.
- Options individuelles **Write firmware**, **Write bootloader**, **Write
  audio files**, chacune lancée en cliquant sur le bouton gris foncé situé
  à côté de l'option choisie.
- **Flash from a local file** — contourne le téléchargement en utilisant un
  fichier de firmware déjà présent sur le disque.

Sélectionner une version consiste d'abord à choisir une **branche**
(Stable/Testing) puis une version. La mise à jour invite d'abord à
effectuer une sauvegarde (**Go to backup page**) — faites-la. Si le module
RF interne n'est pas en v3.0.1+, Ethos 1.6.0+ exige sa mise à niveau avant
de poursuivre (**Go to Module manager** le flashe automatiquement, puis la
mise à jour d'Ethos reprend) — et pour les récepteurs TD/TW/AP/AP Plus, il
faut ensuite supprimer la télémétrie et relancer la découverte afin de
récupérer les noms de capteurs actualisés.

La progression de la mise à jour est affichée étape par étape (passage en
bootloader, téléchargement, copie, démontage, écriture, rafraîchissement,
« Update successful! ») — l'écran de la radio reflète également la
progression de l'écriture.

!!! note "Mises à jour préliminaires"
    Les fichiers d'une version préliminaire peuvent changer sans que son
    numéro de version change, ce que Suite ne peut pas détecter — reflashez
    toujours une version préliminaire que vous utilisez déjà lorsqu'elle
    devient une version définitive. En cas de doute, vérifiez la date du
    firmware dans [System → Info](../system-setup/information.md).

!!! note "Mise à jour depuis Ethos 1.2.8 ou antérieur"
    Suite peut ne pas être en mesure de flasher entièrement
    automatiquement le firmware/bootloader depuis une version aussi
    ancienne — une boîte de dialogue guidée de flash manuel apparaît à la
    place. Dans les deux cas, éjectez les lecteurs manuellement avant de
    débrancher l'USB.

Les fichiers bitmaps système sont désormais mis à jour automatiquement avec
le firmware (aucune gestion séparée n'est nécessaire) ; les fichiers audio
se mettent à jour via **Write all components** ou **Write audio files**
(téléchargement du pack linguistique sélectionné, par exemple « English
audio pack »).

### RF Module Manager

Sélectionnez une version (normalement la plus récente) puis **Flash
module** pour mettre à jour directement le firmware du module RF interne —
la mention « ...has been flashed successfully » confirme la fin de
l'opération. Cette procédure est également déclenchée automatiquement par
la mise à niveau obligatoire en v3.0.1 décrite ci-dessus.

### Ethos Mode

**Switch to Ethos** redémarre la radio hors du mode bootloader pour lancer
Ethos (signalé par une icône USB verte sur la radio, et par la disparition
de la mention « (Bootloader Mode) » dans l'en-tête de Suite). C'est
nécessaire pour que le **Download center** puisse utiliser la radio comme
relais pour flasher des modules, récepteurs, capteurs et servos. Le bouton
devient alors **Switch to Bootloader** pour revenir en arrière. **Eject
Drives** déconnecte proprement la radio.

### Model Manager

Sauvegarde les fichiers de modèles et les réglages sur le disque, ou
restaure une sauvegarde antérieure.

!!! warning
    La restauration ne restaure **pas** le firmware — après avoir restauré
    les modèles/réglages, reflashez séparément la version de firmware
    correspondant réellement à cette sauvegarde (voir [Mise à jour
    d'Ethos](#updating-ethos)), car les fichiers de modèles ne sont pas
    rétrocompatibles.

- **Backup Location** — parcourez jusqu'à un dossier (mémorisé par type de
  radio) ; la date/heure de la dernière sauvegarde s'affiche en dessous.
- **Backup** — enregistre les fichiers de modèles en y consignant la
  version d'Ethos actuelle.
- **Restore** — sélectionnez les composants à restaurer : Audio (désactivé
  par défaut), Scripts, Screenshots, System Bitmaps (désactivé par défaut —
  désormais gérés avec le firmware), Models (y compris les fichiers texte
  de [liste de vérification définie par
  l'utilisateur](../how-to/user-defined-checklist.md) stockés à leurs
  côtés), Language, User Bitmaps, Logs, System Settings.

### Lua library

Parcourez et installez en un clic des scripts/outils Lua depuis la
bibliothèque distante de FrSky (ou installez depuis un fichier zip local) ;
les scripts installés apparaissent aux côtés du catalogue distant dès qu'il
en existe.

## Section Tools

- **Download center** — téléchargez n'importe quel firmware depuis le site
  FrSky et (lorsque la radio est en mode Ethos) utilisez-la comme relais
  pour flasher un module, un capteur, un servo ou un récepteur connecté via
  une liaison de mise à jour S.Port. Choisissez le produit dans la liste
  (par exemple un récepteur TW SR8), parcourez les **assets** disponibles,
  puis **Download** pour enregistrer localement ou **Flash** pour écrire
  directement sur l'appareil connecté — une barre de progression suit le
  flash et se termine par « ...has been flashed successfully! »

- **Image manager** — convertit les images au format natif d'Ethos (BMP
  32 bits, RGB, canal alpha ajouté uniquement si nécessaire) à la taille
  choisie, en conservant les proportions. Tailles de référence : images de
  modèle 300×280 (X20) / 180×168 (X18) ; images plein écran 800×480 (X20) /
  480×320 (X18) — voir le [Gestionnaire de
  fichiers](../system-setup/file-manager.md#top-level-folders) pour les
  règles de nommage des bitmaps. Permet également de parcourir directement
  les dossiers `bitmaps/gps`, `bitmaps/models` et `bitmaps/user` de la
  radio, avec prise en charge de l'envoi. Ajoutez des images à la liste de
  transcodage avec **+** (le TIFF n'est pas pris en charge), choisissez un
  chemin de sortie (un dossier local ; directement sur la radio dans les
  images de modèle/utilisateur/GPS ; ou le dossier de la radio actuellement
  ouvert), et éventuellement ouvrez automatiquement le dossier de sortie ou
  forcez un canal alpha.

- **Audio manager** — convertit l'audio au format d'Ethos (PCM linéaire,
  32 kHz, mono, 16 bits little-endian). Ajoutez des fichiers avec **+**,
  choisissez un dossier local ou envoyez directement dans le dossier
  `audio` de la radio (en le déplaçant ensuite dans le bon sous-dossier de
  voix), avec ouverture automatique facultative de la destination.

- **Lua development tools** — **Lua Docs** renvoie au guide de référence
  Lua d'Ethos (voir aussi le fil rcgroups *FrSky - ETHOS Lua Script
  Programming*) ; **Lua Demo Scripts** renvoie à des exemples de scripts
  sur le GitHub Ethos-Feedback-Community ; **Debug** ouvre une fenêtre de
  journal en direct pour les traces Lua `print()` envoyées via USB-Serial
  lorsque la radio est en mode Serial :

  1. Connectez la radio à Suite normalement et passez en mode Ethos.
  2. Modifiez les scripts Lua directement sur le lecteur monté de la radio,
     dans n'importe quel éditeur de code.
  3. Ouvrez **Lua Development Tools** → **START DEBUG** — la radio
     redémarre en mode Serial/débogage et réinitialise les scripts.
  4. La sortie `print()` de chaque script actif est diffusée dans le
     terminal de Suite.
  5. **STOP DEBUG** repasse en mode Ethos normal pour poursuivre les
     modifications.

- **DFU Flasher** — flashe le bootloader via une connexion USB hors
  tension (DFU), ce qui fonctionne même avec un firmware totalement
  corrompu, puisque le bootloader ST sous-jacent réside en ROM. **Select
  Bootloader** pour choisir un fichier téléchargé (Suite indique sa
  version/sa compatibilité), connectez la radio **hors tension**, puis
  **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Il s'agit généralement d'un pilote DFU manquant ou incorrect. La
      plupart des PC sous Windows 10+ gèrent les systèmes Tandem avec le
      pilote USB DFU par défaut, mais Windows Update le remplace parfois
      par un pilote générique qui ne fonctionne pas — vérifiez le
      Gestionnaire de périphériques et envisagez un outil comme Impulse
      Driver Fixer. Les utilisateurs de Horus X10 en particulier peuvent
      devoir installer manuellement le pilote USB du bootloader STM32
      (Impulse Driver Fixer ou Zadig), car Windows 10 ne l'installe pas par
      défaut.

- **Repair Tool** — pour les X18/S, TW Lite, XE et X20 Pro/R/RS : reformate
  la mémoire interne lorsque la radio ne parvient pas à lire la NAND ou à
  enregistrer les réglages.

## Section Others

- **Documentation** — liens vers le GitHub Ethos-Feedback-Community, les
  manuels officiels d'Ethos (téléchargeables) et une FAQ Ethos Suite.
- **Ethos Github** — versions et suivi des problèmes (recherchez parmi les
  problèmes existants avant d'en signaler un nouveau).

### Paramètres de Suite

- **Language** — tchèque, allemand, anglais, espagnol, français, hébreu,
  italien, néerlandais, norvégien, portugais, slovène, chinois.
- **Server location** — **FrSky server** ou **GitHub** (nécessaire pour
  l'accès aux versions préliminaires ci-dessus).
- **Debug options** — activer/désactiver la fenêtre d'erreur fatale ;
  activer la journalisation de débogage complète de Suite (pas seulement
  les plantages) ; ouvrir le dossier des journaux.
- **Version** / **Update Suite** — version actuelle et vérification
  manuelle des mises à jour.
- **About** — remerciements pour les composants réutilisés.

## Utilisation en ligne de commande

Ethos Suite peut être lancé depuis un terminal :

| Option | Effet |
|---|---|
| `--help` | Affiche l'aide en ligne de commande. |
| `--version` | Affiche la version de Suite installée. |
| `--list-radios` | Liste toutes les radios FrSky prises en charge. |
| `--radio-components --radio {RADIO}` (ou `--radio auto`) | Liste les composants d'une radio connectée et leurs chemins. `auto` détecte automatiquement ; précisez `{RADIO}` si plusieurs radios sont connectées. |
| `--get-path {COMPONENT}` | Obtient le chemin d'un composant — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO` ou `I18N`. |
| `--serial start` \| `--serial stop` | Active/désactive le mode de débogage série. |

!!! note
    Suite ne démarre pas du tout s'il ne reconnaît pas une commande valide.
