---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# System RF

Konfiguruje wewnętrzny i/lub zewnętrzny moduł RF modelu, identyfikator rejestracyjny właściciela (Owner Registration ID), bindowanie odbiornika oraz opcje odbiornika. Tutaj również dokonuje się wyboru pomiędzy modułem wewnętrznym a zewnętrznym dla danego modelu — w odróżnieniu od niemal wszystkiego innego w [Ustawieniach systemu](../system-setup/index.md), wybór sprzętu RF jest **przypisany do modelu**, a nie do całego nadajnika.

!!! note "Zrzuty ekranu w przygotowaniu"
    Zestaw zrzutów ekranu dla tej sekcji nie został jeszcze wykonany (zobacz
    [Proces tworzenia zrzutów ekranu](../contributing/screenshot-pipeline.md)) — poniższa
    treść jest poprawna, ale na razie występuje wyłącznie w formie tekstowej.

## Identyfikator rejestracyjny właściciela {: #owner-registration-id }

Ośmioznakowy unikalny kod (kombinacja wielkich i małych liter oraz cyfr, bez znaków specjalnych), który po rejestracji staje się **identyfikatorem rejestracyjnym** odbiornika. Ustaw *ten sam* kod w kilku nadajnikach, aby korzystać między nimi z funkcji **Smart Share** — zrób to przed utworzeniem modelu, który chcesz współdzielić. Zgodny z EdgeTX; tylko częściowo zgodny z OpenTX.

## Wyłączanie emisji RF

Przytrzymaj `PAGE` podczas włączania zasilania, aby wyłączyć emisję RF zarówno modułu wewnętrznego, jak i zewnętrznego dla danej sesji (ostrzeżenie potwierdzi wyłączenie). Ustawienie **State** modułu pozostaje włączone (ON) — zwykłe ponowne uruchomienie przywraca normalną emisję.

## Tryby modułu wewnętrznego

Moduł wewnętrzny nadajników X18/X20/X20S/X20HD (TD-ISRM) pracuje w jednym z trzech trybów — moduł TD-ISRM Pro w X20 Pro/R/RS działa podobnie, lecz dodatkowo obsługuje LoRa oraz warianty tandem dwupasmowe. Wybrany tryb **musi odpowiadać temu, co obsługuje odbiornik**, w przeciwnym razie bindowanie się nie powiedzie; po zmianie trybu należy dokładnie sprawdzić każdy kanał, a zwłaszcza działanie failsafe.

- **ACCESS** — ścieżki 2,4 GHz i 900 MHz pracujące w tandemie pod jednym zestawem ustawień ACCESS. Łącznie do trzech odbiorników, w dowolnej kombinacji 2,4 GHz (24 kanały) i 900 MHz (16 kanałów); telemetria z obu pasm jest aktywna jednocześnie i oznaczona pasmem. Źródło telemetrii **RX** informuje, który odbiornik jest aktualnie aktywnym źródłem telemetrii.
- **ACCST D16** — pojedyncza ścieżka 2,4 GHz, dla starszych odbiorników serii „X".
- **Tryb TD** — tandem 2,4 GHz + 900 MHz o niskich opóźnieniach i dużym zasięgu, dla odbiorników Tandem, po 24 kanały w każdym paśmie.

Wersje z **firmware Flex** dodają drugą kolumnę Type, umożliwiającą przełączanie między modulacją FLEX915M (915 MHz w stylu FCC) a FLEX868M (868 MHz w stylu LBT) w każdym z trzech powyższych trybów — dla wybranego wariantu należy zamontować odpowiednie anteny. Użytkownicy w UE mogą korzystać z mocy 200/500 mW na 868 MHz; przy 25 mW telemetria przesyłana jest na 868 MHz, przy 200/500 mW przenosi się na 2,4 GHz ze względu na zgodność z przepisami.

Każdy wybór trybu/zakresu kanałów wiąże się z kompromisem w częstotliwości odświeżania — np. w trybie ACCESS 8 kanałów odświeża się co 7 ms, 16 co 14 ms, 24 co 21 ms (rotacyjnie w blokach po 8), a przy kanałach 1–8 z kompatybilnymi odbiornikami (seria RS, v2.1.7+) dostępny jest tryb **Racing** o czasie 4 ms.

## Rejestracja i bindowanie odbiornika (ACCESS) {: #registering-and-binding-a-receiver-access }

Bindowanie odbiornika ACCESS przebiega w dwóch etapach — **rejestracja** musi zostać wykonana tylko raz dla danej pary odbiornik/nadajnik; **bindowanie** można później powtarzać bezprzewodowo, bez użycia przycisku bind.

**Etap 1 — Rejestracja**:

