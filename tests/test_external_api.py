import pytest
from unittest.mock import patch, Mock
from src.external_api import conversion_amount
from typing import Any


tran_data = {
  "id": 41428829,
  "state": "EXECUTED",
  "date": "2019-07-03T18:35:29.512364",
  "operationAmount": {
    "amount": "100",
    "currency": {
      "name": "USD",
      "code": "USD"
    }
  },
  "description": "Перевод организации",
  "from": "MasterCard 7158300734726758",
  "to": "Счет 35383033474447895560"
}


def test_conversion_amount_failed_request() -> Any:
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
            conversion_amount(tran_data)


def test_conversion_amount_success() -> Any:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 10}

    with patch("requests.get", return_value=mock_response):
        result = conversion_amount(tran_data)
        assert result == 10
