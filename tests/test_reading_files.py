import unittest
import os
from unittest.mock import mock_open, patch
from src.reading_files import read_csv, read_excel
import pandas as pd
from unittest import TestCase

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "data", "transactions.csv")
PATH_TO_FILE_XLS = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")


class TestInfoBankOperationsCsv(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "1;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n",
    )
    def test_valid_read_csv(self, mock_file):
        result = read_csv(PATH_TO_FILE_CSV)
        expected_result = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        self.assertEqual(result, expected_result)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found_csv(self, mock_file):
        result = read_csv(PATH_TO_FILE_CSV)
        expected_result = "Файл не найден"
        self.assertEqual(result, expected_result)


class TestInfoBankOperationsXls(TestCase):
    @patch("pandas.read_excel")
    def test_valid_read_excel(self, mock_read_excel):
        mock_df = pd.DataFrame(
            [
                {
                    "id": "1",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": "16210",
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                }
            ]
        )

        mock_read_excel.return_value = mock_df

        result = read_excel(PATH_TO_FILE_XLS)
        expected_result = [
            {
                "id": "1",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        self.assertEqual(result, expected_result)
