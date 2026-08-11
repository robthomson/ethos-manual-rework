---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# כללי

![הגדרות כלליות](../assets/system-general.png)

מכסה מאפייני תצוגה, שמע, וריו, רטט וסרגל הכלים העליון.

## מאפייני תצוגה

- **Language** — שפת תפריטי התצוגה (English, 中文, Česky, Deutsch,
  Español, Français, עברית, Italiano, Nederlands, Norsk, Português
  Brasileiro, Polish, Português ואחרות).
- **Keyboard** — פריסת מקלדת וירטואלית QWERTY, QWERTZ או AZERTY.
- **Brightness** — מחוון לבהירות התאורה האחורית; לחיצה ארוכה על `ENT` כדי
  להפעיל אותה ממקור במקום זאת (למשל מחוון, כמו בדוגמה שלהלן),
  או לאלץ אותה למינימום/מקסימום.

  ![תפריט בהירות](../assets/system-general-brightness-menu.png)
  ![מחוון בהירות](../assets/system-general-brightness-slider.png)

  !!! note
      אם **Brightness** שווה ל־**Sleep mode brightness**, מסך המגע
      נשאר פעיל גם במהלך "שינה".

- **Wake up** — אילו מהאפשרויות הבאות מעירות את התאורה האחורית ממצב שינה (ניתן
  להפעיל יותר מאחת): **Always on** (לא נכנס לשינה), **Sticks**,
  **Switches**, **Gyro** (הטיית המשדר). מקשים תמיד מעירים אותה
  ללא תלות בהגדרות אלו.
- **Sleep** — זמן חוסר פעילות לפני כיבוי התאורה האחורית (מוצג באפור
  אם Wake up מוגדר ל־Always on).
- **Sleep mode brightness** — בהירות התאורה האחורית במצב שינה.
- **Dark mode** — ערכת תצוגה בהירה או כהה.
- **Highlight Color** — צבע ההדגשה של ממשק המשתמש (ברירת מחדל `#F8B038`).

## הגדרות שמע {: #audio-settings }

![הגדרות שמע](../assets/system-general-audio.png)

- **Audio language** — שפת ההודעות הקוליות.
- **Choice of voices** — Ethos תומך בכמה חבילות קול במקביל:

  - **Voice 1 (main)** — משמשת לכל הודעות המערכת המובנות. עבור
    אנגלית, הבחירה כברירת מחדל היא בין חבילות אמריקאית (`us`) ובריטית
    (`gb`), הנקראות מ־`audio/en/us/system` ומ־`audio/en/gb/system`.
    קבצי צלילים של המשתמש עבור [הפונקציה המיוחדת Play Audio](../model-setup/special-functions.md)
    ממוקמים ב־`audio/en/us/`
    או ב־`audio/en/gb/` בהתאמה.
  - **Voice 2 / Voice 3** — חבילות נוספות, למשל קול
    TTS מותאם אישית. כל אחת דורשת את אותו מבנה תיקיות כמו Voice 1 — למשל קול
    בשם "Susan" דורש `audio/en/Susan/` עבור צלילי המשתמש ו־
    `audio/en/Susan/system` עבור צלילי המערכת שלו (כל קול דורש תיקיית
    `/system`, מכיוון שמשם נקראים **Play Value** והודעות
    הטיימרים; רשימת `.csv` של קבצי צלילי המערכת הסטנדרטיים
    מסופקת עם כל גרסת שמע). לאחר ההתקנה, ניתן להקצות קול
    לכל טיימר ולכל פונקציית Play Audio — או אפילו להגדיר אותו כ־Voice
    1 כדי להחליף לחלוטין את הודעות המערכת.
  - **Voice "default"** — מותקן אוטומטית כגיבוי בטוח (וכדי
    למנוע בעיות המרה מהתקנות 1.4.x): אם Voice 1 אינו
    מוגדר כבר בעת התקנה/שדרוג, הוא נקבע ל־`default`, וקורא
    מ־`audio/en/default/system`. קבצי צלילים מותאמים אישית המבוקשים לעתים תכופות
    עבור Play Audio ממוקמים ב־`audio/en/default/`.

- **Main volume** — מחוון לעוצמת השמע הכללית (לחיצה ארוכה על `ENT` כדי
  להפעיל אותו מפוטנציומטר); צפצופים מושמעים במהלך הכיוונון כדי
  שתוכל להעריך את הרמה באוזן.
