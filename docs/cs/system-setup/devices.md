---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Zařízení

![Zařízení](../assets/system-devices.png)

V menu se nazývá **Device config** — nástroje pro konfiguraci periferních
zařízení připojených přes S.Port/FBUS: senzorů, přijímačů, „gas suite",
servomotorů, VTX a regulátoru. Položka **DIY sensors** se zobrazí automaticky,
jakmile je detekován DIY senzor. Podrobné informace najdete v manuálu
příslušného zařízení; tato stránka popisuje to, co mají všechna společné.

!!! note
    Nemá to nic společného s volbou RF modulu (interního nebo externího), přes
    který *model* vysílá — to je nastavení pro každý model zvlášť a je popsáno
    v části [RF systém](../model-setup/rf-system.md).

Device Config je rozšiřitelný: jak uživatelé, tak FrSky zde mohou přidávat
stránky pomocí Lua.

## Změna přiřazení ID senzorů

Obrazovky Device config v Ethos umožňují změnit **Physical ID** a
**Application ID** zařízení na S.Port přímo. Pokud máte více zařízení se
stejnou funkcí, připojujte je **po jednom**: každé vyhledejte v
[Telemetrie → Vyhledat nové senzory](../model-setup/telemetry.md), zde v
Device config změňte jeho Physical ID a Application ID, poté se vraťte a
vyhledejte je znovu pod novým ID.

## Příklad: přijímače

![Volba modulu](../assets/system-devices-module-choice.png)

Stabilizované přijímače FrSky lze konfigurovat zde, jakmile je nainstalován
jejich konfigurační Lua skript (jedním kliknutím z Lua Library v Ethos Suite).
Podle generace přijímače existují dvě cesty konfigurace:

- **Stabilizer config** — novější přijímače s „pokročilou stabilizací"
  (řízení citlivosti na kanálu 13). Jsou zpřístupněny dvě nezávislé
  stabilizační skupiny: Group 1 pokrývá kanály 1–6, Group 2 pokrývá 7–11 —
  pokud piny 7–11 pro stabilizaci nepoužíváte, Group 2 vypněte. Součástí je
  6osá kalibrace, kterou je nutné jednou provést u nového přijímače a znovu
  po každé aktualizaci firmwaru v3.0.x (po obnovení výrobního nastavení).
  V kalibraci každé skupiny byl dřívější krok „self-check" nahrazen
  nezávislou kalibrací vodorovné polohy modelu, středu kanálu a krajních
  bodů kanálu, přičemž každý kanál lze jednotlivě aktivovat/deaktivovat.
  Konfigurace (ne kalibrační data) lze ukládat do PC a odtud je obnovovat.
- **SxR** — starší přijímače, včetně původních modelů a Archer/Archer Pro,
  a dále přijímače jako SR10 Pro, které (přes označení „SRx") mají
  citlivost (Gain) na kanálu 9 místo 13.

  ![Aktuální zařízení](../assets/system-devices-current.png)

!!! warning "Po aktualizaci na firmware přijímače v3.0.x"
    Proveďte obnovení výrobního nastavení (najdete jej v nabídce Options
    přijímače v RF setup), poté přijímač znovu spárujte a kompletně
    nakonfigurujte — zejména funkce Stab a 6osou kalibraci. Vyžaduje to nová
    funkce ukládání failsafe dat ve verzi v3.0.x; následně důkladně
    zkontrolujte funkci failsafe.

FrSky North America zveřejňuje podrobného průvodce nastavením stabilizovaných
přijímačů a k témuž tématu existuje i instruktážní video od FrSky Team Pilota
Juana Sancheze Garcii.

## Konfigurace přes konektor S.Port na vysílači

Zařízení S.Port a FBUS lze konfigurovat také přímo přes konektor S.Port na
horní straně vysílače, bez použití spárovaného přijímače.

1. Zapojte zařízení do konektoru S.Port na vysílači (bílý/žlutý vodič
   směrem k straně s vroubkem).
2. Přejděte do **System → Device config**, přejděte na dané zařízení
   (např. proudový senzor FAS40 ADV) a stiskněte `ENT`.
3. Na konfigurační stránce nastavte **Module** na **S.Port connector**.
4. Proveďte požadované změny — Physical ID a Application ID musí být vždy
   jedinečné — poté sjeďte dolů a stiskněte **Save to flash**.

To platí jak pro zařízení FBUS (viz také [Praktický návod: Konfigurace
systému FBUS](../how-to/fbus-setup.md)), tak pro běžná zařízení S.Port,
například variometr.
