from time import time
from functools import wraps


def log(*, filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            time_1 = time()
            result = round(func(*args, **kwargs))
            time_2 = time()
            if filename is None:
                print(f'Функция: {func.__name__}\n'
                      f'Начала работы: {time_1}, Окончание работы: {time_2}\n'
                      f'Inputs: {args}, {kwargs}\nРезультат: {result}')
            else:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(f'Функция: {func.__name__}\n'
                               f'Начала работы: {time_1}, Окончание работы: {time_2}\n'
                               f'Inputs: {args}, {kwargs}\nРезультат: {result}')
        return inner
    return wrapper


@log(filename='log.txt')
def example(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"


example(10, 2)