1. Naciśnij **Register** (pomiń całkowicie, jeśli odbiornik jest już zarejestrowany).
2. Przytrzymaj przycisk bind odbiornika podczas jego włączania; poczekaj, aż zaświecą się obie diody LED. Okno dialogowe zmieni się z „Waiting for receiver…" na „Receiver connected" i automatycznie uzupełni nazwę odbiornika.
3. Potwierdź lub zmień **Registration ID** (domyślnie identyfikator rejestracyjny właściciela z powyższego pola — to zgodność identyfikatorów między nadajnikami umożliwia działanie Smart Share), **Rx name** oraz **UID**. UID rozróżnia kilka odbiorników używanych razem w jednym modelu — dla pojedynczego odbiornika pozostaw wartość 0; przy kilku (np. po jednym na blok 8 kanałów) przyjęło się stosować 0/1/2. UID nie da się później odczytać z odbiornika, dlatego warto go fizycznie opisać.
4. Naciśnij **Register**, potwierdź komunikat „Registration ok", a następnie wyłącz odbiornik — jest zarejestrowany, ale jeszcze nie zbindowany.

**Etap 2 — Bindowanie**:

!!! warning
    Nigdy nie binduj z podłączonym silnikiem elektrycznym ani z pracującym silnikiem spalinowym.

1. Odbiornik wyłączony; upewnij się, że wybrany jest właściwy tryb modułu.
2. Naciśnij **RX1** (lub 2/3) → **Bind**. Powtarzający się komunikat głosowy „Bind" potwierdza tryb bindowania.
3. Włącz odbiornik **bez** naciskania jego przycisku bind; wybierz go z wyświetlonej listy „Select device".
4. Potwierdź komunikat „Bind successful". Wyłącz i włącz ponownie zarówno nadajnik, jak i odbiornik — zielona dioda LED odbiornika świeci, czerwona zgaszona, co oznacza nawiązane połączenie. Nie trzeba powtarzać bindowania, o ile nie zostanie wymieniona jedna ze stron.
5. Powtórz procedurę dla kolejnych odbiorników (RX2, RX3), jeśli są używane.

## Opcje odbiornika

Przy włączonym odbiorniku naciśnij jego przycisk RX, aby uzyskać dostęp do:

- **Options** — **Telemetry** (włączona/wyłączona dla tego odbiornika), **Reduced telemetry power 25mW** (zamiast normalnych 100 mW — przydatne, jeśli pobliskie serwa odbierają zakłócenia RF), **High PWM Speed** (odświeżanie serw co 7 ms zamiast 18 ms — upewnij się, że serwa to obsłużą), **Telemetry port** (S.Port/F.Port/FBUS), **SBUS** (16 lub 24 kanały — przed włączeniem 24 kanałów każde podłączone urządzenie SBUS musi obsługiwać SBUS-24) oraz **Channel Mapping** do przypisywania kanałów do konkretnych pinów odbiornika.
- **Share** — przekazuje odbiornik innemu nadajnikowi ACCESS o *innym* identyfikatorze rejestracyjnym właściciela. W nadajniku źródłowym naciśnij Share (jego zielona dioda LED zgaśnie); w nadajniku docelowym wykonaj normalne bindowanie — Share pomija ponowną rejestrację, ponieważ identyfikator jest przenoszony automatycznie. Wyjdź z funkcji w nadajniku źródłowym, aby zakończyć współdzielenie; ponowne zbindowanie przywraca odbiornik. (Nie jest to w ogóle potrzebne, jeśli wszystkie nadajniki mają ten sam identyfikator rejestracyjny właściciela — wystarczy zbindować bezpośrednio z nadajnika, który ma sterować modelem).
- **Reset bind** — porządkuje ustawienia po użyciu Share i przywraca własne bindowanie; następnie należy wyłączyć i włączyć odbiornik.
- **Factory reset** — resetuje odbiornik i kasuje jego UID, całkowicie go wyrejestrowując.

Przy **wyłączonym** odbiorniku ten sam przycisk RX udostępnia **Options** (czeka na połączenie odbiornika), **Bind** (np. w celu ponownego zbindowania odbiornika wcześniej zbindowanego gdzie indziej) oraz **Clear** (odpowiednik Reset bind).

## Odbiorniki redundantne {: #redundant-receivers }

Drugi odbiornik można zbindować do nieużywanego slotu RX w celu zapewnienia redundancji — 2,4 G i 900 M mogą wzajemnie się zabezpieczać. Redundancja FrSky ocenia sytuację **dla każdej ramki**, zawsze wykorzystując najlepszą dostępną ramkę (przełączanie active/active), dzięki czemu sterowanie może przeskakiwać między odbiornikami z ramki na ramkę.

