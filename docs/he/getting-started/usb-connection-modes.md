---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# מצבי חיבור USB

![תפריט USB](../assets/usbmenu.png)

מה שחיבור USB למחשב עושה תלוי באופן שבו הופעל המשדר בעת חיבורו.

## מצב כיבוי

חיבור המשדר למחשב באמצעות USB **כאשר הוא כבוי** מעביר אותו למצב DFU, המשמש לצריבת ה-bootloader עצמו.

## מצב Bootloader {: #bootloader-mode }

הפעל את המשדר **בעת החזקת `ENT` לחוץ** כדי לאתחל למצב bootloader (המסך מציג "Bootloader"). חיבור USB בשלב זה משנה את הסטטוס ל-"USB Plugged", והמחשב מזהה **שני** כוננים: זיכרון ה-flash הפנימי של המשדר, ותוכן ה-SD card/eMMC. זהו המצב לקריאה וכתיבה של קבצים ישירות לכל אחד מאזורי האחסון, וכך גם [Ethos Suite](../ethos-suite/index.md) מעדכן את קושחת המשדר — ראה את הפרק Bootloader Mode ב-Ethos Suite.

## מצב הפעלה

חיבור USB בעת שהמשדר **מופעל באופן רגיל** מציג בורר מצבים:

- **Joystick** — מציג את המשדר כ-USB HID joystick, לצורך הפעלת סימולטורי טיסה במחשב.
- **FrSky Suite** — מעביר את המשדר ל-"Ethos mode" לתקשורת עם [Ethos Suite](../ethos-suite/index.md).
- **Serial** — מנתב מעקבי דיבאג של Lua דרך USB-serial (115200 bps). ללשונית Lua Development Tools של Ethos Suite יש מסוף מוטמע להצגתם; ייתכן שיידרש דרייבר Virtual COM Port ל-Windows.
