---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# טלמטריה

![חיישנים שזוהו](../assets/model-telemetry-discovered-new-sensors.png)

הטלמטריה מעבירה מידע מהדגם חזרה אל הטייס — איכות הקישור (RSSI, VFR),
מתחים וזרמים, וכל נתון אחר שמדווח חיישן מחובר (מיקום GPS, גובה וכן
הלאה). נתמכים עד 100 חיישנים לכל דגם; הגילוי וההגדרה מתבצעים כאן, אך
הטלמטריה למעשה *מוצגת* בתור [ווידג'טים במסכי
תצוגה](../displays/index.md), שמוגדרים בנפרד תחת הגדרת מסכים.

## כיצד פועלת הטלמטריה של FrSky {: #how-frsky-telemetry-works }

החיישנים של FrSky אינם דורשים רכזת (hub): **Smart Port (S.Port)** הוא אפיק
תלת-גידי (Gnd, V+, Signal), שמחובר בשרשור בכל סדר אל חיבור ה-S.Port
במקלטים מסדרת X/S ואילך, ופועל בשידור חצי-דופלקס בקצב 57,600 bps (F.Port
ו-FBUS מהירים יותר).

- **Physical ID** — עד 28 צמתים (כולל המקלט) חולקים את האפיק, וכל אחד
  זקוק ל-Physical ID ייחודי (00–1B הקסדצימלי). התקני FrSky מגיעים עם
  ברירות מחדל הגיוניות (למשל Vario = 00, FLVSS = 01, Current = 02,
  GPS = 03) — אם מחברים שני התקנים זהים, יש לשנות את ה-Physical ID של השני
  דרך [הגדרת התקנים](../system-setup/devices.md).
- **Application ID** — בלתי תלוי ב-Physical ID: חיישן אחד יכול לדווח מספר
  ערכים, לכל אחד Application ID משלו. ל-Vario יש Physical ID אחד אך שני
  Application ID (גובה, מהירות אנכית); ל-FLVSS יש Physical ID אחד
  ו-Application ID אחד (מתח). ניטור שתי סוללות 6S בעזרת שני חיישני FLVSS
  מחייב שינוי של **שני** המזהים בחיישן השני — Physical ID לתקשורת בלעדית
  באפיק, ו-Application ID כדי שהמקלט יבחין בין Lipo 1 ל-Lipo 2 (למשל
  `0300` → `0301`). הספרה ההקסדצימלית הרביעית היא זו שמשתנה בדרך כלל, 0–F.

  !!! note
      חיישנים החולקים Application ID אך עם Physical ID שונים תקפים רק כאשר
      [זיהוי התנגשות חיישנים](../system-setup/alerts.md) מושבת — הגדרה
      לשימוש מיוחד, לא מצב ברירת המחדל.

