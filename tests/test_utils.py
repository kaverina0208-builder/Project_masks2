import unittest
import os
from unittest.mock import mock_open, patch
from src.utils import info_bank_operations

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

PATH_TO_FILE = os.path.join(ROOT_DIR, "data", "operations.json")


class TestInfoBankOperations(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
    def test_valid_json(self, mock_file):
        result = info_bank_operations(PATH_TO_FILE)
        self.assertEqual(result, [{"id": 1}])

    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    def test_invalid_json(self, mock_file):
        result = info_bank_operations(PATH_TO_FILE)
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        result = info_bank_operations(PATH_TO_FILE)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
