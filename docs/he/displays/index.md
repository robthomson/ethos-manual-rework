---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# תצוגות

![מסך בית של התצוגה](../assets/display-home.png)

מסך הבית מורכב ממסך תצוגה אחד או יותר (**display screens**), כאשר כל אחד מהם בנוי מ**ווידג'טים** שאתם ממקמים ומגדירים בעצמכם. לחיצה על `DISP` פותחת את עורך התצוגה של המסך הנוכחי.

זמינים עד **שמונה** מסכים, כשכל אחד מתחיל מאחת מ**שלוש עשרה** פריסות (המכילות עד **תשעה** תאי ווידג'ט). ווידג'טים יכולים להציג טלמטריה, אך גם כל אחת מ־17 קטגוריות מידע אחרות — מצב הדגם/המשדר, טיימרים, ערוצים ועוד. הגעה למסכים המוגדרים נעשית באמצעות החלקה במסך המגע או `PAGE` למעלה/למטה; הסרגלים העליון והתחתון נשארים גלויים בכל מסך, למעט פריסת מסך מלא.

## הוספת ווידג'ט

![סוגי ווידג'טים](../assets/display-widget-types.png)

כל מסך הוא רשת; הקשה על תא ריק פותחת את בורר הווידג'טים. הווידג'טים נעים מטקסט פשוט וקריאות מספריות ועד מחוגים, גרפים ויומני טלמטריה מלאים. לאחר המיקום, הקשה חוזרת על ווידג'ט פותחת את אותו תפריט אפשרויות המשמש לשינוי גודלו, הזזתו או הסרתו:

![אפשרויות הגדרת ווידג'ט](../assets/display-widget-config-options.png)

בחירת ההגדרות הייחודיות של ווידג'ט פותחת טופס הגדרה ספציפי לאותו ווידג'ט. שדה ה**מקור** — הערך שהווידג'ט מציג — משתמש באותו [בורר מקור](../getting-started/user-interface-and-navigation.md#choosing-a-source) המשמש בכל מקום אחר ב־Ethos:

![שינוי מקור הווידג'ט](../assets/display-change-source.png)

## סוגי ווידג'טים {: #widget-types }

**Value** — קריאה מספרית או טלמטרית בודדת, המוצגת כטקסט:

![הגדרת ווידג'ט Value](../assets/display-widget-value-config.png)

רוב המקורות תומכים גם בצמצום לערך **min** או **max** חי — לאחר בחירת המקור, יש ללחוץ עליו לחיצה ארוכה ולבחור Min או Max — שימושי לדברים כמו ה־RSSI הגרוע ביותר במהלך טיסה:

![ווידג'ט Value עם min](../assets/display-widget-value-min.png)
![ווידג'ט Value עם min של RSSI](../assets/display-widget-value-min-rssi.png)

לאחר המיקום, הוא מוצג כקריאה פשוטה על המסך:

![ווידג'ט Value של טלמטריה](../assets/display-widget-value-telemetry.png)

**Bitmap** — מציג תמונה סטטית (למשל תצלום של הדגם), או סדרת תמונות המתחלפות בהתאם לערכו של מקור (למשל סמל סוללה המשתנה עם המתח):

![הגדרת ווידג'ט Bitmap](../assets/display-widget-bitmap-config.png)
![סוג ווידג'ט Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — מחוג סוללה מיוחד הקורא מחיישן כגון FLVSS: מתח כולל של המקבץ, מספר התאים ומתח כל תא בנפרד. ירידה מתחת לרמת הסף המוגדרת של **Low voltage** צובעת את התצוגה באדום — בדוגמה שלהלן, סף של 3.3V מופעל על התא הנמוך ביותר:

![הגדרת ווידג'ט LiPo](../assets/display-widget-lipo-config.png)
![ווידג'ט LiPo](../assets/display-widget-lipo.png)

**Channels** — עד 8 ערוצי יציאה כתרשים עמודות, אופקי או אנכי:

![הגדרת ווידג'ט Channels](../assets/display-widget-channels-config.png)
![ווידג'ט Channels](../assets/display-widget-channels.png)

**Line Chart** — משרטט את ערכו של מקור לאורך זמן, ומתאפס בעת Flight Reset:

![הגדרת ווידג'ט Line Chart](../assets/display-widget-line-chart-config.png)
![ווידג'ט Line Chart](../assets/display-widget-line-chart.png)

- **Source** — מה מוצג בגרף.
- **Pause condition** — מקור שמשהה/ממשיך את הרישום (או פשוט הקשה על הווידג'ט הפעיל, אם אין מקור פנוי לכך).
- **Log period** — מרווח הדגימה; 500ms מכסה כ־6 דקות לפני הגלילה, 1s כ־12 דקות.
- **Inverted** — הופך את הגרף אנכית.
- **Auto range** — מתאים את הציר האנכי לנתונים באופן אוטומטי; כשהאפשרות כבויה, נעשה שימוש בערכי **Min**/**Max** קבועים במקום (למשל טווח קבוע של ‎−100%…+100%‎).

הקשה על גרף פעיל מציגה **Pause/resume**, **Reset** (ניקוי והתחלה מחדש), **Configure widget**, או מעבר ל**Configure screens**:

![אפשרויות Line Chart](../assets/display-widget-line-chart-options.png)

**Text** — מציג את תוכנו של קובץ טקסט בפורמט Markdown (נקרא מ־`documents/user/` — ראו [מנהל הקבצים](../system-setup/file-manager.md#top-level-folders)):

![הגדרת ווידג'ט Text](../assets/display-widget-text-config.png)
![ווידג'ט Text](../assets/display-widget-text.png)

**Timer Log** — יומן ניתן לגלילה של ערכיו הקודמים של טיימר נבחר, הנרשם בכל פעם שאותו טיימר מאותפס (שימושי למעקב אחר השימוש בסוללות טיסה במהלך מפגש); האפשרות **Reverse** ממקמת את הרשומה החדשה ביותר בראש הרשימה:

![הגדרת ווידג'ט Timer Log](../assets/display-widget-timer-logs-config.png)
![ווידג'ט Timer Log](../assets/display-widget-timer-log.png)

לחיצה ארוכה על רשומה (או על הווידג'ט) מציגה **Clear logs**, עריכה/איפוס של הטיימר שבבסיסה, או מעבר להגדרת הווידג'ט/המסך:

![תפריט רשומה ביומן הטיימר](../assets/display-widget-timer-log-menu.png)

**GPS Map** — משרטט את מיקום ה־GPS החי כמסלול, עבור דגמים עם חיישן GPS (לפרטים נוספים על ווידג'ט זה בפרט, ראו את השרשור *FrSky - ETHOS Lua Script Programming* באתר rcgroups, הודעה ‎#8854):

![הגדרת ווידג'ט GPS Map](../assets/display-widget-gps-map-config.png)

## אפשרויות ברמת המסך

מלבד הווידג'טים הבודדים, לכל מסך יש הגדרות משלו — גודל רשת הפריסה, הרקע, ואילו מסכים כלולים במחזור ה־`PAGE`:

![אפשרויות הגדרת מסך](../assets/display-screen-config-options.png)

מסך בית מוגדר במלואו משלב כמה ווידג'טים בפריסה אחת קלה לקריאה במבט:

![תצוגה ראשית](../assets/display-main-view.png)

ראו [תצוגות נוספות](additional-displays.md) להוספת מסכים מעבר לברירת המחדל, ו[ווידג'טים מותאמים אישית](custom-widgets.md) לווידג'טים מבוססי סקריפטים של Lua מעבר לסט המובנה.
