---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Test nastavení redundantního přijímače

Redundance má smysl pouze tehdy, pokud je před letem skutečně vyzkoušena —
tento postup předpokládá, že [redundantní přijímač](../model-setup/rf-system.md#redundant-receivers)
je již nakonfigurován.

!!! note "Snímky obrazovek budou doplněny"
    Tato stránka zatím nemá snímky obrazovek ze simulátoru — viz [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## A. Test v reálných podmínkách

S hlavním přijímačem na 2,4 GHz a redundantním na 900 MHz spusťte
[kontrolu dosahu](../model-setup/rf-system.md#range-check) a odcházejte od
modelu, dokud nedojde ke ztrátě signálu na 2,4 GHz (za hranicí výstrahy
RSSI Critical). Redundantní přijímač na 900 MHz by měl v tom okamžiku
převzít řízení.

## B. Test na stole

1. **Ověřte běžné nastavení** — oba přijímače spárované, oba svítí zeleně,
   ovládání reaguje normálně.
2. **Spárujte hlavní přijímač s jiným Model ID** — vytvořte pomocný
   testovací model (např. „TestRx") s odlišným Model ID a spárujte s ním
   *hlavní* přijímač. Přepněte se zpět na testovaný model: LED hlavního
   přijímače by nyní měla svítit **červeně** (spárován jinde), LED
   redundantního přijímače zůstává **zelená** — a ovládání by mělo stále
   fungovat, což dokazuje, že samotný redundantní přijímač udržuje model
   letuschopný.
3. **Spárujte hlavní přijímač zpět** s jeho původním Model ID. Než test
   považujete za dokončený, ověřte, že obě LED opět svítí zeleně a ovládání
   funguje.
