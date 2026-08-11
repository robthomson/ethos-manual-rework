---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Podstawowy przykład helikoptera bezstabilizatorowego (FBL)

Podstawowa konfiguracja helikoptera bez stabilizatora (FBL — flybarless),
na przykładzie kontrolera takiego jak Spirit. W odróżnieniu od modelu
stałopłata, helikopter jest z natury niestabilny — kontroler FBL
wykorzystuje żyroskopy (prędkość obrotu) oraz akcelerometry
(ruch/orientację) do obliczania korekt odchylenia/pochylenia/przechylenia
za pomocą nastrojonej pętli regulacji PID (proporcjonalno-całkująco-
różniczkującej), równoważąc stabilność, reakcję na sterowanie
i przeregulowanie w zależności od konkretnych właściwości mechanicznych
i elektrycznych danego helikoptera.

Ten samouczek obejmuje wyłącznie stronę **programowania nadajnika** —
w pozostałym zakresie należy korzystać z dokumentacji własnej jednostki
FBL, dysponując już solidną ogólną wiedzą o helikopterach.

!!! danger
    Ze względów bezpieczeństwa przed rozpoczęciem zdejmij łopaty wirnika.

## Krok 1. Sprawdź ustawienia systemowe

Kolejność kanałów **AETR**, **[Pierwsze cztery kanały
stałe](../system-setup/controls.md#first-four-channels-fixed)**
**wyłączone (OFF)** — jednostki FBL Spirit oczekują kanałów SBUS dokładnie
w tej kolejności (mimo że wewnętrznie, we własnej konfiguracji, używają
TAER). Zarejestruj (jeśli ACCESS) i zbinduj odbiornik przez [System
RF](../model-setup/rf-system.md).

## Krok 2. Określ wymagane serwa/kanały

| Funkcja | Kanał |
|---|---|
| Przechylenie (lotki) | — |
| Pochylenie (ster wysokości) | — |
| Gaz | — |
| Odchylenie (ster kierunku) | — |
| Czułość żyroskopu | 5 |
| Skok kolektywny | 6 |
| Bank ustawień | 7 |
| Rescue | 8 |

## Krok 3. Utwórz nowy model

![Tworzenie modelu helikoptera](../assets/tut-heli-eg-wiz-create-heli.png)

W [Wyborze modelu](../model-setup/model-select.md) utwórz/wybierz
kategorię Heli, uruchom kreatora i wybierz **Flybarless**:

![Wybór FBL](../assets/tut-heli-eg-wiz-fbl.png)
![Nazwa modelu](../assets/tut-heli-eg-wiz-name.png)

Nadaj mu nazwę i wybierz obrazek.

## Krok 4. Przejrzyj i skonfiguruj miksy

![Przegląd miksów](../assets/tut-heli-eg-mixes.png)

Kreator tworzy Lotki/Ster wysokości/Gaz/Ster kierunku w kolejności AETR,
Pitch na kanale 6 oraz FBL Bank na kanale 7:

![Miks skoku](../assets/tut-heli-eg-mixes-pitch.png)

Upewnij się, że kanał 6 to skok kolektywny. Dwa kolejne kanały wymagają
ręcznego dodania [miksów
wolnych](../model-setup/mixes.md#mix-libraries): **czułość żyroskopu**
(kanał 5) oraz **Rescue/Stabi** (kanał 8).

**Lotki/Ster wysokości/Ster kierunku** — nie ma tu nic do dodania; za
przełożenia (rates) i Expo odpowiada jednostka FBL, więc nadajnik
przekazuje jedynie czysty, liniowy sygnał sterujący.

![Miks lotek](../assets/tut-heli-eg-mixes-ail.png)

**Skok kolektywny** — prosta krzywa liniowa; wystarczy potwierdzić kanał
wyjściowy (zwykle 6). Jak wyżej, przełożenia/Expo obsługuje jednostka
FBL, a nie nadajnik.

**FBL Bank** — trzy banki ustawień Spirita (różne style latania, czułości
czujników przy różnych obrotach albo tryby Beginner/Acro/3D — lub po
prostu presety strojenia) przypisane do przełącznika 3-pozycyjnego, np.
SE:

![Miks banku](../assets/tut-heli-eg-mixes-bank.png)

**Czułość żyroskopu** — dodaj jako miks wolny po ostatnim kanale. Czułość
to zazwyczaj wartość stała: ustaw **Źródło** na Special Value 0, wprowadź
wartość czułości przez **Offset** (dostrajany później w locie) i skieruj
wyjście na kanał 5:

![Miks czułości żyroskopu](../assets/tut-heli-eg-mixes-gyro-gain.png)

### Konfiguracja trybów lotu

![Tryby lotu](../assets/tut-heli-eg-flight-modes.png)

Trzy [tryby lotu](../model-setup/flight-modes.md): zmień nazwę trybu
domyślnego na **Normal** oraz dodaj **Idle Up 1**/**Idle Up 2** na
przełączniku SD.

### Konfiguracja miksu gazu

Trzy krzywe gazu, po jednej na tryb lotu, każda jako [krzywa
niestandardowa](../model-setup/curves.md):

- **Normal** — rozkręcanie/start: zaczyna od −100% (silnik wyłączony)
  i płynnie rośnie. Dobrze sprawdza się krzywa 7-punktowa z włączonym
  **Smooth**; dokładne wartości wymagają strojenia w locie.

  ![Krzywa Normal](../assets/tut-heli-eg-curves-normal.png)

- **Idle Up 1** — loty ogólne: krzywa liniowa dająca stałe ustawienie
  gazu utrzymujące równe obroty wirnika, przy czym ruch modelu wynika ze
  skoku kolektywnego, lotek (przechylenie) i steru wysokości
  (pochylenie). Zachowaj płynne przejście z trybu Normal — bez dużego
  skoku. (Większość jednostek FBL oferuje także funkcję **Governor**,
  utrzymującą stałe obroty wirnika podczas agresywnych manewrów — patrz
  instrukcja jednostki FBL.)

  ![Krzywa Idle Up 1](../assets/tut-heli-eg-curves-iup1.png)

- **Idle Up 2** — latanie agresywne (akrobacja, 3D); również strojone
  w locie.

  ![Krzywa Idle Up 2](../assets/tut-heli-eg-curves-iup2.png)

![Krzywe gazu w miksach](../assets/tut-heli-eg-mixes-thr-curves.png)

**Odcięcie gazu** — przypisz np. przełącznik SG w górę z włączoną opcją
**Sticky**: przestawienie SG w górę natychmiast odcina gaz, a (dzięki
opcji Sticky) ponowne uzbrojenie jest możliwe dopiero po sprowadzeniu
drążka gazu do dołu/zera.

![Odcięcie gazu](../assets/tut-heli-eg-mixes-thr-cut.png)

**Rescue/Stabi** — przypisz analogicznie, np. do przełącznika SA na
kanale 8.

![Miksy końcowe](../assets/tut-heli-eg-mixes-final.png)

## Krok 5. Konfiguracja FBL

1. **Zainstaluj narzędzie konfiguracyjne FBL** — np. Spirit Settings, na
   komputerze PC.
2. **Podłącz odbiornik do jednostki FBL** zgodnie ze schematem połączeń —
   zazwyczaj wyjście SBUS Out odbiornika do portu RUD jednostki FBL
   (niektóre modele Spirit wymagają adaptera SBUS) albo alternatywnie
   przez F.Port1/FBUS.
3. **Podłącz jednostkę FBL do komputera** — kablem lub przez Bluetooth,
   zgodnie z jej instrukcją.

   !!! danger
       Nie podłączaj jeszcze żadnych serw.

4. **Zaktualizuj firmware jednostki FBL**, jeśli to konieczne, z zakładki
   Update w narzędziu konfiguracyjnym.
5. **Ustawienia ogólne** (zakładka General w Spirit Settings):
   - Typ odbiornika: odpowiednio **Futaba SBUS** lub **FrSky F.Port**,
     następnie uruchom ponownie.
   - Przypisanie kanałów (dla AETR z kreatora):

     | Funkcja | Kanał |
     |---|---|
     | Gaz | 1 |
     | Lotki | 2 |
     | Ster wysokości | 3 |
     | Ster kierunku | 4 |
     | Żyroskop | 5 |
     | Skok | 6 |
     | Bank | 7 |
     | Rescue/Stabi | 8 |

     (Takie przypisanie wynika ze sposobu, w jaki jednostka Spirit
     interpretuje pozycje w strumieniu danych SBUS.)

6. **Zakresy kanałów** (zakładka Diagnostic) — jednostka FBL wymaga
   skalibrowanych zakresów kanałów nadajnika i zweryfikowanych pozycji
   neutralnych:

   - Najpierw wyzeruj w nadajniku wszystkie subtrymy i trymy.
   - Ustaw drążek skoku kolektywnego w pozycji środkowej tak, aby
     w [Wyjściach](../model-setup/outputs.md) wskazywał dokładnie 1500 µs.
   - Włącz jednostkę FBL i sprawdź, czy lotki/ster wysokości/skok/ster
     kierunku wskazują 0% w zakładce Diagnostic (jednostka FBL
     automatycznie wykrywa neutrum przy każdej inicjalizacji).
   - Przesuń każdy element sterowania do skrajnych położeń i skoryguj
     odpowiadające im wartości **Min**/**Max** w Wyjściach, aż zakładka
     Diagnostic wskaże dokładnie +100%/−100%, potwierdzając również, że
     kierunek wychylenia paska odpowiada kierunkowi ruchu drążka.

   !!! warning
       Nigdy nie używaj subtrymu ani trymu na tych kanałach — jednostka
       FBL Spirit traktuje je jako komendy sterujące, a nie kalibrację.

7. Dostosuj **Offset** miksu czułości żyroskopu, aby uzyskać działanie
   Heading Lock.

Po wykonaniu tych czynności strona nadajnika jest w pełni skonfigurowana —
dalszą część konfiguracji przeprowadź zgodnie z instrukcją własnej
jednostki FBL.
