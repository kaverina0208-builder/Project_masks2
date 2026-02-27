from functools import wraps
from typing import Any, Union, Callable


def log(filename: Any = None) -> Any:
    """The decorator can log the function's operation and its result to both a file and the console."""

    def wrapper(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                raise

        return inner

    return wrapper


@log()
def example(x: Union[int, float], y: Union[int, float]) -> Any:
    return x / y


example(10, 2)
