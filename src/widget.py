import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string_info: str) -> str:
    """The function returns a card number mask or an account number mask"""
    result = ""
    string_name = ""
    string_number = ""
    if re.search("[а-яА-Я]", string_info[0]):
        for symbol in string_info:
            if symbol.isalpha() or symbol == " ":
                string_name += symbol
            if symbol.isdigit():
                string_number = string_info[string_info.index(symbol):]
                get_mask_account(string_number)
                result = string_name + get_mask_account(string_number)
                break
    if re.search("[a-zA-Z]", string_info[0]):
        for symbol in string_info:
            if symbol.isalpha() or symbol == " ":
                string_name += symbol
            if symbol.isdigit():
                string_number = string_info[string_info.index(symbol):]
                get_mask_card_number(string_number)
                result = string_name + get_mask_card_number(string_number)
                break
    return result


if __name__ == "__main__":
    print(mask_account_card(string_info="MasterCard 7158300734726758"))


def get_date(date_string_info: str) -> str:
    """The function returns a string with the date in the required format"""
    result = ""
    match = re.search(r"(\d{2,4})-(\d{2})-(\d{2,4})", date_string_info)
    if match:
        year, month, day = match.groups()
        if len(str(year)) == 4:
            result = f"{day}.{month}.{year}"
        else:
            result = f"{year}.{month}.{day}"
    else:
        result = "Корректная дата отсутствует"
    return result


if __name__ == "__main__":
    print(get_date(date_string_info="2024-03-11T02:26:18.671407"))
