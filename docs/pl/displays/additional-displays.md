---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Dodatkowe wyświetlacze

![Opcje konfiguracji ekranu](../assets/display-screen-config-options.png)

Domyślny model zawiera jeden ekran (bitmapa modelu oraz trzy widgety
timerów), lecz obsługiwanych jest łącznie do **ośmiu** ekranów. Dotknij
**+** obok pozycji „Screen1”, aby dodać kolejny:

- Do wyboru jest **15** układów, w tym dwa układy dedykowane dla ekranu
  głównego oraz opcja pełnoekranowa, mieszcząca do 9 widgetów —
  konfigurowanych dokładnie tak samo jak pierwszy ekran.
- Kolejność ekranów można zmieniać, a same ekrany usuwać z poziomu ich
  własnego okna edycji (dotknij Screen1, Screen2 itd.).

## Przykład praktyczny

![Widok główny](../assets/display-main-view.png)

Typowy układ: bitmapa modelu (konfigurowana w [Edycja modelu →
Obrazek](../model-setup/model-edit.md)) po lewej stronie, a po prawej —
ułożone jedno pod drugim — napięcie akumulatora odbiornika, RSSI oraz
widget stanu „Throttle ACTIVE” (widget Lua stworzony przez społeczność,
pochodzący z wątku *FrSky - ETHOS Lua Script Programming* na rcgroups).
Dotknięcie dowolnego widgetu otwiera jego konfigurację lub przenosi do
głównej funkcji Konfiguracja ekranów.

## Opcje na poziomie ekranu

Poza poszczególnymi widgetami każdy ekran ma własne ustawienia — rozmiar
siatki układu, tło oraz określenie, które ekrany są uwzględniane w cyklu
przewijania klawiszem `PAGE`.

Informacje o samych widgetach znajdziesz w rozdziale [Wyświetlacze](index.md),
a o dodawaniu widgetów opartych na skryptach Lua, wykraczających poza zestaw
wbudowany — w rozdziale [Własne widgety](custom-widgets.md).
