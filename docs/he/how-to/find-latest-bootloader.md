---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# מצא את גרסת ה-Bootloader העדכנית או רכיב אחר

גרסאות קושחת Ethos מפרסמות קובץ `components.json` המפרט את הגרסה
הנוכחית של כל רכיב עבור כל משדר, דבר שימושי לאימות
האם גרסה מסוימת של bootloader/קושחה/אודיו/קבצי מערכת היא
אכן העדכנית לפני צריבתה.

!!! note "צילומי מסך בהמתנה"
    לדף זה אין עדיין צילומי מסך מהסימולטור — ראה [צינור צילומי
    המסך](../contributing/screenshot-pipeline.md).

1. הורד את `components.json` מגרסת Ethos האחרונה.
2. פתח אותו בעורך טקסט (VS Code, Notepad וכדומה).
3. מצא את המקטע המתאים למשדר שלך — לדוגמה `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (דוגמה מנקודת זמן מסוימת — בדוק תמיד את הקובץ של הגרסה *הנוכחית* כדי
   לקבל מספרי גרסה אמיתיים.)

4. קרא את הגרסה של הרכיב הדרוש לך — בדוגמה
   שלמעלה, ה-bootloader העדכני עבור משפחת X20 הוא `1.4.15`.

ראה [מנהל הקבצים](../system-setup/file-manager.md#top-level-folders) כדי לדעת
היכן למקם את קובץ הקושחה שהורדת, ו-[מצבי חיבור
USB](../getting-started/usb-connection-modes.md#bootloader-mode) כדי
להעביר את המשדר למצב bootloader לצורך הצריבה — או השתמש ב-[Ethos
Suite](../ethos-suite/index.md), שמטפל בבדיקת הגרסאות ובצריבה
באופן אוטומטי.
