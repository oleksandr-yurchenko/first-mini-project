"""
Урок 1.3 · Перевірка Git і GitHub

Нічого писати не треба. Запусти файл (кнопка ▶), і він перевірить проєкт
C:/dev/python-course:
- чи це Git-репозиторій (було git init);
- чи є .gitignore, у якому є .venv/;
- скільки зроблено комітів (треба щонайменше 2);
- чи підключено GitHub (git remote) і чи .venv не потрапило в Git;
- чи все закомічено.
"""
import shutil
import subprocess
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


def git(*args):
    r = subprocess.run(["git", "-C", str(PROJECT), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.returncode, r.stdout.strip()


if not shutil.which("git"):
    check(False, "", "Git не знайдено", "етап 0, урок 5")
else:
    is_repo = (PROJECT / ".git").is_dir()
    check(is_repo, "Проєкт — це Git-репозиторій", f"У {PROJECT} не було git init", "крок 3")

    gi = PROJECT / ".gitignore"
    gi_text = gi.read_text(encoding="utf-8", errors="replace") if gi.exists() else ""
    check(".venv" in gi_text, ".gitignore є і містить .venv/",
          "Немає .gitignore з рядком .venv/", "назва рівно .gitignore, без .txt, поруч з .venv (крок 2)")

    if is_repo:
        code, count = git("rev-list", "--count", "HEAD")
        n = int(count) if code == 0 and count.isdigit() else 0
        check(n >= 2, f"Комітів: {n}", f"Комітів: {n} — треба щонайменше 2",
              "git add . → git commit -m \"...\" (кроки 3 і 7)")

        code, url = git("remote", "get-url", "origin")
        check(code == 0 and "github.com" in url, f"GitHub підключено: {url}",
              "GitHub не підключено (немає origin)", "крок 6: git remote add origin ...")

        _, tracked_venv = git("ls-files", ".venv")
        check(tracked_venv == "", ".venv не потрапило в Git", ".venv є в Git — так не можна",
              "перевір .gitignore, потім: git rm -r --cached .venv і новий коміт")

        _, status = git("status", "--porcelain")
        check(status == "", "Усе закомічено (working tree clean)", "Є незакомічені зміни",
              "git add . → git commit -m \"...\" → git push")

print("-" * 40)
if all(results):
    print("✓ Git і GitHub налаштовано правильно!")
else:
    print(f"Не пройдено перевірок: {results.count(False)} з {len(results)}. Виправ і запусти знову.")
