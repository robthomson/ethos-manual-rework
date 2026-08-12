---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Mikser Butterfly (kruk)

Hamowanie aerodynamiczne typu butterfly (znane też jako crow) pozwala
kontrolować prędkość opadania, głównie w szybowcach: lotki unoszą się
nieznacznie, podczas gdy klapy wychylają się mocno w dół, wytwarzając
duży opór — idealne do kontrolowania podejścia do lądowania. Ten opis
zakłada szybowiec, w którym kanały klap już istnieją (utworzone przez
kreator [Wybór modelu](../model-setup/model-select.md)), a jako wejście
hamulca wykorzystywany jest drążek gazu: brak butterfly przy drążku w
górze, coraz więcej w miarę przesuwania go w dół, z kompensacją steru
wysokości, aby szybowiec nie zadzierał nosa przy wypuszczaniu crow.

## 1. Wyłączenie domyślnego miksu klap

![Wyłączenie miksu klap](../assets/how-to-butterfly-flaps-disable.png)

Ustaw **Warunek aktywacji** utworzonego przez kreator miksu klap na `---`
— nie będzie on używany.

## 2. Utworzenie miksu Butterfly

![Dodany miks Butterfly](../assets/how-to-butterfly-mix-added.png)

Dotknij dowolnego miksu, **Dodaj miks** → **Butterfly** z [biblioteki
miksów](../model-setup/mixes.md#mix-libraries), umieszczając go za (teraz
wyłączonym) miksem klap.

## 3. Konfiguracja wejścia

![Wejście gazu](../assets/how-to-butterfly-mix-source-thr.png)

Ustaw **Wejście** na **Gaz**. Ponieważ gaz normalnie osiąga maksimum przy
drążku w górze, a butterfly musi wynosić 0 przy drążku w górze,
przytrzymaj `ENT` na pozycji Gaz i wybierz **Odwróć**:

