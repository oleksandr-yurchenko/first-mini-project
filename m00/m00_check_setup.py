"""
Етап 0 · Перевірка налаштування комп’ютера

Нічого писати не треба. Просто запусти цей файл (кнопка ▶ угорі праворуч),
і він перевірить, чи все встановлено: Python, pip, Git, ім’я та email у Git
і робочу папку C:/dev/python-course.

Біля кожного пункту з’явиться ✓ або ✗. Для ✗ є підказка, який урок повторити.
"""
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT = Path("C:/dev/python-course")  # якщо твоя робоча папка інша — зміни тут

results = []


def check(ok, good, bad, hint=""):
    results.append(ok)
    if ok:
        print("✓", good)
    else:
        print("✗", bad)
        if hint:
            print("   Підказка:", hint)


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
        return r.returncode, (r.stdout or r.stderr).strip()
    except (OSError, subprocess.SubprocessError):
        return 1, ""


v = sys.version_info
check(v >= (3, 12), f"Python {v.major}.{v.minor}.{v.micro}",
      f"Python {v.major}.{v.minor} — потрібен 3.12 або новіший", "урок 0.2")

code, out = run([sys.executable, "-m", "pip", "--version"])
check(code == 0, "pip працює: " + out.split(" from ")[0], "pip не знайдено", "урок 0.2, крок 4")

git = shutil.which("git")
code, out = run(["git", "--version"]) if git else (1, "")
check(code == 0, out or "git є", "Git не встановлено або не в PATH", "урок 0.5; після встановлення перезапусти VS Code")

if git:
    _, user = run(["git", "config", "--global", "user.name"])
    _, email = run(["git", "config", "--global", "user.email"])
    check(bool(user), f"Git знає твоє ім’я: {user}", "у Git не вказано ім’я",
          'git config --global user.name "Твоє Ім’я" (урок 0.5)')
    check(bool(email), f"Git знає твій email: {email}", "у Git не вказано email",
          'git config --global user.email "пошта@gmail.com" (урок 0.5)')

check(PROJECT.is_dir(), f"Робоча папка є: {PROJECT}", f"Немає папки {PROJECT}", "урок 0.3, крок 3")

if shutil.which("code"):
    print("✓ VS Code доступний з терміналу (команда code)")
else:
    print("· Команда code не знайдена — це не страшно, якщо VS Code відкривається з меню")

print("-" * 40)
if all(results):
    print("✓ Усе налаштовано! Етап 0 технічно пройдено.")
else:
    print(f"Не пройдено перевірок: {results.count(False)} з {len(results)}. Виправ і запусти знову.")
