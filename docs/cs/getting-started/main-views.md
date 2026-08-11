---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Hlavní zobrazení

## Domovská obrazovka

![Domovská obrazovka](../assets/mainview.png)

Domovská obrazovka je to, co vidíte vždy, když není otevřena žádná nabídka — sada až
**osmi** zobrazovacích obrazovek, které si sami nakonfigurujete (viz
[Displeje](../displays/index.md)), mezi nimiž se přepíná klávesou `PAGE`
nebo přejetím prstem po dotykovém displeji. Nově vytvořený model začíná pouze s jednou obrazovkou,
která zobrazuje obrázek modelu, tři widgety časovačů a indikátory trimů/potenciometrů;
vše na ní je odtud uživatelsky konfigurovatelné.

Obrazovky obvykle sdílejí horní a spodní lištu popsané níže, ale
obrazovku lze také nastavit na celoobrazovkový režim, čímž se obě lišty skryjí.

## Horní lišta

Horní lišta zobrazuje vlevo název modelu (plus aktivní letový režim,
pokud je nějaký nakonfigurován) a vpravo řadu stavových ikon:

- Aktivní záznam dat
- Stav trenéra (master nebo slave, podle situace)
- RSSI — spoj 2,4 GHz
- RSSI — spoj 900 MHz (je-li nasazen dvoupásmový / long-range modul)
- Hlasitost zvuku
- Stav baterie vysílače

Dotykem ikony hlasitosti nebo baterie přejdete přímo na odpovídající panel nastavení
[Obecné](../system-setup/general.md) (zvuk) nebo
[Baterie](../system-setup/battery.md).

### Varování o chybě

Kdykoli Ethos zjistí chybu, objeví se v horní liště červený trojúhelník —
nejčastějšími příčinami jsou chyba Lua skriptu, chyba záložní RAM nebo použití
nightly / nestabilní verze firmwaru. Podrobnosti k tomuto varování najdete vždy
v **System → Info**, na téže stránce jako dobu provozu vysílače a
[protokoly chyb](../system-setup/information.md).

## Spodní lišta

![Spodní lišta](../assets/bottombar.png)

Podél spodní hrany jsou čtyři karty pro hlavní sekce — **Domů**,
**Nastavení modelu**, **Konfigurace obrazovek**, **Nastavení systému** — a vpravo
systémové hodiny (dotykem přejdete přímo na
[Datum a čas](../system-setup/date-and-time.md)).

## Oblast widgetů

Střed každé obrazovky je vyplněn **widgety**: obrázek modelu, časovače,
telemetrické údaje, indikátory trimů/potenciometrů a další, přičemž jejich rozmístění
a nastavení je zcela na vás. Postup přidávání, přesouvání a konfigurace widgetů najdete
v části [Displeje](../displays/index.md) a přidání více než výchozí jedné obrazovky
v části [Další displeje](../displays/additional-displays.md).
