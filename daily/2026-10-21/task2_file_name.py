"""
Щоденна задача · 2026-10-21 · Задача 2 — Ім’я файлу
Тренує: find, зрізи, startswith, count, in (урок 2.3)

У змінній filename — назва файлу.
1) dot — індекс крапки в назві (знайди методом, не рахуй пальцем).
2) name — усе, що стоїть ДО крапки (зріз з використанням dot).
3) is_report — чи починається назва зі слова report (True/False).
4) underscores — скільки в назві символів _ .
5) has_year — чи є в назві "2026" (True/False).

Приклад: для "photo_2025.png" було б dot = 10, name = "photo_2025",
is_report = False, underscores = 1, has_year = False.
"""

filename = "report_october_2026.txt"

# ↓↓↓ ТВІЙ КОД НИЖЧЕ ↓↓↓



# ↑↑↑ ТВІЙ КОД ВИЩЕ ↑↑↑

# ---------- автоперевірка, не змінюй ----------
import sys, pathlib  # noqa: E401,E402
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from _check import expect, expect_type  # noqa: E402

expect(globals(), "dot", 19, "Таблиця методів у кроці 4 уроку 2.3: який метод повертає індекс?")
expect(globals(), "name", "report_october_2026", "Зріз s[:stop] не включає stop — це якраз те, що треба.")
expect(globals(), "is_report", True, "Метод, назва якого перекладається «починається з».")
expect(globals(), "underscores", 2, "Метод, який рахує, скільки разів зустрічається символ.")
expect(globals(), "has_year", True, "Тут не метод, а слово in.")
