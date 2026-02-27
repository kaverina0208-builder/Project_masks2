import pytest
from src.decorators import log


@log()
def func_console(x, y):
    return x / y


@pytest.mark.parametrize("x, y, expected", [
    (3, 2, "func_console ok"),
    (1, 0, "func_console error: ZeroDivisionError. Inputs: (1, 0), {}")
])

def test_log_to_console(capsys, x, y, expected):
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            func_console(x, y)
    else:
        func_console(x, y)
    captured = capsys.readouterr()
    assert expected in captured.out


@log(filename="test_log.txt")
def func_file(x, y):
    return x / y


@pytest.mark.parametrize("x, y, expected", [
    (3, 2, "func_file ok"),
    (1, 0, "func_file error: ZeroDivisionError. Inputs: (1, 0), {}")
])
def test_log_to_file(x, y, expected):
    log_file = "test_log.txt"


    if y == 0:
        with pytest.raises(ZeroDivisionError):
            func_file(x, y)
    else:
        func_file(x, y)


    with open(log_file, 'r') as f:
        content = f.read()
        assert expected in content
