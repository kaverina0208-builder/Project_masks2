import csv
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "transactions.csv")
PATH_TO_FILE_XLS = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")

def read_csv(path:str) -> list[dict]:
    """The function reads the csv-file"""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                reader = csv.DictReader(file, delimiter=';')
                result = []
                for row in reader:
                    result.append(row)
            except pd.errors.ParserError as e:
                raise ValueError(f"Ошибка при чтении файла {path}")
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл {path} не найден')
    return result


if __name__ == '__main__':
    print(read_csv(PATH_TO_FILE_CSV))


def read_excel(path: str) -> list[dict]:
    """The function reads the excel-file"""
    try:
        df_exl = pd.read_excel(path)
        transactions_exl_list = df_exl.to_dict(orient="records")
        result = transactions_exl_list
    except ValueError:
        raise ValueError(f'Ошибка при чтении файла {path}')
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл {path} не найден')
    return result


if __name__ == '__main__':
    print(read_excel(PATH_TO_FILE_XLS))