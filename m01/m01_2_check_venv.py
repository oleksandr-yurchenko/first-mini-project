"""
Урок 1.2 · Перевірка віртуального середовища

Нічого писати не треба. Запусти файл (кнопка ▶), і він перевірить твій проєкт
C:/dev/python-course:
- чи створено середовище .venv;
- чи встановлено в нього бібліотеку rich;
- чи є файл colors.py, який її використовує;
- чи є requirements.txt зі списком бібліотек.
"""
import subprocess
import sys
from pathlib import Path

PROJECT = Path("C:/dev/python-course")  # якщо твій проєкт в іншій папці — зміни тут

results = []


def check(ok, good, bad, hint=""):
    results.append(ok)
    if ok:
        print("✓", good)
    else:
        print("✗", bad)
        if hint:
            print("   Підказка:", hint)


venv = PROJECT / ".venv"
win_py = venv / "Scripts" / "python.exe"
nix_py = venv / "bin" / "python"
venv_py = win_py if win_py.exists() else nix_py

check(PROJECT.is_dir(), f"Папка проєкту є: {PROJECT}", f"Немає папки {PROJECT}", "етап 0, урок 3")
check(venv_py.exists(), "Середовище .venv створено", "Середовища .venv немає",
      "у терміналі в папці проєкту: python -m venv .venv (крок 2)")

rich_ok = False
if venv_py.exists():
    r = subprocess.run([str(venv_py), "-c", "import rich"], capture_output=True)
    rich_ok = r.returncode == 0
check(rich_ok, "rich встановлено в .venv", "rich не встановлено в .venv",
      "увімкни середовище (має бути (.venv) на початку рядка), потім pip install rich")

colors = PROJECT / "colors.py"
text = colors.read_text(encoding="utf-8", errors="replace") if colors.exists() else ""
check("from rich import print" in text, "colors.py є і підключає rich",
      "Немає colors.py з рядком from rich import print", "крок 5")

req = PROJECT / "requirements.txt"
req_text = req.read_text(encoding="utf-8", errors="replace").lower() if req.exists() else ""
check("rich" in req_text, "requirements.txt є і містить rich",
      "Немає requirements.txt з rich", "pip freeze > requirements.txt (крок 6), з увімкненим (.venv)")

if sys.prefix != sys.base_prefix:
    print("· Цей файл зараз запущено через віртуальне середовище")
else:
    print("· Цей файл запущено системним Python — для перевірки це нормально")

print("-" * 40)
if all(results):
    print("✓ Середовище налаштовано правильно!")
else:
    print(f"Не пройдено перевірок: {results.count(False)} з {len(results)}. Виправ і запусти знову.")
