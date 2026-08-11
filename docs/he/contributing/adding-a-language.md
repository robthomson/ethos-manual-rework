---
translated_from: 23549d0bf136da221c75de9a0c5695864d338cab
---

# הוספת שפה חדשה

מדריך שלב-אחר-שלב להקמת לוקאל מאפס ועד מדריך מתורגם במלואו וניתן לניווט
במלואו — כתוב עבור מי שיבצע את הבא בתור (אדם או סוכן). כל שלב להלן בוצע
בפועל, בסדר הזה, עבור `de`, `fr`, `es`, `it`, `pt-BR` ו-`zh`; המכשולים
המצוינים הם כשלים אמיתיים שנתקלנו בהם בדרך, לא היפותטיים.

## רשימת בדיקה

עבדו לפי הסדר; כל פריט מקשר לסעיף שבו מופיעות הפקודות עצמן והמכשולים
שנתקלנו בהם בפועל. אל תדלגו ישר לשלב 4 — שלבים 1 ו-3 זולים ומונעים עבודה
כפולה בהמשך.

- [ ] **[1](#1-confirm-the-locale-code-before-touching-anything)** — ודאו ש-Ethos מסופק עם ממשק משתמש בשפה זו, ובחרו קוד לוקאל שקיים עבורו תבנית ב-`mkdocs-material` (לא בהכרח הקוד שכלי הפיתוח של FrSky עצמה משתמשים בו פנימית — `pb` מול `pt-BR` הפיל אותנו כאן).
- [ ] **[2](#2-add-the-locale-to-mkdocsyml)** — הוסיפו את הלוקאל ל-`mkdocs.yml` (עדיין בלי `nav_translations`).
- [ ] **[3](#3-seed-a-glossary-in-scriptstranslatepy)** — זרעו מילון של כ-30 מונחים ב-`GLOSSARIES` שבתוך `scripts/translate.py`.
- [ ] **[4](#4-translate)** — הריצו `scripts/translate.py --only <code>` (קודם בהרצה יבשה); ודאו `0 failed`.
- [ ] **[5](#5-check-for-existing-screenshots-before-considering-the-simulator)** — בדקו במאגר הוותיק `ethos-manual` אם קיימת ערכת צילומי מסך שכבר צולמה, לפני שאתם מניחים שנדרש צינור הסימולטור; העתיקו בכמות ובדקו ויזואלית נקודתית אם יש התאמה.
- [ ] **[6](#6-check-and-fix-anchor-links)** — הריצו `python scripts/check_anchors.py --fix`.
- [ ] **[7](#7-verify-for-real)** — `mkdocs build --strict` ובדקו ש-`$?` הוא `0` (לא רק שהפלט נראה נקי); ש-`check_anchors.py` מדווח 0.
- [ ] **[8](#8-add-nav_translations-once-after-page-coverage-is-complete)** — לאחר שכיסוי העמודים הושלם, הוסיפו `nav_translations` (תוויות עלה מתוך ה-H1 של כל עמוד, לשוניות מקטעים מתוך המילון).
- [ ] **[9](#9-ship-it)** — בצעו commit, push, עקבו אחר ה-Action, ואמתו בסביבה החיה (קחו בחשבון השהיית התפשטות ב-CDN עבור נתיבים חדשים לגמרי).

## 1. אשרו את קוד הלוקאל לפני שנוגעים בכל דבר אחר {: #1-confirm-the-locale-code-before-touching-anything }

שני דברים נפרדים צריכים להסתדר יחד, וטעות בכל אחד מהם מסורבלת לתיקון
בהמשך (כתובות ה-URL מקבעות את הקוד באופן קבוע):

- **האם Ethos אכן מסופק עם ממשק משתמש בשפה זו?** מדריך בשפה שהקושחה
  אינה תומכת בה מבלבל, לא מועיל. יישום שולחן העבודה
  [Ethos Suite](https://www.frsky-rc.com/) של FrSky מסופק עם קובץ
  `i18n/*.json` לכל שפה נתמכת — בהתקנה מקומית הוא נמצא ב-
  `Program Files/Ethos Suite/i18n/`. הרשימה הזו (`cs`, `de`, `en`, `es`,
  `fr`, `he`, `it`, `nl`, `no`, `pb`, `sk`, `zh-CN` בבדיקה האחרונה) היא
  מדד אמין למה ש-Ethos עצמו תומך בו.
- **האם `mkdocs-material` מסופק עם תבנית מחלף שפות עבור אותו קוד?** זו
  רשימה *אחרת*, והשתיים לא תמיד מסתדרות — התיקייה של Ethos Suite נקראת
  ממש `pb`, אבל ל-Material אין `partials/languages/pb.html`, אלא רק
  `pt-BR.html`. שימוש ב-`pb` נבנה בסדר גמור עד לשלב יצירת ה-sitemap
  שלאחר הבנייה ב-`mkdocs build`, שם הוא קורס עם
  `jinja2.exceptions.TemplateNotFound` — **והקריסה הזו אינה מכילה את
  המילה "error" או "warning"**, כך שחיפוש grep של אלה בפלט הבנייה (דבר
  סביר לחלוטין לעשות) ידווח על בנייה נקייה שבפועל יצאה עם קוד שונה מאפס.
  בדקו תמיד את `$?` אחרי `mkdocs build --strict`, לא רק את הפלט המודפס
  שלו. כדי לראות את הקודים המדויקים ש-Material תומך בהם:

  ```python
  import material
  from pathlib import Path
  p = Path(material.__file__).parent / "templates" / "partials" / "languages"
  print(sorted(x.stem for x in p.glob("*.html")))
  ```

## 2. הוספת הלוקאל ל-`mkdocs.yml` {: #2-add-the-locale-to-mkdocsyml }

```yaml
languages:
  - locale: <code>
    name: <native display name>
    build: true
```

עדיין בלי `nav_translations` — זה שלב 6, אחרי שיש תוכן אמיתי שאליו אפשר
להתאים תוויות.

## 3. זריעת מילון ב-`scripts/translate.py` {: #3-seed-a-glossary-in-scriptstranslatepy }

הוסיפו רשומת `GLOSSARIES["<code>"]` (ראו את הרשומות הקיימות
`fr`/`de`/`es`/`it` עבור רשימת המונחים שיש לכסות — שמות משטחי טיסה,
אוצר מילים של מיקס/יציאות/טיימר/טרים, מתגים, חיישנים וכו'). זה מה ששומר
על עקביות טרמינולוגית מהעמוד המתורגם הראשון, במקום סחיפה מעמוד לעמוד.
כ-30 מונחים מספיקים; זו רצפה לבנות עליה, לא מילון שלם.

אם הקונסולה מחזירה שגיאת `UnicodeEncodeError` באמצע הרצה — זה קרה
ל-`zh` באופן ספציפי — הסיבה היא שברירת המחדל של הקונסולה של Windows היא
`cp1252`, שאינה יכולה לקודד כתבים שאינם לטיניים. הבעיה כבר תוקנה בראש
הסקריפט (`sys.stdout.reconfigure(encoding="utf-8", ...)`); אם היא חוזרת,
שם כדאי לחפש.

## 4. תרגום {: #4-translate }

```bash
python scripts/translate.py --only <code> --dry-run   # confirm scope/cost first
python scripts/translate.py --only <code> --yes
```

לוקאלים בלתי תלויים יכולים לרוץ **במקביל** (תהליכי רקע נפרדים) — הם רק
קוראים קבצים משותפים (`docs/en/`, `mkdocs.yml`) וכותבים לעצי
`docs/<code>/` נפרדים לחלוטין, כך שאין תנאי תחרות. ארבעה לוקאלים שתורגמו
במקביל הסתיימו בקירוב באותו זמן שעון-קיר כמו אחד.

בדקו ביומן את `Done: N translated, 0 failed` לפני שממשיכים.

## 5. בדקו אם קיימים צילומי מסך לפני ששוקלים את הסימולטור {: #5-check-for-existing-screenshots-before-considering-the-simulator }

**אל תניחו שצילומי מסך חדשים מחייבים הרצת צינור הסימולטור — בדקו
קודם.** המאגר הקודם
([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), בדרך כלל
משוכפל כתיקייה מקבילה) עשוי להכיל כבר ערכת צילומי מסך פר-שפה שצולמה
בידי הצוות של FrSky ויושבת ללא שימוש. כך היה עבור גרמנית, צרפתית (דרך
התיקייה `french_LT/` — לא זו הקטנה והחלקית `french/`), איטלקית וספרדית;
לא היה שם דבר עבור פורטוגזית או סינית. בדקו חפיפת שמות קבצים מול מה
שהמאגר הנוכחי מפנה אליו:

```python
from pathlib import Path
old_repo_lang_assets = Path("../ethos-manual/<language-folder>/assets")  # sibling checkout
current = {p.name for p in Path("docs/en/assets").iterdir() if p.suffix.lower() == ".png"}
old = {p.name for p in old_repo_lang_assets.glob("*.png")}
print(f"{len(old & current)} / {len(current)} would match")
```

שיעור התאמה גבוה (≥90%, בפועל) אומר שמדובר בהעתקה ישירה אל
`docs/<code>/assets/` — `fallback_to_default` ב-`mkdocs.yml` מבטיח שזה
*כל* מה שנדרש; אין שינויים ב-markdown. **בדקו ויזואלית לפחות תמונה אחת
שהועתקה** לפני שסומכים על ההתאמה (פתחו אותה, ודאו שזה באמת ממשק המשתמש
בשפת היעד, ולא צילום מיושן או לא מתאים) — התאמת שמות קבצים אינה מבטיחה
בהכרח התאמת תוכן, גם אם עד כה זה תמיד היה כך.

אם אין התאמה (פורטוגזית, סינית, או כל שפה עתידית שהמאגר הוותיק מעולם לא
כיסה), הלוקאל נופל אוטומטית ובאופן נכון לצילומי המסך באנגלית. זהו המצב
הצפוי והתקין — סגירת הפער באמת פירושה העברה/הרצה של צינור המאקרו האמיתי
מול הסימולטור (ראו [Screenshot Pipeline](screenshot-pipeline.md)), דבר
שנמצא מחוץ להיקף של מעבר תרגום טקסטואלי ומצריך התקנה מקומית של
הסימולטור.

## 6. בדיקה ותיקון של קישורי עוגן {: #6-check-and-fix-anchor-links }

תרגום כותרת משנה את ה-slug שנוצר לה אוטומטית, מה ששובר בשקט כל קישור
`#that-heading-slug` מעמוד אחר — ו**זו אינה שגיאת בנייה**:
`mkdocs build --strict` אינו נכשל על כך, כך שדבר לא יודיע לכם שזה קרה
מלבד קישור מת שקורא לוחץ עליו.

```bash
python scripts/check_anchors.py         # report only
python scripts/check_anchors.py --fix   # pin every finding, in en + every locale that has the page
```

זו מחלקת תקלות אמיתית וחוזרת, לא ניקוי חד-פעמי — כל לוקאל שנוסף עד כה
חשף כמה מקרים חדשים (אלה שבמקרה חפפו ל-slug מתורגם ספציפי ל-`<locale>`
שהתפצל מהאנגלית, בעוד שתרגום של לוקאל *אחר* לא עשה זאת). הריצו זאת אחרי
כל אצווה של תרגומים חדשים/מעודכנים. הסקריפט בונה מחדש את האתר בעצמו
כברירת מחדל (קודם `mkdocs build --strict`), כך שהתוצאות מעולם אינן
מיושנות.

## 7. אימות אמיתי {: #7-verify-for-real }

```bash
mkdocs build --strict; echo "exit code: $?"   # must be 0, not just free of "error"/"warn" text
python scripts/check_anchors.py                # must report 0
```

## 8. הוספת `nav_translations` — פעם אחת, לאחר שכיסוי העמודים הושלם {: #8-add-nav_translations-once-after-page-coverage-is-complete }

תוויות לשוניות וסרגל צד ב-`nav:` אינן מאמצות אוטומטית את כותרת העמוד
המתורגמת של לוקאל, אלא אם לרשומת הניווט אין תווית מפורשת כלל. הוסיפו
`nav_translations` תחת רשומת הלוקאל ב-`mkdocs.yml` פעם אחת, לאחר (ולא
לפני) שללוקאל יש כיסוי עמודים מלא — או כמעט מלא; תרגום מסגרת הממשק לפני
התוכן שאליו היא מפנה נקרא באופן מוזר. תוויות עלה יש להעתיק מילה במילה
מה-H1 של כל עמוד מתורגם (כדי שטקסט סרגל הצד יתאים בדיוק לכותרת העמוד);
תוויות לשוניות מקטעים (בית, תחילת העבודה, ...) צריכות להתאים למילון
משלב 3. חלצו כל H1 באופן פרוגרמטי במקום להקליד תוויות מחדש ידנית — זה
מהיר יותר ומבטל כל אפשרות לאי-התאמה בהעתקה:

```python
import re
h1 = re.search(r"^#\s+(.+)$", Path(f"docs/{code}/{rel_path}").read_text(encoding="utf-8"), re.MULTILINE).group(1).strip()
```

דלגו על `Translation Status` — זהו עמוד מתוחזק שנוצר אוטומטית, באנגלית
בלבד, ואין לו מקבילה מתורגמת בשום לוקאל.

## 9. שילוח {: #9-ship-it }

בצעו commit, push ל-`main`, ועקבו אחר ריצת ה-Action `Deploy Docs`.
ה-CDN של GitHub Pages עלול להחזיר 404 עבור נתיב לוקאל חדש לגמרי במשך
15–30+ השניות הראשונות אחרי פריסה שהצליחה באמת — זו השהיית התפשטות של
מטמון הקצה, לא כשל. אמתו דרך ה-API של GitHub שהקובץ קיים ב-`gh-pages`
לפני שאתם דואגים:

```bash
gh api "repos/<owner>/<repo>/contents/<version>/<code>/<path>?ref=gh-pages" --jq '.sha, .size'
```

ואז נסו שוב את ה-URL החי עם השהייה קצרה.
