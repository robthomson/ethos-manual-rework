---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lista kontrolna z tekstem użytkownika

![Tekst listy kontrolnej użytkownika](../assets/model-checklist-user-checklist.png)

Funkcja [Lista kontrolna](../model-setup/checklist.md) może wyświetlać
własny tekst przy starcie — zwykły tekst lub sformatowany w Markdown —
automatycznie, przy każdym załadowaniu danego modelu.

## 1. Utwórz tekst listy kontrolnej

**Zwykły tekst** — napisz go w dowolnym edytorze tekstu (Notepad++ lub
nawet MS Word z zapisem jako zwykły tekst) i zapisz jako `<model name>.txt`.

**Tekst rozszerzony (Markdown)** — Ethos obsługuje formatowanie Markdown,
np. `##` dla nagłówka, `**bold**` dla pogrubienia. Użyj dowolnego edytora
tekstu (wpisując składnię Markdown ręcznie) lub dedykowanego edytora
Markdown (Nextpad, MarkText itp.) i zapisz jako `<model name>.md`.

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. Skopiuj plik do nadajnika

Skopiuj plik do tego samego folderu `models/`, w którym znajduje się plik
`.bin` modelu (zobacz [Menedżer plików](../system-setup/file-manager.md#top-level-folders)),
a następnie bezpiecznie odłącz dyski nadajnika przed rozłączeniem kabla.

## 3. Sprawdź efekt

Załaduj model — tekst listy kontrolnej pojawi się teraz automatycznie jako
część kontroli startowych, z możliwością przewijania, jeśli jest dłuższy
niż jeden ekran.
