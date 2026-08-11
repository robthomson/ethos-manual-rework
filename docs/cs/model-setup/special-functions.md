---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# Speciální funkce

![Nabídka speciálních funkcí](../assets/model-sf-menu.png)

Speciální funkce spustí akci — přehrání zvuku, vytvoření snímku
obrazovky, zápis logů, vibrační odezvu a další — jakmile je splněna
zadaná podmínka. Podporováno je až 100 funkcí; ve výchozím stavu není
definována žádná. Novou přidáte tlačítkem **+**; klepnutím na existující
získáte volby **Upravit**/**Přesunout**/**Kopírovat-vložit**/
**Klonovat**/**Smazat**.

![Přidání speciální funkce](../assets/model-sf-add.png)
![Přesunutí](../assets/model-sf-move.png)

## Pole společná pro všechny akce

- **Stav** — povolí či zakáže tuto funkci, aniž byste ji museli mazat.
- **Podmínka aktivace** — **Vždy zapnuto**, nebo podmíněná polohou
  přepínače/funkčního přepínače/logického přepínače/trimu, případně
  letovým režimem. Dlouhým stiskem `ENT` na přepínači a zatržením
  **Negativní** jej invertujete (např. `SG-up` se změní na `!SG-up`,
  aktivní vždy, když SG *není* nahoře).
- **Globální** — přidá tuto funkci do **každého** modelu, existujícího i
  budoucího. Pokud už model obsahuje shodně nastavenou lokální funkci,
  volba Globální ji přidá jako další samostatnou položku; vypnutím volby
  Globální se funkce odstraní ze všech modelů kromě právě zvoleného.
  Globální funkce jsou uloženy v `radio.bin`, lokální v souboru modelu.

## Akce {: #actions }

**Reset** — resetuje **Letová data** (telemetrii + časovače), **Všechny
časovače** nebo **Celou telemetrii**.

![Reset](../assets/model-sf-reset.png)

**Snímek obrazovky** — uloží snímek obrazovky do složky `screenshots/` na
SD card/eMMC.

![Snímek obrazovky](../assets/model-sf-screenshot.png)

**Nastavit failsafe** — uloží aktuální polohy kanálů jako failsafe,
prostřednictvím interního nebo externího RF **Modulu**.

![Nastavit failsafe](../assets/model-sf-set-failsafe.png)

**Přehrát zvuk** — nejbohatší akce, podporující celou sekvenci:

![Přehrát zvuk](../assets/model-sf-play-audio.png)

- **Hlas** — který z až 3 nakonfigurovaných hlasů se použije (viz
  [Obecné](../system-setup/general.md#audio-settings)).
- **Opakování** — přehrát jednou, nebo opakovat v nastavitelném intervalu
  (až 10 minut).
- **Vynechat při startu** — potlačí spuštění této funkce během startu.
- **Sekvence** — až 100 kroků, každý jednoho z těchto typů:

  - **Přehrát soubor** — přehraje zvolený zvukový soubor.

    ![Přehrát soubor](../assets/model-sf-play-audio-add-play-file.png)

  - **Přehrát hodnotu** — vysloví hodnotu zdroje: analogových ovladačů,
    přepínačů, logických přepínačů, trimů, kanálů, gyra, systémových
    hodin, trenéra, časovačů nebo telemetrie.

    ![Přehrát hodnotu](../assets/model-sf-play-audio-add-play-value.png)

  - **Čekat po dobu** — pevná pauza, až 10 minut.
  - **Čekat na podmínku** — pozastaví sekvenci, dokud není podmínka
    splněna.

  ![Přidání řádku sekvence](../assets/model-sf-play-audio-add-line.png)
  ![Typ řádku sekvence](../assets/model-sf-play-audio-add-line-type.png)

  Například: přehrát `vfrlow.wav`, jakmile se logický přepínač `VFRlow`
  stane aktivním, a poté vyslovit zaznamenanou minimální hodnotu VFR —

  ![Přehrání hodnoty po souboru](../assets/model-sf-play-audio-add-play-value-add-line.png)

  — nebo pozastavit sekvenci, dokud se přepínač SH nepřesune dolů:

  ![Sekvence s podmínkou čekání](../assets/model-sf-play-audio-add-sequence.png)

  Klepnutím na kterýkoli řádek sekvence jej lze upravit, přidat další,
  změnit pořadí nebo jej smazat:

  ![Správa sekvence](../assets/model-sf-play-audio-add-sequence-management.png)

**Vibrace** — vibrační odezva:

![Vibrace](../assets/model-sf-haptic.png)

- **Vzor** — jednoduchý, dvojitý, trojitý, pětinásobný nebo velmi krátký.

  ![Vzor vibrací](../assets/model-sf-haptic-pattern.png)

- **Intenzita** — 1–10 (výchozí 5).
- **Opakování** — jednorázově, nebo v nastaveném intervalu.
- **Volba vibračních motorků** — u vysílačů s vibračními motorky v gimbalech
  (X20 Pro AW, X20RS nebo X20 Pro/X20R vybavený gimbaly MC20R — viz
  [Hardware](../system-setup/hardware.md#radio-specific-hardware-options)):
  **Výchozí** (interní vibrace), **Všechny motorky**, **Levá páčka** nebo
  **Pravá páčka**.

  ![Vibrace na X20 Pro AW](../assets/model-sf-haptic-x20proaw.png)

**Zápis logů** — zapisuje logy `.csv` do složky `Logs/` na SD card/eMMC,
s časovou značkou z RTC (nezbytné pro pozdější rozlišení jednotlivých
letových sezení):

![Zápis logů](../assets/model-sf-write-logs.png)

- **Interval zápisu** — 100–500 ms.
- **Páčky/Potenciometry/Posuvníky**, **Přepínače**, **Logické přepínače**,
  **Kanály** — nezávisle přepínatelné kategorie zaznamenávaných dat.

  **Zobrazení logů**: otevřete soubor logu ze složky `/Logs` ve Správci
  souborů. Zvolte, které kanály se mají vykreslit (RSSI je vybráno
  standardně); posouvat lze rotačním enkodérem nebo přejetím prstem,
  přibližovat otáčením enkodéru při současném držení `PAGE`. Tlačítko
  `DISP` přesune zaměření na první tlačítko v pravém sloupci.

**Přehrát text** (pouze X20 Pro) — syntéza řeči přímo ve vysílači místo
předem nahraného souboru:

![Přehrát text](../assets/model-sf-x20pro-play-text.png)

- **Text** — řetězec, který se má vyslovit. VELKÁ PÍSMENA se hláskují po
  jednotlivých znacích (např. „OFF“ → „O-F-F“), malá písmena se vysloví
  jako slovo („off“).
- **Opakování**, **Vynechat při startu** — jak je popsáno výše.

**Přejít na obrazovku** — přepne displej na zvolenou obrazovku, například
na záznam letových dat přijímače po stisknutí tlačítka:

![Přejít na obrazovku](../assets/model-sf-go-to-screen.png)
![Volby obrazovek](../assets/model-sf-go-to-screen-options.png)

**Zamknout dotykovou obrazovku** — zamkne dotykovou obrazovku proti
nechtěnému ovládání (dostupné také přímo podržením `ENT` + `PAGE` po dobu
1 s na domovské obrazovce):

![Zamknout dotykovou obrazovku](../assets/model-sf-lock-touchscreen.png)

**Načíst model** — po spuštění načte zadaný **Model**, volitelně s
**Potvrzením** před samotným přepnutím:

![Načíst model](../assets/model-sf-load-model.png)

**Přehrát vario** — ovládá zvuk varia podle zvoleného zdroje (obvykle
senzor VSpeed varia FrSky, ale funguje jakýkoli senzor s jednotkou m/s):

![Přehrát vario](../assets/model-sf-play-vario.png)
![Zdroj varia: VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **Rozsah** — rychlost stoupání/klesání přiřazená výšce tónu, výchozí
  ±10 m/s (až ±100 m/s). Nad hodnotou **Střed** roste výška tónu lineárně
  s rychlostí stoupání až po maximální hodnotu Rozsahu (výška tónu při
  maximální rychlosti se nastavuje v [Obecné →
  Vario](../system-setup/general.md#vario)); při klesání se ozývá
  nepřerušovaný tón, jehož výška klesá směrem k minimální hodnotě
  Rozsahu.
- **Střed** — pásmo „nulového stoupání“, výchozí ±0,3 m/s (až ±2 m/s);
  uvnitř tohoto pásma je výška tónu stálá (výška tónu při nulové
  rychlosti se rovněž nastavuje v Obecné → Vario). Přepnutím z **Pípání**
  na **Ticho** tón úplně vypnete.

  ![Volby rozsahu/středu varia](../assets/model-sf-play-vario-options.png)
