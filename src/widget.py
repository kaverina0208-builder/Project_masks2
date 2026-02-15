import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(srting_info: str) -> str:
    """The function returns a card number mask or an account number mask"""
    result = ""
    string_name = ""
    string_number = ""
    if re.search("[а-яА-Я]", srting_info[0]):
        for symbol in srting_info:
            if symbol.isalpha() or symbol == " ":
                string_name += symbol
            if symbol.isdigit():
                string_number += symbol
        result = string_name + get_mask_account(string_number)
    if re.search("[a-zA-Z]", srting_info[0]):
        for symbol in srting_info:
            if symbol.isalpha() or symbol == " ":
                string_name += symbol
            if symbol.isdigit():
                string_number += symbol
        result = string_name + get_mask_card_number(string_number)
    return result


print(mask_account_card(srting_info="MasterCard 7158300734726758"))


def get_date(date_string_info: str) -> str:
    """The function returns a string with the date in the required format"""
    result = ""
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_string_info)
    if match:
        year, month, day = match.groups()
    result = f"{day}.{month}.{year}"
    return result


print(get_date(date_string_info="2024-03-11T02:26:18.671407"))