- **Audio mode**:
  - **Silent** — ללא שמע (עדיין מפעיל את [התראת המצב השקט](alerts.md)
    בהפעלה, אם היא מאופשרת).
  - **Alarms only** — רק אזעקות נשמעות.
  - **Default** — צלילים רגילים.
  - **Often** — מוסיף צפצופי שגיאה כאשר ערך נדחף מעבר
    למינימום/מקסימום שלו.
  - **Always** — מוסיף צפצופים לניווט תפריטים רגיל, בנוסף ל־Often.
  - **Bluetooth** (X20S/HD/Pro/R/RS בלבד) — מעביר שמע להתקן
    Bluetooth מותאם (אוזניות וכדומה). בחר **Search Devices**, העבר את
    התקן היעד למצב התאמה, ולאחר מכן בחר אותו כשיימצא:

    ![התאמת Bluetooth](../assets/system-general-audio-bluetooth.png)
    ![חיפוש Bluetooth](../assets/system-general-audio-bluetooth-searching.png)
    ![התקן Bluetooth נבחר](../assets/system-general-audio-bluetooth-device-selected.png)
    ![מתחבר ל־Bluetooth](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth מחובר](../assets/system-general-audio-bluetooth-connected-ok.png)

    **Speaker mute** שולט לאחר מכן ברמקול המובנה — תמיד פעיל,
    רק בזמן שהטלמטריה פעילה, או מופעל ממקור (למשל
    מתג). המשדר זוכר את ההתקן המותאם; הפעל את המשדר
    לפני התקן ה־Bluetooth לתפעול תקין, והמתן מספר
    שניות לאחר התחברותו עד שהשתקת הרמקול תחזור לפעולה.

## וריו {: #vario }

![שמע וריו](../assets/system-general-audio-vario.png)

- **Volume** — עוצמה יחסית של צליל הוריו.
- **Pitch zero** — גובה הצליל בקצב טיפוס אפס.
- **Pitch max** — גובה הצליל בקצב טיפוס מקסימלי.
- **Repeat** — השהיה בין צפצופים בגובה צליל אפס.

ראה גם את חיישן VSpeed תחת [טלמטריה](../model-setup/telemetry.md)
ואת [הפונקציה המיוחדת Play Vario](../model-setup/special-functions.md)
להתנהגות וריו נוספת.

## רטט

- **Strength** — מחוון לעוצמת הרטט.
- **Mode** — אותה קבוצת אפשרויות כמו Audio mode שלעיל.

## מיקום אחסון (X18 ו־X20 Pro/R/RS) {: #storage-location-x18-and-x20-prorrs }

למשדרים אלו יש eMMC פנימי בנפח 8GB. כברירת מחדל Ethos משתמש בו, כך
ש־SD card הוא אופציונלי — אך ניתן לבחור את ה־eMMC, SD card או
שילוב של שניהם. אם מעבירים את המערכת והדגמים ל־SD card, העתק
את התיקיות/הקבצים הרלוונטיים (כולל שמע ותמונות) **לפני**
שינוי מיקום האחסון.

![מיקום אחסון](../assets/system-general-storage.png)

## סרגל הכלים העליון

![הגדרות סרגל הכלים העליון](../assets/system-general-topbar.png)

- **Digital voltage** — מציג את מתח סוללת המשדר כמספר במקום
  כפס בסרגל הכלים העליון.
- **Digital RSSI** — אותו הדבר, עבור RSSI של 2.4GHz ו־900MHz.
- **Select model at power on** — מציג את מסך בחירת הדגם
  בהפעלה, לפני הופעת התראות רשימת הבדיקה של הדגם הקודם, כך שתוכל
  להחליף דגמים ללא צורך לבטל אותן קודם. הדגם שהיה בשימוש לאחרונה
  מודגש כברירת מחדל.

  ![בחירת דגם בהפעלה](../assets/system-general-model-start.png)

## בחירה מוקדמת של מצב USB

![מצב USB](../assets/system-general-usb.png)

מה שקורה אוטומטית כאשר המשדר מתחבר למחשב דרך USB:

- **Not set** — מציג בקשה לבחירה בזמן החיבור.
- **Joystick** — נכנס מיד למצב ג'ויסטיק עבור סימולטור RC.
- **Ethos Suite** — נכנס מיד למצב Ethos עבור [Ethos
  Suite](../ethos-suite/index.md).
- **Serial** — נכנס מיד למצב Serial, ומנתב מעקבי ניפוי באגים של Lua
  דרך USB-Serial במהירות 115200 bps (עשוי להידרש מנהל התקן של יציאת COM וירטואלית ב־Windows).
