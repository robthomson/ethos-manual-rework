---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Varování při vyčerpání kapacity baterie

Varování podle **odebrané kapacity** (mAh) namísto napětí — jde o
přímější měřítko toho, kolik z akumulátoru bylo skutečně spotřebováno.
K cíli vedou dvě cesty podle toho, jaký hardware je instalován.

## Varianta A: regulátor řady Neuron

Regulátory FrSky Neuron hlásí spotřebu přímo — není potřeba žádný
vypočítaný senzor. Nastavte [Volby přijímače → Telemetrický
port](../system-setup/devices.md) na S.Port, připojte telemetrický vodič
regulátoru Neuron a [vyhledejte
senzory](../model-setup/telemetry.md#discovering-sensors) — hledaným
senzorem je **ESC Consumption**.

1. Přidejte [logický přepínač](../model-setup/logical-switches.md) na
   `ESC Consumption`, pravdivý nad (například) 900 mAh — což je přibližně
   60 % kapacity akumulátoru dimenzovaného tak, aby po přistání zůstalo
   ještě ~30 % rezervy.
2. Přidejte [speciální funkci Play
   audio](../model-setup/special-functions.md) s aktivační podmínkou
   tímto novým přepínačem a s krokem **Play value** pro `ESC
   Consumption`.

Jako druhou linii obrany hlásí regulátory Neuron také **ESC Voltage** —
nastavte druhý logický přepínač stejným způsobem jako u [varování při
nízkém napětí baterie](low-battery-warning.md) (pod 3,4 V na článek —
tedy např. 13,6 V pro 4S akumulátor), s vlastní funkcí Play audio
opakovanou každých 5 sekund.

## Varianta B: senzor proudu + vypočítaný senzor

Pokud regulátor spotřebu nehlásí, stejnou úlohu zajistí senzor proudu
(např. FrSky FASxxx) v kombinaci s [vypočítaným senzorem
**Consumption**](../model-setup/telemetry.md#calculated-sensors).

### 1. Připojení a vyhledání

![Senzor proudu](../assets/how-to-consumption-telemetry-current-sensor.png)

Připojte vodič S.Port senzoru proudu a vyhledejte jej — objeví se jako
**Current**. Nastavte jeho **Range** tak, aby odpovídal senzoru (např.
0–100 A pro FAS100):

![Úprava senzoru proudu](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Vytvoření vypočítaného senzoru Consumption

![Vytvoření vypočítaného senzoru](../assets/how-to-consumption-create-calc-select.png)
![Senzor Consumption](../assets/how-to-consumption-create-calc-sensor.png)

V nabídce Telemetrie zvolte **Create Calculated Sensor** →
**Consumption**. Nastavte jednotky na `mAh` a **Range** na kapacitu
akumulátoru (např. 2800 mAh); **Source** na `Current`.

![Úprava senzoru](../assets/how-to-consumption-sensor-edit.png)
![Úprava senzoru 2](../assets/how-to-consumption-sensor-edit2.png)

Nastavte **Reset** na systémovou událost `!Telemetry Active` — vyberte
**Telemetry Active**, dlouze stiskněte `ENT` a zvolte **Invert** — aby se
průběžný součet automaticky vynuloval, jakmile telemetrie vypadne (tedy
při vypnutí napájení modelu).

### 3. Hlášení dílčích mezníků

![Logický přepínač Δ 200 mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Přidejte logický přepínač s funkcí **Δ > X** na `Consumption`, který se
aktivuje vždy, když hodnota vzroste o pevný krok — např. každých 200 mAh,
což je vhodný díl kapacity 2800mAh akumulátoru.

!!! tip
    Nastavte **Check interval** na `---` (nekonečno), aby se hodnota
    neomezeně kumulovala až k dalšímu prahu místo vynulování po pevně
    daném intervalu. Během ladění dejte parametru **Min Duration** malou
    nenulovou hodnotu — při 0,0 je aktivace příliš krátká, než aby byla
    na displeji vidět.

Přidejte funkci Play Audio s aktivační podmínkou tímto přepínačem a s
krokem Play value pro `Consumption`:

![Hlášení dílčího přírůstku](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Varování při nízké zbývající kapacitě

![Druhý logický přepínač](../assets/how-to-consumption-lsw2-play-battlow.png)

Druhý logický přepínač se aktivuje jednorázově při překročení pevného
prahu nízké kapacity — např. 2000 mAh z 2800mAh akumulátoru — v kombinaci
s funkcí Play Audio opakovanou každých 10 sekund, dokud není model
resetován:

![Play value při nízkém stavu baterie](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value: consumption při nízkém stavu baterie](../assets/how-to-consumption-sf2-play-value-consumption.png)
