import json
import os
import logging


ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")
PATH_TO_FILE_LOG = os.path.join(ROOT_DIR, "logs", "utils.log")

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_FILE_LOG, mode='w')
file_formater = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def info_bank_operations(path) -> list:
    """The function returns a list with data about financial transactions"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                result = json.load(f)
                logger.debug('Successful file reading')
                return result
            except json.JSONDecodeError:
                result = []
                logger.error('JSONDecodeError')
                return result
    except FileNotFoundError:
        result = []
        logger.error('FileNotFoundError')
    logger.info('Program shutdown')
    return result


if __name__ == "__main__":
    print(info_bank_operations(PATH_TO_FILE))
