import  re
from collections import Counter
import os
from utils import info_bank_operations

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")

list_operations = info_bank_operations(PATH_TO_FILE)


def process_bank_search(data:list[dict], search_word:str) -> list[dict]:
    """The function filters operations by the specified row"""
    searched_info = []
    for element in data:
        if element.get('description'):
            if re.search(search_word, element.get('description'), flags=re.IGNORECASE):
                searched_info.append(element)
    return searched_info

if __name__ == '__main__':
    print(process_bank_search(list_operations,  'Открытие вклада'))


def process_bank_operations(data: list[dict], categories: list = None) -> dict:
    """The function counts the number of operations in each category"""
    categories = categories or categories_default
    descriptions = (transaction.get("description") for transaction in data)
    return dict(Counter(desc for desc in descriptions if desc in categories))

categories_default = ["Перевод организации", "Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод с карты на счет"]

if __name__ == '__main__':
    print(process_bank_operations(list_operations, categories_default))

