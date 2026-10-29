"""
Урок 2.2 · Задача 1 — Годинник

У змінній seconds — кількість секунд. Порахуй, скільки це годин, хвилин і секунд,
і поклади в змінні hours, minutes, secs.
Використай // (ціла частина) і % (остача). Спробуй потім інші значення seconds.

Як перевірити: запусти цей файл (кнопка ▶ у VS Code або `python m02_2_task1_clock.py`
у терміналі, коли ти в папці practice\m02). Унизу побачиш ✓ або ✗.
"""

seconds = 7384

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓



# ↑↑↑ ТВІЙ КОД ВИЩЕ ↑↑↑

# ---------- автоперевірка, не змінюй ----------
from _check import expect, expect_type  # noqa: E402

expect(globals(), "hours", 2, "seconds // 3600")
expect(globals(), "minutes", 3, "спершу rest = seconds % 3600, потім rest // 60")
expect(globals(), "secs", 4, "rest % 60")
