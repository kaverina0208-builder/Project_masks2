import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")


def info_bank_operations(path) -> list:
    """ The function returns a list with data about financial transactions"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                result = json.load(f)
                return result
            except json.JSONDecodeError:
                result = []
                return result
    except FileNotFoundError:
        result = []
        # return result
    return result


if __name__ == '__main__':
    print(info_bank_operations(PATH_TO_FILE))
