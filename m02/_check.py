"""Допоміжний файл для автоперевірки задач. НЕ змінюй його.

Задачі імпортують звідси функції expect / expect_type, які порівнюють
твої змінні з очікуваними значеннями і друкують ✓ або ✗.
"""
import atexit

_results = []
_MISSING = object()


def _show(value):
    return f"{value!r} (тип {type(value).__name__})"


def expect(scope, name, expected, hint=""):
    """Перевіряє, що змінна name існує і дорівнює expected (з тим самим типом)."""
    actual = scope.get(name, _MISSING)
    if actual is _MISSING:
        _results.append(False)
        print(f"✗ Змінну {name} не знайдено — створи її (перевір написання імені).")
        return
    if isinstance(expected, float) and isinstance(actual, (int, float)) and not isinstance(actual, bool):
        ok = abs(actual - expected) < 1e-9
    else:
        ok = type(actual) is type(expected) and actual == expected
    _results.append(ok)
    if ok:
        print(f"✓ {name} = {actual!r}")
    else:
        print(f"✗ {name}: очікувалось {_show(expected)}, а маєш {_show(actual)}")
        if hint:
            print(f"   Підказка: {hint}")


def expect_type(scope, name, expected_type, hint=""):
    """Перевіряє, що змінна name існує, має потрібний тип і не порожня."""
    actual = scope.get(name, _MISSING)
    if actual is _MISSING:
        _results.append(False)
        print(f"✗ Змінну {name} не знайдено — створи її.")
        return
    ok = type(actual) is expected_type and (actual != "" if expected_type is str else True)
    _results.append(ok)
    if ok:
        print(f"✓ {name} = {actual!r} (тип {expected_type.__name__})")
    else:
        print(f"✗ {name}: має бути тип {expected_type.__name__}, а маєш {_show(actual)}")
        if hint:
            print(f"   Підказка: {hint}")


@atexit.register
def _summary():
    if not _results:
        return
    print("-" * 40)
    if all(_results):
        print("✓ Усе правильно! Задачу розв’язано — можна відмітити її на сайті.")
    else:
        bad = _results.count(False)
        print(f"Не пройдено перевірок: {bad} з {len(_results)}. Виправ і запусти знову.")
