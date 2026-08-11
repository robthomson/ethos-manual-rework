---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![בדיקת חומרה של X20 Pro](../assets/system-hardware-check-x20pro.png)

הבדלים מבסיס ה-X20S שעל פיו נכתב מדריך זה — ההבדלים חלים על **X20 Pro**, ובמרבית המקרים חלים גם על **X20 Pro AW** ועל משפחת **X20R/RS**.

- **אמצעי אחסון** — זיכרון eMMC פנימי בנפח 8GB כברירת מחדל, SD card אופציונלי — ראו [כללי → מקום
  אחסון](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **טרימים נוספים** — נוספים מתגי טרים **T5** ו-**T6** — ראו
  [טרימים](../model-setup/trims.md#trim-settings).
- **מתגים נוספים** — שני מתגי לחיצה נעצרים, **K** ו-**L**,
  בכתפיים האחוריות, ובנוסף מצבי מתג **M**/**N** אם הם מחוברים
  (בדרך כלל מתגי קצה ג'ויסטיק) — ראו [חומרה →
  מתגים](../system-setup/hardware.md#switches-settings).
- **פוטנציומטרים נוספים** — **Ext1**/**Ext2**, המשמשים בדרך כלל עם גימבלים תלת-צירים
  — ראו [חומרה → פוטנציומטרים/מחוונים](../system-setup/hardware.md#potssliders-settings).
  הדבר מזיז את האינדקס ב[מפקח ערכי ADC](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 ממוקמים בין Pot2 והמחוונים.
- **משוב הפטי** — דגמי **X20 Pro AW** ו-**X20RS** מסופקים עם גימבלים מסוג MC20R
  הכוללים מנועי רעידה מובנים לג'ויסטיקים; ב-**X20 Pro** או
  **X20R** ניתן להשיג את אותה יכולת באמצעות שדרוג גימבל MC20R בהתאמה מאוחרת, המופעל
  תחת [חומרה → הפעלת שדרוגי גימבל
  הפטי](../system-setup/hardware.md#radio-specific-hardware-options).
  לאחר ההפעלה, [בחירת מנועים
  הפטיים](../model-setup/special-functions.md#actions) מציעה את האפשרויות Default,
  All motors, Left stick או Right stick.
- **מקודד סיבובי** — ה-X20 Pro AW וה-X20R/RS משתמשים במקודד רגיש יותר;
  אפשרות **half steps** תחת [חומרה → אפשרות
  מקודד](../system-setup/hardware.md#radio-specific-hardware-options)
  מפחיתה את הרגישות.
- **מודול RF פנימי** — ה-X20 Pro/R/RS משתמשים במודול **TD-ISRM Pro**
  (תומך LoRa, עם מצבי tandem dual-band ו-TD-Pro בנוסף
  ל-ACCESS/ACCST D16), במקום מודול ה-TD-ISRM שנמצא ב-X18/X20/X20S/X20HD — ראו [מערכת RF](../model-setup/rf-system.md).
