import os
from utils import info_bank_operations
from reading_files import read_csv, read_excel
from process_bank import process_bank_search
from processing import sort_by_date, filter_by_state
from widget import get_date, mask_account_card

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")
PATH_TO_FILE_LOG = os.path.join(ROOT_DIR, "logs", "utils.log")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "transactions.csv")
PATH_TO_FILE_XLS = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")


def main() -> None:
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
    )

    data_format = input("Введите номер из списка:___ ")
    while data_format not in ["1", "2", "3"]:
        if data_format in ["1", "2", "3"]:
            break
        else:
            data_format = input("Введите номер из списка:___ ")

    if data_format == "1":
        print("Для обработки выбран JSON-файл")
        first_list = info_bank_operations(PATH_TO_FILE)
    elif data_format == "2":
        print("Для обработки выбран CSV-файл")
        first_list = read_csv(PATH_TO_FILE_CSV)
    elif data_format == "3":
        print("Для обработки выбран XLSX-файл")
        first_list = read_excel(PATH_TO_FILE_XLS)

    result_1 = first_list
    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING__"
    ).upper()

    while status not in status_list:
        if status in status_list:
            break
        else:
            print(f'Статус операции "{status}" недоступен.')
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию."
                "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING__"
            )
            .upper()
            .strip()
        )

    if status == "EXECUTED":
        print('Операции отфильтрованы по статусу "EXECUTED"')
        second_list = filter_by_state(result_1, status)
    elif status == "CANCELED":
        print('Операции отфильтрованы по статусу "CANCELED"')
        second_list = filter_by_state(result_1, status)
    elif status == "PENDING":
        print('Операции отфильтрованы по статусу "PENDING"')
        second_list = filter_by_state(result_1, status)
    result_2 = second_list

    sort_data = input("Отсортировать операции по дате? Да/Нет__").upper().strip()
    if sort_data == "ДА":
        sort_data_yes = input("Отсортировать по возрастанию или по убыванию?__").lower().strip()
        if sort_data_yes == "по убыванию":
            third_list = sort_by_date(result_2)
        else:
            third_list = sort_by_date(result_2, False)
    else:
        third_list = second_list
    result_3 = third_list

    sort_currency = input("Выводить только рублевые транзакции? Да/Нет__").upper().strip()
    if sort_currency == "ДА":
        if data_format == "1":
            fourth_list = [elem for elem in result_3 if elem["operationAmount"]["currency"]["code"] == "RUB"]
        else:
            fourth_list = [elem for elem in result_3 if elem.get("currency_code", 0) == "RUB"]
    else:
        fourth_list = result_3
    result_4 = fourth_list

    descr_data = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет___").upper().strip()
    if descr_data == "ДА":
        descriptions = set([elem.get("description", 0) for elem in result_4])
        for elem in descriptions:
            print(f"--{elem}")
        search_data = input("Введите слово или фразу:___")
        fifth_list = process_bank_search(result_4, search_data[:-1])
    else:
        fifth_list = result_4
    result_5 = fifth_list
    if len(result_5) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(result_5)}")
        if data_format == "1":
            for element in result_5:
                print(f'{get_date(element["date"])} {element.get("description", 0)}')
                if element.get("description", 0) == "Открытие вклада":
                    print(f'{mask_account_card(element["to"])}')
                else:
                    print(f'{mask_account_card(element["from"])} -> {mask_account_card(element["to"])}')
                print(
                    f'Сумма: {element["operationAmount"]["amount"]} {element["operationAmount"]["currency"]["name"]}'
                )
        else:
            for element in result_5:
                print(f'{get_date(element["date"])}  {element.get("description", 0)}')
                if element.get("description", 0) == "Открытие вклада":
                    print(f'{mask_account_card(element["to"])}')
                else:
                    print(f'{mask_account_card(element["from"])} -> {mask_account_card(element["to"])}')
                print(f'Сумма: {element.get("amount", 0)} {element.get("currency_name", 0)}')
    return True


if __name__ == "__main__":
    print(main())
