---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# אזהרת מתח סוללה נמוך

ניטור מתח סוללת הטיסה **בעומס** והתראה מתחת לסף מסוים הם גישה אמינה יותר מהסתמכות על טיימר קבוע — חיישן כגון FrSky FLVSS מאפשר זאת בפשטות.

## 1. חיבור וגילוי החיישן

![חיישן טלמטריה LiPo](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

הגדר את [Receiver Options → Telemetry Port](../system-setup/devices.md) ל־**S.Port**, חבר את ה־FLVSS למקלט באמצעות כבל S.Port, ולאחר מכן הפעל **Discover new sensors** תחת [טלמטריה](../model-setup/telemetry.md) — חיישן ה־LiPo יופיע לצד שאר החיישנים שגולו קודם לכן.

## 2. הוספת מתג לוגי

![מתג לוגי למתח סוללה נמוך](../assets/how-to-low-batt-lsw-battlow-lipo.png)

הוסף [מתג לוגי](../model-setup/logical-switches.md) חדש כאשר חיישן ה־Lipo מוגדר כמקור שלו. לחיצה ארוכה על `ENT` על החיישן המסומן מאפשרת לבחור באיזה מהערכים שלו להשתמש:

![בחירת התא הנמוך ביותר](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- מתח מינימלי של הסוללה / מתח מקסימלי של הסוללה
- **מתח התא הנמוך ביותר** / מתח התא הגבוה ביותר
- מספר התאים
- מתחים של תאים בודדים (ניתנים לבחירה רק כאשר החיישן מחובר בפועל למקלט משויך עם סוללת LiPo מחוברת)

בחר **Lowest** (מתח תא) — הערך הרלוונטי להגנה מסוג LVC.

![התא הנמוך ביותר נבחר](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

הגדר את ערך ההשוואה לכ־**3.4V** ואת **Delay before active** ל־**4 שניות** — המתג יהפוך לאמת ברגע שמתח התא הנמוך ביותר נמדד מתחת ל־3.4V לתא באופן רציף למשך 4 שניות או יותר. (מתח של 3.4V *בעומס* חוזר בדרך כלל לכ־3.7V לאחר הסרת העומס, ולכן סף זה משקף צניחת מתח אמיתית ולא רק רעש רגעי.)

![המתג הלוגי המושלם](../assets/how-to-low-batt-lsw-summary.png)

## 3. הוספת פונקציה מיוחדת

![פונקציה מיוחדת: BattLow](../assets/how-to-low-batt-sf-battlow.png)

הוסף [פונקציה מיוחדת מסוג Play audio](../model-setup/special-functions.md), כאשר **Active condition** מוגדר למתג הלוגי `BattLow`, בחר קול, ותחת **Sequence** הוסף שלב **Play value** עבור מתח ה־LiPo הכולל:

![Play value: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![סיכום הסדרה](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

כאשר **Repeat** מוגדר ל־10 שניות, מתח ה־LiPo יוקרא בקול כל 10 שניות כל עוד מתח התא הנמוך ביותר נשאר מתחת לסף של 3.4V/4 שניות.
