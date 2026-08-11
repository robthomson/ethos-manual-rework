---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Časovače

![Časovače](../assets/model-timers.png)

Osm plně programovatelných časovačů, každý s odpočítáváním nahoru nebo dolů.
Nový přidáte pomocí **+** vedle záhlaví sloupců nebo přes **Add** níže.
Dotykem na časovač se otevřou volby reset/úprava/přidání/přesun/kopírovat-vložit.

![Úprava časovače](../assets/model-timer1-edit.png)

## Společná pole (odpočet dolů i nahoru)

- **Value** — aktuální hodnota časovače.
- **Name** — editovatelný.
- **Mode** — **Up** (nahoru) nebo **Down** (dolů).
- **Start value** (pouze při odpočtu dolů) — hodnota, od které se odpočítává.
- **Alarm Value** (pouze při počítání nahoru) — hodnota, při níž je časovač
  považován za uplynulý; počítá dál i za ni, ale ve widgetech časovače se
  zobrazuje červeně.
- **Start condition** — spouští časovač. Pokud je **Stop condition**
  ponechána na výchozí hodnotě, řídí podmínka spuštění samostatně start *i*
  stop. V ostatních případech se časovač spustí při prvním splnění podmínky
  spuštění a od té chvíle běží dál.
- **Stop condition** — pokud není ponechána na výchozí hodnotě, řídí běžící
  časovač: při splnění podmínky je zastaven, při nesplnění běží. V níže
  uvedeném příkladu se časovač spustí, když se `ThrottleActive` stane
  pravdivým, a zastaví se, jakmile již není aktivní telemetrie:

  ![Podmínka zastavení](../assets/model-timer1-edit-stop.png)

- **Proportional timing source** — `---` znamená počítání v reálném čase.
  Jakýkoli jiný zdroj (např. páčka plynu nebo kanál plynu) mění rychlost
  časovače: při −100 % je časovač zastaven, při +100 % běží rychlostí
  reálného času a mezi těmito hodnotami se mění proporcionálně.
- **Reset** — přepínač, funkční přepínač, logický přepínač nebo poloha trimu,
  která časovač resetuje; časovač zůstává vynulovaný po celou dobu, kdy je
  podmínka splněna.
- **Persistent** — zachová hodnotu časovače při vypnutí nebo změně modelu
  a při dalším použití modelu ji znovu načte.
- **Voice** — který [hlasový balíček](../system-setup/general.md#audio-settings)
  tento časovač ohlašuje.

## Zvukové akce

![Přidání zvukové akce](../assets/model-timer1-add-action.png)
![Typ akce](../assets/model-timer1-action-type-select.png)
![Akce odpočtu](../assets/model-timer1-action-countdown.png)

Plně flexibilní konfigurace upozornění pro každý časovač. Každá akce má svůj
typ — **Countdown** (mluvený), **Beep countdown** (pípání místo řeči),
**Play file** nebo **Play value** — a dále:

- **Start** — hodnota, od které odpočet této akce začíná.
- **Step** — interval ohlašování, až 10 minut (600 s).
- **Haptic** — doplní ohlášení vibrací.

Typická sestava tří akcí:

![Přehled akcí](../assets/model-timer1-actions-summary.png)
![Akce časovače 2](../assets/model-timer2-actions-summary.png)

1. Mluvený odpočet začínající při zbývajících 2:00, každých 30 s, s vibrací.
2. Pípající odpočet začínající při zbývajících 0:10, každou 1 s, s vibrací.
3. Vlastní soubor (např. `timer-1-elapsed`) přehraný při uplynutí, s vibrací.

Další akce přidáte pomocí **Add**; seznam se vykonává v pořadí priority,
přičemž **nejvyšší priorita je poslední**.

Viz také [widget displeje Timer Log](../displays/index.md#widget-types)
pro průběžný záznam předchozích běhů časovače.

![Widget časovače](../assets/model-timers-widget.png)
