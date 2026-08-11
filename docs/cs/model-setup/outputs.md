---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Výstupy

![Výstupy](../assets/model-outputs.png)

Výstupy jsou hranicí mezi čistou „logikou“ [Mixů](mixes.md) a fyzickým
světem — servy, táhly, kormidly, aktuátory a snímači. Zde se koncové body,
reverzace, středění a korekční křivky přizpůsobují tomu, co model
mechanicky skutečně potřebuje. Každý výstupní kanál odpovídá jednomu
servo výstupu přijímače (CH1 → konektor serva č. 1, při výchozím nastavení
protokolu).

Ethos pracuje v procentech, ale serva jsou nakonec řízena šířkou PWM
impulzu v mikrosekundách:

| % | µs |
|---|---|
| −150% | 732 |
| −100% | 988 |
| 0% | 1500 |
| 100% | 2012 |
| 150% | 2268 |

!!! warning
    Kanál **bez aktivního mixu** vysílá neutrál (0 % / 1500 µs) — to
    zahrnuje i kanál, jehož jediný mix (či mixy) je právě neaktivní.
    Ujistěte se, že každý skutečně používaný kanál má vždy aktivní mix,
    který jej zajišťuje. Konkrétně u kanálu plynu znamená neutrál
    **poloviční plyn**.

Obrazovka Výstupy zobrazuje u každého kanálu dva pruhy: dolní (zelený)
pruh je hodnota mixéru pro daný kanál, horní (oranžový) pruh je hodnota po
zpracování Výstupy, která se skutečně posílá do přijímače (v % i µs).
Limity Min/Max se zobrazují jako zešedlé části oranžového pruhu. Kanály,
které se právě nevysílají do RF modulu, mají tmavší pozadí. U kanálu se
objeví malé ikony, pokud bylo jeho nastavení Směr, Křivka, Zpomalení nebo
Vyvážení změněno z výchozí hodnoty — díky tomu poznáte nevýchozí kanály na
první pohled.

!!! tip
    Dlouhý stisk `ENT` na obrazovce Mixy nebo Letové režimy vás přenese
    přímo sem.

## Editace kanálu {: #editing-a-channel }

![Editace výstupu výškovky](../assets/model-outputs-elevator-edit.png)
![Editace výstupu plynu](../assets/model-outputs-throttle-edit.png)

Kanál otevřete klepnutím. Náhled v horní části zobrazuje hodnotu mixu
(zeleně) proti hodnotě výstupu (oranžově), s malou bílou značkou pro body
Min/Max.

- **Název** — lze upravit.
- **Směr** — obrací výstup kanálu, typicky pro obrácení smyslu otáčení
  serva. Na kanálu se zobrazuje jako ikona dvojité šipky. **Neovlivňuje**
  mixy, které kanál napájejí, a **nezaměňuje** limity Min/Max.
