---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Matériel

![Vérification du matériel](../assets/system-hardware-check-x20s.png)

Test et calibration des commandes physiques de la radio, définition du type
des interrupteurs et mappage des touches d'accueil.

## Vérification du matériel {: #hardware-check }

Sollicite chaque entrée physique afin de confirmer que chacune est
correctement détectée.

![Vérification du matériel X20 Pro](../assets/system-hardware-check-x20pro.png)
![Vérification du matériel X18S](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — vérifie également les deux boutons-poussoirs à
  verrouillage **K** et **L** situés sur les épaules arrière, ainsi que les
  trims supplémentaires **T5**/**T6**.
- **X18** — vérifie également les trims supplémentaires **T5**/**T6**.

## Calibration des analogiques {: #analogs-calibration }

![Calibration des analogiques](../assets/system-hardware-analogs-calibration.png)

Indique à la radio la position exacte du centre et des butées de chaque
manche, potentiomètre et curseur. Cette procédure est exécutée
automatiquement au premier démarrage ; répétez-la après le remplacement d'un
manche, d'un potentiomètre ou d'un curseur.

## Calibration du gyroscope

![Calibration du gyroscope](../assets/system-hardware-gyro-calibration.png)

Calibre le gyroscope intégré afin que les entrées basées sur l'inclinaison
réagissent correctement lorsque vous inclinez la radio — la position
« à plat » devient celle dans laquelle vous tenez habituellement la radio.
Cette procédure est également exécutée automatiquement au premier démarrage.

## Filtre des analogiques

Filtre ADC activable/désactivable pour les manches, activé par défaut — il
réduit les tremblements autour du centre du manche. Il s'agit du réglage
**global** ; il existe aussi une surcharge **par modèle** du filtre des
analogiques dans [Édition du modèle](../model-setup/model-edit.md).

## Réglages des potentiomètres/curseurs {: #potssliders-settings }

Permet de renommer les potentiomètres et les curseurs. Le **X20 Pro/R/RS**
prend en outre en charge deux potentiomètres supplémentaires,
**Ext1**/**Ext2**, généralement utilisés pour des manches à 3 axes.

![Valeurs ADC, potentiomètres](../assets/system-hardware-pots-x20s.png)
![Valeurs ADC, potentiomètres (X20 Pro)](../assets/system-hardware-pots-x20pro.png)

## Réglages des interrupteurs {: #switches-settings }

![Interrupteurs](../assets/system-hardware-switches.png)

- **Délai de détection de la position médiane** — empêche qu'un basculement
  rapide haut→bas (ou bas→haut) d'un interrupteur 3 positions n'enregistre
  momentanément la position médiane ; celle-ci ne doit être prise en compte
  que lorsque l'interrupteur s'y arrête effectivement. La valeur par défaut
  est 0 ms, choisie pour convenir à la détection d'« auto-test » des
  récepteurs stabilisés FrSky sur la voie CH12.
- **Type d'interrupteur** — chaque interrupteur SA–SJ peut être défini comme
  **None**, **Momentary**, **2 POS** ou **3 POS**, ce qui permet d'échanger
  les fonctionnalités entre interrupteurs physiques (par exemple attribuer à
  l'interrupteur momentané SH le rôle normalement tenu par l'interrupteur
  2 positions SF) — dans la limite de ce que le câblage de la radio permet
  réellement (un rôle 3 positions ne peut généralement pas être attribué à un
  matériel qui n'est pas câblé pour cela).

  ![Options des interrupteurs](../assets/system-hardware-switches-options.png)
  ![Interrupteurs supplémentaires](../assets/system-hardware-switches-2.png)

- **Renommage** — les interrupteurs peuvent être renommés de SA–SJ vers des
  noms personnalisés ; ces noms sont globaux pour tous les modèles.
- **X20 Pro** — ajoute les boutons-poussoirs **K**/**L** sur les épaules
  arrière, ainsi que les positions **M**/**N** si elles sont câblées
  (généralement pour des interrupteurs en bout de manche).

## Mappage des touches d'accueil

Redéfinit la destination des touches d'accueil `SYS`, `MDL` et `DISP`
(`TELE` sur les radios plus anciennes).

- **`DISP`** — l'appui court comme l'appui long peuvent être réaffectés à
  n'importe quelle page Modèle, page Système, à Configurer les écrans, à
  Accueil ou à l'enregistrement des données de vol. Par souci de cohérence
  avec la série X10, l'appui long sur `DISP` est conventionnellement réglé
  sur Configurer les écrans.
- **`SYS`/`MDL`** — seul l'appui long est réaffectable (vers le même
  ensemble de destinations) ; un appui court ouvre toujours respectivement
  la section Système ou Modèle.

## Options matérielles spécifiques à chaque radio {: #radio-specific-hardware-options }

- **Activation des manches haptiques** (X20 Pro, X20R) — les X20 Pro AW et
  X20RS sont livrés avec des manches MC20R équipés de moteurs de vibration
  haptique ; si des manches MC20R ont été installés en rétrofit sur un
  X20 Pro ou un X20R, activez-les ici (voir
  [Fonctions spéciales](../model-setup/special-functions.md) pour la
  configuration des motifs haptiques eux-mêmes).

  ![Haptique (X20 Pro)](../assets/system-hardware-haptic-x20pro.png)
  ![Haptique (X20 Pro AW)](../assets/system-hardware-haptic-x20proaw.png)

- **Option de l'encodeur** (X20 Pro AW, X20R/RS) — ces radios disposent d'un
  encodeur rotatif plus sensible ; activez les **demi-pas** pour en atténuer
  la sensibilité.

  ![Option de l'encodeur (X20 Pro AW)](../assets/system-hardware-x20proaw-encoder-option.png)

## Inspecteur des valeurs ADC {: #adc-value-inspector }

Affiche les valeurs brutes de conversion analogique-numérique lues par le
processeur pour chaque entrée analogique :

![Vérification ADC (X20S)](../assets/system-hardware-adc-check-x20s.png)
![Vérification ADC (X20 Pro)](../assets/system-hardware-adc-check-x20pro.png)

**X20S** : 1 manche gauche horizontal, 2 manche gauche vertical, 3 manche
droit vertical, 4 manche droit horizontal, 5 Pot 1, 6 Pot 2, 7 curseur
central, 8 curseur gauche, 9 curseur droit.

**X20 Pro** : identique à ce qui précède, mais avec deux voies
supplémentaires de potentiomètres externes (7 Ext1, 8 Ext2 — par exemple des
potentiomètres montés sur les manches) insérées avant les curseurs, qui
deviennent 9 curseur central, 10 curseur gauche, 11 curseur droit.
