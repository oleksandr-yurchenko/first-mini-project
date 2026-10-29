"""
Урок 2.3 · Задача 3 — Зрізи

Отримай ЗРІЗАМИ з рядка s:
- first3 = "Pro"
- last4 = "ming"
- middle = "gram"
- reversed_s = "gnimmargorP"

Як перевірити: запусти цей файл (кнопка ▶ у VS Code або `python m02_3_task3_slices.py`
у терміналі, коли ти в папці practice\m02). Унизу побачиш ✓ або ✗.
"""

s = "Programming"

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓
first3 = s[0:3]
last4 = s[-4::]
middle = s[3:7]
reversed_s = s[::-1]


# ↑↑↑ ТВІЙ КОД ВИЩЕ ↑↑↑

# ---------- автоперевірка, не змінюй ----------
from _check import expect, expect_type  # noqa: E402

expect(globals(), "first3", "Pro", "зріз [start:stop] не включає stop")
expect(globals(), "last4", "ming", "від’ємні індекси рахуються з кінця")
expect(globals(), "middle", "gram", "'g' має індекс 3; кінець зрізу не включається")
expect(globals(), "reversed_s", "gnimmargorP", "крок -1 іде задом наперед")