![Odwrócenie gazu](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![Odwrócony gaz](../assets/how-to-butterfly-mix-source-thr-neg.png)

Wejście wskazuje teraz 0 przy drążku w skrajnym górnym położeniu, a pole
pokazuje `-Throttle`, potwierdzając odwrócenie. Ustaw **Warunek
aktywacji** na tryb lotu do lądowania (lub inny przełącznik), jeśli
butterfly nie powinno być dostępne przez cały czas.

## 4. Dodanie krzywej ze strefą martwą

![Wybór krzywej](../assets/how-to-butterfly-mix-curve-select.png)

Niewielka strefa martwa przy zerowym końcu zakresu drążka zapobiega
przypadkowemu uruchomieniu przez drobne szumy drążka w pobliżu ogranicznika.
Dodaj własną 3-punktową krzywą (np. o nazwie „Crowdb") z wyłączonym
**Trybem uproszczonym**, aby możliwe było przesuwanie punktów X:

![Krzywa 3-punktowa](../assets/how-to-butterfly-mix-curve-3pt.png)
![Punkty krzywej](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    Dodanie własnej krzywej do miksu Butterfly usuwa jego wewnętrzne
    przesunięcie 0–100 (normalnie stosowane automatycznie) — sama krzywa
    musi teraz odtworzyć tę transformację 0–100. W tym przykładzie wyjście
    pozostaje na poziomie 0% aż drążek gazu osiągnie −90%, a następnie
    rośnie liniowo do 100%:

    ![Dodana krzywa](../assets/how-to-butterfly-mix-curve-added.png)

## 5. Konfiguracja lotek i klap

![Wyjście lotek](../assets/how-to-butterfly-mix-ailerons.png)

Umiarkowane uniesienie lotek (np. 20%) w połączeniu z dużym wychyleniem
klap to typowy podział. Klapy zwykle wymagają znacznie większego skoku w
dół niż w górę — najczęściej uzyskuje się to przez przesunięcie orczyków
serw klap o 20–30° od położenia neutralnego w samym łączu, przez co przy
neutralnym położeniu serwa klapy pozostają mniej więcej w połowie
wychylone w dół:

![Klapy w górze](../assets/how-to-butterfly-mix-flaps-up.png)
![Klapy w dole](../assets/how-to-butterfly-mix-flaps-down.png)

Ustaw wysoką wagę miksu klap (np. −180%) dla maksymalnego skoku;
rzeczywisty skok fizyczny jest ograniczany przez wartości Min/Max w
[Wyjściach](../model-setup/outputs.md).

!!! tip
    Aby uniknąć przesterowania serw, zacznij od zachowawczych wartości
    Min/Max w Wyjściach (np. ±30%) i ostrożnie je poszerzaj podczas
    finalnej konfiguracji, zwracając uwagę na blokowanie się mechaniki.

## 6. Dodanie miksu przesunięcia „Flaps Neutral"

![Miks przesunięcia 80%](../assets/how-to-butterfly-offset-mix-80.png)

Ponieważ przesunięcie orczyków serw pozostawia klapy wychylone o ~20–30%
przy neutralnym położeniu serwa, **Miks przesunięcia** sprowadza je z
powrotem do rzeczywistego położenia neutralnego skrzydła na potrzeby
normalnego lotu. Zacznij od przesunięcia 80% (do dostrojenia), z 2 kanałami
wyjściowymi przypisanymi do obu kanałów klap:

![Klapy w górze z przesunięciem](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![Klapy w dole z przesunięciem](../assets/how-to-butterfly-offset-mix-flaps-down.png)

Przy drążku gazu w skrajnym górnym położeniu (miks Butterfly wyłączony)
sprawdź, czy wartości miksera klap znajdują się na poziomie przesunięcia
(80%); przesunięcie drążka klap do pełnego wychylenia powinno zmienić
wyjście miksera o pełną wagę (np. z 80% do −100%, czyli o 180%). Dokładne
ograniczenia rzeczywistego skoku dostrój w Wyjściach za pomocą Min/Max lub
krzywej.

## 7. Dodanie krzywej i miksu kompensacji steru wysokości {: #7-add-the-elevator-compensation-curve-and-mix }

![Krzywa kompensacji](../assets/how-to-butterfly-comp-curve.png)
![Punkty krzywej kompensacji](../assets/how-to-butterfly-comp-curve-points.png)

Ponieważ wymagana kompensacja jest nieliniowa, użyj krzywej zamiast stałej
wagi. Zdefiniuj własną 5-punktową krzywą (np. „EleComp") — w tym przykładzie
zaczyna się ona od wartości 12%/10%/8%/5%/0% w kolejnych punktach; bez
znanego punktu wyjścia dla danego płatowca wartości te trzeba wyznaczyć
empirycznie.

Następnie przekształć tę krzywą w wartość nadającą się do użycia jako
**Waga** miksu: dodaj [Miks wolny](../model-setup/mixes.md#mix-libraries)
(„EleCompx") ze źródłem Gaz i dołączoną krzywą EleComp, z wyjściem na
wysoki, nieużywany kanał (np. CH20):

![Miks kompensacji na CH20](../assets/how-to-butterfly-comp-mix-ch20.png)

Wróć do miksu Butterfly, przytrzymaj `ENT` na **Wadze** wyjścia steru
wysokości, wybierz **Użyj źródła**, a następnie wskaż CH20 (EleCompx) z
kategorii Kanały:

![Ster wysokości używający CH20 jako źródła](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![Wybór źródła](../assets/how-to-butterfly-mix-ele-use-source.png)

Miks Butterfly jest teraz w pełni skonfigurowany:

![Skonfigurowana kompensacja steru wysokości](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. Weryfikacja w widoku według kanałów

![Widok według kanałów](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

Przełącz się na [widok według kanałów](../model-setup/mixes.md#per-channel-view)
dla steru wysokości, aby obserwować wszystkie składowe miksy (wejście z
drążka + kompensacja Butterfly) aktualizujące się jednocześnie podczas
poruszania drążkiem gazu/hamulca — znacznie ułatwia to diagnostykę w
porównaniu z płaskim widokiem tabelarycznym.

!!! tip
    Warto dysponować danymi o wymaganym wychyleniu steru wysokości w
    zależności od wychylenia klap (od producenta płatowca lub ze źródeł
    społecznościowych) przed doborem wartości początkowych krzywej
    kompensacji. W ich braku zacznij od kilku milimetrów wychylenia steru
    wysokości na pełne wypuszczenie klap i dostrajaj od tego punktu.
