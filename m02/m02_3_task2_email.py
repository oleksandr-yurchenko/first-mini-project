"""
Урок 2.3 · Задача 2 — Логін і домен

Розбий email на логін (до @) і домен (після @): змінні login і domain.

Як перевірити: запусти цей файл (кнопка ▶ у VS Code або `python m02_3_task2_email.py`
у терміналі, коли ти в папці practice\m02). Унизу побачиш ✓ або ✗.
"""

email = "ivan.petrenko@gmail.com"

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓
parts = email.split("@")
login = parts[0]
domain = parts[1]
print("login:", login)
print("domain:", domain)

# ↑↑↑ ТВІЙ КОД ВИЩЕ ↑↑↑

# ---------- автоперевірка, не змінюй ----------
from _check import expect, expect_type  # noqa: E402

expect(globals(), "login", "ivan.petrenko", "split(\"@\") повертає список з двох частин — його можна розпакувати в дві змінні")
expect(globals(), "domain", "gmail.com")
