---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Configurer un système FBUS

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (anciennement
F.Port2) regroupe le contrôle et la télémétrie sur une seule ligne, permettant à
plusieurs périphériques FBUS de partager une unique liaison en guirlande, avec
configuration sans fil complète. Ce guide explique le câblage de deux servos Xact
sur les voies d'ailerons (1 et 5) de l'[exemple d'avion de
base](../tutorials/basic-fixed-wing.md).

!!! note "Captures d'écran à venir"
    Cette page ne comporte pas encore de captures d'écran du simulateur — voir
    [Chaîne de production des captures](../contributing/screenshot-pipeline.md).

## 1. Télécharger le firmware le plus récent

FBUS exige un firmware à jour, tant sur le récepteur que sur les périphériques —
par exemple, les servos Xact nécessitent la version v2.0.1 ou supérieure.
Récupérez les mises à jour correspondantes sur la
[page de téléchargement FrSky](https://www.frsky-rc.com/download/).

## 2. Flasher le firmware

Copiez les fichiers de firmware dans le dossier `Firmware/` de la carte SD /
eMMC. Dans le [Gestionnaire de
fichiers](../system-setup/file-manager.md), branchez le servo sur le connecteur
S.Port de la radio (fil blanc/jaune vers l'encoche), sélectionnez le fichier de
firmware, puis **Flash External Device**.

## 3 / 5. Configurer les ID physiques

Les deux servos utilisent par défaut l'ID physique `0C` hex / l'ID d'application
`6800` hex — ils entreront en conflit sur le bus partagé si l'un des deux n'est
pas modifié. Deux méthodes sont possibles selon le type de récepteur :

**Via le connecteur S.Port de l'émetteur** (tout récepteur) :

1. Branchez le servo 1, allez dans **Device Config → XAct**, réglez **Module**
   sur **S.Port connector**. Laissez l'ID physique `0C` / l'ID d'application
   `6800` et la voie `CH1` à leurs valeurs par défaut, puis **Save to flash**.
2. Branchez le servo 2 à la place, dans le même menu. Changez l'**ID physique**
   en `0D` hex et l'**ID d'application** en `6801` hex (voir le [tableau des ID
   physiques](../model-setup/telemetry.md#how-frsky-telemetry-works) pour
   connaître les emplacements libres), réglez la **voie** sur `CH5`, puis
   **Save to flash**.

**Directement via le récepteur** (par exemple TD-R18 Tandem, avec les deux servos
câblés simultanément — voir l'[étape 4](#4-configure-the-receiver-for-fbus)) :

1. Avec le servo 1 seul connecté (par exemple sur la Pin1 du récepteur), allez
   dans **Device Config → XAct**, **Module** → **Internal module**. Confirmez les
   valeurs par défaut (`0C` / `6800` / `CH1`), puis **Save to flash**.
2. Avec le servo 2 seul connecté (Pin5), même menu (Device Config ne dialogue
   qu'avec un servo à la fois) — passez à `0D` / `6801` / `CH5`, puis **Save to
   flash**. Sélectionnez de nouveau Device Config ensuite pour vérifier que la
   modification a bien été prise en compte.

## 4. Configurer le récepteur pour FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro** : [Système RF](../model-setup/rf-system.md) → le bouton du récepteur
→ **Options** → réglez **Telemetry Port** sur **FBUS**. Les servos Xact se
raccordent alors en guirlande sur ce port ; comme chaque servo ne possède qu'un
seul connecteur, un répartiteur multivoies F.Port2 (FP2CH4/6/8) permet de le
diviser vers plusieurs servos.

**TD-R18 Tandem** : Système RF → le bouton du récepteur → **Options** → réglez
individuellement les broches (par exemple **Pin1**, **Pin5**) sur **FBUS** —
autant de broches que nécessaire peuvent être réaffectées ainsi, ce qui évite
totalement les répartiteurs ; chaque broche affectée à FBUS transporte le même
signal FBUS.

## 5. Vérifier le contrôle FBUS des servos

Branchez le servo 1 sur la Pin1 et le servo 2 sur la Pin5 (les voies d'ailerons
de l'exemple d'avion), mettez sous tension, et vérifiez que les voies 1 et 5
actionnent les bons servos.

## 6. Vérifier la télémétrie FBUS

Avec les deux servos connectés, supprimez les éventuels capteurs `SRV` existants
dans [Télémétrie](../model-setup/telemetry.md) et relancez la découverte. Chaque
servo transmet 4 capteurs : courant, tension, température et état (`OK` en
fonctionnement normal).

## 7. Modifier la configuration ultérieurement

Une fois le modèle entièrement câblé, isoler un servo pour le reconfigurer via
Device Config n'est pas pratique. Procédez plutôt ainsi : allez dans Télémétrie,
repérez un capteur appartenant au servo concerné (par exemple `SRV1 curr`) et
choisissez **Configure** — cela ouvre directement la configuration de ce servo.
Effectuez **Save to flash** après chaque modification.

!!! warning
    Ne modifiez pas par inadvertance l'ID physique ou l'ID d'application depuis
    cet écran — c'est ce qui garantit que chaque servo reste adressable sur le
    bus partagé.
