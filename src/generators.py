from typing import Any, Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(lst1: list, name: str = "USD") -> Any:
    """The function returns transactions where the currency of the operation matches the specified currency."""
    new_lst = list(filter(lambda x: x.get("operationAmount", {}).get("currency", {}).get("name", 0) == name, lst1))
    if len(new_lst) == 0:
        yield "Нет операций в такой валюте"
    else:
        for x in new_lst:
            yield x


usd_transactions = filter_by_currency(transactions, "EUR")
if len(transactions) == 0:
    print("Список пуст")
for _ in range(len(transactions)):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Список исчерпан")
        break




def transaction_descriptions(lst1: list) -> Generator:
    """The function returns a description of each operation in turn"""
    for element in lst1:
        result = element.get("description")
        yield result


descriptions = transaction_descriptions(transactions)
if len(transactions) == 0:
    print("Список пуст")
for _ in range(len(transactions)):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Список исчерпан")
        break




def card_number_generator(start: int, stop: int) -> Generator:
    """The function generates card numbers in the specified range"""
    if start < 0 or stop < 0:
        yield "Введены некорректные данные"
    else:
        while start <= stop:
            length_result = 16 - len(str(start))
            length_result_string = "0" * length_result + str(start)
            yield (
                f"{length_result_string[0:4]} "
                f"{length_result_string[4:8]} "
                f"{length_result_string[8:12]} "
                f"{length_result_string[12:]}"
            )
            start += 1

if __name__ == '__main__':
    for card_number in card_number_generator(9999999999999999, 9999999999999999):
        print(card_number)
