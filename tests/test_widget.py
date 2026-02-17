import pytest
from typing import Any
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maзщьлдб 1596838687895199", "Maзщьлдб 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 70007922lll06361", "Visa Platinum Введен некорректный номер карты"),
    ],
)
def test_mask_account_card(number: str, expected: str) -> Any:
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "string_info, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("11-02-2025T02:26:18.671407", "11.02.2025"),
        ("2024-03T02:26:18.671407", "Корректная дата отсутствует"),
    ],
)
def test_get_date(string_info: str, expected: str) -> Any:
    assert get_date(string_info) == expected
