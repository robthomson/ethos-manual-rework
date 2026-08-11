---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Avvisi

![Avvisi](../assets/system-alerts.png)

Quattro avvisi validi per l'intera radio, ciascuno attivabile in modo indipendente — distinti dalle [funzioni speciali](../model-setup/special-functions.md) e dagli [interruttori logici](../model-setup/logical-switches.md) specifici di ciascun modello che si configurano manualmente.

- **Modalità silenziosa** — un avviso vocale all'avvio quando questo controllo è attivo e [Generale → Modalità audio](general.md) è impostata su Silenzioso, come promemoria del fatto che la radio è muta.
- **Tensione principale** — "Radio battery is low" quando la batteria principale della radio scende al di sotto della soglia di **Bassa tensione** impostata in [Batteria](battery.md).
- **Tensione RTC** — "RTC battery is low" quando la batteria a bottone dell'RTC scende al di sotto di 2,5 V (la soglia predefinita). La registrazione dei dati dipende dall'orologio in tempo reale; un orario non valido rende difficile la lettura dei log, in particolare la distinzione tra le diverse sessioni di volo. Questo avviso può essere silenziato temporaneamente in attesa di sostituire la batteria, ma non dovrebbe restare disattivato a tempo indeterminato.
- **Avviso conflitto sensori** — rileva ID di sensori di telemetria in conflitto. Conviene disattivarlo solo se si utilizzano sensori non conformi alla specifica S.Port.
- **Inattività** — un avviso vocale "Prolonged inactivity" (accompagnato da una vibrazione, nel caso in cui il volume sia basso) dopo che la radio è rimasta inutilizzata per un tempo superiore a quello configurato — 10 minuti per impostazione predefinita.
