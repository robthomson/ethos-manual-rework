---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Regulowana w locie krzywa kompensacji

## Dlaczego

Wypuszczenie klap zmienia wysklepienie profilu skrzydła — modele górnopłatowe
zwykle „podskakują” w górę, dolnopłatowe mają tendencję do opadania — co wymaga
korekty sterem wysokości, która nie jest liniowa względem wychylenia klap, a więc
raczej krzywej niż stałego przesunięcia. Ten przewodnik wykorzystuje
[Zmienne](../model-setup/variables.md), aby punkty krzywej kompensacji były
regulowane **w locie**, za pomocą przypisanego ponownie trymu gazu, uzależnionego
od tego, w pobliżu którego punktu krzywej znajduje się aktualnie drążek klap —
rozwijając krok kompensacji steru wysokości z [Poradnika: Mikser
butterfly](butterfly-mixer.md).

## 1. Wybór typu krzywej

5-punktowa [krzywa własna](../model-setup/curves.md) w zupełności wystarcza do
płynnej kompensacji bez nadmiernej złożoności. Punkt 5 (skrajnie prawy, drążek
klap całkowicie w górze / brak klap) jest zawsze ustalony na zero — przy
schowanych klapach kompensacja nie jest potrzebna. Pozostałe 4 punkty są
regulowane za pomocą Zmiennych. Ponieważ drążek klap często znajduje się między
dwoma zdefiniowanymi punktami, w strefie nakładania się oba sąsiadujące punkty
muszą być regulowane jednocześnie.

## 2. Obliczenie nakładających się zakresów

Zakresy między punktami (zaadaptowane, za zgodą autora, z „Crow-aware adaptive
elevator trim” Mike'a Shellima dla OpenTX na rc-soar.com — nieznacznie
rozszerzone, tak aby zakres Pt2 sięgał aż do +100%, z powodu wyjaśnionego w
[Kroku 6](#6-apply-the-curve)):

| Zakres drążka klap | Aktywny punkt (punkty) |
|---|---|
| +100% do +45% | tylko Pt2 |
| +45% do +20% | Pt2 i Pt3 |
| +20% do −20% | tylko Pt3 |
| −20% do −45% | Pt3 i Pt4 |
| −45% do −90% | tylko Pt4 |
| −90% do −100% | tylko Pt5 |

## 3. Konfiguracja przełączników logicznych

![Przełączniki logiczne punktów adaptacyjnych](../assets/how-in-flight-comp-lsws.png)

Cztery [przełączniki logiczne](../model-setup/logical-switches.md), każdy
wykorzystujący funkcję **Range** na drążku klap (gazu), aktywne, gdy drążek
znajduje się w strefie danego punktu:

- `AdaptivePt2` — zakres od 20% do 100% (rozszerzony do 100% właśnie po to, aby
  Pt2 można było regulować nawet przy schowanych klapach — patrz Krok 6).

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` — zakres od −45% do 45%.

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` — zakres od −90% do −20%.

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` — zakres od −100% do −90%.

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. Definiowanie Zmiennych regulacyjnych

![Przegląd Zmiennych](../assets/how-in-flight-comp-vars.png)

Cztery [Zmienne](../model-setup/variables.md), `VAdjPt2`–`VAdjPt5`, każda o
zakresie 0–50% (w razie potrzeby można go poszerzyć) oraz z akcją **przypisanego
ponownie trymu gazu** — wielkość kroku 1,0%, warunek aktywacji to odpowiadający
przełącznik logiczny:

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![Akcja VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![Akcja VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![Akcja VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![Akcja VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5-2.png)

Ponieważ w danej chwili aktywny jest tylko jeden przełącznik logiczny (co
najwyżej dwa w strefach nakładania), ten sam fizyczny trym bezpiecznie reguluje
różne Zmienne w zależności od położenia klap.

## 5. Definiowanie krzywej kompensacji

![Krzywa kompensacji](../assets/how-in-flight-comp-var-comp-curve.png)
![Punkty krzywej kompensacji](../assets/how-in-flight-comp-var-comp-curve-pts.png)

Nowa 5-punktowa krzywa własna (np. „EleComp”) z włączoną opcją **Smooth**.
Przytrzymaj `ENT` na punktach 1–4 i wybierz **Use a source**, aby przypisać
odpowiednio `VAdjPt5`…`VAdjPt2` (punkt 5 pozostaje ustalony na 0, zgodnie z
Krokiem 1).

## 6. Zastosowanie krzywej {: #6-apply-the-curve }

Użyj tej krzywej dokładnie w tym miejscu, w którym [Poradnik: Mikser
butterfly](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix)
podpina swoją krzywą EleComp do miksu kompensacji steru wysokości.

Tam, gdzie to możliwe, zacznij od rzeczywistych danych (zaleceń producenta,
wpisów społeczności) dotyczących tego, jakiego wychylenia steru wysokości wymaga
dane wychylenie klap; w przeciwnym razie kilka milimetrów kompensacji przy
pełnych klapach jest rozsądnym punktem wyjścia.

!!! tip "Sposób strojenia"
    Zacznij od niewielkiego wychylenia klap i drobnych korekt trymem.
    `AdaptivePt2` można stroić **przy całkowicie schowanych klapach** — dodaj
    odrobinę klap, schowaj je ponownie i dobieraj kompensację po trochu, zamiast
    walczyć z podskakującym lub opadającym modelem, próbując trymować pod
    presją. Ponownie dodaj odrobinę klap, aby sprawdzić efekt, i w razie potrzeby
    skoryguj. Gdy Pt2 będzie już właściwy, przejdź do kolejnego punktu w okolicy
    środka zakresu drążka — jeśli Pt2 wymagał dużej zmiany trymu, warto
    wylądować i ustawić pozostałe punkty tak, aby każdy był nieco większy od
    poprzedniego, zamiast zgadywać na ślepo.