- **Min/Max** — pevné limity, které nikdy nelze překročit — nastavte je
  tak, aby nedocházelo k mechanickému zablokování. Fungují jako nastavení
  koncových bodů / zesílení: jejich zmenšením se zmenší výchylka, nedojde
  k „odstřižení“ signálu. Výchozí hodnota je ±100 %, nastavitelná až do
  ±150 %. Při nastavování se tučně zobrazuje ten konec, ke kterému se
  právě pohybujete (např. posuňte páčku výškovky dopředu a hodnota Max
  zesílí, což potvrzuje, že nastavujete právě tento konec).

  ![Upozornění na redundanci SBUS](../assets/model-outputs-sbus-warning.png)

  !!! warning "Redundance SBUS"
      Redundantní zapojení využívající SBUS nedokáže pohnout servem za
      hranici přibližně ±125 %. Samotná pole Min/Max mají nesymetrické
      rozsahy (−150–0 % a 0–150 %) — pokud je řídíte z
      [proměnné](variables.md), nastavte této proměnné shodný rozsah nebo
      zapněte **Ignorovat rozsah** (viz [možnosti
      zdroje](../getting-started/user-interface-and-navigation.md#choosing-a-source)),
      jinak automatický převod rozsahu vytvoří neočekávané hodnoty. Pokud
      výstup hlavního přijímače překročí 125 % a přijímač přejde do
      failsafe, redundantní přijímač, který jej přes SBUS převezme, jej
      omezí zpět na 125 %.

- **Střed/Subtrim** — posouvá výstup, typicky pro vystředění páky serva;
  koncové body zůstávají nedotčeny.

  !!! warning
      Nepoužívejte subtrim pro velké posuny — vnáší do odezvy serva
      výrazný diferenciál. Pro cokoli nad rámec jemného středění použijte
      místo toho **offsetový mix**.

- **PWM střed** — podobné subtrimu, ale posouvá *celé* pásmo dráhy serva
  včetně pevných limitů, a to fakticky uvnitř samotného serva, takže se to
  neprojeví v monitoru kanálů. Tím se mechanické středění drží oddělené od
  trimování.
- **Křivka** — připojí Expo nebo vlastní křivku (existující či novou, po
  nastavení se zobrazí zkratka **Editovat**) pro korekci reálné odezvy —
  např. pro přesné sledování polohy levé a pravé klapky. Na kanálu se
  zobrazuje jako ikona křivky.
- **Zpomalení nahoru/dolů** — zpomaluje odezvu výstupu na změny vstupu,
  v sekundách potřebných pro pohyb 0→100 % — např. pro zpomalení zatahovacího
  podvozku poháněného běžným proporcionálním servem. Na kanálu se
  zobrazuje jako ikona hodin. (**Zpoždění**, které je odlišné od
  zpomalení, je dostupné u [logických přepínačů](logical-switches.md).)

## Záměna kanálů {: #swap-channels }

![Záměna kanálů](../assets/model-outputs-swap-channels.png)
![Výběr kanálu pro záměnu](../assets/model-outputs-swap-channels-select.png)

Zamění dva výstupní kanály. Dialog se otevře s předvyplněným aktuálním
kanálem; vyberte druhý a potvrďte — záměna je okamžitá a každý mix, který
na některý z těchto kanálů odkazuje, se odpovídajícím způsobem aktualizuje.

## Reset nastavení

![Reset kanálu](../assets/model-outputs-reset-select.png)

Vymaže všechny parametry kanálu na výchozí hodnoty — užitečné před
přeurčením kanálu k jinému účelu; potvrzovací dialog zabraňuje nechtěným
změnám.

## Vyvážení kanálů {: #balance-channels }

![Výběr kanálů k vyvážení](../assets/model-outputs-balance-choose_channels.png)
![Výběr CH7/CH6](../assets/model-outputs-balance-choose-ch7-and-ch6.png)

Vyváží pár (nebo až 4) kanálů tak, aby se pohybovaly souhlasně — např.
klapky, které se nepohybují stejně, mohou vyvolat nežádoucí klopení;
nevyvážené plyny na víceMotorovém modelu mohou vyvolat nežádoucí zatáčení.
Ethos vytvoří pro každý vybraný kanál diferenciální vyvažovací křivku;
porovnáním fyzických poloh kormidel v každém bodě křivky je můžete
nastavit tak, aby si odpovídaly, což vede k perfektně sladěným kormidlům.

**Před vyvažováním**, v tomto pořadí:

1. Nastavte směry serv pro správný chod.
2. S mixy v neutrálu případně použijte **PWM střed** k vyrovnání pák serv.
3. Nastavte Min/Max a Subtrim.
4. Nakonfigurujte všechny další křivky.
5. Nakonfigurujte Zpomalení.
6. *Teprve poté* vyvažujte a srovnávejte v celém rozsahu dráhy.

**Použití**: vyberte kanály k vyvážení a pořadí, v jakém se mají zobrazit —

![Vybráno CH7/CH6](../assets/model-outputs-balance-ch7-and-ch6.png)

— výstup mixu na ose X, diferenciál vyvažovací korekce na ose Y. Klepnutím
na graf kanálu (nebo jeho vybráním a stiskem `ENT`) otevřete editaci jeho
vyvažovací křivky; klávesa `PAGE` přepíná mezi kanály během editace:

![Editor vyvažovací křivky](../assets/model-outputs-balance-curve-edit.png)

Ovládací prvky editoru:

- **Zdroj** — obvykle vlastní zdroj(e) mixu nebo jakýkoli jiný vhodný
  analogový vstup; **Automatický analogový vstup** převezme jako osu X
  první páčku/posuvník/potenciometr, kterým pohnete, a to jak v grafu, tak
  v samotném modelu.
- **Magnet** — automaticky přichytí úpravu otočným enkodérem k nejbližšímu
  bodu křivky na ose X:

  ![Magnet vypnutý](../assets/model-outputs-balance-ch6-magnet-off.png)
  ![Magnet zapnutý](../assets/model-outputs-balance-ch6-magnet-on.png)

  Vstupem je i tak nutné pohnout tak, aby se X zarovnalo s bodem křivky,
  než jej lze upravovat.
- **Zámek** — přepíná se klepnutím na jeho ikonu nebo stiskem `ENT`
  v režimu editace grafu; uzamkne všechny vstupy, takže můžete pustit
  páčku a při úpravě křivky sledovat kormidla.
- **Konfigurace** — změna počtu bodů na kanál (u všech nebo jednotlivě)
  a nastavení, zda je každá křivka vyhlazená.
- **Nápověda** (`?`, také klávesa `MDL`) — otevře vestavěnou nápovědu.

**Více kanálů**: společně lze vyvážit až 4 kanály —

![Vyvážení 4 kanálů](../assets/model-outputs-balance-ch2-9-8-1.png)

Jakmile je vyvažovací křivka nastavena, lze ji zkontrolovat, upravit nebo
vymazat na konfigurační stránce daného kanálu — na grafu kanálu ji
označuje ikona vyvážení (spolu s ikonou Směr, pokud i ten není ve výchozím
stavu).
