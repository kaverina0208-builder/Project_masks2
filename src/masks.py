def get_mask_card_number(card_number: str) -> str:
    """The function returns the mask of the card number"""
    result = ""
    if len(card_number) != 16 or len(card_number) == "" or card_number.isdigit() is False:
        result = "Введен некорректный номер карты"
    else:
        result = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    return result


# print(get_mask_card_number(card_number="1234567891231234"))


def get_mask_account(account_number: str) -> str:
    """The function returns the mask of the account number"""
    result = ""
    if len(account_number) != 20 or account_number.isdigit() is False:
        result = "Введен некорректный номер счета"
    else:
        result = f"**{account_number[-4:]}"
    return result


# print(get_mask_account(account_number="12345678912345678912"))
