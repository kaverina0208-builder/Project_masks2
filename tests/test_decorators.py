import pytest
from typing import Union, Any
from src.decorators import log


@log()
def func_console(x: Union[int, float], y: Union[int, float]) -> Any:
    return x / y


@pytest.mark.parametrize(
    "x, y, expected", [(3, 2, "func_console ok"), (1, 0, "func_console error: ZeroDivisionError. Inputs: (1, 0), {}")]
)
def test_log_to_console(capsys: Any, x: Union[int, float], y: Union[int, float], expected: Any) -> Any:
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            func_console(x, y)
    else:
        func_console(x, y)
    captured = capsys.readouterr()
    assert expected in captured.out


@log(filename="test_log.txt")
def func_file(x: Union[int, float], y: Union[int, float]) -> Any:
    return x / y


@pytest.mark.parametrize(
    "x, y, expected", [(3, 2, "func_file ok"), (1, 0, "func_file error: ZeroDivisionError. Inputs: (1, 0), {}")]
)
def test_log_to_file(x: Union[int, float], y: Union[int, float], expected: Any) -> Any:
    log_file = "test_log.txt"

    if y == 0:
        with pytest.raises(ZeroDivisionError):
            func_file(x, y)
    else:
        func_file(x, y)

    with open(log_file, "r") as f:
        content = f.read()
        assert expected in content
