---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Alerte de capacité batterie

Alerte basée sur la **capacité consommée** (mAh) plutôt que sur la tension — une mesure plus directe de la part du pack réellement utilisée. Deux approches sont possibles, selon le matériel installé.

## Option A : un ESC de la série Neuron

Les ESC Neuron de FrSky transmettent directement la consommation — aucun capteur calculé n'est nécessaire. Réglez [Options du récepteur → Port de télémétrie](../system-setup/devices.md) sur S.Port, connectez le fil de télémétrie du Neuron, puis [découvrez les capteurs](../model-setup/telemetry.md#discovering-sensors) — le capteur qui nous intéresse est **ESC Consumption**.

1. Ajoutez un [interrupteur logique](../model-setup/logical-switches.md) sur `ESC Consumption`, vrai au-dessus de (par exemple) 900 mAh — soit environ 60 % d'un pack dimensionné pour atterrir avec encore ~30 % de réserve.
2. Ajoutez une [fonction spéciale Play audio](../model-setup/special-functions.md), avec le nouvel interrupteur comme condition d'activation, et une étape **Play value** pour `ESC Consumption`.

Comme seconde ligne de défense, les ESC Neuron transmettent également **ESC Voltage** — configurez un second interrupteur logique de la même manière que dans [Alerte de tension batterie basse](low-battery-warning.md) (en dessous de 3,4 V/élément — soit 13,6 V pour un pack 4S), avec sa propre fonction Play audio répétée toutes les 5 secondes.

## Option B : un capteur de courant + un capteur calculé

Si l'ESC ne transmet pas la consommation, un capteur de courant (par exemple FrSky FASxxx) associé à un [capteur calculé **Consumption**](../model-setup/telemetry.md#calculated-sensors) remplit la même fonction.

### 1. Connecter et découvrir

![Capteur de courant](../assets/how-to-consumption-telemetry-current-sensor.png)

Connectez le fil S.Port du capteur de courant et lancez la découverte — il apparaît sous le nom **Current**. Réglez sa **Plage** pour correspondre au capteur (par exemple 0–100 A pour un FAS100) :

![Édition du capteur de courant](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Créer le capteur calculé Consumption

![Créer un capteur calculé](../assets/how-to-consumption-create-calc-select.png)
![Capteur Consumption](../assets/how-to-consumption-create-calc-sensor.png)

Dans Télémétrie, **Créer un capteur calculé** → **Consumption**. Réglez l'unité sur `mAh` et la **Plage** sur la capacité du pack (par exemple 2800 mAh) ; la **Source** sur `Current`.

![Édition du capteur](../assets/how-to-consumption-sensor-edit.png)
![Édition du capteur 2](../assets/how-to-consumption-sensor-edit2.png)

Réglez **Reset** sur l'événement système `!Telemetry Active` — sélectionnez **Telemetry Active**, faites un appui long sur `ENT`, puis choisissez **Inverser** — afin que le total cumulé soit remis à zéro automatiquement dès que la télémétrie est perdue (c'est-à-dire lorsque le modèle est mis hors tension).

### 3. Annonces par palier

![Interrupteur logique Δ 200 mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Ajoutez un interrupteur logique utilisant la fonction **Δ > X** sur `Consumption`, qui se déclenche chaque fois que la valeur augmente d'un pas fixe — par exemple tous les 200 mAh, une fraction commode d'un pack de 2800 mAh.

!!! tip
    Réglez **Intervalle de vérification** sur `---` (infini) afin que le cumul se poursuive indéfiniment vers le seuil suivant plutôt que d'être réinitialisé après une fenêtre fixe. Donnez à **Durée minimale** une petite valeur non nulle pendant la mise au point — à 0,0 le déclenchement est trop bref pour être visible à l'écran.

Ajoutez une fonction Play audio, avec cet interrupteur comme condition d'activation, et une étape Play value pour `Consumption` :

![Annonce du delta](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value : consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Alerte de capacité basse

![Second interrupteur logique](../assets/how-to-consumption-lsw2-play-battlow.png)

Un second interrupteur logique se déclenche une seule fois, au-delà d'un seuil bas strict de capacité — par exemple 2000 mAh sur un pack de 2800 mAh — associé à une fonction Play audio répétée toutes les 10 secondes jusqu'à la réinitialisation du modèle :

![Play value sur batterie basse](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value : consumption sur batterie basse](../assets/how-to-consumption-sf2-play-value-consumption.png)
