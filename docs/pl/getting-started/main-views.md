---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Widoki główne

## Ekran główny

![Ekran główny](../assets/mainview.png)

Ekran główny to widok wyświetlany zawsze wtedy, gdy nie jest otwarte żadne menu —
stos maksymalnie **ośmiu** ekranów, które konfigurujesz samodzielnie (zobacz
[Wyświetlacze](../displays/index.md)); przełączasz się między nimi klawiszem `PAGE`
lub gestem przesunięcia palcem. Nowo utworzony model zaczyna od pojedynczego ekranu
zawierającego obraz modelu, trzy widgety timerów oraz wskaźniki trymów i potencjometrów;
wszystko na nim można następnie dowolnie skonfigurować.

Ekrany zwykle współdzielą opisane poniżej górny i dolny pasek, ale dany ekran można
także ustawić jako pełnoekranowy, co ukrywa oba paski.

## Górny pasek

Górny pasek pokazuje po lewej stronie nazwę modelu (a także aktywny tryb lotu,
jeśli został skonfigurowany), a po prawej rząd ikon stanu:

- Aktywne rejestrowanie danych
- Stan trenera (odpowiednio: nauczyciel lub uczeń)
- RSSI — łącze 2,4 GHz
- RSSI — łącze 900 MHz (jeśli zamontowano moduł dwupasmowy / dalekiego zasięgu)
- Głośność
- Stan akumulatora nadajnika

Dotknięcie ikony głośnika lub akumulatora przenosi bezpośrednio do odpowiedniego
panelu ustawień [Ogólne](../system-setup/general.md) (dźwięk) lub
[Akumulator](../system-setup/battery.md).

### Ostrzeżenie o błędzie

Czerwony trójkąt pojawia się w górnym pasku zawsze, gdy Ethos wykryje błąd —
najczęstsze przyczyny to błąd skryptu Lua, błąd kopii zapasowej pamięci RAM
lub korzystanie z nocnej/niestabilnej wersji oprogramowania. Szczegóły
ostrzeżenia znajdują się zawsze w **System → Informacje**, na tej samej stronie co czas
pracy nadajnika i [dzienniki błędów](../system-setup/information.md).

## Dolny pasek

![Dolny pasek](../assets/bottombar.png)

Wzdłuż dolnej krawędzi znajdują się cztery zakładki odpowiadające sekcjom najwyższego
poziomu — **Strona główna**, **Konfiguracja modelu**, **Konfiguracja ekranów**,
**Ustawienia systemu** — a po prawej stronie zegar systemowy (dotknij go, aby przejść
bezpośrednio do [Data i godzina](../system-setup/date-and-time.md)).

## Obszar widgetów

Środkową część każdego ekranu wypełniają **widgety**: obraz modelu, timery,
odczyty telemetrii, paski trymów i potencjometrów oraz wiele innych — wszystkie
rozmieszczone i skonfigurowane przez użytkownika. W rozdziale
[Wyświetlacze](../displays/index.md) opisano, jak dodawać, przesuwać i konfigurować
widgety, a w rozdziale [Dodatkowe ekrany](../displays/additional-displays.md) — jak
dodać więcej ekranów niż domyślny pojedynczy.
