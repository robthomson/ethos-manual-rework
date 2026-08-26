# Operazioni a linea di Commando

FrSky Suite può essere eseguito dalla riga di comando di un terminale.

Sono disponibili le seguenti opzioni da riga di comando:

| --help | Testo di aiuto per lo strumento da riga di comando FrSky Suite. |
| --- | --- |
| --version | Mostra la versione di FrSky Suite installata. |
| --list-radios | Elenca tutte le radio FrSky supportate. |
| --radio-components<br>--radio {RADIO}<br>--radio auto | Elenca tutti i componenti e i relativi percorsi. <br>Se al computer sono collegate più schede radio, è possibile utilizzare \[--radio {RADIO}\] per indicarne uno. <br>In caso contrario, è possibile ometterlo \[--radio {RADIO}\] o usa  \[--radio auto\] per il rilevamento automatico. |
| --get-path {COMPONENT} | Ottieni il percorso del componente specificato. <br>Componenti attualmente supportati: BITMAPS, SCRIPTS, SCREENSHOTS, AUDIO, I18N. |
| --serial start\|stop | abilitare/disabilitare la modalità di debug seriale. |

Avviso: l'app Suite non si avvierà a meno che non riconosca correttamente un comando.
