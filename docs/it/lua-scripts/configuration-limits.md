# Limiti di configurazione dello scripting Lua

- 2MB per le bitmap (una bitmap a schermo intero su X20 consuma 768K)

- 2MB per gli script Lua (si tratta di una quantità elevata)

Evita di utilizzare troppa ram per le mappe bit. Si suggerisce agli utenti di utilizzare il caricamento pigro = caricare una bitmap SOLO quando serve. Poi la manterrà in memoria per l'uso successivo, per evitare letture multiple dalla scheda SD o dalla eMMC.
