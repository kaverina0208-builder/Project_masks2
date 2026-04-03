import pytest
from unittest.mock import patch, Mock
from src.external_api import conversion_amount
from typing import Any


def test_conversion_amount_failed_request() -> Any:
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
            conversion_amount("USD")


def test_conversion_amount_success() -> Any:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 10}

    with patch("requests.get", return_value=mock_response):
        result = conversion_amount("USD")
        assert result == 10
