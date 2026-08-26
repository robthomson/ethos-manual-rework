# Procedura per la migrazione a FrSky Suite

- Assicurati di avere almeno la versione 1.1.4 di Ethos, la versione minima necessaria per flashare il nuovo bootloader compatibile con FrSky Suite (formato FRSK) dal File Manager della radio. In caso contrario, dovrai aggiornare manualmente alla versione 1.1.4 per poter migrare a FrSky Suite per gli aggiornamenti automatici.

- Fai un backup della tua scheda SD o eMMC (è consigliabile copiare tutto in una cartella del computer).

- Scarica da [https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases ](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)il file zip del bootloader più recente per la tua radio e decomprimilo. Le versioni attuali del bootloader sono elencate in un file chiamato components.json che elenca tutti i componenti utilizzati in una release. Il file viene pubblicato con ogni nuova versione del firmware e può essere aperto con un editor di testo come Note Pad.

- Cerca la tua radio tra le voci "obiettivi", quindi il numero di versione del Bootloader sarà elencato sotto. Troverai il Bootloader elencato nelle risorse della release di Ethos con quel numero.

- Accendi la radio in modalità bootloader (tieni premuto il tasto enter, tienilo premuto e poi premi power ON) e collega il sistema al PC con un cavo USB dati.

- Copia il bootloader in una cartella della scheda SD o dell'eMMC (di solito la cartella Firmware), quindi espelli le unità e scollega la radio dal PC.

- Avvia la radio, vai su System / File Manager, tocca il file bootloader.frsk che hai appena copiato e seleziona l'opzione "Flash bootloader".

- Scarica e installa FrSky Suite. A questo punto dovresti essere in grado di seguire le sezioni seguenti per aggiornare il firmware della radio e i file della scheda Flash e SD o eMMC alle versioni più recenti e per utilizzare le altre funzioni della FrSky Suite.

- Tieni presente che potrebbe essere necessario rinominare la cartella bitmaps/user sulla scheda SD o eMMC in bitmaps/models se FrSky Suite non lo fa per te. Questa è la cartella in cui sono memorizzate le bitmap degli utenti.
