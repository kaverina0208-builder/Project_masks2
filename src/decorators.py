from time import time
from functools import wraps


def log(*, filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if filename is None:
                    print(f'{func.__name__} ok')
                else:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ok')
                return result
            except Exception as e:
                if filename is None:
                    print((f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n'))
                else:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n')
                raise
        return inner
    return wrapper

#
# @log(filename='mylog.txt')
# def example(x, y):
#     return x / y
#
#
# example(10, 0)
#
