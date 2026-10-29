"""
Урок 2.1 · Задача 1 — Анкета

Створи змінні з даними про себе:
- name — ім’я (рядок)
- age — вік (ціле число)
- height — зріст у метрах (дробове число, наприклад 1.78)
- is_student — чи навчаєшся зараз (True або False)
Потім виведи кожну змінну разом з її типом: print(name, type(name)) і т. д.

Як перевірити: запусти цей файл (кнопка ▶ у VS Code або `python m02_1_task1_anketa.py`
у терміналі, коли ти в папці practice\m02). Унизу побачиш ✓ або ✗.
"""

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓



# ↑↑↑ ТВІЙ КОД ВИЩЕ ↑↑↑

# ---------- автоперевірка, не змінюй ----------
from _check import expect, expect_type  # noqa: E402

expect_type(globals(), "name", str)
expect_type(globals(), "age", int, "вік без лапок: 30, а не \"30\"")
expect_type(globals(), "height", float, "дробове число пишеться з крапкою: 1.78")
expect_type(globals(), "is_student", bool, "True або False з великої літери, без лапок")
