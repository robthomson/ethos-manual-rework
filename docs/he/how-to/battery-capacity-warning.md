---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# אזהרת קיבולת סוללה

אזהרה על בסיס **קיבולת שנוצלה** (mAh) במקום מתח — מדד ישיר יותר לכמה
מהסוללה נוצל בפועל. יש שתי דרכים להשיג זאת, בהתאם לחומרה המותקנת.

## אפשרות א': בקר מהירות מסדרת Neuron

בקרי המהירות Neuron של FrSky מדווחים על הצריכה ישירות — אין צורך בחיישן
מחושב. הגדירו את [Receiver Options → Telemetry
Port](../system-setup/devices.md) ל-S.Port, חברו את חוט הטלמטריה של ה-Neuron
ו[גלו את החיישנים](../model-setup/telemetry.md#discovering-sensors) — החיישן
הרלוונטי הוא **ESC Consumption**.

1. הוסיפו [מתג לוגי](../model-setup/logical-switches.md) על `ESC
   Consumption`, אמיתי מעל (נאמר) 900mAh — בקירוב 60% מסוללה שגודלה מחושב
   כך שתנחת עם כ-30% עדיין ברזרבה.
2. הוסיפו [פונקציה מיוחדת Play
   audio](../model-setup/special-functions.md), כשתנאי ההפעלה הוא המתג החדש,
   עם שלב **Play value** עבור `ESC Consumption`.

כקו הגנה שני, בקרי Neuron מדווחים גם על **ESC Voltage** — הגדירו מתג לוגי
שני באותו אופן כמו ב[אזהרת מתח סוללה
נמוך](low-battery-warning.md) (מתחת ל-3.4V לתא עבור 4s — למשל
13.6V לסוללת 4S), עם פונקציית Play audio משלו שחוזרת כל 5
שניות.

## אפשרות ב': חיישן זרם + חיישן מחושב

אם בקר המהירות אינו מדווח על צריכה, חיישן זרם (למשל FrSky
FASxxx) בשילוב עם [חיישן **Consumption**
מחושב](../model-setup/telemetry.md#calculated-sensors) עושה את אותה
עבודה.

### 1. חיבור וגילוי

![חיישן זרם](../assets/how-to-consumption-telemetry-current-sensor.png)

חברו את חוט ה-S.Port של חיישן הזרם וגלו אותו — הוא יופיע בשם
**Current**. הגדירו את **Range** שלו כך שיתאים לחיישן (למשל 0–100A עבור
FAS100):

![עריכת חיישן זרם](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. יצירת חיישן Consumption מחושב

![יצירת חיישן מחושב](../assets/how-to-consumption-create-calc-select.png)
![חיישן Consumption](../assets/how-to-consumption-create-calc-sensor.png)

בתפריט Telemetry, בחרו **Create Calculated Sensor** → **Consumption**. הגדירו
את היחידות ל-`mAh` ואת **Range** לקיבולת הסוללה (למשל 2800mAh); ואת **Source**
ל-`Current`.

![עריכת חיישן](../assets/how-to-consumption-sensor-edit.png)
![עריכת חיישן 2](../assets/how-to-consumption-sensor-edit2.png)

הגדירו את **Reset** לאירוע המערכת `!Telemetry Active` — בחרו **Telemetry
Active**, לחצו לחיצה ארוכה על `ENT` ובחרו **Invert** — כך שהסכום המצטבר
יתאפס אוטומטית ברגע שהטלמטריה נקטעת (כלומר, הדגם כובה).

### 3. הכרזות אבני דרך

![מתג לוגי דלתא 200mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

הוסיפו מתג לוגי בשימוש בפונקציה **Δ > X** על `Consumption`, כך שיופעל
בכל פעם שהערך עולה בצעד קבוע — למשל כל 200mAh, שהם חלק נוח מסוללת
2800mAh.

!!! tip
    הגדירו את **Check interval** ל-`---` (אינסופי) כדי שהערך ימשיך להצטבר
    לעבר הסף הבא ללא הגבלה, במקום להתאפס בסוף חלון זמן קבוע. תנו ל-**Min
    Duration** ערך קטן שאינו אפס בזמן ניפוי הבאגים — בערך 0.0 ההפעלה קצרה
    מדי מכדי להיראות על המסך.

הוסיפו פונקציית Play Audio, כשתנאי ההפעלה הוא מתג זה, עם שלב Play
value עבור `Consumption`:

![הכרזת דלתא](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. אזהרת קיבולת נמוכה

![מתג לוגי שני](../assets/how-to-consumption-lsw2-play-battlow.png)

מתג לוגי שני מופעל פעם אחת, בחציית סף קיבולת נמוכה קבוע — למשל
2000mAh מתוך סוללת 2800mAh — בשילוב עם פונקציית Play Audio
שחוזרת כל 10 שניות עד לאיפוס הדגם:

![Play value באזהרת סוללה נמוכה](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value: consumption באזהרת סוללה נמוכה](../assets/how-to-consumption-sf2-play-value-consumption.png)
