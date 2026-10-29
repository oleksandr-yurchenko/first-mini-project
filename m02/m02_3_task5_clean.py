"""
Урок 2.3 · Задача 5 — Прибрати безлад

Користувач ввів ім’я з зайвими пробілами й дивним регістром.
Зроби з нього охайне "Ivan Petrenko" і поклади в clean.
Підказка: strip() → split() → title() → " ".join(...)

Як перевірити: запусти цей файл (кнопка ▶ у VS Code або `python m02_3_task5_clean.py`
у терміналі, коли ти в папці practice\m02). Унизу побачиш ✓ або ✗.
"""

raw = "   iVaN    peTRenko  "

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓

clean = raw.strip()
clean = clean.title()
clean = clean.split()


clean = " ".join(clean)

# ↑↑↑ ТВІЙ КОД ВИЩЕ ↑↑↑

# ---------- автоперевірка, не змінюй ----------
from _check import expect, expect_type  # noqa: E402

expect(globals(), "clean", "Ivan Petrenko", "split() без аргументів сам прибирає зайві пробіли")
