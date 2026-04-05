import logging
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "logs", "masks.log")

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(PATH_TO_FILE, mode='w')
file_formater = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """The function returns the mask of the card number"""
    logger.info('Getting data from the user')
    result = ""
    if len(card_number) != 16 or len(card_number) == "" or card_number.isdigit() is False:
        result = "Введен некорректный номер карты"
        logger.error('Incorrect card number entered')
    else:
        result = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
        logger.info('The card number has been generated')
    logger.info('Program shutdown')
    return result


if __name__ == '__main__':
    print(get_mask_card_number('1234564562589654'))


def get_mask_account(account_number: str) -> str:
    """The function returns the mask of the account number"""
    logger.info('Getting data from the user')
    result = ""
    if len(account_number) != 20 or account_number.isdigit() is False:
        result = "Введен некорректный номер счета"
        logger.error('Incorrect account number entered')
    else:
        result = f"**{account_number[-4:]}"
        logger.info('The account number has been generated')
    logger.info('Program shutdown')
    return result


if __name__ == '__main__':
    print(get_mask_account('1234564562589654'))
