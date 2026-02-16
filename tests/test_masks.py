import pytest
from typing import Any
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, expected",
    [
        ("1234567891231234", "1234 56** **** 1234"),
        ("258962", "Введен некорректный номер карты"),
        ("", "Введен некорректный номер карты"),
        ("asdfghjkloiuy900", "Введен некорректный номер карты"),
    ],
)
def test_get_mask_card_number(number: str, expected: str) -> Any:
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("12345678912345678912", "**8912"),
        ("258962", "Введен некорректный номер счета"),
        ("", "Введен некорректный номер счета"),
        ("asdfghjkloiuy900", "Введен некорректный номер счета"),
    ],
)
def test_get_mask_account(number: str, expected: str) -> Any:
    assert get_mask_account(number) == expected
