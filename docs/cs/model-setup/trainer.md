---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Ve výchozím nastavení vypnuto. Nastavte vysílač jako **Master** (vysílač
instruktora, který přijímá až 16 ovládacích prvků od žáka) nebo **Slave**
(vysílač žáka, který instruktorovi odesílá nastavitelný počet kanálů).

## Režim Master

![Režim Master](../assets/model-trainer-master.png)
![Možnosti Traineru](../assets/model-trainer-options.png)

### Režim spojení

![Možnosti režimu spojení](../assets/model-trainer-link-mode-options.png)

- **Trainer cable** — 3,5mm mono audio kabel mezi oběma vysílači.
- **Bluetooth** —

  ![Spojení přes Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Mode** — normální nebo vysoká rychlost; vysokou rychlost použijte
    pro nižší latenci, pokud ji podporují oba vysílače.

    ![Režim Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Local name** — název BT zobrazovaný ostatním zařízením (výchozí
    `FrSkyBT`, lze upravit).
  - **Local address** — Bluetooth adresa tohoto vysílače.
  - **Distant address** — adresa spárovaného vysílače po vytvoření
    spojení.
  - **Search devices** (pouze v režimu Master) — vyhledá zařízení
    v okolí:

    ![Vyhledávání](../assets/model-trainer-link-mode-bt-search.png)
    ![Čekání](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Výběr zařízení](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Připojeno](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Connect Last Device** / **Reset Module** — znovu se připojit
    k předchozímu párování, nebo úplně vymazat konfiguraci Bluetooth
    modulu.

- **SBUS external module** — vstup SBUS na pinu PXX-IN šachty externího
  modulu, umožňující připojit FrSky přijímač s výstupem SBUS (např.
  Archer RS) jako přijímací stranu bezdrátového spojení — díky tomu může
  jako strana žáka (buddy box) fungovat **jakýkoli** FrSky vysílač
  spárovaný s tímto přijímačem.
- **CPPM external module** — totéž prostřednictvím vstupu CPPM, pro
  starší přijímač s výstupem CPPM.

### Podmínka aktivace

![Podmínka aktivace](../assets/model-trainer-active-condition.png)

Přepínač/tlačítko, funkční přepínač, logický přepínač, poloha trimu nebo
letový režim, který po aktivaci předá řízení žákovi.

### Kanály Traineru

![Úprava podmínky aktivace](../assets/model-trainer-active-condition-edit.png)

Dokud je podmínka aktivace splněna, může se od žáka k učiteli přenášet až
16 kanálů. Klepnutím na kanál jej nakonfigurujete samostatně:

- **Active condition** — přepsání nastavení pro jednotlivý kanál, např.
  pro vyřazení pouze vstupu výškovky žáka pro část výcviku.
- **Mode** — **OFF** (pro Trainer vypnuto), **Add** (signály učitele
  a žáka se sčítají, takže na ovládací prvek mohou působit oba současně)
  nebo **Replace** (normální režim — žák má nad tímto kanálem plnou
  kontrolu, dokud je aktivní).
- **Percent** — škáluje vstup žáka, běžně 100 %.
- **Destination** — na kterou funkci se kanál žáka mapuje.

Praktický příklad, jak instruktor okamžitě přebírá řízení pomocí
přepínače, najdete v [Praktický návod: Okamžité převzetí
řízení](../how-to/instant-takeback.md) a informace o vyloučení pohybu
páček žáka z logického přepínače, který sleduje vlastní páčky instruktora,
v části [Ignorovat vstup
Traineru](../getting-started/user-interface-and-navigation.md#choosing-a-source).

## Režim Slave

![Režim Slave](../assets/model-trainer-slave-mode.png)

- **Link Mode** — stejná volba mezi kabelem Traineru, Bluetooth nebo
  externím modulem SBUS/CPPM jako u režimu Master (stejná pole Bluetooth
  **Mode**/**Local Name**/**Local Address**/**Dist Address**).

  ![Režim spojení v režimu Slave](../assets/model-trainer-slave-link-mode.png)

- **Channel Range** — který rozsah kanálů tohoto vysílače se odesílá
  učiteli.

  ![Kanály v režimu Slave](../assets/model-trainer-slave-channels.png)
  ![Úprava kanálu v režimu Slave](../assets/model-trainer-slave-channel-edit.png)
