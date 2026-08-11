---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# מאמן

![מאמן](../assets/model-trainer.png)

כברירת מחדל כבוי. ניתן להגדיר את המשדר כ-**Master** (משדר המדריך, המקבל עד 16 פקדים מהתלמיד) או כ-**Slave** (משדר התלמיד, השולח מספר ערוצים הניתן להגדרה אל המדריך).

## מצב Master

![מצב Master](../assets/model-trainer-master.png)
![אפשרויות מאמן](../assets/model-trainer-options.png)

### מצב קישור

![אפשרויות מצב קישור](../assets/model-trainer-link-mode-options.png)

- **כבל מאמן** — כבל אודיו מונו בקוטר 3.5 מ"מ בין שני המשדרים.
- **Bluetooth** —

  ![קישור Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Mode** — רגיל או מהירות גבוהה; השתמשו במהירות גבוהה להשהיה נמוכה יותר, אם שני המשדרים תומכים בכך.

    ![מצב Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Local name** — שם ה-BT המוצג להתקנים אחרים (ברירת המחדל `FrSkyBT`, ניתן לעריכה).
  - **Local address** — כתובת ה-Bluetooth של משדר זה.
  - **Distant address** — כתובת המשדר המצומד, לאחר יצירת הקישור.
  - **Search devices** (במצב Master בלבד) — סורק התקנים בסביבה:

    ![סורק](../assets/model-trainer-link-mode-bt-search.png)
    ![ממתין](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![בחירת התקן](../assets/model-trainer-link-mode-bt-select-device.png)
    ![מחובר](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Connect Last Device** / **Reset Module** — התחברות מחדש לצימוד הקודם, או מחיקה מלאה של הגדרות מודול ה-Bluetooth.

- **מודול SBUS חיצוני** — כניסת SBUS בפין PXX-IN של תא המודול החיצוני, להתקנת מקלט FrSky עם יציאת SBUS (למשל Archer RS) בקצה המקבל של קישור אלחוטי — כך **כל** משדר FrSky יכול לשמש כצד התלמיד (buddy box), כשהוא מקושר לאותו מקלט.
- **מודול CPPM חיצוני** — אותו רעיון באמצעות כניסת CPPM, עבור מקלט ותיק עם יציאת CPPM.

### תנאי הפעלה

![תנאי הפעלה](../assets/model-trainer-active-condition.png)

מתג/לחצן, מתג פונקציה, מתג לוגי, מצב טרים או מצב טיסה שמעביר את השליטה לתלמיד בזמן שהוא פעיל.

### ערוצי מאמן

![עריכת תנאי הפעלה](../assets/model-trainer-active-condition-edit.png)

ניתן להעביר עד 16 ערוצים מהתלמיד אל ה-Master בזמן שתנאי ההפעלה מתקיים. הקישו על ערוץ כדי להגדיר אותו בנפרד:

- **תנאי הפעלה** — עקיפה ברמת הערוץ, למשל כדי להשבית רק את קלט המעלית של התלמיד בחלק מהאימון.
- **Mode** — **OFF** (מושבת לשימוש מאמן), **Add** (אותות ה-Master והתלמיד מתחברים יחד, כך ששניהם יכולים לפעול על הפקד בו-זמנית), או **Replace** (המצב הרגיל — לתלמיד יש שליטה מלאה על ערוץ זה בזמן שהוא פעיל).
- **Percent** — שינוי קנה המידה של קלט התלמיד, בדרך כלל 100%.
- **Destination** — הפונקציה שאליה ממופה ערוץ התלמיד.

ראו [מדריך הדרכה: השבת שליטה מיידית](../how-to/instant-takeback.md) לדוגמה מעשית של מדריך המשיב לעצמו את השליטה באופן מיידי באמצעות מתג, וכן [התעלמות מקלט המאמן](../getting-started/user-interface-and-navigation.md#choosing-a-source) כדי להחריג את תנועת הג'ויסטיק של התלמיד ממתג לוגי העוקב אחר הג'ויסטיקים של המדריך עצמו.

## מצב Slave

![מצב Slave](../assets/model-trainer-slave-mode.png)

- **Link Mode** — אותה בחירה של כבל מאמן, Bluetooth או מודול SBUS/CPPM חיצוני כמו במצב Master (אותם שדות Bluetooth: **Mode**/**Local Name**/**Local Address**/**Dist Address**).

  ![מצב קישור Slave](../assets/model-trainer-slave-link-mode.png)

- **Channel Range** — טווח הערוצים של משדר זה שנשלח אל ה-Master.

  ![ערוצי Slave](../assets/model-trainer-slave-channels.png)
  ![עריכת ערוץ Slave](../assets/model-trainer-slave-channel-edit.png)