כל ערך שמתקבל נרשם כחיישן נפרד: ערך, Physical/Application ID, שם הניתן
לעריכה, יחידה, דיוק עשרוני, דגל אופציונלי לרישום לוג ב-SD card, וערכי
מינימום/מקסימום משלו. החיישנים מזוהים אוטומטית בכל הדלקה לאחר שהוגדרו, אך
בפעם הראשונה חייבים לגלות אותם **ידנית**. לאחר הגילוי, ניתן להשמיע חיישן
בקול, להזין אותו אל [חיישנים מחושבים](#calculated-sensors), להשתמש בו
ב[מתגים לוגיים](logical-switches.md), ב-[Vars](variables.md) או
ב[מיקסים](mixes.md), להציג אותו במסך טלמטריה מותאם, או לקרוא אותו ישירות
מדף הגדרות זה בלי לבנות מסך כלל.

**FBUS** (שנקרא בעבר F.Port2) משפר זאת עוד יותר, ומאחד שליטת SBUS וטלמטריית
S.Port על גיד אחד בקצב 460,800 bps (לעומת 115,200 של F.Port ו-57,600 של
S.Port — שלושת קצבי הסיביות אינם תואמים זה לזה), ומאפשר למאחד יחיד לתקשר עם
כמה אביזרי עבד על אותו גיד בודד, כשכולם ניתנים להגדרה אלחוטית מהמשדר.

### טלמטריה ממספר מקלטים (ACCESS Trio)

כאשר רשומים עד שלושה מקלטים תחת [מערכת
RF](rf-system.md#registering-and-binding-a-receiver-access), ניתן להגדיר כל
מקלט מקושר בנפרד (פיני יציאה וכדומה) דרך RX1/RX2/RX3. בדרך כלל קיים נתיב
טלמטריה נכנס אחד לכל קישור RF — מערכות Tandem/TD הן החריג, ומפעילות 2.4GHz
ו-900MHz כשני נתיבים על מודול אחד. מקור הטלמטריה הפעיל יכול להתחלף בזמן
הטיסה בהתאם לתנאי ה-RF; החיישן **RX** מדווח בזמן אמת איזה מקלט שולח כרגע
טלמטריה (וגם רושם זאת בלוג).

ההגדרה הנפוצה: לשרשר את אפיק חיישני ה-S.Port על פני שלושת המקלטים, עם ספק
מתח משותף, ואז לרשום/לקשר כל מקלט ולגלות חיישנים כרגיל — מקור הטלמטריה
מתחלף אוטומטית עם החלפת ה-RX הפעיל, ונתוני חיישני S.Port *חיצוניים* עוברים
יחד באופן שקוף. (חיישנים פנימיים של המקלט — RSSI, VFR, RxBatt, ADC2 ו-RX
עצמו — אינם מקושרים כך; הם תמיד מדווחים עבור המקלט שהוא המקור הנוכחי.
טלמטריה בו-זמנית משלושתם יחד מתוכננת אך אינה זמינה עדיין.)

## חיישני איכות קישור

- **RSSI** (מחוון עוצמת אות במקלט) — עד כמה חזק שידור המשדר בנקודת המקלט.
  התראות ברירת מחדל: **ACCESS**/**TD**/**TW** 35 (נמוך) / 32 (קריטי), אובדן
  שליטה סביב 28; **ACCST** 45 / 42, אובדן שליטה סביב 38. ההודעה "Telemetry
  Lost" מופעלת כאשר הקישור אבד לחלוטין — מנקודה זו **לא יכולות להישמע
  התראות נוספות**, שכן למשדר אין עוד טלמטריה להעריך; יש להתייחס לכך כאיתות
  לחזור מיד. (בהפרדה של פחות מ-1 מטר בקירוב, המקלט עלול להיות מוצף ולייצר
  לופים שגויים של התראות Lost/Recovered — אינה תקלה אמיתית.) RSSI מהווה
  קירוב טוב לטווח האפקטיבי, אך VFR הוא מחוון איכות הקישור המהימן יותר.

  ![חיישן RSSI](../assets/model-telemetry-edit-rssi-sensor.png)

  מקלטי TD מדווחים RSSI לכל תחום (2.4G, 900M); גם מקלטי TW מדווחים אחד לכל
  תחום (2.4FSK, 2.4LoRa, 900M) — הפעילו **Individual RSSI alert per band**
  כדי לקבל התראות קוליות נפרדות לכל תחום במקום התראה משולבת אחת:

  ![התראת RSSI נפרדת](../assets/model-telemetry-rssi-individual-alert.png)

- **VFR** (Valid Frame Rate) — מספר החבילות התקינות מכל 100 שהתקבלו;
  התחליף שהוצג לאחר ACCESS 2.1 לשילוב קצב המסגרות האבודות בתוך RSSI.
  ברירת המחדל של **אזהרת ערך נמוך** היא 50%.

  ![חיישן VFR](../assets/model-telemetry-edit-vfr-sensor.png)

  מקלטי TD/TW מדווחים שני זרמי VFR (אחד לכל תחום); **Rx VFR** (במקלטי
  TD/TW/AP/AP Plus) לעומת זאת סופר כל מסגרת תקינה ללא תלות בתחום שבו הגיעה
  — זה הערך שכדאי לעקוב אחריו אם עוקבים אחר ערך VFR בודד בלבד.

- **RxBatt** — מתח סוללת המקלט.
- **ADC2** — כניסת מתח אנלוגית שנייה, במקלטים שתומכים בכך.
- **SWR** — SWR של האנטנה, בשימוש באנטנה חיצונית.
- חיישני מצב מרחבי/תנועה, במקום שנתמך: **R.Angle**, **P.Angle**,
  **AccX/Y/Z**.

לכל חיישן מספרי נוצרים גם חיישני מינימום/מקסימום אוטומטיים
`<name>-`/`<name>+`, גם אם אינם מוצגים ברשימת החיישנים הראשית.

## גילוי חיישנים {: #discovering-sensors }

![גילוי חיישנים חדשים: מופעל](../assets/model-telemetry-discover-new-sensors-on.png)

כשהכול מקושר ומופעל, הפעילו את **Discover new sensors** — נקודה מהבהבת (או
ערך אדום, אם אין נתונים עדיין) מסמנת כל חיישן ברגע שנמצא, והמסך מתמלא
אוטומטית. יש לחזור על כך **לכל דגם**, ושוב בכל פעם שמתווסף חיישן חדש.

![גילוי חיישנים חדשים: כבוי](../assets/model-telemetry-discover-new-sensors-off.png)

- החזירו את הגילוי למצב **Off** בסיום.
- **Delete all** מוחק את כל החיישנים כדי להתחיל מחדש.

  ![חיישנים נמחקו](../assets/model-telemetry-sensors-deleted.png)

- **Competition mode** מצמצם את הטלמטריה ל-RSSI ו-RxBatt בלבד — עבור
  תחרויות שמתירות חיישני מצב קישור בלבד. כיבוי המצב מחייב מחזור הפעלה לפני
  שניתן לגלות חיישנים מחדש.

  ![אישור מצב תחרות](../assets/model-telemetry-comp-only-confirm.png)

- מצב טלמטריית **Bluetooth** מבצע התאמה עם אפליקציית הטלפון FrSky
  FreeLink, שיכולה להציג טלמטריה בזמן אמת וגם להגדיר התקני FrSky כמו
  מקלטים מיוצבים.

  ![טלמטריית Bluetooth](../assets/model-telemetry-bt-option.png)

## עריכת חיישן {: #editing-a-sensor }

![בחירת אפשרות עריכה](../assets/model-telemetry-edit-option-select.png)

הקישו על חיישן לקבלת **Edit**, **Move**, **Reset** או **Delete**. שדות
נפוצים: **Value** (לקריאה בלבד), **ID** (Physical + Application ID, והמקלט
השולח), **Name**, **Unit**, **Decimals**, **Range** (גבולות סקאלה קבועים —
רלוונטי בעיקר כאשר החיישן משמש כמקור לערוץ), **Write logs**, **Reset**
(מקור שמאפס את החיישן הזה), ו-**Sensor lost warning delay** (השבתה מלאה, או
1–30 שניות, ברירת מחדל 10 שניות, לסינון נפילות קצרות — יש להבין את הסיכון
בקביעת ערך גבוה מדי; הודעת "sensor lost" מושמעת פעם אחת בלבד גם אם חיישנים
רבים נופלים בו-זמנית; מושבת כברירת מחדל עבור חיישנים פנימיים של המקלט, שכן
הם נעלמים לעיתים רחוקות).

חלק מהחיישנים מוסיפים שדות משלהם:

- **ADC2** — **Ratio** ו-**Offset**, לתיקון הסקאלה.

  ![עריכת חיישן ADC2](../assets/model-telemetry-edit-adc2-sensor.png)

- **RSSI** — ספי **Critical value** ו-**Low value warning**.
- **VFR** — **Low value warning** (ברירת מחדל 50%).
- **VSpeed** (מהירות אנכית של הוריו) — **Range** עד ±100 מ'/ש' (ברירת מחדל
  ±10 מ'/ש'). התנהגות שמע הוריו עצמה נמצאת כיום תחת [הפונקציה המיוחדת Play
  Vario](special-functions.md), ולא כאן.

  ![עריכת חיישן VSpeed](../assets/model-telemetry-edit-vspeed-sensor.png)

## חיישני DIY / צד שלישי

![יצירת חיישן DIY](../assets/model-telemetry-diy-sensor-select.png)

**Create DIY Sensor** מוסיף חיישן שאינו של FrSky באופן ידני: **Auto
detect** (מאכלס אוטומטית את Physical ID, Application ID ו-Module, אם ניתן),
או הגדרתם ידנית, בתוספת **Protocol decimals/unit** (הדיוק הנכנס, 0–3 מקומות
עשרוניים, והיחידה המקורית) ו-**Display decimals/unit** (בלתי תלוי בזה של
הפרוטוקול) לצד אותם שדות **Range**/**Ratio**/**Offset**/**Write
logs**/**Reset**/**Sensor lost warning delay** כמו בכל חיישן אחר.

![זיהוי אוטומטי של חיישן DIY](../assets/model-telemetry-diy-sensor-auto-detect.png)

## חיישנים מחושבים {: #calculated-sensors }

![יצירת חיישן מחושב](../assets/model-telemetry-calculated-sensor-select.png)

גזירת חיישן חדש מחיישן קיים אחד או יותר:

- **Consumption** — האנרגיה שנצרכה, באינטגרציה מחיישן זרם (למשל סדרת FAS).
  יחידה mAh/Ah, טווח עד 1000Ah.

  ![חיישן Consumption](../assets/model-telemetry-calculated-sensor-consumption.png)

- **Distance** — ממקור GPS (בתוספת מקור גובה, למרחק תלת-ממדי). יחידות
  ס"מ/מ'/ק"מ/רגל, עד 20 ק"מ.

  ![חיישן Distance](../assets/model-telemetry-calculated-sensor-distance.png)

- **Trip** — מרחק מצטבר בין קיבועי GPS עוקבים. אותן יחידות, עד 1000 ק"מ.

  ![חיישן Trip](../assets/model-telemetry-calculated-sensor-trip.png)

- **Multi Lipo** — משרשר שני חיישני מתח Lipo או יותר לניטור סוללות גדולות
  מ-6S (עד 67.2V/8S). בחרו כל חיישן תא מהנמוך לגבוה; לכל חיישן Lipo נוסף יש
  לשנות תחילה את ה-Physical **וגם** ה-Application ID ב[הגדרת
  התקנים](../system-setup/devices.md) (כלי ההגדרה Lipo Voltage שם מסייע
  בכך), לגלות אותם אחד-אחד ולשנות שם כדי שיהיו ניתנים להבחנה.

  ![חיישן Multi Lipo](../assets/model-telemetry-calculated-sensor-multi-lipo.png)

- **Percent** — משנה את סקאלת החיישן ל-0–100%, עם אפשרות **Invert** (למשל
  כדי להציג את האחוז *הנותר* במקום הנצרך).

  ![חיישן Percent](../assets/model-telemetry-calculated-sensor-percent.png)

- **Power** — הספק בוואט מזוג מקורות **Current** ו-**Voltage**, עד
  1,000,000W.

  ![חיישן Power](../assets/model-telemetry-calculated-sensor-power.png)

- **Custom** — נוסחה שרירותית המשורשרת ממקור אחד או יותר.

לכל חיישן מחושב יש גם **Persistent** (נשמר לאחר כיבוי/החלפת דגם, ונטען
מחדש בשימוש הבא) ולחצן **Reset** ישירות במסך העריכה.

### חיישנים מותאמים

![חיישן מותאם](../assets/model-telemetry-edit-custom-sensor.png)

מתחילים ממקור אחד, ואז **Add** משרשר פעולות נוספות: **Add(+)**,
**Minus(-)**, **Multiply(×)**, **Divide(/)**, **Min**, **Max**, **Sqrt**.
היחידות נבחרות מרשימה ארוכה הכוללת מתח, זרם, קיבול, הספק, מרחק, מהירות,
זמן, טמפרטורה, אחוזים, זוויות, לחץ ועוד; טווח מ-−1,000,000 עד 1,000,000,
0–4 מקומות עשרוניים.

![הוספת שורת חישוב](../assets/model-telemetry-edit-custom-sensor-add-action.png)

!!! example "הספק שיא"
    הכפילו חיישן מתח (`VFAS`) בחיישן זרם (`Current`), ואז הוסיפו שלב
    **Max** המפנה לערך הנוכחי של החיישן עצמו (`MaxPower`) כדי לעקוב אחר
    הקריאה הגבוהה ביותר שנמדדה — 288W בהרצה שבדוגמה זו:

    ![דוגמת MaxPower](../assets/model-telemetry-edit-custom-sensor-maxpower.png)

!!! example "חישוב אריתמטי מול קבוע"
    המקור מוגדר כ-`RSSI 2.4G` (קריאה של 64dB), ואחר כך פעולת **Subtract**
    שעל המקור שלה בוצעה לחיצה ארוכה והופעל **Convert to value**, מה שהופך
    אותו לקבוע הניתן לעריכה (20) במקום מקור חי — התוצאה היא 44dB יציבים
    (64 − 20):

    ![דוגמת חיסור](../assets/model-telemetry-edit-custom-sensor-subtrexample.png)
    ![המרה לערך](../assets/model-telemetry-edit-custom-sensor-subtrexample-conv2val.png)

!!! note "הערך הפנימי של מקור"
    לכל [מקור](../getting-started/user-interface-and-navigation.md#choosing-a-source)
    יש טווח שלמים פנימי של ±1024 המקביל לטווח המוצג של ±100% — ניתן לראות
    זאת ישירות על ידי הפניית חיישן Custom, למשל, אל מצערת: מצערת מלאה נקראת
    פנימית **+1024**, ומצערת אחורית מלאה נקראת **−1024**.

    ![ערך פנימי במקסימום](../assets/model-telemetry-edit-custom-sensor-internal-value-max.png)
    ![ערך פנימי במינימום](../assets/model-telemetry-edit-custom-sensor-internal-value-min.png)
