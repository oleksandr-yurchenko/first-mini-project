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
    _printed_lines()  # зупинити запам’ятовування виводу перед перевірками
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
    _printed_lines()  # зупинити запам’ятовування виводу перед перевірками
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


# ---------- перевірка того, що програма надрукувала ----------
import io as _io
import sys as _sys


class _Tee:
    def __init__(self, real):
        self.real = real
        self.buf = _io.StringIO()

    def write(self, s):
        self.buf.write(s)
        return self.real.write(s)

    def flush(self):
        self.real.flush()

    def __getattr__(self, name):
        return getattr(self.real, name)


_tee = None


def start_capture():
    """Починає запам’ятовувати все, що друкує програма (виклик угорі файлу)."""
    global _tee
    if _tee is None:
        _tee = _Tee(_sys.stdout)
        _sys.stdout = _tee


def _stop_capture():
    global _tee
    out = ""
    if _tee is not None:
        out = _tee.buf.getvalue()
        _sys.stdout = _tee.real
        _tee = None
    return out


_printed_cache = None


def _printed_lines():
    global _printed_cache
    if _printed_cache is None:
        _printed_cache = [line.rstrip() for line in _stop_capture().splitlines()]
    return _printed_cache


def expect_printed(expected_lines, hint=""):
    """Перевіряє, що програма надрукувала рівно ці рядки (пробіли в кінці не важливі)."""
    got = _printed_lines()
    exp = [line.rstrip() for line in expected_lines]
    ok = got == exp
    _results.append(ok)
    if ok:
        print(f"✓ Надруковано правильно ({len(exp)} рядк.)")
        return
    print("✗ Надруковано не те, що треба.")
    for i in range(max(len(got), len(exp))):
        g = got[i] if i < len(got) else "(нічого)"
        e = exp[i] if i < len(exp) else "(нічого)"
        if g != e:
            print(f"   Рядок {i + 1}: очікувалось {e!r}")
            print(f"            а маєш     {g!r}")
            break
    if hint:
        print(f"   Підказка: {hint}")


def expect_printed_has(text, hint=""):
    """Перевіряє, що серед надрукованого є рядок, який містить text."""
    got = _printed_lines()
    ok = any(text in line for line in got)
    _results.append(ok)
    if ok:
        print(f"✓ У виводі є {text!r}")
    else:
        print(f"✗ У виводі немає {text!r}")
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
