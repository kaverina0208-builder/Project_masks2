import pytest
from src.generators import card_number_generator


def test_filter_by_currency():
    pass






# @pytest.mark.parametrize("start, stop, expected", [(1, 3, '0000 0000 0000 0001'),
#                                                    (1, 3, '0000 0000 0000 0002'),
#                                                    (1, 3, '0000 0000 0000 0003')])



def test_card_number_generator():
    generator = card_number_generator(start=1, stop=2)
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'
    # assert next(generator) == expected