1. Połącz wyjście SBUS Out odbiornika redundantnego z wejściem SBUS In odbiornika głównego.
2. Włącz odpowiedni wewnętrzny moduł RF (np. 900M) i ustaw jego antenę/moc.
3. Zarejestruj nowy odbiornik (jeśli nie jest jeszcze zarejestrowany), a następnie zbinduj go z wolnym slotem RX zgodnie z powyższym opisem.
4. Sprawdź, czy jego zielona dioda LED świeci — odbiornik jest teraz wyświetlany jako redundantny.

## Failsafe {: #failsafe }

Dane failsafe są przesyłane ponownie z nadajnika mniej więcej co 10 sekund; w odbiornikach TD/TW/AP/AP Plus są także zapisywane po stronie odbiornika, dzięki czemu przetrwają jego ponowne uruchomienie. Po każdej aktualizacji firmware odbiornika wprowadzającej takie działanie należy starannie ponownie sprawdzić failsafe.

- **Hold** — utrzymuje ostatnio odebrane pozycje kanałów.
- **Custom** — dla każdego kanału osobno: **Not Set**, **Hold**, **Custom** (stała wartość — naciśnij ikonę strzałki, aby przechwycić bieżącą wartość, lub wprowadź ją bezpośrednio) albo **No Pulses**.
- **No Pulses** — całkowicie wstrzymuje impulsy, dla kontrolerów lotu posiadających własną procedurę powrotu do domu po utracie sygnału.
- **Receiver** — (odbiorniki serii X lub nowsze) ustawia failsafe bezpośrednio w odbiorniku.

!!! warning
    Dokładnie przetestuj wybrane ustawienie failsafe, zanim zaczniesz na nim polegać.

## Test zasięgu {: #range-check }

Wykonuj go na lotnisku przed każdą sesją lotów z nową lub zmienioną konfiguracją. Wybranie **Range Check** celowo redukuje moc nadawania (powtarzający się komunikat głosowy potwierdza ten tryb) i wyświetla na żywo wartości VFR%/RSSI do oceny jakości łącza. Poziom mocy przy teście zasięgu FrSky wynosi około −10 dB względem normalnego poziomu roboczego +20 dB; przy wysokości 1 m zarówno nadajnika, jak i odbiornika, alarm krytyczny powinien pojawić się w okolicach 30 m — wystąpienie go bliżej w normalnych warunkach może wskazywać na problem.

Przy kilku zbindowanych odbiornikach dane testu zasięgu są prezentowane dla jednego aktywnego odbiornika na pasmo — wyłączenie aktualnie aktywnego pozwala przejąć rolę kolejnemu (według priorytetu 0/1/2, widocznego przez czujnik **RX**), dzięki czemu każdy można sprawdzić po kolei.

## Zewnętrzne moduły RF i moduły innych producentów

Zewnętrzne moduły FrSky (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro) korzystają z tego samego schematu rejestracji i bindowania co moduł wewnętrzny, przy różnej dla poszczególnych protokołów liczbie kanałów, poziomach mocy i wymaganiach dotyczących anten — dokładne dane znajdziesz w instrukcji konkretnego modułu.

**ELRS** (ExpressLRS) jest obsługiwany zarówno przez tryb ELRS modułu TWIN Lite Pro, jak i przez oryginalne moduły ELRS (które wymagają zainstalowania skryptu ELRS Lua w katalogu `scripts/elrs`, zanim pojawią się jako opcja modułu). Dostępnych jest dwanaście kanałów; kluczowe ustawienia to **Packet Rate** (kompromis między opóźnieniem a zasięgiem), **Telemetry Ratio** (jak często wysyłana jest telemetria, od 1:1 do 1:128), **Switch Mode** (**Hybrid** — większość kanałów pomocniczych ograniczona do 2–3 pozycji dla mniejszych opóźnień — albo **Wide** — pełna rozdzielczość 64–128 kroków), **Model Match** oraz **Tx Power** (10 mW–1000 mW, opcjonalnie **Dynamic Power** do automatycznego skalowania wraz z jakością łącza — wymaga włączonej telemetrii).

**Moduły innych producentów** (obecnie Ghost, Multi-protocol, Crossfire, oprócz ELRS) wymagają samodzielnego zainstalowania własnego skryptu Lua — zobacz uwagi dotyczące katalogu `scripts/` w [Procesie tworzenia zrzutów ekranu](../contributing/screenshot-pipeline.md) oraz wątek *Third-Party External Modules* na rcgroups. Pozycja modułu pojawia się na ekranie RF dopiero po zainstalowaniu jego skryptu. Moduł Multi-protocol (IRX4 Lite) można dodatkowo flashować firmware bezpośrednio z poziomu [Menedżera plików](../system-setup/file-manager.md): skopiuj plik firmware do katalogu `Firmware/`, a następnie użyj opcji **Flash external multimodule**.
