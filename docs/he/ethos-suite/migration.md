---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# מיגרציה

מעבר של משדר מכלי העדכון הנפרדים והישנים למחשב אל Ethos Suite, בפעם הראשונה.

1. **ודאו שגרסת Ethos היא ≥ 1.1.4** — הגרסה המינימלית שיכולה לצרוב את ה-bootloader החדש התואם ל-Suite (פורמט FRSK) ישירות מתוך [מנהל הקבצים](../system-setup/file-manager.md). אם צריך, עדכנו קודם ידנית לגרסה 1.1.4.
2. **גבו את ה-SD card/eMMC** — העתיקו את כל התוכן לתיקייה במחשב.
3. **הורידו את ה-bootloader העדכני ביותר** מתוך [שחרורי ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases) וחלצו את הקובץ. בכל שחרור מתפרסם קובץ `components.json` המפרט את הגרסה הנוכחית של כל רכיב — ראו [מדריך הדרכה: איתור ה-Bootloader העדכני](../how-to/find-latest-bootloader.md) להסבר על קריאתו.
4. אתרו את המשדר תחת הערך `targets` בקובץ זה כדי לדעת את גרסת ה-bootloader המדויקת שיש להשתמש בה, ומצאו את הקובץ המתאים בנכסים (assets) של אותו שחרור.
5. הפעילו את המשדר במעבר ל[מצב bootloader](../getting-started/usb-connection-modes.md#bootloader-mode) (החזיקו את `ENT` ואז הדליקו) וחברו אותו באמצעות USB.
6. העתיקו את קובץ ה-bootloader אל ה-SD card/eMMC (בדרך כלל לתיקייה `Firmware/`), לאחר מכן הוציאו את הכוננים (Eject) ונתקו את החיבור.
7. הפעילו את המשדר כרגיל, עברו אל **System → מנהל הקבצים**, הקישו על קובץ `bootloader.frsk` שהועתק כרגע, ובחרו **Flash bootloader**.
8. הורידו והתקינו את Ethos Suite — [הפעלה](operation.md) מסביר על עדכון קושחה/קבצים ועל שאר היכולות של Suite מכאן והלאה.
9. אם Ethos Suite לא עושה זאת אוטומטית, ייתכן שיש לשנות את שם התיקייה `bitmaps/user` שב-SD card/eMMC ל-`bitmaps/models` (שם נשמרות תמונות הדגמים של המשתמש).
